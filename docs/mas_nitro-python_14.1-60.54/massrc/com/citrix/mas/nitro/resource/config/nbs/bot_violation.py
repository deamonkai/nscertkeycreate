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


import os
import logging
from logging import handlers, Formatter
from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for Bot Violation resource
'''

class bot_violation(base_resource):
	_bot_type= ""
	_bot_detection_mechanism_desc= ""
	_bot_category= ""
	_signature_id= ""
	_domain_name= ""
	_city= ""
	_bot_detection_mechanism= ""
	_ip_address= ""
	_latitude= ""
	_action_type= ""
	_appname= ""
	_bot_severity_desc= ""
	_bot_developer= ""
	_transaction_id= ""
	_bot_true_client_ip= ""
	_backend_vserver= ""
	_rpt_sample_time= ""
	_bot_signature_category= ""
	_attack_time= ""
	_ctnsappname= ""
	_http_req_url= ""
	_bot_severity= ""
	_region_code= ""
	_source_ip_address= ""
	_bot_category_desc= ""
	_longitude= ""
	_action_type_desc= ""
	_total_attacks= ""
	_country_code= ""
	_profile_name= ""
	_bot_log_message= ""
	_backend_appname= ""
	_bot_type_desc= ""
	_session_id= ""
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/macro/v1/security/bot_violation"
		except Exception as e :
			raise e

	'''
	get the resource id
	'''
	def get_resource_id(self) :
		try:
			if hasattr(self, 'id'):
				return self.id 
			else:
				return None 
		except Exception as e :
			raise e

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "bot_violation"
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
			return "bot_violations"
		except Exception as e :
			raise e



	'''
	get bot_type
	'''
	@property
	def bot_type(self) :
		try:
			return self._bot_type
		except Exception as e :
			raise e
	'''
	set bot_type
	'''
	@bot_type.setter
	def bot_type(self,bot_type):
		try :
			if not isinstance(bot_type,int):
				raise TypeError("bot_type must be set to int value")
			self._bot_type = bot_type
		except Exception as e :
			raise e


	'''
	get Bot Detection Mechanism Desc
	'''
	@property
	def bot_detection_mechanism_desc(self) :
		try:
			return self._bot_detection_mechanism_desc
		except Exception as e :
			raise e
	'''
	set Bot Detection Mechanism Desc
	'''
	@bot_detection_mechanism_desc.setter
	def bot_detection_mechanism_desc(self,bot_detection_mechanism_desc):
		try :
			if not isinstance(bot_detection_mechanism_desc,str):
				raise TypeError("bot_detection_mechanism_desc must be set to str value")
			self._bot_detection_mechanism_desc = bot_detection_mechanism_desc
		except Exception as e :
			raise e


	'''
	get Bot Category.
	'''
	@property
	def bot_category(self) :
		try:
			return self._bot_category
		except Exception as e :
			raise e
	'''
	set Bot Category.
	'''
	@bot_category.setter
	def bot_category(self,bot_category):
		try :
			if not isinstance(bot_category,long):
				raise TypeError("bot_category must be set to long value")
			self._bot_category = bot_category
		except Exception as e :
			raise e


	'''
	get Signature Id
	'''
	@property
	def signature_id(self) :
		try:
			return self._signature_id
		except Exception as e :
			raise e
	'''
	set Signature Id
	'''
	@signature_id.setter
	def signature_id(self,signature_id):
		try :
			if not isinstance(signature_id,long):
				raise TypeError("signature_id must be set to long value")
			self._signature_id = signature_id
		except Exception as e :
			raise e


	'''
	get Domain Name
	'''
	@property
	def domain_name(self) :
		try:
			return self._domain_name
		except Exception as e :
			raise e
	'''
	set Domain Name
	'''
	@domain_name.setter
	def domain_name(self,domain_name):
		try :
			if not isinstance(domain_name,str):
				raise TypeError("domain_name must be set to str value")
			self._domain_name = domain_name
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
	get Bot Detection Mechanism.
	'''
	@property
	def bot_detection_mechanism(self) :
		try:
			return self._bot_detection_mechanism
		except Exception as e :
			raise e
	'''
	set Bot Detection Mechanism.
	'''
	@bot_detection_mechanism.setter
	def bot_detection_mechanism(self,bot_detection_mechanism):
		try :
			if not isinstance(bot_detection_mechanism,int):
				raise TypeError("bot_detection_mechanism must be set to int value")
			self._bot_detection_mechanism = bot_detection_mechanism
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
	get Bot Type.
	'''
	@property
	def action_type(self) :
		try:
			return self._action_type
		except Exception as e :
			raise e
	'''
	set Bot Type.
	'''
	@action_type.setter
	def action_type(self,action_type):
		try :
			if not isinstance(action_type,long):
				raise TypeError("action_type must be set to long value")
			self._action_type = action_type
		except Exception as e :
			raise e


	'''
	get App Name
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set App Name
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
	get Bot Severity Desc
	'''
	@property
	def bot_severity_desc(self) :
		try:
			return self._bot_severity_desc
		except Exception as e :
			raise e
	'''
	set Bot Severity Desc
	'''
	@bot_severity_desc.setter
	def bot_severity_desc(self,bot_severity_desc):
		try :
			if not isinstance(bot_severity_desc,str):
				raise TypeError("bot_severity_desc must be set to str value")
			self._bot_severity_desc = bot_severity_desc
		except Exception as e :
			raise e


	'''
	get Bot Developer
	'''
	@property
	def bot_developer(self) :
		try:
			return self._bot_developer
		except Exception as e :
			raise e
	'''
	set Bot Developer
	'''
	@bot_developer.setter
	def bot_developer(self,bot_developer):
		try :
			if not isinstance(bot_developer,str):
				raise TypeError("bot_developer must be set to str value")
			self._bot_developer = bot_developer
		except Exception as e :
			raise e


	'''
	get Transaction ID
	'''
	@property
	def transaction_id(self) :
		try:
			return self._transaction_id
		except Exception as e :
			raise e
	'''
	set Transaction ID
	'''
	@transaction_id.setter
	def transaction_id(self,transaction_id):
		try :
			if not isinstance(transaction_id,long):
				raise TypeError("transaction_id must be set to long value")
			self._transaction_id = transaction_id
		except Exception as e :
			raise e


	'''
	get True Client IP
	'''
	@property
	def bot_true_client_ip(self) :
		try:
			return self._bot_true_client_ip
		except Exception as e :
			raise e
	'''
	set True Client IP
	'''
	@bot_true_client_ip.setter
	def bot_true_client_ip(self,bot_true_client_ip):
		try :
			if not isinstance(bot_true_client_ip,int):
				raise TypeError("bot_true_client_ip must be set to int value")
			self._bot_true_client_ip = bot_true_client_ip
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
	get Bot Signature Category
	'''
	@property
	def bot_signature_category(self) :
		try:
			return self._bot_signature_category
		except Exception as e :
			raise e
	'''
	set Bot Signature Category
	'''
	@bot_signature_category.setter
	def bot_signature_category(self,bot_signature_category):
		try :
			if not isinstance(bot_signature_category,str):
				raise TypeError("bot_signature_category must be set to str value")
			self._bot_signature_category = bot_signature_category
		except Exception as e :
			raise e


	'''
	get Attack time.
	'''
	@property
	def attack_time(self) :
		try:
			return self._attack_time
		except Exception as e :
			raise e
	'''
	set Attack time.
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
	get bot_severity.
	'''
	@property
	def bot_severity(self) :
		try:
			return self._bot_severity
		except Exception as e :
			raise e
	'''
	set bot_severity.
	'''
	@bot_severity.setter
	def bot_severity(self,bot_severity):
		try :
			if not isinstance(bot_severity,int):
				raise TypeError("bot_severity must be set to int value")
			self._bot_severity = bot_severity
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
	get Bot Category Desc.
	'''
	@property
	def bot_category_desc(self) :
		try:
			return self._bot_category_desc
		except Exception as e :
			raise e
	'''
	set Bot Category Desc.
	'''
	@bot_category_desc.setter
	def bot_category_desc(self,bot_category_desc):
		try :
			if not isinstance(bot_category_desc,str):
				raise TypeError("bot_category_desc must be set to str value")
			self._bot_category_desc = bot_category_desc
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
	get Action Type Description
	'''
	@property
	def action_type_desc(self) :
		try:
			return self._action_type_desc
		except Exception as e :
			raise e
	'''
	set Action Type Description
	'''
	@action_type_desc.setter
	def action_type_desc(self,action_type_desc):
		try :
			if not isinstance(action_type_desc,str):
				raise TypeError("action_type_desc must be set to str value")
			self._action_type_desc = action_type_desc
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
	get Bot Log Message
	'''
	@property
	def bot_log_message(self) :
		try:
			return self._bot_log_message
		except Exception as e :
			raise e
	'''
	set Bot Log Message
	'''
	@bot_log_message.setter
	def bot_log_message(self,bot_log_message):
		try :
			if not isinstance(bot_log_message,str):
				raise TypeError("bot_log_message must be set to str value")
			self._bot_log_message = bot_log_message
		except Exception as e :
			raise e


	'''
	get Backend App Name
	'''
	@property
	def backend_appname(self) :
		try:
			return self._backend_appname
		except Exception as e :
			raise e
	'''
	set Backend App Name
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
	get Bot Type Description
	'''
	@property
	def bot_type_desc(self) :
		try:
			return self._bot_type_desc
		except Exception as e :
			raise e
	'''
	set Bot Type Description
	'''
	@bot_type_desc.setter
	def bot_type_desc(self,bot_type_desc):
		try :
			if not isinstance(bot_type_desc,str):
				raise TypeError("bot_type_desc must be set to str value")
			self._bot_type_desc = bot_type_desc
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
	Get the list of bot violations..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			response=""
			if not resource :
				bot_violation_obj=bot_violation()
				response = bot_violation_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of bot_violation resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			bot_violation_obj = bot_violation()
			option_ = options()
			option_._filter=filter_
			return bot_violation_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the bot_violation resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			bot_violation_obj = bot_violation()
			option_ = options()
			option_._count=True
			response = bot_violation_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of bot_violation resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			bot_violation_obj = bot_violation()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = bot_violation_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(bot_violation_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.bot_violation
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(bot_violation_responses, response, "bot_violation_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.bot_violation_response_array
				i=0
				error = [bot_violation() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.bot_violation_response_array
			i=0
			bot_violation_objs = [bot_violation() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_bot_violation'):
					for props in obj._bot_violation:
						result = service.payload_formatter.string_to_bulk_resource(bot_violation_response,self.__class__.__name__,props)
						bot_violation_objs[i] = result.bot_violation
						i=i+1
			return bot_violation_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(bot_violation,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class bot_violation_response(base_response):
	def __init__(self,length=1) :
		self.bot_violation= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.bot_violation= [ bot_violation() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class bot_violation_responses(base_response):
	def __init__(self,length=1) :
		self.bot_violation_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.bot_violation_response_array = [ bot_violation() for _ in range(length)]
