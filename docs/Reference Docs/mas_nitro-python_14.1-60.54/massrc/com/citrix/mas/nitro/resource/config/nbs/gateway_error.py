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


import os
import logging
from logging import handlers, Formatter
from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for Provides info about Gateway errors resource
'''

class gateway_error(base_resource):
	_metric= ""
	_username= ""
	_rpt_sample_time= ""
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/macro/v1/gateway/gateway_error"
		except Exception as e :
			raise e

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
			return "gateway_error"
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
			return "gateway_errors"
		except Exception as e :
			raise e



	'''
	get Metric
	'''
	@property
	def metric(self) :
		try:
			return self._metric
		except Exception as e :
			raise e
	'''
	set Metric
	'''
	@metric.setter
	def metric(self,metric):
		try :
			if not isinstance(metric,str):
				raise TypeError("metric must be set to str value")
			self._metric = metric
		except Exception as e :
			raise e


	'''
	get Username
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set Username
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e


	'''
	get Report Sample time (epoch time)
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time (epoch time)
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,str):
				raise TypeError("rpt_sample_time must be set to str value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e

	'''
	Provides info about Gateway errors.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			response=""
			if not resource :
				gateway_error_obj=gateway_error()
				response = gateway_error_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of gateway_error resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			gateway_error_obj = gateway_error()
			option_ = options()
			option_._filter=filter_
			return gateway_error_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the gateway_error resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			gateway_error_obj = gateway_error()
			option_ = options()
			option_._count=True
			response = gateway_error_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of gateway_error resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			gateway_error_obj = gateway_error()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = gateway_error_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(gateway_error_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gateway_error
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(gateway_error_responses, response, "gateway_error_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.gateway_error_response_array
				i=0
				error = [gateway_error() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.gateway_error_response_array
			i=0
			gateway_error_objs = [gateway_error() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_gateway_error'):
					for props in obj._gateway_error:
						result = service.payload_formatter.string_to_bulk_resource(gateway_error_response,self.__class__.__name__,props)
						gateway_error_objs[i] = result.gateway_error
						i=i+1
			return gateway_error_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(gateway_error,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class gateway_error_response(base_response):
	def __init__(self,length=1) :
		self.gateway_error= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.gateway_error= [ gateway_error() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class gateway_error_responses(base_response):
	def __init__(self,length=1) :
		self.gateway_error_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.gateway_error_response_array = [ gateway_error() for _ in range(length)]
