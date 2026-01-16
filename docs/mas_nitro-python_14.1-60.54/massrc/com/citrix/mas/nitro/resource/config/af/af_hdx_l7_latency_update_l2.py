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
Configuration for AF HDX L7 latency update  resource
'''

class af_hdx_l7_latency_update_l2(base_resource):
	_l7_max_client_breach_latency= ""
	_breach_configured_value= ""
	_rpt_sample_time= ""
	_session_id= ""
	_l7_avg_client_breach_latency= ""
	_exporter_id= ""
	_ctnsappname= ""
	_l7_avg_server_breach_latency= ""
	_ip_address= ""
	_l7_max_server_breach_latency= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_hdx_l7_latency_update_l2"
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
			return "af_hdx_l7_latency_update_l2s"
		except Exception as e :
			raise e



	'''
	get L7 MAX Client Breach Latency
	'''
	@property
	def l7_max_client_breach_latency(self) :
		try:
			return self._l7_max_client_breach_latency
		except Exception as e :
			raise e
	'''
	set L7 MAX Client Breach Latency
	'''
	@l7_max_client_breach_latency.setter
	def l7_max_client_breach_latency(self,l7_max_client_breach_latency):
		try :
			if not isinstance(l7_max_client_breach_latency,int):
				raise TypeError("l7_max_client_breach_latency must be set to int value")
			self._l7_max_client_breach_latency = l7_max_client_breach_latency
		except Exception as e :
			raise e


	'''
	get L7 Breach Configured value
	'''
	@property
	def breach_configured_value(self) :
		try:
			return self._breach_configured_value
		except Exception as e :
			raise e
	'''
	set L7 Breach Configured value
	'''
	@breach_configured_value.setter
	def breach_configured_value(self,breach_configured_value):
		try :
			if not isinstance(breach_configured_value,int):
				raise TypeError("breach_configured_value must be set to int value")
			self._breach_configured_value = breach_configured_value
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
	get Session GUID.
	'''
	@property
	def session_id(self) :
		try:
			return self._session_id
		except Exception as e :
			raise e
	'''
	set Session GUID.
	'''
	@session_id.setter
	def session_id(self,session_id):
		try :
			if not isinstance(session_id,str):
				raise TypeError("session_id must be set to str value")
			self._session_id = session_id
		except Exception as e :
			raise e


	'''
	get L7 Average Client Breach Latency
	'''
	@property
	def l7_avg_client_breach_latency(self) :
		try:
			return self._l7_avg_client_breach_latency
		except Exception as e :
			raise e
	'''
	set L7 Average Client Breach Latency
	'''
	@l7_avg_client_breach_latency.setter
	def l7_avg_client_breach_latency(self,l7_avg_client_breach_latency):
		try :
			if not isinstance(l7_avg_client_breach_latency,float):
				raise TypeError("l7_avg_client_breach_latency must be set to float value")
			self._l7_avg_client_breach_latency = l7_avg_client_breach_latency
		except Exception as e :
			raise e


	'''
	get Exporter ID
	'''
	@property
	def exporter_id(self) :
		try:
			return self._exporter_id
		except Exception as e :
			raise e
	'''
	set Exporter ID
	'''
	@exporter_id.setter
	def exporter_id(self,exporter_id):
		try :
			if not isinstance(exporter_id,long):
				raise TypeError("exporter_id must be set to long value")
			self._exporter_id = exporter_id
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
	get L7 Average Server Breach Latency
	'''
	@property
	def l7_avg_server_breach_latency(self) :
		try:
			return self._l7_avg_server_breach_latency
		except Exception as e :
			raise e
	'''
	set L7 Average Server Breach Latency
	'''
	@l7_avg_server_breach_latency.setter
	def l7_avg_server_breach_latency(self,l7_avg_server_breach_latency):
		try :
			if not isinstance(l7_avg_server_breach_latency,float):
				raise TypeError("l7_avg_server_breach_latency must be set to float value")
			self._l7_avg_server_breach_latency = l7_avg_server_breach_latency
		except Exception as e :
			raise e


	'''
	get Field to store the ip address as it is along with any extension
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Field to store the ip address as it is along with any extension
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
	get L7 Max Server Breach Latency
	'''
	@property
	def l7_max_server_breach_latency(self) :
		try:
			return self._l7_max_server_breach_latency
		except Exception as e :
			raise e
	'''
	set L7 Max Server Breach Latency
	'''
	@l7_max_server_breach_latency.setter
	def l7_max_server_breach_latency(self,l7_max_server_breach_latency):
		try :
			if not isinstance(l7_max_server_breach_latency,int):
				raise TypeError("l7_max_server_breach_latency must be set to int value")
			self._l7_max_server_breach_latency = l7_max_server_breach_latency
		except Exception as e :
			raise e

	'''
	Af HDX Report for ICA User Duration update collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_hdx_l7_latency_update_l2_obj=af_hdx_l7_latency_update_l2()
				response = af_hdx_l7_latency_update_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_hdx_l7_latency_update_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_hdx_l7_latency_update_l2_obj = af_hdx_l7_latency_update_l2()
			option_ = options()
			option_._filter=filter_
			return af_hdx_l7_latency_update_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_hdx_l7_latency_update_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_hdx_l7_latency_update_l2_obj = af_hdx_l7_latency_update_l2()
			option_ = options()
			option_._count=True
			response = af_hdx_l7_latency_update_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_hdx_l7_latency_update_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_hdx_l7_latency_update_l2_obj = af_hdx_l7_latency_update_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_hdx_l7_latency_update_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_hdx_l7_latency_update_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_hdx_l7_latency_update_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_hdx_l7_latency_update_l2_responses, response, "af_hdx_l7_latency_update_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_hdx_l7_latency_update_l2_response_array
				i=0
				error = [af_hdx_l7_latency_update_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_hdx_l7_latency_update_l2_response_array
			i=0
			af_hdx_l7_latency_update_l2_objs = [af_hdx_l7_latency_update_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_hdx_l7_latency_update_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_hdx_l7_latency_update_l2_response,self.__class__.__name__,props)
					af_hdx_l7_latency_update_l2_objs[i] = result.af_hdx_l7_latency_update_l2
					i=i+1
			return af_hdx_l7_latency_update_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_hdx_l7_latency_update_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_hdx_l7_latency_update_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_hdx_l7_latency_update_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_hdx_l7_latency_update_l2= [ af_hdx_l7_latency_update_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_hdx_l7_latency_update_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_hdx_l7_latency_update_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_hdx_l7_latency_update_l2_response_array = [ af_hdx_l7_latency_update_l2() for _ in range(length)]
