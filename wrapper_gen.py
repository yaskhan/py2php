import xml.etree.ElementTree as etree
import os.path as pt
import os, re, getopt, sys


def create_folders(path, namespace):
    if namespace[:1] == "\\":
        namespace = namespace[1:]
    fpath = os.path.join(path, namespace)
    if not os.path.exists(fpath):
        os.makedirs(fpath)
    
def get_bool(txt):
    if txt == "true": return True
    else: return False
    
def none_to_string(txt):
    if txt == None: return ""
    else: return txt
    
def replace_nl(txt, spaces = 4):
    return txt.replace("\n", "\n" + (spaces * " "))

def long_and_short_description(long_description, description, spaces = 4):
    space = ' ' * spaces
    output = ''
    if description or long_description:
        output += space + '"""\n'
        output += space + replace_nl(none_to_string(description), spaces) + "\n"
        output += space + replace_nl(none_to_string(long_description), spaces) + '\n' + space + '"""\n'
        return output
    else: return ''

def to_lower(txt):
    if not txt: return 
    spl = txt.split("\\")
    if len(spl) == 1:
        return txt
    qwe = []
    for d in spl[:-1]:
        qwe.append(d.lower())
    qwe.append(spl[-1:][0])
    return ".".join(qwe)
	
def get_type(php_type):
    if not php_type: return 'None'
    reg = re.match("array\\((.*?)\\)", php_type)
    arr = []
    if php_type == "string": return '""'
    elif php_type == "integer": return '0'
    elif php_type == "float": return '0.0'
    elif php_type == "array()" or php_type == "array" or reg:
        if reg:
            if re.match(".*?=>", reg.group(1)):
                for t in reg.group(1).split(","):
                    (r,e) = t.split("=>")
                    arr.append(' : '.join((get_type(r.strip()),get_type(e.strip()))))
                return "{%s}" % ", ".join(arr)
            else:
                return "[" + reg.group(1) + "]"
        return '[]'
    elif php_type == "true": return 'True'
    elif php_type == "false": return 'False'
    elif php_type == "null": return 'None'
    elif php_type == "": return 'None'
    else:  return php_type
	
	
def method_gen(name, node, description, long_description, method = True):
    output = ''
    if method:
        spaces = 8
        space = ' ' * 4
        args = ["self"]
    else:
        spaces = 4
        space = ''
        args = []
        
    output += space + "def " 
    if name == "__construct":
        output += "__init__"
    else:
        output += name
    output += "("
    
    tmp = ""
    for arg in node.findall("argument"):
        tmp += arg.find("name").text[1:]
        default = arg.find("default").text
        if default:
            tmp += " = " + get_type(default)
        args.append(tmp)
        tmp = ""
    output += ", ".join(args) +  "):\n"
        
    output += long_and_short_description(long_description, description, spaces)     
    #for tag in node.findall("docblock//tag"):
    output += ' '*spaces + "pass\n\n"
    return output
                
            
def gen_class(elem, class_ = "class"):
    output = ''
    for clazz in elem.findall(class_):
        if class_ == "class" and clazz.attrib["final"] == "true":
            output += "@final\n"
        if class_ == "class" and clazz.attrib["abstract"] == "true":
            output += "@abstract\n"
        if class_ == "interface":
            output += "@interface\n"
        
        output += "class " + clazz.find("name").text
        ext_list = []
        ext = clazz.find("extends")
        if ext: ext = ext.text
        else: ext = ""
        for impl in clazz.findall("implements"):
            ext_list.append(impl.text)
        ext_list.append(ext)
        output += "("
        output += ", ".join([to_lower(n) for n in filter(None, ext_list)])
        output +=  "):\n"
            
        description = clazz.find("docblock//description").text
        long_description = clazz.find("docblock//long-description").text
        
        class_property = clazz.findall("property")
        class_methods = clazz.findall("method")
        
        output += long_and_short_description(long_description, description)
            
        if len(class_property) == 0 and len(class_methods) == 0:
            output += '    pass\n\n'
        else:
            for property_ in class_property:
                output += "    " + property_.find("name").text[1:]
                default = property_.find("default").text
                type_ = property_.find("docblock//tag//type")
                if type_: type_ = type_.text
                
                if default:
                    output += " = " + get_type(default) + "\n"
                else:
                    output += " = " + get_type(type_) + "\n"
                    
            
            for method in class_methods:
                name = method.find("name").text
                abstract = get_bool(method.attrib["abstract"])
                final = get_bool(method.attrib["final"])
                #visibility = method.attrib["visibility"]
                static = get_bool(method.attrib["static"])
                description = method.find("docblock//description").text
                long_description = method.find("docblock//long-description").text
                
                if abstract: output += "    @abstractmethod\n"
                if final: output += "    @finalmethod\n"
                if static: output += "    @staticmethod\n"
                output += method_gen(name, method, description, long_description)

    return output + "\n"
            
def xml_to_py(xml_file_to_parse, folder = "."):
    '''
    returns file name, namespace, generated python code
    '''

    tree = etree.parse(xml_file_to_parse)
    project = tree.getroot()

    for file in project.findall("file"):
        output = "from wrapper.builtins import .*\n\n"
        
        for namespace in file.findall("namespace-alias"):
            namespace = namespace.text.lower()
            create_folders(folder, namespace)
            output += "import " + namespace.replace('\\','.')[1:] + "\n"
        output += "\n"
        
        output += gen_class(file)
        output += gen_class(file, "interface")
     
        for function in file.findall("function"):
            name = function.find("name").text
            description = function.find("docblock//description").text
            long_description = function.find("docblock//long-description").text
            output += method_gen(name, function, description, long_description, False)

        php_file = file.attrib["path"].lower()
        cname = file.find("class//name").text.lower()
        fcname = file.find("class//full_name").text.lower()
        namespace = fcname.replace(cname, "")[1:]

        #folder = folder_to_save#pt.dirname(xml_file)
        create_folders(folder, namespace)
        ftosave = open(pt.join(folder, namespace, php_file[:-4] + ".py"), "w")
        ftosave.write(output)
        ftosave.close()

        output = ''
        open(pt.join(folder, namespace,"__init__.py"), 'a').close()
        f = folder.replace(namespace, "")
        for ff in namespace.split("\\"):
            f = pt.join(f, ff)
            open(pt.join(f,"__init__.py"), 'a').close()

def usage():
    print("wrapper_gen.py -i xmlfile -o outpath")
    
if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:i:o:", ["help","input=", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = "./gen_wrapper"
    input_file = None
    
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i", "--input"):
            input_file = a
            
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"    

    xml_to_py(input_file, output)
