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
Configuration for Proxy configuration resource
'''

class proxy_server(base_resource):
	_port= ""
	_enabled= ""
	_id= ""
	_password= ""
	_ip_address= ""
	_username= ""
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
			return "proxy_server"
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
			return "proxy_servers"
		except Exception as e :
			raise e



	'''
	get Port number of proxy server
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set Port number of proxy server
	'''
	@port.setter
	def port(self,port):
		try :
			if not isinstance(port,int):
				raise TypeError("port must be set to int value")
			self._port = port
		except Exception as e :
			raise e


	'''
	get Is proxy server enabled
	'''
	@property
	def enabled(self) :
		try:
			return self._enabled
		except Exception as e :
			raise e
	'''
	set Is proxy server enabled
	'''
	@enabled.setter
	def enabled(self,enabled):
		try :
			if not isinstance(enabled,bool):
				raise TypeError("enabled must be set to bool value")
			self._enabled = enabled
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
	get Password for proxy server
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password for proxy server
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e


	'''
	get IP address of proxy server
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP address of proxy server
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get Username for proxy server
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set Username for proxy server
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e

	'''
	Use this operation to modify proxy server.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				proxy_server_obj=proxy_server()
				return cls.update_bulk_request(client,resource,proxy_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get proxy server details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				proxy_server_obj=proxy_server()
				response = proxy_server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of proxy_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			proxy_server_obj = proxy_server()
			option_ = options()
			option_._filter=filter_
			return proxy_server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the proxy_server resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			proxy_server_obj = proxy_server()
			option_ = options()
			option_._count=True
			response = proxy_server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of proxy_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			proxy_server_obj = proxy_server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = proxy_server_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(proxy_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.proxy_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(proxy_server_responses, response, "proxy_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.proxy_server_response_array
				i=0
				error = [proxy_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.proxy_server_response_array
			i=0
			proxy_server_objs = [proxy_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_proxy_server'):
					for props in obj._proxy_server:
						result = service.payload_formatter.string_to_bulk_resource(proxy_server_response,self.__class__.__name__,props)
						proxy_server_objs[i] = result.proxy_server
						i=i+1
			return proxy_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(proxy_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class proxy_server_response(base_response):
	def __init__(self,length=1) :
		self.proxy_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.proxy_server= [ proxy_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class proxy_server_responses(base_response):
	def __init__(self,length=1) :
		self.proxy_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.proxy_server_response_array = [ proxy_server() for _ in range(length)]
