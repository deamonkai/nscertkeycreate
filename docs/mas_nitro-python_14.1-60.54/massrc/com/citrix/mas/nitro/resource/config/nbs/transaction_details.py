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
Configuration for Application Transaction Details resource
'''

class transaction_details(base_resource):
	_tx_max_bytes= ""
	_rpt_sample_time= ""
	_rx_max_bytes= ""
	_ctnsappname= ""
	_login_successes= ""
	_count_unique_client_ip= ""
	_login_failures= ""
	_ip_address= ""
	_transaction_start_time= ""
	_transaction_end_time= ""
	_total_requests= ""
	_country= ""
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
			return "/macro/v1/security/transaction_details"
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
			return "transaction_details"
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
			return "transaction_detailss"
		except Exception as e :
			raise e



	'''
	get Tx Max Bytes
	'''
	@property
	def tx_max_bytes(self) :
		try:
			return self._tx_max_bytes
		except Exception as e :
			raise e
	'''
	set Tx Max Bytes
	'''
	@tx_max_bytes.setter
	def tx_max_bytes(self,tx_max_bytes):
		try :
			if not isinstance(tx_max_bytes,long):
				raise TypeError("tx_max_bytes must be set to long value")
			self._tx_max_bytes = tx_max_bytes
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
	get Rx Max Bytes
	'''
	@property
	def rx_max_bytes(self) :
		try:
			return self._rx_max_bytes
		except Exception as e :
			raise e
	'''
	set Rx Max Bytes
	'''
	@rx_max_bytes.setter
	def rx_max_bytes(self,rx_max_bytes):
		try :
			if not isinstance(rx_max_bytes,long):
				raise TypeError("rx_max_bytes must be set to long value")
			self._rx_max_bytes = rx_max_bytes
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
	get Login Success
	'''
	@property
	def login_successes(self) :
		try:
			return self._login_successes
		except Exception as e :
			raise e
	'''
	set Login Success
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
	get Client Unique Client IP
	'''
	@property
	def count_unique_client_ip(self) :
		try:
			return self._count_unique_client_ip
		except Exception as e :
			raise e
	'''
	set Client Unique Client IP
	'''
	@count_unique_client_ip.setter
	def count_unique_client_ip(self,count_unique_client_ip):
		try :
			if not isinstance(count_unique_client_ip,long):
				raise TypeError("count_unique_client_ip must be set to long value")
			self._count_unique_client_ip = count_unique_client_ip
		except Exception as e :
			raise e


	'''
	get Login Failure
	'''
	@property
	def login_failures(self) :
		try:
			return self._login_failures
		except Exception as e :
			raise e
	'''
	set Login Failure
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
	get Transaction Start Time
	'''
	@property
	def transaction_start_time(self) :
		try:
			return self._transaction_start_time
		except Exception as e :
			raise e
	'''
	set Transaction Start Time
	'''
	@transaction_start_time.setter
	def transaction_start_time(self,transaction_start_time):
		try :
			if not isinstance(transaction_start_time,long):
				raise TypeError("transaction_start_time must be set to long value")
			self._transaction_start_time = transaction_start_time
		except Exception as e :
			raise e


	'''
	get Transaction End Time
	'''
	@property
	def transaction_end_time(self) :
		try:
			return self._transaction_end_time
		except Exception as e :
			raise e
	'''
	set Transaction End Time
	'''
	@transaction_end_time.setter
	def transaction_end_time(self,transaction_end_time):
		try :
			if not isinstance(transaction_end_time,long):
				raise TypeError("transaction_end_time must be set to long value")
			self._transaction_end_time = transaction_end_time
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
	get Country
	'''
	@property
	def country(self) :
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	set Country
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
	Get the transaction details for the detected anomaly.
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
				transaction_details_obj=transaction_details()
				response = transaction_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of transaction_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			transaction_details_obj = transaction_details()
			option_ = options()
			option_._filter=filter_
			return transaction_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the transaction_details resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			transaction_details_obj = transaction_details()
			option_ = options()
			option_._count=True
			response = transaction_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of transaction_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			transaction_details_obj = transaction_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = transaction_details_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(transaction_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.transaction_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(transaction_details_responses, response, "transaction_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.transaction_details_response_array
				i=0
				error = [transaction_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.transaction_details_response_array
			i=0
			transaction_details_objs = [transaction_details() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_transaction_details'):
					for props in obj._transaction_details:
						result = service.payload_formatter.string_to_bulk_resource(transaction_details_response,self.__class__.__name__,props)
						transaction_details_objs[i] = result.transaction_details
						i=i+1
			return transaction_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(transaction_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class transaction_details_response(base_response):
	def __init__(self,length=1) :
		self.transaction_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.transaction_details= [ transaction_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class transaction_details_responses(base_response):
	def __init__(self,length=1) :
		self.transaction_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.transaction_details_response_array = [ transaction_details() for _ in range(length)]
