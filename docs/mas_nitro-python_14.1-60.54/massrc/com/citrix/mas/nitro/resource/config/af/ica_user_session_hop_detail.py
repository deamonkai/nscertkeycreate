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
Configuration for Af report for ICA User Session Hop resource
'''

class ica_user_session_hop_detail(af_generic_api):
	_launch_duration= ""
	_region_code= ""
	_rpt_sample_time= ""
	_client_jitter= ""
	_session_rtt= ""
	_client_side_ns_delay= ""
	_country= ""
	_client_srtt= ""
	_country_code= ""
	_client_type= ""
	___count= ""
	_clientside_cb= ""
	_clientside_packet_retransmits= ""
	_client_version= ""
	_clientside_rto= ""
	_client_ip_address= ""
	_clientside_0_win= ""
	_session_end_time= ""
	_ica_user_name= ""
	_session_setup_time= ""
	_region= ""
	_id= ""
	_edt_type= ""
	_client_latency= ""
	_city= ""
	_l7_clientside_latency= ""
	_state= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_user_session_hop_detail"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ica_user_session_hop_detail,self).get_object_id()
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
			return "ica_user_session_hop_details"
		except Exception as e :
			raise e


	'''
	ica session launch duration.
	'''
	@property
	def launch_duration(self):
		try:
			return self._launch_duration
		except Exception as e :
			raise e
	'''
	ica session launch duration.
	'''
	@launch_duration.setter
	def launch_duration(self,launch_duration):
		try :
			if not isinstance(launch_duration,float):
				raise TypeError("launch_duration must be set to float value")
			self._launch_duration = launch_duration
		except Exception as e :
			raise e

	'''
	region_code
	'''
	@property
	def region_code(self):
		try:
			return self._region_code
		except Exception as e :
			raise e
	'''
	region_code
	'''
	@region_code.setter
	def region_code(self,region_code):
		try :
			if not isinstance(region_code,str):
				raise TypeError("region_code must be set to str value")
			self._region_code = region_code
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
	ICA User client jitter.
	'''
	@property
	def client_jitter(self):
		try:
			return self._client_jitter
		except Exception as e :
			raise e
	'''
	ICA User client jitter.
	'''
	@client_jitter.setter
	def client_jitter(self,client_jitter):
		try :
			if not isinstance(client_jitter,float):
				raise TypeError("client_jitter must be set to float value")
			self._client_jitter = client_jitter
		except Exception as e :
			raise e

	'''
	ICA Session rtt.
	'''
	@property
	def session_rtt(self):
		try:
			return self._session_rtt
		except Exception as e :
			raise e
	'''
	ICA Session rtt.
	'''
	@session_rtt.setter
	def session_rtt(self,session_rtt):
		try :
			if not isinstance(session_rtt,float):
				raise TypeError("session_rtt must be set to float value")
			self._session_rtt = session_rtt
		except Exception as e :
			raise e

	'''
	Client to Server NetScaler delay.
	'''
	@property
	def client_side_ns_delay(self):
		try:
			return self._client_side_ns_delay
		except Exception as e :
			raise e
	'''
	Client to Server NetScaler delay.
	'''
	@client_side_ns_delay.setter
	def client_side_ns_delay(self,client_side_ns_delay):
		try :
			if not isinstance(client_side_ns_delay,float):
				raise TypeError("client_side_ns_delay must be set to float value")
			self._client_side_ns_delay = client_side_ns_delay
		except Exception as e :
			raise e

	'''
	country
	'''
	@property
	def country(self):
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	country
	'''
	@country.setter
	def country(self,country):
		try :
			if not isinstance(country,str):
				raise TypeError("country must be set to str value")
			self._country = country
		except Exception as e :
			raise e

	'''
	client Smothen RTT.
	'''
	@property
	def client_srtt(self):
		try:
			return self._client_srtt
		except Exception as e :
			raise e
	'''
	client Smothen RTT.
	'''
	@client_srtt.setter
	def client_srtt(self,client_srtt):
		try :
			if not isinstance(client_srtt,float):
				raise TypeError("client_srtt must be set to float value")
			self._client_srtt = client_srtt
		except Exception as e :
			raise e

	'''
	country_code
	'''
	@property
	def country_code(self):
		try:
			return self._country_code
		except Exception as e :
			raise e
	'''
	country_code
	'''
	@country_code.setter
	def country_code(self,country_code):
		try :
			if not isinstance(country_code,str):
				raise TypeError("country_code must be set to str value")
			self._country_code = country_code
		except Exception as e :
			raise e

	'''
	Client Type
	'''
	@property
	def client_type(self):
		try:
			return self._client_type
		except Exception as e :
			raise e
	'''
	Client Type
	'''
	@client_type.setter
	def client_type(self,client_type):
		try :
			if not isinstance(client_type,str):
				raise TypeError("client_type must be set to str value")
			self._client_type = client_type
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
	clientside cb
	'''
	@property
	def clientside_cb(self):
		try:
			return self._clientside_cb
		except Exception as e :
			raise e
	'''
	clientside cb
	'''
	@clientside_cb.setter
	def clientside_cb(self,clientside_cb):
		try :
			if not isinstance(clientside_cb,float):
				raise TypeError("clientside_cb must be set to float value")
			self._clientside_cb = clientside_cb
		except Exception as e :
			raise e

	'''
	Client side packet retransmits.
	'''
	@property
	def clientside_packet_retransmits(self):
		try:
			return self._clientside_packet_retransmits
		except Exception as e :
			raise e
	'''
	Client side packet retransmits.
	'''
	@clientside_packet_retransmits.setter
	def clientside_packet_retransmits(self,clientside_packet_retransmits):
		try :
			if not isinstance(clientside_packet_retransmits,float):
				raise TypeError("clientside_packet_retransmits must be set to float value")
			self._clientside_packet_retransmits = clientside_packet_retransmits
		except Exception as e :
			raise e

	'''
	Client Version
	'''
	@property
	def client_version(self):
		try:
			return self._client_version
		except Exception as e :
			raise e
	'''
	Client Version
	'''
	@client_version.setter
	def client_version(self,client_version):
		try :
			if not isinstance(client_version,str):
				raise TypeError("client_version must be set to str value")
			self._client_version = client_version
		except Exception as e :
			raise e

	'''
	clientside rto.
	'''
	@property
	def clientside_rto(self):
		try:
			return self._clientside_rto
		except Exception as e :
			raise e
	'''
	clientside rto.
	'''
	@clientside_rto.setter
	def clientside_rto(self,clientside_rto):
		try :
			if not isinstance(clientside_rto,float):
				raise TypeError("clientside_rto must be set to float value")
			self._clientside_rto = clientside_rto
		except Exception as e :
			raise e

	'''
	Client IP Address.
	'''
	@property
	def client_ip_address(self):
		try:
			return self._client_ip_address
		except Exception as e :
			raise e
	'''
	Client IP Address.
	'''
	@client_ip_address.setter
	def client_ip_address(self,client_ip_address):
		try :
			if not isinstance(client_ip_address,str):
				raise TypeError("client_ip_address must be set to str value")
			self._client_ip_address = client_ip_address
		except Exception as e :
			raise e

	'''
	Client side 0 window count.
	'''
	@property
	def clientside_0_win(self):
		try:
			return self._clientside_0_win
		except Exception as e :
			raise e
	'''
	Client side 0 window count.
	'''
	@clientside_0_win.setter
	def clientside_0_win(self,clientside_0_win):
		try :
			if not isinstance(clientside_0_win,float):
				raise TypeError("clientside_0_win must be set to float value")
			self._clientside_0_win = clientside_0_win
		except Exception as e :
			raise e

	'''
	ICA Session end time.
	'''
	@property
	def session_end_time(self):
		try:
			return self._session_end_time
		except Exception as e :
			raise e
	'''
	ICA Session end time.
	'''
	@session_end_time.setter
	def session_end_time(self,session_end_time):
		try :
			if not isinstance(session_end_time,float):
				raise TypeError("session_end_time must be set to float value")
			self._session_end_time = session_end_time
		except Exception as e :
			raise e

	'''
	Name of ICA User
	'''
	@property
	def ica_user_name(self):
		try:
			return self._ica_user_name
		except Exception as e :
			raise e
	'''
	Name of ICA User
	'''
	@ica_user_name.setter
	def ica_user_name(self,ica_user_name):
		try :
			if not isinstance(ica_user_name,str):
				raise TypeError("ica_user_name must be set to str value")
			self._ica_user_name = ica_user_name
		except Exception as e :
			raise e

	'''
	ICA Session setup time.
	'''
	@property
	def session_setup_time(self):
		try:
			return self._session_setup_time
		except Exception as e :
			raise e
	'''
	ICA Session setup time.
	'''
	@session_setup_time.setter
	def session_setup_time(self,session_setup_time):
		try :
			if not isinstance(session_setup_time,float):
				raise TypeError("session_setup_time must be set to float value")
			self._session_setup_time = session_setup_time
		except Exception as e :
			raise e

	'''
	region
	'''
	@property
	def region(self):
		try:
			return self._region
		except Exception as e :
			raise e
	'''
	region
	'''
	@region.setter
	def region(self,region):
		try :
			if not isinstance(region,str):
				raise TypeError("region must be set to str value")
			self._region = region
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
	edt_type
	'''
	@property
	def edt_type(self):
		try:
			return self._edt_type
		except Exception as e :
			raise e
	'''
	edt_type
	'''
	@edt_type.setter
	def edt_type(self,edt_type):
		try :
			if not isinstance(edt_type,str):
				raise TypeError("edt_type must be set to str value")
			self._edt_type = edt_type
		except Exception as e :
			raise e

	'''
	ica session client latency.
	'''
	@property
	def client_latency(self):
		try:
			return self._client_latency
		except Exception as e :
			raise e
	'''
	ica session client latency.
	'''
	@client_latency.setter
	def client_latency(self,client_latency):
		try :
			if not isinstance(client_latency,float):
				raise TypeError("client_latency must be set to float value")
			self._client_latency = client_latency
		except Exception as e :
			raise e

	'''
	city
	'''
	@property
	def city(self):
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	city
	'''
	@city.setter
	def city(self,city):
		try :
			if not isinstance(city,str):
				raise TypeError("city must be set to str value")
			self._city = city
		except Exception as e :
			raise e

	'''
	L7 clientside latency
	'''
	@property
	def l7_clientside_latency(self):
		try:
			return self._l7_clientside_latency
		except Exception as e :
			raise e
	'''
	L7 clientside latency
	'''
	@l7_clientside_latency.setter
	def l7_clientside_latency(self,l7_clientside_latency):
		try :
			if not isinstance(l7_clientside_latency,float):
				raise TypeError("l7_clientside_latency must be set to float value")
			self._l7_clientside_latency = l7_clientside_latency
		except Exception as e :
			raise e

	'''
	ICA Session state.
	'''
	@property
	def state(self):
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	ICA Session state.
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
		except Exception as e :
			raise e

	'''
	Af Report for ICA User..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_user_session_hop_detail_obj=ica_user_session_hop_detail()
				response = ica_user_session_hop_detail_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_user_session_hop_detail resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_user_session_hop_detail_obj = ica_user_session_hop_detail()
			option_ = options()
			option_._filter=filter_
			return ica_user_session_hop_detail_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_user_session_hop_detail resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_user_session_hop_detail_obj = ica_user_session_hop_detail()
			option_ = options()
			option_._count=True
			response = ica_user_session_hop_detail_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_user_session_hop_detail resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_user_session_hop_detail_obj = ica_user_session_hop_detail()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_user_session_hop_detail_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ica_user_session_hop_detail_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_user_session_hop_detail
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_user_session_hop_detail_responses, response, "ica_user_session_hop_detail_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_user_session_hop_detail_response_array
				i=0
				error = [ica_user_session_hop_detail() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_user_session_hop_detail_response_array
			i=0
			ica_user_session_hop_detail_objs = [ica_user_session_hop_detail() for _ in range(len(response))]
			for obj in response :
				for props in obj._ica_user_session_hop_detail:
					result = service.payload_formatter.string_to_bulk_resource(ica_user_session_hop_detail_response,self.__class__.__name__,props)
					ica_user_session_hop_detail_objs[i] = result.ica_user_session_hop_detail
					i=i+1
			return ica_user_session_hop_detail_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_user_session_hop_detail,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_user_session_hop_detail_response(base_response):
	def __init__(self,length=1) :
		self.ica_user_session_hop_detail= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_user_session_hop_detail= [ ica_user_session_hop_detail() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_user_session_hop_detail_responses(base_response):
	def __init__(self,length=1) :
		self.ica_user_session_hop_detail_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_user_session_hop_detail_response_array = [ ica_user_session_hop_detail() for _ in range(length)]
