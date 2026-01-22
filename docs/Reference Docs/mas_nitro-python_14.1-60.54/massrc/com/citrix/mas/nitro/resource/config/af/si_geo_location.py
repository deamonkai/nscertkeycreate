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
Configuration for AF Geo Threat Data Report table resource
'''

class si_geo_location(af_generic_api):
	_latitude= ""
	_id= ""
	_name= ""
	_city= ""
	_violation_type= ""
	_http_req_url= ""
	_not_blocked_flags= ""
	_attack_category= ""
	_violation_threat_index= ""
	_violation_name= ""
	_country_code= ""
	_severity= ""
	_longitude= ""
	_transformed_flags= ""
	_country= ""
	_signature_category= ""
	_si_device_ip_address= ""
	_violation_location= ""
	_total_attacks= ""
	_threat_index= ""
	_violation_value= ""
	___count= ""
	_source_ip_address= ""
	_violation_action= ""
	_attack_time= ""
	_si_app_unit_name= ""
	_http_method= ""
	_block_flags= ""
	_severity_type= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "si_geo_location"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(si_geo_location,self).get_object_id()
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
			return "si_geo_locations"
		except Exception as e :
			raise e


	'''
	latitude
	'''
	@property
	def latitude(self):
		try:
			return self._latitude
		except Exception as e :
			raise e
	'''
	latitude
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
	Id is Security check violation name
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is Security check violation name
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
	AppName
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	AppName
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
	City Name
	'''
	@property
	def city(self):
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	City Name
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
	Violation Type
	'''
	@property
	def violation_type(self):
		try:
			return self._violation_type
		except Exception as e :
			raise e
	'''
	Violation Type
	'''
	@violation_type.setter
	def violation_type(self,violation_type):
		try :
			if not isinstance(violation_type,str):
				raise TypeError("violation_type must be set to str value")
			self._violation_type = violation_type
		except Exception as e :
			raise e

	'''
	HTTP Request URL
	'''
	@property
	def http_req_url(self):
		try:
			return self._http_req_url
		except Exception as e :
			raise e
	'''
	HTTP Request URL
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
	Not Block Flags
	'''
	@property
	def not_blocked_flags(self):
		try:
			return self._not_blocked_flags
		except Exception as e :
			raise e
	'''
	Not Block Flags
	'''
	@not_blocked_flags.setter
	def not_blocked_flags(self,not_blocked_flags):
		try :
			if not isinstance(not_blocked_flags,float):
				raise TypeError("not_blocked_flags must be set to float value")
			self._not_blocked_flags = not_blocked_flags
		except Exception as e :
			raise e

	'''
	Attack Category
	'''
	@property
	def attack_category(self):
		try:
			return self._attack_category
		except Exception as e :
			raise e
	'''
	Attack Category
	'''
	@attack_category.setter
	def attack_category(self,attack_category):
		try :
			if not isinstance(attack_category,str):
				raise TypeError("attack_category must be set to str value")
			self._attack_category = attack_category
		except Exception as e :
			raise e

	'''
	Violation Threat Index
	'''
	@property
	def violation_threat_index(self):
		try:
			return self._violation_threat_index
		except Exception as e :
			raise e
	'''
	Violation Threat Index
	'''
	@violation_threat_index.setter
	def violation_threat_index(self,violation_threat_index):
		try :
			if not isinstance(violation_threat_index,str):
				raise TypeError("violation_threat_index must be set to str value")
			self._violation_threat_index = violation_threat_index
		except Exception as e :
			raise e

	'''
	Violation  Name
	'''
	@property
	def violation_name(self):
		try:
			return self._violation_name
		except Exception as e :
			raise e
	'''
	Violation  Name
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
	Country Code
	'''
	@property
	def country_code(self):
		try:
			return self._country_code
		except Exception as e :
			raise e
	'''
	Country Code
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
	severity
	'''
	@property
	def severity(self):
		try:
			return self._severity
		except Exception as e :
			raise e
	'''
	severity
	'''
	@severity.setter
	def severity(self,severity):
		try :
			if not isinstance(severity,str):
				raise TypeError("severity must be set to str value")
			self._severity = severity
		except Exception as e :
			raise e

	'''
	longitude
	'''
	@property
	def longitude(self):
		try:
			return self._longitude
		except Exception as e :
			raise e
	'''
	longitude
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
	Transformed Flags.
	'''
	@property
	def transformed_flags(self):
		try:
			return self._transformed_flags
		except Exception as e :
			raise e
	'''
	Transformed Flags.
	'''
	@transformed_flags.setter
	def transformed_flags(self,transformed_flags):
		try :
			if not isinstance(transformed_flags,float):
				raise TypeError("transformed_flags must be set to float value")
			self._transformed_flags = transformed_flags
		except Exception as e :
			raise e

	'''
	country
	'''
	@property
	def country(self):
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	country
	'''
	@country.setter
	def country(self,country):
		try :
			if not isinstance(country,str):
				raise TypeError("country must be set to str value")
			self._country = country
		except Exception as e :
			raise e

	'''
	Signature Category
	'''
	@property
	def signature_category(self):
		try:
			return self._signature_category
		except Exception as e :
			raise e
	'''
	Signature Category
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
	NetScaler IP Address.
	'''
	@property
	def si_device_ip_address(self):
		try:
			return self._si_device_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address.
	'''
	@si_device_ip_address.setter
	def si_device_ip_address(self,si_device_ip_address):
		try :
			if not isinstance(si_device_ip_address,str):
				raise TypeError("si_device_ip_address must be set to str value")
			self._si_device_ip_address = si_device_ip_address
		except Exception as e :
			raise e

	'''
	Violation Location
	'''
	@property
	def violation_location(self):
		try:
			return self._violation_location
		except Exception as e :
			raise e
	'''
	Violation Location
	'''
	@violation_location.setter
	def violation_location(self,violation_location):
		try :
			if not isinstance(violation_location,str):
				raise TypeError("violation_location must be set to str value")
			self._violation_location = violation_location
		except Exception as e :
			raise e

	'''
	total attacks.
	'''
	@property
	def total_attacks(self):
		try:
			return self._total_attacks
		except Exception as e :
			raise e
	'''
	total attacks.
	'''
	@total_attacks.setter
	def total_attacks(self,total_attacks):
		try :
			if not isinstance(total_attacks,float):
				raise TypeError("total_attacks must be set to float value")
			self._total_attacks = total_attacks
		except Exception as e :
			raise e

	'''
	Threat Index
	'''
	@property
	def threat_index(self):
		try:
			return self._threat_index
		except Exception as e :
			raise e
	'''
	Threat Index
	'''
	@threat_index.setter
	def threat_index(self,threat_index):
		try :
			if not isinstance(threat_index,float):
				raise TypeError("threat_index must be set to float value")
			self._threat_index = threat_index
		except Exception as e :
			raise e

	'''
	Violation Value
	'''
	@property
	def violation_value(self):
		try:
			return self._violation_value
		except Exception as e :
			raise e
	'''
	Violation Value
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
	Number of records
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	Number of records
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
	Source IP Address
	'''
	@property
	def source_ip_address(self):
		try:
			return self._source_ip_address
		except Exception as e :
			raise e
	'''
	Source IP Address
	'''
	@source_ip_address.setter
	def source_ip_address(self,source_ip_address):
		try :
			if not isinstance(source_ip_address,str):
				raise TypeError("source_ip_address must be set to str value")
			self._source_ip_address = source_ip_address
		except Exception as e :
			raise e

	'''
	Violation Action
	'''
	@property
	def violation_action(self):
		try:
			return self._violation_action
		except Exception as e :
			raise e
	'''
	Violation Action
	'''
	@violation_action.setter
	def violation_action(self,violation_action):
		try :
			if not isinstance(violation_action,str):
				raise TypeError("violation_action must be set to str value")
			self._violation_action = violation_action
		except Exception as e :
			raise e

	'''
	Attack Time
	'''
	@property
	def attack_time(self):
		try:
			return self._attack_time
		except Exception as e :
			raise e
	'''
	Attack Time
	'''
	@attack_time.setter
	def attack_time(self,attack_time):
		try :
			if not isinstance(attack_time,str):
				raise TypeError("attack_time must be set to str value")
			self._attack_time = attack_time
		except Exception as e :
			raise e

	'''
	AppName
	'''
	@property
	def si_app_unit_name(self):
		try:
			return self._si_app_unit_name
		except Exception as e :
			raise e
	'''
	AppName
	'''
	@si_app_unit_name.setter
	def si_app_unit_name(self,si_app_unit_name):
		try :
			if not isinstance(si_app_unit_name,str):
				raise TypeError("si_app_unit_name must be set to str value")
			self._si_app_unit_name = si_app_unit_name
		except Exception as e :
			raise e

	'''
	http_method
	'''
	@property
	def http_method(self):
		try:
			return self._http_method
		except Exception as e :
			raise e
	'''
	http_method
	'''
	@http_method.setter
	def http_method(self,http_method):
		try :
			if not isinstance(http_method,str):
				raise TypeError("http_method must be set to str value")
			self._http_method = http_method
		except Exception as e :
			raise e

	'''
	Block Flags.
	'''
	@property
	def block_flags(self):
		try:
			return self._block_flags
		except Exception as e :
			raise e
	'''
	Block Flags.
	'''
	@block_flags.setter
	def block_flags(self,block_flags):
		try :
			if not isinstance(block_flags,float):
				raise TypeError("block_flags must be set to float value")
			self._block_flags = block_flags
		except Exception as e :
			raise e

	'''
	Severity Type
	'''
	@property
	def severity_type(self):
		try:
			return self._severity_type
		except Exception as e :
			raise e
	'''
	Severity Type
	'''
	@severity_type.setter
	def severity_type(self,severity_type):
		try :
			if not isinstance(severity_type,str):
				raise TypeError("severity_type must be set to str value")
			self._severity_type = severity_type
		except Exception as e :
			raise e

	'''
	Af Report for Security Insight Device..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				si_geo_location_obj=si_geo_location()
				response = si_geo_location_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of si_geo_location resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			si_geo_location_obj = si_geo_location()
			option_ = options()
			option_._filter=filter_
			return si_geo_location_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the si_geo_location resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			si_geo_location_obj = si_geo_location()
			option_ = options()
			option_._count=True
			response = si_geo_location_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of si_geo_location resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			si_geo_location_obj = si_geo_location()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = si_geo_location_obj.getfiltered(service, option_)
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
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - cr_enabled
	'''
	@classmethod
	def set_queryparam_cr_enabled(cls, option, value):
		option.add_queryparam("cr_enabled",value)

	'''
	Set Query Parameter - type
	'''
	@classmethod
	def set_queryparam_type(cls, option, value):
		option.add_queryparam("type",value)

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
			result=service.payload_formatter.string_to_resource(si_geo_location_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.si_geo_location
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_geo_location_responses, response, "si_geo_location_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.si_geo_location_response_array
				i=0
				error = [si_geo_location() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.si_geo_location_response_array
			i=0
			si_geo_location_objs = [si_geo_location() for _ in range(len(response))]
			for obj in response :
				for props in obj._si_geo_location:
					result = service.payload_formatter.string_to_bulk_resource(si_geo_location_response,self.__class__.__name__,props)
					si_geo_location_objs[i] = result.si_geo_location
					i=i+1
			return si_geo_location_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(si_geo_location,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class si_geo_location_response(base_response):
	def __init__(self,length=1) :
		self.si_geo_location= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.si_geo_location= [ si_geo_location() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class si_geo_location_responses(base_response):
	def __init__(self,length=1) :
		self.si_geo_location_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.si_geo_location_response_array = [ si_geo_location() for _ in range(length)]
