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

class active_ica_session(af_generic_api):
	_edt_type= ""
	_server_srtt= ""
	_state= ""
	_session_duration= ""
	_client_latency= ""
	_l7_clientside_latency= ""
	_session_setup_time= ""
	_hdx_desktop_username= ""
	_id= ""
	_client_rx_bytes= ""
	_pn_agent_version= ""
	_session_hop_diagram= ""
	_clientside_0_win= ""
	_client_version= ""
	_bandwidth= ""
	_is_multi_hop= ""
	_total_bytes= ""
	___count= ""
	_is_active= ""
	_session_reconnect= ""
	_host_delay= ""
	_client_srtt= ""
	_client_type= ""
	_client_tx_bytes= ""
	_server_latency= ""
	_up_time= ""
	_rpt_sample_time= ""
	_serverside_packet_retransmits= ""
	_vdi_image_name= ""
	_serverside_0_win= ""
	_ica_user_name= ""
	_serverside_cb= ""
	_clientside_rto= ""
	_client_ip_address= ""
	_application_enumeration_duration= ""
	_ica_rtt= ""
	_session_end_time= ""
	_receiver_version= ""
	_server_jitter= ""
	_clientside_packet_retransmits= ""
	_session_type= ""
	_server_side_ns_delay= ""
	_ica_app_name= ""
	_clientside_cb= ""
	_device_type= ""
	_l7_serverside_latency= ""
	_client_jitter= ""
	_session_rtt= ""
	_client_side_ns_delay= ""
	_launch_duration= ""
	_euem= ""
	_server_ip_address= ""
	_serverside_rto= ""
	_ica_device_ip_address= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "active_ica_session"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(active_ica_session,self).get_object_id()
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
			return "active_ica_sessions"
		except Exception as e :
			raise e


	'''
	EDT Type.
	'''
	@property
	def edt_type(self):
		try:
			return self._edt_type
		except Exception as e :
			raise e
	'''
	EDT Type.
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
	session duration.
	'''
	@property
	def session_duration(self):
		try:
			return self._session_duration
		except Exception as e :
			raise e
	'''
	session duration.
	'''
	@session_duration.setter
	def session_duration(self,session_duration):
		try :
			if not isinstance(session_duration,float):
				raise TypeError("session_duration must be set to float value")
			self._session_duration = session_duration
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
	username
	'''
	@property
	def hdx_desktop_username(self):
		try:
			return self._hdx_desktop_username
		except Exception as e :
			raise e
	'''
	username
	'''
	@hdx_desktop_username.setter
	def hdx_desktop_username(self,hdx_desktop_username):
		try :
			if not isinstance(hdx_desktop_username,str):
				raise TypeError("hdx_desktop_username must be set to str value")
			self._hdx_desktop_username = hdx_desktop_username
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
	Session Hop Diagram
	'''
	@property
	def session_hop_diagram(self):
		try:
			return self._session_hop_diagram
		except Exception as e :
			raise e
	'''
	Session Hop Diagram
	'''
	@session_hop_diagram.setter
	def session_hop_diagram(self,session_hop_diagram):
		try :
			if not isinstance(session_hop_diagram,bool):
				raise TypeError("session_hop_diagram must be set to bool value")
			self._session_hop_diagram = session_hop_diagram
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
	Is Multi hop.
	'''
	@property
	def is_multi_hop(self):
		try:
			return self._is_multi_hop
		except Exception as e :
			raise e
	'''
	Is Multi hop.
	'''
	@is_multi_hop.setter
	def is_multi_hop(self,is_multi_hop):
		try :
			if not isinstance(is_multi_hop,float):
				raise TypeError("is_multi_hop must be set to float value")
			self._is_multi_hop = is_multi_hop
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
	Is Active.
	'''
	@property
	def is_active(self):
		try:
			return self._is_active
		except Exception as e :
			raise e
	'''
	Is Active.
	'''
	@is_active.setter
	def is_active(self,is_active):
		try :
			if not isinstance(is_active,float):
				raise TypeError("is_active must be set to float value")
			self._is_active = is_active
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
	vdi_image_name
	'''
	@property
	def vdi_image_name(self):
		try:
			return self._vdi_image_name
		except Exception as e :
			raise e
	'''
	vdi_image_name
	'''
	@vdi_image_name.setter
	def vdi_image_name(self,vdi_image_name):
		try :
			if not isinstance(vdi_image_name,str):
				raise TypeError("vdi_image_name must be set to str value")
			self._vdi_image_name = vdi_image_name
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
	ICA rtt.
	'''
	@property
	def ica_rtt(self):
		try:
			return self._ica_rtt
		except Exception as e :
			raise e
	'''
	ICA rtt.
	'''
	@ica_rtt.setter
	def ica_rtt(self,ica_rtt):
		try :
			if not isinstance(ica_rtt,float):
				raise TypeError("ica_rtt must be set to float value")
			self._ica_rtt = ica_rtt
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
	Session Type
	'''
	@property
	def session_type(self):
		try:
			return self._session_type
		except Exception as e :
			raise e
	'''
	Session Type
	'''
	@session_type.setter
	def session_type(self,session_type):
		try :
			if not isinstance(session_type,float):
				raise TypeError("session_type must be set to float value")
			self._session_type = session_type
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
	Device Type.
	'''
	@property
	def device_type(self):
		try:
			return self._device_type
		except Exception as e :
			raise e
	'''
	Device Type.
	'''
	@device_type.setter
	def device_type(self,device_type):
		try :
			if not isinstance(device_type,str):
				raise TypeError("device_type must be set to str value")
			self._device_type = device_type
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
	EUEM.
	'''
	@property
	def euem(self):
		try:
			return self._euem
		except Exception as e :
			raise e
	'''
	EUEM.
	'''
	@euem.setter
	def euem(self,euem):
		try :
			if not isinstance(euem,float):
				raise TypeError("euem must be set to float value")
			self._euem = euem
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
	Af Report for ICA User..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				active_ica_session_obj=active_ica_session()
				response = active_ica_session_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of active_ica_session resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			active_ica_session_obj = active_ica_session()
			option_ = options()
			option_._filter=filter_
			return active_ica_session_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the active_ica_session resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			active_ica_session_obj = active_ica_session()
			option_ = options()
			option_._count=True
			response = active_ica_session_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of active_ica_session resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			active_ica_session_obj = active_ica_session()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = active_ica_session_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(active_ica_session_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.active_ica_session
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(active_ica_session_responses, response, "active_ica_session_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.active_ica_session_response_array
				i=0
				error = [active_ica_session() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.active_ica_session_response_array
			i=0
			active_ica_session_objs = [active_ica_session() for _ in range(len(response))]
			for obj in response :
				for props in obj._active_ica_session:
					result = service.payload_formatter.string_to_bulk_resource(active_ica_session_response,self.__class__.__name__,props)
					active_ica_session_objs[i] = result.active_ica_session
					i=i+1
			return active_ica_session_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(active_ica_session,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class active_ica_session_response(base_response):
	def __init__(self,length=1) :
		self.active_ica_session= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.active_ica_session= [ active_ica_session() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class active_ica_session_responses(base_response):
	def __init__(self,length=1) :
		self.active_ica_session_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.active_ica_session_response_array = [ active_ica_session() for _ in range(length)]
