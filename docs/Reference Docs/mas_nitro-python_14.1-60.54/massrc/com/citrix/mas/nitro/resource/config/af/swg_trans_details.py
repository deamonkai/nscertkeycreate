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
Configuration for SWG Transaction Report resource
'''

class swg_trans_details(base_resource):
	_domain_name_prev= ""
	_clean_url_count= ""
	_url_reputation= ""
	_ssli_action_prev= ""
	_block_count_prev= ""
	_user_count_prev= ""
	_port= ""
	_url_repu_level_2_count_prev= ""
	_url_repu_level_3_count= ""
	_total_bytes= ""
	_http_req_method= ""
	___count= ""
	_url_repu_level_4_count= ""
	_total_bytes_out= ""
	_urlcategory_prev= ""
	_url_repu_level_3_count_prev= ""
	_url_group_category_prev= ""
	_rpt_sample_time= ""
	_total_requests_prev= ""
	_total_bytes_in_prev= ""
	_user_agent= ""
	_http_rsp_status= ""
	_domain_name= ""
	_vserver_name= ""
	_exporter_id= ""
	_user_name= ""
	_client_ip_address= ""
	_total_bytes_prev= ""
	_url_repu_level_4_count_prev= ""
	_total_ssl_intercepts= ""
	_total_bytes_in= ""
	_ssli_action= ""
	_block_count= ""
	_total_bytes_out_prev= ""
	_total_requests= ""
	_urlcategory= ""
	_url_category= ""
	_protocol= ""
	_user_count= ""
	_operating_system= ""
	_url_group_category= ""
	_url_repu_level_2_count= ""
	_clean_url_count_prev= ""
	_url_reputation_prev= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "swg_trans_details"
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
			return "swg_trans_detailss"
		except Exception as e :
			raise e



	'''
	get HTTP Request URL.
	'''
	@property
	def domain_name_prev(self) :
		try:
			return self._domain_name_prev
		except Exception as e :
			raise e
	'''
	set HTTP Request URL.
	'''
	@domain_name_prev.setter
	def domain_name_prev(self,domain_name_prev):
		try :
			if not isinstance(domain_name_prev,str):
				raise TypeError("domain_name_prev must be set to str value")
			self._domain_name_prev = domain_name_prev
		except Exception as e :
			raise e


	'''
	get Clean URL count
	'''
	@property
	def clean_url_count(self) :
		try:
			return self._clean_url_count
		except Exception as e :
			raise e
	'''
	set Clean URL count
	'''
	@clean_url_count.setter
	def clean_url_count(self,clean_url_count):
		try :
			if not isinstance(clean_url_count,float):
				raise TypeError("clean_url_count must be set to float value")
			self._clean_url_count = clean_url_count
		except Exception as e :
			raise e


	'''
	get URL reputation
	'''
	@property
	def url_reputation(self) :
		try:
			return self._url_reputation
		except Exception as e :
			raise e
	'''
	set URL reputation
	'''
	@url_reputation.setter
	def url_reputation(self,url_reputation):
		try :
			if not isinstance(url_reputation,float):
				raise TypeError("url_reputation must be set to float value")
			self._url_reputation = url_reputation
		except Exception as e :
			raise e


	'''
	get URL Action
	'''
	@property
	def ssli_action_prev(self) :
		try:
			return self._ssli_action_prev
		except Exception as e :
			raise e
	'''
	set URL Action
	'''
	@ssli_action_prev.setter
	def ssli_action_prev(self,ssli_action_prev):
		try :
			if not isinstance(ssli_action_prev,str):
				raise TypeError("ssli_action_prev must be set to str value")
			self._ssli_action_prev = ssli_action_prev
		except Exception as e :
			raise e


	'''
	get BLOCK URL Count
	'''
	@property
	def block_count_prev(self) :
		try:
			return self._block_count_prev
		except Exception as e :
			raise e
	'''
	set BLOCK URL Count
	'''
	@block_count_prev.setter
	def block_count_prev(self,block_count_prev):
		try :
			if not isinstance(block_count_prev,float):
				raise TypeError("block_count_prev must be set to float value")
			self._block_count_prev = block_count_prev
		except Exception as e :
			raise e


	'''
	get Users Count
	'''
	@property
	def user_count_prev(self) :
		try:
			return self._user_count_prev
		except Exception as e :
			raise e
	'''
	set Users Count
	'''
	@user_count_prev.setter
	def user_count_prev(self,user_count_prev):
		try :
			if not isinstance(user_count_prev,float):
				raise TypeError("user_count_prev must be set to float value")
			self._user_count_prev = user_count_prev
		except Exception as e :
			raise e


	'''
	get prot used
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set prot used
	'''
	@port.setter
	def port(self,port):
		try :
			if not isinstance(port,float):
				raise TypeError("port must be set to float value")
			self._port = port
		except Exception as e :
			raise e


	'''
	get URL reputation level 2 count prev
	'''
	@property
	def url_repu_level_2_count_prev(self) :
		try:
			return self._url_repu_level_2_count_prev
		except Exception as e :
			raise e
	'''
	set URL reputation level 2 count prev
	'''
	@url_repu_level_2_count_prev.setter
	def url_repu_level_2_count_prev(self,url_repu_level_2_count_prev):
		try :
			if not isinstance(url_repu_level_2_count_prev,float):
				raise TypeError("url_repu_level_2_count_prev must be set to float value")
			self._url_repu_level_2_count_prev = url_repu_level_2_count_prev
		except Exception as e :
			raise e


	'''
	get URL reputation level 3 count
	'''
	@property
	def url_repu_level_3_count(self) :
		try:
			return self._url_repu_level_3_count
		except Exception as e :
			raise e
	'''
	set URL reputation level 3 count
	'''
	@url_repu_level_3_count.setter
	def url_repu_level_3_count(self,url_repu_level_3_count):
		try :
			if not isinstance(url_repu_level_3_count,float):
				raise TypeError("url_repu_level_3_count must be set to float value")
			self._url_repu_level_3_count = url_repu_level_3_count
		except Exception as e :
			raise e


	'''
	get Total bytes
	'''
	@property
	def total_bytes(self) :
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	set Total bytes
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
			if not isinstance(http_req_method,str):
				raise TypeError("http_req_method must be set to str value")
			self._http_req_method = http_req_method
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
	get URL reputation level 4 count
	'''
	@property
	def url_repu_level_4_count(self) :
		try:
			return self._url_repu_level_4_count
		except Exception as e :
			raise e
	'''
	set URL reputation level 4 count
	'''
	@url_repu_level_4_count.setter
	def url_repu_level_4_count(self,url_repu_level_4_count):
		try :
			if not isinstance(url_repu_level_4_count,float):
				raise TypeError("url_repu_level_4_count must be set to float value")
			self._url_repu_level_4_count = url_repu_level_4_count
		except Exception as e :
			raise e


	'''
	get Total bytes out
	'''
	@property
	def total_bytes_out(self) :
		try:
			return self._total_bytes_out
		except Exception as e :
			raise e
	'''
	set Total bytes out
	'''
	@total_bytes_out.setter
	def total_bytes_out(self,total_bytes_out):
		try :
			if not isinstance(total_bytes_out,float):
				raise TypeError("total_bytes_out must be set to float value")
			self._total_bytes_out = total_bytes_out
		except Exception as e :
			raise e


	'''
	get URL Category
	'''
	@property
	def urlcategory_prev(self) :
		try:
			return self._urlcategory_prev
		except Exception as e :
			raise e
	'''
	set URL Category
	'''
	@urlcategory_prev.setter
	def urlcategory_prev(self,urlcategory_prev):
		try :
			if not isinstance(urlcategory_prev,str):
				raise TypeError("urlcategory_prev must be set to str value")
			self._urlcategory_prev = urlcategory_prev
		except Exception as e :
			raise e


	'''
	get URL reputation level 3 count prev
	'''
	@property
	def url_repu_level_3_count_prev(self) :
		try:
			return self._url_repu_level_3_count_prev
		except Exception as e :
			raise e
	'''
	set URL reputation level 3 count prev
	'''
	@url_repu_level_3_count_prev.setter
	def url_repu_level_3_count_prev(self,url_repu_level_3_count_prev):
		try :
			if not isinstance(url_repu_level_3_count_prev,float):
				raise TypeError("url_repu_level_3_count_prev must be set to float value")
			self._url_repu_level_3_count_prev = url_repu_level_3_count_prev
		except Exception as e :
			raise e


	'''
	get URL Group Category
	'''
	@property
	def url_group_category_prev(self) :
		try:
			return self._url_group_category_prev
		except Exception as e :
			raise e
	'''
	set URL Group Category
	'''
	@url_group_category_prev.setter
	def url_group_category_prev(self,url_group_category_prev):
		try :
			if not isinstance(url_group_category_prev,str):
				raise TypeError("url_group_category_prev must be set to str value")
			self._url_group_category_prev = url_group_category_prev
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
	get Total transactions
	'''
	@property
	def total_requests_prev(self) :
		try:
			return self._total_requests_prev
		except Exception as e :
			raise e
	'''
	set Total transactions
	'''
	@total_requests_prev.setter
	def total_requests_prev(self,total_requests_prev):
		try :
			if not isinstance(total_requests_prev,float):
				raise TypeError("total_requests_prev must be set to float value")
			self._total_requests_prev = total_requests_prev
		except Exception as e :
			raise e


	'''
	get Total bytes in
	'''
	@property
	def total_bytes_in_prev(self) :
		try:
			return self._total_bytes_in_prev
		except Exception as e :
			raise e
	'''
	set Total bytes in
	'''
	@total_bytes_in_prev.setter
	def total_bytes_in_prev(self,total_bytes_in_prev):
		try :
			if not isinstance(total_bytes_in_prev,float):
				raise TypeError("total_bytes_in_prev must be set to float value")
			self._total_bytes_in_prev = total_bytes_in_prev
		except Exception as e :
			raise e


	'''
	get User Agent Name.
	'''
	@property
	def user_agent(self) :
		try:
			return self._user_agent
		except Exception as e :
			raise e
	'''
	set User Agent Name.
	'''
	@user_agent.setter
	def user_agent(self,user_agent):
		try :
			if not isinstance(user_agent,str):
				raise TypeError("user_agent must be set to str value")
			self._user_agent = user_agent
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
			if not isinstance(http_rsp_status,str):
				raise TypeError("http_rsp_status must be set to str value")
			self._http_rsp_status = http_rsp_status
		except Exception as e :
			raise e


	'''
	get HTTP Request URL.
	'''
	@property
	def domain_name(self) :
		try:
			return self._domain_name
		except Exception as e :
			raise e
	'''
	set HTTP Request URL.
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
	get User Name
	'''
	@property
	def user_name(self) :
		try:
			return self._user_name
		except Exception as e :
			raise e
	'''
	set User Name
	'''
	@user_name.setter
	def user_name(self,user_name):
		try :
			if not isinstance(user_name,str):
				raise TypeError("user_name must be set to str value")
			self._user_name = user_name
		except Exception as e :
			raise e


	'''
	get Client ip address
	'''
	@property
	def client_ip_address(self) :
		try:
			return self._client_ip_address
		except Exception as e :
			raise e
	'''
	set Client ip address
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
	get Total bytes prev
	'''
	@property
	def total_bytes_prev(self) :
		try:
			return self._total_bytes_prev
		except Exception as e :
			raise e
	'''
	set Total bytes prev
	'''
	@total_bytes_prev.setter
	def total_bytes_prev(self,total_bytes_prev):
		try :
			if not isinstance(total_bytes_prev,float):
				raise TypeError("total_bytes_prev must be set to float value")
			self._total_bytes_prev = total_bytes_prev
		except Exception as e :
			raise e


	'''
	get URL reputation level 4 count prev
	'''
	@property
	def url_repu_level_4_count_prev(self) :
		try:
			return self._url_repu_level_4_count_prev
		except Exception as e :
			raise e
	'''
	set URL reputation level 4 count prev
	'''
	@url_repu_level_4_count_prev.setter
	def url_repu_level_4_count_prev(self,url_repu_level_4_count_prev):
		try :
			if not isinstance(url_repu_level_4_count_prev,float):
				raise TypeError("url_repu_level_4_count_prev must be set to float value")
			self._url_repu_level_4_count_prev = url_repu_level_4_count_prev
		except Exception as e :
			raise e


	'''
	get Total Intercepts
	'''
	@property
	def total_ssl_intercepts(self) :
		try:
			return self._total_ssl_intercepts
		except Exception as e :
			raise e
	'''
	set Total Intercepts
	'''
	@total_ssl_intercepts.setter
	def total_ssl_intercepts(self,total_ssl_intercepts):
		try :
			if not isinstance(total_ssl_intercepts,float):
				raise TypeError("total_ssl_intercepts must be set to float value")
			self._total_ssl_intercepts = total_ssl_intercepts
		except Exception as e :
			raise e


	'''
	get Total bytes in
	'''
	@property
	def total_bytes_in(self) :
		try:
			return self._total_bytes_in
		except Exception as e :
			raise e
	'''
	set Total bytes in
	'''
	@total_bytes_in.setter
	def total_bytes_in(self,total_bytes_in):
		try :
			if not isinstance(total_bytes_in,float):
				raise TypeError("total_bytes_in must be set to float value")
			self._total_bytes_in = total_bytes_in
		except Exception as e :
			raise e


	'''
	get URL Action
	'''
	@property
	def ssli_action(self) :
		try:
			return self._ssli_action
		except Exception as e :
			raise e
	'''
	set URL Action
	'''
	@ssli_action.setter
	def ssli_action(self,ssli_action):
		try :
			if not isinstance(ssli_action,str):
				raise TypeError("ssli_action must be set to str value")
			self._ssli_action = ssli_action
		except Exception as e :
			raise e


	'''
	get Block URL Count
	'''
	@property
	def block_count(self) :
		try:
			return self._block_count
		except Exception as e :
			raise e
	'''
	set Block URL Count
	'''
	@block_count.setter
	def block_count(self,block_count):
		try :
			if not isinstance(block_count,float):
				raise TypeError("block_count must be set to float value")
			self._block_count = block_count
		except Exception as e :
			raise e


	'''
	get Total bytes out
	'''
	@property
	def total_bytes_out_prev(self) :
		try:
			return self._total_bytes_out_prev
		except Exception as e :
			raise e
	'''
	set Total bytes out
	'''
	@total_bytes_out_prev.setter
	def total_bytes_out_prev(self,total_bytes_out_prev):
		try :
			if not isinstance(total_bytes_out_prev,float):
				raise TypeError("total_bytes_out_prev must be set to float value")
			self._total_bytes_out_prev = total_bytes_out_prev
		except Exception as e :
			raise e


	'''
	get Total transactions
	'''
	@property
	def total_requests(self) :
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	set Total transactions
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
	get URL Category
	'''
	@property
	def urlcategory(self) :
		try:
			return self._urlcategory
		except Exception as e :
			raise e
	'''
	set URL Category
	'''
	@urlcategory.setter
	def urlcategory(self,urlcategory):
		try :
			if not isinstance(urlcategory,str):
				raise TypeError("urlcategory must be set to str value")
			self._urlcategory = urlcategory
		except Exception as e :
			raise e


	'''
	get URL Category
	'''
	@property
	def url_category(self) :
		try:
			return self._url_category
		except Exception as e :
			raise e
	'''
	set URL Category
	'''
	@url_category.setter
	def url_category(self,url_category):
		try :
			if not isinstance(url_category,float):
				raise TypeError("url_category must be set to float value")
			self._url_category = url_category
		except Exception as e :
			raise e


	'''
	get protocol used
	'''
	@property
	def protocol(self) :
		try:
			return self._protocol
		except Exception as e :
			raise e
	'''
	set protocol used
	'''
	@protocol.setter
	def protocol(self,protocol):
		try :
			if not isinstance(protocol,str):
				raise TypeError("protocol must be set to str value")
			self._protocol = protocol
		except Exception as e :
			raise e


	'''
	get Users Count
	'''
	@property
	def user_count(self) :
		try:
			return self._user_count
		except Exception as e :
			raise e
	'''
	set Users Count
	'''
	@user_count.setter
	def user_count(self,user_count):
		try :
			if not isinstance(user_count,float):
				raise TypeError("user_count must be set to float value")
			self._user_count = user_count
		except Exception as e :
			raise e


	'''
	get Client Operating System Name.
	'''
	@property
	def operating_system(self) :
		try:
			return self._operating_system
		except Exception as e :
			raise e
	'''
	set Client Operating System Name.
	'''
	@operating_system.setter
	def operating_system(self,operating_system):
		try :
			if not isinstance(operating_system,str):
				raise TypeError("operating_system must be set to str value")
			self._operating_system = operating_system
		except Exception as e :
			raise e


	'''
	get URL Group Category
	'''
	@property
	def url_group_category(self) :
		try:
			return self._url_group_category
		except Exception as e :
			raise e
	'''
	set URL Group Category
	'''
	@url_group_category.setter
	def url_group_category(self,url_group_category):
		try :
			if not isinstance(url_group_category,str):
				raise TypeError("url_group_category must be set to str value")
			self._url_group_category = url_group_category
		except Exception as e :
			raise e


	'''
	get URL reputation level 2 count
	'''
	@property
	def url_repu_level_2_count(self) :
		try:
			return self._url_repu_level_2_count
		except Exception as e :
			raise e
	'''
	set URL reputation level 2 count
	'''
	@url_repu_level_2_count.setter
	def url_repu_level_2_count(self,url_repu_level_2_count):
		try :
			if not isinstance(url_repu_level_2_count,float):
				raise TypeError("url_repu_level_2_count must be set to float value")
			self._url_repu_level_2_count = url_repu_level_2_count
		except Exception as e :
			raise e


	'''
	get Clean URL count Prev
	'''
	@property
	def clean_url_count_prev(self) :
		try:
			return self._clean_url_count_prev
		except Exception as e :
			raise e
	'''
	set Clean URL count Prev
	'''
	@clean_url_count_prev.setter
	def clean_url_count_prev(self,clean_url_count_prev):
		try :
			if not isinstance(clean_url_count_prev,float):
				raise TypeError("clean_url_count_prev must be set to float value")
			self._clean_url_count_prev = clean_url_count_prev
		except Exception as e :
			raise e


	'''
	get URL reputation
	'''
	@property
	def url_reputation_prev(self) :
		try:
			return self._url_reputation_prev
		except Exception as e :
			raise e
	'''
	set URL reputation
	'''
	@url_reputation_prev.setter
	def url_reputation_prev(self,url_reputation_prev):
		try :
			if not isinstance(url_reputation_prev,long):
				raise TypeError("url_reputation_prev must be set to long value")
			self._url_reputation_prev = url_reputation_prev
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
				swg_trans_details_obj=swg_trans_details()
				response = swg_trans_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of swg_trans_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			swg_trans_details_obj = swg_trans_details()
			option_ = options()
			option_._filter=filter_
			return swg_trans_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the swg_trans_details resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			swg_trans_details_obj = swg_trans_details()
			option_ = options()
			option_._count=True
			response = swg_trans_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of swg_trans_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			swg_trans_details_obj = swg_trans_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = swg_trans_details_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(swg_trans_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.swg_trans_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(swg_trans_details_responses, response, "swg_trans_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.swg_trans_details_response_array
				i=0
				error = [swg_trans_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.swg_trans_details_response_array
			i=0
			swg_trans_details_objs = [swg_trans_details() for _ in range(len(response))]
			for obj in response :
				for props in obj._swg_trans_details:
					result = service.payload_formatter.string_to_bulk_resource(swg_trans_details_response,self.__class__.__name__,props)
					swg_trans_details_objs[i] = result.swg_trans_details
					i=i+1
			return swg_trans_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(swg_trans_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class swg_trans_details_response(base_response):
	def __init__(self,length=1) :
		self.swg_trans_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.swg_trans_details= [ swg_trans_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class swg_trans_details_responses(base_response):
	def __init__(self,length=1) :
		self.swg_trans_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.swg_trans_details_response_array = [ swg_trans_details() for _ in range(length)]
