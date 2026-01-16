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
Configuration for AF VPN Session Error details table for Level 4 resource
'''

class af_vpn_error_details_l4(base_resource):
	_sso_method_type= ""
	_authentication_state= ""
	_policy_name= ""
	_count_sta= ""
	_epa_session_id= ""
	_resource_name= ""
	_exporter_id= ""
	_city_name= ""
	_latitude= ""
	_client_ip_str= ""
	_epa_method_type= ""
	_flag= ""
	_session_state= ""
	_error_code= ""
	_epa_expression= ""
	_server_ip= ""
	_ip_address= ""
	_count_epa= ""
	_session_id= ""
	_count_ad= ""
	_ctnsappname= ""
	_longitude= ""
	_session_mode= ""
	_vpn_fqdn= ""
	_current_factor_policy_label= ""
	_region_name= ""
	_username= ""
	_auth_type= ""
	_vpn_server_name= ""
	_rpt_sample_time= ""
	_client_ip= ""
	_cs_vserver_name= ""
	_req_url= ""
	_error_counts= ""
	_server_ip_str= ""
	_server_ip_address= ""
	_country_name= ""
	_sta_ip= ""
	_next_factor_policy_label= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_vpn_error_details_l4"
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
			return "af_vpn_error_details_l4s"
		except Exception as e :
			raise e



	'''
	get SSO Method Type
	'''
	@property
	def sso_method_type(self) :
		try:
			return self._sso_method_type
		except Exception as e :
			raise e
	'''
	set SSO Method Type
	'''
	@sso_method_type.setter
	def sso_method_type(self,sso_method_type):
		try :
			if not isinstance(sso_method_type,int):
				raise TypeError("sso_method_type must be set to int value")
			self._sso_method_type = sso_method_type
		except Exception as e :
			raise e


	'''
	get Authentication State
	'''
	@property
	def authentication_state(self) :
		try:
			return self._authentication_state
		except Exception as e :
			raise e
	'''
	set Authentication State
	'''
	@authentication_state.setter
	def authentication_state(self,authentication_state):
		try :
			if not isinstance(authentication_state,int):
				raise TypeError("authentication_state must be set to int value")
			self._authentication_state = authentication_state
		except Exception as e :
			raise e


	'''
	get Policy Name.
	'''
	@property
	def policy_name(self) :
		try:
			return self._policy_name
		except Exception as e :
			raise e
	'''
	set Policy Name.
	'''
	@policy_name.setter
	def policy_name(self,policy_name):
		try :
			if not isinstance(policy_name,str):
				raise TypeError("policy_name must be set to str value")
			self._policy_name = policy_name
		except Exception as e :
			raise e


	'''
	get Error Count for STA Failure
	'''
	@property
	def count_sta(self) :
		try:
			return self._count_sta
		except Exception as e :
			raise e
	'''
	set Error Count for STA Failure
	'''
	@count_sta.setter
	def count_sta(self,count_sta):
		try :
			if not isinstance(count_sta,int):
				raise TypeError("count_sta must be set to int value")
			self._count_sta = count_sta
		except Exception as e :
			raise e


	'''
	get EPA Session GUID.
	'''
	@property
	def epa_session_id(self) :
		try:
			return self._epa_session_id
		except Exception as e :
			raise e
	'''
	set EPA Session GUID.
	'''
	@epa_session_id.setter
	def epa_session_id(self,epa_session_id):
		try :
			if not isinstance(epa_session_id,str):
				raise TypeError("epa_session_id must be set to str value")
			self._epa_session_id = epa_session_id
		except Exception as e :
			raise e


	'''
	get Resource Name.
	'''
	@property
	def resource_name(self) :
		try:
			return self._resource_name
		except Exception as e :
			raise e
	'''
	set Resource Name.
	'''
	@resource_name.setter
	def resource_name(self,resource_name):
		try :
			if not isinstance(resource_name,str):
				raise TypeError("resource_name must be set to str value")
			self._resource_name = resource_name
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
	get EPA Auth Type.
	'''
	@property
	def epa_method_type(self) :
		try:
			return self._epa_method_type
		except Exception as e :
			raise e
	'''
	set EPA Auth Type.
	'''
	@epa_method_type.setter
	def epa_method_type(self,epa_method_type):
		try :
			if not isinstance(epa_method_type,int):
				raise TypeError("epa_method_type must be set to int value")
			self._epa_method_type = epa_method_type
		except Exception as e :
			raise e


	'''
	get Flag to determine type of error(EPA, AD Failure, STA Failure)
	'''
	@property
	def flag(self) :
		try:
			return self._flag
		except Exception as e :
			raise e
	'''
	set Flag to determine type of error(EPA, AD Failure, STA Failure)
	'''
	@flag.setter
	def flag(self,flag):
		try :
			if not isinstance(flag,int):
				raise TypeError("flag must be set to int value")
			self._flag = flag
		except Exception as e :
			raise e


	'''
	get Session State Failure
	'''
	@property
	def session_state(self) :
		try:
			return self._session_state
		except Exception as e :
			raise e
	'''
	set Session State Failure
	'''
	@session_state.setter
	def session_state(self,session_state):
		try :
			if not isinstance(session_state,int):
				raise TypeError("session_state must be set to int value")
			self._session_state = session_state
		except Exception as e :
			raise e


	'''
	get Error code for AD Failure
	'''
	@property
	def error_code(self) :
		try:
			return self._error_code
		except Exception as e :
			raise e
	'''
	set Error code for AD Failure
	'''
	@error_code.setter
	def error_code(self,error_code):
		try :
			if not isinstance(error_code,int):
				raise TypeError("error_code must be set to int value")
			self._error_code = error_code
		except Exception as e :
			raise e


	'''
	get EPA Expression
	'''
	@property
	def epa_expression(self) :
		try:
			return self._epa_expression
		except Exception as e :
			raise e
	'''
	set EPA Expression
	'''
	@epa_expression.setter
	def epa_expression(self,epa_expression):
		try :
			if not isinstance(epa_expression,str):
				raise TypeError("epa_expression must be set to str value")
			self._epa_expression = epa_expression
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
	get Error Count for EPA Failure
	'''
	@property
	def count_epa(self) :
		try:
			return self._count_epa
		except Exception as e :
			raise e
	'''
	set Error Count for EPA Failure
	'''
	@count_epa.setter
	def count_epa(self,count_epa):
		try :
			if not isinstance(count_epa,int):
				raise TypeError("count_epa must be set to int value")
			self._count_epa = count_epa
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
	get Error Count for AD Failuree
	'''
	@property
	def count_ad(self) :
		try:
			return self._count_ad
		except Exception as e :
			raise e
	'''
	set Error Count for AD Failuree
	'''
	@count_ad.setter
	def count_ad(self,count_ad):
		try :
			if not isinstance(count_ad,int):
				raise TypeError("count_ad must be set to int value")
			self._count_ad = count_ad
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
	get Session Mode faliure
	'''
	@property
	def session_mode(self) :
		try:
			return self._session_mode
		except Exception as e :
			raise e
	'''
	set Session Mode faliure
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
	get VPN Fqdn
	'''
	@property
	def vpn_fqdn(self) :
		try:
			return self._vpn_fqdn
		except Exception as e :
			raise e
	'''
	set VPN Fqdn
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
	get current_factor_policy_label
	'''
	@property
	def current_factor_policy_label(self) :
		try:
			return self._current_factor_policy_label
		except Exception as e :
			raise e
	'''
	set current_factor_policy_label
	'''
	@current_factor_policy_label.setter
	def current_factor_policy_label(self,current_factor_policy_label):
		try :
			if not isinstance(current_factor_policy_label,str):
				raise TypeError("current_factor_policy_label must be set to str value")
			self._current_factor_policy_label = current_factor_policy_label
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
	get Authentication Type (LDAP, RADIUS ...)
	'''
	@property
	def auth_type(self) :
		try:
			return self._auth_type
		except Exception as e :
			raise e
	'''
	set Authentication Type (LDAP, RADIUS ...)
	'''
	@auth_type.setter
	def auth_type(self,auth_type):
		try :
			if not isinstance(auth_type,int):
				raise TypeError("auth_type must be set to int value")
			self._auth_type = auth_type
		except Exception as e :
			raise e


	'''
	get VPN Server Name.
	'''
	@property
	def vpn_server_name(self) :
		try:
			return self._vpn_server_name
		except Exception as e :
			raise e
	'''
	set VPN Server Name.
	'''
	@vpn_server_name.setter
	def vpn_server_name(self,vpn_server_name):
		try :
			if not isinstance(vpn_server_name,str):
				raise TypeError("vpn_server_name must be set to str value")
			self._vpn_server_name = vpn_server_name
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
			if not isinstance(client_ip,long):
				raise TypeError("client_ip must be set to long value")
			self._client_ip = client_ip
		except Exception as e :
			raise e


	'''
	get CS Server Name.
	'''
	@property
	def cs_vserver_name(self) :
		try:
			return self._cs_vserver_name
		except Exception as e :
			raise e
	'''
	set CS Server Name.
	'''
	@cs_vserver_name.setter
	def cs_vserver_name(self,cs_vserver_name):
		try :
			if not isinstance(cs_vserver_name,str):
				raise TypeError("cs_vserver_name must be set to str value")
			self._cs_vserver_name = cs_vserver_name
		except Exception as e :
			raise e


	'''
	get req_url
	'''
	@property
	def req_url(self) :
		try:
			return self._req_url
		except Exception as e :
			raise e
	'''
	set req_url
	'''
	@req_url.setter
	def req_url(self,req_url):
		try :
			if not isinstance(req_url,str):
				raise TypeError("req_url must be set to str value")
			self._req_url = req_url
		except Exception as e :
			raise e


	'''
	get Error Count 
	'''
	@property
	def error_counts(self) :
		try:
			return self._error_counts
		except Exception as e :
			raise e
	'''
	set Error Count 
	'''
	@error_counts.setter
	def error_counts(self,error_counts):
		try :
			if not isinstance(error_counts,int):
				raise TypeError("error_counts must be set to int value")
			self._error_counts = error_counts
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
	get Server IP Address/Agent Name
	'''
	@property
	def server_ip_address(self) :
		try:
			return self._server_ip_address
		except Exception as e :
			raise e
	'''
	set Server IP Address/Agent Name
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
	get STA IP Address/Agent Name
	'''
	@property
	def sta_ip(self) :
		try:
			return self._sta_ip
		except Exception as e :
			raise e
	'''
	set STA IP Address/Agent Name
	'''
	@sta_ip.setter
	def sta_ip(self,sta_ip):
		try :
			if not isinstance(sta_ip,str):
				raise TypeError("sta_ip must be set to str value")
			self._sta_ip = sta_ip
		except Exception as e :
			raise e


	'''
	get next_factor_policy_label
	'''
	@property
	def next_factor_policy_label(self) :
		try:
			return self._next_factor_policy_label
		except Exception as e :
			raise e
	'''
	set next_factor_policy_label
	'''
	@next_factor_policy_label.setter
	def next_factor_policy_label(self,next_factor_policy_label):
		try :
			if not isinstance(next_factor_policy_label,str):
				raise TypeError("next_factor_policy_label must be set to str value")
			self._next_factor_policy_label = next_factor_policy_label
		except Exception as e :
			raise e

	'''
	Af VPN Error Report for collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_vpn_error_details_l4_obj=af_vpn_error_details_l4()
				response = af_vpn_error_details_l4_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_vpn_error_details_l4 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_vpn_error_details_l4_obj = af_vpn_error_details_l4()
			option_ = options()
			option_._filter=filter_
			return af_vpn_error_details_l4_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_vpn_error_details_l4 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_vpn_error_details_l4_obj = af_vpn_error_details_l4()
			option_ = options()
			option_._count=True
			response = af_vpn_error_details_l4_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_vpn_error_details_l4 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_vpn_error_details_l4_obj = af_vpn_error_details_l4()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_vpn_error_details_l4_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_vpn_error_details_l4_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_vpn_error_details_l4
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_vpn_error_details_l4_responses, response, "af_vpn_error_details_l4_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_vpn_error_details_l4_response_array
				i=0
				error = [af_vpn_error_details_l4() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_vpn_error_details_l4_response_array
			i=0
			af_vpn_error_details_l4_objs = [af_vpn_error_details_l4() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_vpn_error_details_l4:
					result = service.payload_formatter.string_to_bulk_resource(af_vpn_error_details_l4_response,self.__class__.__name__,props)
					af_vpn_error_details_l4_objs[i] = result.af_vpn_error_details_l4
					i=i+1
			return af_vpn_error_details_l4_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_vpn_error_details_l4,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_vpn_error_details_l4_response(base_response):
	def __init__(self,length=1) :
		self.af_vpn_error_details_l4= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_vpn_error_details_l4= [ af_vpn_error_details_l4() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_vpn_error_details_l4_responses(base_response):
	def __init__(self,length=1) :
		self.af_vpn_error_details_l4_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_vpn_error_details_l4_response_array = [ af_vpn_error_details_l4() for _ in range(length)]
