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
Configuration for Af report for ICA Device Skip flow details resource
'''

class ica_device_skip_flow_details(af_generic_api):
	___count= ""
	_ica_app_name= ""
	_session_reconnect= ""
	_host_delay= ""
	_client_srtt= ""
	_client_tx_bytes= ""
	_skipflow_description= ""
	_server_latency= ""
	_up_time= ""
	_rpt_sample_time= ""
	_client_jitter= ""
	_serverside_packet_retransmits= ""
	_session_rtt= ""
	_client_side_ns_delay= ""
	_launch_duration= ""
	_server_ip_address= ""
	_serverside_rto= ""
	_serverside_0_win= ""
	_ica_device_ip_address= ""
	_group_reason_id= ""
	_server_srtt= ""
	_skipflow_count= ""
	_state= ""
	_client_latency= ""
	_session_setup_time= ""
	_ica_user_name= ""
	_id= ""
	_client_rx_bytes= ""
	_pn_agent_version= ""
	_skipflow_reason_id= ""
	_clientside_rto= ""
	_client_ip_address= ""
	_application_enumeration_duration= ""
	_receiver_version= ""
	_clientside_0_win= ""
	_session_end_time= ""
	_bandwidth= ""
	_server_jitter= ""
	_clientside_packet_retransmits= ""
	_total_bytes= ""
	_server_side_ns_delay= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_device_skip_flow_details"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ica_device_skip_flow_details,self).get_object_id()
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
			return "ica_device_skip_flow_detailss"
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
	Name of ICA app
	'''
	@property
	def ica_app_name(self):
		try:
			return self._ica_app_name
		except Exception as e :
			raise e
	'''
	Name of ICA app
	'''
	@ica_app_name.setter
	def ica_app_name(self,ica_app_name):
		try :
			if not isinstance(ica_app_name,str):
				raise TypeError("ica_app_name must be set to str value")
			self._ica_app_name = ica_app_name
		except Exception as e :
			raise e

	'''
	Session reconnect.
	'''
	@property
	def session_reconnect(self):
		try:
			return self._session_reconnect
		except Exception as e :
			raise e
	'''
	Session reconnect.
	'''
	@session_reconnect.setter
	def session_reconnect(self,session_reconnect):
		try :
			if not isinstance(session_reconnect,float):
				raise TypeError("session_reconnect must be set to float value")
			self._session_reconnect = session_reconnect
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
	Client Side Tx bytes.
	'''
	@property
	def client_tx_bytes(self):
		try:
			return self._client_tx_bytes
		except Exception as e :
			raise e
	'''
	Client Side Tx bytes.
	'''
	@client_tx_bytes.setter
	def client_tx_bytes(self,client_tx_bytes):
		try :
			if not isinstance(client_tx_bytes,float):
				raise TypeError("client_tx_bytes must be set to float value")
			self._client_tx_bytes = client_tx_bytes
		except Exception as e :
			raise e

	'''
	Reason for skip flow.
	'''
	@property
	def skipflow_description(self):
		try:
			return self._skipflow_description
		except Exception as e :
			raise e
	'''
	Reason for skip flow.
	'''
	@skipflow_description.setter
	def skipflow_description(self,skipflow_description):
		try :
			if not isinstance(skipflow_description,str):
				raise TypeError("skipflow_description must be set to str value")
			self._skipflow_description = skipflow_description
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
	ica session up time.
	'''
	@property
	def up_time(self):
		try:
			return self._up_time
		except Exception as e :
			raise e
	'''
	ica session up time.
	'''
	@up_time.setter
	def up_time(self,up_time):
		try :
			if not isinstance(up_time,float):
				raise TypeError("up_time must be set to float value")
			self._up_time = up_time
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
	ICA Device IP Address.
	'''
	@property
	def ica_device_ip_address(self):
		try:
			return self._ica_device_ip_address
		except Exception as e :
			raise e
	'''
	ICA Device IP Address.
	'''
	@ica_device_ip_address.setter
	def ica_device_ip_address(self,ica_device_ip_address):
		try :
			if not isinstance(ica_device_ip_address,str):
				raise TypeError("ica_device_ip_address must be set to str value")
			self._ica_device_ip_address = ica_device_ip_address
		except Exception as e :
			raise e

	'''
	Skip flow group reason id.
	'''
	@property
	def group_reason_id(self):
		try:
			return self._group_reason_id
		except Exception as e :
			raise e
	'''
	Skip flow group reason id.
	'''
	@group_reason_id.setter
	def group_reason_id(self,group_reason_id):
		try :
			if not isinstance(group_reason_id,float):
				raise TypeError("group_reason_id must be set to float value")
			self._group_reason_id = group_reason_id
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
	Skip flow count..
	'''
	@property
	def skipflow_count(self):
		try:
			return self._skipflow_count
		except Exception as e :
			raise e
	'''
	Skip flow count..
	'''
	@skipflow_count.setter
	def skipflow_count(self,skipflow_count):
		try :
			if not isinstance(skipflow_count,float):
				raise TypeError("skipflow_count must be set to float value")
			self._skipflow_count = skipflow_count
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
	Client Side Rx bytes.
	'''
	@property
	def client_rx_bytes(self):
		try:
			return self._client_rx_bytes
		except Exception as e :
			raise e
	'''
	Client Side Rx bytes.
	'''
	@client_rx_bytes.setter
	def client_rx_bytes(self,client_rx_bytes):
		try :
			if not isinstance(client_rx_bytes,float):
				raise TypeError("client_rx_bytes must be set to float value")
			self._client_rx_bytes = client_rx_bytes
		except Exception as e :
			raise e

	'''
	Name of ICA session pn agent version
	'''
	@property
	def pn_agent_version(self):
		try:
			return self._pn_agent_version
		except Exception as e :
			raise e
	'''
	Name of ICA session pn agent version
	'''
	@pn_agent_version.setter
	def pn_agent_version(self,pn_agent_version):
		try :
			if not isinstance(pn_agent_version,str):
				raise TypeError("pn_agent_version must be set to str value")
			self._pn_agent_version = pn_agent_version
		except Exception as e :
			raise e

	'''
	Skip flow reason id.
	'''
	@property
	def skipflow_reason_id(self):
		try:
			return self._skipflow_reason_id
		except Exception as e :
			raise e
	'''
	Skip flow reason id.
	'''
	@skipflow_reason_id.setter
	def skipflow_reason_id(self,skipflow_reason_id):
		try :
			if not isinstance(skipflow_reason_id,float):
				raise TypeError("skipflow_reason_id must be set to float value")
			self._skipflow_reason_id = skipflow_reason_id
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
	Time taken for app enumeration to launch.
	'''
	@property
	def application_enumeration_duration(self):
		try:
			return self._application_enumeration_duration
		except Exception as e :
			raise e
	'''
	Time taken for app enumeration to launch.
	'''
	@application_enumeration_duration.setter
	def application_enumeration_duration(self,application_enumeration_duration):
		try :
			if not isinstance(application_enumeration_duration,float):
				raise TypeError("application_enumeration_duration must be set to float value")
			self._application_enumeration_duration = application_enumeration_duration
		except Exception as e :
			raise e

	'''
	Name of ICA session receiver version
	'''
	@property
	def receiver_version(self):
		try:
			return self._receiver_version
		except Exception as e :
			raise e
	'''
	Name of ICA session receiver version
	'''
	@receiver_version.setter
	def receiver_version(self,receiver_version):
		try :
			if not isinstance(receiver_version,str):
				raise TypeError("receiver_version must be set to str value")
			self._receiver_version = receiver_version
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
	Avg Bandwidth.
	'''
	@property
	def bandwidth(self):
		try:
			return self._bandwidth
		except Exception as e :
			raise e
	'''
	Avg Bandwidth.
	'''
	@bandwidth.setter
	def bandwidth(self,bandwidth):
		try :
			if not isinstance(bandwidth,float):
				raise TypeError("bandwidth must be set to float value")
			self._bandwidth = bandwidth
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
	Total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes accounted by this URL in sampled timeframe.
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
	Af Report for ICA Device Skip Flow details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_device_skip_flow_details_obj=ica_device_skip_flow_details()
				response = ica_device_skip_flow_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_device_skip_flow_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_device_skip_flow_details_obj = ica_device_skip_flow_details()
			option_ = options()
			option_._filter=filter_
			return ica_device_skip_flow_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_device_skip_flow_details resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_device_skip_flow_details_obj = ica_device_skip_flow_details()
			option_ = options()
			option_._count=True
			response = ica_device_skip_flow_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_device_skip_flow_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_device_skip_flow_details_obj = ica_device_skip_flow_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_device_skip_flow_details_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ica_device_skip_flow_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_device_skip_flow_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_device_skip_flow_details_responses, response, "ica_device_skip_flow_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_device_skip_flow_details_response_array
				i=0
				error = [ica_device_skip_flow_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_device_skip_flow_details_response_array
			i=0
			ica_device_skip_flow_details_objs = [ica_device_skip_flow_details() for _ in range(len(response))]
			for obj in response :
				for props in obj._ica_device_skip_flow_details:
					result = service.payload_formatter.string_to_bulk_resource(ica_device_skip_flow_details_response,self.__class__.__name__,props)
					ica_device_skip_flow_details_objs[i] = result.ica_device_skip_flow_details
					i=i+1
			return ica_device_skip_flow_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_device_skip_flow_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_device_skip_flow_details_response(base_response):
	def __init__(self,length=1) :
		self.ica_device_skip_flow_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_device_skip_flow_details= [ ica_device_skip_flow_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_device_skip_flow_details_responses(base_response):
	def __init__(self,length=1) :
		self.ica_device_skip_flow_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_device_skip_flow_details_response_array = [ ica_device_skip_flow_details() for _ in range(length)]
