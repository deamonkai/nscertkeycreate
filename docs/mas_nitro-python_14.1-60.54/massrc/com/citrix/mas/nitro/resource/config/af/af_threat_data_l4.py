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
Configuration for AF Threat exporter  data table for Level 4 resource
'''

class af_threat_data_l4(base_resource):
	_latitude= ""
	_exporter_id= ""
	_app_threat_index= ""
	_medium_threat= ""
	_city= ""
	_appname= ""
	_high_threat= ""
	_violation_type= ""
	_not_blocked_flags= ""
	_ip_address= ""
	_attack_category= ""
	_violation_category= ""
	_ns_city= ""
	_country_code= ""
	_transformed_flags= ""
	_longitude= ""
	_ctnsappname= ""
	_severity= ""
	_signature_category= ""
	_counter_value= ""
	_ns_latitude= ""
	_total_attacks= ""
	_source_ip_address= ""
	_region_code= ""
	_violation_action= ""
	_ns_longitude= ""
	_low_threat= ""
	_block_flags= ""
	_rpt_sample_time= ""
	_severity_type= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_threat_data_l4"
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
			return "af_threat_data_l4s"
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
	get threat index.
	'''
	@property
	def app_threat_index(self) :
		try:
			return self._app_threat_index
		except Exception as e :
			raise e
	'''
	set threat index.
	'''
	@app_threat_index.setter
	def app_threat_index(self,app_threat_index):
		try :
			if not isinstance(app_threat_index,long):
				raise TypeError("app_threat_index must be set to long value")
			self._app_threat_index = app_threat_index
		except Exception as e :
			raise e


	'''
	get medium_threat count.
	'''
	@property
	def medium_threat(self) :
		try:
			return self._medium_threat
		except Exception as e :
			raise e
	'''
	set medium_threat count.
	'''
	@medium_threat.setter
	def medium_threat(self,medium_threat):
		try :
			if not isinstance(medium_threat,long):
				raise TypeError("medium_threat must be set to long value")
			self._medium_threat = medium_threat
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
	get high_threats count.
	'''
	@property
	def high_threat(self) :
		try:
			return self._high_threat
		except Exception as e :
			raise e
	'''
	set high_threats count.
	'''
	@high_threat.setter
	def high_threat(self,high_threat):
		try :
			if not isinstance(high_threat,long):
				raise TypeError("high_threat must be set to long value")
			self._high_threat = high_threat
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
			if not isinstance(violation_type,long):
				raise TypeError("violation_type must be set to long value")
			self._violation_type = violation_type
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
			if not isinstance(not_blocked_flags,long):
				raise TypeError("not_blocked_flags must be set to long value")
			self._not_blocked_flags = not_blocked_flags
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
	get attack_category
	'''
	@property
	def attack_category(self) :
		try:
			return self._attack_category
		except Exception as e :
			raise e
	'''
	set attack_category
	'''
	@attack_category.setter
	def attack_category(self,attack_category):
		try :
			if not isinstance(attack_category,long):
				raise TypeError("attack_category must be set to long value")
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
	get NetScaler city
	'''
	@property
	def ns_city(self) :
		try:
			return self._ns_city
		except Exception as e :
			raise e
	'''
	set NetScaler city
	'''
	@ns_city.setter
	def ns_city(self,ns_city):
		try :
			if not isinstance(ns_city,str):
				raise TypeError("ns_city must be set to str value")
			self._ns_city = ns_city
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
			if not isinstance(transformed_flags,long):
				raise TypeError("transformed_flags must be set to long value")
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
			if not isinstance(severity,long):
				raise TypeError("severity must be set to long value")
			self._severity = severity
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
	get NetScaler latitude
	'''
	@property
	def ns_latitude(self) :
		try:
			return self._ns_latitude
		except Exception as e :
			raise e
	'''
	set NetScaler latitude
	'''
	@ns_latitude.setter
	def ns_latitude(self,ns_latitude):
		try :
			if not isinstance(ns_latitude,float):
				raise TypeError("ns_latitude must be set to float value")
			self._ns_latitude = ns_latitude
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
	get violation_action blocked tranformed non_blocked.
	'''
	@property
	def violation_action(self) :
		try:
			return self._violation_action
		except Exception as e :
			raise e
	'''
	set violation_action blocked tranformed non_blocked.
	'''
	@violation_action.setter
	def violation_action(self,violation_action):
		try :
			if not isinstance(violation_action,long):
				raise TypeError("violation_action must be set to long value")
			self._violation_action = violation_action
		except Exception as e :
			raise e


	'''
	get NetScaler longitude
	'''
	@property
	def ns_longitude(self) :
		try:
			return self._ns_longitude
		except Exception as e :
			raise e
	'''
	set NetScaler longitude
	'''
	@ns_longitude.setter
	def ns_longitude(self,ns_longitude):
		try :
			if not isinstance(ns_longitude,float):
				raise TypeError("ns_longitude must be set to float value")
			self._ns_longitude = ns_longitude
		except Exception as e :
			raise e


	'''
	get low_threat. count
	'''
	@property
	def low_threat(self) :
		try:
			return self._low_threat
		except Exception as e :
			raise e
	'''
	set low_threat. count
	'''
	@low_threat.setter
	def low_threat(self,low_threat):
		try :
			if not isinstance(low_threat,long):
				raise TypeError("low_threat must be set to long value")
			self._low_threat = low_threat
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
			if not isinstance(block_flags,long):
				raise TypeError("block_flags must be set to long value")
			self._block_flags = block_flags
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
	get severity to severity_type mapped 0_critical 1_medim 2_low .
	'''
	@property
	def severity_type(self) :
		try:
			return self._severity_type
		except Exception as e :
			raise e
	'''
	set severity to severity_type mapped 0_critical 1_medim 2_low .
	'''
	@severity_type.setter
	def severity_type(self,severity_type):
		try :
			if not isinstance(severity_type,long):
				raise TypeError("severity_type must be set to long value")
			self._severity_type = severity_type
		except Exception as e :
			raise e

	'''
	Af Report for Threat Data..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_threat_data_l4_obj=af_threat_data_l4()
				response = af_threat_data_l4_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_threat_data_l4 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_threat_data_l4_obj = af_threat_data_l4()
			option_ = options()
			option_._filter=filter_
			return af_threat_data_l4_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_threat_data_l4 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_threat_data_l4_obj = af_threat_data_l4()
			option_ = options()
			option_._count=True
			response = af_threat_data_l4_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_threat_data_l4 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_threat_data_l4_obj = af_threat_data_l4()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_threat_data_l4_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_threat_data_l4_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_threat_data_l4
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_threat_data_l4_responses, response, "af_threat_data_l4_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_threat_data_l4_response_array
				i=0
				error = [af_threat_data_l4() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_threat_data_l4_response_array
			i=0
			af_threat_data_l4_objs = [af_threat_data_l4() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_threat_data_l4:
					result = service.payload_formatter.string_to_bulk_resource(af_threat_data_l4_response,self.__class__.__name__,props)
					af_threat_data_l4_objs[i] = result.af_threat_data_l4
					i=i+1
			return af_threat_data_l4_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_threat_data_l4,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_threat_data_l4_response(base_response):
	def __init__(self,length=1) :
		self.af_threat_data_l4= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_threat_data_l4= [ af_threat_data_l4() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_threat_data_l4_responses(base_response):
	def __init__(self,length=1) :
		self.af_threat_data_l4_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_threat_data_l4_response_array = [ af_threat_data_l4() for _ in range(length)]
