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
Configuration for AF API Rate Limit Report table resource
'''

class api_rate_limit(af_generic_api):
	_total_ratelimited_requests= ""
	_api_endpoint= ""
	_api_instance= ""
	_http_req_method= ""
	_total_requests= ""
	_total_bytes= ""
	_rpt_sample_time= ""
	___count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "api_rate_limit"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(api_rate_limit,self).get_object_id()
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
			return "api_rate_limits"
		except Exception as e :
			raise e


	'''
	Total Ratelimited Requests.
	'''
	@property
	def total_ratelimited_requests(self):
		try:
			return self._total_ratelimited_requests
		except Exception as e :
			raise e
	'''
	Total Ratelimited Requests.
	'''
	@total_ratelimited_requests.setter
	def total_ratelimited_requests(self,total_ratelimited_requests):
		try :
			if not isinstance(total_ratelimited_requests,float):
				raise TypeError("total_ratelimited_requests must be set to float value")
			self._total_ratelimited_requests = total_ratelimited_requests
		except Exception as e :
			raise e

	'''
	API Endpoint Name
	'''
	@property
	def api_endpoint(self):
		try:
			return self._api_endpoint
		except Exception as e :
			raise e
	'''
	API Endpoint Name
	'''
	@api_endpoint.setter
	def api_endpoint(self,api_endpoint):
		try :
			if not isinstance(api_endpoint,str):
				raise TypeError("api_endpoint must be set to str value")
			self._api_endpoint = api_endpoint
		except Exception as e :
			raise e

	'''
	API Instance Name
	'''
	@property
	def api_instance(self):
		try:
			return self._api_instance
		except Exception as e :
			raise e
	'''
	API Instance Name
	'''
	@api_instance.setter
	def api_instance(self,api_instance):
		try :
			if not isinstance(api_instance,str):
				raise TypeError("api_instance must be set to str value")
			self._api_instance = api_instance
		except Exception as e :
			raise e

	'''
	HTTP Request Method.
	'''
	@property
	def http_req_method(self):
		try:
			return self._http_req_method
		except Exception as e :
			raise e
	'''
	HTTP Request Method.
	'''
	@http_req_method.setter
	def http_req_method(self,http_req_method):
		try :
			if not isinstance(http_req_method,str):
				raise TypeError("http_req_method must be set to str value")
			self._http_req_method = http_req_method
		except Exception as e :
			raise e

	'''
	Total Requests in given sampled timeframe.
	'''
	@property
	def total_requests(self):
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	Total Requests in given sampled timeframe.
	'''
	@total_requests.setter
	def total_requests(self,total_requests):
		try :
			if not isinstance(total_requests,float):
				raise TypeError("total_requests must be set to float value")
			self._total_requests = total_requests
		except Exception as e :
			raise e

	'''
	Total bytes in sampled timeframe.
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes in sampled timeframe.
	'''
	@total_bytes.setter
	def total_bytes(self,total_bytes):
		try :
			if not isinstance(total_bytes,float):
				raise TypeError("total_bytes must be set to float value")
			self._total_bytes = total_bytes
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
	AF API HTTP Rate Limit Report table..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				api_rate_limit_obj=api_rate_limit()
				response = api_rate_limit_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of api_rate_limit resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			api_rate_limit_obj = api_rate_limit()
			option_ = options()
			option_._filter=filter_
			return api_rate_limit_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the api_rate_limit resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			api_rate_limit_obj = api_rate_limit()
			option_ = options()
			option_._count=True
			response = api_rate_limit_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of api_rate_limit resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			api_rate_limit_obj = api_rate_limit()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = api_rate_limit_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(api_rate_limit_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.api_rate_limit
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(api_rate_limit_responses, response, "api_rate_limit_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.api_rate_limit_response_array
				i=0
				error = [api_rate_limit() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.api_rate_limit_response_array
			i=0
			api_rate_limit_objs = [api_rate_limit() for _ in range(len(response))]
			for obj in response :
				for props in obj._api_rate_limit:
					result = service.payload_formatter.string_to_bulk_resource(api_rate_limit_response,self.__class__.__name__,props)
					api_rate_limit_objs[i] = result.api_rate_limit
					i=i+1
			return api_rate_limit_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(api_rate_limit,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class api_rate_limit_response(base_response):
	def __init__(self,length=1) :
		self.api_rate_limit= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.api_rate_limit= [ api_rate_limit() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class api_rate_limit_responses(base_response):
	def __init__(self,length=1) :
		self.api_rate_limit_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.api_rate_limit_response_array = [ api_rate_limit() for _ in range(length)]
