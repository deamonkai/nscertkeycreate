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
Configuration for NetScaler Usage summary resource
'''

class device_usage_summary(base_resource):
	_license_usage= ""
	_bandwidth_usage= ""
	_id= ""
	_average_bandwidth_usage= ""
	_average_license_usage= ""
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
			return "device_usage_summary"
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
			return "device_usage_summarys"
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
	get Bandwidth usage of the Instance
	'''
	@property
	def bandwidth_usage(self) :
		try:
			return self._bandwidth_usage
		except Exception as e :
			raise e
	'''
	set Bandwidth usage of the Instance
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
	get Average bandwidth usage of the Instance
	'''
	@property
	def average_bandwidth_usage(self) :
		try:
			return self._average_bandwidth_usage
		except Exception as e :
			raise e
	'''
	set Average bandwidth usage of the Instance
	'''
	@average_bandwidth_usage.setter
	def average_bandwidth_usage(self,average_bandwidth_usage):
		try :
			if not isinstance(average_bandwidth_usage,float):
				raise TypeError("average_bandwidth_usage must be set to float value")
			self._average_bandwidth_usage = average_bandwidth_usage
		except Exception as e :
			raise e


	'''
	get Average license usage of the Instance
	'''
	@property
	def average_license_usage(self) :
		try:
			return self._average_license_usage
		except Exception as e :
			raise e
	'''
	set Average license usage of the Instance
	'''
	@average_license_usage.setter
	def average_license_usage(self,average_license_usage):
		try :
			if not isinstance(average_license_usage,float):
				raise TypeError("average_license_usage must be set to float value")
			self._average_license_usage = average_license_usage
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
				device_usage_summary_obj=device_usage_summary()
				response = device_usage_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of device_usage_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			device_usage_summary_obj = device_usage_summary()
			option_ = options()
			option_._filter=filter_
			return device_usage_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the device_usage_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			device_usage_summary_obj = device_usage_summary()
			option_ = options()
			option_._count=True
			response = device_usage_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of device_usage_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			device_usage_summary_obj = device_usage_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = device_usage_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(device_usage_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_usage_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_usage_summary_responses, response, "device_usage_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_usage_summary_response_array
				i=0
				error = [device_usage_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_usage_summary_response_array
			i=0
			device_usage_summary_objs = [device_usage_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_usage_summary'):
					for props in obj._device_usage_summary:
						result = service.payload_formatter.string_to_bulk_resource(device_usage_summary_response,self.__class__.__name__,props)
						device_usage_summary_objs[i] = result.device_usage_summary
						i=i+1
			return device_usage_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_usage_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_usage_summary_response(base_response):
	def __init__(self,length=1) :
		self.device_usage_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_usage_summary= [ device_usage_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_usage_summary_responses(base_response):
	def __init__(self,length=1) :
		self.device_usage_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_usage_summary_response_array = [ device_usage_summary() for _ in range(length)]
