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
Configuration for System Settings resource
'''

class system_settings(base_resource):
	_session_timeout= ""
	_id= ""
	_disable_agent_old_password_input= ""
	_is_metering_enabled= ""
	_secure_access_only= ""
	_enable_certificate_download= ""
	_basicauth= ""
	_heartbeatinterval= ""
	_enable_apiproxy_credentials= ""
	_enable_session_timeout= ""
	_inventoryrefreshinterval= ""
	_enable_shell_access= ""
	_enable_delete_interface_on_adc= ""
	_keep_alive_ping_interval= ""
	_authorize_deviceapiproxy= ""
	_disk_utilization_threshold= ""
	_port_model= ""
	_enable_nsrecover_login= ""
	_prompt_creds_for_stylebooks= ""
	_enable_cuxip= ""
	_keep_adc_image_count= ""
	_svm_ns_comm= ""
	_session_timeout_unit= ""
	_act_id= ""
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
			return "system_settings"
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
			return "system_settingss"
		except Exception as e :
			raise e



	'''
	get Session timeout for the system
	'''
	@property
	def session_timeout(self) :
		try:
			return self._session_timeout
		except Exception as e :
			raise e
	'''
	set Session timeout for the system
	'''
	@session_timeout.setter
	def session_timeout(self,session_timeout):
		try :
			if not isinstance(session_timeout,int):
				raise TypeError("session_timeout must be set to int value")
			self._session_timeout = session_timeout
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
	get Disable old password input requirement while changing NetScaler Agent password
	'''
	@property
	def disable_agent_old_password_input(self) :
		try:
			return self._disable_agent_old_password_input
		except Exception as e :
			raise e
	'''
	set Disable old password input requirement while changing NetScaler Agent password
	'''
	@disable_agent_old_password_input.setter
	def disable_agent_old_password_input(self,disable_agent_old_password_input):
		try :
			if not isinstance(disable_agent_old_password_input,bool):
				raise TypeError("disable_agent_old_password_input must be set to bool value")
			self._disable_agent_old_password_input = disable_agent_old_password_input
		except Exception as e :
			raise e


	'''
	get Enable Metering for NetScaler VPX on SDX
	'''
	@property
	def is_metering_enabled(self) :
		try:
			return self._is_metering_enabled
		except Exception as e :
			raise e
	'''
	set Enable Metering for NetScaler VPX on SDX
	'''
	@is_metering_enabled.setter
	def is_metering_enabled(self,is_metering_enabled):
		try :
			if not isinstance(is_metering_enabled,bool):
				raise TypeError("is_metering_enabled must be set to bool value")
			self._is_metering_enabled = is_metering_enabled
		except Exception as e :
			raise e


	'''
	get Secure Access only
	'''
	@property
	def secure_access_only(self) :
		try:
			return self._secure_access_only
		except Exception as e :
			raise e
	'''
	set Secure Access only
	'''
	@secure_access_only.setter
	def secure_access_only(self,secure_access_only):
		try :
			if not isinstance(secure_access_only,bool):
				raise TypeError("secure_access_only must be set to bool value")
			self._secure_access_only = secure_access_only
		except Exception as e :
			raise e


	'''
	get Enable Certificate Download
	'''
	@property
	def enable_certificate_download(self) :
		try:
			return self._enable_certificate_download
		except Exception as e :
			raise e
	'''
	set Enable Certificate Download
	'''
	@enable_certificate_download.setter
	def enable_certificate_download(self,enable_certificate_download):
		try :
			if not isinstance(enable_certificate_download,bool):
				raise TypeError("enable_certificate_download must be set to bool value")
			self._enable_certificate_download = enable_certificate_download
		except Exception as e :
			raise e


	'''
	get Allow Basic Authentication Protocol
	'''
	@property
	def basicauth(self) :
		try:
			return self._basicauth
		except Exception as e :
			raise e
	'''
	set Allow Basic Authentication Protocol
	'''
	@basicauth.setter
	def basicauth(self,basicauth):
		try :
			if not isinstance(basicauth,bool):
				raise TypeError("basicauth must be set to bool value")
			self._basicauth = basicauth
		except Exception as e :
			raise e


	'''
	get Client heart beat interval in seconds
	'''
	@property
	def heartbeatinterval(self) :
		try:
			return self._heartbeatinterval
		except Exception as e :
			raise e
	'''
	set Client heart beat interval in seconds
	'''
	@heartbeatinterval.setter
	def heartbeatinterval(self,heartbeatinterval):
		try :
			if not isinstance(heartbeatinterval,int):
				raise TypeError("heartbeatinterval must be set to int value")
			self._heartbeatinterval = heartbeatinterval
		except Exception as e :
			raise e


	'''
	get Enable API Proxy Credentials
	'''
	@property
	def enable_apiproxy_credentials(self) :
		try:
			return self._enable_apiproxy_credentials
		except Exception as e :
			raise e
	'''
	set Enable API Proxy Credentials
	'''
	@enable_apiproxy_credentials.setter
	def enable_apiproxy_credentials(self,enable_apiproxy_credentials):
		try :
			if not isinstance(enable_apiproxy_credentials,bool):
				raise TypeError("enable_apiproxy_credentials must be set to bool value")
			self._enable_apiproxy_credentials = enable_apiproxy_credentials
		except Exception as e :
			raise e


	'''
	get Enables session timeout feature
	'''
	@property
	def enable_session_timeout(self) :
		try:
			return self._enable_session_timeout
		except Exception as e :
			raise e
	'''
	set Enables session timeout feature
	'''
	@enable_session_timeout.setter
	def enable_session_timeout(self,enable_session_timeout):
		try :
			if not isinstance(enable_session_timeout,bool):
				raise TypeError("enable_session_timeout must be set to bool value")
			self._enable_session_timeout = enable_session_timeout
		except Exception as e :
			raise e


	'''
	get Client inventory refresh interval in minutes
	'''
	@property
	def inventoryrefreshinterval(self) :
		try:
			return self._inventoryrefreshinterval
		except Exception as e :
			raise e
	'''
	set Client inventory refresh interval in minutes
	'''
	@inventoryrefreshinterval.setter
	def inventoryrefreshinterval(self,inventoryrefreshinterval):
		try :
			if not isinstance(inventoryrefreshinterval,int):
				raise TypeError("inventoryrefreshinterval must be set to int value")
			self._inventoryrefreshinterval = inventoryrefreshinterval
		except Exception as e :
			raise e


	'''
	get Enable Shell access for non-nsroot User(s)
	'''
	@property
	def enable_shell_access(self) :
		try:
			return self._enable_shell_access
		except Exception as e :
			raise e
	'''
	set Enable Shell access for non-nsroot User(s)
	'''
	@enable_shell_access.setter
	def enable_shell_access(self,enable_shell_access):
		try :
			if not isinstance(enable_shell_access,bool):
				raise TypeError("enable_shell_access must be set to bool value")
			self._enable_shell_access = enable_shell_access
		except Exception as e :
			raise e


	'''
	get Flag to enable/disable deleting interface from ADCs on SDX
	'''
	@property
	def enable_delete_interface_on_adc(self) :
		try:
			return self._enable_delete_interface_on_adc
		except Exception as e :
			raise e
	'''
	set Flag to enable/disable deleting interface from ADCs on SDX
	'''
	@enable_delete_interface_on_adc.setter
	def enable_delete_interface_on_adc(self,enable_delete_interface_on_adc):
		try :
			if not isinstance(enable_delete_interface_on_adc,bool):
				raise TypeError("enable_delete_interface_on_adc must be set to bool value")
			self._enable_delete_interface_on_adc = enable_delete_interface_on_adc
		except Exception as e :
			raise e


	'''
	get Agent web socket keep alive ping interval for the system
	'''
	@property
	def keep_alive_ping_interval(self) :
		try:
			return self._keep_alive_ping_interval
		except Exception as e :
			raise e
	'''
	set Agent web socket keep alive ping interval for the system
	'''
	@keep_alive_ping_interval.setter
	def keep_alive_ping_interval(self,keep_alive_ping_interval):
		try :
			if not isinstance(keep_alive_ping_interval,int):
				raise TypeError("keep_alive_ping_interval must be set to int value")
			self._keep_alive_ping_interval = keep_alive_ping_interval
		except Exception as e :
			raise e


	'''
	get Authorize the DeviceAPIProxy request
	'''
	@property
	def authorize_deviceapiproxy(self) :
		try:
			return self._authorize_deviceapiproxy
		except Exception as e :
			raise e
	'''
	set Authorize the DeviceAPIProxy request
	'''
	@authorize_deviceapiproxy.setter
	def authorize_deviceapiproxy(self,authorize_deviceapiproxy):
		try :
			if not isinstance(authorize_deviceapiproxy,bool):
				raise TypeError("authorize_deviceapiproxy must be set to bool value")
			self._authorize_deviceapiproxy = authorize_deviceapiproxy
		except Exception as e :
			raise e


	'''
	get Disk utilization threshold after which data processing it stopped
	'''
	@property
	def disk_utilization_threshold(self) :
		try:
			return self._disk_utilization_threshold
		except Exception as e :
			raise e
	'''
	set Disk utilization threshold after which data processing it stopped
	'''
	@disk_utilization_threshold.setter
	def disk_utilization_threshold(self,disk_utilization_threshold):
		try :
			if not isinstance(disk_utilization_threshold,int):
				raise TypeError("disk_utilization_threshold must be set to int value")
			self._disk_utilization_threshold = disk_utilization_threshold
		except Exception as e :
			raise e


	'''
	get Port Model for BR instance
	'''
	@property
	def port_model(self) :
		try:
			return self._port_model
		except Exception as e :
			raise e


	'''
	get This setting enalbes nsrecover login for SVM
	'''
	@property
	def enable_nsrecover_login(self) :
		try:
			return self._enable_nsrecover_login
		except Exception as e :
			raise e
	'''
	set This setting enalbes nsrecover login for SVM
	'''
	@enable_nsrecover_login.setter
	def enable_nsrecover_login(self,enable_nsrecover_login):
		try :
			if not isinstance(enable_nsrecover_login,bool):
				raise TypeError("enable_nsrecover_login must be set to bool value")
			self._enable_nsrecover_login = enable_nsrecover_login
		except Exception as e :
			raise e


	'''
	get Prompt Credentials for Stylebooks
	'''
	@property
	def prompt_creds_for_stylebooks(self) :
		try:
			return self._prompt_creds_for_stylebooks
		except Exception as e :
			raise e
	'''
	set Prompt Credentials for Stylebooks
	'''
	@prompt_creds_for_stylebooks.setter
	def prompt_creds_for_stylebooks(self,prompt_creds_for_stylebooks):
		try :
			if not isinstance(prompt_creds_for_stylebooks,bool):
				raise TypeError("prompt_creds_for_stylebooks must be set to bool value")
			self._prompt_creds_for_stylebooks = prompt_creds_for_stylebooks
		except Exception as e :
			raise e


	'''
	get Used to enable/disable CUXIP(Customer User Experience Improvement Program)
	'''
	@property
	def enable_cuxip(self) :
		try:
			return self._enable_cuxip
		except Exception as e :
			raise e
	'''
	set Used to enable/disable CUXIP(Customer User Experience Improvement Program)
	'''
	@enable_cuxip.setter
	def enable_cuxip(self,enable_cuxip):
		try :
			if not isinstance(enable_cuxip,bool):
				raise TypeError("enable_cuxip must be set to bool value")
			self._enable_cuxip = enable_cuxip
		except Exception as e :
			raise e


	'''
	get Count for number of NetScaler images to be saved in Agent
	'''
	@property
	def keep_adc_image_count(self) :
		try:
			return self._keep_adc_image_count
		except Exception as e :
			raise e
	'''
	set Count for number of NetScaler images to be saved in Agent
	'''
	@keep_adc_image_count.setter
	def keep_adc_image_count(self,keep_adc_image_count):
		try :
			if not isinstance(keep_adc_image_count,int):
				raise TypeError("keep_adc_image_count must be set to int value")
			self._keep_adc_image_count = keep_adc_image_count
		except Exception as e :
			raise e


	'''
	get Communication with Instances
	'''
	@property
	def svm_ns_comm(self) :
		try:
			return self._svm_ns_comm
		except Exception as e :
			raise e
	'''
	set Communication with Instances
	'''
	@svm_ns_comm.setter
	def svm_ns_comm(self,svm_ns_comm):
		try :
			if not isinstance(svm_ns_comm,str):
				raise TypeError("svm_ns_comm must be set to str value")
			self._svm_ns_comm = svm_ns_comm
		except Exception as e :
			raise e


	'''
	get Session timeout unit for the system
	'''
	@property
	def session_timeout_unit(self) :
		try:
			return self._session_timeout_unit
		except Exception as e :
			raise e
	'''
	set Session timeout unit for the system
	'''
	@session_timeout_unit.setter
	def session_timeout_unit(self,session_timeout_unit):
		try :
			if not isinstance(session_timeout_unit,str):
				raise TypeError("session_timeout_unit must be set to str value")
			self._session_timeout_unit = session_timeout_unit
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
	Use this operation to get system settings.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				system_settings_obj=system_settings()
				response = system_settings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify system settings.
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
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of system_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			system_settings_obj = system_settings()
			option_ = options()
			option_._filter=filter_
			return system_settings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the system_settings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			system_settings_obj = system_settings()
			option_ = options()
			option_._count=True
			response = system_settings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of system_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			system_settings_obj = system_settings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = system_settings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(system_settings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.system_settings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(system_settings_responses, response, "system_settings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.system_settings_response_array
				i=0
				error = [system_settings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.system_settings_response_array
			i=0
			system_settings_objs = [system_settings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_system_settings'):
					for props in obj._system_settings:
						result = service.payload_formatter.string_to_bulk_resource(system_settings_response,self.__class__.__name__,props)
						system_settings_objs[i] = result.system_settings
						i=i+1
			return system_settings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(system_settings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class system_settings_response(base_response):
	def __init__(self,length=1) :
		self.system_settings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.system_settings= [ system_settings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class system_settings_responses(base_response):
	def __init__(self,length=1) :
		self.system_settings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.system_settings_response_array = [ system_settings() for _ in range(length)]
