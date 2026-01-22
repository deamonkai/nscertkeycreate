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
from massrc.com.citrix.mas.nitro.resource.config.ns.adc_waf_bot_vserver_info import adc_waf_bot_vserver_info


'''
Configuration for Bot Profile Configuration Info resource
'''

class adc_waf_bot_profile_config(base_resource):
	_is_global= ""
	_stylebook_params= ""
	_configpack_id= ""
	_sb_version_info= ""
	_adc_vserver_profile_info=[]
	_sb_type= ""
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
			return "adc_waf_bot_profile_config"
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
			return "adc_waf_bot_profile_configs"
		except Exception as e :
			raise e



	'''
	get Bot Global Policy or Bot Vserver Level Policy
	'''
	@property
	def is_global(self) :
		try:
			return self._is_global
		except Exception as e :
			raise e
	'''
	set Bot Global Policy or Bot Vserver Level Policy
	'''
	@is_global.setter
	def is_global(self,is_global):
		try :
			if not isinstance(is_global,bool):
				raise TypeError("is_global must be set to bool value")
			self._is_global = is_global
		except Exception as e :
			raise e


	'''
	get Stylebook Parameter
	'''
	@property
	def stylebook_params(self) :
		try:
			return self._stylebook_params
		except Exception as e :
			raise e
	'''
	set Stylebook Parameter
	'''
	@stylebook_params.setter
	def stylebook_params(self,stylebook_params):
		try :
			if not isinstance(stylebook_params,str):
				raise TypeError("stylebook_params must be set to str value")
			self._stylebook_params = stylebook_params
		except Exception as e :
			raise e


	'''
	get configpack_id
	'''
	@property
	def configpack_id(self) :
		try:
			return self._configpack_id
		except Exception as e :
			raise e
	'''
	set configpack_id
	'''
	@configpack_id.setter
	def configpack_id(self,configpack_id):
		try :
			if not isinstance(configpack_id,str):
				raise TypeError("configpack_id must be set to str value")
			self._configpack_id = configpack_id
		except Exception as e :
			raise e


	'''
	get Stylebook Version Info
	'''
	@property
	def sb_version_info(self) :
		try:
			return self._sb_version_info
		except Exception as e :
			raise e
	'''
	set Stylebook Version Info
	'''
	@sb_version_info.setter
	def sb_version_info(self,sb_version_info):
		try :
			if not isinstance(sb_version_info,str):
				raise TypeError("sb_version_info must be set to str value")
			self._sb_version_info = sb_version_info
		except Exception as e :
			raise e


	'''
	get NetScaler Vserver info object
	'''
	@property
	def adc_vserver_profile_info(self) :
		try:
			return self._adc_vserver_profile_info
		except Exception as e :
			raise e
	'''
	set NetScaler Vserver info object
	'''
	@adc_vserver_profile_info.setter
	def adc_vserver_profile_info(self,adc_vserver_profile_info) :
		try :
			if not isinstance(adc_vserver_profile_info,list):
				raise TypeError("adc_vserver_profile_info must be set to array of adc_waf_bot_vserver_info value")
			for item in adc_vserver_profile_info :
				if not isinstance(item,adc_waf_bot_vserver_info):
					raise TypeError("item must be set to adc_waf_bot_vserver_info value")
			self._adc_vserver_profile_info = adc_vserver_profile_info
		except Exception as e :
			raise e


	'''
	get Stylebook Type WAF or BOT
	'''
	@property
	def sb_type(self) :
		try:
			return self._sb_type
		except Exception as e :
			raise e
	'''
	set Stylebook Type WAF or BOT
	'''
	@sb_type.setter
	def sb_type(self,sb_type):
		try :
			if not isinstance(sb_type,str):
				raise TypeError("sb_type must be set to str value")
			self._sb_type = sb_type
		except Exception as e :
			raise e

	'''
	Use this operation to modify system group.
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
				adc_waf_bot_profile_config_obj=adc_waf_bot_profile_config()
				return cls.update_bulk_request(client,resource,adc_waf_bot_profile_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add system group.
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
				adc_waf_bot_profile_config_obj= adc_waf_bot_profile_config()
				return cls.perform_operation_bulk_request(service,resource,adc_waf_bot_profile_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get system groups.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adc_waf_bot_profile_config_obj=adc_waf_bot_profile_config()
				response = adc_waf_bot_profile_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete system group(s).
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
					adc_waf_bot_profile_config_obj=adc_waf_bot_profile_config()
					return cls.delete_bulk_request(client,resource,adc_waf_bot_profile_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adc_waf_bot_profile_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adc_waf_bot_profile_config_obj = adc_waf_bot_profile_config()
			option_ = options()
			option_._filter=filter_
			return adc_waf_bot_profile_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adc_waf_bot_profile_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adc_waf_bot_profile_config_obj = adc_waf_bot_profile_config()
			option_ = options()
			option_._count=True
			response = adc_waf_bot_profile_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adc_waf_bot_profile_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adc_waf_bot_profile_config_obj = adc_waf_bot_profile_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adc_waf_bot_profile_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adc_waf_bot_profile_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_waf_bot_profile_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_waf_bot_profile_config_responses, response, "adc_waf_bot_profile_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_waf_bot_profile_config_response_array
				i=0
				error = [adc_waf_bot_profile_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_waf_bot_profile_config_response_array
			i=0
			adc_waf_bot_profile_config_objs = [adc_waf_bot_profile_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_waf_bot_profile_config'):
					for props in obj._adc_waf_bot_profile_config:
						result = service.payload_formatter.string_to_bulk_resource(adc_waf_bot_profile_config_response,self.__class__.__name__,props)
						adc_waf_bot_profile_config_objs[i] = result.adc_waf_bot_profile_config
						i=i+1
			return adc_waf_bot_profile_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_waf_bot_profile_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_waf_bot_profile_config_response(base_response):
	def __init__(self,length=1) :
		self.adc_waf_bot_profile_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_waf_bot_profile_config= [ adc_waf_bot_profile_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_waf_bot_profile_config_responses(base_response):
	def __init__(self,length=1) :
		self.adc_waf_bot_profile_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_waf_bot_profile_config_response_array = [ adc_waf_bot_profile_config() for _ in range(length)]
