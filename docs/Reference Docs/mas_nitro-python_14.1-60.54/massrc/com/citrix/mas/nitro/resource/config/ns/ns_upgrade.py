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
Configuration for NetScaler Upgrade resource
'''

class ns_upgrade(base_resource):
	_type= ""
	_tasklog_id= ""
	_mode= ""
	_mail_profiles= ""
	_is_skip_upload_image= ""
	_do_backup= ""
	_adc_cloud_image_version= ""
	_is_pre_post_upgrade_pre_failover_script_same= ""
	_ha_two_phase_upgrade= ""
	_name= ""
	_do_cleanup= ""
	_is_post_upgrade_pre_failover_script_selected= ""
	_scheduleTimesEpoch2= ""
	_id= ""
	_image_name= ""
	_adc_cloud_image_id= ""
	_scheduleTimesEpoch= ""
	_device_groups=[]
	_post_upgrade_script= ""
	_pre_upgrade_script= ""
	_saveconfig_enabled= ""
	_is_post_upgrade_script_selected= ""
	_slack_profile= ""
	_doc_file= ""
	_is_issu_enabled= ""
	_is_remote_download= ""
	_default_configdiff_template=[]
	_second_failover_enabled= ""
	_issu_migration_timeout= ""
	_is_pre_post_upgrade_script_same= ""
	_is_pre_upgrade_script_selected= ""
	_act_id= ""
	_ns_ip_address_arr=[]
	_delay_ha_failover= ""
	_cleanup_unsupported_policy= ""
	_disable_build_image_upload_to_primary= ""
	_scheduleId= ""
	_ha_node2_devices=[]
	_post_upgrade_pre_failover_script= ""
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
			return "ns_upgrade"
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
			return "ns_upgrades"
		except Exception as e :
			raise e



	'''
	get Device type for NS device family
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Device type for NS device family
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
	get Task Log Id of the Config Job
	'''
	@property
	def tasklog_id(self) :
		try:
			return self._tasklog_id
		except Exception as e :
			raise e


	'''
	get Provide 0 for uploading and installing the image, 1 for only uploading the image, 2 for only installing the image and 3 for upgrade pre-validation
	'''
	@property
	def mode(self) :
		try:
			return self._mode
		except Exception as e :
			raise e
	'''
	set Provide 0 for uploading and installing the image, 1 for only uploading the image, 2 for only installing the image and 3 for upgrade pre-validation
	'''
	@mode.setter
	def mode(self,mode):
		try :
			if not isinstance(mode,int):
				raise TypeError("mode must be set to int value")
			self._mode = mode
		except Exception as e :
			raise e


	'''
	get Comma separated list of Mail profiles
	'''
	@property
	def mail_profiles(self) :
		try:
			return self._mail_profiles
		except Exception as e :
			raise e
	'''
	set Comma separated list of Mail profiles
	'''
	@mail_profiles.setter
	def mail_profiles(self,mail_profiles):
		try :
			if not isinstance(mail_profiles,str):
				raise TypeError("mail_profiles must be set to str value")
			self._mail_profiles = mail_profiles
		except Exception as e :
			raise e


	'''
	get True, if skip upload build image
	'''
	@property
	def is_skip_upload_image(self) :
		try:
			return self._is_skip_upload_image
		except Exception as e :
			raise e
	'''
	set True, if skip upload build image
	'''
	@is_skip_upload_image.setter
	def is_skip_upload_image(self,is_skip_upload_image):
		try :
			if not isinstance(is_skip_upload_image,bool):
				raise TypeError("is_skip_upload_image must be set to bool value")
			self._is_skip_upload_image = is_skip_upload_image
		except Exception as e :
			raise e


	'''
	get True, if user wants to take backup before ns upgrade
	'''
	@property
	def do_backup(self) :
		try:
			return self._do_backup
		except Exception as e :
			raise e
	'''
	set True, if user wants to take backup before ns upgrade
	'''
	@do_backup.setter
	def do_backup(self,do_backup):
		try :
			if not isinstance(do_backup,bool):
				raise TypeError("do_backup must be set to bool value")
			self._do_backup = do_backup
		except Exception as e :
			raise e


	'''
	get NetScaler Cloud Image Version to which AutoScaleGroup(s) is/are to be upgraded
	'''
	@property
	def adc_cloud_image_version(self) :
		try:
			return self._adc_cloud_image_version
		except Exception as e :
			raise e
	'''
	set NetScaler Cloud Image Version to which AutoScaleGroup(s) is/are to be upgraded
	'''
	@adc_cloud_image_version.setter
	def adc_cloud_image_version(self,adc_cloud_image_version):
		try :
			if not isinstance(adc_cloud_image_version,str):
				raise TypeError("adc_cloud_image_version must be set to str value")
			self._adc_cloud_image_version = adc_cloud_image_version
		except Exception as e :
			raise e


	'''
	get True, if pre and post upgrade pre failover custom scripts are same
	'''
	@property
	def is_pre_post_upgrade_pre_failover_script_same(self) :
		try:
			return self._is_pre_post_upgrade_pre_failover_script_same
		except Exception as e :
			raise e
	'''
	set True, if pre and post upgrade pre failover custom scripts are same
	'''
	@is_pre_post_upgrade_pre_failover_script_same.setter
	def is_pre_post_upgrade_pre_failover_script_same(self,is_pre_post_upgrade_pre_failover_script_same):
		try :
			if not isinstance(is_pre_post_upgrade_pre_failover_script_same,bool):
				raise TypeError("is_pre_post_upgrade_pre_failover_script_same must be set to bool value")
			self._is_pre_post_upgrade_pre_failover_script_same = is_pre_post_upgrade_pre_failover_script_same
		except Exception as e :
			raise e


	'''
	get True, if user wants to upgarde ha in two phases or steps
	'''
	@property
	def ha_two_phase_upgrade(self) :
		try:
			return self._ha_two_phase_upgrade
		except Exception as e :
			raise e
	'''
	set True, if user wants to upgarde ha in two phases or steps
	'''
	@ha_two_phase_upgrade.setter
	def ha_two_phase_upgrade(self,ha_two_phase_upgrade):
		try :
			if not isinstance(ha_two_phase_upgrade,bool):
				raise TypeError("ha_two_phase_upgrade must be set to bool value")
			self._ha_two_phase_upgrade = ha_two_phase_upgrade
		except Exception as e :
			raise e


	'''
	get Name of upgrade
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of upgrade
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
	get True, if user wants to clean the image files once upgrade is completed successfully
	'''
	@property
	def do_cleanup(self) :
		try:
			return self._do_cleanup
		except Exception as e :
			raise e
	'''
	set True, if user wants to clean the image files once upgrade is completed successfully
	'''
	@do_cleanup.setter
	def do_cleanup(self,do_cleanup):
		try :
			if not isinstance(do_cleanup,bool):
				raise TypeError("do_cleanup must be set to bool value")
			self._do_cleanup = do_cleanup
		except Exception as e :
			raise e


	'''
	get True, if post upgrade pre failover custom script is selected
	'''
	@property
	def is_post_upgrade_pre_failover_script_selected(self) :
		try:
			return self._is_post_upgrade_pre_failover_script_selected
		except Exception as e :
			raise e
	'''
	set True, if post upgrade pre failover custom script is selected
	'''
	@is_post_upgrade_pre_failover_script_selected.setter
	def is_post_upgrade_pre_failover_script_selected(self,is_post_upgrade_pre_failover_script_selected):
		try :
			if not isinstance(is_post_upgrade_pre_failover_script_selected,bool):
				raise TypeError("is_post_upgrade_pre_failover_script_selected must be set to bool value")
			self._is_post_upgrade_pre_failover_script_selected = is_post_upgrade_pre_failover_script_selected
		except Exception as e :
			raise e


	'''
	get Schedule time epoch for ha primary node (string representation of 11 digit numbers).
	'''
	@property
	def scheduleTimesEpoch2(self) :
		try:
			return self._scheduleTimesEpoch2
		except Exception as e :
			raise e
	'''
	set Schedule time epoch for ha primary node (string representation of 11 digit numbers).
	'''
	@scheduleTimesEpoch2.setter
	def scheduleTimesEpoch2(self,scheduleTimesEpoch2):
		try :
			if not isinstance(scheduleTimesEpoch2,str):
				raise TypeError("scheduleTimesEpoch2 must be set to str value")
			self._scheduleTimesEpoch2 = scheduleTimesEpoch2
		except Exception as e :
			raise e


	'''
	get Id is maintenance job id
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is maintenance job id
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
	get image_name
	'''
	@property
	def image_name(self) :
		try:
			return self._image_name
		except Exception as e :
			raise e
	'''
	set image_name
	'''
	@image_name.setter
	def image_name(self,image_name):
		try :
			if not isinstance(image_name,str):
				raise TypeError("image_name must be set to str value")
			self._image_name = image_name
		except Exception as e :
			raise e


	'''
	get NetScaler Cloud Image ID to which AutoScaleGroup(s) is/are to be upgraded
	'''
	@property
	def adc_cloud_image_id(self) :
		try:
			return self._adc_cloud_image_id
		except Exception as e :
			raise e
	'''
	set NetScaler Cloud Image ID to which AutoScaleGroup(s) is/are to be upgraded
	'''
	@adc_cloud_image_id.setter
	def adc_cloud_image_id(self,adc_cloud_image_id):
		try :
			if not isinstance(adc_cloud_image_id,str):
				raise TypeError("adc_cloud_image_id must be set to str value")
			self._adc_cloud_image_id = adc_cloud_image_id
		except Exception as e :
			raise e


	'''
	get Schedule time epoch (string representation of 11 digit numbers).
	'''
	@property
	def scheduleTimesEpoch(self) :
		try:
			return self._scheduleTimesEpoch
		except Exception as e :
			raise e
	'''
	set Schedule time epoch (string representation of 11 digit numbers).
	'''
	@scheduleTimesEpoch.setter
	def scheduleTimesEpoch(self,scheduleTimesEpoch):
		try :
			if not isinstance(scheduleTimesEpoch,str):
				raise TypeError("scheduleTimesEpoch must be set to str value")
			self._scheduleTimesEpoch = scheduleTimesEpoch
		except Exception as e :
			raise e


	'''
	get Device Group Array on which for which job is run
	'''
	@property
	def device_groups(self) :
		try:
			return self._device_groups
		except Exception as e :
			raise e
	'''
	set Device Group Array on which for which job is run
	'''
	@device_groups.setter
	def device_groups(self,device_groups) :
		try :
			if not isinstance(device_groups,list):
				raise TypeError("device_groups must be set to array of str value")
			for item in device_groups :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._device_groups = device_groups
		except Exception as e :
			raise e


	'''
	get Name of post upgrade script file
	'''
	@property
	def post_upgrade_script(self) :
		try:
			return self._post_upgrade_script
		except Exception as e :
			raise e
	'''
	set Name of post upgrade script file
	'''
	@post_upgrade_script.setter
	def post_upgrade_script(self,post_upgrade_script):
		try :
			if not isinstance(post_upgrade_script,str):
				raise TypeError("post_upgrade_script must be set to str value")
			self._post_upgrade_script = post_upgrade_script
		except Exception as e :
			raise e


	'''
	get Name of pre upgrade script file
	'''
	@property
	def pre_upgrade_script(self) :
		try:
			return self._pre_upgrade_script
		except Exception as e :
			raise e
	'''
	set Name of pre upgrade script file
	'''
	@pre_upgrade_script.setter
	def pre_upgrade_script(self,pre_upgrade_script):
		try :
			if not isinstance(pre_upgrade_script,str):
				raise TypeError("pre_upgrade_script must be set to str value")
			self._pre_upgrade_script = pre_upgrade_script
		except Exception as e :
			raise e


	'''
	get True, if save config before upgrade
	'''
	@property
	def saveconfig_enabled(self) :
		try:
			return self._saveconfig_enabled
		except Exception as e :
			raise e
	'''
	set True, if save config before upgrade
	'''
	@saveconfig_enabled.setter
	def saveconfig_enabled(self,saveconfig_enabled):
		try :
			if not isinstance(saveconfig_enabled,bool):
				raise TypeError("saveconfig_enabled must be set to bool value")
			self._saveconfig_enabled = saveconfig_enabled
		except Exception as e :
			raise e


	'''
	get True, if post upgrade custom script is selected
	'''
	@property
	def is_post_upgrade_script_selected(self) :
		try:
			return self._is_post_upgrade_script_selected
		except Exception as e :
			raise e
	'''
	set True, if post upgrade custom script is selected
	'''
	@is_post_upgrade_script_selected.setter
	def is_post_upgrade_script_selected(self,is_post_upgrade_script_selected):
		try :
			if not isinstance(is_post_upgrade_script_selected,bool):
				raise TypeError("is_post_upgrade_script_selected must be set to bool value")
			self._is_post_upgrade_script_selected = is_post_upgrade_script_selected
		except Exception as e :
			raise e


	'''
	get Slack profile
	'''
	@property
	def slack_profile(self) :
		try:
			return self._slack_profile
		except Exception as e :
			raise e
	'''
	set Slack profile
	'''
	@slack_profile.setter
	def slack_profile(self,slack_profile):
		try :
			if not isinstance(slack_profile,str):
				raise TypeError("slack_profile must be set to str value")
			self._slack_profile = slack_profile
		except Exception as e :
			raise e


	'''
	get Documentation File Name
	'''
	@property
	def doc_file(self) :
		try:
			return self._doc_file
		except Exception as e :
			raise e
	'''
	set Documentation File Name
	'''
	@doc_file.setter
	def doc_file(self,doc_file):
		try :
			if not isinstance(doc_file,str):
				raise TypeError("doc_file must be set to str value")
			self._doc_file = doc_file
		except Exception as e :
			raise e


	'''
	get True, if ISSU is enabled
	'''
	@property
	def is_issu_enabled(self) :
		try:
			return self._is_issu_enabled
		except Exception as e :
			raise e
	'''
	set True, if ISSU is enabled
	'''
	@is_issu_enabled.setter
	def is_issu_enabled(self,is_issu_enabled):
		try :
			if not isinstance(is_issu_enabled,bool):
				raise TypeError("is_issu_enabled must be set to bool value")
			self._is_issu_enabled = is_issu_enabled
		except Exception as e :
			raise e


	'''
	get True if upgrade is remote download instead of direct upload from NetScaler Console
	'''
	@property
	def is_remote_download(self) :
		try:
			return self._is_remote_download
		except Exception as e :
			raise e
	'''
	set True if upgrade is remote download instead of direct upload from NetScaler Console
	'''
	@is_remote_download.setter
	def is_remote_download(self,is_remote_download):
		try :
			if not isinstance(is_remote_download,bool):
				raise TypeError("is_remote_download must be set to bool value")
			self._is_remote_download = is_remote_download
		except Exception as e :
			raise e


	'''
	get List of default upgrade templates
	'''
	@property
	def default_configdiff_template(self) :
		try:
			return self._default_configdiff_template
		except Exception as e :
			raise e
	'''
	set List of default upgrade templates
	'''
	@default_configdiff_template.setter
	def default_configdiff_template(self,default_configdiff_template) :
		try :
			if not isinstance(default_configdiff_template,list):
				raise TypeError("default_configdiff_template must be set to array of str value")
			for item in default_configdiff_template :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._default_configdiff_template = default_configdiff_template
		except Exception as e :
			raise e


	'''
	get True, if second failover for HA upgrade is enabled
	'''
	@property
	def second_failover_enabled(self) :
		try:
			return self._second_failover_enabled
		except Exception as e :
			raise e
	'''
	set True, if second failover for HA upgrade is enabled
	'''
	@second_failover_enabled.setter
	def second_failover_enabled(self,second_failover_enabled):
		try :
			if not isinstance(second_failover_enabled,bool):
				raise TypeError("second_failover_enabled must be set to bool value")
			self._second_failover_enabled = second_failover_enabled
		except Exception as e :
			raise e


	'''
	get ISSU migration timeout value in minutes
	'''
	@property
	def issu_migration_timeout(self) :
		try:
			return self._issu_migration_timeout
		except Exception as e :
			raise e
	'''
	set ISSU migration timeout value in minutes
	'''
	@issu_migration_timeout.setter
	def issu_migration_timeout(self,issu_migration_timeout):
		try :
			if not isinstance(issu_migration_timeout,int):
				raise TypeError("issu_migration_timeout must be set to int value")
			self._issu_migration_timeout = issu_migration_timeout
		except Exception as e :
			raise e


	'''
	get True, if pre and post upgrade post failover custom scripts are same
	'''
	@property
	def is_pre_post_upgrade_script_same(self) :
		try:
			return self._is_pre_post_upgrade_script_same
		except Exception as e :
			raise e
	'''
	set True, if pre and post upgrade post failover custom scripts are same
	'''
	@is_pre_post_upgrade_script_same.setter
	def is_pre_post_upgrade_script_same(self,is_pre_post_upgrade_script_same):
		try :
			if not isinstance(is_pre_post_upgrade_script_same,bool):
				raise TypeError("is_pre_post_upgrade_script_same must be set to bool value")
			self._is_pre_post_upgrade_script_same = is_pre_post_upgrade_script_same
		except Exception as e :
			raise e


	'''
	get True, if pre upgrade custom script is selected
	'''
	@property
	def is_pre_upgrade_script_selected(self) :
		try:
			return self._is_pre_upgrade_script_selected
		except Exception as e :
			raise e
	'''
	set True, if pre upgrade custom script is selected
	'''
	@is_pre_upgrade_script_selected.setter
	def is_pre_upgrade_script_selected(self,is_pre_upgrade_script_selected):
		try :
			if not isinstance(is_pre_upgrade_script_selected,bool):
				raise TypeError("is_pre_upgrade_script_selected must be set to bool value")
			self._is_pre_upgrade_script_selected = is_pre_upgrade_script_selected
		except Exception as e :
			raise e


	'''
	get Activity Id
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e


	'''
	get List of NetScaler IP Address
	'''
	@property
	def ns_ip_address_arr(self) :
		try:
			return self._ns_ip_address_arr
		except Exception as e :
			raise e
	'''
	set List of NetScaler IP Address
	'''
	@ns_ip_address_arr.setter
	def ns_ip_address_arr(self,ns_ip_address_arr) :
		try :
			if not isinstance(ns_ip_address_arr,list):
				raise TypeError("ns_ip_address_arr must be set to array of str value")
			for item in ns_ip_address_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_ip_address_arr = ns_ip_address_arr
		except Exception as e :
			raise e


	'''
	get True, if detal two phase HA failover
	'''
	@property
	def delay_ha_failover(self) :
		try:
			return self._delay_ha_failover
		except Exception as e :
			raise e
	'''
	set True, if detal two phase HA failover
	'''
	@delay_ha_failover.setter
	def delay_ha_failover(self,delay_ha_failover):
		try :
			if not isinstance(delay_ha_failover,bool):
				raise TypeError("delay_ha_failover must be set to bool value")
			self._delay_ha_failover = delay_ha_failover
		except Exception as e :
			raise e


	'''
	get True, if user selected to delete unsupported policies after upgrade.
	'''
	@property
	def cleanup_unsupported_policy(self) :
		try:
			return self._cleanup_unsupported_policy
		except Exception as e :
			raise e
	'''
	set True, if user selected to delete unsupported policies after upgrade.
	'''
	@cleanup_unsupported_policy.setter
	def cleanup_unsupported_policy(self,cleanup_unsupported_policy):
		try :
			if not isinstance(cleanup_unsupported_policy,bool):
				raise TypeError("cleanup_unsupported_policy must be set to bool value")
			self._cleanup_unsupported_policy = cleanup_unsupported_policy
		except Exception as e :
			raise e


	'''
	get True, if disable build image upload to HA primary device
	'''
	@property
	def disable_build_image_upload_to_primary(self) :
		try:
			return self._disable_build_image_upload_to_primary
		except Exception as e :
			raise e
	'''
	set True, if disable build image upload to HA primary device
	'''
	@disable_build_image_upload_to_primary.setter
	def disable_build_image_upload_to_primary(self,disable_build_image_upload_to_primary):
		try :
			if not isinstance(disable_build_image_upload_to_primary,bool):
				raise TypeError("disable_build_image_upload_to_primary must be set to bool value")
			self._disable_build_image_upload_to_primary = disable_build_image_upload_to_primary
		except Exception as e :
			raise e


	'''
	get scheduleId is used to refer maintenaince schedule task
	'''
	@property
	def scheduleId(self) :
		try:
			return self._scheduleId
		except Exception as e :
			raise e
	'''
	set scheduleId is used to refer maintenaince schedule task
	'''
	@scheduleId.setter
	def scheduleId(self,scheduleId):
		try :
			if not isinstance(scheduleId,str):
				raise TypeError("scheduleId must be set to str value")
			self._scheduleId = scheduleId
		except Exception as e :
			raise e


	'''
	get List of HA NetScaler IP Address upgrade in second phase
	'''
	@property
	def ha_node2_devices(self) :
		try:
			return self._ha_node2_devices
		except Exception as e :
			raise e
	'''
	set List of HA NetScaler IP Address upgrade in second phase
	'''
	@ha_node2_devices.setter
	def ha_node2_devices(self,ha_node2_devices) :
		try :
			if not isinstance(ha_node2_devices,list):
				raise TypeError("ha_node2_devices must be set to array of str value")
			for item in ha_node2_devices :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ha_node2_devices = ha_node2_devices
		except Exception as e :
			raise e


	'''
	get Name of post upgrade pre failover script file
	'''
	@property
	def post_upgrade_pre_failover_script(self) :
		try:
			return self._post_upgrade_pre_failover_script
		except Exception as e :
			raise e
	'''
	set Name of post upgrade pre failover script file
	'''
	@post_upgrade_pre_failover_script.setter
	def post_upgrade_pre_failover_script(self,post_upgrade_pre_failover_script):
		try :
			if not isinstance(post_upgrade_pre_failover_script,str):
				raise TypeError("post_upgrade_pre_failover_script must be set to str value")
			self._post_upgrade_pre_failover_script = post_upgrade_pre_failover_script
		except Exception as e :
			raise e

	'''
	Use this operation to update upgrade.
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
				ns_upgrade_obj=ns_upgrade()
				return cls.update_bulk_request(client,resource,ns_upgrade_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get ns upgrade.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_upgrade_obj=ns_upgrade()
				response = ns_upgrade_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to upgrade NetScaler.
	'''
	@classmethod
	def upgrade(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"upgrade")
				return res
			else : 
				ns_upgrade_obj= ns_upgrade()
				return cls.perform_operation_bulk_request(service,"upgrade",resource,ns_upgrade_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_upgrade resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_upgrade_obj = ns_upgrade()
			option_ = options()
			option_._filter=filter_
			return ns_upgrade_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_upgrade resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_upgrade_obj = ns_upgrade()
			option_ = options()
			option_._count=True
			response = ns_upgrade_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_upgrade resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_upgrade_obj = ns_upgrade()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_upgrade_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_upgrade_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_upgrade
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_upgrade_responses, response, "ns_upgrade_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_upgrade_response_array
				i=0
				error = [ns_upgrade() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_upgrade_response_array
			i=0
			ns_upgrade_objs = [ns_upgrade() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_upgrade'):
					for props in obj._ns_upgrade:
						result = service.payload_formatter.string_to_bulk_resource(ns_upgrade_response,self.__class__.__name__,props)
						ns_upgrade_objs[i] = result.ns_upgrade
						i=i+1
			return ns_upgrade_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_upgrade,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_upgrade_response(base_response):
	def __init__(self,length=1) :
		self.ns_upgrade= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_upgrade= [ ns_upgrade() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_upgrade_responses(base_response):
	def __init__(self,length=1) :
		self.ns_upgrade_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_upgrade_response_array = [ ns_upgrade() for _ in range(length)]
