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
Configuration for Mapping Unified Appsec profile with Protection Info resource
'''

class protection_info(base_resource):
	_parent_id= ""
	_id= ""
	_type= ""
	_protection_id= ""
	_protection_name= ""
	_parent_name= ""
	_enable_keys= ""
	_config= ""
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
			return "protection_info"
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
			return "protection_infos"
		except Exception as e :
			raise e



	'''
	get Id of the parent resource
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set Id of the parent resource
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for protection
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for protection
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
	get Protection category
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Protection category
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get ID to validate the Protection
	'''
	@property
	def protection_id(self) :
		try:
			return self._protection_id
		except Exception as e :
			raise e
	'''
	set ID to validate the Protection
	'''
	@protection_id.setter
	def protection_id(self,protection_id):
		try :
			if not isinstance(protection_id,int):
				raise TypeError("protection_id must be set to int value")
			self._protection_id = protection_id
		except Exception as e :
			raise e


	'''
	get Protection name
	'''
	@property
	def protection_name(self) :
		try:
			return self._protection_name
		except Exception as e :
			raise e
	'''
	set Protection name
	'''
	@protection_name.setter
	def protection_name(self,protection_name):
		try :
			if not isinstance(protection_name,str):
				raise TypeError("protection_name must be set to str value")
			self._protection_name = protection_name
		except Exception as e :
			raise e


	'''
	get Resource name of parent resource
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set Resource name of parent resource
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e

	'''
	Protection rules enable keys
	'''
	@property
	def enable_keys(self):
		try:
			return self._enable_keys
		except Exception as e :
			raise e
	'''
	Protection rules enable keys
	'''
	@enable_keys.setter
	def enable_keys(self,enable_keys):
		try :
			if not isinstance(enable_keys,str):
				raise TypeError("enable_keys must be set to str value")
			self._enable_keys = enable_keys
		except Exception as e :
			raise e

	'''
	Protection rules
	'''
	@property
	def config(self):
		try:
			return self._config
		except Exception as e :
			raise e
	'''
	Protection rules
	'''
	@config.setter
	def config(self,config):
		try :
			if not isinstance(config,str):
				raise TypeError("config must be set to str value")
			self._config = config
		except Exception as e :
			raise e

	'''
	Use this operation to modify protections.
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
				protection_info_obj=protection_info()
				return cls.update_bulk_request(client,resource,protection_info_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get protection info.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				protection_info_obj=protection_info()
				response = protection_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete protections.
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
					protection_info_obj=protection_info()
					return cls.delete_bulk_request(client,resource,protection_info_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of protection_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			protection_info_obj = protection_info()
			option_ = options()
			option_._filter=filter_
			return protection_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the protection_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			protection_info_obj = protection_info()
			option_ = options()
			option_._count=True
			response = protection_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of protection_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			protection_info_obj = protection_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = protection_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(protection_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protection_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(protection_info_responses, response, "protection_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.protection_info_response_array
				i=0
				error = [protection_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.protection_info_response_array
			i=0
			protection_info_objs = [protection_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_protection_info'):
					for props in obj._protection_info:
						result = service.payload_formatter.string_to_bulk_resource(protection_info_response,self.__class__.__name__,props)
						protection_info_objs[i] = result.protection_info
						i=i+1
			return protection_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(protection_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class protection_info_response(base_response):
	def __init__(self,length=1) :
		self.protection_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.protection_info= [ protection_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class protection_info_responses(base_response):
	def __init__(self,length=1) :
		self.protection_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.protection_info_response_array = [ protection_info() for _ in range(length)]
