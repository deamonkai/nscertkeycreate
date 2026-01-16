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

from massrc.com.citrix.mas.nitro.resource.config.mps.af_generic_api import af_generic_api

'''
Configuration for Af report for Threshold config timeline resource
'''

class threshold_config_timeline(af_generic_api):
	_rpt_sample_time= ""
	_enable_flag= ""
	_configure_value= ""
	___count= ""
	_entity_type= ""
	_configure_metric= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "threshold_config_timeline"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(threshold_config_timeline,self).get_object_id()
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
			return "threshold_config_timelines"
		except Exception as e :
			raise e


	'''
	Report Sample time.
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	Report Sample time.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,float):
				raise TypeError("rpt_sample_time must be set to float value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e

	'''
	enable_flag.
	'''
	@property
	def enable_flag(self):
		try:
			return self._enable_flag
		except Exception as e :
			raise e
	'''
	enable_flag.
	'''
	@enable_flag.setter
	def enable_flag(self,enable_flag):
		try :
			if not isinstance(enable_flag,float):
				raise TypeError("enable_flag must be set to float value")
			self._enable_flag = enable_flag
		except Exception as e :
			raise e

	'''
	threshold configure_value
	'''
	@property
	def configure_value(self):
		try:
			return self._configure_value
		except Exception as e :
			raise e
	'''
	threshold configure_value
	'''
	@configure_value.setter
	def configure_value(self,configure_value):
		try :
			if not isinstance(configure_value,float):
				raise TypeError("configure_value must be set to float value")
			self._configure_value = configure_value
		except Exception as e :
			raise e

	'''
	count.
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	count.
	'''
	@__count.setter
	def __count(self,__count):
		try :
			if not isinstance(__count,float):
				raise TypeError("__count must be set to float value")
			self.___count = __count
		except Exception as e :
			raise e

	'''
	entity_type
	'''
	@property
	def entity_type(self):
		try:
			return self._entity_type
		except Exception as e :
			raise e
	'''
	entity_type
	'''
	@entity_type.setter
	def entity_type(self,entity_type):
		try :
			if not isinstance(entity_type,str):
				raise TypeError("entity_type must be set to str value")
			self._entity_type = entity_type
		except Exception as e :
			raise e

	'''
	configure_metric
	'''
	@property
	def configure_metric(self):
		try:
			return self._configure_metric
		except Exception as e :
			raise e
	'''
	configure_metric
	'''
	@configure_metric.setter
	def configure_metric(self,configure_metric):
		try :
			if not isinstance(configure_metric,str):
				raise TypeError("configure_metric must be set to str value")
			self._configure_metric = configure_metric
		except Exception as e :
			raise e

	'''
	Af report for Threshold config timeline..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				threshold_config_timeline_obj=threshold_config_timeline()
				response = threshold_config_timeline_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of threshold_config_timeline resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			threshold_config_timeline_obj = threshold_config_timeline()
			option_ = options()
			option_._filter=filter_
			return threshold_config_timeline_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the threshold_config_timeline resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			threshold_config_timeline_obj = threshold_config_timeline()
			option_ = options()
			option_._count=True
			response = threshold_config_timeline_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of threshold_config_timeline resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			threshold_config_timeline_obj = threshold_config_timeline()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = threshold_config_timeline_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(threshold_config_timeline_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.threshold_config_timeline
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(threshold_config_timeline_responses, response, "threshold_config_timeline_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.threshold_config_timeline_response_array
				i=0
				error = [threshold_config_timeline() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.threshold_config_timeline_response_array
			i=0
			threshold_config_timeline_objs = [threshold_config_timeline() for _ in range(len(response))]
			for obj in response :
				for props in obj._threshold_config_timeline:
					result = service.payload_formatter.string_to_bulk_resource(threshold_config_timeline_response,self.__class__.__name__,props)
					threshold_config_timeline_objs[i] = result.threshold_config_timeline
					i=i+1
			return threshold_config_timeline_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(threshold_config_timeline,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class threshold_config_timeline_response(base_response):
	def __init__(self,length=1) :
		self.threshold_config_timeline= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.threshold_config_timeline= [ threshold_config_timeline() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class threshold_config_timeline_responses(base_response):
	def __init__(self,length=1) :
		self.threshold_config_timeline_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.threshold_config_timeline_response_array = [ threshold_config_timeline() for _ in range(length)]
