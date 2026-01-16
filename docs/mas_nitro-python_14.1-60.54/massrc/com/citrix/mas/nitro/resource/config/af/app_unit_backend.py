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
Configuration for AF APP Report table resource
'''

class app_unit_backend(af_generic_api):
	_application_name= ""
	_total_requests= ""
	_total_bytes= ""
	_application_response_time= ""
	_vservername= ""
	_network_latency_client_side= ""
	_device_ip_address= ""
	_network_latency_server_side= ""
	_rpt_sample_time= ""
	_ctnsappname_b= ""
	_netscaler_processing_time= ""
	_server_response_time= ""
	___count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "app_unit_backend"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(app_unit_backend,self).get_object_id()
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
			return "app_unit_backends"
		except Exception as e :
			raise e


	'''
	Application Name
	'''
	@property
	def application_name(self):
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	Application Name
	'''
	@application_name.setter
	def application_name(self,application_name):
		try :
			if not isinstance(application_name,str):
				raise TypeError("application_name must be set to str value")
			self._application_name = application_name
		except Exception as e :
			raise e

	'''
	Total requests to this Application in given sampled timeframe.
	'''
	@property
	def total_requests(self):
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	Total requests to this Application in given sampled timeframe.
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
	Total bytes accounted by this Application in sampled timeframe.
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes accounted by this Application in sampled timeframe.
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
	Application response time.
	'''
	@property
	def application_response_time(self):
		try:
			return self._application_response_time
		except Exception as e :
			raise e
	'''
	Application response time.
	'''
	@application_response_time.setter
	def application_response_time(self,application_response_time):
		try :
			if not isinstance(application_response_time,float):
				raise TypeError("application_response_time must be set to float value")
			self._application_response_time = application_response_time
		except Exception as e :
			raise e

	'''
	Application Name
	'''
	@property
	def vservername(self):
		try:
			return self._vservername
		except Exception as e :
			raise e
	'''
	Application Name
	'''
	@vservername.setter
	def vservername(self,vservername):
		try :
			if not isinstance(vservername,str):
				raise TypeError("vservername must be set to str value")
			self._vservername = vservername
		except Exception as e :
			raise e

	'''
	Network latency client side.
	'''
	@property
	def network_latency_client_side(self):
		try:
			return self._network_latency_client_side
		except Exception as e :
			raise e
	'''
	Network latency client side.
	'''
	@network_latency_client_side.setter
	def network_latency_client_side(self,network_latency_client_side):
		try :
			if not isinstance(network_latency_client_side,float):
				raise TypeError("network_latency_client_side must be set to float value")
			self._network_latency_client_side = network_latency_client_side
		except Exception as e :
			raise e

	'''
	NetScaler IP Address.
	'''
	@property
	def device_ip_address(self):
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address.
	'''
	@device_ip_address.setter
	def device_ip_address(self,device_ip_address):
		try :
			if not isinstance(device_ip_address,str):
				raise TypeError("device_ip_address must be set to str value")
			self._device_ip_address = device_ip_address
		except Exception as e :
			raise e

	'''
	Network latency server side.
	'''
	@property
	def network_latency_server_side(self):
		try:
			return self._network_latency_server_side
		except Exception as e :
			raise e
	'''
	Network latency server side.
	'''
	@network_latency_server_side.setter
	def network_latency_server_side(self,network_latency_server_side):
		try :
			if not isinstance(network_latency_server_side,float):
				raise TypeError("network_latency_server_side must be set to float value")
			self._network_latency_server_side = network_latency_server_side
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
	Backend Application Name
	'''
	@property
	def ctnsappname_b(self):
		try:
			return self._ctnsappname_b
		except Exception as e :
			raise e
	'''
	Backend Application Name
	'''
	@ctnsappname_b.setter
	def ctnsappname_b(self,ctnsappname_b):
		try :
			if not isinstance(ctnsappname_b,str):
				raise TypeError("ctnsappname_b must be set to str value")
			self._ctnsappname_b = ctnsappname_b
		except Exception as e :
			raise e

	'''
	NetScaler processing time.
	'''
	@property
	def netscaler_processing_time(self):
		try:
			return self._netscaler_processing_time
		except Exception as e :
			raise e
	'''
	NetScaler processing time.
	'''
	@netscaler_processing_time.setter
	def netscaler_processing_time(self,netscaler_processing_time):
		try :
			if not isinstance(netscaler_processing_time,float):
				raise TypeError("netscaler_processing_time must be set to float value")
			self._netscaler_processing_time = netscaler_processing_time
		except Exception as e :
			raise e

	'''
	Server response time.
	'''
	@property
	def server_response_time(self):
		try:
			return self._server_response_time
		except Exception as e :
			raise e
	'''
	Server response time.
	'''
	@server_response_time.setter
	def server_response_time(self,server_response_time):
		try :
			if not isinstance(server_response_time,float):
				raise TypeError("server_response_time must be set to float value")
			self._server_response_time = server_response_time
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
	Af Report for Top Backend APP by Request Count Managed by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				app_unit_backend_obj=app_unit_backend()
				response = app_unit_backend_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of app_unit_backend resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			app_unit_backend_obj = app_unit_backend()
			option_ = options()
			option_._filter=filter_
			return app_unit_backend_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the app_unit_backend resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			app_unit_backend_obj = app_unit_backend()
			option_ = options()
			option_._count=True
			response = app_unit_backend_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of app_unit_backend resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			app_unit_backend_obj = app_unit_backend()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = app_unit_backend_obj.getfiltered(service, option_)
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
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_unit_backend_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.app_unit_backend
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_unit_backend_responses, response, "app_unit_backend_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.app_unit_backend_response_array
				i=0
				error = [app_unit_backend() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.app_unit_backend_response_array
			i=0
			app_unit_backend_objs = [app_unit_backend() for _ in range(len(response))]
			for obj in response :
				for props in obj._app_unit_backend:
					result = service.payload_formatter.string_to_bulk_resource(app_unit_backend_response,self.__class__.__name__,props)
					app_unit_backend_objs[i] = result.app_unit_backend
					i=i+1
			return app_unit_backend_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(app_unit_backend,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class app_unit_backend_response(base_response):
	def __init__(self,length=1) :
		self.app_unit_backend= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.app_unit_backend= [ app_unit_backend() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class app_unit_backend_responses(base_response):
	def __init__(self,length=1) :
		self.app_unit_backend_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.app_unit_backend_response_array = [ app_unit_backend() for _ in range(length)]
