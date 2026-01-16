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
Configuration for Af report for ICA Device Session hop detail resource
'''

class ica_device_session_hop_detail(af_generic_api):
	_instance_state= ""
	_name= ""
	_ica_user_name= ""
	_id= ""
	_ica_session_id= ""
	_server_latency= ""
	_is_gateway= ""
	___count= ""
	_client_latency= ""
	_license= ""
	_version= ""
	_device_ip_address= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ica_device_session_hop_detail"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ica_device_session_hop_detail,self).get_object_id()
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
			return "ica_device_session_hop_details"
		except Exception as e :
			raise e


	'''
	State of device, UP only if device accessible
	'''
	@property
	def instance_state(self):
		try:
			return self._instance_state
		except Exception as e :
			raise e
	'''
	State of device, UP only if device accessible
	'''
	@instance_state.setter
	def instance_state(self,instance_state):
		try :
			if not isinstance(instance_state,str):
				raise TypeError("instance_state must be set to str value")
			self._instance_state = instance_state
		except Exception as e :
			raise e

	'''
	Name of ICA Device
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Name of ICA Device
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
	Name of ICA User
	'''
	@property
	def ica_user_name(self):
		try:
			return self._ica_user_name
		except Exception as e :
			raise e
	'''
	Name of ICA User
	'''
	@ica_user_name.setter
	def ica_user_name(self,ica_user_name):
		try :
			if not isinstance(ica_user_name,str):
				raise TypeError("ica_user_name must be set to str value")
			self._ica_user_name = ica_user_name
		except Exception as e :
			raise e

	'''
	Id is ICA Device IPAddress
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is ICA Device IPAddress
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
	Id is ICA Session ID
	'''
	@property
	def ica_session_id(self):
		try:
			return self._ica_session_id
		except Exception as e :
			raise e
	'''
	Id is ICA Session ID
	'''
	@ica_session_id.setter
	def ica_session_id(self,ica_session_id):
		try :
			if not isinstance(ica_session_id,str):
				raise TypeError("ica_session_id must be set to str value")
			self._ica_session_id = ica_session_id
		except Exception as e :
			raise e

	'''
	ica session server latency.
	'''
	@property
	def server_latency(self):
		try:
			return self._server_latency
		except Exception as e :
			raise e
	'''
	ica session server latency.
	'''
	@server_latency.setter
	def server_latency(self,server_latency):
		try :
			if not isinstance(server_latency,float):
				raise TypeError("server_latency must be set to float value")
			self._server_latency = server_latency
		except Exception as e :
			raise e

	'''
	Is this device acting as Gateway.
	'''
	@property
	def is_gateway(self):
		try:
			return self._is_gateway
		except Exception as e :
			raise e
	'''
	Is this device acting as Gateway.
	'''
	@is_gateway.setter
	def is_gateway(self,is_gateway):
		try :
			if not isinstance(is_gateway,bool):
				raise TypeError("is_gateway must be set to bool value")
			self._is_gateway = is_gateway
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
	ica session client latency.
	'''
	@property
	def client_latency(self):
		try:
			return self._client_latency
		except Exception as e :
			raise e
	'''
	ica session client latency.
	'''
	@client_latency.setter
	def client_latency(self,client_latency):
		try :
			if not isinstance(client_latency,float):
				raise TypeError("client_latency must be set to float value")
			self._client_latency = client_latency
		except Exception as e :
			raise e

	'''
	Feature License for NetScaler Instance, needs to be set while provisioning (standard, enterprise, platinum)
	'''
	@property
	def license(self):
		try:
			return self._license
		except Exception as e :
			raise e
	'''
	Feature License for NetScaler Instance, needs to be set while provisioning (standard, enterprise, platinum)
	'''
	@license.setter
	def license(self,license):
		try :
			if not isinstance(license,str):
				raise TypeError("license must be set to str value")
			self._license = license
		except Exception as e :
			raise e

	'''
	Device Version
	'''
	@property
	def version(self):
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	Device Version
	'''
	@version.setter
	def version(self,version):
		try :
			if not isinstance(version,str):
				raise TypeError("version must be set to str value")
			self._version = version
		except Exception as e :
			raise e

	'''
	ICA Device IP Address.
	'''
	@property
	def device_ip_address(self):
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	ICA Device IP Address.
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
	Af Report for ICA Device..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ica_device_session_hop_detail_obj=ica_device_session_hop_detail()
				response = ica_device_session_hop_detail_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ica_device_session_hop_detail resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ica_device_session_hop_detail_obj = ica_device_session_hop_detail()
			option_ = options()
			option_._filter=filter_
			return ica_device_session_hop_detail_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ica_device_session_hop_detail resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ica_device_session_hop_detail_obj = ica_device_session_hop_detail()
			option_ = options()
			option_._count=True
			response = ica_device_session_hop_detail_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ica_device_session_hop_detail resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ica_device_session_hop_detail_obj = ica_device_session_hop_detail()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ica_device_session_hop_detail_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ica_device_session_hop_detail_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ica_device_session_hop_detail
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ica_device_session_hop_detail_responses, response, "ica_device_session_hop_detail_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ica_device_session_hop_detail_response_array
				i=0
				error = [ica_device_session_hop_detail() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ica_device_session_hop_detail_response_array
			i=0
			ica_device_session_hop_detail_objs = [ica_device_session_hop_detail() for _ in range(len(response))]
			for obj in response :
				for props in obj._ica_device_session_hop_detail:
					result = service.payload_formatter.string_to_bulk_resource(ica_device_session_hop_detail_response,self.__class__.__name__,props)
					ica_device_session_hop_detail_objs[i] = result.ica_device_session_hop_detail
					i=i+1
			return ica_device_session_hop_detail_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ica_device_session_hop_detail,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ica_device_session_hop_detail_response(base_response):
	def __init__(self,length=1) :
		self.ica_device_session_hop_detail= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ica_device_session_hop_detail= [ ica_device_session_hop_detail() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ica_device_session_hop_detail_responses(base_response):
	def __init__(self,length=1) :
		self.ica_device_session_hop_detail_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ica_device_session_hop_detail_response_array = [ ica_device_session_hop_detail() for _ in range(length)]
