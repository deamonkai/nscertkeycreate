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
Configuration for Security App Dashboard Report table resource
'''

class security_app_dashboard_details(base_resource):
	_ip_address= ""
	_violation_category= ""
	_attack_category= ""
	_violation_type= ""
	_app_safety_index_prev= ""
	_source_ip_address_prev= ""
	_app_safety_index= ""
	_ns_city= ""
	_device_ip_address= ""
	_app_threat_index= ""
	_vserver_name= ""
	_name= ""
	_exporter_id= ""
	_description= ""
	_latitude= ""
	_appname= ""
	_app_threat_index_prev= ""
	_city= ""
	_app_category= ""
	_ns_longitude= ""
	_block_flags_prev= ""
	_block_flags= ""
	_severity_type= ""
	_rpt_sample_time= ""
	_total_attacks_prev= ""
	_longitude= ""
	_country= ""
	_ctnsappname= ""
	_safety_index= ""
	_country_code= ""
	_threat_index= ""
	___count= ""
	_source_ip_address= ""
	_total_attacks= ""
	_ns_latitude= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "security_app_dashboard_details"
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
			return "security_app_dashboard_detailss"
		except Exception as e :
			raise e



	'''
	get NetScaler IP Address.
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address.
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
	get violation Category.
	'''
	@property
	def violation_category(self) :
		try:
			return self._violation_category
		except Exception as e :
			raise e
	'''
	set violation Category.
	'''
	@violation_category.setter
	def violation_category(self,violation_category):
		try :
			if not isinstance(violation_category,str):
				raise TypeError("violation_category must be set to str value")
			self._violation_category = violation_category
		except Exception as e :
			raise e


	'''
	get Attack Category.
	'''
	@property
	def attack_category(self) :
		try:
			return self._attack_category
		except Exception as e :
			raise e
	'''
	set Attack Category.
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
	get Violation Type
	'''
	@property
	def violation_type(self) :
		try:
			return self._violation_type
		except Exception as e :
			raise e
	'''
	set Violation Type
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
	get App safety index prev
	'''
	@property
	def app_safety_index_prev(self) :
		try:
			return self._app_safety_index_prev
		except Exception as e :
			raise e
	'''
	set App safety index prev
	'''
	@app_safety_index_prev.setter
	def app_safety_index_prev(self,app_safety_index_prev):
		try :
			if not isinstance(app_safety_index_prev,float):
				raise TypeError("app_safety_index_prev must be set to float value")
			self._app_safety_index_prev = app_safety_index_prev
		except Exception as e :
			raise e


	'''
	get Client ip address
	'''
	@property
	def source_ip_address_prev(self) :
		try:
			return self._source_ip_address_prev
		except Exception as e :
			raise e
	'''
	set Client ip address
	'''
	@source_ip_address_prev.setter
	def source_ip_address_prev(self,source_ip_address_prev):
		try :
			if not isinstance(source_ip_address_prev,str):
				raise TypeError("source_ip_address_prev must be set to str value")
			self._source_ip_address_prev = source_ip_address_prev
		except Exception as e :
			raise e


	'''
	get App Safety Index
	'''
	@property
	def app_safety_index(self) :
		try:
			return self._app_safety_index
		except Exception as e :
			raise e
	'''
	set App Safety Index
	'''
	@app_safety_index.setter
	def app_safety_index(self,app_safety_index):
		try :
			if not isinstance(app_safety_index,float):
				raise TypeError("app_safety_index must be set to float value")
			self._app_safety_index = app_safety_index
		except Exception as e :
			raise e


	'''
	get NetScaler Location city
	'''
	@property
	def ns_city(self) :
		try:
			return self._ns_city
		except Exception as e :
			raise e
	'''
	set NetScaler Location city
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
	get Device IP Address
	'''
	@property
	def device_ip_address(self) :
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	set Device IP Address
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
	get Application threat Index
	'''
	@property
	def app_threat_index(self) :
		try:
			return self._app_threat_index
		except Exception as e :
			raise e
	'''
	set Application threat Index
	'''
	@app_threat_index.setter
	def app_threat_index(self,app_threat_index):
		try :
			if not isinstance(app_threat_index,float):
				raise TypeError("app_threat_index must be set to float value")
			self._app_threat_index = app_threat_index
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def vserver_name(self) :
		try:
			return self._vserver_name
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@vserver_name.setter
	def vserver_name(self,vserver_name):
		try :
			if not isinstance(vserver_name,str):
				raise TypeError("vserver_name must be set to str value")
			self._vserver_name = vserver_name
		except Exception as e :
			raise e


	'''
	get Name of NetScaler Instance
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of NetScaler Instance
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
			if not isinstance(exporter_id,str):
				raise TypeError("exporter_id must be set to str value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e


	'''
	get Violation Type Description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Violation Type Description
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
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
	get App threat index previous
	'''
	@property
	def app_threat_index_prev(self) :
		try:
			return self._app_threat_index_prev
		except Exception as e :
			raise e
	'''
	set App threat index previous
	'''
	@app_threat_index_prev.setter
	def app_threat_index_prev(self,app_threat_index_prev):
		try :
			if not isinstance(app_threat_index_prev,float):
				raise TypeError("app_threat_index_prev must be set to float value")
			self._app_threat_index_prev = app_threat_index_prev
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
	get App Category
	'''
	@property
	def app_category(self) :
		try:
			return self._app_category
		except Exception as e :
			raise e
	'''
	set App Category
	'''
	@app_category.setter
	def app_category(self,app_category):
		try :
			if not isinstance(app_category,str):
				raise TypeError("app_category must be set to str value")
			self._app_category = app_category
		except Exception as e :
			raise e


	'''
	get NetScaler Location longitude
	'''
	@property
	def ns_longitude(self) :
		try:
			return self._ns_longitude
		except Exception as e :
			raise e
	'''
	set NetScaler Location longitude
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
	get Block flag count
	'''
	@property
	def block_flags_prev(self) :
		try:
			return self._block_flags_prev
		except Exception as e :
			raise e
	'''
	set Block flag count
	'''
	@block_flags_prev.setter
	def block_flags_prev(self,block_flags_prev):
		try :
			if not isinstance(block_flags_prev,float):
				raise TypeError("block_flags_prev must be set to float value")
			self._block_flags_prev = block_flags_prev
		except Exception as e :
			raise e


	'''
	get Block flag count
	'''
	@property
	def block_flags(self) :
		try:
			return self._block_flags
		except Exception as e :
			raise e
	'''
	set Block flag count
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
	get severity_type
	'''
	@property
	def severity_type(self) :
		try:
			return self._severity_type
		except Exception as e :
			raise e
	'''
	set severity_type
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
			if not isinstance(rpt_sample_time,float):
				raise TypeError("rpt_sample_time must be set to float value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e


	'''
	get Count of attacks in given sampled timeframe.
	'''
	@property
	def total_attacks_prev(self) :
		try:
			return self._total_attacks_prev
		except Exception as e :
			raise e
	'''
	set Count of attacks in given sampled timeframe.
	'''
	@total_attacks_prev.setter
	def total_attacks_prev(self,total_attacks_prev):
		try :
			if not isinstance(total_attacks_prev,float):
				raise TypeError("total_attacks_prev must be set to float value")
			self._total_attacks_prev = total_attacks_prev
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
	get country
	'''
	@property
	def country(self) :
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	set country
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
	get safety index.
	'''
	@property
	def safety_index(self) :
		try:
			return self._safety_index
		except Exception as e :
			raise e
	'''
	set safety index.
	'''
	@safety_index.setter
	def safety_index(self,safety_index):
		try :
			if not isinstance(safety_index,float):
				raise TypeError("safety_index must be set to float value")
			self._safety_index = safety_index
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
	get threat_index
	'''
	@property
	def threat_index(self) :
		try:
			return self._threat_index
		except Exception as e :
			raise e
	'''
	set threat_index
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
	get count.
	'''
	@property
	def __count(self) :
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	set count.
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
	get Client ip address
	'''
	@property
	def source_ip_address(self) :
		try:
			return self._source_ip_address
		except Exception as e :
			raise e
	'''
	set Client ip address
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
	get Count of this URL in given sampled timeframe.
	'''
	@property
	def total_attacks(self) :
		try:
			return self._total_attacks
		except Exception as e :
			raise e
	'''
	set Count of this URL in given sampled timeframe.
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
	get NetScaler Location latitude
	'''
	@property
	def ns_latitude(self) :
		try:
			return self._ns_latitude
		except Exception as e :
			raise e
	'''
	set NetScaler Location latitude
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
	Af Report for Security App Dashboard.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				security_app_dashboard_details_obj=security_app_dashboard_details()
				response = security_app_dashboard_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of security_app_dashboard_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			security_app_dashboard_details_obj = security_app_dashboard_details()
			option_ = options()
			option_._filter=filter_
			return security_app_dashboard_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the security_app_dashboard_details resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			security_app_dashboard_details_obj = security_app_dashboard_details()
			option_ = options()
			option_._count=True
			response = security_app_dashboard_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of security_app_dashboard_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			security_app_dashboard_details_obj = security_app_dashboard_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = security_app_dashboard_details_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

	'''
	Set Query Parameter - group_by
	'''
	@classmethod
	def set_queryparam_group_by(cls, option, value):
		option.add_queryparam("group_by",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(security_app_dashboard_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.security_app_dashboard_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(security_app_dashboard_details_responses, response, "security_app_dashboard_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.security_app_dashboard_details_response_array
				i=0
				error = [security_app_dashboard_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.security_app_dashboard_details_response_array
			i=0
			security_app_dashboard_details_objs = [security_app_dashboard_details() for _ in range(len(response))]
			for obj in response :
				for props in obj._security_app_dashboard_details:
					result = service.payload_formatter.string_to_bulk_resource(security_app_dashboard_details_response,self.__class__.__name__,props)
					security_app_dashboard_details_objs[i] = result.security_app_dashboard_details
					i=i+1
			return security_app_dashboard_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(security_app_dashboard_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class security_app_dashboard_details_response(base_response):
	def __init__(self,length=1) :
		self.security_app_dashboard_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.security_app_dashboard_details= [ security_app_dashboard_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class security_app_dashboard_details_responses(base_response):
	def __init__(self,length=1) :
		self.security_app_dashboard_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.security_app_dashboard_details_response_array = [ security_app_dashboard_details() for _ in range(length)]
