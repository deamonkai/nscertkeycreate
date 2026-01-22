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
Configuration for NetScaler Prediction data resource
'''

class aa_adc_prediction_l2_v2(base_resource):
	_prediction_hour_id= ""
	_window_start_time= ""
	_rpt_sample_time= ""
	_prediction_upbound= ""
	_tenant_id= ""
	_prediction_time= ""
	_prediction_avg= ""
	_ip_address= ""
	_window_end_time= ""
	_prediction_metric= ""
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
			return "aa_adc_prediction_l2_v2"
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
			return "aa_adc_prediction_l2_v2s"
		except Exception as e :
			raise e



	'''
	get Prediction Hour ID.
	'''
	@property
	def prediction_hour_id(self) :
		try:
			return self._prediction_hour_id
		except Exception as e :
			raise e
	'''
	set Prediction Hour ID.
	'''
	@prediction_hour_id.setter
	def prediction_hour_id(self,prediction_hour_id):
		try :
			if not isinstance(prediction_hour_id,long):
				raise TypeError("prediction_hour_id must be set to long value")
			self._prediction_hour_id = prediction_hour_id
		except Exception as e :
			raise e


	'''
	get Window Start time.
	'''
	@property
	def window_start_time(self) :
		try:
			return self._window_start_time
		except Exception as e :
			raise e
	'''
	set Window Start time.
	'''
	@window_start_time.setter
	def window_start_time(self,window_start_time):
		try :
			if not isinstance(window_start_time,long):
				raise TypeError("window_start_time must be set to long value")
			self._window_start_time = window_start_time
		except Exception as e :
			raise e


	'''
	get rpt_sample_time
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set rpt_sample_time
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
	get Prediction Upper bound.
	'''
	@property
	def prediction_upbound(self) :
		try:
			return self._prediction_upbound
		except Exception as e :
			raise e
	'''
	set Prediction Upper bound.
	'''
	@prediction_upbound.setter
	def prediction_upbound(self,prediction_upbound):
		try :
			if not isinstance(prediction_upbound,float):
				raise TypeError("prediction_upbound must be set to float value")
			self._prediction_upbound = prediction_upbound
		except Exception as e :
			raise e


	'''
	get tenant_id
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set tenant_id
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e


	'''
	get Prediction Time.
	'''
	@property
	def prediction_time(self) :
		try:
			return self._prediction_time
		except Exception as e :
			raise e
	'''
	set Prediction Time.
	'''
	@prediction_time.setter
	def prediction_time(self,prediction_time):
		try :
			if not isinstance(prediction_time,long):
				raise TypeError("prediction_time must be set to long value")
			self._prediction_time = prediction_time
		except Exception as e :
			raise e


	'''
	get Prediction Average
	'''
	@property
	def prediction_avg(self) :
		try:
			return self._prediction_avg
		except Exception as e :
			raise e
	'''
	set Prediction Average
	'''
	@prediction_avg.setter
	def prediction_avg(self,prediction_avg):
		try :
			if not isinstance(prediction_avg,float):
				raise TypeError("prediction_avg must be set to float value")
			self._prediction_avg = prediction_avg
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
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
	get Window End time.
	'''
	@property
	def window_end_time(self) :
		try:
			return self._window_end_time
		except Exception as e :
			raise e
	'''
	set Window End time.
	'''
	@window_end_time.setter
	def window_end_time(self,window_end_time):
		try :
			if not isinstance(window_end_time,long):
				raise TypeError("window_end_time must be set to long value")
			self._window_end_time = window_end_time
		except Exception as e :
			raise e


	'''
	get prediction_metric
	'''
	@property
	def prediction_metric(self) :
		try:
			return self._prediction_metric
		except Exception as e :
			raise e
	'''
	set prediction_metric
	'''
	@prediction_metric.setter
	def prediction_metric(self,prediction_metric):
		try :
			if not isinstance(prediction_metric,str):
				raise TypeError("prediction_metric must be set to str value")
			self._prediction_metric = prediction_metric
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler Prediction details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				aa_adc_prediction_l2_v2_obj=aa_adc_prediction_l2_v2()
				response = aa_adc_prediction_l2_v2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_adc_prediction_l2_v2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_adc_prediction_l2_v2_obj = aa_adc_prediction_l2_v2()
			option_ = options()
			option_._filter=filter_
			return aa_adc_prediction_l2_v2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_adc_prediction_l2_v2 resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_adc_prediction_l2_v2_obj = aa_adc_prediction_l2_v2()
			option_ = options()
			option_._count=True
			response = aa_adc_prediction_l2_v2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_adc_prediction_l2_v2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_adc_prediction_l2_v2_obj = aa_adc_prediction_l2_v2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_adc_prediction_l2_v2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_adc_prediction_l2_v2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_adc_prediction_l2_v2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_adc_prediction_l2_v2_responses, response, "aa_adc_prediction_l2_v2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_adc_prediction_l2_v2_response_array
				i=0
				error = [aa_adc_prediction_l2_v2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_adc_prediction_l2_v2_response_array
			i=0
			aa_adc_prediction_l2_v2_objs = [aa_adc_prediction_l2_v2() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_aa_adc_prediction_l2_v2'):
					for props in obj._aa_adc_prediction_l2_v2:
						result = service.payload_formatter.string_to_bulk_resource(aa_adc_prediction_l2_v2_response,self.__class__.__name__,props)
						aa_adc_prediction_l2_v2_objs[i] = result.aa_adc_prediction_l2_v2
						i=i+1
			return aa_adc_prediction_l2_v2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_adc_prediction_l2_v2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_adc_prediction_l2_v2_response(base_response):
	def __init__(self,length=1) :
		self.aa_adc_prediction_l2_v2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_adc_prediction_l2_v2= [ aa_adc_prediction_l2_v2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_adc_prediction_l2_v2_responses(base_response):
	def __init__(self,length=1) :
		self.aa_adc_prediction_l2_v2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_adc_prediction_l2_v2_response_array = [ aa_adc_prediction_l2_v2() for _ in range(length)]
