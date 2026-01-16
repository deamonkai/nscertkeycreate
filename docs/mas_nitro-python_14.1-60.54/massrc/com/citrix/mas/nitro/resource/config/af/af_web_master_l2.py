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
Configuration for AF Web Master Report table for Level 2 resource
'''

class af_web_master_l2(base_resource):
	_ic_miss= ""
	_is_auth= ""
	_is_api= ""
	_rpt_sample_time= ""
	_network_latency_client_side_max= ""
	_auth_success= ""
	_network_latency_server_side_max= ""
	_stnssource_ip_address= ""
	_unsupportedciphers= ""
	_auth_failure= ""
	_ic_hits= ""
	_api_spec_name= ""
	_total_bytes= ""
	_http_req_url= ""
	_http_req_method= ""
	_max_query_param= ""
	_latitude= ""
	_netscaler_processing_time= ""
	_cipherStrength_frontend= ""
	_ctnssource_ip_address= ""
	_device= ""
	_server_response_time= ""
	_network_latency_server_side= ""
	_isSSL= ""
	_ctnssource_ip_address_str= ""
	_region_code= ""
	_network_latency_client_side= ""
	_total_ratelimited_requests= ""
	_stnssource_ip_address_str= ""
	_load_time= ""
	_sslVersion_frontend= ""
	_min_query_param= ""
	_country_code= ""
	_operating_system= ""
	_api_endpoint= ""
	_ctnsappname= ""
	_srvr_cert_hash_frontend= ""
	_longitude= ""
	_browser= ""
	_authentication_status_code= ""
	_total_requests= ""
	_cipherValue_frontend= ""
	_application_response_time= ""
	_isSSLError= ""
	_query_param= ""
	_application_name= ""
	_ip_address= ""
	_mismatchciphers= ""
	_vservername= ""
	_render_time= ""
	_isfrontend= ""
	_city= ""
	_http_rsp_status= ""
	_serverCertSize_frontend= ""
	_handshakemsg= ""
	_domain_name= ""
	_server_response_time_max= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_web_master_l2"
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
			return "af_web_master_l2s"
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
	get is authentication enabled
	'''
	@property
	def is_auth(self) :
		try:
			return self._is_auth
		except Exception as e :
			raise e
	'''
	set is authentication enabled
	'''
	@is_auth.setter
	def is_auth(self,is_auth):
		try :
			if not isinstance(is_auth,int):
				raise TypeError("is_auth must be set to int value")
			self._is_auth = is_auth
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
	get Network Latency Client side Time.
	'''
	@property
	def network_latency_client_side_max(self) :
		try:
			return self._network_latency_client_side_max
		except Exception as e :
			raise e
	'''
	set Network Latency Client side Time.
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
	get Authentication Success Count.
	'''
	@property
	def auth_success(self) :
		try:
			return self._auth_success
		except Exception as e :
			raise e
	'''
	set Authentication Success Count.
	'''
	@auth_success.setter
	def auth_success(self,auth_success):
		try :
			if not isinstance(auth_success,long):
				raise TypeError("auth_success must be set to long value")
			self._auth_success = auth_success
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
	get Server Source IP Address
	'''
	@property
	def stnssource_ip_address(self) :
		try:
			return self._stnssource_ip_address
		except Exception as e :
			raise e
	'''
	set Server Source IP Address
	'''
	@stnssource_ip_address.setter
	def stnssource_ip_address(self,stnssource_ip_address):
		try :
			if not isinstance(stnssource_ip_address,long):
				raise TypeError("stnssource_ip_address must be set to long value")
			self._stnssource_ip_address = stnssource_ip_address
		except Exception as e :
			raise e


	'''
	get Unsupported Cipher
	'''
	@property
	def unsupportedciphers(self) :
		try:
			return self._unsupportedciphers
		except Exception as e :
			raise e
	'''
	set Unsupported Cipher
	'''
	@unsupportedciphers.setter
	def unsupportedciphers(self,unsupportedciphers):
		try :
			if not isinstance(unsupportedciphers,str):
				raise TypeError("unsupportedciphers must be set to str value")
			self._unsupportedciphers = unsupportedciphers
		except Exception as e :
			raise e


	'''
	get Authentication Failure Count.
	'''
	@property
	def auth_failure(self) :
		try:
			return self._auth_failure
		except Exception as e :
			raise e
	'''
	set Authentication Failure Count.
	'''
	@auth_failure.setter
	def auth_failure(self,auth_failure):
		try :
			if not isinstance(auth_failure,long):
				raise TypeError("auth_failure must be set to long value")
			self._auth_failure = auth_failure
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
	get API Spec Name.
	'''
	@property
	def api_spec_name(self) :
		try:
			return self._api_spec_name
		except Exception as e :
			raise e
	'''
	set API Spec Name.
	'''
	@api_spec_name.setter
	def api_spec_name(self,api_spec_name):
		try :
			if not isinstance(api_spec_name,str):
				raise TypeError("api_spec_name must be set to str value")
			self._api_spec_name = api_spec_name
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
	get Maximum number of query param
	'''
	@property
	def max_query_param(self) :
		try:
			return self._max_query_param
		except Exception as e :
			raise e
	'''
	set Maximum number of query param
	'''
	@max_query_param.setter
	def max_query_param(self,max_query_param):
		try :
			if not isinstance(max_query_param,int):
				raise TypeError("max_query_param must be set to int value")
			self._max_query_param = max_query_param
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
	get cipherStrength_frontend value. Cipher Negotiated. High, Medium, Low.
	'''
	@property
	def cipherStrength_frontend(self) :
		try:
			return self._cipherStrength_frontend
		except Exception as e :
			raise e
	'''
	set cipherStrength_frontend value. Cipher Negotiated. High, Medium, Low.
	'''
	@cipherStrength_frontend.setter
	def cipherStrength_frontend(self,cipherStrength_frontend):
		try :
			if not isinstance(cipherStrength_frontend,int):
				raise TypeError("cipherStrength_frontend must be set to int value")
			self._cipherStrength_frontend = cipherStrength_frontend
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
	get Client Device.
	'''
	@property
	def device(self) :
		try:
			return self._device
		except Exception as e :
			raise e
	'''
	set Client Device.
	'''
	@device.setter
	def device(self,device):
		try :
			if not isinstance(device,int):
				raise TypeError("device must be set to int value")
			self._device = device
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
	get isSSL value. 0, 1.
	'''
	@property
	def isSSL(self) :
		try:
			return self._isSSL
		except Exception as e :
			raise e
	'''
	set isSSL value. 0, 1.
	'''
	@isSSL.setter
	def isSSL(self,isSSL):
		try :
			if not isinstance(isSSL,int):
				raise TypeError("isSSL must be set to int value")
			self._isSSL = isSSL
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
	get Field to store Rate Limited total Requests
	'''
	@property
	def total_ratelimited_requests(self) :
		try:
			return self._total_ratelimited_requests
		except Exception as e :
			raise e
	'''
	set Field to store Rate Limited total Requests
	'''
	@total_ratelimited_requests.setter
	def total_ratelimited_requests(self,total_ratelimited_requests):
		try :
			if not isinstance(total_ratelimited_requests,long):
				raise TypeError("total_ratelimited_requests must be set to long value")
			self._total_ratelimited_requests = total_ratelimited_requests
		except Exception as e :
			raise e


	'''
	get Server Source IP Address String
	'''
	@property
	def stnssource_ip_address_str(self) :
		try:
			return self._stnssource_ip_address_str
		except Exception as e :
			raise e
	'''
	set Server Source IP Address String
	'''
	@stnssource_ip_address_str.setter
	def stnssource_ip_address_str(self,stnssource_ip_address_str):
		try :
			if not isinstance(stnssource_ip_address_str,str):
				raise TypeError("stnssource_ip_address_str must be set to str value")
			self._stnssource_ip_address_str = stnssource_ip_address_str
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
	get sslVersion_frontend value. SSL Certificate, SHA-1, SHA-2
	'''
	@property
	def sslVersion_frontend(self) :
		try:
			return self._sslVersion_frontend
		except Exception as e :
			raise e
	'''
	set sslVersion_frontend value. SSL Certificate, SHA-1, SHA-2
	'''
	@sslVersion_frontend.setter
	def sslVersion_frontend(self,sslVersion_frontend):
		try :
			if not isinstance(sslVersion_frontend,int):
				raise TypeError("sslVersion_frontend must be set to int value")
			self._sslVersion_frontend = sslVersion_frontend
		except Exception as e :
			raise e


	'''
	get Minimum number of query param
	'''
	@property
	def min_query_param(self) :
		try:
			return self._min_query_param
		except Exception as e :
			raise e
	'''
	set Minimum number of query param
	'''
	@min_query_param.setter
	def min_query_param(self,min_query_param):
		try :
			if not isinstance(min_query_param,int):
				raise TypeError("min_query_param must be set to int value")
			self._min_query_param = min_query_param
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
	get Operating System.
	'''
	@property
	def operating_system(self) :
		try:
			return self._operating_system
		except Exception as e :
			raise e
	'''
	set Operating System.
	'''
	@operating_system.setter
	def operating_system(self,operating_system):
		try :
			if not isinstance(operating_system,int):
				raise TypeError("operating_system must be set to int value")
			self._operating_system = operating_system
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
	get srvr_cert_hash_frontend value. SSL Protocol, TLS 1.1, TLS 1.2, SSLv3
	'''
	@property
	def srvr_cert_hash_frontend(self) :
		try:
			return self._srvr_cert_hash_frontend
		except Exception as e :
			raise e
	'''
	set srvr_cert_hash_frontend value. SSL Protocol, TLS 1.1, TLS 1.2, SSLv3
	'''
	@srvr_cert_hash_frontend.setter
	def srvr_cert_hash_frontend(self,srvr_cert_hash_frontend):
		try :
			if not isinstance(srvr_cert_hash_frontend,int):
				raise TypeError("srvr_cert_hash_frontend must be set to int value")
			self._srvr_cert_hash_frontend = srvr_cert_hash_frontend
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
	get Browser.
	'''
	@property
	def browser(self) :
		try:
			return self._browser
		except Exception as e :
			raise e
	'''
	set Browser.
	'''
	@browser.setter
	def browser(self,browser):
		try :
			if not isinstance(browser,int):
				raise TypeError("browser must be set to int value")
			self._browser = browser
		except Exception as e :
			raise e


	'''
	get Authentication Status Code
	'''
	@property
	def authentication_status_code(self) :
		try:
			return self._authentication_status_code
		except Exception as e :
			raise e
	'''
	set Authentication Status Code
	'''
	@authentication_status_code.setter
	def authentication_status_code(self,authentication_status_code):
		try :
			if not isinstance(authentication_status_code,int):
				raise TypeError("authentication_status_code must be set to int value")
			self._authentication_status_code = authentication_status_code
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
	get cipherValue_frontend value. Cipher name.
	'''
	@property
	def cipherValue_frontend(self) :
		try:
			return self._cipherValue_frontend
		except Exception as e :
			raise e
	'''
	set cipherValue_frontend value. Cipher name.
	'''
	@cipherValue_frontend.setter
	def cipherValue_frontend(self,cipherValue_frontend):
		try :
			if not isinstance(cipherValue_frontend,int):
				raise TypeError("cipherValue_frontend must be set to int value")
			self._cipherValue_frontend = cipherValue_frontend
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
	get is SSL Error
	'''
	@property
	def isSSLError(self) :
		try:
			return self._isSSLError
		except Exception as e :
			raise e
	'''
	set is SSL Error
	'''
	@isSSLError.setter
	def isSSLError(self,isSSLError):
		try :
			if not isinstance(isSSLError,int):
				raise TypeError("isSSLError must be set to int value")
			self._isSSLError = isSSLError
		except Exception as e :
			raise e


	'''
	get URL Query Param information
	'''
	@property
	def query_param(self) :
		try:
			return self._query_param
		except Exception as e :
			raise e
	'''
	set URL Query Param information
	'''
	@query_param.setter
	def query_param(self,query_param):
		try :
			if not isinstance(query_param,str):
				raise TypeError("query_param must be set to str value")
			self._query_param = query_param
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
	get Mismatch Cipher
	'''
	@property
	def mismatchciphers(self) :
		try:
			return self._mismatchciphers
		except Exception as e :
			raise e
	'''
	set Mismatch Cipher
	'''
	@mismatchciphers.setter
	def mismatchciphers(self,mismatchciphers):
		try :
			if not isinstance(mismatchciphers,str):
				raise TypeError("mismatchciphers must be set to str value")
			self._mismatchciphers = mismatchciphers
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
	get isfrontend.
	'''
	@property
	def isfrontend(self) :
		try:
			return self._isfrontend
		except Exception as e :
			raise e
	'''
	set isfrontend.
	'''
	@isfrontend.setter
	def isfrontend(self,isfrontend):
		try :
			if not isinstance(isfrontend,int):
				raise TypeError("isfrontend must be set to int value")
			self._isfrontend = isfrontend
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
	get HTTP Response Status.
	'''
	@property
	def http_rsp_status(self) :
		try:
			return self._http_rsp_status
		except Exception as e :
			raise e
	'''
	set HTTP Response Status.
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
	get serverCertSize_frontend value. Key Strenght, 2048, 1024, 4096.
	'''
	@property
	def serverCertSize_frontend(self) :
		try:
			return self._serverCertSize_frontend
		except Exception as e :
			raise e
	'''
	set serverCertSize_frontend value. Key Strenght, 2048, 1024, 4096.
	'''
	@serverCertSize_frontend.setter
	def serverCertSize_frontend(self,serverCertSize_frontend):
		try :
			if not isinstance(serverCertSize_frontend,int):
				raise TypeError("serverCertSize_frontend must be set to int value")
			self._serverCertSize_frontend = serverCertSize_frontend
		except Exception as e :
			raise e


	'''
	get HandShake Message.
	'''
	@property
	def handshakemsg(self) :
		try:
			return self._handshakemsg
		except Exception as e :
			raise e
	'''
	set HandShake Message.
	'''
	@handshakemsg.setter
	def handshakemsg(self,handshakemsg):
		try :
			if not isinstance(handshakemsg,long):
				raise TypeError("handshakemsg must be set to long value")
			self._handshakemsg = handshakemsg
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
	get Server Response Time.
	'''
	@property
	def server_response_time_max(self) :
		try:
			return self._server_response_time_max
		except Exception as e :
			raise e
	'''
	set Server Response Time.
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
	Af Report for Web Insight..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_web_master_l2_obj=af_web_master_l2()
				response = af_web_master_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_web_master_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_web_master_l2_obj = af_web_master_l2()
			option_ = options()
			option_._filter=filter_
			return af_web_master_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_web_master_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_web_master_l2_obj = af_web_master_l2()
			option_ = options()
			option_._count=True
			response = af_web_master_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_web_master_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_web_master_l2_obj = af_web_master_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_web_master_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_web_master_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_web_master_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_web_master_l2_responses, response, "af_web_master_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_web_master_l2_response_array
				i=0
				error = [af_web_master_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_web_master_l2_response_array
			i=0
			af_web_master_l2_objs = [af_web_master_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_web_master_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_web_master_l2_response,self.__class__.__name__,props)
					af_web_master_l2_objs[i] = result.af_web_master_l2
					i=i+1
			return af_web_master_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_web_master_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_web_master_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_web_master_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_web_master_l2= [ af_web_master_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_web_master_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_web_master_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_web_master_l2_response_array = [ af_web_master_l2() for _ in range(length)]
