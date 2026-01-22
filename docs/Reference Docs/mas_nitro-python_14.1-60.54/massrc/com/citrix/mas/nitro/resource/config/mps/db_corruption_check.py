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
Configuration for DB Corruption Check resource
'''

class db_corruption_check(base_resource):
	_completion_percentage= ""
	_job_trigger_time= ""
	_scan_scope= ""
	_id= ""
	_result= ""
	_job_trigger_end_time= ""
	_recommendation= ""
	_status= ""
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
			return "db_corruption_check"
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
			return "db_corruption_checks"
		except Exception as e :
			raise e



	'''
	get Percentage of completion of the database corruption scan script execution
	'''
	@property
	def completion_percentage(self) :
		try:
			return self._completion_percentage
		except Exception as e :
			raise e
	'''
	set Percentage of completion of the database corruption scan script execution
	'''
	@completion_percentage.setter
	def completion_percentage(self,completion_percentage):
		try :
			if not isinstance(completion_percentage,int):
				raise TypeError("completion_percentage must be set to int value")
			self._completion_percentage = completion_percentage
		except Exception as e :
			raise e


	'''
	get Time when database corruption scan is started
	'''
	@property
	def job_trigger_time(self) :
		try:
			return self._job_trigger_time
		except Exception as e :
			raise e
	'''
	set Time when database corruption scan is started
	'''
	@job_trigger_time.setter
	def job_trigger_time(self,job_trigger_time):
		try :
			if not isinstance(job_trigger_time,int):
				raise TypeError("job_trigger_time must be set to int value")
			self._job_trigger_time = job_trigger_time
		except Exception as e :
			raise e


	'''
	get Scope of database corruption scan - CONFIG_TABLES for configuration data only, ALL_TABLES for complete database scan
	'''
	@property
	def scan_scope(self) :
		try:
			return self._scan_scope
		except Exception as e :
			raise e
	'''
	set Scope of database corruption scan - CONFIG_TABLES for configuration data only, ALL_TABLES for complete database scan
	'''
	@scan_scope.setter
	def scan_scope(self,scan_scope):
		try :
			if not isinstance(scan_scope,str):
				raise TypeError("scan_scope must be set to str value")
			self._scan_scope = scan_scope
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all entries.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all entries.
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
	get Result of the database corruption scan script execution
	'''
	@property
	def result(self) :
		try:
			return self._result
		except Exception as e :
			raise e
	'''
	set Result of the database corruption scan script execution
	'''
	@result.setter
	def result(self,result):
		try :
			if not isinstance(result,str):
				raise TypeError("result must be set to str value")
			self._result = result
		except Exception as e :
			raise e


	'''
	get Time when database corruption scan is ended
	'''
	@property
	def job_trigger_end_time(self) :
		try:
			return self._job_trigger_end_time
		except Exception as e :
			raise e
	'''
	set Time when database corruption scan is ended
	'''
	@job_trigger_end_time.setter
	def job_trigger_end_time(self,job_trigger_end_time):
		try :
			if not isinstance(job_trigger_end_time,int):
				raise TypeError("job_trigger_end_time must be set to int value")
			self._job_trigger_end_time = job_trigger_end_time
		except Exception as e :
			raise e


	'''
	get Recommendation based on the database corruption scan script execution
	'''
	@property
	def recommendation(self) :
		try:
			return self._recommendation
		except Exception as e :
			raise e
	'''
	set Recommendation based on the database corruption scan script execution
	'''
	@recommendation.setter
	def recommendation(self,recommendation):
		try :
			if not isinstance(recommendation,str):
				raise TypeError("recommendation must be set to str value")
			self._recommendation = recommendation
		except Exception as e :
			raise e


	'''
	get Status of database corruption scan e.g. SUCCESS, FAILED, In Progress
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of database corruption scan e.g. SUCCESS, FAILED, In Progress
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
	Use this operation to start database corruption scan.
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
				db_corruption_check_obj= db_corruption_check()
				return cls.perform_operation_bulk_request(service,resource,db_corruption_check_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get details of database corruption scan.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				db_corruption_check_obj=db_corruption_check()
				response = db_corruption_check_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of db_corruption_check resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			db_corruption_check_obj = db_corruption_check()
			option_ = options()
			option_._filter=filter_
			return db_corruption_check_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the db_corruption_check resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			db_corruption_check_obj = db_corruption_check()
			option_ = options()
			option_._count=True
			response = db_corruption_check_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of db_corruption_check resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			db_corruption_check_obj = db_corruption_check()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = db_corruption_check_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(db_corruption_check_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.db_corruption_check
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(db_corruption_check_responses, response, "db_corruption_check_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.db_corruption_check_response_array
				i=0
				error = [db_corruption_check() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.db_corruption_check_response_array
			i=0
			db_corruption_check_objs = [db_corruption_check() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_db_corruption_check'):
					for props in obj._db_corruption_check:
						result = service.payload_formatter.string_to_bulk_resource(db_corruption_check_response,self.__class__.__name__,props)
						db_corruption_check_objs[i] = result.db_corruption_check
						i=i+1
			return db_corruption_check_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(db_corruption_check,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class db_corruption_check_response(base_response):
	def __init__(self,length=1) :
		self.db_corruption_check= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.db_corruption_check= [ db_corruption_check() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class db_corruption_check_responses(base_response):
	def __init__(self,length=1) :
		self.db_corruption_check_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.db_corruption_check_response_array = [ db_corruption_check() for _ in range(length)]
