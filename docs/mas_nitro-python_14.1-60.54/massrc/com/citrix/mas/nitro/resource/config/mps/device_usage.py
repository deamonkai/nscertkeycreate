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
Configuration for NetScaler Usage information resource
'''

class device_usage(base_resource):
	_bandwidth_usage= ""
	_total_limit= ""
	_license_usage= ""
	_timeslot= ""
	_hostname= ""
	_license_name= ""
	_ip_address= ""
	_base_limit= ""
	_id= ""
	_timestamp= ""
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
			return "device_usage"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._id
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
			return "device_usages"
		except Exception as e :
			raise e



	'''
	get bandwidth usage of the Instance
	'''
	@property
	def bandwidth_usage(self) :
		try:
			return self._bandwidth_usage
		except Exception as e :
			raise e
	'''
	set bandwidth usage of the Instance
	'''
	@bandwidth_usage.setter
	def bandwidth_usage(self,bandwidth_usage):
		try :
			if not isinstance(bandwidth_usage,float):
				raise TypeError("bandwidth_usage must be set to float value")
			self._bandwidth_usage = bandwidth_usage
		except Exception as e :
			raise e


	'''
	get Total license limit for the user (including burst)
	'''
	@property
	def total_limit(self) :
		try:
			return self._total_limit
		except Exception as e :
			raise e
	'''
	set Total license limit for the user (including burst)
	'''
	@total_limit.setter
	def total_limit(self,total_limit):
		try :
			if not isinstance(total_limit,int):
				raise TypeError("total_limit must be set to int value")
			self._total_limit = total_limit
		except Exception as e :
			raise e


	'''
	get License used by the NetScaler (Bandwidth/vCPU)
	'''
	@property
	def license_usage(self) :
		try:
			return self._license_usage
		except Exception as e :
			raise e


	'''
	get Device usage information at this timestamp
	'''
	@property
	def timeslot(self) :
		try:
			return self._timeslot
		except Exception as e :
			raise e
	'''
	set Device usage information at this timestamp
	'''
	@timeslot.setter
	def timeslot(self,timeslot):
		try :
			if not isinstance(timeslot,long):
				raise TypeError("timeslot must be set to long value")
			self._timeslot = timeslot
		except Exception as e :
			raise e


	'''
	get Host name of the device
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	set Host name of the device
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
	get License name for the device
	'''
	@property
	def license_name(self) :
		try:
			return self._license_name
		except Exception as e :
			raise e


	'''
	get IP Address of the device
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e


	'''
	get Base limit usage for the user (excluding burst)
	'''
	@property
	def base_limit(self) :
		try:
			return self._base_limit
		except Exception as e :
			raise e
	'''
	set Base limit usage for the user (excluding burst)
	'''
	@base_limit.setter
	def base_limit(self,base_limit):
		try :
			if not isinstance(base_limit,int):
				raise TypeError("base_limit must be set to int value")
			self._base_limit = base_limit
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get Max Device usage information per hour at this timestamp
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e
	'''
	set Max Device usage information per hour at this timestamp
	'''
	@timestamp.setter
	def timestamp(self,timestamp):
		try :
			if not isinstance(timestamp,long):
				raise TypeError("timestamp must be set to long value")
			self._timestamp = timestamp
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler Usage information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				device_usage_obj=device_usage()
				response = device_usage_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of device_usage resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			device_usage_obj = device_usage()
			option_ = options()
			option_._filter=filter_
			return device_usage_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the device_usage resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			device_usage_obj = device_usage()
			option_ = options()
			option_._count=True
			response = device_usage_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of device_usage resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			device_usage_obj = device_usage()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = device_usage_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(device_usage_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_usage
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_usage_responses, response, "device_usage_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_usage_response_array
				i=0
				error = [device_usage() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_usage_response_array
			i=0
			device_usage_objs = [device_usage() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_usage'):
					for props in obj._device_usage:
						result = service.payload_formatter.string_to_bulk_resource(device_usage_response,self.__class__.__name__,props)
						device_usage_objs[i] = result.device_usage
						i=i+1
			return device_usage_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_usage,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_usage_response(base_response):
	def __init__(self,length=1) :
		self.device_usage= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_usage= [ device_usage() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_usage_responses(base_response):
	def __init__(self,length=1) :
		self.device_usage_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_usage_response_array = [ device_usage() for _ in range(length)]
