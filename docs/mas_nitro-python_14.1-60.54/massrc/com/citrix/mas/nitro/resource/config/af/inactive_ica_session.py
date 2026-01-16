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
Configuration for Af report for ICA Session InActive resource
'''

class inactive_ica_session(af_generic_api):
	_device_type= ""
	_client_srtt= ""
	_server_latency= ""
	_client_tx_bytes= ""
	___count= ""
	_ica_app_name= ""
	_server_ip_address= ""
	_serverside_rto= ""
	_launch_duration= ""
	_ica_device_ip_address= ""
	_serverside_0_win= ""
	_rpt_sample_time= ""
	_client_jitter= ""
	_up_time= ""
	_vdi_image_name= ""
	_session_rtt= ""
	_hdx_desktop_username= ""
	_ica_user_name= ""
	_session_setup_time= ""
	_id= ""
	_client_rx_bytes= ""
	_pn_agent_version= ""
	_server_srtt= ""
	_edt_type= ""
	_client_latency= ""
	_session_duration= ""
	_state= ""
	_server_jitter= ""
	_bandwidth= ""
	_total_bytes= ""
	_session_type= ""
	_clientside_rto= ""
	_client_ip_address= ""
	_application_enumeration_duration= ""
	_ica_rtt= ""
	_receiver_version= ""
	_clientside_0_win= ""
	_session_end_time= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "inactive_ica_session"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(inactive_ica_session,self).get_object_id()
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
			return "inactive_ica_sessions"
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
	Af Report for ICA User..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				inactive_ica_session_obj=inactive_ica_session()
				response = inactive_ica_session_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of inactive_ica_session resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			inactive_ica_session_obj = inactive_ica_session()
			option_ = options()
			option_._filter=filter_
			return inactive_ica_session_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the inactive_ica_session resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			inactive_ica_session_obj = inactive_ica_session()
			option_ = options()
			option_._count=True
			response = inactive_ica_session_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of inactive_ica_session resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			inactive_ica_session_obj = inactive_ica_session()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = inactive_ica_session_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(inactive_ica_session_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.inactive_ica_session
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(inactive_ica_session_responses, response, "inactive_ica_session_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.inactive_ica_session_response_array
				i=0
				error = [inactive_ica_session() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.inactive_ica_session_response_array
			i=0
			inactive_ica_session_objs = [inactive_ica_session() for _ in range(len(response))]
			for obj in response :
				for props in obj._inactive_ica_session:
					result = service.payload_formatter.string_to_bulk_resource(inactive_ica_session_response,self.__class__.__name__,props)
					inactive_ica_session_objs[i] = result.inactive_ica_session
					i=i+1
			return inactive_ica_session_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(inactive_ica_session,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class inactive_ica_session_response(base_response):
	def __init__(self,length=1) :
		self.inactive_ica_session= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.inactive_ica_session= [ inactive_ica_session() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class inactive_ica_session_responses(base_response):
	def __init__(self,length=1) :
		self.inactive_ica_session_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.inactive_ica_session_response_array = [ inactive_ica_session() for _ in range(length)]
