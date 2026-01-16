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
Configuration for Prediction Band resource
'''

class prediction_band(base_resource):
	_ctnsappname= ""
	_total_violations= ""
	_ind_id= ""
	_prediction_exp_value= ""
	_ind_category_desc= ""
	_rpt_sample_time= ""
	_ip_address= ""
	_ind_name_desc= ""
	_prediction_max_value= ""
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
			return "/macro/v1/security/prediction_band"
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
			return "prediction_band"
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
			return "prediction_bands"
		except Exception as e :
			raise e



	'''
	get AppName
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@ctnsappname.setter
	def ctnsappname(self,ctnsappname):
		try :
			if not isinstance(ctnsappname,str):
				raise TypeError("ctnsappname must be set to str value")
			self._ctnsappname = ctnsappname
		except Exception as e :
			raise e


	'''
	get Total Violation
	'''
	@property
	def total_violations(self) :
		try:
			return self._total_violations
		except Exception as e :
			raise e
	'''
	set Total Violation
	'''
	@total_violations.setter
	def total_violations(self,total_violations):
		try :
			if not isinstance(total_violations,long):
				raise TypeError("total_violations must be set to long value")
			self._total_violations = total_violations
		except Exception as e :
			raise e


	'''
	get Indicator Id
	'''
	@property
	def ind_id(self) :
		try:
			return self._ind_id
		except Exception as e :
			raise e
	'''
	set Indicator Id
	'''
	@ind_id.setter
	def ind_id(self,ind_id):
		try :
			if not isinstance(ind_id,long):
				raise TypeError("ind_id must be set to long value")
			self._ind_id = ind_id
		except Exception as e :
			raise e


	'''
	get Prediction Expected Value
	'''
	@property
	def prediction_exp_value(self) :
		try:
			return self._prediction_exp_value
		except Exception as e :
			raise e
	'''
	set Prediction Expected Value
	'''
	@prediction_exp_value.setter
	def prediction_exp_value(self,prediction_exp_value):
		try :
			if not isinstance(prediction_exp_value,long):
				raise TypeError("prediction_exp_value must be set to long value")
			self._prediction_exp_value = prediction_exp_value
		except Exception as e :
			raise e


	'''
	get Indicator category description
	'''
	@property
	def ind_category_desc(self) :
		try:
			return self._ind_category_desc
		except Exception as e :
			raise e
	'''
	set Indicator category description
	'''
	@ind_category_desc.setter
	def ind_category_desc(self,ind_category_desc):
		try :
			if not isinstance(ind_category_desc,str):
				raise TypeError("ind_category_desc must be set to str value")
			self._ind_category_desc = ind_category_desc
		except Exception as e :
			raise e


	'''
	get Report Sample time.
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,long):
				raise TypeError("rpt_sample_time must be set to long value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e


	'''
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get Indicator name description
	'''
	@property
	def ind_name_desc(self) :
		try:
			return self._ind_name_desc
		except Exception as e :
			raise e
	'''
	set Indicator name description
	'''
	@ind_name_desc.setter
	def ind_name_desc(self,ind_name_desc):
		try :
			if not isinstance(ind_name_desc,str):
				raise TypeError("ind_name_desc must be set to str value")
			self._ind_name_desc = ind_name_desc
		except Exception as e :
			raise e


	'''
	get Prediction Max Value
	'''
	@property
	def prediction_max_value(self) :
		try:
			return self._prediction_max_value
		except Exception as e :
			raise e
	'''
	set Prediction Max Value
	'''
	@prediction_max_value.setter
	def prediction_max_value(self,prediction_max_value):
		try :
			if not isinstance(prediction_max_value,long):
				raise TypeError("prediction_max_value must be set to long value")
			self._prediction_max_value = prediction_max_value
		except Exception as e :
			raise e

	'''
	Prediction Band Summary.
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
				prediction_band_obj=prediction_band()
				response = prediction_band_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of prediction_band resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			prediction_band_obj = prediction_band()
			option_ = options()
			option_._filter=filter_
			return prediction_band_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the prediction_band resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			prediction_band_obj = prediction_band()
			option_ = options()
			option_._count=True
			response = prediction_band_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of prediction_band resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			prediction_band_obj = prediction_band()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = prediction_band_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(prediction_band_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.prediction_band
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(prediction_band_responses, response, "prediction_band_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.prediction_band_response_array
				i=0
				error = [prediction_band() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.prediction_band_response_array
			i=0
			prediction_band_objs = [prediction_band() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_prediction_band'):
					for props in obj._prediction_band:
						result = service.payload_formatter.string_to_bulk_resource(prediction_band_response,self.__class__.__name__,props)
						prediction_band_objs[i] = result.prediction_band
						i=i+1
			return prediction_band_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(prediction_band,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class prediction_band_response(base_response):
	def __init__(self,length=1) :
		self.prediction_band= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.prediction_band= [ prediction_band() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class prediction_band_responses(base_response):
	def __init__(self,length=1) :
		self.prediction_band_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.prediction_band_response_array = [ prediction_band() for _ in range(length)]
