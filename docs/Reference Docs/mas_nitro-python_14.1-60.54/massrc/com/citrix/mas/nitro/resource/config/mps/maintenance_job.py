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
Configuration for Maintenance Job resource
'''

class maintenance_job(base_resource):
	_device_family= ""
	_name= ""
	_tasklog_id= ""
	_parent_id= ""
	_status= ""
	_timestamp= ""
	_tenant_id= ""
	_type= ""
	_maintenance_job_username= ""
	_scheduleTimesEpoch= ""
	_task_name= ""
	_slack_profile= ""
	_username= ""
	_mail_profiles= ""
	_id= ""
	_devices=[]
	_devices_completed_count= ""
	_additional_info=[]
	_failed_devices=[]
	_attached_maintenance_job= ""
	_devices_count= ""
	_failed_message=[]
	_scheduleTime= ""
	_device_groups=[]
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
			return "maintenance_job"
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
			return "maintenance_jobs"
		except Exception as e :
			raise e



	'''
	get Family of Devices for which config job was executed
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Family of Devices for which config job was executed
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
	get Name of maintenance job
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of maintenance job
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
	set Task Log Id of the Config Job
	'''
	@tasklog_id.setter
	def tasklog_id(self,tasklog_id):
		try :
			if not isinstance(tasklog_id,str):
				raise TypeError("tasklog_id must be set to str value")
			self._tasklog_id = tasklog_id
		except Exception as e :
			raise e


	'''
	get Parent Id of maintenance job.
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set Parent Id of maintenance job.
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
	get Status of maintenance Job Started, In Progress, Scheduled, Failed, Completed
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e


	'''
	get Time of Creation of Maintenance Job
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
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
	get Device type for selected device_family
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Device type for selected device_family
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
	get Name of user who created maintenance job
	'''
	@property
	def maintenance_job_username(self) :
		try:
			return self._maintenance_job_username
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
	get task name of maintenance job.
	'''
	@property
	def task_name(self) :
		try:
			return self._task_name
		except Exception as e :
			raise e
	'''
	set task name of maintenance job.
	'''
	@task_name.setter
	def task_name(self,task_name):
		try :
			if not isinstance(task_name,str):
				raise TypeError("task_name must be set to str value")
			self._task_name = task_name
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
	get Name of user who created maintenance job
	'''
	@property
	def username(self) :
		try:
			return self._username
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
	get Id is system generated key for all the maintenance jobs
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the maintenance jobs
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
	Device IP Address Array on which job is run
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e
	'''
	Device IP Address Array on which job is run
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
	Devices Completed Count
	'''
	@property
	def devices_completed_count(self):
		try:
			return self._devices_completed_count
		except Exception as e :
			raise e

	'''
	Additional info Array
	'''
	@property
	def additional_info(self) :
		try:
			return self._additional_info
		except Exception as e :
			raise e
	'''
	Additional info Array
	'''
	@additional_info.setter
	def additional_info(self,additional_info) :
		try :
			if not isinstance(additional_info,list):
				raise TypeError("additional_info must be set to array of str value")
			for item in additional_info :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._additional_info = additional_info
		except Exception as e :
			raise e

	'''
	filter failed_devices:true to get list of failed devices as array in this property.
	'''
	@property
	def failed_devices(self) :
		try:
			return self._failed_devices
		except Exception as e :
			raise e
	'''
	filter failed_devices:true to get list of failed devices as array in this property.
	'''
	@failed_devices.setter
	def failed_devices(self,failed_devices) :
		try :
			if not isinstance(failed_devices,list):
				raise TypeError("failed_devices must be set to array of str value")
			for item in failed_devices :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._failed_devices = failed_devices
		except Exception as e :
			raise e

	'''
	Attached maintenance job
	'''
	@property
	def attached_maintenance_job(self):
		try:
			return self._attached_maintenance_job
		except Exception as e :
			raise e
	'''
	Attached maintenance job
	'''
	@attached_maintenance_job.setter
	def attached_maintenance_job(self,attached_maintenance_job):
		try :
			if not isinstance(attached_maintenance_job,str):
				raise TypeError("attached_maintenance_job must be set to str value")
			self._attached_maintenance_job = attached_maintenance_job
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
	Comma separated instances error details
	'''
	@property
	def failed_message(self) :
		try:
			return self._failed_message
		except Exception as e :
			raise e
	'''
	Comma separated instances error details
	'''
	@failed_message.setter
	def failed_message(self,failed_message) :
		try :
			if not isinstance(failed_message,list):
				raise TypeError("failed_message must be set to array of str value")
			for item in failed_message :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._failed_message = failed_message
		except Exception as e :
			raise e

	'''
	Comma separated times of the day(DD:HH:MM) on which Configuration Template is scheduled
	'''
	@property
	def scheduleTime(self):
		try:
			return self._scheduleTime
		except Exception as e :
			raise e
	'''
	Comma separated times of the day(DD:HH:MM) on which Configuration Template is scheduled
	'''
	@scheduleTime.setter
	def scheduleTime(self,scheduleTime):
		try :
			if not isinstance(scheduleTime,str):
				raise TypeError("scheduleTime must be set to str value")
			self._scheduleTime = scheduleTime
		except Exception as e :
			raise e

	'''
	Device Group Array on which for which job is run
	'''
	@property
	def device_groups(self) :
		try:
			return self._device_groups
		except Exception as e :
			raise e
	'''
	Device Group Array on which for which job is run
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
	Use this operation to get config job.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				maintenance_job_obj=maintenance_job()
				response = maintenance_job_obj.get_resources(client,option_)
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
				maintenance_job_obj= maintenance_job()
				return cls.perform_operation_bulk_request(service,resource,maintenance_job_obj)
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
				maintenance_job_obj=maintenance_job()
				return cls.update_bulk_request(client,resource,maintenance_job_obj)
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
					maintenance_job_obj=maintenance_job()
					return cls.delete_bulk_request(client,resource,maintenance_job_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of maintenance_job resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			maintenance_job_obj = maintenance_job()
			option_ = options()
			option_._filter=filter_
			return maintenance_job_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the maintenance_job resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			maintenance_job_obj = maintenance_job()
			option_ = options()
			option_._count=True
			response = maintenance_job_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of maintenance_job resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			maintenance_job_obj = maintenance_job()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = maintenance_job_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(maintenance_job_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.maintenance_job
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(maintenance_job_responses, response, "maintenance_job_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.maintenance_job_response_array
				i=0
				error = [maintenance_job() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.maintenance_job_response_array
			i=0
			maintenance_job_objs = [maintenance_job() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_maintenance_job'):
					for props in obj._maintenance_job:
						result = service.payload_formatter.string_to_bulk_resource(maintenance_job_response,self.__class__.__name__,props)
						maintenance_job_objs[i] = result.maintenance_job
						i=i+1
			return maintenance_job_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(maintenance_job,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class maintenance_job_response(base_response):
	def __init__(self,length=1) :
		self.maintenance_job= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.maintenance_job= [ maintenance_job() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class maintenance_job_responses(base_response):
	def __init__(self,length=1) :
		self.maintenance_job_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.maintenance_job_response_array = [ maintenance_job() for _ in range(length)]
