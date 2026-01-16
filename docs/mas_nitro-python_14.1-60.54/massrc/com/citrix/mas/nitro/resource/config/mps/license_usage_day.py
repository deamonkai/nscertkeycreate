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

class license_usage_day(base_resource):
	_ip_address= ""
	_id= ""
	_bandwidth_usage= ""
	_total_limit= ""
	_license_usage= ""
	_hostname= ""
	_license_name= ""
	_timeslot= ""
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
			return "license_usage_day"
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
			return "license_usage_days"
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
	get Peak bandwidth usage of the Instance in a day
	'''
	@property
	def bandwidth_usage(self) :
		try:
			return self._bandwidth_usage
		except Exception as e :
			raise e
	'''
	set Peak bandwidth usage of the Instance in a day
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
	get Peak License used by the NetScaler (Bandwidth/vCPU) in a day
	'''
	@property
	def license_usage(self) :
		try:
			return self._license_usage
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
	Use this operation to get NetScaler Usage information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				license_usage_day_obj=license_usage_day()
				response = license_usage_day_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of license_usage_day resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			license_usage_day_obj = license_usage_day()
			option_ = options()
			option_._filter=filter_
			return license_usage_day_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the license_usage_day resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			license_usage_day_obj = license_usage_day()
			option_ = options()
			option_._count=True
			response = license_usage_day_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of license_usage_day resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			license_usage_day_obj = license_usage_day()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = license_usage_day_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(license_usage_day_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.license_usage_day
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(license_usage_day_responses, response, "license_usage_day_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.license_usage_day_response_array
				i=0
				error = [license_usage_day() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.license_usage_day_response_array
			i=0
			license_usage_day_objs = [license_usage_day() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_license_usage_day'):
					for props in obj._license_usage_day:
						result = service.payload_formatter.string_to_bulk_resource(license_usage_day_response,self.__class__.__name__,props)
						license_usage_day_objs[i] = result.license_usage_day
						i=i+1
			return license_usage_day_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(license_usage_day,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class license_usage_day_response(base_response):
	def __init__(self,length=1) :
		self.license_usage_day= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.license_usage_day= [ license_usage_day() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class license_usage_day_responses(base_response):
	def __init__(self,length=1) :
		self.license_usage_day_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.license_usage_day_response_array = [ license_usage_day() for _ in range(length)]
