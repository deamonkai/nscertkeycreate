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
Configuration for Af report for related HDX Desktop Session resource
'''

class related_desktop_session(af_generic_api):
	_selected_time_total_byte= ""
	_ica_rtt= ""
	_session_end_time= ""
	_duration_summary_bandwidth= ""
	_clientside_rto= ""
	_client_ip_address= ""
	_acr_count= ""
	_server_side_ns_delay= ""
	_server_jitter= ""
	_clientside_packet_retransmits= ""
	_city= ""
	_serverside_cb= ""
	_user_type= ""
	_sr_reconnect_count= ""
	_session_rtt= ""
	_client_side_ns_delay= ""
	_ip_block_name= ""
	_l7_serverside_latency= ""
	_client_jitter= ""
	_session_setup_time_local= ""
	_region_code= ""
	_ica_device_ip_address= ""
	_euem= ""
	_server_ip_address= ""
	_serverside_rto= ""
	_clientside_cb= ""
	_country_code= ""
	_device_type= ""
	_country= ""
	_longitude= ""
	_clientside_0_win= ""
	_session_hop_diagram= ""
	_total_bytes= ""
	_client_version= ""
	_bandwidth= ""
	_is_multi_hop= ""
	_state= ""
	_session_duration= ""
	_client_latency= ""
	_l7_clientside_latency= ""
	_server_srtt= ""
	_edt_type= ""
	_id= ""
	_latitude= ""
	_region= ""
	_session_setup_time= ""
	_hdx_desktop_username= ""
	_serverside_packet_retransmits= ""
	_vdi_image_name= ""
	_up_time= ""
	_rpt_sample_time= ""
	_serverside_0_win= ""
	_host_delay= ""
	_is_msi= ""
	___count= ""
	_client_type= ""
	_server_latency= ""
	_client_srtt= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "related_desktop_session"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(related_desktop_session,self).get_object_id()
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
			return "related_desktop_sessions"
		except Exception as e :
			raise e


	'''
	Total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def selected_time_total_byte(self):
		try:
			return self._selected_time_total_byte
		except Exception as e :
			raise e
	'''
	Total bytes accounted by this URL in sampled timeframe.
	'''
	@selected_time_total_byte.setter
	def selected_time_total_byte(self,selected_time_total_byte):
		try :
			if not isinstance(selected_time_total_byte,float):
				raise TypeError("selected_time_total_byte must be set to float value")
			self._selected_time_total_byte = selected_time_total_byte
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
	Avg Bandwidth for duration summary.
	'''
	@property
	def duration_summary_bandwidth(self):
		try:
			return self._duration_summary_bandwidth
		except Exception as e :
			raise e
	'''
	Avg Bandwidth for duration summary.
	'''
	@duration_summary_bandwidth.setter
	def duration_summary_bandwidth(self,duration_summary_bandwidth):
		try :
			if not isinstance(duration_summary_bandwidth,float):
				raise TypeError("duration_summary_bandwidth must be set to float value")
			self._duration_summary_bandwidth = duration_summary_bandwidth
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
	Session Reliability ACR count
	'''
	@property
	def acr_count(self):
		try:
			return self._acr_count
		except Exception as e :
			raise e
	'''
	Session Reliability ACR count
	'''
	@acr_count.setter
	def acr_count(self,acr_count):
		try :
			if not isinstance(acr_count,float):
				raise TypeError("acr_count must be set to float value")
			self._acr_count = acr_count
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
	User Access Type
	'''
	@property
	def user_type(self):
		try:
			return self._user_type
		except Exception as e :
			raise e
	'''
	User Access Type
	'''
	@user_type.setter
	def user_type(self,user_type):
		try :
			if not isinstance(user_type,str):
				raise TypeError("user_type must be set to str value")
			self._user_type = user_type
		except Exception as e :
			raise e

	'''
	Session Reliability Reconnect count
	'''
	@property
	def sr_reconnect_count(self):
		try:
			return self._sr_reconnect_count
		except Exception as e :
			raise e
	'''
	Session Reliability Reconnect count
	'''
	@sr_reconnect_count.setter
	def sr_reconnect_count(self,sr_reconnect_count):
		try :
			if not isinstance(sr_reconnect_count,float):
				raise TypeError("sr_reconnect_count must be set to float value")
			self._sr_reconnect_count = sr_reconnect_count
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
	ip_block_name
	'''
	@property
	def ip_block_name(self):
		try:
			return self._ip_block_name
		except Exception as e :
			raise e
	'''
	ip_block_name
	'''
	@ip_block_name.setter
	def ip_block_name(self,ip_block_name):
		try :
			if not isinstance(ip_block_name,str):
				raise TypeError("ip_block_name must be set to str value")
			self._ip_block_name = ip_block_name
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
	ICA Session setup time in local timezone.
	'''
	@property
	def session_setup_time_local(self):
		try:
			return self._session_setup_time_local
		except Exception as e :
			raise e
	'''
	ICA Session setup time in local timezone.
	'''
	@session_setup_time_local.setter
	def session_setup_time_local(self,session_setup_time_local):
		try :
			if not isinstance(session_setup_time_local,float):
				raise TypeError("session_setup_time_local must be set to float value")
			self._session_setup_time_local = session_setup_time_local
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
	ICA device ip address.
	'''
	@property
	def ica_device_ip_address(self):
		try:
			return self._ica_device_ip_address
		except Exception as e :
			raise e
	'''
	ICA device ip address.
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
	longitude
	'''
	@property
	def longitude(self):
		try:
			return self._longitude
		except Exception as e :
			raise e
	'''
	longitude
	'''
	@longitude.setter
	def longitude(self,longitude):
		try :
			if not isinstance(longitude,float):
				raise TypeError("longitude must be set to float value")
			self._longitude = longitude
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
	Total bytes.
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes.
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
	Desktop Session state.
	'''
	@property
	def state(self):
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	Desktop Session state.
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
	client latency.
	'''
	@property
	def client_latency(self):
		try:
			return self._client_latency
		except Exception as e :
			raise e
	'''
	client latency.
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
	Id is HDX Desktop user session ID
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is HDX Desktop user session ID
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
	latitude
	'''
	@property
	def latitude(self):
		try:
			return self._latitude
		except Exception as e :
			raise e
	'''
	latitude
	'''
	@latitude.setter
	def latitude(self,latitude):
		try :
			if not isinstance(latitude,float):
				raise TypeError("latitude must be set to float value")
			self._latitude = latitude
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
	hdx desktop session up time.
	'''
	@property
	def up_time(self):
		try:
			return self._up_time
		except Exception as e :
			raise e
	'''
	hdx desktop session up time.
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
	If Session is MSI or not
	'''
	@property
	def is_msi(self):
		try:
			return self._is_msi
		except Exception as e :
			raise e
	'''
	If Session is MSI or not
	'''
	@is_msi.setter
	def is_msi(self,is_msi):
		try :
			if not isinstance(is_msi,float):
				raise TypeError("is_msi must be set to float value")
			self._is_msi = is_msi
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
	server latency.
	'''
	@property
	def server_latency(self):
		try:
			return self._server_latency
		except Exception as e :
			raise e
	'''
	server latency.
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
	Af Report for related HDX Desktop Session..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				related_desktop_session_obj=related_desktop_session()
				response = related_desktop_session_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of related_desktop_session resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			related_desktop_session_obj = related_desktop_session()
			option_ = options()
			option_._filter=filter_
			return related_desktop_session_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the related_desktop_session resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			related_desktop_session_obj = related_desktop_session()
			option_ = options()
			option_._count=True
			response = related_desktop_session_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of related_desktop_session resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			related_desktop_session_obj = related_desktop_session()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = related_desktop_session_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(related_desktop_session_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.related_desktop_session
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(related_desktop_session_responses, response, "related_desktop_session_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.related_desktop_session_response_array
				i=0
				error = [related_desktop_session() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.related_desktop_session_response_array
			i=0
			related_desktop_session_objs = [related_desktop_session() for _ in range(len(response))]
			for obj in response :
				for props in obj._related_desktop_session:
					result = service.payload_formatter.string_to_bulk_resource(related_desktop_session_response,self.__class__.__name__,props)
					related_desktop_session_objs[i] = result.related_desktop_session
					i=i+1
			return related_desktop_session_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(related_desktop_session,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class related_desktop_session_response(base_response):
	def __init__(self,length=1) :
		self.related_desktop_session= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.related_desktop_session= [ related_desktop_session() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class related_desktop_session_responses(base_response):
	def __init__(self,length=1) :
		self.related_desktop_session_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.related_desktop_session_response_array = [ related_desktop_session() for _ in range(length)]
