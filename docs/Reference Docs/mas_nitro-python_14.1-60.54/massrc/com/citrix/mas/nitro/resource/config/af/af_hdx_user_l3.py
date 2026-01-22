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
Configuration for AF HDX User Update table for Level 3 resource
'''

class af_hdx_user_l3(base_resource):
	_serverside_0_win= ""
	_region_code= ""
	_serverside_rto= ""
	_server_total_rtt= ""
	_serverside_packet_retransmits= ""
	_server_delay= ""
	_client_ip= ""
	_rpt_sample_time= ""
	_l7_serverside_latency= ""
	_client_jitter= ""
	_country_code= ""
	_username= ""
	_client_srtt= ""
	_ctnsappname= ""
	_app_count= ""
	_longitude= ""
	_user_count= ""
	_server_rtt= ""
	_session_reconnect= ""
	_ip_block= ""
	_client_to_server_ns_delay= ""
	_total_bytes= ""
	_client_total_rtt= ""
	_edt= ""
	_ip_address= ""
	_server_ip= ""
	_server_jitter= ""
	_clientside_packet_retransmits= ""
	_server_to_client_ns_delay= ""
	_ica_rtt= ""
	_clientside_0_win= ""
	_clientside_rto= ""
	_latitude= ""
	_exporter_id= ""
	_client_rtt= ""
	_user_type= ""
	_city= ""
	_l7_clientside_latency= ""
	_server_srtt= ""
	_user_agent= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_hdx_user_l3"
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
			return "af_hdx_user_l3s"
		except Exception as e :
			raise e



	'''
	get server side 0 window count.
	'''
	@property
	def serverside_0_win(self) :
		try:
			return self._serverside_0_win
		except Exception as e :
			raise e
	'''
	set server side 0 window count.
	'''
	@serverside_0_win.setter
	def serverside_0_win(self,serverside_0_win):
		try :
			if not isinstance(serverside_0_win,long):
				raise TypeError("serverside_0_win must be set to long value")
			self._serverside_0_win = serverside_0_win
		except Exception as e :
			raise e


	'''
	get Region Code
	'''
	@property
	def region_code(self) :
		try:
			return self._region_code
		except Exception as e :
			raise e
	'''
	set Region Code
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
	get serverside rto.
	'''
	@property
	def serverside_rto(self) :
		try:
			return self._serverside_rto
		except Exception as e :
			raise e
	'''
	set serverside rto.
	'''
	@serverside_rto.setter
	def serverside_rto(self,serverside_rto):
		try :
			if not isinstance(serverside_rto,long):
				raise TypeError("serverside_rto must be set to long value")
			self._serverside_rto = serverside_rto
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
	get Serverside Packet Retransmits.
	'''
	@property
	def serverside_packet_retransmits(self) :
		try:
			return self._serverside_packet_retransmits
		except Exception as e :
			raise e
	'''
	set Serverside Packet Retransmits.
	'''
	@serverside_packet_retransmits.setter
	def serverside_packet_retransmits(self,serverside_packet_retransmits):
		try :
			if not isinstance(serverside_packet_retransmits,long):
				raise TypeError("serverside_packet_retransmits must be set to long value")
			self._serverside_packet_retransmits = serverside_packet_retransmits
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
			if not isinstance(server_delay,long):
				raise TypeError("server_delay must be set to long value")
			self._server_delay = server_delay
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
	get Country Code
	'''
	@property
	def country_code(self) :
		try:
			return self._country_code
		except Exception as e :
			raise e
	'''
	set Country Code
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
	get App count.
	'''
	@property
	def app_count(self) :
		try:
			return self._app_count
		except Exception as e :
			raise e
	'''
	set App count.
	'''
	@app_count.setter
	def app_count(self,app_count):
		try :
			if not isinstance(app_count,long):
				raise TypeError("app_count must be set to long value")
			self._app_count = app_count
		except Exception as e :
			raise e


	'''
	get Longitude
	'''
	@property
	def longitude(self) :
		try:
			return self._longitude
		except Exception as e :
			raise e
	'''
	set Longitude
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
	get User count.
	'''
	@property
	def user_count(self) :
		try:
			return self._user_count
		except Exception as e :
			raise e
	'''
	set User count.
	'''
	@user_count.setter
	def user_count(self,user_count):
		try :
			if not isinstance(user_count,long):
				raise TypeError("user_count must be set to long value")
			self._user_count = user_count
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
			if not isinstance(session_reconnect,long):
				raise TypeError("session_reconnect must be set to long value")
			self._session_reconnect = session_reconnect
		except Exception as e :
			raise e


	'''
	get Ip Block
	'''
	@property
	def ip_block(self) :
		try:
			return self._ip_block
		except Exception as e :
			raise e
	'''
	set Ip Block
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
			if not isinstance(client_to_server_ns_delay,long):
				raise TypeError("client_to_server_ns_delay must be set to long value")
			self._client_to_server_ns_delay = client_to_server_ns_delay
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
	get Transport Type
	'''
	@property
	def edt(self) :
		try:
			return self._edt
		except Exception as e :
			raise e
	'''
	set Transport Type
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
	get Clientside Packet Retransmits.
	'''
	@property
	def clientside_packet_retransmits(self) :
		try:
			return self._clientside_packet_retransmits
		except Exception as e :
			raise e
	'''
	set Clientside Packet Retransmits.
	'''
	@clientside_packet_retransmits.setter
	def clientside_packet_retransmits(self,clientside_packet_retransmits):
		try :
			if not isinstance(clientside_packet_retransmits,long):
				raise TypeError("clientside_packet_retransmits must be set to long value")
			self._clientside_packet_retransmits = clientside_packet_retransmits
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
			if not isinstance(server_to_client_ns_delay,long):
				raise TypeError("server_to_client_ns_delay must be set to long value")
			self._server_to_client_ns_delay = server_to_client_ns_delay
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
	get Client side 0 window count.
	'''
	@property
	def clientside_0_win(self) :
		try:
			return self._clientside_0_win
		except Exception as e :
			raise e
	'''
	set Client side 0 window count.
	'''
	@clientside_0_win.setter
	def clientside_0_win(self,clientside_0_win):
		try :
			if not isinstance(clientside_0_win,long):
				raise TypeError("clientside_0_win must be set to long value")
			self._clientside_0_win = clientside_0_win
		except Exception as e :
			raise e


	'''
	get clientside rto.
	'''
	@property
	def clientside_rto(self) :
		try:
			return self._clientside_rto
		except Exception as e :
			raise e
	'''
	set clientside rto.
	'''
	@clientside_rto.setter
	def clientside_rto(self,clientside_rto):
		try :
			if not isinstance(clientside_rto,long):
				raise TypeError("clientside_rto must be set to long value")
			self._clientside_rto = clientside_rto
		except Exception as e :
			raise e


	'''
	get Latitude
	'''
	@property
	def latitude(self) :
		try:
			return self._latitude
		except Exception as e :
			raise e
	'''
	set Latitude
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
			if not isinstance(user_type,long):
				raise TypeError("user_type must be set to long value")
			self._user_type = user_type
		except Exception as e :
			raise e


	'''
	get City
	'''
	@property
	def city(self) :
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	set City
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
			if not isinstance(l7_clientside_latency,float):
				raise TypeError("l7_clientside_latency must be set to float value")
			self._l7_clientside_latency = l7_clientside_latency
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
	get User Agent.
	'''
	@property
	def user_agent(self) :
		try:
			return self._user_agent
		except Exception as e :
			raise e
	'''
	set User Agent.
	'''
	@user_agent.setter
	def user_agent(self,user_agent):
		try :
			if not isinstance(user_agent,long):
				raise TypeError("user_agent must be set to long value")
			self._user_agent = user_agent
		except Exception as e :
			raise e

	'''
	Af HDX Report for ICA User update collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_hdx_user_l3_obj=af_hdx_user_l3()
				response = af_hdx_user_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_hdx_user_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_hdx_user_l3_obj = af_hdx_user_l3()
			option_ = options()
			option_._filter=filter_
			return af_hdx_user_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_hdx_user_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_hdx_user_l3_obj = af_hdx_user_l3()
			option_ = options()
			option_._count=True
			response = af_hdx_user_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_hdx_user_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_hdx_user_l3_obj = af_hdx_user_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_hdx_user_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_hdx_user_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_hdx_user_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_hdx_user_l3_responses, response, "af_hdx_user_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_hdx_user_l3_response_array
				i=0
				error = [af_hdx_user_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_hdx_user_l3_response_array
			i=0
			af_hdx_user_l3_objs = [af_hdx_user_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_hdx_user_l3:
					result = service.payload_formatter.string_to_bulk_resource(af_hdx_user_l3_response,self.__class__.__name__,props)
					af_hdx_user_l3_objs[i] = result.af_hdx_user_l3
					i=i+1
			return af_hdx_user_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_hdx_user_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_hdx_user_l3_response(base_response):
	def __init__(self,length=1) :
		self.af_hdx_user_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_hdx_user_l3= [ af_hdx_user_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_hdx_user_l3_responses(base_response):
	def __init__(self,length=1) :
		self.af_hdx_user_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_hdx_user_l3_response_array = [ af_hdx_user_l3() for _ in range(length)]
