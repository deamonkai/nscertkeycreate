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
Configuration for config audit template scheduler resource
'''

class ns_configtemplate_scheduler(base_resource):
	_recurrenceOptions= ""
	_daily_time= ""
	_tz_offset= ""
	_recurrence_type= ""
	_id= ""
	_scheduleTimesEpoch= ""
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
			return "ns_configtemplate_scheduler"
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
			return "ns_configtemplate_schedulers"
		except Exception as e :
			raise e



	'''
	get Comma separated recurrence options of job that is scheduled
	'''
	@property
	def recurrenceOptions(self) :
		try:
			return self._recurrenceOptions
		except Exception as e :
			raise e
	'''
	set Comma separated recurrence options of job that is scheduled
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
	get Daily time details of scheduler
	'''
	@property
	def daily_time(self) :
		try:
			return self._daily_time
		except Exception as e :
			raise e
	'''
	set Daily time details of scheduler
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
	get Daily, Week or Monthly option
	'''
	@property
	def recurrence_type(self) :
		try:
			return self._recurrence_type
		except Exception as e :
			raise e
	'''
	set Daily, Week or Monthly option
	'''
	@recurrence_type.setter
	def recurrence_type(self,recurrence_type):
		try :
			if not isinstance(recurrence_type,str):
				raise TypeError("recurrence_type must be set to str value")
			self._recurrence_type = recurrence_type
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
	get Epoch times for scheduling the job
	'''
	@property
	def scheduleTimesEpoch(self) :
		try:
			return self._scheduleTimesEpoch
		except Exception as e :
			raise e
	'''
	set Epoch times for scheduling the job
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
	Use this operation to get form  ns_configtemplate_scheduler.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_configtemplate_scheduler_obj=ns_configtemplate_scheduler()
				response = ns_configtemplate_scheduler_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete from ns_configtemplate_scheduler.
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
					ns_configtemplate_scheduler_obj=ns_configtemplate_scheduler()
					return cls.delete_bulk_request(client,resource,ns_configtemplate_scheduler_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add to ns_configtemplate_scheduler.
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
				ns_configtemplate_scheduler_obj= ns_configtemplate_scheduler()
				return cls.perform_operation_bulk_request(service,resource,ns_configtemplate_scheduler_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify ns_configtemplate_scheduler.
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
				ns_configtemplate_scheduler_obj=ns_configtemplate_scheduler()
				return cls.update_bulk_request(client,resource,ns_configtemplate_scheduler_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_configtemplate_scheduler resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_configtemplate_scheduler_obj = ns_configtemplate_scheduler()
			option_ = options()
			option_._filter=filter_
			return ns_configtemplate_scheduler_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_configtemplate_scheduler resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_configtemplate_scheduler_obj = ns_configtemplate_scheduler()
			option_ = options()
			option_._count=True
			response = ns_configtemplate_scheduler_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_configtemplate_scheduler resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_configtemplate_scheduler_obj = ns_configtemplate_scheduler()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_configtemplate_scheduler_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_configtemplate_scheduler_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_configtemplate_scheduler
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_configtemplate_scheduler_responses, response, "ns_configtemplate_scheduler_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_configtemplate_scheduler_response_array
				i=0
				error = [ns_configtemplate_scheduler() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_configtemplate_scheduler_response_array
			i=0
			ns_configtemplate_scheduler_objs = [ns_configtemplate_scheduler() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_configtemplate_scheduler'):
					for props in obj._ns_configtemplate_scheduler:
						result = service.payload_formatter.string_to_bulk_resource(ns_configtemplate_scheduler_response,self.__class__.__name__,props)
						ns_configtemplate_scheduler_objs[i] = result.ns_configtemplate_scheduler
						i=i+1
			return ns_configtemplate_scheduler_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_configtemplate_scheduler,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_configtemplate_scheduler_response(base_response):
	def __init__(self,length=1) :
		self.ns_configtemplate_scheduler= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_configtemplate_scheduler= [ ns_configtemplate_scheduler() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_configtemplate_scheduler_responses(base_response):
	def __init__(self,length=1) :
		self.ns_configtemplate_scheduler_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_configtemplate_scheduler_response_array = [ ns_configtemplate_scheduler() for _ in range(length)]
