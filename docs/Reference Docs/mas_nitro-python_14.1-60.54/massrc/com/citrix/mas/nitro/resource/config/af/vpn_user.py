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
Configuration for vpn user report resource
'''

class vpn_user(base_resource):
	_total_bytes= ""
	_total_requests= ""
	_server_ip_address= ""
	_http_resp_status_name= ""
	_operating_system_name= ""
	_device_ip_address= ""
	_rpt_sample_time= ""
	_user_agent_name= ""
	_client_ip_address= ""
	_id= ""
	_name= ""
	___count= ""
	_http_req_method_name= ""
	_max_transaction_time= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "vpn_user"
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
			return "vpn_users"
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
	Total Requests for this device in given sampled timeframe.
	'''
	@property
	def total_requests(self):
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	Total Requests for this device in given sampled timeframe.
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
	vpn user name
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	vpn user name
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
	vpn user name.
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	vpn user name.
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
	Af Report for Device..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vpn_user_obj=vpn_user()
				response = vpn_user_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vpn_user resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vpn_user_obj = vpn_user()
			option_ = options()
			option_._filter=filter_
			return vpn_user_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vpn_user resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vpn_user_obj = vpn_user()
			option_ = options()
			option_._count=True
			response = vpn_user_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vpn_user resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vpn_user_obj = vpn_user()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vpn_user_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(vpn_user_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpn_user
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vpn_user_responses, response, "vpn_user_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vpn_user_response_array
				i=0
				error = [vpn_user() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vpn_user_response_array
			i=0
			vpn_user_objs = [vpn_user() for _ in range(len(response))]
			for obj in response :
				for props in obj._vpn_user:
					result = service.payload_formatter.string_to_bulk_resource(vpn_user_response,self.__class__.__name__,props)
					vpn_user_objs[i] = result.vpn_user
					i=i+1
			return vpn_user_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vpn_user,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vpn_user_response(base_response):
	def __init__(self,length=1) :
		self.vpn_user= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vpn_user= [ vpn_user() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vpn_user_responses(base_response):
	def __init__(self,length=1) :
		self.vpn_user_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vpn_user_response_array = [ vpn_user() for _ in range(length)]
