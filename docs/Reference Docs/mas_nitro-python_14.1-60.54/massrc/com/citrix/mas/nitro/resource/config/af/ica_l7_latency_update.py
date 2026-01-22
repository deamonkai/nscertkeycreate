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
Configuration for Af report for ICA Session resource
'''

class ica_l7_latency_update(af_generic_api):
	_id= ""
	_l7_threshold_avg_client_breach= ""
	_l7_threshold_max_server_breach= ""
	_l7_threshold_max_client_breach= ""
	_l7_threshold_configure_value= ""
	___count= ""
	_l7_threshold_avg_server_breach= ""
	_rpt_sample_time= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_l7_latency_update"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ica_l7_latency_update,self).get_object_id()
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
			return "ica_l7_latency_updates"
		except Exception as e :
			raise e


	'''
	Id is ICA Session ID
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is ICA Session ID
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
	L7 Threshold AVG Client Breach Value
	'''
	@property
	def l7_threshold_avg_client_breach(self):
		try:
			return self._l7_threshold_avg_client_breach
		except Exception as e :
			raise e
	'''
	L7 Threshold AVG Client Breach Value
	'''
	@l7_threshold_avg_client_breach.setter
	def l7_threshold_avg_client_breach(self,l7_threshold_avg_client_breach):
		try :
			if not isinstance(l7_threshold_avg_client_breach,float):
				raise TypeError("l7_threshold_avg_client_breach must be set to float value")
			self._l7_threshold_avg_client_breach = l7_threshold_avg_client_breach
		except Exception as e :
			raise e

	'''
	L7 Threshold MAX Server Breach Value
	'''
	@property
	def l7_threshold_max_server_breach(self):
		try:
			return self._l7_threshold_max_server_breach
		except Exception as e :
			raise e
	'''
	L7 Threshold MAX Server Breach Value
	'''
	@l7_threshold_max_server_breach.setter
	def l7_threshold_max_server_breach(self,l7_threshold_max_server_breach):
		try :
			if not isinstance(l7_threshold_max_server_breach,float):
				raise TypeError("l7_threshold_max_server_breach must be set to float value")
			self._l7_threshold_max_server_breach = l7_threshold_max_server_breach
		except Exception as e :
			raise e

	'''
	L7 Threshold MAX Client Breach Value
	'''
	@property
	def l7_threshold_max_client_breach(self):
		try:
			return self._l7_threshold_max_client_breach
		except Exception as e :
			raise e
	'''
	L7 Threshold MAX Client Breach Value
	'''
	@l7_threshold_max_client_breach.setter
	def l7_threshold_max_client_breach(self,l7_threshold_max_client_breach):
		try :
			if not isinstance(l7_threshold_max_client_breach,float):
				raise TypeError("l7_threshold_max_client_breach must be set to float value")
			self._l7_threshold_max_client_breach = l7_threshold_max_client_breach
		except Exception as e :
			raise e

	'''
	L7 Threshold value
	'''
	@property
	def l7_threshold_configure_value(self):
		try:
			return self._l7_threshold_configure_value
		except Exception as e :
			raise e
	'''
	L7 Threshold value
	'''
	@l7_threshold_configure_value.setter
	def l7_threshold_configure_value(self,l7_threshold_configure_value):
		try :
			if not isinstance(l7_threshold_configure_value,float):
				raise TypeError("l7_threshold_configure_value must be set to float value")
			self._l7_threshold_configure_value = l7_threshold_configure_value
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
	L7 Threshold AVG Server Breach Value
	'''
	@property
	def l7_threshold_avg_server_breach(self):
		try:
			return self._l7_threshold_avg_server_breach
		except Exception as e :
			raise e
	'''
	L7 Threshold AVG Server Breach Value
	'''
	@l7_threshold_avg_server_breach.setter
	def l7_threshold_avg_server_breach(self,l7_threshold_avg_server_breach):
		try :
			if not isinstance(l7_threshold_avg_server_breach,float):
				raise TypeError("l7_threshold_avg_server_breach must be set to float value")
			self._l7_threshold_avg_server_breach = l7_threshold_avg_server_breach
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
	Af Report for L7 Latency report.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_l7_latency_update_obj=ica_l7_latency_update()
				response = ica_l7_latency_update_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_l7_latency_update resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_l7_latency_update_obj = ica_l7_latency_update()
			option_ = options()
			option_._filter=filter_
			return ica_l7_latency_update_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_l7_latency_update resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_l7_latency_update_obj = ica_l7_latency_update()
			option_ = options()
			option_._count=True
			response = ica_l7_latency_update_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_l7_latency_update resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_l7_latency_update_obj = ica_l7_latency_update()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_l7_latency_update_obj.getfiltered(service, option_)
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
	Set Query Parameter - sla_enabled
	'''
	@classmethod
	def set_queryparam_sla_enabled(cls, option, value):
		option.add_queryparam("sla_enabled",value)

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
			result=service.payload_formatter.string_to_resource(ica_l7_latency_update_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_l7_latency_update
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_l7_latency_update_responses, response, "ica_l7_latency_update_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_l7_latency_update_response_array
				i=0
				error = [ica_l7_latency_update() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_l7_latency_update_response_array
			i=0
			ica_l7_latency_update_objs = [ica_l7_latency_update() for _ in range(len(response))]
			for obj in response :
				for props in obj._ica_l7_latency_update:
					result = service.payload_formatter.string_to_bulk_resource(ica_l7_latency_update_response,self.__class__.__name__,props)
					ica_l7_latency_update_objs[i] = result.ica_l7_latency_update
					i=i+1
			return ica_l7_latency_update_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_l7_latency_update,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_l7_latency_update_response(base_response):
	def __init__(self,length=1) :
		self.ica_l7_latency_update= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_l7_latency_update= [ ica_l7_latency_update() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_l7_latency_update_responses(base_response):
	def __init__(self,length=1) :
		self.ica_l7_latency_update_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_l7_latency_update_response_array = [ ica_l7_latency_update() for _ in range(length)]
