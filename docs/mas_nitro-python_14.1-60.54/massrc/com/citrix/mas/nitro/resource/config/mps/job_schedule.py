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
from massrc.com.citrix.mas.nitro.resource.config.mps.property_map import property_map


'''
Configuration for Job Schedule Detail resource
'''

class job_schedule(base_resource):
	_misfire_instruction= ""
	_next_scheduletime= ""
	_trigger_type= ""
	_daily_time= ""
	_node_id= ""
	_scheduler_name_org= ""
	_duration= ""
	_tenant_id= ""
	_expiry= ""
	_jobdata_map=[]
	_status= ""
	_weekday_time= ""
	_timezoneOffset= ""
	_scheduler_name= ""
	_recur_hr= ""
	_feature_origin= ""
	_module_name= ""
	_job_schedule_name= ""
	_id= ""
	_monthday_time= ""
	_description= ""
	_job_name= ""
	_recur_min= ""
	_start= ""
	_recurrenceType= ""
	_job_description= ""
	_job_type= ""
	_recurrenceOptions= ""
	_recurrenceTimes= ""
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
			return "job_schedule"
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
			return "job_schedules"
		except Exception as e :
			raise e



	'''
	get Misfire Instruction
	'''
	@property
	def misfire_instruction(self) :
		try:
			return self._misfire_instruction
		except Exception as e :
			raise e
	'''
	set Misfire Instruction
	'''
	@misfire_instruction.setter
	def misfire_instruction(self,misfire_instruction):
		try :
			if not isinstance(misfire_instruction,str):
				raise TypeError("misfire_instruction must be set to str value")
			self._misfire_instruction = misfire_instruction
		except Exception as e :
			raise e


	'''
	get Next Schedule Time
	'''
	@property
	def next_scheduletime(self) :
		try:
			return self._next_scheduletime
		except Exception as e :
			raise e
	'''
	set Next Schedule Time
	'''
	@next_scheduletime.setter
	def next_scheduletime(self,next_scheduletime):
		try :
			if not isinstance(next_scheduletime,int):
				raise TypeError("next_scheduletime must be set to int value")
			self._next_scheduletime = next_scheduletime
		except Exception as e :
			raise e


	'''
	get Trigger type.Possible values: fixed,daily,weekly,monthly
	'''
	@property
	def trigger_type(self) :
		try:
			return self._trigger_type
		except Exception as e :
			raise e
	'''
	set Trigger type.Possible values: fixed,daily,weekly,monthly
	'''
	@trigger_type.setter
	def trigger_type(self,trigger_type):
		try :
			if not isinstance(trigger_type,str):
				raise TypeError("trigger_type must be set to str value")
			self._trigger_type = trigger_type
		except Exception as e :
			raise e


	'''
	get Time of the day.Format is HH:MM where HH is hours and MM is minutes.Applicable for trigger of type daily
	'''
	@property
	def daily_time(self) :
		try:
			return self._daily_time
		except Exception as e :
			raise e
	'''
	set Time of the day.Format is HH:MM where HH is hours and MM is minutes.Applicable for trigger of type daily
	'''
	@daily_time.setter
	def daily_time(self,daily_time):
		try :
			if not isinstance(daily_time,str):
				raise TypeError("daily_time must be set to str value")
			self._daily_time = daily_time
		except Exception as e :
			raise e


	'''
	get Node on which this job schedule has to be executed
	'''
	@property
	def node_id(self) :
		try:
			return self._node_id
		except Exception as e :
			raise e
	'''
	set Node on which this job schedule has to be executed
	'''
	@node_id.setter
	def node_id(self,node_id):
		try :
			if not isinstance(node_id,str):
				raise TypeError("node_id must be set to str value")
			self._node_id = node_id
		except Exception as e :
			raise e


	'''
	get Original scheduler name
	'''
	@property
	def scheduler_name_org(self) :
		try:
			return self._scheduler_name_org
		except Exception as e :
			raise e
	'''
	set Original scheduler name
	'''
	@scheduler_name_org.setter
	def scheduler_name_org(self,scheduler_name_org):
		try :
			if not isinstance(scheduler_name_org,str):
				raise TypeError("scheduler_name_org must be set to str value")
			self._scheduler_name_org = scheduler_name_org
		except Exception as e :
			raise e


	'''
	get Duration in days for which the trigger should last. Applicable for trigger of type fixed
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e
	'''
	set Duration in days for which the trigger should last. Applicable for trigger of type fixed
	'''
	@duration.setter
	def duration(self,duration):
		try :
			if not isinstance(duration,str):
				raise TypeError("duration must be set to str value")
			self._duration = duration
		except Exception as e :
			raise e


	'''
	get Tenant Id of the Notification Jobs
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Time at which the trigger should end.Format:YY:MM:DD:HH:MM.Applicable for trigger of type fixed
	'''
	@property
	def expiry(self) :
		try:
			return self._expiry
		except Exception as e :
			raise e
	'''
	set Time at which the trigger should end.Format:YY:MM:DD:HH:MM.Applicable for trigger of type fixed
	'''
	@expiry.setter
	def expiry(self,expiry):
		try :
			if not isinstance(expiry,str):
				raise TypeError("expiry must be set to str value")
			self._expiry = expiry
		except Exception as e :
			raise e


	'''
	get Job data in a property map
	'''
	@property
	def jobdata_map(self) :
		try:
			return self._jobdata_map
		except Exception as e :
			raise e
	'''
	set Job data in a property map
	'''
	@jobdata_map.setter
	def jobdata_map(self,jobdata_map) :
		try :
			if not isinstance(jobdata_map,list):
				raise TypeError("jobdata_map must be set to array of property_map value")
			for item in jobdata_map :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._jobdata_map = jobdata_map
		except Exception as e :
			raise e


	'''
	get Schedule Status
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Schedule Status
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
	get Days of the week.Format is Day:HH:MM where Day is 0-6 for sunday-saturday,HH is hours and MM is minutes.Applicable for trigger of type weekly
	'''
	@property
	def weekday_time(self) :
		try:
			return self._weekday_time
		except Exception as e :
			raise e
	'''
	set Days of the week.Format is Day:HH:MM where Day is 0-6 for sunday-saturday,HH is hours and MM is minutes.Applicable for trigger of type weekly
	'''
	@weekday_time.setter
	def weekday_time(self,weekday_time):
		try :
			if not isinstance(weekday_time,str):
				raise TypeError("weekday_time must be set to str value")
			self._weekday_time = weekday_time
		except Exception as e :
			raise e


	'''
	get Timezone offset of the recurrence epoch times from UTC time
	'''
	@property
	def timezoneOffset(self) :
		try:
			return self._timezoneOffset
		except Exception as e :
			raise e
	'''
	set Timezone offset of the recurrence epoch times from UTC time
	'''
	@timezoneOffset.setter
	def timezoneOffset(self,timezoneOffset):
		try :
			if not isinstance(timezoneOffset,int):
				raise TypeError("timezoneOffset must be set to int value")
			self._timezoneOffset = timezoneOffset
		except Exception as e :
			raise e


	'''
	get Scheduler Name
	'''
	@property
	def scheduler_name(self) :
		try:
			return self._scheduler_name
		except Exception as e :
			raise e
	'''
	set Scheduler Name
	'''
	@scheduler_name.setter
	def scheduler_name(self,scheduler_name):
		try :
			if not isinstance(scheduler_name,str):
				raise TypeError("scheduler_name must be set to str value")
			self._scheduler_name = scheduler_name
		except Exception as e :
			raise e


	'''
	get Recur interval in hours. Applicable for trigger of type fixed
	'''
	@property
	def recur_hr(self) :
		try:
			return self._recur_hr
		except Exception as e :
			raise e
	'''
	set Recur interval in hours. Applicable for trigger of type fixed
	'''
	@recur_hr.setter
	def recur_hr(self,recur_hr):
		try :
			if not isinstance(recur_hr,str):
				raise TypeError("recur_hr must be set to str value")
			self._recur_hr = recur_hr
		except Exception as e :
			raise e


	'''
	get Origin of the scheduled export job request
	'''
	@property
	def feature_origin(self) :
		try:
			return self._feature_origin
		except Exception as e :
			raise e
	'''
	set Origin of the scheduled export job request
	'''
	@feature_origin.setter
	def feature_origin(self,feature_origin):
		try :
			if not isinstance(feature_origin,str):
				raise TypeError("feature_origin must be set to str value")
			self._feature_origin = feature_origin
		except Exception as e :
			raise e


	'''
	get Module Name
	'''
	@property
	def module_name(self) :
		try:
			return self._module_name
		except Exception as e :
			raise e
	'''
	set Module Name
	'''
	@module_name.setter
	def module_name(self,module_name):
		try :
			if not isinstance(module_name,str):
				raise TypeError("module_name must be set to str value")
			self._module_name = module_name
		except Exception as e :
			raise e


	'''
	get Name that uniquely identfies a particular scheduled job
	'''
	@property
	def job_schedule_name(self) :
		try:
			return self._job_schedule_name
		except Exception as e :
			raise e
	'''
	set Name that uniquely identfies a particular scheduled job
	'''
	@job_schedule_name.setter
	def job_schedule_name(self,job_schedule_name):
		try :
			if not isinstance(job_schedule_name,str):
				raise TypeError("job_schedule_name must be set to str value")
			self._job_schedule_name = job_schedule_name
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the job_schedule details
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the job_schedule details
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
	get Days of the month.Format is DD:HH:MM where DD is either 1-31 or "last" for days of the month,HH is hours and MM is minutes.Applicable for trigger of type monthly.
	'''
	@property
	def monthday_time(self) :
		try:
			return self._monthday_time
		except Exception as e :
			raise e
	'''
	set Days of the month.Format is DD:HH:MM where DD is either 1-31 or "last" for days of the month,HH is hours and MM is minutes.Applicable for trigger of type monthly.
	'''
	@monthday_time.setter
	def monthday_time(self,monthday_time):
		try :
			if not isinstance(monthday_time,str):
				raise TypeError("monthday_time must be set to str value")
			self._monthday_time = monthday_time
		except Exception as e :
			raise e


	'''
	get Trigger description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Trigger description
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e


	'''
	get Job Name
	'''
	@property
	def job_name(self) :
		try:
			return self._job_name
		except Exception as e :
			raise e
	'''
	set Job Name
	'''
	@job_name.setter
	def job_name(self,job_name):
		try :
			if not isinstance(job_name,str):
				raise TypeError("job_name must be set to str value")
			self._job_name = job_name
		except Exception as e :
			raise e


	'''
	get Recur interval in minutes. Applicable for trigger of type fixed
	'''
	@property
	def recur_min(self) :
		try:
			return self._recur_min
		except Exception as e :
			raise e
	'''
	set Recur interval in minutes. Applicable for trigger of type fixed
	'''
	@recur_min.setter
	def recur_min(self,recur_min):
		try :
			if not isinstance(recur_min,str):
				raise TypeError("recur_min must be set to str value")
			self._recur_min = recur_min
		except Exception as e :
			raise e


	'''
	get Time at which the trigger should start.Format:YY:MM:DD:HH:MM
	'''
	@property
	def start(self) :
		try:
			return self._start
		except Exception as e :
			raise e
	'''
	set Time at which the trigger should start.Format:YY:MM:DD:HH:MM
	'''
	@start.setter
	def start(self,start):
		try :
			if not isinstance(start,str):
				raise TypeError("start must be set to str value")
			self._start = start
		except Exception as e :
			raise e


	'''
	get Recurrrence Type of job that is scheduled
	'''
	@property
	def recurrenceType(self) :
		try:
			return self._recurrenceType
		except Exception as e :
			raise e
	'''
	set Recurrrence Type of job that is scheduled
	'''
	@recurrenceType.setter
	def recurrenceType(self,recurrenceType):
		try :
			if not isinstance(recurrenceType,str):
				raise TypeError("recurrenceType must be set to str value")
			self._recurrenceType = recurrenceType
		except Exception as e :
			raise e


	'''
	get Job Description
	'''
	@property
	def job_description(self) :
		try:
			return self._job_description
		except Exception as e :
			raise e
	'''
	set Job Description
	'''
	@job_description.setter
	def job_description(self,job_description):
		try :
			if not isinstance(job_description,str):
				raise TypeError("job_description must be set to str value")
			self._job_description = job_description
		except Exception as e :
			raise e


	'''
	get Indicates the type of job (USER, SCHEDULED, STAR)
	'''
	@property
	def job_type(self) :
		try:
			return self._job_type
		except Exception as e :
			raise e
	'''
	set Indicates the type of job (USER, SCHEDULED, STAR)
	'''
	@job_type.setter
	def job_type(self,job_type):
		try :
			if not isinstance(job_type,str):
				raise TypeError("job_type must be set to str value")
			self._job_type = job_type
		except Exception as e :
			raise e

	'''
	Comma separated recurrence options of job that is scheduled
	'''
	@property
	def recurrenceOptions(self):
		try:
			return self._recurrenceOptions
		except Exception as e :
			raise e
	'''
	Comma separated recurrence options of job that is scheduled
	'''
	@recurrenceOptions.setter
	def recurrenceOptions(self,recurrenceOptions):
		try :
			if not isinstance(recurrenceOptions,str):
				raise TypeError("recurrenceOptions must be set to str value")
			self._recurrenceOptions = recurrenceOptions
		except Exception as e :
			raise e

	'''
	Comma separated recurrence epoch times at which job is to be executed
	'''
	@property
	def recurrenceTimes(self):
		try:
			return self._recurrenceTimes
		except Exception as e :
			raise e
	'''
	Comma separated recurrence epoch times at which job is to be executed
	'''
	@recurrenceTimes.setter
	def recurrenceTimes(self,recurrenceTimes):
		try :
			if not isinstance(recurrenceTimes,str):
				raise TypeError("recurrenceTimes must be set to str value")
			self._recurrenceTimes = recurrenceTimes
		except Exception as e :
			raise e

	'''
	Use this operation to get job_schedule detail.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				job_schedule_obj=job_schedule()
				response = job_schedule_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add job schedule.
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
				job_schedule_obj= job_schedule()
				return cls.perform_operation_bulk_request(service,resource,job_schedule_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete job schedule(s).
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
					job_schedule_obj=job_schedule()
					return cls.delete_bulk_request(client,resource,job_schedule_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify job schedule.
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
				job_schedule_obj=job_schedule()
				return cls.update_bulk_request(client,resource,job_schedule_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of job_schedule resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			job_schedule_obj = job_schedule()
			option_ = options()
			option_._filter=filter_
			return job_schedule_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the job_schedule resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			job_schedule_obj = job_schedule()
			option_ = options()
			option_._count=True
			response = job_schedule_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of job_schedule resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			job_schedule_obj = job_schedule()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = job_schedule_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(job_schedule_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.job_schedule
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(job_schedule_responses, response, "job_schedule_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.job_schedule_response_array
				i=0
				error = [job_schedule() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.job_schedule_response_array
			i=0
			job_schedule_objs = [job_schedule() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_job_schedule'):
					for props in obj._job_schedule:
						result = service.payload_formatter.string_to_bulk_resource(job_schedule_response,self.__class__.__name__,props)
						job_schedule_objs[i] = result.job_schedule
						i=i+1
			return job_schedule_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(job_schedule,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class job_schedule_response(base_response):
	def __init__(self,length=1) :
		self.job_schedule= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.job_schedule= [ job_schedule() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class job_schedule_responses(base_response):
	def __init__(self,length=1) :
		self.job_schedule_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.job_schedule_response_array = [ job_schedule() for _ in range(length)]
