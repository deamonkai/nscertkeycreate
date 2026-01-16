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
Configuration for af geoclient API resource resource
'''

class af_geoclient(af_generic_api):
	_country= ""
	_region= ""
	_domain_name= ""
	_country_code= ""
	_app_unit_name= ""
	___count= ""
	_city= ""
	_bandwidth= ""
	_network_latency_client_side= ""
	_application_name= ""
	_region_code= ""
	_application_response_time= ""
	_total_bytes= ""
	_total_requests= ""
	_client_ip_address= ""
	_total_user= ""
	_device_ip_address= ""
	_network_latency_server_side= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_geoclient"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(af_geoclient,self).get_object_id()
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
			return "af_geoclients"
		except Exception as e :
			raise e


	'''
	Country Name
	'''
	@property
	def country(self):
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	Country Name
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
	Region Name
	'''
	@property
	def region(self):
		try:
			return self._region
		except Exception as e :
			raise e
	'''
	Region Name
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
	Domain Name.
	'''
	@property
	def domain_name(self):
		try:
			return self._domain_name
		except Exception as e :
			raise e
	'''
	Domain Name.
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
	Vserver Name
	'''
	@property
	def app_unit_name(self):
		try:
			return self._app_unit_name
		except Exception as e :
			raise e
	'''
	Vserver Name
	'''
	@app_unit_name.setter
	def app_unit_name(self,app_unit_name):
		try :
			if not isinstance(app_unit_name,str):
				raise TypeError("app_unit_name must be set to str value")
			self._app_unit_name = app_unit_name
		except Exception as e :
			raise e

	'''
	count of geo location record.
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	count of geo location record.
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
	Average Bandwidth.
	'''
	@property
	def bandwidth(self):
		try:
			return self._bandwidth
		except Exception as e :
			raise e
	'''
	Average Bandwidth.
	'''
	@bandwidth.setter
	def bandwidth(self,bandwidth):
		try :
			if not isinstance(bandwidth,float):
				raise TypeError("bandwidth must be set to float value")
			self._bandwidth = bandwidth
		except Exception as e :
			raise e

	'''
	Network latency client side in selected geo client.
	'''
	@property
	def network_latency_client_side(self):
		try:
			return self._network_latency_client_side
		except Exception as e :
			raise e
	'''
	Network latency client side in selected geo client.
	'''
	@network_latency_client_side.setter
	def network_latency_client_side(self,network_latency_client_side):
		try :
			if not isinstance(network_latency_client_side,float):
				raise TypeError("network_latency_client_side must be set to float value")
			self._network_latency_client_side = network_latency_client_side
		except Exception as e :
			raise e

	'''
	Application Name
	'''
	@property
	def application_name(self):
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	Application Name
	'''
	@application_name.setter
	def application_name(self,application_name):
		try :
			if not isinstance(application_name,str):
				raise TypeError("application_name must be set to str value")
			self._application_name = application_name
		except Exception as e :
			raise e

	'''
	Region Code
	'''
	@property
	def region_code(self):
		try:
			return self._region_code
		except Exception as e :
			raise e
	'''
	Region Code
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
	Application response time.
	'''
	@property
	def application_response_time(self):
		try:
			return self._application_response_time
		except Exception as e :
			raise e
	'''
	Application response time.
	'''
	@application_response_time.setter
	def application_response_time(self,application_response_time):
		try :
			if not isinstance(application_response_time,float):
				raise TypeError("application_response_time must be set to float value")
			self._application_response_time = application_response_time
		except Exception as e :
			raise e

	'''
	Total bytes accounted by this in selected geo client.
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes accounted by this in selected geo client.
	'''
	@total_bytes.setter
	def total_bytes(self,total_bytes):
		try :
			if not isinstance(total_bytes,float):
				raise TypeError("total_bytes must be set to float value")
			self._total_bytes = total_bytes
		except Exception as e :
			raise e

	'''
	Count of URL request in selected geo client.
	'''
	@property
	def total_requests(self):
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	Count of URL request in selected geo client.
	'''
	@total_requests.setter
	def total_requests(self,total_requests):
		try :
			if not isinstance(total_requests,float):
				raise TypeError("total_requests must be set to float value")
			self._total_requests = total_requests
		except Exception as e :
			raise e

	'''
	Client IP Address
	'''
	@property
	def client_ip_address(self):
		try:
			return self._client_ip_address
		except Exception as e :
			raise e
	'''
	Client IP Address
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
	Count of user i.e. various client IP addresses in the selected region.
	'''
	@property
	def total_user(self):
		try:
			return self._total_user
		except Exception as e :
			raise e
	'''
	Count of user i.e. various client IP addresses in the selected region.
	'''
	@total_user.setter
	def total_user(self,total_user):
		try :
			if not isinstance(total_user,float):
				raise TypeError("total_user must be set to float value")
			self._total_user = total_user
		except Exception as e :
			raise e

	'''
	NetScaler IP Address
	'''
	@property
	def device_ip_address(self):
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address
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
	Network latency server side in selected geo client.
	'''
	@property
	def network_latency_server_side(self):
		try:
			return self._network_latency_server_side
		except Exception as e :
			raise e
	'''
	Network latency server side in selected geo client.
	'''
	@network_latency_server_side.setter
	def network_latency_server_side(self,network_latency_server_side):
		try :
			if not isinstance(network_latency_server_side,float):
				raise TypeError("network_latency_server_side must be set to float value")
			self._network_latency_server_side = network_latency_server_side
		except Exception as e :
			raise e

	'''
	Use this operation to get geo client ip.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_geoclient_obj=af_geoclient()
				response = af_geoclient_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_geoclient resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_geoclient_obj = af_geoclient()
			option_ = options()
			option_._filter=filter_
			return af_geoclient_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_geoclient resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_geoclient_obj = af_geoclient()
			option_ = options()
			option_._count=True
			response = af_geoclient_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_geoclient resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_geoclient_obj = af_geoclient()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_geoclient_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_geoclient_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_geoclient
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_geoclient_responses, response, "af_geoclient_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_geoclient_response_array
				i=0
				error = [af_geoclient() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_geoclient_response_array
			i=0
			af_geoclient_objs = [af_geoclient() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_geoclient:
					result = service.payload_formatter.string_to_bulk_resource(af_geoclient_response,self.__class__.__name__,props)
					af_geoclient_objs[i] = result.af_geoclient
					i=i+1
			return af_geoclient_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_geoclient,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_geoclient_response(base_response):
	def __init__(self,length=1) :
		self.af_geoclient= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_geoclient= [ af_geoclient() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_geoclient_responses(base_response):
	def __init__(self,length=1) :
		self.af_geoclient_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_geoclient_response_array = [ af_geoclient() for _ in range(length)]
