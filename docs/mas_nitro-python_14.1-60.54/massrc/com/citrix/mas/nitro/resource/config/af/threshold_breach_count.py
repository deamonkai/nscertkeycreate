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
Configuration for Af report for threshold breach count for individual metric resource
'''

class threshold_breach_count(af_generic_api):
	_threshold_count= ""
	_category= ""
	_threshold_name= ""
	___count= ""
	_entity= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "threshold_breach_count"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(threshold_breach_count,self).get_object_id()
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
			return "threshold_breach_counts"
		except Exception as e :
			raise e


	'''
	threshold breach count for particular metric
	'''
	@property
	def threshold_count(self):
		try:
			return self._threshold_count
		except Exception as e :
			raise e
	'''
	threshold breach count for particular metric
	'''
	@threshold_count.setter
	def threshold_count(self,threshold_count):
		try :
			if not isinstance(threshold_count,float):
				raise TypeError("threshold_count must be set to float value")
			self._threshold_count = threshold_count
		except Exception as e :
			raise e

	'''
	All Resource Type for which threshold is violated would be displayed in category e.g. APP, DEVICE, URL
	'''
	@property
	def category(self):
		try:
			return self._category
		except Exception as e :
			raise e
	'''
	All Resource Type for which threshold is violated would be displayed in category e.g. APP, DEVICE, URL
	'''
	@category.setter
	def category(self,category):
		try :
			if not isinstance(category,str):
				raise TypeError("category must be set to str value")
			self._category = category
		except Exception as e :
			raise e

	'''
	threshold name
	'''
	@property
	def threshold_name(self):
		try:
			return self._threshold_name
		except Exception as e :
			raise e
	'''
	threshold name
	'''
	@threshold_name.setter
	def threshold_name(self,threshold_name):
		try :
			if not isinstance(threshold_name,str):
				raise TypeError("threshold_name must be set to str value")
			self._threshold_name = threshold_name
		except Exception as e :
			raise e

	'''
	Number of records
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	Number of records
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
	threshold violated entity e.g outlook
	'''
	@property
	def entity(self):
		try:
			return self._entity
		except Exception as e :
			raise e
	'''
	threshold violated entity e.g outlook
	'''
	@entity.setter
	def entity(self,entity):
		try :
			if not isinstance(entity,str):
				raise TypeError("entity must be set to str value")
			self._entity = entity
		except Exception as e :
			raise e

	'''
	Af Report for threshold breach count for individual metric.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				threshold_breach_count_obj=threshold_breach_count()
				response = threshold_breach_count_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of threshold_breach_count resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			threshold_breach_count_obj = threshold_breach_count()
			option_ = options()
			option_._filter=filter_
			return threshold_breach_count_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the threshold_breach_count resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			threshold_breach_count_obj = threshold_breach_count()
			option_ = options()
			option_._count=True
			response = threshold_breach_count_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of threshold_breach_count resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			threshold_breach_count_obj = threshold_breach_count()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = threshold_breach_count_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - cr_enabled
	'''
	@classmethod
	def set_queryparam_cr_enabled(cls, option, value):
		option.add_queryparam("cr_enabled",value)

	'''
	Set Query Parameter - type
	'''
	@classmethod
	def set_queryparam_type(cls, option, value):
		option.add_queryparam("type",value)

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(threshold_breach_count_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.threshold_breach_count
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(threshold_breach_count_responses, response, "threshold_breach_count_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.threshold_breach_count_response_array
				i=0
				error = [threshold_breach_count() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.threshold_breach_count_response_array
			i=0
			threshold_breach_count_objs = [threshold_breach_count() for _ in range(len(response))]
			for obj in response :
				for props in obj._threshold_breach_count:
					result = service.payload_formatter.string_to_bulk_resource(threshold_breach_count_response,self.__class__.__name__,props)
					threshold_breach_count_objs[i] = result.threshold_breach_count
					i=i+1
			return threshold_breach_count_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(threshold_breach_count,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class threshold_breach_count_response(base_response):
	def __init__(self,length=1) :
		self.threshold_breach_count= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.threshold_breach_count= [ threshold_breach_count() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class threshold_breach_count_responses(base_response):
	def __init__(self,length=1) :
		self.threshold_breach_count_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.threshold_breach_count_response_array = [ threshold_breach_count() for _ in range(length)]
