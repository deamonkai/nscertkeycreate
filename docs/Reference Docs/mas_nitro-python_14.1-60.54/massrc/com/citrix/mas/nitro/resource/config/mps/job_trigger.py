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
Configuration for API used to trigger AppServer Job given Job Scheduler name resource
'''

class job_trigger(base_resource):
	_next_scheduletime= ""
	_job_schedule_name= ""
	_job_status= ""
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
			return "job_trigger"
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
			return "job_triggers"
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
			if not isinstance(next_scheduletime,long):
				raise TypeError("next_scheduletime must be set to long value")
			self._next_scheduletime = next_scheduletime
		except Exception as e :
			raise e


	'''
	get Job Schedule Name
	'''
	@property
	def job_schedule_name(self) :
		try:
			return self._job_schedule_name
		except Exception as e :
			raise e
	'''
	set Job Schedule Name
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
	get Job Status
	'''
	@property
	def job_status(self) :
		try:
			return self._job_status
		except Exception as e :
			raise e
	'''
	set Job Status
	'''
	@job_status.setter
	def job_status(self,job_status):
		try :
			if not isinstance(job_status,str):
				raise TypeError("job_status must be set to str value")
			self._job_status = job_status
		except Exception as e :
			raise e

	'''
	Triggers/fetch status of job with given scheduler name.
	'''
	@classmethod
	def post(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"post")
				return res
			else : 
				job_trigger_obj= job_trigger()
				return cls.perform_operation_bulk_request(service,"post",resource,job_trigger_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(job_trigger_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.job_trigger
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(job_trigger_responses, response, "job_trigger_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.job_trigger_response_array
				i=0
				error = [job_trigger() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.job_trigger_response_array
			i=0
			job_trigger_objs = [job_trigger() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_job_trigger'):
					for props in obj._job_trigger:
						result = service.payload_formatter.string_to_bulk_resource(job_trigger_response,self.__class__.__name__,props)
						job_trigger_objs[i] = result.job_trigger
						i=i+1
			return job_trigger_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(job_trigger,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class job_trigger_response(base_response):
	def __init__(self,length=1) :
		self.job_trigger= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.job_trigger= [ job_trigger() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class job_trigger_responses(base_response):
	def __init__(self,length=1) :
		self.job_trigger_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.job_trigger_response_array = [ job_trigger() for _ in range(length)]
