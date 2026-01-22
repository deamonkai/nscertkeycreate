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
Configuration for Built-in Agent resource
'''

class built_in_agent(base_resource):
	_id= ""
	_name= ""
	_mastools_ws_state= ""
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
			return "built_in_agent"
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
			return "built_in_agents"
		except Exception as e :
			raise e



	'''
	get Built-in Agent ID
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Built-in Agent ID
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
	get Built-in Agent Name (IP Address)
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Built-in Agent Name (IP Address)
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get WebSocket State of built in agent, UP only if Web Socket is connected
	'''
	@property
	def mastools_ws_state(self) :
		try:
			return self._mastools_ws_state
		except Exception as e :
			raise e

	'''
	Use this operation to get Built-in Agent associated with a Tenant .
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				built_in_agent_obj=built_in_agent()
				response = built_in_agent_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add a Built-in Agent..
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
				built_in_agent_obj= built_in_agent()
				return cls.perform_operation_bulk_request(service,resource,built_in_agent_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify a Built-in Agent..
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
				built_in_agent_obj=built_in_agent()
				return cls.update_bulk_request(client,resource,built_in_agent_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete a Built-in Agent..
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
					built_in_agent_obj=built_in_agent()
					return cls.delete_bulk_request(client,resource,built_in_agent_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of built_in_agent resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			built_in_agent_obj = built_in_agent()
			option_ = options()
			option_._filter=filter_
			return built_in_agent_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the built_in_agent resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			built_in_agent_obj = built_in_agent()
			option_ = options()
			option_._count=True
			response = built_in_agent_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of built_in_agent resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			built_in_agent_obj = built_in_agent()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = built_in_agent_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(built_in_agent_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.built_in_agent
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(built_in_agent_responses, response, "built_in_agent_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.built_in_agent_response_array
				i=0
				error = [built_in_agent() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.built_in_agent_response_array
			i=0
			built_in_agent_objs = [built_in_agent() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_built_in_agent'):
					for props in obj._built_in_agent:
						result = service.payload_formatter.string_to_bulk_resource(built_in_agent_response,self.__class__.__name__,props)
						built_in_agent_objs[i] = result.built_in_agent
						i=i+1
			return built_in_agent_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(built_in_agent,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class built_in_agent_response(base_response):
	def __init__(self,length=1) :
		self.built_in_agent= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.built_in_agent= [ built_in_agent() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class built_in_agent_responses(base_response):
	def __init__(self,length=1) :
		self.built_in_agent_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.built_in_agent_response_array = [ built_in_agent() for _ in range(length)]
