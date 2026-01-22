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
Configuration for AF Threat exporter raw data table for Level 2 resource
'''

class af_threat_exporter_data_l2(base_resource):
	_appfw_aaa_username= ""
	_not_blocked_flags= ""
	_http_req_url= ""
	_violation_type= ""
	_attack_category= ""
	_violation_category= ""
	_ip_address= ""
	_violation_threat_index= ""
	_profile_name= ""
	_latitude= ""
	_exporter_id= ""
	_transactionid= ""
	_backend_vserver= ""
	_app_threat_index= ""
	_true_client_ip= ""
	_city= ""
	_src_ip_address_str= ""
	_appname= ""
	_attack_time= ""
	_region_code= ""
	_violation_action= ""
	_source_ipv6_address= ""
	_http_method= ""
	_rpt_sample_time= ""
	_severity_type= ""
	_block_flags= ""
	_country_code= ""
	_violation_name= ""
	_ctnsappname= ""
	_transformed_flags= ""
	_longitude= ""
	_iprep_category= ""
	_severity= ""
	_appfw_aaa_user_email= ""
	_backend_appname= ""
	_total_attacks= ""
	_counter_value= ""
	_violation_location= ""
	_signature_category= ""
	_source_ip_address= ""
	_violation_value= ""
	_session_id= ""
	_iprep_score= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_threat_exporter_data_l2"
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
			return "af_threat_exporter_data_l2s"
		except Exception as e :
			raise e



	'''
	get AppFW AAA user name
	'''
	@property
	def appfw_aaa_username(self) :
		try:
			return self._appfw_aaa_username
		except Exception as e :
			raise e
	'''
	set AppFW AAA user name
	'''
	@appfw_aaa_username.setter
	def appfw_aaa_username(self,appfw_aaa_username):
		try :
			if not isinstance(appfw_aaa_username,str):
				raise TypeError("appfw_aaa_username must be set to str value")
			self._appfw_aaa_username = appfw_aaa_username
		except Exception as e :
			raise e


	'''
	get block_flags.
	'''
	@property
	def not_blocked_flags(self) :
		try:
			return self._not_blocked_flags
		except Exception as e :
			raise e
	'''
	set block_flags.
	'''
	@not_blocked_flags.setter
	def not_blocked_flags(self,not_blocked_flags):
		try :
			if not isinstance(not_blocked_flags,int):
				raise TypeError("not_blocked_flags must be set to int value")
			self._not_blocked_flags = not_blocked_flags
		except Exception as e :
			raise e


	'''
	get HTTP Request URL.
	'''
	@property
	def http_req_url(self) :
		try:
			return self._http_req_url
		except Exception as e :
			raise e
	'''
	set HTTP Request URL.
	'''
	@http_req_url.setter
	def http_req_url(self,http_req_url):
		try :
			if not isinstance(http_req_url,str):
				raise TypeError("http_req_url must be set to str value")
			self._http_req_url = http_req_url
		except Exception as e :
			raise e


	'''
	get violation_type.
	'''
	@property
	def violation_type(self) :
		try:
			return self._violation_type
		except Exception as e :
			raise e
	'''
	set violation_type.
	'''
	@violation_type.setter
	def violation_type(self,violation_type):
		try :
			if not isinstance(violation_type,int):
				raise TypeError("violation_type must be set to int value")
			self._violation_type = violation_type
		except Exception as e :
			raise e


	'''
	get Attack Category
	'''
	@property
	def attack_category(self) :
		try:
			return self._attack_category
		except Exception as e :
			raise e
	'''
	set Attack Category
	'''
	@attack_category.setter
	def attack_category(self,attack_category):
		try :
			if not isinstance(attack_category,int):
				raise TypeError("attack_category must be set to int value")
			self._attack_category = attack_category
		except Exception as e :
			raise e


	'''
	get violation_category.
	'''
	@property
	def violation_category(self) :
		try:
			return self._violation_category
		except Exception as e :
			raise e
	'''
	set violation_category.
	'''
	@violation_category.setter
	def violation_category(self,violation_category):
		try :
			if not isinstance(violation_category,int):
				raise TypeError("violation_category must be set to int value")
			self._violation_category = violation_category
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
	get violation threat index.
	'''
	@property
	def violation_threat_index(self) :
		try:
			return self._violation_threat_index
		except Exception as e :
			raise e
	'''
	set violation threat index.
	'''
	@violation_threat_index.setter
	def violation_threat_index(self,violation_threat_index):
		try :
			if not isinstance(violation_threat_index,int):
				raise TypeError("violation_threat_index must be set to int value")
			self._violation_threat_index = violation_threat_index
		except Exception as e :
			raise e


	'''
	get profile_name
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set profile_name
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
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
	get transactionid.
	'''
	@property
	def transactionid(self) :
		try:
			return self._transactionid
		except Exception as e :
			raise e
	'''
	set transactionid.
	'''
	@transactionid.setter
	def transactionid(self,transactionid):
		try :
			if not isinstance(transactionid,long):
				raise TypeError("transactionid must be set to long value")
			self._transactionid = transactionid
		except Exception as e :
			raise e


	'''
	get Backend Vserver
	'''
	@property
	def backend_vserver(self) :
		try:
			return self._backend_vserver
		except Exception as e :
			raise e
	'''
	set Backend Vserver
	'''
	@backend_vserver.setter
	def backend_vserver(self,backend_vserver):
		try :
			if not isinstance(backend_vserver,str):
				raise TypeError("backend_vserver must be set to str value")
			self._backend_vserver = backend_vserver
		except Exception as e :
			raise e


	'''
	get violation threat index.
	'''
	@property
	def app_threat_index(self) :
		try:
			return self._app_threat_index
		except Exception as e :
			raise e
	'''
	set violation threat index.
	'''
	@app_threat_index.setter
	def app_threat_index(self,app_threat_index):
		try :
			if not isinstance(app_threat_index,int):
				raise TypeError("app_threat_index must be set to int value")
			self._app_threat_index = app_threat_index
		except Exception as e :
			raise e


	'''
	get True Client IP Address
	'''
	@property
	def true_client_ip(self) :
		try:
			return self._true_client_ip
		except Exception as e :
			raise e
	'''
	set True Client IP Address
	'''
	@true_client_ip.setter
	def true_client_ip(self,true_client_ip):
		try :
			if not isinstance(true_client_ip,str):
				raise TypeError("true_client_ip must be set to str value")
			self._true_client_ip = true_client_ip
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
	get Field to store the Client ip address as IP Address format
	'''
	@property
	def src_ip_address_str(self) :
		try:
			return self._src_ip_address_str
		except Exception as e :
			raise e
	'''
	set Field to store the Client ip address as IP Address format
	'''
	@src_ip_address_str.setter
	def src_ip_address_str(self,src_ip_address_str):
		try :
			if not isinstance(src_ip_address_str,str):
				raise TypeError("src_ip_address_str must be set to str value")
			self._src_ip_address_str = src_ip_address_str
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@appname.setter
	def appname(self,appname):
		try :
			if not isinstance(appname,str):
				raise TypeError("appname must be set to str value")
			self._appname = appname
		except Exception as e :
			raise e


	'''
	get Attack Report Sample time.
	'''
	@property
	def attack_time(self) :
		try:
			return self._attack_time
		except Exception as e :
			raise e
	'''
	set Attack Report Sample time.
	'''
	@attack_time.setter
	def attack_time(self,attack_time):
		try :
			if not isinstance(attack_time,long):
				raise TypeError("attack_time must be set to long value")
			self._attack_time = attack_time
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
	get action.
	'''
	@property
	def violation_action(self) :
		try:
			return self._violation_action
		except Exception as e :
			raise e
	'''
	set action.
	'''
	@violation_action.setter
	def violation_action(self,violation_action):
		try :
			if not isinstance(violation_action,int):
				raise TypeError("violation_action must be set to int value")
			self._violation_action = violation_action
		except Exception as e :
			raise e


	'''
	get Field to store the client ipv6 address
	'''
	@property
	def source_ipv6_address(self) :
		try:
			return self._source_ipv6_address
		except Exception as e :
			raise e
	'''
	set Field to store the client ipv6 address
	'''
	@source_ipv6_address.setter
	def source_ipv6_address(self,source_ipv6_address):
		try :
			if not isinstance(source_ipv6_address,str):
				raise TypeError("source_ipv6_address must be set to str value")
			self._source_ipv6_address = source_ipv6_address
		except Exception as e :
			raise e


	'''
	get HTTP Method.
	'''
	@property
	def http_method(self) :
		try:
			return self._http_method
		except Exception as e :
			raise e
	'''
	set HTTP Method.
	'''
	@http_method.setter
	def http_method(self,http_method):
		try :
			if not isinstance(http_method,int):
				raise TypeError("http_method must be set to int value")
			self._http_method = http_method
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
	get severity_type.
	'''
	@property
	def severity_type(self) :
		try:
			return self._severity_type
		except Exception as e :
			raise e
	'''
	set severity_type.
	'''
	@severity_type.setter
	def severity_type(self,severity_type):
		try :
			if not isinstance(severity_type,int):
				raise TypeError("severity_type must be set to int value")
			self._severity_type = severity_type
		except Exception as e :
			raise e


	'''
	get block_flags.
	'''
	@property
	def block_flags(self) :
		try:
			return self._block_flags
		except Exception as e :
			raise e
	'''
	set block_flags.
	'''
	@block_flags.setter
	def block_flags(self,block_flags):
		try :
			if not isinstance(block_flags,int):
				raise TypeError("block_flags must be set to int value")
			self._block_flags = block_flags
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
	get Violation Name.
	'''
	@property
	def violation_name(self) :
		try:
			return self._violation_name
		except Exception as e :
			raise e
	'''
	set Violation Name.
	'''
	@violation_name.setter
	def violation_name(self,violation_name):
		try :
			if not isinstance(violation_name,str):
				raise TypeError("violation_name must be set to str value")
			self._violation_name = violation_name
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
	get transformed_flags.
	'''
	@property
	def transformed_flags(self) :
		try:
			return self._transformed_flags
		except Exception as e :
			raise e
	'''
	set transformed_flags.
	'''
	@transformed_flags.setter
	def transformed_flags(self,transformed_flags):
		try :
			if not isinstance(transformed_flags,int):
				raise TypeError("transformed_flags must be set to int value")
			self._transformed_flags = transformed_flags
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
	get category of IP
	'''
	@property
	def iprep_category(self) :
		try:
			return self._iprep_category
		except Exception as e :
			raise e
	'''
	set category of IP
	'''
	@iprep_category.setter
	def iprep_category(self,iprep_category):
		try :
			if not isinstance(iprep_category,int):
				raise TypeError("iprep_category must be set to int value")
			self._iprep_category = iprep_category
		except Exception as e :
			raise e


	'''
	get severity.
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e
	'''
	set severity.
	'''
	@severity.setter
	def severity(self,severity):
		try :
			if not isinstance(severity,int):
				raise TypeError("severity must be set to int value")
			self._severity = severity
		except Exception as e :
			raise e


	'''
	get AppFW AAA User Email Id
	'''
	@property
	def appfw_aaa_user_email(self) :
		try:
			return self._appfw_aaa_user_email
		except Exception as e :
			raise e
	'''
	set AppFW AAA User Email Id
	'''
	@appfw_aaa_user_email.setter
	def appfw_aaa_user_email(self,appfw_aaa_user_email):
		try :
			if not isinstance(appfw_aaa_user_email,str):
				raise TypeError("appfw_aaa_user_email must be set to str value")
			self._appfw_aaa_user_email = appfw_aaa_user_email
		except Exception as e :
			raise e


	'''
	get Backend AppName
	'''
	@property
	def backend_appname(self) :
		try:
			return self._backend_appname
		except Exception as e :
			raise e
	'''
	set Backend AppName
	'''
	@backend_appname.setter
	def backend_appname(self,backend_appname):
		try :
			if not isinstance(backend_appname,str):
				raise TypeError("backend_appname must be set to str value")
			self._backend_appname = backend_appname
		except Exception as e :
			raise e


	'''
	get Total attacks to this APP in given sampled timeframe.
	'''
	@property
	def total_attacks(self) :
		try:
			return self._total_attacks
		except Exception as e :
			raise e
	'''
	set Total attacks to this APP in given sampled timeframe.
	'''
	@total_attacks.setter
	def total_attacks(self,total_attacks):
		try :
			if not isinstance(total_attacks,long):
				raise TypeError("total_attacks must be set to long value")
			self._total_attacks = total_attacks
		except Exception as e :
			raise e


	'''
	get TCP counter values .
	'''
	@property
	def counter_value(self) :
		try:
			return self._counter_value
		except Exception as e :
			raise e
	'''
	set TCP counter values .
	'''
	@counter_value.setter
	def counter_value(self,counter_value):
		try :
			if not isinstance(counter_value,long):
				raise TypeError("counter_value must be set to long value")
			self._counter_value = counter_value
		except Exception as e :
			raise e


	'''
	get violation location.
	'''
	@property
	def violation_location(self) :
		try:
			return self._violation_location
		except Exception as e :
			raise e
	'''
	set violation location.
	'''
	@violation_location.setter
	def violation_location(self,violation_location):
		try :
			if not isinstance(violation_location,int):
				raise TypeError("violation_location must be set to int value")
			self._violation_location = violation_location
		except Exception as e :
			raise e


	'''
	get signature_category
	'''
	@property
	def signature_category(self) :
		try:
			return self._signature_category
		except Exception as e :
			raise e
	'''
	set signature_category
	'''
	@signature_category.setter
	def signature_category(self,signature_category):
		try :
			if not isinstance(signature_category,str):
				raise TypeError("signature_category must be set to str value")
			self._signature_category = signature_category
		except Exception as e :
			raise e


	'''
	get Server Source IP Address
	'''
	@property
	def source_ip_address(self) :
		try:
			return self._source_ip_address
		except Exception as e :
			raise e
	'''
	set Server Source IP Address
	'''
	@source_ip_address.setter
	def source_ip_address(self,source_ip_address):
		try :
			if not isinstance(source_ip_address,long):
				raise TypeError("source_ip_address must be set to long value")
			self._source_ip_address = source_ip_address
		except Exception as e :
			raise e


	'''
	get Violation value.
	'''
	@property
	def violation_value(self) :
		try:
			return self._violation_value
		except Exception as e :
			raise e
	'''
	set Violation value.
	'''
	@violation_value.setter
	def violation_value(self,violation_value):
		try :
			if not isinstance(violation_value,str):
				raise TypeError("violation_value must be set to str value")
			self._violation_value = violation_value
		except Exception as e :
			raise e


	'''
	get session_id
	'''
	@property
	def session_id(self) :
		try:
			return self._session_id
		except Exception as e :
			raise e
	'''
	set session_id
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
	get Reputation Score of IP
	'''
	@property
	def iprep_score(self) :
		try:
			return self._iprep_score
		except Exception as e :
			raise e
	'''
	set Reputation Score of IP
	'''
	@iprep_score.setter
	def iprep_score(self,iprep_score):
		try :
			if not isinstance(iprep_score,int):
				raise TypeError("iprep_score must be set to int value")
			self._iprep_score = iprep_score
		except Exception as e :
			raise e

	'''
	Af Report for Threat Exporter data..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_threat_exporter_data_l2_obj=af_threat_exporter_data_l2()
				response = af_threat_exporter_data_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_threat_exporter_data_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_threat_exporter_data_l2_obj = af_threat_exporter_data_l2()
			option_ = options()
			option_._filter=filter_
			return af_threat_exporter_data_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_threat_exporter_data_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_threat_exporter_data_l2_obj = af_threat_exporter_data_l2()
			option_ = options()
			option_._count=True
			response = af_threat_exporter_data_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_threat_exporter_data_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_threat_exporter_data_l2_obj = af_threat_exporter_data_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_threat_exporter_data_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_threat_exporter_data_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_threat_exporter_data_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_threat_exporter_data_l2_responses, response, "af_threat_exporter_data_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_threat_exporter_data_l2_response_array
				i=0
				error = [af_threat_exporter_data_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_threat_exporter_data_l2_response_array
			i=0
			af_threat_exporter_data_l2_objs = [af_threat_exporter_data_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_threat_exporter_data_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_threat_exporter_data_l2_response,self.__class__.__name__,props)
					af_threat_exporter_data_l2_objs[i] = result.af_threat_exporter_data_l2
					i=i+1
			return af_threat_exporter_data_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_threat_exporter_data_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_threat_exporter_data_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_threat_exporter_data_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_threat_exporter_data_l2= [ af_threat_exporter_data_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_threat_exporter_data_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_threat_exporter_data_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_threat_exporter_data_l2_response_array = [ af_threat_exporter_data_l2() for _ in range(length)]
