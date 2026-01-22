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
Configuration for Af report for VPN Session resource
'''

class vpn_active_sessions(af_generic_api):
	_state= ""
	_total_bytes_received= ""
	_city_name= ""
	_id= ""
	_session_setup_time= ""
	_session_end_time= ""
	_vpn_user_name= ""
	_device_ip_address= ""
	_total_bytes_sent= ""
	_session_type= ""
	_total_bytes= ""
	_server_ip= ""
	_gateway_fqdn= ""
	_bandwidth= ""
	___count= ""
	_region_name= ""
	_gateway_ipaddress= ""
	_os_type= ""
	_up_time= ""
	_client_ip= ""
	_logout_mode= ""
	_rpt_sample_time= ""
	_country_name= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "vpn_active_sessions"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(vpn_active_sessions,self).get_object_id()
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
			return "vpn_active_sessionss"
		except Exception as e :
			raise e


	'''
	State (Active/Idle/Terminated)
	'''
	@property
	def state(self):
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	State (Active/Idle/Terminated)
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
	Total Bytes Received
	'''
	@property
	def total_bytes_received(self):
		try:
			return self._total_bytes_received
		except Exception as e :
			raise e
	'''
	Total Bytes Received
	'''
	@total_bytes_received.setter
	def total_bytes_received(self,total_bytes_received):
		try :
			if not isinstance(total_bytes_received,long):
				raise TypeError("total_bytes_received must be set to long value")
			self._total_bytes_received = total_bytes_received
		except Exception as e :
			raise e

	'''
	City
	'''
	@property
	def city_name(self):
		try:
			return self._city_name
		except Exception as e :
			raise e
	'''
	City
	'''
	@city_name.setter
	def city_name(self,city_name):
		try :
			if not isinstance(city_name,str):
				raise TypeError("city_name must be set to str value")
			self._city_name = city_name
		except Exception as e :
			raise e

	'''
	Id is VPN Session ID
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is VPN Session ID
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
	vpn session start time
	'''
	@property
	def session_setup_time(self):
		try:
			return self._session_setup_time
		except Exception as e :
			raise e
	'''
	vpn session start time
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
	vpn session end time
	'''
	@property
	def session_end_time(self):
		try:
			return self._session_end_time
		except Exception as e :
			raise e
	'''
	vpn session end time
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
	Name of VPN User
	'''
	@property
	def vpn_user_name(self):
		try:
			return self._vpn_user_name
		except Exception as e :
			raise e
	'''
	Name of VPN User
	'''
	@vpn_user_name.setter
	def vpn_user_name(self,vpn_user_name):
		try :
			if not isinstance(vpn_user_name,str):
				raise TypeError("vpn_user_name must be set to str value")
			self._vpn_user_name = vpn_user_name
		except Exception as e :
			raise e

	'''
	Device IP Address.
	'''
	@property
	def device_ip_address(self):
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	Device IP Address.
	'''
	@device_ip_address.setter
	def device_ip_address(self,device_ip_address):
		try :
			if not isinstance(device_ip_address,str):
				raise TypeError("device_ip_address must be set to str value")
			self._device_ip_address = device_ip_address
		except Exception as e :
			raise e

	'''
	Total Bytes Sent
	'''
	@property
	def total_bytes_sent(self):
		try:
			return self._total_bytes_sent
		except Exception as e :
			raise e
	'''
	Total Bytes Sent
	'''
	@total_bytes_sent.setter
	def total_bytes_sent(self,total_bytes_sent):
		try :
			if not isinstance(total_bytes_sent,long):
				raise TypeError("total_bytes_sent must be set to long value")
			self._total_bytes_sent = total_bytes_sent
		except Exception as e :
			raise e

	'''
	Session type
	'''
	@property
	def session_type(self):
		try:
			return self._session_type
		except Exception as e :
			raise e
	'''
	Session type
	'''
	@session_type.setter
	def session_type(self,session_type):
		try :
			if not isinstance(session_type,str):
				raise TypeError("session_type must be set to str value")
			self._session_type = session_type
		except Exception as e :
			raise e

	'''
	Total Bytes
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total Bytes
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
	Server IP Address.
	'''
	@property
	def server_ip(self):
		try:
			return self._server_ip
		except Exception as e :
			raise e
	'''
	Server IP Address.
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
	FQDN of Gateway
	'''
	@property
	def gateway_fqdn(self):
		try:
			return self._gateway_fqdn
		except Exception as e :
			raise e
	'''
	FQDN of Gateway
	'''
	@gateway_fqdn.setter
	def gateway_fqdn(self,gateway_fqdn):
		try :
			if not isinstance(gateway_fqdn,str):
				raise TypeError("gateway_fqdn must be set to str value")
			self._gateway_fqdn = gateway_fqdn
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
	Region
	'''
	@property
	def region_name(self):
		try:
			return self._region_name
		except Exception as e :
			raise e
	'''
	Region
	'''
	@region_name.setter
	def region_name(self,region_name):
		try :
			if not isinstance(region_name,str):
				raise TypeError("region_name must be set to str value")
			self._region_name = region_name
		except Exception as e :
			raise e

	'''
	Gateway IPAddress
	'''
	@property
	def gateway_ipaddress(self):
		try:
			return self._gateway_ipaddress
		except Exception as e :
			raise e
	'''
	Gateway IPAddress
	'''
	@gateway_ipaddress.setter
	def gateway_ipaddress(self,gateway_ipaddress):
		try :
			if not isinstance(gateway_ipaddress,str):
				raise TypeError("gateway_ipaddress must be set to str value")
			self._gateway_ipaddress = gateway_ipaddress
		except Exception as e :
			raise e

	'''
	OS type
	'''
	@property
	def os_type(self):
		try:
			return self._os_type
		except Exception as e :
			raise e
	'''
	OS type
	'''
	@os_type.setter
	def os_type(self,os_type):
		try :
			if not isinstance(os_type,str):
				raise TypeError("os_type must be set to str value")
			self._os_type = os_type
		except Exception as e :
			raise e

	'''
	Session Up Time
	'''
	@property
	def up_time(self):
		try:
			return self._up_time
		except Exception as e :
			raise e
	'''
	Session Up Time
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
	Client IP Address.
	'''
	@property
	def client_ip(self):
		try:
			return self._client_ip
		except Exception as e :
			raise e
	'''
	Client IP Address.
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
	Logout Reason
	'''
	@property
	def logout_mode(self):
		try:
			return self._logout_mode
		except Exception as e :
			raise e
	'''
	Logout Reason
	'''
	@logout_mode.setter
	def logout_mode(self,logout_mode):
		try :
			if not isinstance(logout_mode,str):
				raise TypeError("logout_mode must be set to str value")
			self._logout_mode = logout_mode
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
	Country
	'''
	@property
	def country_name(self):
		try:
			return self._country_name
		except Exception as e :
			raise e
	'''
	Country
	'''
	@country_name.setter
	def country_name(self,country_name):
		try :
			if not isinstance(country_name,str):
				raise TypeError("country_name must be set to str value")
			self._country_name = country_name
		except Exception as e :
			raise e

	'''
	Af Report for VPN Error Counts ....
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vpn_active_sessions_obj=vpn_active_sessions()
				response = vpn_active_sessions_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vpn_active_sessions resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vpn_active_sessions_obj = vpn_active_sessions()
			option_ = options()
			option_._filter=filter_
			return vpn_active_sessions_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vpn_active_sessions resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vpn_active_sessions_obj = vpn_active_sessions()
			option_ = options()
			option_._count=True
			response = vpn_active_sessions_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vpn_active_sessions resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vpn_active_sessions_obj = vpn_active_sessions()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vpn_active_sessions_obj.getfiltered(service, option_)
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
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpn_active_sessions_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpn_active_sessions
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpn_active_sessions_responses, response, "vpn_active_sessions_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vpn_active_sessions_response_array
				i=0
				error = [vpn_active_sessions() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vpn_active_sessions_response_array
			i=0
			vpn_active_sessions_objs = [vpn_active_sessions() for _ in range(len(response))]
			for obj in response :
				for props in obj._vpn_active_sessions:
					result = service.payload_formatter.string_to_bulk_resource(vpn_active_sessions_response,self.__class__.__name__,props)
					vpn_active_sessions_objs[i] = result.vpn_active_sessions
					i=i+1
			return vpn_active_sessions_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vpn_active_sessions,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vpn_active_sessions_response(base_response):
	def __init__(self,length=1) :
		self.vpn_active_sessions= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vpn_active_sessions= [ vpn_active_sessions() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vpn_active_sessions_responses(base_response):
	def __init__(self,length=1) :
		self.vpn_active_sessions_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vpn_active_sessions_response_array = [ vpn_active_sessions() for _ in range(length)]
