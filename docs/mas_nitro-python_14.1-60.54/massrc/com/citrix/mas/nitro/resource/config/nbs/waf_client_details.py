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


import os
import logging
from logging import handlers, Formatter
from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for WAF Client Details resource
'''

class waf_client_details(base_resource):
	_query_params= ""
	_ind_weight_desc= ""
	_ind_name_desc= ""
	_client_ip= ""
	_rpt_sample_time= ""
	_suspicious_http_component= ""
	_anomalous_requests= ""
	_session_id= ""
	_ind_detection_time= ""
	_ctnsappname= ""
	_http_req_headers= ""
	_url= ""
	_ip_address= ""
	_ind_category_desc= ""
	_user_agent= ""
	_ind_id= ""
	_total_requests= ""
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/macro/v1/security/waf_client_details"
		except Exception as e :
			raise e

	'''
	get the resource id
	'''
	def get_resource_id(self) :
		try:
			if hasattr(self, 'id'):
				return self.id 
			else:
				return None 
		except Exception as e :
			raise e

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "waf_client_details"
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
			return "waf_client_detailss"
		except Exception as e :
			raise e



	'''
	get URL Query Params
	'''
	@property
	def query_params(self) :
		try:
			return self._query_params
		except Exception as e :
			raise e
	'''
	set URL Query Params
	'''
	@query_params.setter
	def query_params(self,query_params):
		try :
			if not isinstance(query_params,str):
				raise TypeError("query_params must be set to str value")
			self._query_params = query_params
		except Exception as e :
			raise e


	'''
	get Indicator weight description
	'''
	@property
	def ind_weight_desc(self) :
		try:
			return self._ind_weight_desc
		except Exception as e :
			raise e
	'''
	set Indicator weight description
	'''
	@ind_weight_desc.setter
	def ind_weight_desc(self,ind_weight_desc):
		try :
			if not isinstance(ind_weight_desc,int):
				raise TypeError("ind_weight_desc must be set to int value")
			self._ind_weight_desc = ind_weight_desc
		except Exception as e :
			raise e


	'''
	get Indicator name description
	'''
	@property
	def ind_name_desc(self) :
		try:
			return self._ind_name_desc
		except Exception as e :
			raise e
	'''
	set Indicator name description
	'''
	@ind_name_desc.setter
	def ind_name_desc(self,ind_name_desc):
		try :
			if not isinstance(ind_name_desc,str):
				raise TypeError("ind_name_desc must be set to str value")
			self._ind_name_desc = ind_name_desc
		except Exception as e :
			raise e


	'''
	get Client IP address
	'''
	@property
	def client_ip(self) :
		try:
			return self._client_ip
		except Exception as e :
			raise e
	'''
	set Client IP address
	'''
	@client_ip.setter
	def client_ip(self,client_ip):
		try :
			if not isinstance(client_ip,long):
				raise TypeError("client_ip must be set to long value")
			self._client_ip = client_ip
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
	get type of suspicious component: url, req header, query params
	'''
	@property
	def suspicious_http_component(self) :
		try:
			return self._suspicious_http_component
		except Exception as e :
			raise e
	'''
	set type of suspicious component: url, req header, query params
	'''
	@suspicious_http_component.setter
	def suspicious_http_component(self,suspicious_http_component):
		try :
			if not isinstance(suspicious_http_component,str):
				raise TypeError("suspicious_http_component must be set to str value")
			self._suspicious_http_component = suspicious_http_component
		except Exception as e :
			raise e


	'''
	get Anomalous Requests
	'''
	@property
	def anomalous_requests(self) :
		try:
			return self._anomalous_requests
		except Exception as e :
			raise e
	'''
	set Anomalous Requests
	'''
	@anomalous_requests.setter
	def anomalous_requests(self,anomalous_requests):
		try :
			if not isinstance(anomalous_requests,long):
				raise TypeError("anomalous_requests must be set to long value")
			self._anomalous_requests = anomalous_requests
		except Exception as e :
			raise e


	'''
	get Session ID
	'''
	@property
	def session_id(self) :
		try:
			return self._session_id
		except Exception as e :
			raise e
	'''
	set Session ID
	'''
	@session_id.setter
	def session_id(self,session_id):
		try :
			if not isinstance(session_id,str):
				raise TypeError("session_id must be set to str value")
			self._session_id = session_id
		except Exception as e :
			raise e


	'''
	get Anamoly detection time.
	'''
	@property
	def ind_detection_time(self) :
		try:
			return self._ind_detection_time
		except Exception as e :
			raise e
	'''
	set Anamoly detection time.
	'''
	@ind_detection_time.setter
	def ind_detection_time(self,ind_detection_time):
		try :
			if not isinstance(ind_detection_time,long):
				raise TypeError("ind_detection_time must be set to long value")
			self._ind_detection_time = ind_detection_time
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
	get HTTP Request Headers
	'''
	@property
	def http_req_headers(self) :
		try:
			return self._http_req_headers
		except Exception as e :
			raise e
	'''
	set HTTP Request Headers
	'''
	@http_req_headers.setter
	def http_req_headers(self,http_req_headers):
		try :
			if not isinstance(http_req_headers,str):
				raise TypeError("http_req_headers must be set to str value")
			self._http_req_headers = http_req_headers
		except Exception as e :
			raise e


	'''
	get Anonymous URL
	'''
	@property
	def url(self) :
		try:
			return self._url
		except Exception as e :
			raise e
	'''
	set Anonymous URL
	'''
	@url.setter
	def url(self,url):
		try :
			if not isinstance(url,str):
				raise TypeError("url must be set to str value")
			self._url = url
		except Exception as e :
			raise e


	'''
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
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
	get Indicator category description
	'''
	@property
	def ind_category_desc(self) :
		try:
			return self._ind_category_desc
		except Exception as e :
			raise e
	'''
	set Indicator category description
	'''
	@ind_category_desc.setter
	def ind_category_desc(self,ind_category_desc):
		try :
			if not isinstance(ind_category_desc,str):
				raise TypeError("ind_category_desc must be set to str value")
			self._ind_category_desc = ind_category_desc
		except Exception as e :
			raise e


	'''
	get User Agent String
	'''
	@property
	def user_agent(self) :
		try:
			return self._user_agent
		except Exception as e :
			raise e
	'''
	set User Agent String
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
	get Indicator Rule Id
	'''
	@property
	def ind_id(self) :
		try:
			return self._ind_id
		except Exception as e :
			raise e
	'''
	set Indicator Rule Id
	'''
	@ind_id.setter
	def ind_id(self,ind_id):
		try :
			if not isinstance(ind_id,int):
				raise TypeError("ind_id must be set to int value")
			self._ind_id = ind_id
		except Exception as e :
			raise e


	'''
	get Total Requests
	'''
	@property
	def total_requests(self) :
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	set Total Requests
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
	Get the client details of waf violations..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			response=""
			if not resource :
				waf_client_details_obj=waf_client_details()
				response = waf_client_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of waf_client_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			waf_client_details_obj = waf_client_details()
			option_ = options()
			option_._filter=filter_
			return waf_client_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the waf_client_details resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			waf_client_details_obj = waf_client_details()
			option_ = options()
			option_._count=True
			response = waf_client_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of waf_client_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			waf_client_details_obj = waf_client_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = waf_client_details_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(waf_client_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.waf_client_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(waf_client_details_responses, response, "waf_client_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.waf_client_details_response_array
				i=0
				error = [waf_client_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.waf_client_details_response_array
			i=0
			waf_client_details_objs = [waf_client_details() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_waf_client_details'):
					for props in obj._waf_client_details:
						result = service.payload_formatter.string_to_bulk_resource(waf_client_details_response,self.__class__.__name__,props)
						waf_client_details_objs[i] = result.waf_client_details
						i=i+1
			return waf_client_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(waf_client_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class waf_client_details_response(base_response):
	def __init__(self,length=1) :
		self.waf_client_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.waf_client_details= [ waf_client_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class waf_client_details_responses(base_response):
	def __init__(self,length=1) :
		self.waf_client_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.waf_client_details_response_array = [ waf_client_details() for _ in range(length)]
