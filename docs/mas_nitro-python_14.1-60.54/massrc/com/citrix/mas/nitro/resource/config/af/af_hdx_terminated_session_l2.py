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
Configuration for AF HDX Terminated Session Report table for Level 1 resource
'''

class af_hdx_terminated_session_l2(base_resource):
	_rpt_sample_time= ""
	_client_ip= ""
	_serverside_packet_retransmits= ""
	_max_l7lat_breach_client= ""
	_session_terminate_time= ""
	_serverside_0_win= ""
	_session_id= ""
	_is_msi= ""
	_ip_block= ""
	_session_reconnect= ""
	_client_srtt= ""
	_client_type= ""
	_is_clientside_cb= ""
	_clientside_0_win= ""
	_server_to_client_ns_delay= ""
	_server_ip= ""
	_client_version= ""
	_total_bytes= ""
	_server_srtt= ""
	_count_usb_rejected= ""
	_l7_clientside_latency= ""
	_is_desktop= ""
	_session_setup_time= ""
	_terminated_reason= ""
	_latitude= ""
	_session_terminate_time_local= ""
	_client_jitter= ""
	_l7_serverside_latency= ""
	_usb_status= ""
	_count_usb_stopped= ""
	_server_delay= ""
	_sr_disconnect_count= ""
	_server_total_rtt= ""
	_serverside_rto= ""
	_euem= ""
	_region_code= ""
	_client_to_server_ns_delay= ""
	_is_serverside_cb= ""
	_count_usb_accepted= ""
	_max_l7lat_breach_server= ""
	_server_rtt= ""
	_longitude= ""
	_ctnsappname= ""
	_app_count= ""
	_ha_failover_count= ""
	_agent_ip_address= ""
	_country_code= ""
	_username= ""
	_clientside_rto= ""
	_count_l7lat_breach= ""
	_ica_rtt= ""
	_clientside_packet_retransmits= ""
	_server_jitter= ""
	_desktop_name= ""
	_ip_address= ""
	_edt= ""
	_acr_count= ""
	_client_total_rtt= ""
	_city= ""
	_sr_reconnect_count= ""
	_user_type= ""
	_l7_monitoring_supported= ""
	_client_rtt= ""
	_exporter_id= ""
	_client_hostname= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_hdx_terminated_session_l2"
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
			return "af_hdx_terminated_session_l2s"
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
	get Client IP Address.
	'''
	@property
	def client_ip(self) :
		try:
			return self._client_ip
		except Exception as e :
			raise e
	'''
	set Client IP Address.
	'''
	@client_ip.setter
	def client_ip(self,client_ip):
		try :
			if not isinstance(client_ip,str):
				raise TypeError("client_ip must be set to str value")
			self._client_ip = client_ip
		except Exception as e :
			raise e


	'''
	get serverside packet retransmits
	'''
	@property
	def serverside_packet_retransmits(self) :
		try:
			return self._serverside_packet_retransmits
		except Exception as e :
			raise e
	'''
	set serverside packet retransmits
	'''
	@serverside_packet_retransmits.setter
	def serverside_packet_retransmits(self,serverside_packet_retransmits):
		try :
			if not isinstance(serverside_packet_retransmits,int):
				raise TypeError("serverside_packet_retransmits must be set to int value")
			self._serverside_packet_retransmits = serverside_packet_retransmits
		except Exception as e :
			raise e


	'''
	get max_l7lat_breach_client
	'''
	@property
	def max_l7lat_breach_client(self) :
		try:
			return self._max_l7lat_breach_client
		except Exception as e :
			raise e
	'''
	set max_l7lat_breach_client
	'''
	@max_l7lat_breach_client.setter
	def max_l7lat_breach_client(self,max_l7lat_breach_client):
		try :
			if not isinstance(max_l7lat_breach_client,int):
				raise TypeError("max_l7lat_breach_client must be set to int value")
			self._max_l7lat_breach_client = max_l7lat_breach_client
		except Exception as e :
			raise e


	'''
	get Session terminate time.
	'''
	@property
	def session_terminate_time(self) :
		try:
			return self._session_terminate_time
		except Exception as e :
			raise e
	'''
	set Session terminate time.
	'''
	@session_terminate_time.setter
	def session_terminate_time(self,session_terminate_time):
		try :
			if not isinstance(session_terminate_time,long):
				raise TypeError("session_terminate_time must be set to long value")
			self._session_terminate_time = session_terminate_time
		except Exception as e :
			raise e


	'''
	get serverside0 win
	'''
	@property
	def serverside_0_win(self) :
		try:
			return self._serverside_0_win
		except Exception as e :
			raise e
	'''
	set serverside0 win
	'''
	@serverside_0_win.setter
	def serverside_0_win(self,serverside_0_win):
		try :
			if not isinstance(serverside_0_win,int):
				raise TypeError("serverside_0_win must be set to int value")
			self._serverside_0_win = serverside_0_win
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
	get If Session is MSI or not
	'''
	@property
	def is_msi(self) :
		try:
			return self._is_msi
		except Exception as e :
			raise e
	'''
	set If Session is MSI or not
	'''
	@is_msi.setter
	def is_msi(self,is_msi):
		try :
			if not isinstance(is_msi,int):
				raise TypeError("is_msi must be set to int value")
			self._is_msi = is_msi
		except Exception as e :
			raise e


	'''
	get ip_block_name
	'''
	@property
	def ip_block(self) :
		try:
			return self._ip_block
		except Exception as e :
			raise e
	'''
	set ip_block_name
	'''
	@ip_block.setter
	def ip_block(self,ip_block):
		try :
			if not isinstance(ip_block,str):
				raise TypeError("ip_block must be set to str value")
			self._ip_block = ip_block
		except Exception as e :
			raise e


	'''
	get Session Reconnect.
	'''
	@property
	def session_reconnect(self) :
		try:
			return self._session_reconnect
		except Exception as e :
			raise e
	'''
	set Session Reconnect.
	'''
	@session_reconnect.setter
	def session_reconnect(self,session_reconnect):
		try :
			if not isinstance(session_reconnect,int):
				raise TypeError("session_reconnect must be set to int value")
			self._session_reconnect = session_reconnect
		except Exception as e :
			raise e


	'''
	get client Smothen RTT.
	'''
	@property
	def client_srtt(self) :
		try:
			return self._client_srtt
		except Exception as e :
			raise e
	'''
	set client Smothen RTT.
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
	get Client Type
	'''
	@property
	def client_type(self) :
		try:
			return self._client_type
		except Exception as e :
			raise e
	'''
	set Client Type
	'''
	@client_type.setter
	def client_type(self,client_type):
		try :
			if not isinstance(client_type,int):
				raise TypeError("client_type must be set to int value")
			self._client_type = client_type
		except Exception as e :
			raise e


	'''
	get Is Clientside CB
	'''
	@property
	def is_clientside_cb(self) :
		try:
			return self._is_clientside_cb
		except Exception as e :
			raise e
	'''
	set Is Clientside CB
	'''
	@is_clientside_cb.setter
	def is_clientside_cb(self,is_clientside_cb):
		try :
			if not isinstance(is_clientside_cb,int):
				raise TypeError("is_clientside_cb must be set to int value")
			self._is_clientside_cb = is_clientside_cb
		except Exception as e :
			raise e


	'''
	get clientside0 win
	'''
	@property
	def clientside_0_win(self) :
		try:
			return self._clientside_0_win
		except Exception as e :
			raise e
	'''
	set clientside0 win
	'''
	@clientside_0_win.setter
	def clientside_0_win(self,clientside_0_win):
		try :
			if not isinstance(clientside_0_win,int):
				raise TypeError("clientside_0_win must be set to int value")
			self._clientside_0_win = clientside_0_win
		except Exception as e :
			raise e


	'''
	get Server to Client NetScaler delay.
	'''
	@property
	def server_to_client_ns_delay(self) :
		try:
			return self._server_to_client_ns_delay
		except Exception as e :
			raise e
	'''
	set Server to Client NetScaler delay.
	'''
	@server_to_client_ns_delay.setter
	def server_to_client_ns_delay(self,server_to_client_ns_delay):
		try :
			if not isinstance(server_to_client_ns_delay,int):
				raise TypeError("server_to_client_ns_delay must be set to int value")
			self._server_to_client_ns_delay = server_to_client_ns_delay
		except Exception as e :
			raise e


	'''
	get Server IP Address.
	'''
	@property
	def server_ip(self) :
		try:
			return self._server_ip
		except Exception as e :
			raise e
	'''
	set Server IP Address.
	'''
	@server_ip.setter
	def server_ip(self,server_ip):
		try :
			if not isinstance(server_ip,str):
				raise TypeError("server_ip must be set to str value")
			self._server_ip = server_ip
		except Exception as e :
			raise e


	'''
	get Client Version
	'''
	@property
	def client_version(self) :
		try:
			return self._client_version
		except Exception as e :
			raise e
	'''
	set Client Version
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
	get Total bytes.
	'''
	@property
	def total_bytes(self) :
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	set Total bytes.
	'''
	@total_bytes.setter
	def total_bytes(self,total_bytes):
		try :
			if not isinstance(total_bytes,long):
				raise TypeError("total_bytes must be set to long value")
			self._total_bytes = total_bytes
		except Exception as e :
			raise e


	'''
	get server Smothen RTT.
	'''
	@property
	def server_srtt(self) :
		try:
			return self._server_srtt
		except Exception as e :
			raise e
	'''
	set server Smothen RTT.
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
	get count_usb_rejected
	'''
	@property
	def count_usb_rejected(self) :
		try:
			return self._count_usb_rejected
		except Exception as e :
			raise e
	'''
	set count_usb_rejected
	'''
	@count_usb_rejected.setter
	def count_usb_rejected(self,count_usb_rejected):
		try :
			if not isinstance(count_usb_rejected,int):
				raise TypeError("count_usb_rejected must be set to int value")
			self._count_usb_rejected = count_usb_rejected
		except Exception as e :
			raise e


	'''
	get L7 clientside latency
	'''
	@property
	def l7_clientside_latency(self) :
		try:
			return self._l7_clientside_latency
		except Exception as e :
			raise e
	'''
	set L7 clientside latency
	'''
	@l7_clientside_latency.setter
	def l7_clientside_latency(self,l7_clientside_latency):
		try :
			if not isinstance(l7_clientside_latency,long):
				raise TypeError("l7_clientside_latency must be set to long value")
			self._l7_clientside_latency = l7_clientside_latency
		except Exception as e :
			raise e


	'''
	get Is Desktop.
	'''
	@property
	def is_desktop(self) :
		try:
			return self._is_desktop
		except Exception as e :
			raise e
	'''
	set Is Desktop.
	'''
	@is_desktop.setter
	def is_desktop(self,is_desktop):
		try :
			if not isinstance(is_desktop,int):
				raise TypeError("is_desktop must be set to int value")
			self._is_desktop = is_desktop
		except Exception as e :
			raise e


	'''
	get Session setup time.
	'''
	@property
	def session_setup_time(self) :
		try:
			return self._session_setup_time
		except Exception as e :
			raise e
	'''
	set Session setup time.
	'''
	@session_setup_time.setter
	def session_setup_time(self,session_setup_time):
		try :
			if not isinstance(session_setup_time,long):
				raise TypeError("session_setup_time must be set to long value")
			self._session_setup_time = session_setup_time
		except Exception as e :
			raise e


	'''
	get terminated Reason
	'''
	@property
	def terminated_reason(self) :
		try:
			return self._terminated_reason
		except Exception as e :
			raise e
	'''
	set terminated Reason
	'''
	@terminated_reason.setter
	def terminated_reason(self,terminated_reason):
		try :
			if not isinstance(terminated_reason,int):
				raise TypeError("terminated_reason must be set to int value")
			self._terminated_reason = terminated_reason
		except Exception as e :
			raise e


	'''
	get latitude
	'''
	@property
	def latitude(self) :
		try:
			return self._latitude
		except Exception as e :
			raise e
	'''
	set latitude
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
	get ICA terminate setup time in local timezone.
	'''
	@property
	def session_terminate_time_local(self) :
		try:
			return self._session_terminate_time_local
		except Exception as e :
			raise e
	'''
	set ICA terminate setup time in local timezone.
	'''
	@session_terminate_time_local.setter
	def session_terminate_time_local(self,session_terminate_time_local):
		try :
			if not isinstance(session_terminate_time_local,long):
				raise TypeError("session_terminate_time_local must be set to long value")
			self._session_terminate_time_local = session_terminate_time_local
		except Exception as e :
			raise e


	'''
	get Client Jitter.
	'''
	@property
	def client_jitter(self) :
		try:
			return self._client_jitter
		except Exception as e :
			raise e
	'''
	set Client Jitter.
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
	get L7 serverside latency
	'''
	@property
	def l7_serverside_latency(self) :
		try:
			return self._l7_serverside_latency
		except Exception as e :
			raise e
	'''
	set L7 serverside latency
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
	get usb_statuse
	'''
	@property
	def usb_status(self) :
		try:
			return self._usb_status
		except Exception as e :
			raise e
	'''
	set usb_statuse
	'''
	@usb_status.setter
	def usb_status(self,usb_status):
		try :
			if not isinstance(usb_status,int):
				raise TypeError("usb_status must be set to int value")
			self._usb_status = usb_status
		except Exception as e :
			raise e


	'''
	get User Type
	'''
	@property
	def count_usb_stopped(self) :
		try:
			return self._count_usb_stopped
		except Exception as e :
			raise e
	'''
	set User Type
	'''
	@count_usb_stopped.setter
	def count_usb_stopped(self,count_usb_stopped):
		try :
			if not isinstance(count_usb_stopped,int):
				raise TypeError("count_usb_stopped must be set to int value")
			self._count_usb_stopped = count_usb_stopped
		except Exception as e :
			raise e


	'''
	get Server induced delay.
	'''
	@property
	def server_delay(self) :
		try:
			return self._server_delay
		except Exception as e :
			raise e
	'''
	set Server induced delay.
	'''
	@server_delay.setter
	def server_delay(self,server_delay):
		try :
			if not isinstance(server_delay,int):
				raise TypeError("server_delay must be set to int value")
			self._server_delay = server_delay
		except Exception as e :
			raise e


	'''
	get Session Disliability Disconnect count
	'''
	@property
	def sr_disconnect_count(self) :
		try:
			return self._sr_disconnect_count
		except Exception as e :
			raise e
	'''
	set Session Disliability Disconnect count
	'''
	@sr_disconnect_count.setter
	def sr_disconnect_count(self,sr_disconnect_count):
		try :
			if not isinstance(sr_disconnect_count,int):
				raise TypeError("sr_disconnect_count must be set to int value")
			self._sr_disconnect_count = sr_disconnect_count
		except Exception as e :
			raise e


	'''
	get server total RTT.
	'''
	@property
	def server_total_rtt(self) :
		try:
			return self._server_total_rtt
		except Exception as e :
			raise e
	'''
	set server total RTT.
	'''
	@server_total_rtt.setter
	def server_total_rtt(self,server_total_rtt):
		try :
			if not isinstance(server_total_rtt,float):
				raise TypeError("server_total_rtt must be set to float value")
			self._server_total_rtt = server_total_rtt
		except Exception as e :
			raise e


	'''
	get serverside rto
	'''
	@property
	def serverside_rto(self) :
		try:
			return self._serverside_rto
		except Exception as e :
			raise e
	'''
	set serverside rto
	'''
	@serverside_rto.setter
	def serverside_rto(self,serverside_rto):
		try :
			if not isinstance(serverside_rto,int):
				raise TypeError("serverside_rto must be set to int value")
			self._serverside_rto = serverside_rto
		except Exception as e :
			raise e


	'''
	get EUEM.
	'''
	@property
	def euem(self) :
		try:
			return self._euem
		except Exception as e :
			raise e
	'''
	set EUEM.
	'''
	@euem.setter
	def euem(self,euem):
		try :
			if not isinstance(euem,int):
				raise TypeError("euem must be set to int value")
			self._euem = euem
		except Exception as e :
			raise e


	'''
	get region_code
	'''
	@property
	def region_code(self) :
		try:
			return self._region_code
		except Exception as e :
			raise e
	'''
	set region_code
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
	get Client to Server NetScaler delay.
	'''
	@property
	def client_to_server_ns_delay(self) :
		try:
			return self._client_to_server_ns_delay
		except Exception as e :
			raise e
	'''
	set Client to Server NetScaler delay.
	'''
	@client_to_server_ns_delay.setter
	def client_to_server_ns_delay(self,client_to_server_ns_delay):
		try :
			if not isinstance(client_to_server_ns_delay,int):
				raise TypeError("client_to_server_ns_delay must be set to int value")
			self._client_to_server_ns_delay = client_to_server_ns_delay
		except Exception as e :
			raise e


	'''
	get Is Serverside CB
	'''
	@property
	def is_serverside_cb(self) :
		try:
			return self._is_serverside_cb
		except Exception as e :
			raise e
	'''
	set Is Serverside CB
	'''
	@is_serverside_cb.setter
	def is_serverside_cb(self,is_serverside_cb):
		try :
			if not isinstance(is_serverside_cb,int):
				raise TypeError("is_serverside_cb must be set to int value")
			self._is_serverside_cb = is_serverside_cb
		except Exception as e :
			raise e


	'''
	get count_usb_accepted
	'''
	@property
	def count_usb_accepted(self) :
		try:
			return self._count_usb_accepted
		except Exception as e :
			raise e
	'''
	set count_usb_accepted
	'''
	@count_usb_accepted.setter
	def count_usb_accepted(self,count_usb_accepted):
		try :
			if not isinstance(count_usb_accepted,int):
				raise TypeError("count_usb_accepted must be set to int value")
			self._count_usb_accepted = count_usb_accepted
		except Exception as e :
			raise e


	'''
	get max_l7lat_breach_servere
	'''
	@property
	def max_l7lat_breach_server(self) :
		try:
			return self._max_l7lat_breach_server
		except Exception as e :
			raise e
	'''
	set max_l7lat_breach_servere
	'''
	@max_l7lat_breach_server.setter
	def max_l7lat_breach_server(self,max_l7lat_breach_server):
		try :
			if not isinstance(max_l7lat_breach_server,int):
				raise TypeError("max_l7lat_breach_server must be set to int value")
			self._max_l7lat_breach_server = max_l7lat_breach_server
		except Exception as e :
			raise e


	'''
	get server RTT.
	'''
	@property
	def server_rtt(self) :
		try:
			return self._server_rtt
		except Exception as e :
			raise e
	'''
	set server RTT.
	'''
	@server_rtt.setter
	def server_rtt(self,server_rtt):
		try :
			if not isinstance(server_rtt,float):
				raise TypeError("server_rtt must be set to float value")
			self._server_rtt = server_rtt
		except Exception as e :
			raise e


	'''
	get longitude
	'''
	@property
	def longitude(self) :
		try:
			return self._longitude
		except Exception as e :
			raise e
	'''
	set longitude
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
	get App Count.
	'''
	@property
	def app_count(self) :
		try:
			return self._app_count
		except Exception as e :
			raise e
	'''
	set App Count.
	'''
	@app_count.setter
	def app_count(self,app_count):
		try :
			if not isinstance(app_count,int):
				raise TypeError("app_count must be set to int value")
			self._app_count = app_count
		except Exception as e :
			raise e


	'''
	get ha_failover_count
	'''
	@property
	def ha_failover_count(self) :
		try:
			return self._ha_failover_count
		except Exception as e :
			raise e
	'''
	set ha_failover_count
	'''
	@ha_failover_count.setter
	def ha_failover_count(self,ha_failover_count):
		try :
			if not isinstance(ha_failover_count,int):
				raise TypeError("ha_failover_count must be set to int value")
			self._ha_failover_count = ha_failover_count
		except Exception as e :
			raise e


	'''
	get Agent IP Address
	'''
	@property
	def agent_ip_address(self) :
		try:
			return self._agent_ip_address
		except Exception as e :
			raise e
	'''
	set Agent IP Address
	'''
	@agent_ip_address.setter
	def agent_ip_address(self,agent_ip_address):
		try :
			if not isinstance(agent_ip_address,str):
				raise TypeError("agent_ip_address must be set to str value")
			self._agent_ip_address = agent_ip_address
		except Exception as e :
			raise e


	'''
	get country_code
	'''
	@property
	def country_code(self) :
		try:
			return self._country_code
		except Exception as e :
			raise e
	'''
	set country_code
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
	get User Name.
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set User Name.
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e


	'''
	get clientside rto
	'''
	@property
	def clientside_rto(self) :
		try:
			return self._clientside_rto
		except Exception as e :
			raise e
	'''
	set clientside rto
	'''
	@clientside_rto.setter
	def clientside_rto(self,clientside_rto):
		try :
			if not isinstance(clientside_rto,int):
				raise TypeError("clientside_rto must be set to int value")
			self._clientside_rto = clientside_rto
		except Exception as e :
			raise e


	'''
	get count_l7lat_breach
	'''
	@property
	def count_l7lat_breach(self) :
		try:
			return self._count_l7lat_breach
		except Exception as e :
			raise e
	'''
	set count_l7lat_breach
	'''
	@count_l7lat_breach.setter
	def count_l7lat_breach(self,count_l7lat_breach):
		try :
			if not isinstance(count_l7lat_breach,int):
				raise TypeError("count_l7lat_breach must be set to int value")
			self._count_l7lat_breach = count_l7lat_breach
		except Exception as e :
			raise e


	'''
	get ICA RTT.
	'''
	@property
	def ica_rtt(self) :
		try:
			return self._ica_rtt
		except Exception as e :
			raise e
	'''
	set ICA RTT.
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
	get clientside packet retransmits
	'''
	@property
	def clientside_packet_retransmits(self) :
		try:
			return self._clientside_packet_retransmits
		except Exception as e :
			raise e
	'''
	set clientside packet retransmits
	'''
	@clientside_packet_retransmits.setter
	def clientside_packet_retransmits(self,clientside_packet_retransmits):
		try :
			if not isinstance(clientside_packet_retransmits,int):
				raise TypeError("clientside_packet_retransmits must be set to int value")
			self._clientside_packet_retransmits = clientside_packet_retransmits
		except Exception as e :
			raise e


	'''
	get Server Jitter.
	'''
	@property
	def server_jitter(self) :
		try:
			return self._server_jitter
		except Exception as e :
			raise e
	'''
	set Server Jitter.
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
	get Desktop name which this session belongs.
	'''
	@property
	def desktop_name(self) :
		try:
			return self._desktop_name
		except Exception as e :
			raise e
	'''
	set Desktop name which this session belongs.
	'''
	@desktop_name.setter
	def desktop_name(self,desktop_name):
		try :
			if not isinstance(desktop_name,str):
				raise TypeError("desktop_name must be set to str value")
			self._desktop_name = desktop_name
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
	get User Type
	'''
	@property
	def edt(self) :
		try:
			return self._edt
		except Exception as e :
			raise e
	'''
	set User Type
	'''
	@edt.setter
	def edt(self,edt):
		try :
			if not isinstance(edt,int):
				raise TypeError("edt must be set to int value")
			self._edt = edt
		except Exception as e :
			raise e


	'''
	get ACR reconnects
	'''
	@property
	def acr_count(self) :
		try:
			return self._acr_count
		except Exception as e :
			raise e
	'''
	set ACR reconnects
	'''
	@acr_count.setter
	def acr_count(self,acr_count):
		try :
			if not isinstance(acr_count,int):
				raise TypeError("acr_count must be set to int value")
			self._acr_count = acr_count
		except Exception as e :
			raise e


	'''
	get client total RTT.
	'''
	@property
	def client_total_rtt(self) :
		try:
			return self._client_total_rtt
		except Exception as e :
			raise e
	'''
	set client total RTT.
	'''
	@client_total_rtt.setter
	def client_total_rtt(self,client_total_rtt):
		try :
			if not isinstance(client_total_rtt,float):
				raise TypeError("client_total_rtt must be set to float value")
			self._client_total_rtt = client_total_rtt
		except Exception as e :
			raise e


	'''
	get city
	'''
	@property
	def city(self) :
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	set city
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
	get SR reconnects
	'''
	@property
	def sr_reconnect_count(self) :
		try:
			return self._sr_reconnect_count
		except Exception as e :
			raise e
	'''
	set SR reconnects
	'''
	@sr_reconnect_count.setter
	def sr_reconnect_count(self,sr_reconnect_count):
		try :
			if not isinstance(sr_reconnect_count,int):
				raise TypeError("sr_reconnect_count must be set to int value")
			self._sr_reconnect_count = sr_reconnect_count
		except Exception as e :
			raise e


	'''
	get User Type
	'''
	@property
	def user_type(self) :
		try:
			return self._user_type
		except Exception as e :
			raise e
	'''
	set User Type
	'''
	@user_type.setter
	def user_type(self,user_type):
		try :
			if not isinstance(user_type,int):
				raise TypeError("user_type must be set to int value")
			self._user_type = user_type
		except Exception as e :
			raise e


	'''
	get l7_monitoring_supported
	'''
	@property
	def l7_monitoring_supported(self) :
		try:
			return self._l7_monitoring_supported
		except Exception as e :
			raise e
	'''
	set l7_monitoring_supported
	'''
	@l7_monitoring_supported.setter
	def l7_monitoring_supported(self,l7_monitoring_supported):
		try :
			if not isinstance(l7_monitoring_supported,int):
				raise TypeError("l7_monitoring_supported must be set to int value")
			self._l7_monitoring_supported = l7_monitoring_supported
		except Exception as e :
			raise e


	'''
	get client RTT.
	'''
	@property
	def client_rtt(self) :
		try:
			return self._client_rtt
		except Exception as e :
			raise e
	'''
	set client RTT.
	'''
	@client_rtt.setter
	def client_rtt(self,client_rtt):
		try :
			if not isinstance(client_rtt,float):
				raise TypeError("client_rtt must be set to float value")
			self._client_rtt = client_rtt
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
	get client_hostname
	'''
	@property
	def client_hostname(self) :
		try:
			return self._client_hostname
		except Exception as e :
			raise e
	'''
	set client_hostname
	'''
	@client_hostname.setter
	def client_hostname(self,client_hostname):
		try :
			if not isinstance(client_hostname,str):
				raise TypeError("client_hostname must be set to str value")
			self._client_hostname = client_hostname
		except Exception as e :
			raise e

	'''
	Af HDX Report for terminated Session information collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_hdx_terminated_session_l2_obj=af_hdx_terminated_session_l2()
				response = af_hdx_terminated_session_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_hdx_terminated_session_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_hdx_terminated_session_l2_obj = af_hdx_terminated_session_l2()
			option_ = options()
			option_._filter=filter_
			return af_hdx_terminated_session_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_hdx_terminated_session_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_hdx_terminated_session_l2_obj = af_hdx_terminated_session_l2()
			option_ = options()
			option_._count=True
			response = af_hdx_terminated_session_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_hdx_terminated_session_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_hdx_terminated_session_l2_obj = af_hdx_terminated_session_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_hdx_terminated_session_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_hdx_terminated_session_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_hdx_terminated_session_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_hdx_terminated_session_l2_responses, response, "af_hdx_terminated_session_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_hdx_terminated_session_l2_response_array
				i=0
				error = [af_hdx_terminated_session_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_hdx_terminated_session_l2_response_array
			i=0
			af_hdx_terminated_session_l2_objs = [af_hdx_terminated_session_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_hdx_terminated_session_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_hdx_terminated_session_l2_response,self.__class__.__name__,props)
					af_hdx_terminated_session_l2_objs[i] = result.af_hdx_terminated_session_l2
					i=i+1
			return af_hdx_terminated_session_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_hdx_terminated_session_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_hdx_terminated_session_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_hdx_terminated_session_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_hdx_terminated_session_l2= [ af_hdx_terminated_session_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_hdx_terminated_session_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_hdx_terminated_session_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_hdx_terminated_session_l2_response_array = [ af_hdx_terminated_session_l2() for _ in range(length)]
