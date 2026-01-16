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
Configuration for AF Device Report table for Level 3 resource
'''

class af_app_client_geo_second_l3(base_resource):
	_load_time= ""
	_network_latency_server_side_max= ""
	_country_code= ""
	_longitude= ""
	_ctnsappname= ""
	_api_endpoint= ""
	_ic_miss= ""
	_network_latency_server_side= ""
	_rpt_sample_time= ""
	_network_latency_client_side_max= ""
	_is_api= ""
	_region_code= ""
	_ctnssource_ip_address_str= ""
	_network_latency_client_side= ""
	_city= ""
	_render_time= ""
	_http_rsp_status= ""
	_exporter_id= ""
	_latitude= ""
	_netscaler_processing_time= ""
	_server_response_time= ""
	_server_response_time_max= ""
	_ctnssource_ip_address= ""
	_ic_hits= ""
	_application_name= ""
	_http_req_method= ""
	_http_req_url= ""
	_application_response_time= ""
	_total_bytes= ""
	_total_requests= ""
	_vservername= ""
	_ip_address= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_app_client_geo_second_l3"
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
			return "af_app_client_geo_second_l3s"
		except Exception as e :
			raise e



	'''
	get URI Load time.
	'''
	@property
	def load_time(self) :
		try:
			return self._load_time
		except Exception as e :
			raise e
	'''
	set URI Load time.
	'''
	@load_time.setter
	def load_time(self,load_time):
		try :
			if not isinstance(load_time,long):
				raise TypeError("load_time must be set to long value")
			self._load_time = load_time
		except Exception as e :
			raise e


	'''
	get Network Latency Client server Time.
	'''
	@property
	def network_latency_server_side_max(self) :
		try:
			return self._network_latency_server_side_max
		except Exception as e :
			raise e
	'''
	set Network Latency Client server Time.
	'''
	@network_latency_server_side_max.setter
	def network_latency_server_side_max(self,network_latency_server_side_max):
		try :
			if not isinstance(network_latency_server_side_max,long):
				raise TypeError("network_latency_server_side_max must be set to long value")
			self._network_latency_server_side_max = network_latency_server_side_max
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
	get API Endpoint based on API Spec Name.
	'''
	@property
	def api_endpoint(self) :
		try:
			return self._api_endpoint
		except Exception as e :
			raise e
	'''
	set API Endpoint based on API Spec Name.
	'''
	@api_endpoint.setter
	def api_endpoint(self,api_endpoint):
		try :
			if not isinstance(api_endpoint,str):
				raise TypeError("api_endpoint must be set to str value")
			self._api_endpoint = api_endpoint
		except Exception as e :
			raise e


	'''
	get Total IC miss accounted in sampled timeframe.
	'''
	@property
	def ic_miss(self) :
		try:
			return self._ic_miss
		except Exception as e :
			raise e
	'''
	set Total IC miss accounted in sampled timeframe.
	'''
	@ic_miss.setter
	def ic_miss(self,ic_miss):
		try :
			if not isinstance(ic_miss,long):
				raise TypeError("ic_miss must be set to long value")
			self._ic_miss = ic_miss
		except Exception as e :
			raise e


	'''
	get Network Latency Client server Time.
	'''
	@property
	def network_latency_server_side(self) :
		try:
			return self._network_latency_server_side
		except Exception as e :
			raise e
	'''
	set Network Latency Client server Time.
	'''
	@network_latency_server_side.setter
	def network_latency_server_side(self,network_latency_server_side):
		try :
			if not isinstance(network_latency_server_side,long):
				raise TypeError("network_latency_server_side must be set to long value")
			self._network_latency_server_side = network_latency_server_side
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
	get Max value Network Latency Client side in given duration.
	'''
	@property
	def network_latency_client_side_max(self) :
		try:
			return self._network_latency_client_side_max
		except Exception as e :
			raise e
	'''
	set Max value Network Latency Client side in given duration.
	'''
	@network_latency_client_side_max.setter
	def network_latency_client_side_max(self,network_latency_client_side_max):
		try :
			if not isinstance(network_latency_client_side_max,long):
				raise TypeError("network_latency_client_side_max must be set to long value")
			self._network_latency_client_side_max = network_latency_client_side_max
		except Exception as e :
			raise e


	'''
	get is this API traffic
	'''
	@property
	def is_api(self) :
		try:
			return self._is_api
		except Exception as e :
			raise e
	'''
	set is this API traffic
	'''
	@is_api.setter
	def is_api(self,is_api):
		try :
			if not isinstance(is_api,int):
				raise TypeError("is_api must be set to int value")
			self._is_api = is_api
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
	get Client Source IP Address String
	'''
	@property
	def ctnssource_ip_address_str(self) :
		try:
			return self._ctnssource_ip_address_str
		except Exception as e :
			raise e
	'''
	set Client Source IP Address String
	'''
	@ctnssource_ip_address_str.setter
	def ctnssource_ip_address_str(self,ctnssource_ip_address_str):
		try :
			if not isinstance(ctnssource_ip_address_str,str):
				raise TypeError("ctnssource_ip_address_str must be set to str value")
			self._ctnssource_ip_address_str = ctnssource_ip_address_str
		except Exception as e :
			raise e


	'''
	get Network Latency Client side Time.
	'''
	@property
	def network_latency_client_side(self) :
		try:
			return self._network_latency_client_side
		except Exception as e :
			raise e
	'''
	set Network Latency Client side Time.
	'''
	@network_latency_client_side.setter
	def network_latency_client_side(self,network_latency_client_side):
		try :
			if not isinstance(network_latency_client_side,long):
				raise TypeError("network_latency_client_side must be set to long value")
			self._network_latency_client_side = network_latency_client_side
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
	get Render time.
	'''
	@property
	def render_time(self) :
		try:
			return self._render_time
		except Exception as e :
			raise e
	'''
	set Render time.
	'''
	@render_time.setter
	def render_time(self,render_time):
		try :
			if not isinstance(render_time,long):
				raise TypeError("render_time must be set to long value")
			self._render_time = render_time
		except Exception as e :
			raise e


	'''
	get HTTP Response Status Method.
	'''
	@property
	def http_rsp_status(self) :
		try:
			return self._http_rsp_status
		except Exception as e :
			raise e
	'''
	set HTTP Response Status Method.
	'''
	@http_rsp_status.setter
	def http_rsp_status(self,http_rsp_status):
		try :
			if not isinstance(http_rsp_status,long):
				raise TypeError("http_rsp_status must be set to long value")
			self._http_rsp_status = http_rsp_status
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
	get NetScaler Processing Time.
	'''
	@property
	def netscaler_processing_time(self) :
		try:
			return self._netscaler_processing_time
		except Exception as e :
			raise e
	'''
	set NetScaler Processing Time.
	'''
	@netscaler_processing_time.setter
	def netscaler_processing_time(self,netscaler_processing_time):
		try :
			if not isinstance(netscaler_processing_time,long):
				raise TypeError("netscaler_processing_time must be set to long value")
			self._netscaler_processing_time = netscaler_processing_time
		except Exception as e :
			raise e


	'''
	get Server Response Time.
	'''
	@property
	def server_response_time(self) :
		try:
			return self._server_response_time
		except Exception as e :
			raise e
	'''
	set Server Response Time.
	'''
	@server_response_time.setter
	def server_response_time(self,server_response_time):
		try :
			if not isinstance(server_response_time,long):
				raise TypeError("server_response_time must be set to long value")
			self._server_response_time = server_response_time
		except Exception as e :
			raise e


	'''
	get Max value of Server Response Time for given duration.
	'''
	@property
	def server_response_time_max(self) :
		try:
			return self._server_response_time_max
		except Exception as e :
			raise e
	'''
	set Max value of Server Response Time for given duration.
	'''
	@server_response_time_max.setter
	def server_response_time_max(self,server_response_time_max):
		try :
			if not isinstance(server_response_time_max,long):
				raise TypeError("server_response_time_max must be set to long value")
			self._server_response_time_max = server_response_time_max
		except Exception as e :
			raise e


	'''
	get Client Source IP Address
	'''
	@property
	def ctnssource_ip_address(self) :
		try:
			return self._ctnssource_ip_address
		except Exception as e :
			raise e
	'''
	set Client Source IP Address
	'''
	@ctnssource_ip_address.setter
	def ctnssource_ip_address(self,ctnssource_ip_address):
		try :
			if not isinstance(ctnssource_ip_address,long):
				raise TypeError("ctnssource_ip_address must be set to long value")
			self._ctnssource_ip_address = ctnssource_ip_address
		except Exception as e :
			raise e


	'''
	get Total IC hits accounted in sampled timeframe.
	'''
	@property
	def ic_hits(self) :
		try:
			return self._ic_hits
		except Exception as e :
			raise e
	'''
	set Total IC hits accounted in sampled timeframe.
	'''
	@ic_hits.setter
	def ic_hits(self,ic_hits):
		try :
			if not isinstance(ic_hits,long):
				raise TypeError("ic_hits must be set to long value")
			self._ic_hits = ic_hits
		except Exception as e :
			raise e


	'''
	get Application Name
	'''
	@property
	def application_name(self) :
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	set Application Name
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
	get HTTP Request Method.
	'''
	@property
	def http_req_method(self) :
		try:
			return self._http_req_method
		except Exception as e :
			raise e
	'''
	set HTTP Request Method.
	'''
	@http_req_method.setter
	def http_req_method(self,http_req_method):
		try :
			if not isinstance(http_req_method,long):
				raise TypeError("http_req_method must be set to long value")
			self._http_req_method = http_req_method
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
	get Application Response Time.
	'''
	@property
	def application_response_time(self) :
		try:
			return self._application_response_time
		except Exception as e :
			raise e
	'''
	set Application Response Time.
	'''
	@application_response_time.setter
	def application_response_time(self,application_response_time):
		try :
			if not isinstance(application_response_time,long):
				raise TypeError("application_response_time must be set to long value")
			self._application_response_time = application_response_time
		except Exception as e :
			raise e


	'''
	get Total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes(self) :
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	set Total bytes accounted by this URL in sampled timeframe.
	'''
	@total_bytes.setter
	def total_bytes(self,total_bytes):
		try :
			if not isinstance(total_bytes,long):
				raise TypeError("total_bytes must be set to long value")
			self._total_bytes = total_bytes
		except Exception as e :
			raise e


	'''
	get Total Requests for this device in given sampled timeframe.
	'''
	@property
	def total_requests(self) :
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	set Total Requests for this device in given sampled timeframe.
	'''
	@total_requests.setter
	def total_requests(self,total_requests):
		try :
			if not isinstance(total_requests,long):
				raise TypeError("total_requests must be set to long value")
			self._total_requests = total_requests
		except Exception as e :
			raise e


	'''
	get Backend Vserver
	'''
	@property
	def vservername(self) :
		try:
			return self._vservername
		except Exception as e :
			raise e
	'''
	set Backend Vserver
	'''
	@vservername.setter
	def vservername(self,vservername):
		try :
			if not isinstance(vservername,str):
				raise TypeError("vservername must be set to str value")
			self._vservername = vservername
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
	Af Report for Device..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_app_client_geo_second_l3_obj=af_app_client_geo_second_l3()
				response = af_app_client_geo_second_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_app_client_geo_second_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_app_client_geo_second_l3_obj = af_app_client_geo_second_l3()
			option_ = options()
			option_._filter=filter_
			return af_app_client_geo_second_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_app_client_geo_second_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_app_client_geo_second_l3_obj = af_app_client_geo_second_l3()
			option_ = options()
			option_._count=True
			response = af_app_client_geo_second_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_app_client_geo_second_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_app_client_geo_second_l3_obj = af_app_client_geo_second_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_app_client_geo_second_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_app_client_geo_second_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_app_client_geo_second_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_app_client_geo_second_l3_responses, response, "af_app_client_geo_second_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_app_client_geo_second_l3_response_array
				i=0
				error = [af_app_client_geo_second_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_app_client_geo_second_l3_response_array
			i=0
			af_app_client_geo_second_l3_objs = [af_app_client_geo_second_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_app_client_geo_second_l3:
					result = service.payload_formatter.string_to_bulk_resource(af_app_client_geo_second_l3_response,self.__class__.__name__,props)
					af_app_client_geo_second_l3_objs[i] = result.af_app_client_geo_second_l3
					i=i+1
			return af_app_client_geo_second_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_app_client_geo_second_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_app_client_geo_second_l3_response(base_response):
	def __init__(self,length=1) :
		self.af_app_client_geo_second_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_app_client_geo_second_l3= [ af_app_client_geo_second_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_app_client_geo_second_l3_responses(base_response):
	def __init__(self,length=1) :
		self.af_app_client_geo_second_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_app_client_geo_second_l3_response_array = [ af_app_client_geo_second_l3() for _ in range(length)]
