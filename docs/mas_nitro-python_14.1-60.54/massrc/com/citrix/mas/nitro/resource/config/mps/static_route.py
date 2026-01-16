'''
Copyright (c) 2008-2020 Citrix Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for Static Route resource
'''

class static_route(base_resource):
	_netmask= ""
	_gateway= ""
	_id= ""
	_network= ""
	__count=""
	'''
	get the resource id
	'''
	def get_resource_id(self) :
		try:
			if hasattr(self, 'id'):
				return self.id 
			else:
				return None 
		except Exception as e :
			raise e

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "static_route"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._id
		except Exception as e :
			raise e

	'''
	Returns the value of object file path argument.
	'''
	@property
	def file_path_value(self) :
		try:
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file component name.
	'''
	@property
	def file_component_value(self) :
		try :
			return "static_routes"
		except Exception as e :
			raise e



	'''
	get netmask for route addition
	'''
	@property
	def netmask(self) :
		try:
			return self._netmask
		except Exception as e :
			raise e
	'''
	set netmask for route addition
	'''
	@netmask.setter
	def netmask(self,netmask):
		try :
			if not isinstance(netmask,str):
				raise TypeError("netmask must be set to str value")
			self._netmask = netmask
		except Exception as e :
			raise e


	'''
	get Gateway for route addition
	'''
	@property
	def gateway(self) :
		try:
			return self._gateway
		except Exception as e :
			raise e
	'''
	set Gateway for route addition
	'''
	@gateway.setter
	def gateway(self,gateway):
		try :
			if not isinstance(gateway,str):
				raise TypeError("gateway must be set to str value")
			self._gateway = gateway
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
	'''
	@id.setter
	def id(self,id):
		try :
			if not isinstance(id,str):
				raise TypeError("id must be set to str value")
			self._id = id
		except Exception as e :
			raise e


	'''
	get network for route addition
	'''
	@property
	def network(self) :
		try:
			return self._network
		except Exception as e :
			raise e
	'''
	set network for route addition
	'''
	@network.setter
	def network(self,network):
		try :
			if not isinstance(network,str):
				raise TypeError("network must be set to str value")
			self._network = network
		except Exception as e :
			raise e

	'''
	Use this operation to get added static routes.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				static_route_obj=static_route()
				response = static_route_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add static route.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				return res
			else : 
				static_route_obj= static_route()
				return cls.perform_operation_bulk_request(service,resource,static_route_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete static route.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				return res
			else :
					static_route_obj=static_route()
					return cls.delete_bulk_request(client,resource,static_route_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of static_route resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			static_route_obj = static_route()
			option_ = options()
			option_._filter=filter_
			return static_route_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the static_route resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			static_route_obj = static_route()
			option_ = options()
			option_._count=True
			response = static_route_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of static_route resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			static_route_obj = static_route()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = static_route_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(static_route_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.static_route
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(static_route_responses, response, "static_route_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.static_route_response_array
				i=0
				error = [static_route() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.static_route_response_array
			i=0
			static_route_objs = [static_route() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_static_route'):
					for props in obj._static_route:
						result = service.payload_formatter.string_to_bulk_resource(static_route_response,self.__class__.__name__,props)
						static_route_objs[i] = result.static_route
						i=i+1
			return static_route_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(static_route,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class static_route_response(base_response):
	def __init__(self,length=1) :
		self.static_route= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.static_route= [ static_route() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class static_route_responses(base_response):
	def __init__(self,length=1) :
		self.static_route_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.static_route_response_array = [ static_route() for _ in range(length)]
