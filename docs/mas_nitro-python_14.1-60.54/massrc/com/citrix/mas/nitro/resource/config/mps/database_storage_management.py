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
Configuration for Resource to fetch database storage management resource
'''

class database_storage_management(base_resource):
	_truncate_id= ""
	_sources_for_truncate=[]
	_is_truncate_allowed= ""
	_allowed_truncate_count= ""
	_data_ingestion= ""
	_maximum_truncate_count= ""
	_truncate_in_progress= ""
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
			return "database_storage_management"
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
			return "database_storage_managements"
		except Exception as e :
			raise e



	'''
	get Unique ID which represents a specific truncate operation initiated by the user
	'''
	@property
	def truncate_id(self) :
		try:
			return self._truncate_id
		except Exception as e :
			raise e
	'''
	set Unique ID which represents a specific truncate operation initiated by the user
	'''
	@truncate_id.setter
	def truncate_id(self,truncate_id):
		try :
			if not isinstance(truncate_id,str):
				raise TypeError("truncate_id must be set to str value")
			self._truncate_id = truncate_id
		except Exception as e :
			raise e


	'''
	get Array of sources whose tables need to be truncated to free up database space.
	'''
	@property
	def sources_for_truncate(self) :
		try:
			return self._sources_for_truncate
		except Exception as e :
			raise e
	'''
	set Array of sources whose tables need to be truncated to free up database space.
	'''
	@sources_for_truncate.setter
	def sources_for_truncate(self,sources_for_truncate) :
		try :
			if not isinstance(sources_for_truncate,list):
				raise TypeError("sources_for_truncate must be set to array of str value")
			for item in sources_for_truncate :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._sources_for_truncate = sources_for_truncate
		except Exception as e :
			raise e


	'''
	get Indicate whether persisted historical data from various sources can be truncated or not.
	'''
	@property
	def is_truncate_allowed(self) :
		try:
			return self._is_truncate_allowed
		except Exception as e :
			raise e
	'''
	set Indicate whether persisted historical data from various sources can be truncated or not.
	'''
	@is_truncate_allowed.setter
	def is_truncate_allowed(self,is_truncate_allowed):
		try :
			if not isinstance(is_truncate_allowed,bool):
				raise TypeError("is_truncate_allowed must be set to bool value")
			self._is_truncate_allowed = is_truncate_allowed
		except Exception as e :
			raise e


	'''
	get Remaining number of times data can be truncated, to restart ingestion in a calendar month
	'''
	@property
	def allowed_truncate_count(self) :
		try:
			return self._allowed_truncate_count
		except Exception as e :
			raise e
	'''
	set Remaining number of times data can be truncated, to restart ingestion in a calendar month
	'''
	@allowed_truncate_count.setter
	def allowed_truncate_count(self,allowed_truncate_count):
		try :
			if not isinstance(allowed_truncate_count,int):
				raise TypeError("allowed_truncate_count must be set to int value")
			self._allowed_truncate_count = allowed_truncate_count
		except Exception as e :
			raise e


	'''
	get Indicates whether data ingestion is enabled or not. Possible values: Enabled, Disabled
	'''
	@property
	def data_ingestion(self) :
		try:
			return self._data_ingestion
		except Exception as e :
			raise e
	'''
	set Indicates whether data ingestion is enabled or not. Possible values: Enabled, Disabled
	'''
	@data_ingestion.setter
	def data_ingestion(self,data_ingestion):
		try :
			if not isinstance(data_ingestion,str):
				raise TypeError("data_ingestion must be set to str value")
			self._data_ingestion = data_ingestion
		except Exception as e :
			raise e


	'''
	get Maximum number of times data can be truncated, to restart ingestion in a calendar month
	'''
	@property
	def maximum_truncate_count(self) :
		try:
			return self._maximum_truncate_count
		except Exception as e :
			raise e
	'''
	set Maximum number of times data can be truncated, to restart ingestion in a calendar month
	'''
	@maximum_truncate_count.setter
	def maximum_truncate_count(self,maximum_truncate_count):
		try :
			if not isinstance(maximum_truncate_count,int):
				raise TypeError("maximum_truncate_count must be set to int value")
			self._maximum_truncate_count = maximum_truncate_count
		except Exception as e :
			raise e


	'''
	get Indicate whether an user initiated truncate operation is already in progress or not
	'''
	@property
	def truncate_in_progress(self) :
		try:
			return self._truncate_in_progress
		except Exception as e :
			raise e
	'''
	set Indicate whether an user initiated truncate operation is already in progress or not
	'''
	@truncate_in_progress.setter
	def truncate_in_progress(self,truncate_in_progress):
		try :
			if not isinstance(truncate_in_progress,bool):
				raise TypeError("truncate_in_progress must be set to bool value")
			self._truncate_in_progress = truncate_in_progress
		except Exception as e :
			raise e

	'''
	get database storage manangement resource.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				database_storage_management_obj=database_storage_management()
				response = database_storage_management_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Truncate the database tables for sources mentioned in the source_for_truncate property.
	'''
	@classmethod
	def truncate(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"truncate")
				return res
			else : 
				database_storage_management_obj= database_storage_management()
				return cls.perform_operation_bulk_request(service,"truncate",resource,database_storage_management_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of database_storage_management resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			database_storage_management_obj = database_storage_management()
			option_ = options()
			option_._filter=filter_
			return database_storage_management_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the database_storage_management resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			database_storage_management_obj = database_storage_management()
			option_ = options()
			option_._count=True
			response = database_storage_management_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of database_storage_management resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			database_storage_management_obj = database_storage_management()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = database_storage_management_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(database_storage_management_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.database_storage_management
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(database_storage_management_responses, response, "database_storage_management_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.database_storage_management_response_array
				i=0
				error = [database_storage_management() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.database_storage_management_response_array
			i=0
			database_storage_management_objs = [database_storage_management() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_database_storage_management'):
					for props in obj._database_storage_management:
						result = service.payload_formatter.string_to_bulk_resource(database_storage_management_response,self.__class__.__name__,props)
						database_storage_management_objs[i] = result.database_storage_management
						i=i+1
			return database_storage_management_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(database_storage_management,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class database_storage_management_response(base_response):
	def __init__(self,length=1) :
		self.database_storage_management= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.database_storage_management= [ database_storage_management() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class database_storage_management_responses(base_response):
	def __init__(self,length=1) :
		self.database_storage_management_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.database_storage_management_response_array = [ database_storage_management() for _ in range(length)]
