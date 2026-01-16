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
Configuration for SWG Transaction Report  resource
'''

class swg_user_details(base_resource):
	_url_repu_3_volume= ""
	_user_name_prev= ""
	_exporter_id= ""
	_clean_url_count= ""
	_domain_name= ""
	_risk_score= ""
	_url_repu_level_0_count= ""
	_total_bytes_in= ""
	_total_ssl_intercepts= ""
	_clean_url_volume= ""
	_risky_url_count= ""
	_block_count_prev= ""
	_url_repu_level_4_count_prev= ""
	_total_bytes_prev= ""
	_user_name= ""
	_url_repu_2_volume= ""
	_url_repu_level_1_count= ""
	_total_requests= ""
	_total_bytes= ""
	_block_count= ""
	_total_bytes_out_prev= ""
	_url_repu_level_3_count= ""
	_url_repu_level_2_count_prev= ""
	_total_domains_prev= ""
	_url_repu_4_volume= ""
	_url_repu_level_4_count= ""
	___count= ""
	_url_repu_level_3_count_prev= ""
	_total_bytes_out= ""
	_total_domains= ""
	_total_requests_prev= ""
	_rpt_sample_time= ""
	_total_ssl_intercepts_prev= ""
	_clean_url_count_prev= ""
	_total_bytes_in_prev= ""
	_risk_score_prev= ""
	_url_repu_level_2_count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "swg_user_details"
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
			return "swg_user_detailss"
		except Exception as e :
			raise e



	'''
	get URL reputation level 3 volume
	'''
	@property
	def url_repu_3_volume(self) :
		try:
			return self._url_repu_3_volume
		except Exception as e :
			raise e
	'''
	set URL reputation level 3 volume
	'''
	@url_repu_3_volume.setter
	def url_repu_3_volume(self,url_repu_3_volume):
		try :
			if not isinstance(url_repu_3_volume,float):
				raise TypeError("url_repu_3_volume must be set to float value")
			self._url_repu_3_volume = url_repu_3_volume
		except Exception as e :
			raise e


	'''
	get User Name
	'''
	@property
	def user_name_prev(self) :
		try:
			return self._user_name_prev
		except Exception as e :
			raise e
	'''
	set User Name
	'''
	@user_name_prev.setter
	def user_name_prev(self,user_name_prev):
		try :
			if not isinstance(user_name_prev,str):
				raise TypeError("user_name_prev must be set to str value")
			self._user_name_prev = user_name_prev
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
			if not isinstance(exporter_id,float):
				raise TypeError("exporter_id must be set to float value")
			self._exporter_id = exporter_id
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
	get Risk Score
	'''
	@property
	def risk_score(self) :
		try:
			return self._risk_score
		except Exception as e :
			raise e
	'''
	set Risk Score
	'''
	@risk_score.setter
	def risk_score(self,risk_score):
		try :
			if not isinstance(risk_score,float):
				raise TypeError("risk_score must be set to float value")
			self._risk_score = risk_score
		except Exception as e :
			raise e


	'''
	get URL reputation level 0 count
	'''
	@property
	def url_repu_level_0_count(self) :
		try:
			return self._url_repu_level_0_count
		except Exception as e :
			raise e
	'''
	set URL reputation level 0 count
	'''
	@url_repu_level_0_count.setter
	def url_repu_level_0_count(self,url_repu_level_0_count):
		try :
			if not isinstance(url_repu_level_0_count,float):
				raise TypeError("url_repu_level_0_count must be set to float value")
			self._url_repu_level_0_count = url_repu_level_0_count
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
	get Clean URL volume
	'''
	@property
	def clean_url_volume(self) :
		try:
			return self._clean_url_volume
		except Exception as e :
			raise e
	'''
	set Clean URL volume
	'''
	@clean_url_volume.setter
	def clean_url_volume(self,clean_url_volume):
		try :
			if not isinstance(clean_url_volume,float):
				raise TypeError("clean_url_volume must be set to float value")
			self._clean_url_volume = clean_url_volume
		except Exception as e :
			raise e


	'''
	get Risky URL count
	'''
	@property
	def risky_url_count(self) :
		try:
			return self._risky_url_count
		except Exception as e :
			raise e
	'''
	set Risky URL count
	'''
	@risky_url_count.setter
	def risky_url_count(self,risky_url_count):
		try :
			if not isinstance(risky_url_count,float):
				raise TypeError("risky_url_count must be set to float value")
			self._risky_url_count = risky_url_count
		except Exception as e :
			raise e


	'''
	get URL Block count Prev
	'''
	@property
	def block_count_prev(self) :
		try:
			return self._block_count_prev
		except Exception as e :
			raise e
	'''
	set URL Block count Prev
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
	get URL reputation level 2 volume
	'''
	@property
	def url_repu_2_volume(self) :
		try:
			return self._url_repu_2_volume
		except Exception as e :
			raise e
	'''
	set URL reputation level 2 volume
	'''
	@url_repu_2_volume.setter
	def url_repu_2_volume(self,url_repu_2_volume):
		try :
			if not isinstance(url_repu_2_volume,float):
				raise TypeError("url_repu_2_volume must be set to float value")
			self._url_repu_2_volume = url_repu_2_volume
		except Exception as e :
			raise e


	'''
	get URL reputation level 1 count
	'''
	@property
	def url_repu_level_1_count(self) :
		try:
			return self._url_repu_level_1_count
		except Exception as e :
			raise e
	'''
	set URL reputation level 1 count
	'''
	@url_repu_level_1_count.setter
	def url_repu_level_1_count(self,url_repu_level_1_count):
		try :
			if not isinstance(url_repu_level_1_count,float):
				raise TypeError("url_repu_level_1_count must be set to float value")
			self._url_repu_level_1_count = url_repu_level_1_count
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
	get URL Block count
	'''
	@property
	def block_count(self) :
		try:
			return self._block_count
		except Exception as e :
			raise e
	'''
	set URL Block count
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
	get Total bytes out prev
	'''
	@property
	def total_bytes_out_prev(self) :
		try:
			return self._total_bytes_out_prev
		except Exception as e :
			raise e
	'''
	set Total bytes out prev
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
	get Domains count
	'''
	@property
	def total_domains_prev(self) :
		try:
			return self._total_domains_prev
		except Exception as e :
			raise e
	'''
	set Domains count
	'''
	@total_domains_prev.setter
	def total_domains_prev(self,total_domains_prev):
		try :
			if not isinstance(total_domains_prev,float):
				raise TypeError("total_domains_prev must be set to float value")
			self._total_domains_prev = total_domains_prev
		except Exception as e :
			raise e


	'''
	get URL reputation level 4 volume
	'''
	@property
	def url_repu_4_volume(self) :
		try:
			return self._url_repu_4_volume
		except Exception as e :
			raise e
	'''
	set URL reputation level 4 volume
	'''
	@url_repu_4_volume.setter
	def url_repu_4_volume(self,url_repu_4_volume):
		try :
			if not isinstance(url_repu_4_volume,float):
				raise TypeError("url_repu_4_volume must be set to float value")
			self._url_repu_4_volume = url_repu_4_volume
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
	get Domains count
	'''
	@property
	def total_domains(self) :
		try:
			return self._total_domains
		except Exception as e :
			raise e
	'''
	set Domains count
	'''
	@total_domains.setter
	def total_domains(self,total_domains):
		try :
			if not isinstance(total_domains,float):
				raise TypeError("total_domains must be set to float value")
			self._total_domains = total_domains
		except Exception as e :
			raise e


	'''
	get Total transactions prev
	'''
	@property
	def total_requests_prev(self) :
		try:
			return self._total_requests_prev
		except Exception as e :
			raise e
	'''
	set Total transactions prev
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
	get Total Intercepts prev
	'''
	@property
	def total_ssl_intercepts_prev(self) :
		try:
			return self._total_ssl_intercepts_prev
		except Exception as e :
			raise e
	'''
	set Total Intercepts prev
	'''
	@total_ssl_intercepts_prev.setter
	def total_ssl_intercepts_prev(self,total_ssl_intercepts_prev):
		try :
			if not isinstance(total_ssl_intercepts_prev,float):
				raise TypeError("total_ssl_intercepts_prev must be set to float value")
			self._total_ssl_intercepts_prev = total_ssl_intercepts_prev
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
	get Total bytes in prev
	'''
	@property
	def total_bytes_in_prev(self) :
		try:
			return self._total_bytes_in_prev
		except Exception as e :
			raise e
	'''
	set Total bytes in prev
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
	get Risk Score prev
	'''
	@property
	def risk_score_prev(self) :
		try:
			return self._risk_score_prev
		except Exception as e :
			raise e
	'''
	set Risk Score prev
	'''
	@risk_score_prev.setter
	def risk_score_prev(self,risk_score_prev):
		try :
			if not isinstance(risk_score_prev,float):
				raise TypeError("risk_score_prev must be set to float value")
			self._risk_score_prev = risk_score_prev
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
	Af Report for Top URL being Count Managed by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				swg_user_details_obj=swg_user_details()
				response = swg_user_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of swg_user_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			swg_user_details_obj = swg_user_details()
			option_ = options()
			option_._filter=filter_
			return swg_user_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the swg_user_details resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			swg_user_details_obj = swg_user_details()
			option_ = options()
			option_._count=True
			response = swg_user_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of swg_user_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			swg_user_details_obj = swg_user_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = swg_user_details_obj.getfiltered(service, option_)
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
	Set Query Parameter - group_by
	'''
	@classmethod
	def set_queryparam_group_by(cls, option, value):
		option.add_queryparam("group_by",value)

	'''
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(swg_user_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.swg_user_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(swg_user_details_responses, response, "swg_user_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.swg_user_details_response_array
				i=0
				error = [swg_user_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.swg_user_details_response_array
			i=0
			swg_user_details_objs = [swg_user_details() for _ in range(len(response))]
			for obj in response :
				for props in obj._swg_user_details:
					result = service.payload_formatter.string_to_bulk_resource(swg_user_details_response,self.__class__.__name__,props)
					swg_user_details_objs[i] = result.swg_user_details
					i=i+1
			return swg_user_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(swg_user_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class swg_user_details_response(base_response):
	def __init__(self,length=1) :
		self.swg_user_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.swg_user_details= [ swg_user_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class swg_user_details_responses(base_response):
	def __init__(self,length=1) :
		self.swg_user_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.swg_user_details_response_array = [ swg_user_details() for _ in range(length)]
