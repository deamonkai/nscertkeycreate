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
Configuration for AF HDX Ica session state table for Level 3 resource
'''

class af_hdx_ica_session_state_details_l3(base_resource):
	_ica_rtt= ""
	_clientside_0_win= ""
	_clientside_rto= ""
	_client_total_rtt= ""
	_total_bytes= ""
	_edt= ""
	_reason_id= ""
	_ip_address= ""
	_server_ip= ""
	_desktop_name= ""
	_server_jitter= ""
	_clientside_packet_retransmits= ""
	_is_desktop= ""
	_group_reason_id= ""
	_server_srtt= ""
	_skipflow_count= ""
	_exporter_id= ""
	_client_rtt= ""
	_session_setup_time= ""
	_serverside_packet_retransmits= ""
	_server_total_rtt= ""
	_client_ip= ""
	_rpt_sample_time= ""
	_client_jitter= ""
	_serverside_0_win= ""
	_serverside_rto= ""
	_server_rtt= ""
	_session_reconnect= ""
	_session_id= ""
	_username= ""
	_client_srtt= ""
	_ctnsappname= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_hdx_ica_session_state_details_l3"
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
			return "af_hdx_ica_session_state_details_l3s"
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
	get Error code when skip flow happens
	'''
	@property
	def reason_id(self) :
		try:
			return self._reason_id
		except Exception as e :
			raise e
	'''
	set Error code when skip flow happens
	'''
	@reason_id.setter
	def reason_id(self,reason_id):
		try :
			if not isinstance(reason_id,long):
				raise TypeError("reason_id must be set to long value")
			self._reason_id = reason_id
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
	get Client side packet retransmits.
	'''
	@property
	def clientside_packet_retransmits(self) :
		try:
			return self._clientside_packet_retransmits
		except Exception as e :
			raise e
	'''
	set Client side packet retransmits.
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
			if not isinstance(is_desktop,long):
				raise TypeError("is_desktop must be set to long value")
			self._is_desktop = is_desktop
		except Exception as e :
			raise e


	'''
	get Group skip flow id
	'''
	@property
	def group_reason_id(self) :
		try:
			return self._group_reason_id
		except Exception as e :
			raise e
	'''
	set Group skip flow id
	'''
	@group_reason_id.setter
	def group_reason_id(self,group_reason_id):
		try :
			if not isinstance(group_reason_id,long):
				raise TypeError("group_reason_id must be set to long value")
			self._group_reason_id = group_reason_id
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
	get Number of time skip flow happens
	'''
	@property
	def skipflow_count(self) :
		try:
			return self._skipflow_count
		except Exception as e :
			raise e
	'''
	set Number of time skip flow happens
	'''
	@skipflow_count.setter
	def skipflow_count(self,skipflow_count):
		try :
			if not isinstance(skipflow_count,long):
				raise TypeError("skipflow_count must be set to long value")
			self._skipflow_count = skipflow_count
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
	get Server side packet retransmits.
	'''
	@property
	def serverside_packet_retransmits(self) :
		try:
			return self._serverside_packet_retransmits
		except Exception as e :
			raise e
	'''
	set Server side packet retransmits.
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
	get Session reconnect.
	'''
	@property
	def session_reconnect(self) :
		try:
			return self._session_reconnect
		except Exception as e :
			raise e
	'''
	set Session reconnect.
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
	Af HDX Report for Device skip flow details..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_hdx_ica_session_state_details_l3_obj=af_hdx_ica_session_state_details_l3()
				response = af_hdx_ica_session_state_details_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_hdx_ica_session_state_details_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_hdx_ica_session_state_details_l3_obj = af_hdx_ica_session_state_details_l3()
			option_ = options()
			option_._filter=filter_
			return af_hdx_ica_session_state_details_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_hdx_ica_session_state_details_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_hdx_ica_session_state_details_l3_obj = af_hdx_ica_session_state_details_l3()
			option_ = options()
			option_._count=True
			response = af_hdx_ica_session_state_details_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_hdx_ica_session_state_details_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_hdx_ica_session_state_details_l3_obj = af_hdx_ica_session_state_details_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_hdx_ica_session_state_details_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_hdx_ica_session_state_details_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_hdx_ica_session_state_details_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_hdx_ica_session_state_details_l3_responses, response, "af_hdx_ica_session_state_details_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_hdx_ica_session_state_details_l3_response_array
				i=0
				error = [af_hdx_ica_session_state_details_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_hdx_ica_session_state_details_l3_response_array
			i=0
			af_hdx_ica_session_state_details_l3_objs = [af_hdx_ica_session_state_details_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_hdx_ica_session_state_details_l3:
					result = service.payload_formatter.string_to_bulk_resource(af_hdx_ica_session_state_details_l3_response,self.__class__.__name__,props)
					af_hdx_ica_session_state_details_l3_objs[i] = result.af_hdx_ica_session_state_details_l3
					i=i+1
			return af_hdx_ica_session_state_details_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_hdx_ica_session_state_details_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_hdx_ica_session_state_details_l3_response(base_response):
	def __init__(self,length=1) :
		self.af_hdx_ica_session_state_details_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_hdx_ica_session_state_details_l3= [ af_hdx_ica_session_state_details_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_hdx_ica_session_state_details_l3_responses(base_response):
	def __init__(self,length=1) :
		self.af_hdx_ica_session_state_details_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_hdx_ica_session_state_details_l3_response_array = [ af_hdx_ica_session_state_details_l3() for _ in range(length)]
