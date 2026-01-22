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
Configuration for Provide the widget level configurations resource
'''

class uber_dashboard_config(base_resource):
	_gateway_high_ica_rtt= ""
	_gateway_high_host_delay= ""
	_gateway_high_dc_latency= ""
	_gateway_high_wan_latency= ""
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
			return "uber_dashboard_config"
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
			return "uber_dashboard_configs"
		except Exception as e :
			raise e



	'''
	get Configure Gateway ICA RTT threshold
	'''
	@property
	def gateway_high_ica_rtt(self) :
		try:
			return self._gateway_high_ica_rtt
		except Exception as e :
			raise e
	'''
	set Configure Gateway ICA RTT threshold
	'''
	@gateway_high_ica_rtt.setter
	def gateway_high_ica_rtt(self,gateway_high_ica_rtt):
		try :
			if not isinstance(gateway_high_ica_rtt,int):
				raise TypeError("gateway_high_ica_rtt must be set to int value")
			self._gateway_high_ica_rtt = gateway_high_ica_rtt
		except Exception as e :
			raise e


	'''
	get Configure Gateway Host Delay threshold
	'''
	@property
	def gateway_high_host_delay(self) :
		try:
			return self._gateway_high_host_delay
		except Exception as e :
			raise e
	'''
	set Configure Gateway Host Delay threshold
	'''
	@gateway_high_host_delay.setter
	def gateway_high_host_delay(self,gateway_high_host_delay):
		try :
			if not isinstance(gateway_high_host_delay,int):
				raise TypeError("gateway_high_host_delay must be set to int value")
			self._gateway_high_host_delay = gateway_high_host_delay
		except Exception as e :
			raise e


	'''
	get Configure Gateway Data Center Latency threshold
	'''
	@property
	def gateway_high_dc_latency(self) :
		try:
			return self._gateway_high_dc_latency
		except Exception as e :
			raise e
	'''
	set Configure Gateway Data Center Latency threshold
	'''
	@gateway_high_dc_latency.setter
	def gateway_high_dc_latency(self,gateway_high_dc_latency):
		try :
			if not isinstance(gateway_high_dc_latency,int):
				raise TypeError("gateway_high_dc_latency must be set to int value")
			self._gateway_high_dc_latency = gateway_high_dc_latency
		except Exception as e :
			raise e


	'''
	get Configure Gateway WAN Latency threshold
	'''
	@property
	def gateway_high_wan_latency(self) :
		try:
			return self._gateway_high_wan_latency
		except Exception as e :
			raise e
	'''
	set Configure Gateway WAN Latency threshold
	'''
	@gateway_high_wan_latency.setter
	def gateway_high_wan_latency(self,gateway_high_wan_latency):
		try :
			if not isinstance(gateway_high_wan_latency,int):
				raise TypeError("gateway_high_wan_latency must be set to int value")
			self._gateway_high_wan_latency = gateway_high_wan_latency
		except Exception as e :
			raise e

	'''
	To get config value.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				uber_dashboard_config_obj=uber_dashboard_config()
				response = uber_dashboard_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	To set config value.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				uber_dashboard_config_obj=uber_dashboard_config()
				return cls.update_bulk_request(client,resource,uber_dashboard_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of uber_dashboard_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			uber_dashboard_config_obj = uber_dashboard_config()
			option_ = options()
			option_._filter=filter_
			return uber_dashboard_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the uber_dashboard_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			uber_dashboard_config_obj = uber_dashboard_config()
			option_ = options()
			option_._count=True
			response = uber_dashboard_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of uber_dashboard_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			uber_dashboard_config_obj = uber_dashboard_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = uber_dashboard_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(uber_dashboard_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.uber_dashboard_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(uber_dashboard_config_responses, response, "uber_dashboard_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.uber_dashboard_config_response_array
				i=0
				error = [uber_dashboard_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.uber_dashboard_config_response_array
			i=0
			uber_dashboard_config_objs = [uber_dashboard_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_uber_dashboard_config'):
					for props in obj._uber_dashboard_config:
						result = service.payload_formatter.string_to_bulk_resource(uber_dashboard_config_response,self.__class__.__name__,props)
						uber_dashboard_config_objs[i] = result.uber_dashboard_config
						i=i+1
			return uber_dashboard_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(uber_dashboard_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class uber_dashboard_config_response(base_response):
	def __init__(self,length=1) :
		self.uber_dashboard_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.uber_dashboard_config= [ uber_dashboard_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class uber_dashboard_config_responses(base_response):
	def __init__(self,length=1) :
		self.uber_dashboard_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.uber_dashboard_config_response_array = [ uber_dashboard_config() for _ in range(length)]
