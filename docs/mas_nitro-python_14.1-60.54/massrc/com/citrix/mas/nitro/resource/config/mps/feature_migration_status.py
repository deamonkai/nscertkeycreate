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
Configuration for Feature Migration Status resource
'''

class feature_migration_status(base_resource):
	_feature_name= ""
	_total_tables= ""
	_feature_status= ""
	_tables_mig_success= ""
	_tables_mig_failed= ""
	_tables_mig_pending= ""
	_message= ""
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
			return "feature_migration_status"
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
			return "feature_migration_statuss"
		except Exception as e :
			raise e



	'''
	get Feature name
	'''
	@property
	def feature_name(self) :
		try:
			return self._feature_name
		except Exception as e :
			raise e
	'''
	set Feature name
	'''
	@feature_name.setter
	def feature_name(self,feature_name):
		try :
			if not isinstance(feature_name,str):
				raise TypeError("feature_name must be set to str value")
			self._feature_name = feature_name
		except Exception as e :
			raise e


	'''
	get Total Tables
	'''
	@property
	def total_tables(self) :
		try:
			return self._total_tables
		except Exception as e :
			raise e
	'''
	set Total Tables
	'''
	@total_tables.setter
	def total_tables(self,total_tables):
		try :
			if not isinstance(total_tables,long):
				raise TypeError("total_tables must be set to long value")
			self._total_tables = total_tables
		except Exception as e :
			raise e


	'''
	get Feature Status:  (pending, success, in-progress, failed)
	'''
	@property
	def feature_status(self) :
		try:
			return self._feature_status
		except Exception as e :
			raise e
	'''
	set Feature Status:  (pending, success, in-progress, failed)
	'''
	@feature_status.setter
	def feature_status(self,feature_status):
		try :
			if not isinstance(feature_status,str):
				raise TypeError("feature_status must be set to str value")
			self._feature_status = feature_status
		except Exception as e :
			raise e


	'''
	get Number of tables successful during migration to new database
	'''
	@property
	def tables_mig_success(self) :
		try:
			return self._tables_mig_success
		except Exception as e :
			raise e
	'''
	set Number of tables successful during migration to new database
	'''
	@tables_mig_success.setter
	def tables_mig_success(self,tables_mig_success):
		try :
			if not isinstance(tables_mig_success,long):
				raise TypeError("tables_mig_success must be set to long value")
			self._tables_mig_success = tables_mig_success
		except Exception as e :
			raise e


	'''
	get Number of tables failed during migration to new database
	'''
	@property
	def tables_mig_failed(self) :
		try:
			return self._tables_mig_failed
		except Exception as e :
			raise e
	'''
	set Number of tables failed during migration to new database
	'''
	@tables_mig_failed.setter
	def tables_mig_failed(self,tables_mig_failed):
		try :
			if not isinstance(tables_mig_failed,long):
				raise TypeError("tables_mig_failed must be set to long value")
			self._tables_mig_failed = tables_mig_failed
		except Exception as e :
			raise e


	'''
	get Number of tables pending for database migration
	'''
	@property
	def tables_mig_pending(self) :
		try:
			return self._tables_mig_pending
		except Exception as e :
			raise e
	'''
	set Number of tables pending for database migration
	'''
	@tables_mig_pending.setter
	def tables_mig_pending(self,tables_mig_pending):
		try :
			if not isinstance(tables_mig_pending,long):
				raise TypeError("tables_mig_pending must be set to long value")
			self._tables_mig_pending = tables_mig_pending
		except Exception as e :
			raise e


	'''
	get Details about feature migration
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e
	'''
	set Details about feature migration
	'''
	@message.setter
	def message(self,message):
		try :
			if not isinstance(message,str):
				raise TypeError("message must be set to str value")
			self._message = message
		except Exception as e :
			raise e

	'''
	Use this operation to get feature migration information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				feature_migration_status_obj=feature_migration_status()
				response = feature_migration_status_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of feature_migration_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			feature_migration_status_obj = feature_migration_status()
			option_ = options()
			option_._filter=filter_
			return feature_migration_status_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the feature_migration_status resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			feature_migration_status_obj = feature_migration_status()
			option_ = options()
			option_._count=True
			response = feature_migration_status_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of feature_migration_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			feature_migration_status_obj = feature_migration_status()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = feature_migration_status_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(feature_migration_status_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.feature_migration_status
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(feature_migration_status_responses, response, "feature_migration_status_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.feature_migration_status_response_array
				i=0
				error = [feature_migration_status() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.feature_migration_status_response_array
			i=0
			feature_migration_status_objs = [feature_migration_status() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_feature_migration_status'):
					for props in obj._feature_migration_status:
						result = service.payload_formatter.string_to_bulk_resource(feature_migration_status_response,self.__class__.__name__,props)
						feature_migration_status_objs[i] = result.feature_migration_status
						i=i+1
			return feature_migration_status_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(feature_migration_status,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class feature_migration_status_response(base_response):
	def __init__(self,length=1) :
		self.feature_migration_status= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.feature_migration_status= [ feature_migration_status() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class feature_migration_status_responses(base_response):
	def __init__(self,length=1) :
		self.feature_migration_status_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.feature_migration_status_response_array = [ feature_migration_status() for _ in range(length)]
