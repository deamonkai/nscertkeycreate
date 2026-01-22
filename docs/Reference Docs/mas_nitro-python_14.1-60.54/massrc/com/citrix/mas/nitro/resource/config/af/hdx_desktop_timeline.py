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
Configuration for Af report for HDX Desktop timeline resource
'''

class hdx_desktop_timeline(af_generic_api):
	_session_duration= ""
	_client_latency= ""
	_server_srtt= ""
	_edt_type= ""
	_active_session_count= ""
	___count= ""
	_username= ""
	_id= ""
	_active_desktop_count= ""
	_server_latency= ""
	_client_srtt= ""
	_ica_rtt= ""
	_selected_time_total_byte= ""
	_duration_summary_bandwidth= ""
	_desktop_count= ""
	_rpt_sample_time= ""
	_total_bytes= ""
	_ica_device_ip_address= ""
	_ip_address= ""
	_bandwidth= ""
	_client_subnet= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "hdx_desktop_timeline"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(hdx_desktop_timeline,self).get_object_id()
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
			return "hdx_desktop_timelines"
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
	active_session_count.
	'''
	@property
	def active_session_count(self):
		try:
			return self._active_session_count
		except Exception as e :
			raise e
	'''
	active_session_count.
	'''
	@active_session_count.setter
	def active_session_count(self,active_session_count):
		try :
			if not isinstance(active_session_count,float):
				raise TypeError("active_session_count must be set to float value")
			self._active_session_count = active_session_count
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
	username
	'''
	@property
	def username(self):
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	username
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
	Id is HDX Desktop username
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is HDX Desktop username
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
	desktop_count.
	'''
	@property
	def desktop_count(self):
		try:
			return self._desktop_count
		except Exception as e :
			raise e
	'''
	desktop_count.
	'''
	@desktop_count.setter
	def desktop_count(self,desktop_count):
		try :
			if not isinstance(desktop_count,float):
				raise TypeError("desktop_count must be set to float value")
			self._desktop_count = desktop_count
		except Exception as e :
			raise e

	'''
	Report Sample time (epoch time)
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	Report Sample time (epoch time)
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
	Ica device IP Address.
	'''
	@property
	def ica_device_ip_address(self):
		try:
			return self._ica_device_ip_address
		except Exception as e :
			raise e
	'''
	Ica device IP Address.
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
	NetScaler IP Address.
	'''
	@property
	def ip_address(self):
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address.
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
	Af Report for HDX Desktop..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				hdx_desktop_timeline_obj=hdx_desktop_timeline()
				response = hdx_desktop_timeline_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of hdx_desktop_timeline resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			hdx_desktop_timeline_obj = hdx_desktop_timeline()
			option_ = options()
			option_._filter=filter_
			return hdx_desktop_timeline_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the hdx_desktop_timeline resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			hdx_desktop_timeline_obj = hdx_desktop_timeline()
			option_ = options()
			option_._count=True
			response = hdx_desktop_timeline_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of hdx_desktop_timeline resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			hdx_desktop_timeline_obj = hdx_desktop_timeline()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = hdx_desktop_timeline_obj.getfiltered(service, option_)
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
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - sla_enabled
	'''
	@classmethod
	def set_queryparam_sla_enabled(cls, option, value):
		option.add_queryparam("sla_enabled",value)

	'''
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(hdx_desktop_timeline_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.hdx_desktop_timeline
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(hdx_desktop_timeline_responses, response, "hdx_desktop_timeline_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.hdx_desktop_timeline_response_array
				i=0
				error = [hdx_desktop_timeline() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.hdx_desktop_timeline_response_array
			i=0
			hdx_desktop_timeline_objs = [hdx_desktop_timeline() for _ in range(len(response))]
			for obj in response :
				for props in obj._hdx_desktop_timeline:
					result = service.payload_formatter.string_to_bulk_resource(hdx_desktop_timeline_response,self.__class__.__name__,props)
					hdx_desktop_timeline_objs[i] = result.hdx_desktop_timeline
					i=i+1
			return hdx_desktop_timeline_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(hdx_desktop_timeline,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class hdx_desktop_timeline_response(base_response):
	def __init__(self,length=1) :
		self.hdx_desktop_timeline= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.hdx_desktop_timeline= [ hdx_desktop_timeline() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class hdx_desktop_timeline_responses(base_response):
	def __init__(self,length=1) :
		self.hdx_desktop_timeline_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.hdx_desktop_timeline_response_array = [ hdx_desktop_timeline() for _ in range(length)]
