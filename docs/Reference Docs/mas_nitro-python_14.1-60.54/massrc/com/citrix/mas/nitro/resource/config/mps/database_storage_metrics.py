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
from massrc.com.citrix.mas.nitro.resource.config.mps.db_usage_trend import db_usage_trend


'''
Configuration for Resource to fetch database storage metrics resource
'''

class database_storage_metrics(base_resource):
	_metrics=[]
	_datetime= ""
	_timeframe= ""
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
			return "database_storage_metrics"
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
			return "database_storage_metricss"
		except Exception as e :
			raise e



	'''
	get Array of objects with fields source,storage and percentage_of_total,representing the db storage metrics
	'''
	@property
	def metrics(self) :
		try:
			return self._metrics
		except Exception as e :
			raise e
	'''
	set Array of objects with fields source,storage and percentage_of_total,representing the db storage metrics
	'''
	@metrics.setter
	def metrics(self,metrics) :
		try :
			if not isinstance(metrics,list):
				raise TypeError("metrics must be set to array of db_usage_trend value")
			for item in metrics :
				if not isinstance(item,db_usage_trend):
					raise TypeError("item must be set to db_usage_trend value")
			self._metrics = metrics
		except Exception as e :
			raise e


	'''
	get Timestamp in milliseconds when storage was calculated
	'''
	@property
	def datetime(self) :
		try:
			return self._datetime
		except Exception as e :
			raise e
	'''
	set Timestamp in milliseconds when storage was calculated
	'''
	@datetime.setter
	def datetime(self,datetime):
		try :
			if not isinstance(datetime,str):
				raise TypeError("datetime must be set to str value")
			self._datetime = datetime
		except Exception as e :
			raise e


	'''
	get Timeframe to get the database storage metrics. Possible values are latest,last_7_days,last_30_days.Default: latest_30_days
	'''
	@property
	def timeframe(self) :
		try:
			return self._timeframe
		except Exception as e :
			raise e
	'''
	set Timeframe to get the database storage metrics. Possible values are latest,last_7_days,last_30_days.Default: latest_30_days
	'''
	@timeframe.setter
	def timeframe(self,timeframe):
		try :
			if not isinstance(timeframe,str):
				raise TypeError("timeframe must be set to str value")
			self._timeframe = timeframe
		except Exception as e :
			raise e

	'''
	Get database storage metrics according to source.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				database_storage_metrics_obj=database_storage_metrics()
				response = database_storage_metrics_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of database_storage_metrics resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			database_storage_metrics_obj = database_storage_metrics()
			option_ = options()
			option_._filter=filter_
			return database_storage_metrics_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the database_storage_metrics resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			database_storage_metrics_obj = database_storage_metrics()
			option_ = options()
			option_._count=True
			response = database_storage_metrics_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of database_storage_metrics resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			database_storage_metrics_obj = database_storage_metrics()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = database_storage_metrics_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(database_storage_metrics_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.database_storage_metrics
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(database_storage_metrics_responses, response, "database_storage_metrics_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.database_storage_metrics_response_array
				i=0
				error = [database_storage_metrics() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.database_storage_metrics_response_array
			i=0
			database_storage_metrics_objs = [database_storage_metrics() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_database_storage_metrics'):
					for props in obj._database_storage_metrics:
						result = service.payload_formatter.string_to_bulk_resource(database_storage_metrics_response,self.__class__.__name__,props)
						database_storage_metrics_objs[i] = result.database_storage_metrics
						i=i+1
			return database_storage_metrics_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(database_storage_metrics,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class database_storage_metrics_response(base_response):
	def __init__(self,length=1) :
		self.database_storage_metrics= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.database_storage_metrics= [ database_storage_metrics() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class database_storage_metrics_responses(base_response):
	def __init__(self,length=1) :
		self.database_storage_metrics_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.database_storage_metrics_response_array = [ database_storage_metrics() for _ in range(length)]
