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
from massrc.com.citrix.mas.nitro.resource.config.ns.protection_info import protection_info
from massrc.com.citrix.mas.nitro.resource.config.mps.app_devices_info import app_devices_info


'''
Configuration for unified_appsec_profile resource
'''

class unified_appsec_profile(base_resource):
	_id= ""
	_app_protections=[]
	_parent_template= ""
	_profile_name= ""
	_monitor_mode_toggle= ""
	_is_default= ""
	_last_modified= ""
	_app_devices=[]
	_configpack_id= ""
	_no_of_protections= ""
	_enable_analytics= ""
	_release= ""
	_appsec_verbose_log= ""
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
			return "unified_appsec_profile"
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
			return "unified_appsec_profiles"
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
	get protection info
	'''
	@property
	def app_protections(self) :
		try:
			return self._app_protections
		except Exception as e :
			raise e
	'''
	set protection info
	'''
	@app_protections.setter
	def app_protections(self,app_protections) :
		try :
			if not isinstance(app_protections,list):
				raise TypeError("app_protections must be set to array of protection_info value")
			for item in app_protections :
				if not isinstance(item,protection_info):
					raise TypeError("item must be set to protection_info value")
			self._app_protections = app_protections
		except Exception as e :
			raise e


	'''
	get Template name used to create this profile
	'''
	@property
	def parent_template(self) :
		try:
			return self._parent_template
		except Exception as e :
			raise e
	'''
	set Template name used to create this profile
	'''
	@parent_template.setter
	def parent_template(self,parent_template):
		try :
			if not isinstance(parent_template,str):
				raise TypeError("parent_template must be set to str value")
			self._parent_template = parent_template
		except Exception as e :
			raise e


	'''
	get Profile name
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile name
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
	get Monitor mode toggle
	'''
	@property
	def monitor_mode_toggle(self) :
		try:
			return self._monitor_mode_toggle
		except Exception as e :
			raise e
	'''
	set Monitor mode toggle
	'''
	@monitor_mode_toggle.setter
	def monitor_mode_toggle(self,monitor_mode_toggle):
		try :
			if not isinstance(monitor_mode_toggle,bool):
				raise TypeError("monitor_mode_toggle must be set to bool value")
			self._monitor_mode_toggle = monitor_mode_toggle
		except Exception as e :
			raise e


	'''
	get Flag to check Default Application
	'''
	@property
	def is_default(self) :
		try:
			return self._is_default
		except Exception as e :
			raise e
	'''
	set Flag to check Default Application
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
	get Last Modified time
	'''
	@property
	def last_modified(self) :
		try:
			return self._last_modified
		except Exception as e :
			raise e
	'''
	set Last Modified time
	'''
	@last_modified.setter
	def last_modified(self,last_modified):
		try :
			if not isinstance(last_modified,str):
				raise TypeError("last_modified must be set to str value")
			self._last_modified = last_modified
		except Exception as e :
			raise e


	'''
	get Mapping ADC IPs to Apps
	'''
	@property
	def app_devices(self) :
		try:
			return self._app_devices
		except Exception as e :
			raise e
	'''
	set Mapping ADC IPs to Apps
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
	get Stylebook Config Pack ID
	'''
	@property
	def configpack_id(self) :
		try:
			return self._configpack_id
		except Exception as e :
			raise e
	'''
	set Stylebook Config Pack ID
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
	Number of Protections
	'''
	@property
	def no_of_protections(self):
		try:
			return self._no_of_protections
		except Exception as e :
			raise e
	'''
	Number of Protections
	'''
	@no_of_protections.setter
	def no_of_protections(self,no_of_protections):
		try :
			if not isinstance(no_of_protections,str):
				raise TypeError("no_of_protections must be set to str value")
			self._no_of_protections = no_of_protections
		except Exception as e :
			raise e

	'''
	Enable Analytics as part of Unified Appsec Config.
	'''
	@property
	def enable_analytics(self):
		try:
			return self._enable_analytics
		except Exception as e :
			raise e
	'''
	Enable Analytics as part of Unified Appsec Config.
	'''
	@enable_analytics.setter
	def enable_analytics(self,enable_analytics):
		try :
			if not isinstance(enable_analytics,bool):
				raise TypeError("enable_analytics must be set to bool value")
			self._enable_analytics = enable_analytics
		except Exception as e :
			raise e

	'''
	NS Release
	'''
	@property
	def release(self):
		try:
			return self._release
		except Exception as e :
			raise e
	'''
	NS Release
	'''
	@release.setter
	def release(self,release):
		try :
			if not isinstance(release,str):
				raise TypeError("release must be set to str value")
			self._release = release
		except Exception as e :
			raise e

	'''
	appsec verbose log
	'''
	@property
	def appsec_verbose_log(self):
		try:
			return self._appsec_verbose_log
		except Exception as e :
			raise e
	'''
	appsec verbose log
	'''
	@appsec_verbose_log.setter
	def appsec_verbose_log(self,appsec_verbose_log):
		try :
			if not isinstance(appsec_verbose_log,str):
				raise TypeError("appsec_verbose_log must be set to str value")
			self._appsec_verbose_log = appsec_verbose_log
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
				unified_appsec_profile_obj=unified_appsec_profile()
				response = unified_appsec_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
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
					unified_appsec_profile_obj=unified_appsec_profile()
					return cls.delete_bulk_request(client,resource,unified_appsec_profile_obj)
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
				unified_appsec_profile_obj= unified_appsec_profile()
				return cls.perform_operation_bulk_request(service,resource,unified_appsec_profile_obj)
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
				unified_appsec_profile_obj=unified_appsec_profile()
				return cls.update_bulk_request(client,resource,unified_appsec_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of unified_appsec_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			unified_appsec_profile_obj = unified_appsec_profile()
			option_ = options()
			option_._filter=filter_
			return unified_appsec_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the unified_appsec_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			unified_appsec_profile_obj = unified_appsec_profile()
			option_ = options()
			option_._count=True
			response = unified_appsec_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of unified_appsec_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			unified_appsec_profile_obj = unified_appsec_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = unified_appsec_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(unified_appsec_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.unified_appsec_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(unified_appsec_profile_responses, response, "unified_appsec_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.unified_appsec_profile_response_array
				i=0
				error = [unified_appsec_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.unified_appsec_profile_response_array
			i=0
			unified_appsec_profile_objs = [unified_appsec_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_unified_appsec_profile'):
					for props in obj._unified_appsec_profile:
						result = service.payload_formatter.string_to_bulk_resource(unified_appsec_profile_response,self.__class__.__name__,props)
						unified_appsec_profile_objs[i] = result.unified_appsec_profile
						i=i+1
			return unified_appsec_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(unified_appsec_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class unified_appsec_profile_response(base_response):
	def __init__(self,length=1) :
		self.unified_appsec_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.unified_appsec_profile= [ unified_appsec_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class unified_appsec_profile_responses(base_response):
	def __init__(self,length=1) :
		self.unified_appsec_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.unified_appsec_profile_response_array = [ unified_appsec_profile() for _ in range(length)]
