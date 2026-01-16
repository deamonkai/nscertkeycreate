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
Configuration for MPX/SDX Platform license Expiry Information resource
'''

class platform_license_expiry(base_resource):
	_ip_address= ""
	_host_id= ""
	_expirydays= ""
	_instance_state= ""
	_hostname= ""
	_serialnumber= ""
	__count=""
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
			return "platform_license_expiry"
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
			return "platform_license_expirys"
		except Exception as e :
			raise e



	'''
	get Ip address of the MPX/SDX device
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Ip address of the MPX/SDX device
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
	get Host ID of the device
	'''
	@property
	def host_id(self) :
		try:
			return self._host_id
		except Exception as e :
			raise e
	'''
	set Host ID of the device
	'''
	@host_id.setter
	def host_id(self,host_id):
		try :
			if not isinstance(host_id,str):
				raise TypeError("host_id must be set to str value")
			self._host_id = host_id
		except Exception as e :
			raise e


	'''
	get No of days for license expiry
	'''
	@property
	def expirydays(self) :
		try:
			return self._expirydays
		except Exception as e :
			raise e
	'''
	set No of days for license expiry
	'''
	@expirydays.setter
	def expirydays(self,expirydays):
		try :
			if not isinstance(expirydays,int):
				raise TypeError("expirydays must be set to int value")
			self._expirydays = expirydays
		except Exception as e :
			raise e


	'''
	get State of device, UP only if device accessible
	'''
	@property
	def instance_state(self) :
		try:
			return self._instance_state
		except Exception as e :
			raise e
	'''
	set State of device, UP only if device accessible
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
	get Hostname of the device
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	set Hostname of the device
	'''
	@hostname.setter
	def hostname(self,hostname):
		try :
			if not isinstance(hostname,str):
				raise TypeError("hostname must be set to str value")
			self._hostname = hostname
		except Exception as e :
			raise e


	'''
	get Serial Number of the device
	'''
	@property
	def serialnumber(self) :
		try:
			return self._serialnumber
		except Exception as e :
			raise e
	'''
	set Serial Number of the device
	'''
	@serialnumber.setter
	def serialnumber(self,serialnumber):
		try :
			if not isinstance(serialnumber,str):
				raise TypeError("serialnumber must be set to str value")
			self._serialnumber = serialnumber
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler Console license information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				platform_license_expiry_obj=platform_license_expiry()
				response = platform_license_expiry_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of platform_license_expiry resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			platform_license_expiry_obj = platform_license_expiry()
			option_ = options()
			option_._filter=filter_
			return platform_license_expiry_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the platform_license_expiry resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			platform_license_expiry_obj = platform_license_expiry()
			option_ = options()
			option_._count=True
			response = platform_license_expiry_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of platform_license_expiry resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			platform_license_expiry_obj = platform_license_expiry()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = platform_license_expiry_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(platform_license_expiry_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.platform_license_expiry
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(platform_license_expiry_responses, response, "platform_license_expiry_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.platform_license_expiry_response_array
				i=0
				error = [platform_license_expiry() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.platform_license_expiry_response_array
			i=0
			platform_license_expiry_objs = [platform_license_expiry() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_platform_license_expiry'):
					for props in obj._platform_license_expiry:
						result = service.payload_formatter.string_to_bulk_resource(platform_license_expiry_response,self.__class__.__name__,props)
						platform_license_expiry_objs[i] = result.platform_license_expiry
						i=i+1
			return platform_license_expiry_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(platform_license_expiry,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class platform_license_expiry_response(base_response):
	def __init__(self,length=1) :
		self.platform_license_expiry= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.platform_license_expiry= [ platform_license_expiry() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class platform_license_expiry_responses(base_response):
	def __init__(self,length=1) :
		self.platform_license_expiry_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.platform_license_expiry_response_array = [ platform_license_expiry() for _ in range(length)]
