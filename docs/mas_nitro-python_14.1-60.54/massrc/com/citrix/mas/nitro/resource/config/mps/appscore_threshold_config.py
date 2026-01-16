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
Configuration for Additional Server node information resource
'''

class appscore_threshold_config(base_resource):
	_highVServerCPU= ""
	_lowThreatScore= ""
	_id= ""
	_highNicCongestion= ""
	_highMemory= ""
	_highCPU= ""
	_lowMemory= ""
	_highSurgeQ= ""
	_lowNicDisCards= ""
	_lowNicCongestion= ""
	_lowCPU= ""
	_activeServicesSLA= ""
	_highNicDisCards= ""
	_lowSurgeQ= ""
	_lowVServerCPU= ""
	_highThreatScore= ""
	_responseTimeSLA= ""
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
			return "appscore_threshold_config"
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
			return "appscore_threshold_configs"
		except Exception as e :
			raise e



	'''
	get High VServer CPU
	'''
	@property
	def highVServerCPU(self) :
		try:
			return self._highVServerCPU
		except Exception as e :
			raise e
	'''
	set High VServer CPU
	'''
	@highVServerCPU.setter
	def highVServerCPU(self,highVServerCPU):
		try :
			if not isinstance(highVServerCPU,float):
				raise TypeError("highVServerCPU must be set to float value")
			self._highVServerCPU = highVServerCPU
		except Exception as e :
			raise e


	'''
	get Low Threat Score
	'''
	@property
	def lowThreatScore(self) :
		try:
			return self._lowThreatScore
		except Exception as e :
			raise e
	'''
	set Low Threat Score
	'''
	@lowThreatScore.setter
	def lowThreatScore(self,lowThreatScore):
		try :
			if not isinstance(lowThreatScore,float):
				raise TypeError("lowThreatScore must be set to float value")
			self._lowThreatScore = lowThreatScore
		except Exception as e :
			raise e


	'''
	get Id
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e


	'''
	get High NIC Congestion
	'''
	@property
	def highNicCongestion(self) :
		try:
			return self._highNicCongestion
		except Exception as e :
			raise e
	'''
	set High NIC Congestion
	'''
	@highNicCongestion.setter
	def highNicCongestion(self,highNicCongestion):
		try :
			if not isinstance(highNicCongestion,float):
				raise TypeError("highNicCongestion must be set to float value")
			self._highNicCongestion = highNicCongestion
		except Exception as e :
			raise e


	'''
	get High Memory Threshold
	'''
	@property
	def highMemory(self) :
		try:
			return self._highMemory
		except Exception as e :
			raise e
	'''
	set High Memory Threshold
	'''
	@highMemory.setter
	def highMemory(self,highMemory):
		try :
			if not isinstance(highMemory,float):
				raise TypeError("highMemory must be set to float value")
			self._highMemory = highMemory
		except Exception as e :
			raise e


	'''
	get High CPU Threshold
	'''
	@property
	def highCPU(self) :
		try:
			return self._highCPU
		except Exception as e :
			raise e
	'''
	set High CPU Threshold
	'''
	@highCPU.setter
	def highCPU(self,highCPU):
		try :
			if not isinstance(highCPU,float):
				raise TypeError("highCPU must be set to float value")
			self._highCPU = highCPU
		except Exception as e :
			raise e


	'''
	get Low Memory Threshold
	'''
	@property
	def lowMemory(self) :
		try:
			return self._lowMemory
		except Exception as e :
			raise e
	'''
	set Low Memory Threshold
	'''
	@lowMemory.setter
	def lowMemory(self,lowMemory):
		try :
			if not isinstance(lowMemory,float):
				raise TypeError("lowMemory must be set to float value")
			self._lowMemory = lowMemory
		except Exception as e :
			raise e


	'''
	get Higher Surge Queue Threshold
	'''
	@property
	def highSurgeQ(self) :
		try:
			return self._highSurgeQ
		except Exception as e :
			raise e
	'''
	set Higher Surge Queue Threshold
	'''
	@highSurgeQ.setter
	def highSurgeQ(self,highSurgeQ):
		try :
			if not isinstance(highSurgeQ,float):
				raise TypeError("highSurgeQ must be set to float value")
			self._highSurgeQ = highSurgeQ
		except Exception as e :
			raise e


	'''
	get Low NIC Discards SLA
	'''
	@property
	def lowNicDisCards(self) :
		try:
			return self._lowNicDisCards
		except Exception as e :
			raise e
	'''
	set Low NIC Discards SLA
	'''
	@lowNicDisCards.setter
	def lowNicDisCards(self,lowNicDisCards):
		try :
			if not isinstance(lowNicDisCards,float):
				raise TypeError("lowNicDisCards must be set to float value")
			self._lowNicDisCards = lowNicDisCards
		except Exception as e :
			raise e


	'''
	get Low NIC Congestion
	'''
	@property
	def lowNicCongestion(self) :
		try:
			return self._lowNicCongestion
		except Exception as e :
			raise e
	'''
	set Low NIC Congestion
	'''
	@lowNicCongestion.setter
	def lowNicCongestion(self,lowNicCongestion):
		try :
			if not isinstance(lowNicCongestion,float):
				raise TypeError("lowNicCongestion must be set to float value")
			self._lowNicCongestion = lowNicCongestion
		except Exception as e :
			raise e


	'''
	get Low CPU Threshold
	'''
	@property
	def lowCPU(self) :
		try:
			return self._lowCPU
		except Exception as e :
			raise e
	'''
	set Low CPU Threshold
	'''
	@lowCPU.setter
	def lowCPU(self,lowCPU):
		try :
			if not isinstance(lowCPU,float):
				raise TypeError("lowCPU must be set to float value")
			self._lowCPU = lowCPU
		except Exception as e :
			raise e


	'''
	get Active Services Threshold
	'''
	@property
	def activeServicesSLA(self) :
		try:
			return self._activeServicesSLA
		except Exception as e :
			raise e
	'''
	set Active Services Threshold
	'''
	@activeServicesSLA.setter
	def activeServicesSLA(self,activeServicesSLA):
		try :
			if not isinstance(activeServicesSLA,float):
				raise TypeError("activeServicesSLA must be set to float value")
			self._activeServicesSLA = activeServicesSLA
		except Exception as e :
			raise e


	'''
	get High NIC Discards SLA
	'''
	@property
	def highNicDisCards(self) :
		try:
			return self._highNicDisCards
		except Exception as e :
			raise e
	'''
	set High NIC Discards SLA
	'''
	@highNicDisCards.setter
	def highNicDisCards(self,highNicDisCards):
		try :
			if not isinstance(highNicDisCards,float):
				raise TypeError("highNicDisCards must be set to float value")
			self._highNicDisCards = highNicDisCards
		except Exception as e :
			raise e


	'''
	get Lower Surge Queue Threshold
	'''
	@property
	def lowSurgeQ(self) :
		try:
			return self._lowSurgeQ
		except Exception as e :
			raise e
	'''
	set Lower Surge Queue Threshold
	'''
	@lowSurgeQ.setter
	def lowSurgeQ(self,lowSurgeQ):
		try :
			if not isinstance(lowSurgeQ,float):
				raise TypeError("lowSurgeQ must be set to float value")
			self._lowSurgeQ = lowSurgeQ
		except Exception as e :
			raise e


	'''
	get Low VServer CPU
	'''
	@property
	def lowVServerCPU(self) :
		try:
			return self._lowVServerCPU
		except Exception as e :
			raise e
	'''
	set Low VServer CPU
	'''
	@lowVServerCPU.setter
	def lowVServerCPU(self,lowVServerCPU):
		try :
			if not isinstance(lowVServerCPU,float):
				raise TypeError("lowVServerCPU must be set to float value")
			self._lowVServerCPU = lowVServerCPU
		except Exception as e :
			raise e


	'''
	get High Threat Score
	'''
	@property
	def highThreatScore(self) :
		try:
			return self._highThreatScore
		except Exception as e :
			raise e
	'''
	set High Threat Score
	'''
	@highThreatScore.setter
	def highThreatScore(self,highThreatScore):
		try :
			if not isinstance(highThreatScore,float):
				raise TypeError("highThreatScore must be set to float value")
			self._highThreatScore = highThreatScore
		except Exception as e :
			raise e


	'''
	get Response Time Threshold
	'''
	@property
	def responseTimeSLA(self) :
		try:
			return self._responseTimeSLA
		except Exception as e :
			raise e
	'''
	set Response Time Threshold
	'''
	@responseTimeSLA.setter
	def responseTimeSLA(self,responseTimeSLA):
		try :
			if not isinstance(responseTimeSLA,float):
				raise TypeError("responseTimeSLA must be set to float value")
			self._responseTimeSLA = responseTimeSLA
		except Exception as e :
			raise e

	'''
	Use this operation to get server nodes.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				appscore_threshold_config_obj=appscore_threshold_config()
				response = appscore_threshold_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add server nodes.
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
				appscore_threshold_config_obj= appscore_threshold_config()
				return cls.perform_operation_bulk_request(service,resource,appscore_threshold_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete server nodes.
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
					appscore_threshold_config_obj=appscore_threshold_config()
					return cls.delete_bulk_request(client,resource,appscore_threshold_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify server nodes.
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
				appscore_threshold_config_obj=appscore_threshold_config()
				return cls.update_bulk_request(client,resource,appscore_threshold_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of appscore_threshold_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			appscore_threshold_config_obj = appscore_threshold_config()
			option_ = options()
			option_._filter=filter_
			return appscore_threshold_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the appscore_threshold_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			appscore_threshold_config_obj = appscore_threshold_config()
			option_ = options()
			option_._count=True
			response = appscore_threshold_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of appscore_threshold_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			appscore_threshold_config_obj = appscore_threshold_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = appscore_threshold_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(appscore_threshold_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appscore_threshold_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(appscore_threshold_config_responses, response, "appscore_threshold_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.appscore_threshold_config_response_array
				i=0
				error = [appscore_threshold_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.appscore_threshold_config_response_array
			i=0
			appscore_threshold_config_objs = [appscore_threshold_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_appscore_threshold_config'):
					for props in obj._appscore_threshold_config:
						result = service.payload_formatter.string_to_bulk_resource(appscore_threshold_config_response,self.__class__.__name__,props)
						appscore_threshold_config_objs[i] = result.appscore_threshold_config
						i=i+1
			return appscore_threshold_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(appscore_threshold_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class appscore_threshold_config_response(base_response):
	def __init__(self,length=1) :
		self.appscore_threshold_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.appscore_threshold_config= [ appscore_threshold_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class appscore_threshold_config_responses(base_response):
	def __init__(self,length=1) :
		self.appscore_threshold_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.appscore_threshold_config_response_array = [ appscore_threshold_config() for _ in range(length)]
