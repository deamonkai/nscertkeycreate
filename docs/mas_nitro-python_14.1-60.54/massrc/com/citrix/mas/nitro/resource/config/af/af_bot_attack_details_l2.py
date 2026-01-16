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
Configuration for AF Bot Attack details table for Level 2 resource
'''

class af_bot_attack_details_l2(base_resource):
	_city= ""
	_total_attacks= ""
	_backend_appname= ""
	_bot_severity= ""
	_appname= ""
	_source_ip_address= ""
	_bot_detection_mechanism= ""
	_bot_type= ""
	_action_type= ""
	_latitude= ""
	_country_code= ""
	_ctnsappname= ""
	_longitude= ""
	_backend_vserver= ""
	_rpt_sample_time= ""
	_bot_category= ""
	_bot_signature_category= ""
	_region_code= ""
	_ip_address= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_bot_attack_details_l2"
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
			return "af_bot_attack_details_l2s"
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
	get bot detection mechanism.
	'''
	@property
	def bot_detection_mechanism(self) :
		try:
			return self._bot_detection_mechanism
		except Exception as e :
			raise e
	'''
	set bot detection mechanism.
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
	get bot_type.
	'''
	@property
	def bot_type(self) :
		try:
			return self._bot_type
		except Exception as e :
			raise e
	'''
	set bot_type.
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
	get action_type.
	'''
	@property
	def action_type(self) :
		try:
			return self._action_type
		except Exception as e :
			raise e
	'''
	set action_type.
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
	get ctnsappname
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set ctnsappname
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
	get Backend vserver name.
	'''
	@property
	def backend_vserver(self) :
		try:
			return self._backend_vserver
		except Exception as e :
			raise e
	'''
	set Backend vserver name.
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
	get bot_category
	'''
	@property
	def bot_category(self) :
		try:
			return self._bot_category
		except Exception as e :
			raise e
	'''
	set bot_category
	'''
	@bot_category.setter
	def bot_category(self,bot_category):
		try :
			if not isinstance(bot_category,int):
				raise TypeError("bot_category must be set to int value")
			self._bot_category = bot_category
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
	Af Report for Bot Attack Details..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_bot_attack_details_l2_obj=af_bot_attack_details_l2()
				response = af_bot_attack_details_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_bot_attack_details_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_bot_attack_details_l2_obj = af_bot_attack_details_l2()
			option_ = options()
			option_._filter=filter_
			return af_bot_attack_details_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_bot_attack_details_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_bot_attack_details_l2_obj = af_bot_attack_details_l2()
			option_ = options()
			option_._count=True
			response = af_bot_attack_details_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_bot_attack_details_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_bot_attack_details_l2_obj = af_bot_attack_details_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_bot_attack_details_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_bot_attack_details_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_bot_attack_details_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_bot_attack_details_l2_responses, response, "af_bot_attack_details_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_bot_attack_details_l2_response_array
				i=0
				error = [af_bot_attack_details_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_bot_attack_details_l2_response_array
			i=0
			af_bot_attack_details_l2_objs = [af_bot_attack_details_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_bot_attack_details_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_bot_attack_details_l2_response,self.__class__.__name__,props)
					af_bot_attack_details_l2_objs[i] = result.af_bot_attack_details_l2
					i=i+1
			return af_bot_attack_details_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_bot_attack_details_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_bot_attack_details_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_bot_attack_details_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_bot_attack_details_l2= [ af_bot_attack_details_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_bot_attack_details_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_bot_attack_details_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_bot_attack_details_l2_response_array = [ af_bot_attack_details_l2() for _ in range(length)]
