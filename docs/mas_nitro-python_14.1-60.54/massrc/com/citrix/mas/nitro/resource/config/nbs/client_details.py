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
Configuration for Client Details resource
'''

class client_details(base_resource):
	_response_bytes= ""
	_first_name= ""
	_last_name= ""
	_rpt_sample_time= ""
	_login_failures= ""
	_vsvr_req_rate= ""
	_login_successes= ""
	_ind_detection_time= ""
	_detection_reason= ""
	_ctnsappname= ""
	_confidence= ""
	_ind_id= ""
	_user_agent= ""
	_request_bytes= ""
	_ip_address= ""
	_total_requests= ""
	_vsvr_rspbytes_rate= ""
	_email_address= ""
	_curr_clients= ""
	_client_ip_address= ""
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
			return "/macro/v1/security/client_details"
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
			return "client_details"
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
			return "client_detailss"
		except Exception as e :
			raise e



	'''
	get Response Bytes
	'''
	@property
	def response_bytes(self) :
		try:
			return self._response_bytes
		except Exception as e :
			raise e
	'''
	set Response Bytes
	'''
	@response_bytes.setter
	def response_bytes(self,response_bytes):
		try :
			if not isinstance(response_bytes,long):
				raise TypeError("response_bytes must be set to long value")
			self._response_bytes = response_bytes
		except Exception as e :
			raise e


	'''
	get First Name
	'''
	@property
	def first_name(self) :
		try:
			return self._first_name
		except Exception as e :
			raise e
	'''
	set First Name
	'''
	@first_name.setter
	def first_name(self,first_name):
		try :
			if not isinstance(first_name,str):
				raise TypeError("first_name must be set to str value")
			self._first_name = first_name
		except Exception as e :
			raise e


	'''
	get Last Name
	'''
	@property
	def last_name(self) :
		try:
			return self._last_name
		except Exception as e :
			raise e
	'''
	set Last Name
	'''
	@last_name.setter
	def last_name(self,last_name):
		try :
			if not isinstance(last_name,str):
				raise TypeError("last_name must be set to str value")
			self._last_name = last_name
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
	get Login Failures
	'''
	@property
	def login_failures(self) :
		try:
			return self._login_failures
		except Exception as e :
			raise e
	'''
	set Login Failures
	'''
	@login_failures.setter
	def login_failures(self,login_failures):
		try :
			if not isinstance(login_failures,long):
				raise TypeError("login_failures must be set to long value")
			self._login_failures = login_failures
		except Exception as e :
			raise e


	'''
	get VServer Requeste Rate
	'''
	@property
	def vsvr_req_rate(self) :
		try:
			return self._vsvr_req_rate
		except Exception as e :
			raise e
	'''
	set VServer Requeste Rate
	'''
	@vsvr_req_rate.setter
	def vsvr_req_rate(self,vsvr_req_rate):
		try :
			if not isinstance(vsvr_req_rate,float):
				raise TypeError("vsvr_req_rate must be set to float value")
			self._vsvr_req_rate = vsvr_req_rate
		except Exception as e :
			raise e


	'''
	get Login Successes
	'''
	@property
	def login_successes(self) :
		try:
			return self._login_successes
		except Exception as e :
			raise e
	'''
	set Login Successes
	'''
	@login_successes.setter
	def login_successes(self,login_successes):
		try :
			if not isinstance(login_successes,long):
				raise TypeError("login_successes must be set to long value")
			self._login_successes = login_successes
		except Exception as e :
			raise e


	'''
	get Indicator detection time.
	'''
	@property
	def ind_detection_time(self) :
		try:
			return self._ind_detection_time
		except Exception as e :
			raise e
	'''
	set Indicator detection time.
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
	get Detection Reason
	'''
	@property
	def detection_reason(self) :
		try:
			return self._detection_reason
		except Exception as e :
			raise e
	'''
	set Detection Reason
	'''
	@detection_reason.setter
	def detection_reason(self,detection_reason):
		try :
			if not isinstance(detection_reason,str):
				raise TypeError("detection_reason must be set to str value")
			self._detection_reason = detection_reason
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
	get Confidence
	'''
	@property
	def confidence(self) :
		try:
			return self._confidence
		except Exception as e :
			raise e
	'''
	set Confidence
	'''
	@confidence.setter
	def confidence(self,confidence):
		try :
			if not isinstance(confidence,int):
				raise TypeError("confidence must be set to int value")
			self._confidence = confidence
		except Exception as e :
			raise e


	'''
	get Indicator ID
	'''
	@property
	def ind_id(self) :
		try:
			return self._ind_id
		except Exception as e :
			raise e
	'''
	set Indicator ID
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
	get User Agent
	'''
	@property
	def user_agent(self) :
		try:
			return self._user_agent
		except Exception as e :
			raise e
	'''
	set User Agent
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
	get Request Bytes
	'''
	@property
	def request_bytes(self) :
		try:
			return self._request_bytes
		except Exception as e :
			raise e
	'''
	set Request Bytes
	'''
	@request_bytes.setter
	def request_bytes(self,request_bytes):
		try :
			if not isinstance(request_bytes,long):
				raise TypeError("request_bytes must be set to long value")
			self._request_bytes = request_bytes
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
	get VServer Response Rate
	'''
	@property
	def vsvr_rspbytes_rate(self) :
		try:
			return self._vsvr_rspbytes_rate
		except Exception as e :
			raise e
	'''
	set VServer Response Rate
	'''
	@vsvr_rspbytes_rate.setter
	def vsvr_rspbytes_rate(self,vsvr_rspbytes_rate):
		try :
			if not isinstance(vsvr_rspbytes_rate,float):
				raise TypeError("vsvr_rspbytes_rate must be set to float value")
			self._vsvr_rspbytes_rate = vsvr_rspbytes_rate
		except Exception as e :
			raise e


	'''
	get Email Address
	'''
	@property
	def email_address(self) :
		try:
			return self._email_address
		except Exception as e :
			raise e
	'''
	set Email Address
	'''
	@email_address.setter
	def email_address(self,email_address):
		try :
			if not isinstance(email_address,str):
				raise TypeError("email_address must be set to str value")
			self._email_address = email_address
		except Exception as e :
			raise e


	'''
	get Curr Clients
	'''
	@property
	def curr_clients(self) :
		try:
			return self._curr_clients
		except Exception as e :
			raise e
	'''
	set Curr Clients
	'''
	@curr_clients.setter
	def curr_clients(self,curr_clients):
		try :
			if not isinstance(curr_clients,long):
				raise TypeError("curr_clients must be set to long value")
			self._curr_clients = curr_clients
		except Exception as e :
			raise e


	'''
	get Client IP Address
	'''
	@property
	def client_ip_address(self) :
		try:
			return self._client_ip_address
		except Exception as e :
			raise e
	'''
	set Client IP Address
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
	Client Details.
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
				client_details_obj=client_details()
				response = client_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of client_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			client_details_obj = client_details()
			option_ = options()
			option_._filter=filter_
			return client_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the client_details resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			client_details_obj = client_details()
			option_ = options()
			option_._count=True
			response = client_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of client_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			client_details_obj = client_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = client_details_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(client_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.client_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(client_details_responses, response, "client_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.client_details_response_array
				i=0
				error = [client_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.client_details_response_array
			i=0
			client_details_objs = [client_details() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_client_details'):
					for props in obj._client_details:
						result = service.payload_formatter.string_to_bulk_resource(client_details_response,self.__class__.__name__,props)
						client_details_objs[i] = result.client_details
						i=i+1
			return client_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(client_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class client_details_response(base_response):
	def __init__(self,length=1) :
		self.client_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.client_details= [ client_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class client_details_responses(base_response):
	def __init__(self,length=1) :
		self.client_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.client_details_response_array = [ client_details() for _ in range(length)]
