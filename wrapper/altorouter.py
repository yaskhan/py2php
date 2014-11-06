class AltoRouter():

	def __init__(self, routes = [], basePath = '', matchTypes = []):
		"""Create router in one call from config."""
		pass


	def addRoutes(self, routes):
		"""
		Add multiple routes at once from array in the following format:
		  routes = [
		     [method, route, target, name]
		  ]
		@author Koen Punt
		"""
		pass
	

	def setBasePath(self, basePath):
		"""
		Set the base path.
		Useful if you are running your application from a subdirectory.
		"""
		pass


	def addMatchTypes(self, matchTypes):
		"""
		Add named match types. It uses array_merge so keys can be overwritten.
		@param matchTypes The key is the name and the value is the regex.
		"""
		pass


	def map(self, method, route, target, name = None):
		"""
		Map a route to a target
		@param method One of 5 HTTP Methods, or a pipe-separated list of multiple HTTP Methods (GET|POST|PATCH|PUT|DELETE)
		@param route The route regex, custom regex must start with an @. You can use multiple pre-set regex filters, like [i:id]
		@param target The target where this route should point to. Can be anything.
		@param name Optional name of this route. Supply if you want to reverse route this url in your application.
		"""
		pass



	def generate(self, routeName, params = []) : 
		"""
		Reversed routing
		Generate the URL for a named route. Replace regexes with supplied parameters
		@param routeName The name of the route.
		@param array @params Associative array of parameters to replace placeholders with.
		@return string The URL of the route with named parameters in place.
		"""
		pass



	def match(self, requestUrl=None, requestMethod=None) :
		"""
		Match a given Request Url against stored routes
		@return array|boolean Array with route information on success, false on failure (no match).
		"""
		pass