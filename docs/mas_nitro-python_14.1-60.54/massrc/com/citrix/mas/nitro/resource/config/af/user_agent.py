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
Configuration for AF URL Report table resource
'''

class user_agent(af_generic_api):
	_total_bytes_ic_hits= ""
	_ic_utilization= ""
	_total_bytes_cache_hits= ""
	___count= ""
	_app_unit_ip_address= ""
	_ic_reval= ""
	_server_ip_address= ""
	_http_resp_status_name= ""
	_ic_miss= ""
	_ic_no_store_reason= ""
	_rpt_sample_time= ""
	_total_bytes_cache_miss= ""
	_ic_non_cache_hits= ""
	_http_media_type_name= ""
	_app_unit_name= ""
	_id= ""
	_percent_bw_saved= ""
	_name= ""
	_cache_hits= ""
	_domain_name= ""
	_render_time= ""
	_total_bytes_ic_reval= ""
	_max_transaction_time= ""
	_http_req_method_name= ""
	_application_name= ""
	_http_content_type_name= ""
	_total_bytes= ""
	_total_requests= ""
	_operating_system_name= ""
	_total_bytes_ic_miss= ""
	_uri_url= ""
	_device_ip_address= ""
	_total_bytes_cache_bypass= ""
	_vpn_user_name= ""
	_cache_miss= ""
	_client_ip_address= ""
	_ic_hits= ""
	_cache_bypass= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "user_agent"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(user_agent,self).get_object_id()
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
			return "user_agents"
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
	Vserver IP Address.
	'''
	@property
	def app_unit_ip_address(self):
		try:
			return self._app_unit_ip_address
		except Exception as e :
			raise e
	'''
	Vserver IP Address.
	'''
	@app_unit_ip_address.setter
	def app_unit_ip_address(self,app_unit_ip_address):
		try :
			if not isinstance(app_unit_ip_address,str):
				raise TypeError("app_unit_ip_address must be set to str value")
			self._app_unit_ip_address = app_unit_ip_address
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
	Server Source IP Address
	'''
	@property
	def server_ip_address(self):
		try:
			return self._server_ip_address
		except Exception as e :
			raise e
	'''
	Server Source IP Address
	'''
	@server_ip_address.setter
	def server_ip_address(self,server_ip_address):
		try :
			if not isinstance(server_ip_address,str):
				raise TypeError("server_ip_address must be set to str value")
			self._server_ip_address = server_ip_address
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
	IC no store reason.
	'''
	@property
	def ic_no_store_reason(self):
		try:
			return self._ic_no_store_reason
		except Exception as e :
			raise e
	'''
	IC no store reason.
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
	Id is User Agent.
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is User Agent.
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
	User Agent Name.
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	User Agent Name.
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
	Render time.
	'''
	@property
	def render_time(self):
		try:
			return self._render_time
		except Exception as e :
			raise e
	'''
	Render time.
	'''
	@render_time.setter
	def render_time(self,render_time):
		try :
			if not isinstance(render_time,float):
				raise TypeError("render_time must be set to float value")
			self._render_time = render_time
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
	Count of this URL in given sampled timeframe.
	'''
	@property
	def total_requests(self):
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	Count of this URL in given sampled timeframe.
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
	Client Source IP Address
	'''
	@property
	def client_ip_address(self):
		try:
			return self._client_ip_address
		except Exception as e :
			raise e
	'''
	Client Source IP Address
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
	Af Report for Top URL being Count Managed by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				user_agent_obj=user_agent()
				response = user_agent_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of user_agent resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			user_agent_obj = user_agent()
			option_ = options()
			option_._filter=filter_
			return user_agent_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the user_agent resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			user_agent_obj = user_agent()
			option_ = options()
			option_._count=True
			response = user_agent_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of user_agent resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			user_agent_obj = user_agent()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = user_agent_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

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
			result=service.payload_formatter.string_to_resource(user_agent_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.user_agent
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(user_agent_responses, response, "user_agent_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.user_agent_response_array
				i=0
				error = [user_agent() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.user_agent_response_array
			i=0
			user_agent_objs = [user_agent() for _ in range(len(response))]
			for obj in response :
				for props in obj._user_agent:
					result = service.payload_formatter.string_to_bulk_resource(user_agent_response,self.__class__.__name__,props)
					user_agent_objs[i] = result.user_agent
					i=i+1
			return user_agent_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(user_agent,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class user_agent_response(base_response):
	def __init__(self,length=1) :
		self.user_agent= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.user_agent= [ user_agent() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class user_agent_responses(base_response):
	def __init__(self,length=1) :
		self.user_agent_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.user_agent_response_array = [ user_agent() for _ in range(length)]
