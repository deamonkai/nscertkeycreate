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
from massrc.com.citrix.mas.nitro.resource.config.ns.adc_vserver_appflow_info import adc_vserver_appflow_info
from massrc.com.citrix.mas.nitro.resource.config.ns.adc_params import adc_params


'''
Configuration for Virtual server appflow config on NetScaler resource
'''

class adc_vserver_appflow_config(base_resource):
	_feature_flag_enabled= ""
	_adc_appflow_info=[]
	_tenant_id= ""
	_is_internal= ""
	_adc_params_info=[]
	_act_id= ""
	_feature_flag_disabled= ""
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
			return "adc_vserver_appflow_config"
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
			return "adc_vserver_appflow_configs"
		except Exception as e :
			raise e


	'''
	Suggests if the enable-request is based on feature_flag
	'''
	@property
	def feature_flag_enabled(self):
		try:
			return self._feature_flag_enabled
		except Exception as e :
			raise e
	'''
	Suggests if the enable-request is based on feature_flag
	'''
	@feature_flag_enabled.setter
	def feature_flag_enabled(self,feature_flag_enabled):
		try :
			if not isinstance(feature_flag_enabled,bool):
				raise TypeError("feature_flag_enabled must be set to bool value")
			self._feature_flag_enabled = feature_flag_enabled
		except Exception as e :
			raise e

	'''
	NetScaler appflow info object
	'''
	@property
	def adc_appflow_info(self) :
		try:
			return self._adc_appflow_info
		except Exception as e :
			raise e
	'''
	NetScaler appflow info object
	'''
	@adc_appflow_info.setter
	def adc_appflow_info(self,adc_appflow_info) :
		try :
			if not isinstance(adc_appflow_info,list):
				raise TypeError("adc_appflow_info must be set to array of adc_vserver_appflow_info value")
			for item in adc_appflow_info :
				if not isinstance(item,adc_vserver_appflow_info):
					raise TypeError("item must be set to adc_vserver_appflow_info value")
			self._adc_appflow_info = adc_appflow_info
		except Exception as e :
			raise e

	'''
	TenantID
	'''
	@property
	def tenant_id(self):
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	TenantID
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e

	'''
	Suggests if the request is internal
	'''
	@property
	def is_internal(self):
		try:
			return self._is_internal
		except Exception as e :
			raise e
	'''
	Suggests if the request is internal
	'''
	@is_internal.setter
	def is_internal(self,is_internal):
		try :
			if not isinstance(is_internal,bool):
				raise TypeError("is_internal must be set to bool value")
			self._is_internal = is_internal
		except Exception as e :
			raise e

	'''
	NetScaler params info object
	'''
	@property
	def adc_params_info(self) :
		try:
			return self._adc_params_info
		except Exception as e :
			raise e
	'''
	NetScaler params info object
	'''
	@adc_params_info.setter
	def adc_params_info(self,adc_params_info) :
		try :
			if not isinstance(adc_params_info,list):
				raise TypeError("adc_params_info must be set to array of adc_params value")
			for item in adc_params_info :
				if not isinstance(item,adc_params):
					raise TypeError("item must be set to adc_params value")
			self._adc_params_info = adc_params_info
		except Exception as e :
			raise e

	'''
	Activity Id
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e

	'''
	Suggests if the disable-request is based on feature_flag
	'''
	@property
	def feature_flag_disabled(self):
		try:
			return self._feature_flag_disabled
		except Exception as e :
			raise e
	'''
	Suggests if the disable-request is based on feature_flag
	'''
	@feature_flag_disabled.setter
	def feature_flag_disabled(self,feature_flag_disabled):
		try :
			if not isinstance(feature_flag_disabled,bool):
				raise TypeError("feature_flag_disabled must be set to bool value")
			self._feature_flag_disabled = feature_flag_disabled
		except Exception as e :
			raise e

	'''
	get NA virtual server.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adc_vserver_appflow_config_obj=adc_vserver_appflow_config()
				response = adc_vserver_appflow_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	delete virtual server policy.
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
					adc_vserver_appflow_config_obj=adc_vserver_appflow_config()
					return cls.delete_bulk_request(client,resource,adc_vserver_appflow_config_obj)
		except Exception as e :
			raise e

	'''
	Add virtual server policy.
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
				adc_vserver_appflow_config_obj= adc_vserver_appflow_config()
				return cls.perform_operation_bulk_request(service,resource,adc_vserver_appflow_config_obj)
		except Exception as e :
			raise e

	'''
	modify virtual server policy.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				adc_vserver_appflow_config_obj=adc_vserver_appflow_config()
				return cls.update_bulk_request(client,resource,adc_vserver_appflow_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adc_vserver_appflow_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adc_vserver_appflow_config_obj = adc_vserver_appflow_config()
			option_ = options()
			option_._filter=filter_
			return adc_vserver_appflow_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adc_vserver_appflow_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adc_vserver_appflow_config_obj = adc_vserver_appflow_config()
			option_ = options()
			option_._count=True
			response = adc_vserver_appflow_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adc_vserver_appflow_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adc_vserver_appflow_config_obj = adc_vserver_appflow_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adc_vserver_appflow_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adc_vserver_appflow_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_vserver_appflow_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_vserver_appflow_config_responses, response, "adc_vserver_appflow_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_vserver_appflow_config_response_array
				i=0
				error = [adc_vserver_appflow_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_vserver_appflow_config_response_array
			i=0
			adc_vserver_appflow_config_objs = [adc_vserver_appflow_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_vserver_appflow_config'):
					for props in obj._adc_vserver_appflow_config:
						result = service.payload_formatter.string_to_bulk_resource(adc_vserver_appflow_config_response,self.__class__.__name__,props)
						adc_vserver_appflow_config_objs[i] = result.adc_vserver_appflow_config
						i=i+1
			return adc_vserver_appflow_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_vserver_appflow_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_vserver_appflow_config_response(base_response):
	def __init__(self,length=1) :
		self.adc_vserver_appflow_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_vserver_appflow_config= [ adc_vserver_appflow_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_vserver_appflow_config_responses(base_response):
	def __init__(self,length=1) :
		self.adc_vserver_appflow_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_vserver_appflow_config_response_array = [ adc_vserver_appflow_config() for _ in range(length)]
