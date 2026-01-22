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
Configuration for Af report for ICA Server session hop detail resource
'''

class ica_server_session_hop_detail(af_generic_api):
	_serverside_cb= ""
	_server_latency= ""
	_id= ""
	_ica_user_name= ""
	_session_setup_time= ""
	_host_delay= ""
	_state= ""
	___count= ""
	_server_srtt= ""
	_edt_type= ""
	_server_side_ns_delay= ""
	_serverside_0_win= ""
	_server_jitter= ""
	_server_ip_address= ""
	_serverside_rto= ""
	_launch_duration= ""
	_session_rtt= ""
	_serverside_packet_retransmits= ""
	_session_end_time= ""
	_rpt_sample_time= ""
	_l7_serverside_latency= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_server_session_hop_detail"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ica_server_session_hop_detail,self).get_object_id()
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
			return "ica_server_session_hop_details"
		except Exception as e :
			raise e


	'''
	serverside cb
	'''
	@property
	def serverside_cb(self):
		try:
			return self._serverside_cb
		except Exception as e :
			raise e
	'''
	serverside cb
	'''
	@serverside_cb.setter
	def serverside_cb(self,serverside_cb):
		try :
			if not isinstance(serverside_cb,float):
				raise TypeError("serverside_cb must be set to float value")
			self._serverside_cb = serverside_cb
		except Exception as e :
			raise e

	'''
	ica session server latency.
	'''
	@property
	def server_latency(self):
		try:
			return self._server_latency
		except Exception as e :
			raise e
	'''
	ica session server latency.
	'''
	@server_latency.setter
	def server_latency(self,server_latency):
		try :
			if not isinstance(server_latency,float):
				raise TypeError("server_latency must be set to float value")
			self._server_latency = server_latency
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
	Server induced delay.
	'''
	@property
	def host_delay(self):
		try:
			return self._host_delay
		except Exception as e :
			raise e
	'''
	Server induced delay.
	'''
	@host_delay.setter
	def host_delay(self,host_delay):
		try :
			if not isinstance(host_delay,float):
				raise TypeError("host_delay must be set to float value")
			self._host_delay = host_delay
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
	server Smothen RTT.
	'''
	@property
	def server_srtt(self):
		try:
			return self._server_srtt
		except Exception as e :
			raise e
	'''
	server Smothen RTT.
	'''
	@server_srtt.setter
	def server_srtt(self,server_srtt):
		try :
			if not isinstance(server_srtt,float):
				raise TypeError("server_srtt must be set to float value")
			self._server_srtt = server_srtt
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
	Server to Client NetScaler delay.
	'''
	@property
	def server_side_ns_delay(self):
		try:
			return self._server_side_ns_delay
		except Exception as e :
			raise e
	'''
	Server to Client NetScaler delay.
	'''
	@server_side_ns_delay.setter
	def server_side_ns_delay(self,server_side_ns_delay):
		try :
			if not isinstance(server_side_ns_delay,float):
				raise TypeError("server_side_ns_delay must be set to float value")
			self._server_side_ns_delay = server_side_ns_delay
		except Exception as e :
			raise e

	'''
	server side 0 window count.
	'''
	@property
	def serverside_0_win(self):
		try:
			return self._serverside_0_win
		except Exception as e :
			raise e
	'''
	server side 0 window count.
	'''
	@serverside_0_win.setter
	def serverside_0_win(self,serverside_0_win):
		try :
			if not isinstance(serverside_0_win,float):
				raise TypeError("serverside_0_win must be set to float value")
			self._serverside_0_win = serverside_0_win
		except Exception as e :
			raise e

	'''
	ICA User server jitter.
	'''
	@property
	def server_jitter(self):
		try:
			return self._server_jitter
		except Exception as e :
			raise e
	'''
	ICA User server jitter.
	'''
	@server_jitter.setter
	def server_jitter(self,server_jitter):
		try :
			if not isinstance(server_jitter,float):
				raise TypeError("server_jitter must be set to float value")
			self._server_jitter = server_jitter
		except Exception as e :
			raise e

	'''
	Server IP Address.
	'''
	@property
	def server_ip_address(self):
		try:
			return self._server_ip_address
		except Exception as e :
			raise e
	'''
	Server IP Address.
	'''
	@server_ip_address.setter
	def server_ip_address(self,server_ip_address):
		try :
			if not isinstance(server_ip_address,str):
				raise TypeError("server_ip_address must be set to str value")
			self._server_ip_address = server_ip_address
		except Exception as e :
			raise e

	'''
	serverside rto.
	'''
	@property
	def serverside_rto(self):
		try:
			return self._serverside_rto
		except Exception as e :
			raise e
	'''
	serverside rto.
	'''
	@serverside_rto.setter
	def serverside_rto(self,serverside_rto):
		try :
			if not isinstance(serverside_rto,float):
				raise TypeError("serverside_rto must be set to float value")
			self._serverside_rto = serverside_rto
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
	Server side packet retransmits.
	'''
	@property
	def serverside_packet_retransmits(self):
		try:
			return self._serverside_packet_retransmits
		except Exception as e :
			raise e
	'''
	Server side packet retransmits.
	'''
	@serverside_packet_retransmits.setter
	def serverside_packet_retransmits(self,serverside_packet_retransmits):
		try :
			if not isinstance(serverside_packet_retransmits,float):
				raise TypeError("serverside_packet_retransmits must be set to float value")
			self._serverside_packet_retransmits = serverside_packet_retransmits
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
	L7 serverside latency
	'''
	@property
	def l7_serverside_latency(self):
		try:
			return self._l7_serverside_latency
		except Exception as e :
			raise e
	'''
	L7 serverside latency
	'''
	@l7_serverside_latency.setter
	def l7_serverside_latency(self,l7_serverside_latency):
		try :
			if not isinstance(l7_serverside_latency,float):
				raise TypeError("l7_serverside_latency must be set to float value")
			self._l7_serverside_latency = l7_serverside_latency
		except Exception as e :
			raise e

	'''
	Af Report for ICA Server Session Hop Detail..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_server_session_hop_detail_obj=ica_server_session_hop_detail()
				response = ica_server_session_hop_detail_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_server_session_hop_detail resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_server_session_hop_detail_obj = ica_server_session_hop_detail()
			option_ = options()
			option_._filter=filter_
			return ica_server_session_hop_detail_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_server_session_hop_detail resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_server_session_hop_detail_obj = ica_server_session_hop_detail()
			option_ = options()
			option_._count=True
			response = ica_server_session_hop_detail_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_server_session_hop_detail resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_server_session_hop_detail_obj = ica_server_session_hop_detail()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_server_session_hop_detail_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ica_server_session_hop_detail_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_server_session_hop_detail
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_server_session_hop_detail_responses, response, "ica_server_session_hop_detail_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_server_session_hop_detail_response_array
				i=0
				error = [ica_server_session_hop_detail() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_server_session_hop_detail_response_array
			i=0
			ica_server_session_hop_detail_objs = [ica_server_session_hop_detail() for _ in range(len(response))]
			for obj in response :
				for props in obj._ica_server_session_hop_detail:
					result = service.payload_formatter.string_to_bulk_resource(ica_server_session_hop_detail_response,self.__class__.__name__,props)
					ica_server_session_hop_detail_objs[i] = result.ica_server_session_hop_detail
					i=i+1
			return ica_server_session_hop_detail_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_server_session_hop_detail,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_server_session_hop_detail_response(base_response):
	def __init__(self,length=1) :
		self.ica_server_session_hop_detail= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_server_session_hop_detail= [ ica_server_session_hop_detail() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_server_session_hop_detail_responses(base_response):
	def __init__(self,length=1) :
		self.ica_server_session_hop_detail_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_server_session_hop_detail_response_array = [ ica_server_session_hop_detail() for _ in range(length)]
