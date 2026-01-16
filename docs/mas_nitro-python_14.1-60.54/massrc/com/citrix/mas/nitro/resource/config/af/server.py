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
Configuration for AF Server Report table resource
'''

class server(af_generic_api):
	_vpn_user_name= ""
	_uri_url= ""
	_total_bytes_ic_miss= ""
	_total_bytes_cache_bypass= ""
	_client_ip_address= ""
	_total_requests= ""
	_application_name= ""
	_ip_address= ""
	_percent_bw_saved= ""
	_domain_name= ""
	_server_response_time_max= ""
	_network_latency_server_side= ""
	_ic_no_store_reason= ""
	_ic_non_cache_hits= ""
	_ic_reval= ""
	_ssl_cipher_name= ""
	_ssl_protocol_name= ""
	_ic_utilization= ""
	_ssl_certificate_name= ""
	_device_ip_address= ""
	_ic_hits= ""
	_cache_bypass= ""
	_user_agent_name= ""
	_ctnsappname_b= ""
	_cache_miss= ""
	_http_content_type_name= ""
	_total_bytes= ""
	_operating_system_name= ""
	_server_type= ""
	_total_bytes_ic_reval= ""
	_max_transaction_time= ""
	_http_req_method_name= ""
	_id= ""
	_app_unit_name= ""
	_http_media_type_name= ""
	_cache_hits= ""
	_ssl_key_strength_name= ""
	_server_response_time= ""
	_ic_miss= ""
	_rpt_sample_time= ""
	_total_bytes_cache_miss= ""
	_ssl_cipher_negotiated_cipher_name= ""
	_http_resp_status_name= ""
	_total_bytes_cache_hits= ""
	_network_latency_server_side_max= ""
	___count= ""
	_total_bytes_ic_hits= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "server"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(server,self).get_object_id()
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
			return "servers"
		except Exception as e :
			raise e


	'''
	vpn user name.
	'''
	@property
	def vpn_user_name(self):
		try:
			return self._vpn_user_name
		except Exception as e :
			raise e
	'''
	vpn user name.
	'''
	@vpn_user_name.setter
	def vpn_user_name(self,vpn_user_name):
		try :
			if not isinstance(vpn_user_name,str):
				raise TypeError("vpn_user_name must be set to str value")
			self._vpn_user_name = vpn_user_name
		except Exception as e :
			raise e

	'''
	HTTP Request URL.
	'''
	@property
	def uri_url(self):
		try:
			return self._uri_url
		except Exception as e :
			raise e
	'''
	HTTP Request URL.
	'''
	@uri_url.setter
	def uri_url(self,uri_url):
		try :
			if not isinstance(uri_url,str):
				raise TypeError("uri_url must be set to str value")
			self._uri_url = uri_url
		except Exception as e :
			raise e

	'''
	Cache Miss total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes_ic_miss(self):
		try:
			return self._total_bytes_ic_miss
		except Exception as e :
			raise e
	'''
	Cache Miss total bytes accounted by this URL in sampled timeframe.
	'''
	@total_bytes_ic_miss.setter
	def total_bytes_ic_miss(self,total_bytes_ic_miss):
		try :
			if not isinstance(total_bytes_ic_miss,float):
				raise TypeError("total_bytes_ic_miss must be set to float value")
			self._total_bytes_ic_miss = total_bytes_ic_miss
		except Exception as e :
			raise e

	'''
	Cache Bypass total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes_cache_bypass(self):
		try:
			return self._total_bytes_cache_bypass
		except Exception as e :
			raise e
	'''
	Cache Bypass total bytes accounted by this URL in sampled timeframe.
	'''
	@total_bytes_cache_bypass.setter
	def total_bytes_cache_bypass(self,total_bytes_cache_bypass):
		try :
			if not isinstance(total_bytes_cache_bypass,float):
				raise TypeError("total_bytes_cache_bypass must be set to float value")
			self._total_bytes_cache_bypass = total_bytes_cache_bypass
		except Exception as e :
			raise e

	'''
	Top Clients for this Server.
	'''
	@property
	def client_ip_address(self):
		try:
			return self._client_ip_address
		except Exception as e :
			raise e
	'''
	Top Clients for this Server.
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
	Total Requests for this server in given sampled timeframe.
	'''
	@property
	def total_requests(self):
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	Total Requests for this server in given sampled timeframe.
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
	Ip Address of this Server.
	'''
	@property
	def ip_address(self):
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	Ip Address of this Server.
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
	Percentage of bw save to this APP in given sampled timeframe.
	'''
	@property
	def percent_bw_saved(self):
		try:
			return self._percent_bw_saved
		except Exception as e :
			raise e
	'''
	Percentage of bw save to this APP in given sampled timeframe.
	'''
	@percent_bw_saved.setter
	def percent_bw_saved(self,percent_bw_saved):
		try :
			if not isinstance(percent_bw_saved,float):
				raise TypeError("percent_bw_saved must be set to float value")
			self._percent_bw_saved = percent_bw_saved
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
	Max value of Server response time.
	'''
	@property
	def server_response_time_max(self):
		try:
			return self._server_response_time_max
		except Exception as e :
			raise e
	'''
	Max value of Server response time.
	'''
	@server_response_time_max.setter
	def server_response_time_max(self,server_response_time_max):
		try :
			if not isinstance(server_response_time_max,float):
				raise TypeError("server_response_time_max must be set to float value")
			self._server_response_time_max = server_response_time_max
		except Exception as e :
			raise e

	'''
	Network latency server side.
	'''
	@property
	def network_latency_server_side(self):
		try:
			return self._network_latency_server_side
		except Exception as e :
			raise e
	'''
	Network latency server side.
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
	ic_no_store_reason.
	'''
	@property
	def ic_no_store_reason(self):
		try:
			return self._ic_no_store_reason
		except Exception as e :
			raise e
	'''
	ic_no_store_reason.
	'''
	@ic_no_store_reason.setter
	def ic_no_store_reason(self,ic_no_store_reason):
		try :
			if not isinstance(ic_no_store_reason,str):
				raise TypeError("ic_no_store_reason must be set to str value")
			self._ic_no_store_reason = ic_no_store_reason
		except Exception as e :
			raise e

	'''
	Total requests to this APP for cache bypass in given sampled timeframe.
	'''
	@property
	def ic_non_cache_hits(self):
		try:
			return self._ic_non_cache_hits
		except Exception as e :
			raise e
	'''
	Total requests to this APP for cache bypass in given sampled timeframe.
	'''
	@ic_non_cache_hits.setter
	def ic_non_cache_hits(self,ic_non_cache_hits):
		try :
			if not isinstance(ic_non_cache_hits,float):
				raise TypeError("ic_non_cache_hits must be set to float value")
			self._ic_non_cache_hits = ic_non_cache_hits
		except Exception as e :
			raise e

	'''
	Total requests to this APP for cache bypass in given sampled timeframe.
	'''
	@property
	def ic_reval(self):
		try:
			return self._ic_reval
		except Exception as e :
			raise e
	'''
	Total requests to this APP for cache bypass in given sampled timeframe.
	'''
	@ic_reval.setter
	def ic_reval(self,ic_reval):
		try :
			if not isinstance(ic_reval,float):
				raise TypeError("ic_reval must be set to float value")
			self._ic_reval = ic_reval
		except Exception as e :
			raise e

	'''
	SSL cipher name.
	'''
	@property
	def ssl_cipher_name(self):
		try:
			return self._ssl_cipher_name
		except Exception as e :
			raise e
	'''
	SSL cipher name.
	'''
	@ssl_cipher_name.setter
	def ssl_cipher_name(self,ssl_cipher_name):
		try :
			if not isinstance(ssl_cipher_name,str):
				raise TypeError("ssl_cipher_name must be set to str value")
			self._ssl_cipher_name = ssl_cipher_name
		except Exception as e :
			raise e

	'''
	SSL protocol name.
	'''
	@property
	def ssl_protocol_name(self):
		try:
			return self._ssl_protocol_name
		except Exception as e :
			raise e
	'''
	SSL protocol name.
	'''
	@ssl_protocol_name.setter
	def ssl_protocol_name(self,ssl_protocol_name):
		try :
			if not isinstance(ssl_protocol_name,str):
				raise TypeError("ssl_protocol_name must be set to str value")
			self._ssl_protocol_name = ssl_protocol_name
		except Exception as e :
			raise e

	'''
	Total IC utilization in given sampled timeframe.
	'''
	@property
	def ic_utilization(self):
		try:
			return self._ic_utilization
		except Exception as e :
			raise e
	'''
	Total IC utilization in given sampled timeframe.
	'''
	@ic_utilization.setter
	def ic_utilization(self,ic_utilization):
		try :
			if not isinstance(ic_utilization,float):
				raise TypeError("ic_utilization must be set to float value")
			self._ic_utilization = ic_utilization
		except Exception as e :
			raise e

	'''
	SSL certificate name.
	'''
	@property
	def ssl_certificate_name(self):
		try:
			return self._ssl_certificate_name
		except Exception as e :
			raise e
	'''
	SSL certificate name.
	'''
	@ssl_certificate_name.setter
	def ssl_certificate_name(self,ssl_certificate_name):
		try :
			if not isinstance(ssl_certificate_name,str):
				raise TypeError("ssl_certificate_name must be set to str value")
			self._ssl_certificate_name = ssl_certificate_name
		except Exception as e :
			raise e

	'''
	NetScaler IP Address.
	'''
	@property
	def device_ip_address(self):
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address.
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
	Total requests to this APP for cache hits in given sampled timeframe.
	'''
	@property
	def ic_hits(self):
		try:
			return self._ic_hits
		except Exception as e :
			raise e
	'''
	Total requests to this APP for cache hits in given sampled timeframe.
	'''
	@ic_hits.setter
	def ic_hits(self,ic_hits):
		try :
			if not isinstance(ic_hits,float):
				raise TypeError("ic_hits must be set to float value")
			self._ic_hits = ic_hits
		except Exception as e :
			raise e

	'''
	Total requests to this APP for cache bypass in given sampled timeframe.
	'''
	@property
	def cache_bypass(self):
		try:
			return self._cache_bypass
		except Exception as e :
			raise e
	'''
	Total requests to this APP for cache bypass in given sampled timeframe.
	'''
	@cache_bypass.setter
	def cache_bypass(self,cache_bypass):
		try :
			if not isinstance(cache_bypass,float):
				raise TypeError("cache_bypass must be set to float value")
			self._cache_bypass = cache_bypass
		except Exception as e :
			raise e

	'''
	User Agent Name.
	'''
	@property
	def user_agent_name(self):
		try:
			return self._user_agent_name
		except Exception as e :
			raise e
	'''
	User Agent Name.
	'''
	@user_agent_name.setter
	def user_agent_name(self,user_agent_name):
		try :
			if not isinstance(user_agent_name,str):
				raise TypeError("user_agent_name must be set to str value")
			self._user_agent_name = user_agent_name
		except Exception as e :
			raise e

	'''
	Backend LB vserver
	'''
	@property
	def ctnsappname_b(self):
		try:
			return self._ctnsappname_b
		except Exception as e :
			raise e
	'''
	Backend LB vserver
	'''
	@ctnsappname_b.setter
	def ctnsappname_b(self,ctnsappname_b):
		try :
			if not isinstance(ctnsappname_b,str):
				raise TypeError("ctnsappname_b must be set to str value")
			self._ctnsappname_b = ctnsappname_b
		except Exception as e :
			raise e

	'''
	Total requests to this APP for cache miss in given sampled timeframe.
	'''
	@property
	def cache_miss(self):
		try:
			return self._cache_miss
		except Exception as e :
			raise e
	'''
	Total requests to this APP for cache miss in given sampled timeframe.
	'''
	@cache_miss.setter
	def cache_miss(self,cache_miss):
		try :
			if not isinstance(cache_miss,float):
				raise TypeError("cache_miss must be set to float value")
			self._cache_miss = cache_miss
		except Exception as e :
			raise e

	'''
	HTTP Content TYPE Name.
	'''
	@property
	def http_content_type_name(self):
		try:
			return self._http_content_type_name
		except Exception as e :
			raise e
	'''
	HTTP Content TYPE Name.
	'''
	@http_content_type_name.setter
	def http_content_type_name(self,http_content_type_name):
		try :
			if not isinstance(http_content_type_name,str):
				raise TypeError("http_content_type_name must be set to str value")
			self._http_content_type_name = http_content_type_name
		except Exception as e :
			raise e

	'''
	Total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes accounted by this URL in sampled timeframe.
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
	Client Operating System Name.
	'''
	@property
	def operating_system_name(self):
		try:
			return self._operating_system_name
		except Exception as e :
			raise e
	'''
	Client Operating System Name.
	'''
	@operating_system_name.setter
	def operating_system_name(self,operating_system_name):
		try :
			if not isinstance(operating_system_name,str):
				raise TypeError("operating_system_name must be set to str value")
			self._operating_system_name = operating_system_name
		except Exception as e :
			raise e

	'''
	Server Type.
	'''
	@property
	def server_type(self):
		try:
			return self._server_type
		except Exception as e :
			raise e
	'''
	Server Type.
	'''
	@server_type.setter
	def server_type(self,server_type):
		try :
			if not isinstance(server_type,str):
				raise TypeError("server_type must be set to str value")
			self._server_type = server_type
		except Exception as e :
			raise e

	'''
	Cache Reval total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes_ic_reval(self):
		try:
			return self._total_bytes_ic_reval
		except Exception as e :
			raise e
	'''
	Cache Reval total bytes accounted by this URL in sampled timeframe.
	'''
	@total_bytes_ic_reval.setter
	def total_bytes_ic_reval(self,total_bytes_ic_reval):
		try :
			if not isinstance(total_bytes_ic_reval,float):
				raise TypeError("total_bytes_ic_reval must be set to float value")
			self._total_bytes_ic_reval = total_bytes_ic_reval
		except Exception as e :
			raise e

	'''
	Last Transaction Time for this URL in the sampled timeframe.
	'''
	@property
	def max_transaction_time(self):
		try:
			return self._max_transaction_time
		except Exception as e :
			raise e
	'''
	Last Transaction Time for this URL in the sampled timeframe.
	'''
	@max_transaction_time.setter
	def max_transaction_time(self,max_transaction_time):
		try :
			if not isinstance(max_transaction_time,float):
				raise TypeError("max_transaction_time must be set to float value")
			self._max_transaction_time = max_transaction_time
		except Exception as e :
			raise e

	'''
	HTTP Request Method.
	'''
	@property
	def http_req_method_name(self):
		try:
			return self._http_req_method_name
		except Exception as e :
			raise e
	'''
	HTTP Request Method.
	'''
	@http_req_method_name.setter
	def http_req_method_name(self,http_req_method_name):
		try :
			if not isinstance(http_req_method_name,str):
				raise TypeError("http_req_method_name must be set to str value")
			self._http_req_method_name = http_req_method_name
		except Exception as e :
			raise e

	'''
	Id is Server IP Address.
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is Server IP Address.
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
	Client App Name
	'''
	@property
	def app_unit_name(self):
		try:
			return self._app_unit_name
		except Exception as e :
			raise e
	'''
	Client App Name
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
	HTTP MEDIA TYPE Name.
	'''
	@property
	def http_media_type_name(self):
		try:
			return self._http_media_type_name
		except Exception as e :
			raise e
	'''
	HTTP MEDIA TYPE Name.
	'''
	@http_media_type_name.setter
	def http_media_type_name(self,http_media_type_name):
		try :
			if not isinstance(http_media_type_name,str):
				raise TypeError("http_media_type_name must be set to str value")
			self._http_media_type_name = http_media_type_name
		except Exception as e :
			raise e

	'''
	Total requests to this APP for cache hits in given sampled timeframe.
	'''
	@property
	def cache_hits(self):
		try:
			return self._cache_hits
		except Exception as e :
			raise e
	'''
	Total requests to this APP for cache hits in given sampled timeframe.
	'''
	@cache_hits.setter
	def cache_hits(self,cache_hits):
		try :
			if not isinstance(cache_hits,float):
				raise TypeError("cache_hits must be set to float value")
			self._cache_hits = cache_hits
		except Exception as e :
			raise e

	'''
	SSL key strength name.
	'''
	@property
	def ssl_key_strength_name(self):
		try:
			return self._ssl_key_strength_name
		except Exception as e :
			raise e
	'''
	SSL key strength name.
	'''
	@ssl_key_strength_name.setter
	def ssl_key_strength_name(self,ssl_key_strength_name):
		try :
			if not isinstance(ssl_key_strength_name,str):
				raise TypeError("ssl_key_strength_name must be set to str value")
			self._ssl_key_strength_name = ssl_key_strength_name
		except Exception as e :
			raise e

	'''
	Server response time.
	'''
	@property
	def server_response_time(self):
		try:
			return self._server_response_time
		except Exception as e :
			raise e
	'''
	Server response time.
	'''
	@server_response_time.setter
	def server_response_time(self,server_response_time):
		try :
			if not isinstance(server_response_time,float):
				raise TypeError("server_response_time must be set to float value")
			self._server_response_time = server_response_time
		except Exception as e :
			raise e

	'''
	Total requests to this APP for cache miss in given sampled timeframe.
	'''
	@property
	def ic_miss(self):
		try:
			return self._ic_miss
		except Exception as e :
			raise e
	'''
	Total requests to this APP for cache miss in given sampled timeframe.
	'''
	@ic_miss.setter
	def ic_miss(self,ic_miss):
		try :
			if not isinstance(ic_miss,float):
				raise TypeError("ic_miss must be set to float value")
			self._ic_miss = ic_miss
		except Exception as e :
			raise e

	'''
	Report Sample time.
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	Report Sample time.
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
	Cache Miss total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes_cache_miss(self):
		try:
			return self._total_bytes_cache_miss
		except Exception as e :
			raise e
	'''
	Cache Miss total bytes accounted by this URL in sampled timeframe.
	'''
	@total_bytes_cache_miss.setter
	def total_bytes_cache_miss(self,total_bytes_cache_miss):
		try :
			if not isinstance(total_bytes_cache_miss,float):
				raise TypeError("total_bytes_cache_miss must be set to float value")
			self._total_bytes_cache_miss = total_bytes_cache_miss
		except Exception as e :
			raise e

	'''
	SSL cipher name.
	'''
	@property
	def ssl_cipher_negotiated_cipher_name(self):
		try:
			return self._ssl_cipher_negotiated_cipher_name
		except Exception as e :
			raise e
	'''
	SSL cipher name.
	'''
	@ssl_cipher_negotiated_cipher_name.setter
	def ssl_cipher_negotiated_cipher_name(self,ssl_cipher_negotiated_cipher_name):
		try :
			if not isinstance(ssl_cipher_negotiated_cipher_name,str):
				raise TypeError("ssl_cipher_negotiated_cipher_name must be set to str value")
			self._ssl_cipher_negotiated_cipher_name = ssl_cipher_negotiated_cipher_name
		except Exception as e :
			raise e

	'''
	HTTP Response Status Method.
	'''
	@property
	def http_resp_status_name(self):
		try:
			return self._http_resp_status_name
		except Exception as e :
			raise e
	'''
	HTTP Response Status Method.
	'''
	@http_resp_status_name.setter
	def http_resp_status_name(self,http_resp_status_name):
		try :
			if not isinstance(http_resp_status_name,str):
				raise TypeError("http_resp_status_name must be set to str value")
			self._http_resp_status_name = http_resp_status_name
		except Exception as e :
			raise e

	'''
	Cache Hits total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes_cache_hits(self):
		try:
			return self._total_bytes_cache_hits
		except Exception as e :
			raise e
	'''
	Cache Hits total bytes accounted by this URL in sampled timeframe.
	'''
	@total_bytes_cache_hits.setter
	def total_bytes_cache_hits(self,total_bytes_cache_hits):
		try :
			if not isinstance(total_bytes_cache_hits,float):
				raise TypeError("total_bytes_cache_hits must be set to float value")
			self._total_bytes_cache_hits = total_bytes_cache_hits
		except Exception as e :
			raise e

	'''
	Max value of Network latency server side.
	'''
	@property
	def network_latency_server_side_max(self):
		try:
			return self._network_latency_server_side_max
		except Exception as e :
			raise e
	'''
	Max value of Network latency server side.
	'''
	@network_latency_server_side_max.setter
	def network_latency_server_side_max(self,network_latency_server_side_max):
		try :
			if not isinstance(network_latency_server_side_max,float):
				raise TypeError("network_latency_server_side_max must be set to float value")
			self._network_latency_server_side_max = network_latency_server_side_max
		except Exception as e :
			raise e

	'''
	count.
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	count.
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
	IC Cache Hits total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes_ic_hits(self):
		try:
			return self._total_bytes_ic_hits
		except Exception as e :
			raise e
	'''
	IC Cache Hits total bytes accounted by this URL in sampled timeframe.
	'''
	@total_bytes_ic_hits.setter
	def total_bytes_ic_hits(self,total_bytes_ic_hits):
		try :
			if not isinstance(total_bytes_ic_hits,float):
				raise TypeError("total_bytes_ic_hits must be set to float value")
			self._total_bytes_ic_hits = total_bytes_ic_hits
		except Exception as e :
			raise e

	'''
	Af Report for Top URL being Count Managed by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				server_obj=server()
				response = server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			server_obj = server()
			option_ = options()
			option_._filter=filter_
			return server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the server resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			server_obj = server()
			option_ = options()
			option_._count=True
			response = server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			server_obj = server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = server_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

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
	Set Query Parameter - type
	'''
	@classmethod
	def set_queryparam_type(cls, option, value):
		option.add_queryparam("type",value)

	'''
	Set Query Parameter - cr_enabled
	'''
	@classmethod
	def set_queryparam_cr_enabled(cls, option, value):
		option.add_queryparam("cr_enabled",value)

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(server_responses, response, "server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.server_response_array
				i=0
				error = [server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.server_response_array
			i=0
			server_objs = [server() for _ in range(len(response))]
			for obj in response :
				for props in obj._server:
					result = service.payload_formatter.string_to_bulk_resource(server_response,self.__class__.__name__,props)
					server_objs[i] = result.server
					i=i+1
			return server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class server_response(base_response):
	def __init__(self,length=1) :
		self.server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.server= [ server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class server_responses(base_response):
	def __init__(self,length=1) :
		self.server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.server_response_array = [ server() for _ in range(length)]
