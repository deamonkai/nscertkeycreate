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
Configuration for Af report for ICA User timeline resource
'''

class ica_user_timeline(af_generic_api):
	_edt_type= ""
	_server_srtt= ""
	_client_latency= ""
	_l7_clientside_latency= ""
	_name= ""
	_id= ""
	_clientside_rto= ""
	_ica_rtt= ""
	_clientside_0_win= ""
	_bandwidth= ""
	_server_jitter= ""
	_clientside_packet_retransmits= ""
	_total_bytes= ""
	_edt_count= ""
	___count= ""
	_ica_app_name= ""
	_user_count= ""
	_session_reconnect= ""
	_client_srtt= ""
	_app_enumeration_duration= ""
	_app_launch_count= ""
	_active_desktop_count= ""
	_server_latency= ""
	_rpt_sample_time= ""
	_client_jitter= ""
	_l7_serverside_latency= ""
	_non_edt_count= ""
	_serverside_packet_retransmits= ""
	_latency= ""
	_client_subnet= ""
	_serverside_rto= ""
	_serverside_0_win= ""
	_ica_device_ip_address= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_user_timeline"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ica_user_timeline,self).get_object_id()
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
			return "ica_user_timelines"
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
	ICA User client latency.
	'''
	@property
	def client_latency(self):
		try:
			return self._client_latency
		except Exception as e :
			raise e
	'''
	ICA User client latency.
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
	Name of ICA User
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Name of ICA User
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e

	'''
	Id is ICA User Name
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is ICA User Name
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
	EDT Count.
	'''
	@property
	def edt_count(self):
		try:
			return self._edt_count
		except Exception as e :
			raise e
	'''
	EDT Count.
	'''
	@edt_count.setter
	def edt_count(self,edt_count):
		try :
			if not isinstance(edt_count,long):
				raise TypeError("edt_count must be set to long value")
			self._edt_count = edt_count
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
	user_count.
	'''
	@property
	def user_count(self):
		try:
			return self._user_count
		except Exception as e :
			raise e
	'''
	user_count.
	'''
	@user_count.setter
	def user_count(self,user_count):
		try :
			if not isinstance(user_count,float):
				raise TypeError("user_count must be set to float value")
			self._user_count = user_count
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
	app_enumeration_duration.
	'''
	@property
	def app_enumeration_duration(self):
		try:
			return self._app_enumeration_duration
		except Exception as e :
			raise e
	'''
	app_enumeration_duration.
	'''
	@app_enumeration_duration.setter
	def app_enumeration_duration(self,app_enumeration_duration):
		try :
			if not isinstance(app_enumeration_duration,float):
				raise TypeError("app_enumeration_duration must be set to float value")
			self._app_enumeration_duration = app_enumeration_duration
		except Exception as e :
			raise e

	'''
	ICA User aapp launch count.
	'''
	@property
	def app_launch_count(self):
		try:
			return self._app_launch_count
		except Exception as e :
			raise e
	'''
	ICA User aapp launch count.
	'''
	@app_launch_count.setter
	def app_launch_count(self,app_launch_count):
		try :
			if not isinstance(app_launch_count,float):
				raise TypeError("app_launch_count must be set to float value")
			self._app_launch_count = app_launch_count
		except Exception as e :
			raise e

	'''
	ica active_desktop_count.
	'''
	@property
	def active_desktop_count(self):
		try:
			return self._active_desktop_count
		except Exception as e :
			raise e
	'''
	ica active_desktop_count.
	'''
	@active_desktop_count.setter
	def active_desktop_count(self,active_desktop_count):
		try :
			if not isinstance(active_desktop_count,float):
				raise TypeError("active_desktop_count must be set to float value")
			self._active_desktop_count = active_desktop_count
		except Exception as e :
			raise e

	'''
	ICA User server latency.
	'''
	@property
	def server_latency(self):
		try:
			return self._server_latency
		except Exception as e :
			raise e
	'''
	ICA User server latency.
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
	NON EDT Count.
	'''
	@property
	def non_edt_count(self):
		try:
			return self._non_edt_count
		except Exception as e :
			raise e
	'''
	NON EDT Count.
	'''
	@non_edt_count.setter
	def non_edt_count(self,non_edt_count):
		try :
			if not isinstance(non_edt_count,long):
				raise TypeError("non_edt_count must be set to long value")
			self._non_edt_count = non_edt_count
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
	ICA User total latency.
	'''
	@property
	def latency(self):
		try:
			return self._latency
		except Exception as e :
			raise e
	'''
	ICA User total latency.
	'''
	@latency.setter
	def latency(self,latency):
		try :
			if not isinstance(latency,float):
				raise TypeError("latency must be set to float value")
			self._latency = latency
		except Exception as e :
			raise e

	'''
	Client Subnet.
	'''
	@property
	def client_subnet(self):
		try:
			return self._client_subnet
		except Exception as e :
			raise e
	'''
	Client Subnet.
	'''
	@client_subnet.setter
	def client_subnet(self,client_subnet):
		try :
			if not isinstance(client_subnet,str):
				raise TypeError("client_subnet must be set to str value")
			self._client_subnet = client_subnet
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
	Af Report for ICA User..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_user_timeline_obj=ica_user_timeline()
				response = ica_user_timeline_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_user_timeline resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_user_timeline_obj = ica_user_timeline()
			option_ = options()
			option_._filter=filter_
			return ica_user_timeline_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_user_timeline resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_user_timeline_obj = ica_user_timeline()
			option_ = options()
			option_._count=True
			response = ica_user_timeline_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_user_timeline resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_user_timeline_obj = ica_user_timeline()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_user_timeline_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

	'''
	Set Query Parameter - type
	'''
	@classmethod
	def set_queryparam_type(cls, option, value):
		option.add_queryparam("type",value)

	'''
	Set Query Parameter - cr_enabled
	'''
	@classmethod
	def set_queryparam_cr_enabled(cls, option, value):
		option.add_queryparam("cr_enabled",value)

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

	'''
	Set Query Parameter - sla_enabled
	'''
	@classmethod
	def set_queryparam_sla_enabled(cls, option, value):
		option.add_queryparam("sla_enabled",value)

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_user_timeline_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_user_timeline
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_user_timeline_responses, response, "ica_user_timeline_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_user_timeline_response_array
				i=0
				error = [ica_user_timeline() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_user_timeline_response_array
			i=0
			ica_user_timeline_objs = [ica_user_timeline() for _ in range(len(response))]
			for obj in response :
				for props in obj._ica_user_timeline:
					result = service.payload_formatter.string_to_bulk_resource(ica_user_timeline_response,self.__class__.__name__,props)
					ica_user_timeline_objs[i] = result.ica_user_timeline
					i=i+1
			return ica_user_timeline_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_user_timeline,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_user_timeline_response(base_response):
	def __init__(self,length=1) :
		self.ica_user_timeline= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_user_timeline= [ ica_user_timeline() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_user_timeline_responses(base_response):
	def __init__(self,length=1) :
		self.ica_user_timeline_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_user_timeline_response_array = [ ica_user_timeline() for _ in range(length)]
