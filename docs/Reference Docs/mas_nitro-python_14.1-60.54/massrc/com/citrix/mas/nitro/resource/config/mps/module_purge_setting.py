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
Configuration for Feature wise purge Setting resource
'''

class module_purge_setting(base_resource):
	_module_name= ""
	_purge_interval= ""
	_id= ""
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
			return "module_purge_setting"
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
			return "module_purge_settings"
		except Exception as e :
			raise e



	'''
	get module name
	'''
	@property
	def module_name(self) :
		try:
			return self._module_name
		except Exception as e :
			raise e
	'''
	set module name
	'''
	@module_name.setter
	def module_name(self,module_name):
		try :
			if not isinstance(module_name,str):
				raise TypeError("module_name must be set to str value")
			self._module_name = module_name
		except Exception as e :
			raise e


	'''
	get purge interval
	'''
	@property
	def purge_interval(self) :
		try:
			return self._purge_interval
		except Exception as e :
			raise e
	'''
	set purge interval
	'''
	@purge_interval.setter
	def purge_interval(self,purge_interval):
		try :
			if not isinstance(purge_interval,int):
				raise TypeError("purge_interval must be set to int value")
			self._purge_interval = purge_interval
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
	Use this operation to modify module purge settings.
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
				module_purge_setting_obj=module_purge_setting()
				return cls.update_bulk_request(client,resource,module_purge_setting_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get module purge settings.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				module_purge_setting_obj=module_purge_setting()
				response = module_purge_setting_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of module_purge_setting resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			module_purge_setting_obj = module_purge_setting()
			option_ = options()
			option_._filter=filter_
			return module_purge_setting_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the module_purge_setting resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			module_purge_setting_obj = module_purge_setting()
			option_ = options()
			option_._count=True
			response = module_purge_setting_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of module_purge_setting resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			module_purge_setting_obj = module_purge_setting()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = module_purge_setting_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(module_purge_setting_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.module_purge_setting
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(module_purge_setting_responses, response, "module_purge_setting_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.module_purge_setting_response_array
				i=0
				error = [module_purge_setting() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.module_purge_setting_response_array
			i=0
			module_purge_setting_objs = [module_purge_setting() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_module_purge_setting'):
					for props in obj._module_purge_setting:
						result = service.payload_formatter.string_to_bulk_resource(module_purge_setting_response,self.__class__.__name__,props)
						module_purge_setting_objs[i] = result.module_purge_setting
						i=i+1
			return module_purge_setting_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(module_purge_setting,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class module_purge_setting_response(base_response):
	def __init__(self,length=1) :
		self.module_purge_setting= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.module_purge_setting= [ module_purge_setting() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class module_purge_setting_responses(base_response):
	def __init__(self,length=1) :
		self.module_purge_setting_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.module_purge_setting_response_array = [ module_purge_setting() for _ in range(length)]
