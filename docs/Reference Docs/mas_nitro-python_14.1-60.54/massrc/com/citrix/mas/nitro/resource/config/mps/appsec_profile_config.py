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
from massrc.com.citrix.mas.nitro.resource.config.mps.app_devices_info import app_devices_info
from massrc.com.citrix.mas.nitro.resource.config.mps.account_takeover_config import account_takeover_config
from massrc.com.citrix.mas.nitro.resource.config.mps.model_settings_info import model_settings_info


'''
Configuration for Appsec Profile config resource
'''

class appsec_profile_config(base_resource):
	_enabled= ""
	_id= ""
	_app_devices=[]
	_profile_name= ""
	_config_mode= ""
	_ato_config=[]
	_model_settings=[]
	_is_default= ""
	_no_of_apps= ""
	_no_of_models= ""
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
			return "appsec_profile_config"
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
			return "appsec_profile_configs"
		except Exception as e :
			raise e



	'''
	get Flag to check if the profile is enabled or not.
	'''
	@property
	def enabled(self) :
		try:
			return self._enabled
		except Exception as e :
			raise e
	'''
	set Flag to check if the profile is enabled or not.
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
	get Id is system generated key.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e


	'''
	get Mapping NetScaler IPs to Apps
	'''
	@property
	def app_devices(self) :
		try:
			return self._app_devices
		except Exception as e :
			raise e
	'''
	set Mapping NetScaler IPs to Apps
	'''
	@app_devices.setter
	def app_devices(self,app_devices) :
		try :
			if not isinstance(app_devices,list):
				raise TypeError("app_devices must be set to array of app_devices_info value")
			for item in app_devices :
				if not isinstance(item,app_devices_info):
					raise TypeError("item must be set to app_devices_info value")
			self._app_devices = app_devices
		except Exception as e :
			raise e


	'''
	get Profile Name used for naming a model sensitivity config
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile Name used for naming a model sensitivity config
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e


	'''
	get Config modes can be Model Sensitivity (0) 
	'''
	@property
	def config_mode(self) :
		try:
			return self._config_mode
		except Exception as e :
			raise e
	'''
	set Config modes can be Model Sensitivity (0) 
	'''
	@config_mode.setter
	def config_mode(self,config_mode):
		try :
			if not isinstance(config_mode,int):
				raise TypeError("config_mode must be set to int value")
			self._config_mode = config_mode
		except Exception as e :
			raise e


	'''
	get Mapping ATO settings to app devices of current profile
	'''
	@property
	def ato_config(self) :
		try:
			return self._ato_config
		except Exception as e :
			raise e
	'''
	set Mapping ATO settings to app devices of current profile
	'''
	@ato_config.setter
	def ato_config(self,ato_config) :
		try :
			if not isinstance(ato_config,list):
				raise TypeError("ato_config must be set to array of account_takeover_config value")
			for item in ato_config :
				if not isinstance(item,account_takeover_config):
					raise TypeError("item must be set to account_takeover_config value")
			self._ato_config = ato_config
		except Exception as e :
			raise e


	'''
	get Appsec Model Settings info
	'''
	@property
	def model_settings(self) :
		try:
			return self._model_settings
		except Exception as e :
			raise e
	'''
	set Appsec Model Settings info
	'''
	@model_settings.setter
	def model_settings(self,model_settings) :
		try :
			if not isinstance(model_settings,list):
				raise TypeError("model_settings must be set to array of model_settings_info value")
			for item in model_settings :
				if not isinstance(item,model_settings_info):
					raise TypeError("item must be set to model_settings_info value")
			self._model_settings = model_settings
		except Exception as e :
			raise e

	'''
	Flag to check Default Application
	'''
	@property
	def is_default(self):
		try:
			return self._is_default
		except Exception as e :
			raise e
	'''
	Flag to check Default Application
	'''
	@is_default.setter
	def is_default(self,is_default):
		try :
			if not isinstance(is_default,bool):
				raise TypeError("is_default must be set to bool value")
			self._is_default = is_default
		except Exception as e :
			raise e

	'''
	Number of Applications configured
	'''
	@property
	def no_of_apps(self):
		try:
			return self._no_of_apps
		except Exception as e :
			raise e
	'''
	Number of Applications configured
	'''
	@no_of_apps.setter
	def no_of_apps(self,no_of_apps):
		try :
			if not isinstance(no_of_apps,str):
				raise TypeError("no_of_apps must be set to str value")
			self._no_of_apps = no_of_apps
		except Exception as e :
			raise e

	'''
	Number of models
	'''
	@property
	def no_of_models(self):
		try:
			return self._no_of_models
		except Exception as e :
			raise e
	'''
	Number of models
	'''
	@no_of_models.setter
	def no_of_models(self,no_of_models):
		try :
			if not isinstance(no_of_models,str):
				raise TypeError("no_of_models must be set to str value")
			self._no_of_models = no_of_models
		except Exception as e :
			raise e

	'''
	Use this operation to get Appsec Config Profile.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				appsec_profile_config_obj=appsec_profile_config()
				response = appsec_profile_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add Appsec Config profile.
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
				appsec_profile_config_obj= appsec_profile_config()
				return cls.perform_operation_bulk_request(service,resource,appsec_profile_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete Appsec Config Profile.
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
					appsec_profile_config_obj=appsec_profile_config()
					return cls.delete_bulk_request(client,resource,appsec_profile_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify Appsec Config profile.
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
				appsec_profile_config_obj=appsec_profile_config()
				return cls.update_bulk_request(client,resource,appsec_profile_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of appsec_profile_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			appsec_profile_config_obj = appsec_profile_config()
			option_ = options()
			option_._filter=filter_
			return appsec_profile_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the appsec_profile_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			appsec_profile_config_obj = appsec_profile_config()
			option_ = options()
			option_._count=True
			response = appsec_profile_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of appsec_profile_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			appsec_profile_config_obj = appsec_profile_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = appsec_profile_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(appsec_profile_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appsec_profile_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(appsec_profile_config_responses, response, "appsec_profile_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.appsec_profile_config_response_array
				i=0
				error = [appsec_profile_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.appsec_profile_config_response_array
			i=0
			appsec_profile_config_objs = [appsec_profile_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_appsec_profile_config'):
					for props in obj._appsec_profile_config:
						result = service.payload_formatter.string_to_bulk_resource(appsec_profile_config_response,self.__class__.__name__,props)
						appsec_profile_config_objs[i] = result.appsec_profile_config
						i=i+1
			return appsec_profile_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(appsec_profile_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class appsec_profile_config_response(base_response):
	def __init__(self,length=1) :
		self.appsec_profile_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.appsec_profile_config= [ appsec_profile_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class appsec_profile_config_responses(base_response):
	def __init__(self,length=1) :
		self.appsec_profile_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.appsec_profile_config_response_array = [ appsec_profile_config() for _ in range(length)]
