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
Configuration for Client URL Details resource
'''

class client_url_details(base_resource):
	_decision_criteria= ""
	_ind_detection_time= ""
	_client_ip_address= ""
	_ctnsappname= ""
	_confidence= ""
	_user_agent= ""
	_ind_id= ""
	_rpt_sample_time= ""
	_ip_address= ""
	_url= ""
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
			return "/macro/v1/security/client_url_details"
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
			return "client_url_details"
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
			return "client_url_detailss"
		except Exception as e :
			raise e



	'''
	get Decision Criteria
	'''
	@property
	def decision_criteria(self) :
		try:
			return self._decision_criteria
		except Exception as e :
			raise e
	'''
	set Decision Criteria
	'''
	@decision_criteria.setter
	def decision_criteria(self,decision_criteria):
		try :
			if not isinstance(decision_criteria,str):
				raise TypeError("decision_criteria must be set to str value")
			self._decision_criteria = decision_criteria
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
	get URL
	'''
	@property
	def url(self) :
		try:
			return self._url
		except Exception as e :
			raise e
	'''
	set URL
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
	Client URL Details.
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
				client_url_details_obj=client_url_details()
				response = client_url_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of client_url_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			client_url_details_obj = client_url_details()
			option_ = options()
			option_._filter=filter_
			return client_url_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the client_url_details resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			client_url_details_obj = client_url_details()
			option_ = options()
			option_._count=True
			response = client_url_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of client_url_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			client_url_details_obj = client_url_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = client_url_details_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(client_url_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.client_url_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(client_url_details_responses, response, "client_url_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.client_url_details_response_array
				i=0
				error = [client_url_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.client_url_details_response_array
			i=0
			client_url_details_objs = [client_url_details() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_client_url_details'):
					for props in obj._client_url_details:
						result = service.payload_formatter.string_to_bulk_resource(client_url_details_response,self.__class__.__name__,props)
						client_url_details_objs[i] = result.client_url_details
						i=i+1
			return client_url_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(client_url_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class client_url_details_response(base_response):
	def __init__(self,length=1) :
		self.client_url_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.client_url_details= [ client_url_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class client_url_details_responses(base_response):
	def __init__(self,length=1) :
		self.client_url_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.client_url_details_response_array = [ client_url_details() for _ in range(length)]
