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
Configuration for AF VPN Active Session details Report table for Level 3 resource
'''

class af_vpn_session_details_l3(base_resource):
	_state= ""
	_app_name= ""
	_latitude= ""
	_city_name= ""
	_exporter_id= ""
	_session_setup_time= ""
	_vpn_name= ""
	_vip_ipaddress_str= ""
	_app_type= ""
	_session_end_time= ""
	_client_ip_str= ""
	_total_bytes= ""
	_session_count= ""
	_ip_address= ""
	_server_ip= ""
	_session_id= ""
	_username= ""
	_region_name= ""
	_vpn_fqdn= ""
	_session_mode= ""
	_session_sharing_key= ""
	_longitude= ""
	_app_count= ""
	_ctnsappname= ""
	_os_type= ""
	_client_ip= ""
	_rpt_sample_time= ""
	_vip_ipadderss= ""
	_country_name= ""
	_server_ip_str= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_vpn_session_details_l3"
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
			return "af_vpn_session_details_l3s"
		except Exception as e :
			raise e



	'''
	get Session state{1: Active, 2: Inactive}
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set Session state{1: Active, 2: Inactive}
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,int):
				raise TypeError("state must be set to int value")
			self._state = state
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def app_name(self) :
		try:
			return self._app_name
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@app_name.setter
	def app_name(self,app_name):
		try :
			if not isinstance(app_name,str):
				raise TypeError("app_name must be set to str value")
			self._app_name = app_name
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
	get City Name
	'''
	@property
	def city_name(self) :
		try:
			return self._city_name
		except Exception as e :
			raise e
	'''
	set City Name
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
	get VIP Name
	'''
	@property
	def vpn_name(self) :
		try:
			return self._vpn_name
		except Exception as e :
			raise e
	'''
	set VIP Name
	'''
	@vpn_name.setter
	def vpn_name(self,vpn_name):
		try :
			if not isinstance(vpn_name,str):
				raise TypeError("vpn_name must be set to str value")
			self._vpn_name = vpn_name
		except Exception as e :
			raise e


	'''
	get Field to store the VIP address as IP Address format
	'''
	@property
	def vip_ipaddress_str(self) :
		try:
			return self._vip_ipaddress_str
		except Exception as e :
			raise e
	'''
	set Field to store the VIP address as IP Address format
	'''
	@vip_ipaddress_str.setter
	def vip_ipaddress_str(self,vip_ipaddress_str):
		try :
			if not isinstance(vip_ipaddress_str,str):
				raise TypeError("vip_ipaddress_str must be set to str value")
			self._vip_ipaddress_str = vip_ipaddress_str
		except Exception as e :
			raise e


	'''
	get Application Type (ICA/Others)
	'''
	@property
	def app_type(self) :
		try:
			return self._app_type
		except Exception as e :
			raise e
	'''
	set Application Type (ICA/Others)
	'''
	@app_type.setter
	def app_type(self,app_type):
		try :
			if not isinstance(app_type,int):
				raise TypeError("app_type must be set to int value")
			self._app_type = app_type
		except Exception as e :
			raise e


	'''
	get Session terrminated time.
	'''
	@property
	def session_end_time(self) :
		try:
			return self._session_end_time
		except Exception as e :
			raise e
	'''
	set Session terrminated time.
	'''
	@session_end_time.setter
	def session_end_time(self,session_end_time):
		try :
			if not isinstance(session_end_time,long):
				raise TypeError("session_end_time must be set to long value")
			self._session_end_time = session_end_time
		except Exception as e :
			raise e


	'''
	get Field to store the Client ip address as IP Address format
	'''
	@property
	def client_ip_str(self) :
		try:
			return self._client_ip_str
		except Exception as e :
			raise e
	'''
	set Field to store the Client ip address as IP Address format
	'''
	@client_ip_str.setter
	def client_ip_str(self,client_ip_str):
		try :
			if not isinstance(client_ip_str,str):
				raise TypeError("client_ip_str must be set to str value")
			self._client_ip_str = client_ip_str
		except Exception as e :
			raise e


	'''
	get Session total bytes
	'''
	@property
	def total_bytes(self) :
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	set Session total bytes
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
	get Session Count
	'''
	@property
	def session_count(self) :
		try:
			return self._session_count
		except Exception as e :
			raise e
	'''
	set Session Count
	'''
	@session_count.setter
	def session_count(self,session_count):
		try :
			if not isinstance(session_count,int):
				raise TypeError("session_count must be set to int value")
			self._session_count = session_count
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
			if not isinstance(server_ip,long):
				raise TypeError("server_ip must be set to long value")
			self._server_ip = server_ip
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
	get Region Name
	'''
	@property
	def region_name(self) :
		try:
			return self._region_name
		except Exception as e :
			raise e
	'''
	set Region Name
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
	get VIP FQDN
	'''
	@property
	def vpn_fqdn(self) :
		try:
			return self._vpn_fqdn
		except Exception as e :
			raise e
	'''
	set VIP FQDN
	'''
	@vpn_fqdn.setter
	def vpn_fqdn(self,vpn_fqdn):
		try :
			if not isinstance(vpn_fqdn,str):
				raise TypeError("vpn_fqdn must be set to str value")
			self._vpn_fqdn = vpn_fqdn
		except Exception as e :
			raise e


	'''
	get session mode
	'''
	@property
	def session_mode(self) :
		try:
			return self._session_mode
		except Exception as e :
			raise e
	'''
	set session mode
	'''
	@session_mode.setter
	def session_mode(self,session_mode):
		try :
			if not isinstance(session_mode,int):
				raise TypeError("session_mode must be set to int value")
			self._session_mode = session_mode
		except Exception as e :
			raise e


	'''
	get Session Sharing Key 
	'''
	@property
	def session_sharing_key(self) :
		try:
			return self._session_sharing_key
		except Exception as e :
			raise e
	'''
	set Session Sharing Key 
	'''
	@session_sharing_key.setter
	def session_sharing_key(self,session_sharing_key):
		try :
			if not isinstance(session_sharing_key,str):
				raise TypeError("session_sharing_key must be set to str value")
			self._session_sharing_key = session_sharing_key
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
	get Application Count
	'''
	@property
	def app_count(self) :
		try:
			return self._app_count
		except Exception as e :
			raise e
	'''
	set Application Count
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
	get OS Type
	'''
	@property
	def os_type(self) :
		try:
			return self._os_type
		except Exception as e :
			raise e
	'''
	set OS Type
	'''
	@os_type.setter
	def os_type(self,os_type):
		try :
			if not isinstance(os_type,int):
				raise TypeError("os_type must be set to int value")
			self._os_type = os_type
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
			if not isinstance(client_ip,long):
				raise TypeError("client_ip must be set to long value")
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
	get VIP Address
	'''
	@property
	def vip_ipadderss(self) :
		try:
			return self._vip_ipadderss
		except Exception as e :
			raise e
	'''
	set VIP Address
	'''
	@vip_ipadderss.setter
	def vip_ipadderss(self,vip_ipadderss):
		try :
			if not isinstance(vip_ipadderss,long):
				raise TypeError("vip_ipadderss must be set to long value")
			self._vip_ipadderss = vip_ipadderss
		except Exception as e :
			raise e


	'''
	get Country Name
	'''
	@property
	def country_name(self) :
		try:
			return self._country_name
		except Exception as e :
			raise e
	'''
	set Country Name
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
	get Field to store the Server ip address as IP Address format
	'''
	@property
	def server_ip_str(self) :
		try:
			return self._server_ip_str
		except Exception as e :
			raise e
	'''
	set Field to store the Server ip address as IP Address format
	'''
	@server_ip_str.setter
	def server_ip_str(self,server_ip_str):
		try :
			if not isinstance(server_ip_str,str):
				raise TypeError("server_ip_str must be set to str value")
			self._server_ip_str = server_ip_str
		except Exception as e :
			raise e

	'''
	Af VPN Report for Session information collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_vpn_session_details_l3_obj=af_vpn_session_details_l3()
				response = af_vpn_session_details_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_vpn_session_details_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_vpn_session_details_l3_obj = af_vpn_session_details_l3()
			option_ = options()
			option_._filter=filter_
			return af_vpn_session_details_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_vpn_session_details_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_vpn_session_details_l3_obj = af_vpn_session_details_l3()
			option_ = options()
			option_._count=True
			response = af_vpn_session_details_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_vpn_session_details_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_vpn_session_details_l3_obj = af_vpn_session_details_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_vpn_session_details_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_vpn_session_details_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_vpn_session_details_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_vpn_session_details_l3_responses, response, "af_vpn_session_details_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_vpn_session_details_l3_response_array
				i=0
				error = [af_vpn_session_details_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_vpn_session_details_l3_response_array
			i=0
			af_vpn_session_details_l3_objs = [af_vpn_session_details_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_vpn_session_details_l3:
					result = service.payload_formatter.string_to_bulk_resource(af_vpn_session_details_l3_response,self.__class__.__name__,props)
					af_vpn_session_details_l3_objs[i] = result.af_vpn_session_details_l3
					i=i+1
			return af_vpn_session_details_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_vpn_session_details_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_vpn_session_details_l3_response(base_response):
	def __init__(self,length=1) :
		self.af_vpn_session_details_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_vpn_session_details_l3= [ af_vpn_session_details_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_vpn_session_details_l3_responses(base_response):
	def __init__(self,length=1) :
		self.af_vpn_session_details_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_vpn_session_details_l3_response_array = [ af_vpn_session_details_l3() for _ in range(length)]
