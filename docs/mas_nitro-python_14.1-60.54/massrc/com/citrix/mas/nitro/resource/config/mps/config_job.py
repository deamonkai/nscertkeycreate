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
from massrc.com.citrix.mas.nitro.resource.config.mps.variable_values import variable_values
from massrc.com.citrix.mas.nitro.resource.config.mps.configuration_template import configuration_template


'''
Configuration for Configuration Job resource
'''

class config_job(base_resource):
	_autoscale_groups=[]
	_execute_on_primary= ""
	_scheduleTimesEpoch= ""
	_credentials_required= ""
	_execute_on_secondary= ""
	_variables=[]
	_lastExecutedTimeEpoch= ""
	_job_username_enc= ""
	_timestamp= ""
	_sms_profiles= ""
	_status= ""
	_devices=[]
	_is_internal= ""
	_is_download_operation= ""
	_username= ""
	_execute_batch= ""
	_execute_password= ""
	_slack_profile= ""
	_device_groups=[]
	_executed_by= ""
	_execute_sequentially= ""
	_execute_username= ""
	_tz_offset= ""
	_on_error= ""
	_tenant_id= ""
	_device_family= ""
	_name= ""
	_tasklog_id= ""
	_lastExecutionStatus= ""
	_id= ""
	_template_info= ""
	_mail_profiles= ""
	_auto_rollback= ""
	_scheduleOptions= ""
	_scheduleType= ""
	_devices_completed_count= ""
	_preview_commands=[]
	_preview_rollback_commands=[]
	_devices_count= ""
	_execute_again= ""
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
			return "config_job"
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
			return "config_jobs"
		except Exception as e :
			raise e



	'''
	get Autoscale Group Array on which for which job is run
	'''
	@property
	def autoscale_groups(self) :
		try:
			return self._autoscale_groups
		except Exception as e :
			raise e
	'''
	set Autoscale Group Array on which for which job is run
	'''
	@autoscale_groups.setter
	def autoscale_groups(self,autoscale_groups) :
		try :
			if not isinstance(autoscale_groups,list):
				raise TypeError("autoscale_groups must be set to array of str value")
			for item in autoscale_groups :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._autoscale_groups = autoscale_groups
		except Exception as e :
			raise e


	'''
	get True if configuration run on HA primary instance
	'''
	@property
	def execute_on_primary(self) :
		try:
			return self._execute_on_primary
		except Exception as e :
			raise e
	'''
	set True if configuration run on HA primary instance
	'''
	@execute_on_primary.setter
	def execute_on_primary(self,execute_on_primary):
		try :
			if not isinstance(execute_on_primary,bool):
				raise TypeError("execute_on_primary must be set to bool value")
			self._execute_on_primary = execute_on_primary
		except Exception as e :
			raise e


	'''
	get Schedule time UTC epoch (string representation of 11 digit numbers).
	'''
	@property
	def scheduleTimesEpoch(self) :
		try:
			return self._scheduleTimesEpoch
		except Exception as e :
			raise e
	'''
	set Schedule time UTC epoch (string representation of 11 digit numbers).
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
	get True if username/password need to be asked before configuration template is to applied on devices
	'''
	@property
	def credentials_required(self) :
		try:
			return self._credentials_required
		except Exception as e :
			raise e
	'''
	set True if username/password need to be asked before configuration template is to applied on devices
	'''
	@credentials_required.setter
	def credentials_required(self,credentials_required):
		try :
			if not isinstance(credentials_required,bool):
				raise TypeError("credentials_required must be set to bool value")
			self._credentials_required = credentials_required
		except Exception as e :
			raise e


	'''
	get True if configuration run on HA secondary instance
	'''
	@property
	def execute_on_secondary(self) :
		try:
			return self._execute_on_secondary
		except Exception as e :
			raise e
	'''
	set True if configuration run on HA secondary instance
	'''
	@execute_on_secondary.setter
	def execute_on_secondary(self,execute_on_secondary):
		try :
			if not isinstance(execute_on_secondary,bool):
				raise TypeError("execute_on_secondary must be set to bool value")
			self._execute_on_secondary = execute_on_secondary
		except Exception as e :
			raise e


	'''
	get Values of Variables used in commands of the configuration template
	'''
	@property
	def variables(self) :
		try:
			return self._variables
		except Exception as e :
			raise e
	'''
	set Values of Variables used in commands of the configuration template
	'''
	@variables.setter
	def variables(self,variables) :
		try :
			if not isinstance(variables,list):
				raise TypeError("variables must be set to array of variable_values value")
			for item in variables :
				if not isinstance(item,variable_values):
					raise TypeError("item must be set to variable_values value")
			self._variables = variables
		except Exception as e :
			raise e


	'''
	get Schedule time epoch at which job was last executed.
	'''
	@property
	def lastExecutedTimeEpoch(self) :
		try:
			return self._lastExecutedTimeEpoch
		except Exception as e :
			raise e


	'''
	get Name of user who created configuration job
	'''
	@property
	def job_username_enc(self) :
		try:
			return self._job_username_enc
		except Exception as e :
			raise e


	'''
	get Time of Creation of Configuration Job
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e


	'''
	get Comma separated list of SMS profiles
	'''
	@property
	def sms_profiles(self) :
		try:
			return self._sms_profiles
		except Exception as e :
			raise e
	'''
	set Comma separated list of SMS profiles
	'''
	@sms_profiles.setter
	def sms_profiles(self,sms_profiles):
		try :
			if not isinstance(sms_profiles,str):
				raise TypeError("sms_profiles must be set to str value")
			self._sms_profiles = sms_profiles
		except Exception as e :
			raise e


	'''
	get Status of Config Job Started, In Progress, Completed, Failed, Aborted, Scheduled 
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of Config Job Started, In Progress, Completed, Failed, Aborted, Scheduled 
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get Device IP Address Array on which job is run
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e
	'''
	set Device IP Address Array on which job is run
	'''
	@devices.setter
	def devices(self,devices) :
		try :
			if not isinstance(devices,list):
				raise TypeError("devices must be set to array of str value")
			for item in devices :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._devices = devices
		except Exception as e :
			raise e


	'''
	get True if internal action config job
	'''
	@property
	def is_internal(self) :
		try:
			return self._is_internal
		except Exception as e :
			raise e
	'''
	set True if internal action config job
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
	get True if job download file from device
	'''
	@property
	def is_download_operation(self) :
		try:
			return self._is_download_operation
		except Exception as e :
			raise e
	'''
	set True if job download file from device
	'''
	@is_download_operation.setter
	def is_download_operation(self,is_download_operation):
		try :
			if not isinstance(is_download_operation,bool):
				raise TypeError("is_download_operation must be set to bool value")
			self._is_download_operation = is_download_operation
		except Exception as e :
			raise e


	'''
	get Name of user who created configuration job
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e


	'''
	get True if config job commands execute as batch
	'''
	@property
	def execute_batch(self) :
		try:
			return self._execute_batch
		except Exception as e :
			raise e
	'''
	set True if config job commands execute as batch
	'''
	@execute_batch.setter
	def execute_batch(self,execute_batch):
		try :
			if not isinstance(execute_batch,bool):
				raise TypeError("execute_batch must be set to bool value")
			self._execute_batch = execute_batch
		except Exception as e :
			raise e


	'''
	get Execute Password for job
	'''
	@property
	def execute_password(self) :
		try:
			return self._execute_password
		except Exception as e :
			raise e
	'''
	set Execute Password for job
	'''
	@execute_password.setter
	def execute_password(self,execute_password):
		try :
			if not isinstance(execute_password,str):
				raise TypeError("execute_password must be set to str value")
			self._execute_password = execute_password
		except Exception as e :
			raise e


	'''
	get name of the slack_profile
	'''
	@property
	def slack_profile(self) :
		try:
			return self._slack_profile
		except Exception as e :
			raise e
	'''
	set name of the slack_profile
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
	get Name of user who executed configuration job
	'''
	@property
	def executed_by(self) :
		try:
			return self._executed_by
		except Exception as e :
			raise e


	'''
	get True if configuration template is to be applied to devices sequentially
	'''
	@property
	def execute_sequentially(self) :
		try:
			return self._execute_sequentially
		except Exception as e :
			raise e
	'''
	set True if configuration template is to be applied to devices sequentially
	'''
	@execute_sequentially.setter
	def execute_sequentially(self,execute_sequentially):
		try :
			if not isinstance(execute_sequentially,bool):
				raise TypeError("execute_sequentially must be set to bool value")
			self._execute_sequentially = execute_sequentially
		except Exception as e :
			raise e


	'''
	get Execute User Name for job
	'''
	@property
	def execute_username(self) :
		try:
			return self._execute_username
		except Exception as e :
			raise e
	'''
	set Execute User Name for job
	'''
	@execute_username.setter
	def execute_username(self,execute_username):
		try :
			if not isinstance(execute_username,str):
				raise TypeError("execute_username must be set to str value")
			self._execute_username = execute_username
		except Exception as e :
			raise e


	'''
	get Time zone offset.
	'''
	@property
	def tz_offset(self) :
		try:
			return self._tz_offset
		except Exception as e :
			raise e
	'''
	set Time zone offset.
	'''
	@tz_offset.setter
	def tz_offset(self,tz_offset):
		try :
			if not isinstance(tz_offset,int):
				raise TypeError("tz_offset must be set to int value")
			self._tz_offset = tz_offset
		except Exception as e :
			raise e


	'''
	get Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT|ROLLBACK
	'''
	@property
	def on_error(self) :
		try:
			return self._on_error
		except Exception as e :
			raise e
	'''
	set Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT|ROLLBACK
	'''
	@on_error.setter
	def on_error(self,on_error):
		try :
			if not isinstance(on_error,str):
				raise TypeError("on_error must be set to str value")
			self._on_error = on_error
		except Exception as e :
			raise e


	'''
	get Tenant Id of the Config Jobs
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Family of Devices ns,sdx for which config job was executed
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Family of Devices ns,sdx for which config job was executed
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
		except Exception as e :
			raise e


	'''
	get Name of configuration job
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of configuration job
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
	get Task Log Id of the Config Job
	'''
	@property
	def tasklog_id(self) :
		try:
			return self._tasklog_id
		except Exception as e :
			raise e


	'''
	get Status of last Execution of Config Job - Started, In Progress, Completed, Failed, Aborted, Scheduled
	'''
	@property
	def lastExecutionStatus(self) :
		try:
			return self._lastExecutionStatus
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the configuration jobs
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the configuration jobs
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
	get Configuration Template to be executed/scheduled
	'''
	@property
	def template_info(self) :
		try:
			return self._template_info
		except Exception as e :
			raise e
	'''
	set Configuration Template to be executed/scheduled
	'''
	@template_info.setter
	def template_info(self,template_info):
		try :
			if not isinstance(template_info,configuration_template):
				raise TypeError("template_info must be set to configuration_template value")
			self._template_info = template_info
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
	get True if auto_rollback enable for config job
	'''
	@property
	def auto_rollback(self) :
		try:
			return self._auto_rollback
		except Exception as e :
			raise e
	'''
	set True if auto_rollback enable for config job
	'''
	@auto_rollback.setter
	def auto_rollback(self,auto_rollback):
		try :
			if not isinstance(auto_rollback,bool):
				raise TypeError("auto_rollback must be set to bool value")
			self._auto_rollback = auto_rollback
		except Exception as e :
			raise e


	'''
	get Comma separated schedule options specific day(s) of week, specific date(s) of month
	'''
	@property
	def scheduleOptions(self) :
		try:
			return self._scheduleOptions
		except Exception as e :
			raise e
	'''
	set Comma separated schedule options specific day(s) of week, specific date(s) of month
	'''
	@scheduleOptions.setter
	def scheduleOptions(self,scheduleOptions):
		try :
			if not isinstance(scheduleOptions,str):
				raise TypeError("scheduleOptions must be set to str value")
			self._scheduleOptions = scheduleOptions
		except Exception as e :
			raise e


	'''
	get Schedule Type fixed, daily, weekly, monthly of Configuration Template that is scheduled
	'''
	@property
	def scheduleType(self) :
		try:
			return self._scheduleType
		except Exception as e :
			raise e
	'''
	set Schedule Type fixed, daily, weekly, monthly of Configuration Template that is scheduled
	'''
	@scheduleType.setter
	def scheduleType(self,scheduleType):
		try :
			if not isinstance(scheduleType,str):
				raise TypeError("scheduleType must be set to str value")
			self._scheduleType = scheduleType
		except Exception as e :
			raise e

	'''
	Number of Devices on which commands execution completed
	'''
	@property
	def devices_completed_count(self):
		try:
			return self._devices_completed_count
		except Exception as e :
			raise e

	'''
	Preview of list of commands
	'''
	@property
	def preview_commands(self) :
		try:
			return self._preview_commands
		except Exception as e :
			raise e

	'''
	Preview of list of rollback commands
	'''
	@property
	def preview_rollback_commands(self) :
		try:
			return self._preview_rollback_commands
		except Exception as e :
			raise e

	'''
	Number of Devices on which commands executed
	'''
	@property
	def devices_count(self):
		try:
			return self._devices_count
		except Exception as e :
			raise e

	'''
	True if Execute again the config job
	'''
	@property
	def execute_again(self):
		try:
			return self._execute_again
		except Exception as e :
			raise e
	'''
	True if Execute again the config job
	'''
	@execute_again.setter
	def execute_again(self,execute_again):
		try :
			if not isinstance(execute_again,bool):
				raise TypeError("execute_again must be set to bool value")
			self._execute_again = execute_again
		except Exception as e :
			raise e

	'''
	Use this operation to save config job.
	'''
	@classmethod
	def save(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"save")
				return res
			else : 
				config_job_obj= config_job()
				return cls.perform_operation_bulk_request(service,"save",resource,config_job_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get config job.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				config_job_obj=config_job()
				response = config_job_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to run config job.
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
				config_job_obj= config_job()
				return cls.perform_operation_bulk_request(service,resource,config_job_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to update config job.
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
				config_job_obj=config_job()
				return cls.update_bulk_request(client,resource,config_job_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete config job.
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
					config_job_obj=config_job()
					return cls.delete_bulk_request(client,resource,config_job_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of config_job resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			config_job_obj = config_job()
			option_ = options()
			option_._filter=filter_
			return config_job_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the config_job resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			config_job_obj = config_job()
			option_ = options()
			option_._count=True
			response = config_job_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of config_job resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			config_job_obj = config_job()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = config_job_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(config_job_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.config_job
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(config_job_responses, response, "config_job_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.config_job_response_array
				i=0
				error = [config_job() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.config_job_response_array
			i=0
			config_job_objs = [config_job() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_config_job'):
					for props in obj._config_job:
						result = service.payload_formatter.string_to_bulk_resource(config_job_response,self.__class__.__name__,props)
						config_job_objs[i] = result.config_job
						i=i+1
			return config_job_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(config_job,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class config_job_response(base_response):
	def __init__(self,length=1) :
		self.config_job= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.config_job= [ config_job() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class config_job_responses(base_response):
	def __init__(self,length=1) :
		self.config_job_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.config_job_response_array = [ config_job() for _ in range(length)]
