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
Configuration for Af report for VPN Error details resource
'''

class vpn_error_details(af_generic_api):
	_country_name= ""
	_server_ip_address= ""
	_sta_ip= ""
	_ica_device_ip_address= ""
	_next_factor_policy_label= ""
	_auth_type= ""
	_vpn_server_name= ""
	_req_url= ""
	_cs_vserver_name= ""
	_current_factor_policy_label= ""
	_region_name= ""
	_username= ""
	_error_count= ""
	_vpn_fqdn= ""
	___count= ""
	_error_time= ""
	_epa_expression= ""
	_flag= ""
	_client_ip_address= ""
	_epa_method_type= ""
	_error_code= ""
	_city_name= ""
	_id= ""
	_resource_name= ""
	_sso_method_type= ""
	_authentication_state= ""
	_error_description= ""
	_ad_server_ip_address= ""
	_policy_name= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "vpn_error_details"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(vpn_error_details,self).get_object_id()
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
			return "vpn_error_detailss"
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
	STA Server IP.
	'''
	@property
	def sta_ip(self):
		try:
			return self._sta_ip
		except Exception as e :
			raise e
	'''
	STA Server IP.
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
	next factor policy label
	'''
	@property
	def next_factor_policy_label(self):
		try:
			return self._next_factor_policy_label
		except Exception as e :
			raise e
	'''
	next factor policy label
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
	Authentication Type
	'''
	@property
	def auth_type(self):
		try:
			return self._auth_type
		except Exception as e :
			raise e
	'''
	Authentication Type
	'''
	@auth_type.setter
	def auth_type(self,auth_type):
		try :
			if not isinstance(auth_type,str):
				raise TypeError("auth_type must be set to str value")
			self._auth_type = auth_type
		except Exception as e :
			raise e

	'''
	VPN Server Name.
	'''
	@property
	def vpn_server_name(self):
		try:
			return self._vpn_server_name
		except Exception as e :
			raise e
	'''
	VPN Server Name.
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
	req_url
	'''
	@property
	def req_url(self):
		try:
			return self._req_url
		except Exception as e :
			raise e
	'''
	req_url
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
	CS Server Name.
	'''
	@property
	def cs_vserver_name(self):
		try:
			return self._cs_vserver_name
		except Exception as e :
			raise e
	'''
	CS Server Name.
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
	current factor policy label
	'''
	@property
	def current_factor_policy_label(self):
		try:
			return self._current_factor_policy_label
		except Exception as e :
			raise e
	'''
	current factor policy label
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
	User Name
	'''
	@property
	def username(self):
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	User Name
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
	Error Code
	'''
	@property
	def error_count(self):
		try:
			return self._error_count
		except Exception as e :
			raise e
	'''
	Error Code
	'''
	@error_count.setter
	def error_count(self,error_count):
		try :
			if not isinstance(error_count,float):
				raise TypeError("error_count must be set to float value")
			self._error_count = error_count
		except Exception as e :
			raise e

	'''
	VPN FQDN
	'''
	@property
	def vpn_fqdn(self):
		try:
			return self._vpn_fqdn
		except Exception as e :
			raise e
	'''
	VPN FQDN
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
	Flag
	'''
	@property
	def error_time(self):
		try:
			return self._error_time
		except Exception as e :
			raise e
	'''
	Flag
	'''
	@error_time.setter
	def error_time(self,error_time):
		try :
			if not isinstance(error_time,float):
				raise TypeError("error_time must be set to float value")
			self._error_time = error_time
		except Exception as e :
			raise e

	'''
	EPA Expression
	'''
	@property
	def epa_expression(self):
		try:
			return self._epa_expression
		except Exception as e :
			raise e
	'''
	EPA Expression
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
	Flag
	'''
	@property
	def flag(self):
		try:
			return self._flag
		except Exception as e :
			raise e
	'''
	Flag
	'''
	@flag.setter
	def flag(self,flag):
		try :
			if not isinstance(flag,float):
				raise TypeError("flag must be set to float value")
			self._flag = flag
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
	EPA Method Type.
	'''
	@property
	def epa_method_type(self):
		try:
			return self._epa_method_type
		except Exception as e :
			raise e
	'''
	EPA Method Type.
	'''
	@epa_method_type.setter
	def epa_method_type(self,epa_method_type):
		try :
			if not isinstance(epa_method_type,str):
				raise TypeError("epa_method_type must be set to str value")
			self._epa_method_type = epa_method_type
		except Exception as e :
			raise e

	'''
	Error Code
	'''
	@property
	def error_code(self):
		try:
			return self._error_code
		except Exception as e :
			raise e
	'''
	Error Code
	'''
	@error_code.setter
	def error_code(self,error_code):
		try :
			if not isinstance(error_code,float):
				raise TypeError("error_code must be set to float value")
			self._error_code = error_code
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
	Id is not dicided yet
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is not dicided yet
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
	Resource Name
	'''
	@property
	def resource_name(self):
		try:
			return self._resource_name
		except Exception as e :
			raise e
	'''
	Resource Name
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
	SSO Method Type
	'''
	@property
	def sso_method_type(self):
		try:
			return self._sso_method_type
		except Exception as e :
			raise e
	'''
	SSO Method Type
	'''
	@sso_method_type.setter
	def sso_method_type(self,sso_method_type):
		try :
			if not isinstance(sso_method_type,str):
				raise TypeError("sso_method_type must be set to str value")
			self._sso_method_type = sso_method_type
		except Exception as e :
			raise e

	'''
	Authentication State
	'''
	@property
	def authentication_state(self):
		try:
			return self._authentication_state
		except Exception as e :
			raise e
	'''
	Authentication State
	'''
	@authentication_state.setter
	def authentication_state(self,authentication_state):
		try :
			if not isinstance(authentication_state,str):
				raise TypeError("authentication_state must be set to str value")
			self._authentication_state = authentication_state
		except Exception as e :
			raise e

	'''
	STA Validation Failure Counts.
	'''
	@property
	def error_description(self):
		try:
			return self._error_description
		except Exception as e :
			raise e
	'''
	STA Validation Failure Counts.
	'''
	@error_description.setter
	def error_description(self,error_description):
		try :
			if not isinstance(error_description,str):
				raise TypeError("error_description must be set to str value")
			self._error_description = error_description
		except Exception as e :
			raise e

	'''
	Active Directory Server IP Address
	'''
	@property
	def ad_server_ip_address(self):
		try:
			return self._ad_server_ip_address
		except Exception as e :
			raise e
	'''
	Active Directory Server IP Address
	'''
	@ad_server_ip_address.setter
	def ad_server_ip_address(self,ad_server_ip_address):
		try :
			if not isinstance(ad_server_ip_address,str):
				raise TypeError("ad_server_ip_address must be set to str value")
			self._ad_server_ip_address = ad_server_ip_address
		except Exception as e :
			raise e

	'''
	EPA Policy Name
	'''
	@property
	def policy_name(self):
		try:
			return self._policy_name
		except Exception as e :
			raise e
	'''
	EPA Policy Name
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
	Af Report for VPN Error Details ....
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vpn_error_details_obj=vpn_error_details()
				response = vpn_error_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vpn_error_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vpn_error_details_obj = vpn_error_details()
			option_ = options()
			option_._filter=filter_
			return vpn_error_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vpn_error_details resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vpn_error_details_obj = vpn_error_details()
			option_ = options()
			option_._count=True
			response = vpn_error_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vpn_error_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vpn_error_details_obj = vpn_error_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vpn_error_details_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - sla_enabled
	'''
	@classmethod
	def set_queryparam_sla_enabled(cls, option, value):
		option.add_queryparam("sla_enabled",value)

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

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
			result=service.payload_formatter.string_to_resource(vpn_error_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpn_error_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpn_error_details_responses, response, "vpn_error_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vpn_error_details_response_array
				i=0
				error = [vpn_error_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vpn_error_details_response_array
			i=0
			vpn_error_details_objs = [vpn_error_details() for _ in range(len(response))]
			for obj in response :
				for props in obj._vpn_error_details:
					result = service.payload_formatter.string_to_bulk_resource(vpn_error_details_response,self.__class__.__name__,props)
					vpn_error_details_objs[i] = result.vpn_error_details
					i=i+1
			return vpn_error_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vpn_error_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vpn_error_details_response(base_response):
	def __init__(self,length=1) :
		self.vpn_error_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vpn_error_details= [ vpn_error_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vpn_error_details_responses(base_response):
	def __init__(self,length=1) :
		self.vpn_error_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vpn_error_details_response_array = [ vpn_error_details() for _ in range(length)]
