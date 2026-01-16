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
Configuration for SSL Vserver A+ Config resource
'''

class ssl_aplus_config(base_resource):
	_act_id= ""
	_application_name= ""
	_operation= ""
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
			return "ssl_aplus_config"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
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
			return "ssl_aplus_configs"
		except Exception as e :
			raise e


	'''
	Activity ID that is used by GUI to track the polling status.
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e
	'''
	Activity ID that is used by GUI to track the polling status.
	'''
	@act_id.setter
	def act_id(self,act_id):
		try :
			if not isinstance(act_id,str):
				raise TypeError("act_id must be set to str value")
			self._act_id = act_id
		except Exception as e :
			raise e

	'''
	Application Name
	'''
	@property
	def application_name(self):
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	Application Name
	'''
	@application_name.setter
	def application_name(self,application_name):
		try :
			if not isinstance(application_name,str):
				raise TypeError("application_name must be set to str value")
			self._application_name = application_name
		except Exception as e :
			raise e

	'''
	operation
	'''
	@property
	def operation(self):
		try:
			return self._operation
		except Exception as e :
			raise e
	'''
	operation
	'''
	@operation.setter
	def operation(self,operation):
		try :
			if not isinstance(operation,str):
				raise TypeError("operation must be set to str value")
			self._operation = operation
		except Exception as e :
			raise e

	'''
	Use this operation to make app A+ / revert A+ changes.
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
				ssl_aplus_config_obj=ssl_aplus_config()
				return cls.update_bulk_request(client,resource,ssl_aplus_config_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ssl_aplus_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ssl_aplus_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ssl_aplus_config_responses, response, "ssl_aplus_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ssl_aplus_config_response_array
				i=0
				error = [ssl_aplus_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ssl_aplus_config_response_array
			i=0
			ssl_aplus_config_objs = [ssl_aplus_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ssl_aplus_config'):
					for props in obj._ssl_aplus_config:
						result = service.payload_formatter.string_to_bulk_resource(ssl_aplus_config_response,self.__class__.__name__,props)
						ssl_aplus_config_objs[i] = result.ssl_aplus_config
						i=i+1
			return ssl_aplus_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ssl_aplus_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ssl_aplus_config_response(base_response):
	def __init__(self,length=1) :
		self.ssl_aplus_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ssl_aplus_config= [ ssl_aplus_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ssl_aplus_config_responses(base_response):
	def __init__(self,length=1) :
		self.ssl_aplus_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ssl_aplus_config_response_array = [ ssl_aplus_config() for _ in range(length)]
