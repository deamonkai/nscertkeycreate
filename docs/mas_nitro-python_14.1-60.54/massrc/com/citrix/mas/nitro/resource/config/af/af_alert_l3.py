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
Configuration for Threshold breach information for Level 3 resource
'''

class af_alert_l3(base_resource):
	_ctnsappname= ""
	_country= ""
	_region= ""
	_violation_count= ""
	_exporter_id= ""
	_breach_value= ""
	_tenant_name= ""
	_city= ""
	_reference_key= ""
	_ip_address= ""
	_duration= ""
	_threshold_value= ""
	_stylebook_flag= ""
	_rpt_sample_time= ""
	_threshold_name= ""
	_metric= ""
	_entity_type= ""
	_is_enable_flag= ""
	_entity= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_alert_l3"
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
			return "af_alert_l3s"
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
	get Country Code
	'''
	@property
	def country(self) :
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	set Country Code
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
	get Region Code
	'''
	@property
	def region(self) :
		try:
			return self._region
		except Exception as e :
			raise e
	'''
	set Region Code
	'''
	@region.setter
	def region(self,region):
		try :
			if not isinstance(region,str):
				raise TypeError("region must be set to str value")
			self._region = region
		except Exception as e :
			raise e


	'''
	get No of times violation happens for particular entity
	'''
	@property
	def violation_count(self) :
		try:
			return self._violation_count
		except Exception as e :
			raise e
	'''
	set No of times violation happens for particular entity
	'''
	@violation_count.setter
	def violation_count(self,violation_count):
		try :
			if not isinstance(violation_count,long):
				raise TypeError("violation_count must be set to long value")
			self._violation_count = violation_count
		except Exception as e :
			raise e


	'''
	get Exporter Id
	'''
	@property
	def exporter_id(self) :
		try:
			return self._exporter_id
		except Exception as e :
			raise e
	'''
	set Exporter Id
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
	get Breach Value
	'''
	@property
	def breach_value(self) :
		try:
			return self._breach_value
		except Exception as e :
			raise e
	'''
	set Breach Value
	'''
	@breach_value.setter
	def breach_value(self,breach_value):
		try :
			if not isinstance(breach_value,str):
				raise TypeError("breach_value must be set to str value")
			self._breach_value = breach_value
		except Exception as e :
			raise e


	'''
	get Tenant Name
	'''
	@property
	def tenant_name(self) :
		try:
			return self._tenant_name
		except Exception as e :
			raise e
	'''
	set Tenant Name
	'''
	@tenant_name.setter
	def tenant_name(self,tenant_name):
		try :
			if not isinstance(tenant_name,str):
				raise TypeError("tenant_name must be set to str value")
			self._tenant_name = tenant_name
		except Exception as e :
			raise e


	'''
	get City
	'''
	@property
	def city(self) :
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	set City
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
	get Reference Key
	'''
	@property
	def reference_key(self) :
		try:
			return self._reference_key
		except Exception as e :
			raise e
	'''
	set Reference Key
	'''
	@reference_key.setter
	def reference_key(self,reference_key):
		try :
			if not isinstance(reference_key,str):
				raise TypeError("reference_key must be set to str value")
			self._reference_key = reference_key
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
	get Threshold calculation frequency period daily,weekly etc
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e
	'''
	set Threshold calculation frequency period daily,weekly etc
	'''
	@duration.setter
	def duration(self,duration):
		try :
			if not isinstance(duration,str):
				raise TypeError("duration must be set to str value")
			self._duration = duration
		except Exception as e :
			raise e


	'''
	get Threshold Value
	'''
	@property
	def threshold_value(self) :
		try:
			return self._threshold_value
		except Exception as e :
			raise e
	'''
	set Threshold Value
	'''
	@threshold_value.setter
	def threshold_value(self,threshold_value):
		try :
			if not isinstance(threshold_value,str):
				raise TypeError("threshold_value must be set to str value")
			self._threshold_value = threshold_value
		except Exception as e :
			raise e


	'''
	get Stylebook threshold configuration true or false
	'''
	@property
	def stylebook_flag(self) :
		try:
			return self._stylebook_flag
		except Exception as e :
			raise e
	'''
	set Stylebook threshold configuration true or false
	'''
	@stylebook_flag.setter
	def stylebook_flag(self,stylebook_flag):
		try :
			if not isinstance(stylebook_flag,bool):
				raise TypeError("stylebook_flag must be set to bool value")
			self._stylebook_flag = stylebook_flag
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
	get Threshold Name
	'''
	@property
	def threshold_name(self) :
		try:
			return self._threshold_name
		except Exception as e :
			raise e
	'''
	set Threshold Name
	'''
	@threshold_name.setter
	def threshold_name(self,threshold_name):
		try :
			if not isinstance(threshold_name,str):
				raise TypeError("threshold_name must be set to str value")
			self._threshold_name = threshold_name
		except Exception as e :
			raise e


	'''
	get Metric
	'''
	@property
	def metric(self) :
		try:
			return self._metric
		except Exception as e :
			raise e
	'''
	set Metric
	'''
	@metric.setter
	def metric(self,metric):
		try :
			if not isinstance(metric,str):
				raise TypeError("metric must be set to str value")
			self._metric = metric
		except Exception as e :
			raise e


	'''
	get Entity Type
	'''
	@property
	def entity_type(self) :
		try:
			return self._entity_type
		except Exception as e :
			raise e
	'''
	set Entity Type
	'''
	@entity_type.setter
	def entity_type(self,entity_type):
		try :
			if not isinstance(entity_type,str):
				raise TypeError("entity_type must be set to str value")
			self._entity_type = entity_type
		except Exception as e :
			raise e


	'''
	get  Only applicable for configuration entries, 1=enable, 2=disable, 3=delete
	'''
	@property
	def is_enable_flag(self) :
		try:
			return self._is_enable_flag
		except Exception as e :
			raise e
	'''
	set  Only applicable for configuration entries, 1=enable, 2=disable, 3=delete
	'''
	@is_enable_flag.setter
	def is_enable_flag(self,is_enable_flag):
		try :
			if not isinstance(is_enable_flag,long):
				raise TypeError("is_enable_flag must be set to long value")
			self._is_enable_flag = is_enable_flag
		except Exception as e :
			raise e


	'''
	get Entity
	'''
	@property
	def entity(self) :
		try:
			return self._entity
		except Exception as e :
			raise e
	'''
	set Entity
	'''
	@entity.setter
	def entity(self,entity):
		try :
			if not isinstance(entity,str):
				raise TypeError("entity must be set to str value")
			self._entity = entity
		except Exception as e :
			raise e

	'''
	AF report for threshold configuration & breaches.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_alert_l3_obj=af_alert_l3()
				response = af_alert_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_alert_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_alert_l3_obj = af_alert_l3()
			option_ = options()
			option_._filter=filter_
			return af_alert_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_alert_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_alert_l3_obj = af_alert_l3()
			option_ = options()
			option_._count=True
			response = af_alert_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_alert_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_alert_l3_obj = af_alert_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_alert_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_alert_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_alert_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_alert_l3_responses, response, "af_alert_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_alert_l3_response_array
				i=0
				error = [af_alert_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_alert_l3_response_array
			i=0
			af_alert_l3_objs = [af_alert_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_alert_l3:
					result = service.payload_formatter.string_to_bulk_resource(af_alert_l3_response,self.__class__.__name__,props)
					af_alert_l3_objs[i] = result.af_alert_l3
					i=i+1
			return af_alert_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_alert_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_alert_l3_response(base_response):
	def __init__(self,length=1) :
		self.af_alert_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_alert_l3= [ af_alert_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_alert_l3_responses(base_response):
	def __init__(self,length=1) :
		self.af_alert_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_alert_l3_response_array = [ af_alert_l3() for _ in range(length)]
