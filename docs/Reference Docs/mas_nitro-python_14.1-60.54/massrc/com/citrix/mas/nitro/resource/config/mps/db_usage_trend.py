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
Configuration for Source wise database usage trend resource resource
'''

class db_usage_trend(base_resource):
	_percentage_of_total= ""
	_timestamp= ""
	_storage= ""
	_id= ""
	_source= ""
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
			return "db_usage_trend"
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
			return "db_usage_trends"
		except Exception as e :
			raise e



	'''
	get Percentage of total storage contributed by a source
	'''
	@property
	def percentage_of_total(self) :
		try:
			return self._percentage_of_total
		except Exception as e :
			raise e
	'''
	set Percentage of total storage contributed by a source
	'''
	@percentage_of_total.setter
	def percentage_of_total(self,percentage_of_total):
		try :
			if not isinstance(percentage_of_total,float):
				raise TypeError("percentage_of_total must be set to float value")
			self._percentage_of_total = percentage_of_total
		except Exception as e :
			raise e


	'''
	get Timestamp when storage was calculated
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e
	'''
	set Timestamp when storage was calculated
	'''
	@timestamp.setter
	def timestamp(self,timestamp):
		try :
			if not isinstance(timestamp,int):
				raise TypeError("timestamp must be set to int value")
			self._timestamp = timestamp
		except Exception as e :
			raise e


	'''
	get DB storage in MB for a specific source.
	'''
	@property
	def storage(self) :
		try:
			return self._storage
		except Exception as e :
			raise e
	'''
	set DB storage in MB for a specific source.
	'''
	@storage.setter
	def storage(self,storage):
		try :
			if not isinstance(storage,float):
				raise TypeError("storage must be set to float value")
			self._storage = storage
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
	get Source for which DB storage is calculated.Example: App Dashboard,Events,WebInsight
	'''
	@property
	def source(self) :
		try:
			return self._source
		except Exception as e :
			raise e
	'''
	set Source for which DB storage is calculated.Example: App Dashboard,Events,WebInsight
	'''
	@source.setter
	def source(self,source):
		try :
			if not isinstance(source,str):
				raise TypeError("source must be set to str value")
			self._source = source
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(db_usage_trend_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.db_usage_trend
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(db_usage_trend_responses, response, "db_usage_trend_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.db_usage_trend_response_array
				i=0
				error = [db_usage_trend() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.db_usage_trend_response_array
			i=0
			db_usage_trend_objs = [db_usage_trend() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_db_usage_trend'):
					for props in obj._db_usage_trend:
						result = service.payload_formatter.string_to_bulk_resource(db_usage_trend_response,self.__class__.__name__,props)
						db_usage_trend_objs[i] = result.db_usage_trend
						i=i+1
			return db_usage_trend_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(db_usage_trend,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class db_usage_trend_response(base_response):
	def __init__(self,length=1) :
		self.db_usage_trend= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.db_usage_trend= [ db_usage_trend() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class db_usage_trend_responses(base_response):
	def __init__(self,length=1) :
		self.db_usage_trend_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.db_usage_trend_response_array = [ db_usage_trend() for _ in range(length)]
