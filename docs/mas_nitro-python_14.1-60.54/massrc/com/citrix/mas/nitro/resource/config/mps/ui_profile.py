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
Configuration for UI Load profile resource
'''

class ui_profile(base_resource):
	_hypervisor_uptime= ""
	_build_number_short= ""
	_build_number= ""
	_current_time= ""
	_time_zone= ""
	_is_cloud= ""
	_motd= ""
	_host= ""
	_bios_version= ""
	_upgrade_agent_version= ""
	_config_motd= ""
	_is_container= ""
	_username= ""
	_serial= ""
	_product_build_number= ""
	_current_user_permission= ""
	_deployment_type= ""
	_hist_mig_inprog= ""
	_platform= ""
	_product= ""
	_time_zone_offset= ""
	_is_cuxip_enabled= ""
	_sysid= ""
	_maps_apikey= ""
	_current_tenant_id= ""
	_is_passive= ""
	_uptime= ""
	_hostname= ""
	_current_time_formatted= ""
	_current_tenant= ""
	_hostid= ""
	_product_version= ""
	_pending_tasks_count= ""
	_cc_client_id= ""
	_agent_count= ""
	_cc_profile_skip= ""
	_is_light_tenant= ""
	_cc_profile_id= ""
	_cloud_platform= ""
	_device_count= ""
	_cloud_deployment_env= ""
	_cc_profile= ""
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
			return "ui_profile"
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
			return "ui_profiles"
		except Exception as e :
			raise e



	'''
	get Hypervisor Uptime
	'''
	@property
	def hypervisor_uptime(self) :
		try:
			return self._hypervisor_uptime
		except Exception as e :
			raise e


	'''
	get Build Number without Date
	'''
	@property
	def build_number_short(self) :
		try:
			return self._build_number_short
		except Exception as e :
			raise e


	'''
	get Build Number
	'''
	@property
	def build_number(self) :
		try:
			return self._build_number
		except Exception as e :
			raise e


	'''
	get Current Time
	'''
	@property
	def current_time(self) :
		try:
			return self._current_time
		except Exception as e :
			raise e


	'''
	get Server Time Zone
	'''
	@property
	def time_zone(self) :
		try:
			return self._time_zone
		except Exception as e :
			raise e


	'''
	get True if its a cloud deployment
	'''
	@property
	def is_cloud(self) :
		try:
			return self._is_cloud
		except Exception as e :
			raise e
	'''
	set True if its a cloud deployment
	'''
	@is_cloud.setter
	def is_cloud(self,is_cloud):
		try :
			if not isinstance(is_cloud,bool):
				raise TypeError("is_cloud must be set to bool value")
			self._is_cloud = is_cloud
		except Exception as e :
			raise e


	'''
	get Message of the Day (contents of motd file) that can be shown on UI after successful login
	'''
	@property
	def motd(self) :
		try:
			return self._motd
		except Exception as e :
			raise e
	'''
	set Message of the Day (contents of motd file) that can be shown on UI after successful login
	'''
	@motd.setter
	def motd(self,motd):
		try :
			if not isinstance(motd,str):
				raise TypeError("motd must be set to str value")
			self._motd = motd
		except Exception as e :
			raise e


	'''
	get Host IP Address on which system is running, this will set for each client session only
	'''
	@property
	def host(self) :
		try:
			return self._host
		except Exception as e :
			raise e


	'''
	get BIOS Version
	'''
	@property
	def bios_version(self) :
		try:
			return self._bios_version
		except Exception as e :
			raise e


	'''
	get Indicates the next version the agent needs to upgrade to.
	'''
	@property
	def upgrade_agent_version(self) :
		try:
			return self._upgrade_agent_version
		except Exception as e :
			raise e
	'''
	set Indicates the next version the agent needs to upgrade to.
	'''
	@upgrade_agent_version.setter
	def upgrade_agent_version(self,upgrade_agent_version):
		try :
			if not isinstance(upgrade_agent_version,str):
				raise TypeError("upgrade_agent_version must be set to str value")
			self._upgrade_agent_version = upgrade_agent_version
		except Exception as e :
			raise e


	'''
	get Configure Message of the Day (contents of motd file), this needs to be set true if user wants to configure message if the day
	'''
	@property
	def config_motd(self) :
		try:
			return self._config_motd
		except Exception as e :
			raise e
	'''
	set Configure Message of the Day (contents of motd file), this needs to be set true if user wants to configure message if the day
	'''
	@config_motd.setter
	def config_motd(self,config_motd):
		try :
			if not isinstance(config_motd,bool):
				raise TypeError("config_motd must be set to bool value")
			self._config_motd = config_motd
		except Exception as e :
			raise e


	'''
	get True if its a container deployment
	'''
	@property
	def is_container(self) :
		try:
			return self._is_container
		except Exception as e :
			raise e
	'''
	set True if its a container deployment
	'''
	@is_container.setter
	def is_container(self,is_container):
		try :
			if not isinstance(is_container,bool):
				raise TypeError("is_container must be set to bool value")
			self._is_container = is_container
		except Exception as e :
			raise e


	'''
	get User Name who is currently connected to the system
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e


	'''
	get Serial Number
	'''
	@property
	def serial(self) :
		try:
			return self._serial
		except Exception as e :
			raise e


	'''
	get Product Build Number
	'''
	@property
	def product_build_number(self) :
		try:
			return self._product_build_number
		except Exception as e :
			raise e


	'''
	get This property will show the permission type for current user
	'''
	@property
	def current_user_permission(self) :
		try:
			return self._current_user_permission
		except Exception as e :
			raise e


	'''
	get Indicates the type of deployment of NetScaler Console: standalone or ha or scaleout.
	'''
	@property
	def deployment_type(self) :
		try:
			return self._deployment_type
		except Exception as e :
			raise e
	'''
	set Indicates the type of deployment of NetScaler Console: standalone or ha or scaleout.
	'''
	@deployment_type.setter
	def deployment_type(self,deployment_type):
		try :
			if not isinstance(deployment_type,str):
				raise TypeError("deployment_type must be set to str value")
			self._deployment_type = deployment_type
		except Exception as e :
			raise e


	'''
	get Indicates whether the historical tables database migration is in progress or not.
	'''
	@property
	def hist_mig_inprog(self) :
		try:
			return self._hist_mig_inprog
		except Exception as e :
			raise e
	'''
	set Indicates whether the historical tables database migration is in progress or not.
	'''
	@hist_mig_inprog.setter
	def hist_mig_inprog(self,hist_mig_inprog):
		try :
			if not isinstance(hist_mig_inprog,bool):
				raise TypeError("hist_mig_inprog must be set to bool value")
			self._hist_mig_inprog = hist_mig_inprog
		except Exception as e :
			raise e


	'''
	get Platform
	'''
	@property
	def platform(self) :
		try:
			return self._platform
		except Exception as e :
			raise e


	'''
	get Product Name
	'''
	@property
	def product(self) :
		try:
			return self._product
		except Exception as e :
			raise e


	'''
	get Time zone offset in minutes (Example:-330)
	'''
	@property
	def time_zone_offset(self) :
		try:
			return self._time_zone_offset
		except Exception as e :
			raise e


	'''
	get Indicates whether CUXIP is enabled or not.
	'''
	@property
	def is_cuxip_enabled(self) :
		try:
			return self._is_cuxip_enabled
		except Exception as e :
			raise e
	'''
	set Indicates whether CUXIP is enabled or not.
	'''
	@is_cuxip_enabled.setter
	def is_cuxip_enabled(self,is_cuxip_enabled):
		try :
			if not isinstance(is_cuxip_enabled,bool):
				raise TypeError("is_cuxip_enabled must be set to bool value")
			self._is_cuxip_enabled = is_cuxip_enabled
		except Exception as e :
			raise e


	'''
	get System Id
	'''
	@property
	def sysid(self) :
		try:
			return self._sysid
		except Exception as e :
			raise e


	'''
	get Maps API Key
	'''
	@property
	def maps_apikey(self) :
		try:
			return self._maps_apikey
		except Exception as e :
			raise e
	'''
	set Maps API Key
	'''
	@maps_apikey.setter
	def maps_apikey(self,maps_apikey):
		try :
			if not isinstance(maps_apikey,str):
				raise TypeError("maps_apikey must be set to str value")
			self._maps_apikey = maps_apikey
		except Exception as e :
			raise e


	'''
	get Current Tenant Id for logged-in user
	'''
	@property
	def current_tenant_id(self) :
		try:
			return self._current_tenant_id
		except Exception as e :
			raise e


	'''
	get Indicates the node's state: ACTIVE or PASSIVE in a HA deployment.
	'''
	@property
	def is_passive(self) :
		try:
			return self._is_passive
		except Exception as e :
			raise e
	'''
	set Indicates the node's state: ACTIVE or PASSIVE in a HA deployment.
	'''
	@is_passive.setter
	def is_passive(self,is_passive):
		try :
			if not isinstance(is_passive,bool):
				raise TypeError("is_passive must be set to bool value")
			self._is_passive = is_passive
		except Exception as e :
			raise e


	'''
	get Uptime
	'''
	@property
	def uptime(self) :
		try:
			return self._uptime
		except Exception as e :
			raise e


	'''
	get Host name on which system is running
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e


	'''
	get Current Time (Formatted)
	'''
	@property
	def current_time_formatted(self) :
		try:
			return self._current_time_formatted
		except Exception as e :
			raise e


	'''
	get Current Tenant Name for logged-in user
	'''
	@property
	def current_tenant(self) :
		try:
			return self._current_tenant
		except Exception as e :
			raise e


	'''
	get Host Id
	'''
	@property
	def hostid(self) :
		try:
			return self._hostid
		except Exception as e :
			raise e


	'''
	get Product Version
	'''
	@property
	def product_version(self) :
		try:
			return self._product_version
		except Exception as e :
			raise e

	'''
	Count of incomplete tasks
	'''
	@property
	def pending_tasks_count(self):
		try:
			return self._pending_tasks_count
		except Exception as e :
			raise e
	'''
	Count of incomplete tasks
	'''
	@pending_tasks_count.setter
	def pending_tasks_count(self,pending_tasks_count):
		try :
			if not isinstance(pending_tasks_count,int):
				raise TypeError("pending_tasks_count must be set to int value")
			self._pending_tasks_count = pending_tasks_count
		except Exception as e :
			raise e

	'''
	Returns cloud profile client id.
	'''
	@property
	def cc_client_id(self):
		try:
			return self._cc_client_id
		except Exception as e :
			raise e
	'''
	Returns cloud profile client id.
	'''
	@cc_client_id.setter
	def cc_client_id(self,cc_client_id):
		try :
			if not isinstance(cc_client_id,str):
				raise TypeError("cc_client_id must be set to str value")
			self._cc_client_id = cc_client_id
		except Exception as e :
			raise e

	'''
	Count of agents deployed
	'''
	@property
	def agent_count(self):
		try:
			return self._agent_count
		except Exception as e :
			raise e
	'''
	Count of agents deployed
	'''
	@agent_count.setter
	def agent_count(self,agent_count):
		try :
			if not isinstance(agent_count,int):
				raise TypeError("agent_count must be set to int value")
			self._agent_count = agent_count
		except Exception as e :
			raise e

	'''
	True, if cloud identity authenticate is to be skipped
	'''
	@property
	def cc_profile_skip(self):
		try:
			return self._cc_profile_skip
		except Exception as e :
			raise e
	'''
	True, if cloud identity authenticate is to be skipped
	'''
	@cc_profile_skip.setter
	def cc_profile_skip(self,cc_profile_skip):
		try :
			if not isinstance(cc_profile_skip,bool):
				raise TypeError("cc_profile_skip must be set to bool value")
			self._cc_profile_skip = cc_profile_skip
		except Exception as e :
			raise e

	'''
	Indicates whether the tenant is light or not
	'''
	@property
	def is_light_tenant(self):
		try:
			return self._is_light_tenant
		except Exception as e :
			raise e
	'''
	Indicates whether the tenant is light or not
	'''
	@is_light_tenant.setter
	def is_light_tenant(self,is_light_tenant):
		try :
			if not isinstance(is_light_tenant,long):
				raise TypeError("is_light_tenant must be set to long value")
			self._is_light_tenant = is_light_tenant
		except Exception as e :
			raise e

	'''
	Returns cloud profile id.
	'''
	@property
	def cc_profile_id(self):
		try:
			return self._cc_profile_id
		except Exception as e :
			raise e
	'''
	Returns cloud profile id.
	'''
	@cc_profile_id.setter
	def cc_profile_id(self,cc_profile_id):
		try :
			if not isinstance(cc_profile_id,str):
				raise TypeError("cc_profile_id must be set to str value")
			self._cc_profile_id = cc_profile_id
		except Exception as e :
			raise e

	'''
	Cloud platform.
	'''
	@property
	def cloud_platform(self):
		try:
			return self._cloud_platform
		except Exception as e :
			raise e
	'''
	Cloud platform.
	'''
	@cloud_platform.setter
	def cloud_platform(self,cloud_platform):
		try :
			if not isinstance(cloud_platform,str):
				raise TypeError("cloud_platform must be set to str value")
			self._cloud_platform = cloud_platform
		except Exception as e :
			raise e

	'''
	Count of devices
	'''
	@property
	def device_count(self):
		try:
			return self._device_count
		except Exception as e :
			raise e
	'''
	Count of devices
	'''
	@device_count.setter
	def device_count(self,device_count):
		try :
			if not isinstance(device_count,int):
				raise TypeError("device_count must be set to int value")
			self._device_count = device_count
		except Exception as e :
			raise e

	'''
	Cloud deployment environment.
	'''
	@property
	def cloud_deployment_env(self):
		try:
			return self._cloud_deployment_env
		except Exception as e :
			raise e
	'''
	Cloud deployment environment.
	'''
	@cloud_deployment_env.setter
	def cloud_deployment_env(self,cloud_deployment_env):
		try :
			if not isinstance(cloud_deployment_env,str):
				raise TypeError("cloud_deployment_env must be set to str value")
			self._cloud_deployment_env = cloud_deployment_env
		except Exception as e :
			raise e

	'''
	True, if cloud profile is updated by user.
	'''
	@property
	def cc_profile(self):
		try:
			return self._cc_profile
		except Exception as e :
			raise e
	'''
	True, if cloud profile is updated by user.
	'''
	@cc_profile.setter
	def cc_profile(self,cc_profile):
		try :
			if not isinstance(cc_profile,bool):
				raise TypeError("cc_profile must be set to bool value")
			self._cc_profile = cc_profile
		except Exception as e :
			raise e

	'''
	Use this operation to modify message of the day.
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
		except Exception as e :
			raise e

	'''
	Use this operation to shutdown.
	'''
	@classmethod
	def shutdown(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"shutdown")
				return res
		except Exception as e :
			raise e

	'''
	Use this operation to get system status.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ui_profile_obj=ui_profile()
				response = ui_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to reboot.
	'''
	@classmethod
	def reboot(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"reboot")
				return res
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ui_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ui_profile_obj = ui_profile()
			option_ = options()
			option_._filter=filter_
			return ui_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ui_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ui_profile_obj = ui_profile()
			option_ = options()
			option_._count=True
			response = ui_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ui_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ui_profile_obj = ui_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ui_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ui_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ui_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ui_profile_responses, response, "ui_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ui_profile_response_array
				i=0
				error = [ui_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ui_profile_response_array
			i=0
			ui_profile_objs = [ui_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ui_profile'):
					for props in obj._ui_profile:
						result = service.payload_formatter.string_to_bulk_resource(ui_profile_response,self.__class__.__name__,props)
						ui_profile_objs[i] = result.ui_profile
						i=i+1
			return ui_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ui_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ui_profile_response(base_response):
	def __init__(self,length=1) :
		self.ui_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ui_profile= [ ui_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ui_profile_responses(base_response):
	def __init__(self,length=1) :
		self.ui_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ui_profile_response_array = [ ui_profile() for _ in range(length)]
