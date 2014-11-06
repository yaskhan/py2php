import ast
import pyphp
import getopt, sys

def usage():
    print("main -i file [opts] -o outfile.php")
    
    
if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hio:d", ["help","input=", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    input_file = None
    dump = False
    for o, a in opts:
        if o == "-d":
            dump = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i", "--input"):
            input_file = a
            
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"    

    ffile = open(input_file, "r")
    oout = open(output, "w")
    txt = ffile.read()

    asst = ast.parse(txt)
    out = pyphp.PythonToPhp(txt)
    if dump:
        duump = open("duump.txt", "w")
        duump.write(ast.dump(asst))
        duump.close()
    
    oout.write("<?php\n\n" + out.get_code())
	

		
    ffile.close()
    oout.close()
    