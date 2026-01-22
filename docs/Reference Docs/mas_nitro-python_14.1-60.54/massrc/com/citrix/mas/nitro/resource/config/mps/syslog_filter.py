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
Configuration for Syslog Suppress Filters resource
'''

class syslog_filter(base_resource):
	_devices= ""
	_name= ""
	_message= ""
	_id= ""
	_severity= ""
	_facilities= ""
	_is_enabled= ""
	_facilities_array=[]
	_devices_array=[]
	_severity_array=[]
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
			return "syslog_filter"
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
			return "syslog_filters"
		except Exception as e :
			raise e



	'''
	get Comma separated string of devices to be suppressed
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e
	'''
	set Comma separated string of devices to be suppressed
	'''
	@devices.setter
	def devices(self,devices):
		try :
			if not isinstance(devices,str):
				raise TypeError("devices must be set to str value")
			self._devices = devices
		except Exception as e :
			raise e


	'''
	get Filter Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Filter Name
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
	get Wildcard substring for syslog message to be suppressed
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e
	'''
	set Wildcard substring for syslog message to be suppressed
	'''
	@message.setter
	def message(self,message):
		try :
			if not isinstance(message,str):
				raise TypeError("message must be set to str value")
			self._message = message
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
	get Comma separated string of severities to be suppressed
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e
	'''
	set Comma separated string of severities to be suppressed
	'''
	@severity.setter
	def severity(self,severity):
		try :
			if not isinstance(severity,str):
				raise TypeError("severity must be set to str value")
			self._severity = severity
		except Exception as e :
			raise e


	'''
	get Comma separated string of facilities to be suppressed
	'''
	@property
	def facilities(self) :
		try:
			return self._facilities
		except Exception as e :
			raise e
	'''
	set Comma separated string of facilities to be suppressed
	'''
	@facilities.setter
	def facilities(self,facilities):
		try :
			if not isinstance(facilities,str):
				raise TypeError("facilities must be set to str value")
			self._facilities = facilities
		except Exception as e :
			raise e


	'''
	get Filter is enabled or disabled
	'''
	@property
	def is_enabled(self) :
		try:
			return self._is_enabled
		except Exception as e :
			raise e
	'''
	set Filter is enabled or disabled
	'''
	@is_enabled.setter
	def is_enabled(self,is_enabled):
		try :
			if not isinstance(is_enabled,bool):
				raise TypeError("is_enabled must be set to bool value")
			self._is_enabled = is_enabled
		except Exception as e :
			raise e

	'''
	Facilities list
	'''
	@property
	def facilities_array(self) :
		try:
			return self._facilities_array
		except Exception as e :
			raise e
	'''
	Facilities list
	'''
	@facilities_array.setter
	def facilities_array(self,facilities_array) :
		try :
			if not isinstance(facilities_array,list):
				raise TypeError("facilities_array must be set to array of str value")
			for item in facilities_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._facilities_array = facilities_array
		except Exception as e :
			raise e

	'''
	Devices list
	'''
	@property
	def devices_array(self) :
		try:
			return self._devices_array
		except Exception as e :
			raise e
	'''
	Devices list
	'''
	@devices_array.setter
	def devices_array(self,devices_array) :
		try :
			if not isinstance(devices_array,list):
				raise TypeError("devices_array must be set to array of str value")
			for item in devices_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._devices_array = devices_array
		except Exception as e :
			raise e

	'''
	Severity list
	'''
	@property
	def severity_array(self) :
		try:
			return self._severity_array
		except Exception as e :
			raise e
	'''
	Severity list
	'''
	@severity_array.setter
	def severity_array(self,severity_array) :
		try :
			if not isinstance(severity_array,list):
				raise TypeError("severity_array must be set to array of str value")
			for item in severity_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._severity_array = severity_array
		except Exception as e :
			raise e

	'''
	Use this operation to add filter.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				return res
			else : 
				syslog_filter_obj= syslog_filter()
				return cls.perform_operation_bulk_request(service,resource,syslog_filter_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get filters.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				syslog_filter_obj=syslog_filter()
				response = syslog_filter_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete filter.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				return res
			else :
					syslog_filter_obj=syslog_filter()
					return cls.delete_bulk_request(client,resource,syslog_filter_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify filter.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				syslog_filter_obj=syslog_filter()
				return cls.update_bulk_request(client,resource,syslog_filter_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of syslog_filter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			syslog_filter_obj = syslog_filter()
			option_ = options()
			option_._filter=filter_
			return syslog_filter_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the syslog_filter resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			syslog_filter_obj = syslog_filter()
			option_ = options()
			option_._count=True
			response = syslog_filter_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of syslog_filter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			syslog_filter_obj = syslog_filter()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = syslog_filter_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(syslog_filter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.syslog_filter
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(syslog_filter_responses, response, "syslog_filter_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.syslog_filter_response_array
				i=0
				error = [syslog_filter() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.syslog_filter_response_array
			i=0
			syslog_filter_objs = [syslog_filter() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_syslog_filter'):
					for props in obj._syslog_filter:
						result = service.payload_formatter.string_to_bulk_resource(syslog_filter_response,self.__class__.__name__,props)
						syslog_filter_objs[i] = result.syslog_filter
						i=i+1
			return syslog_filter_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(syslog_filter,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class syslog_filter_response(base_response):
	def __init__(self,length=1) :
		self.syslog_filter= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.syslog_filter= [ syslog_filter() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class syslog_filter_responses(base_response):
	def __init__(self,length=1) :
		self.syslog_filter_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.syslog_filter_response_array = [ syslog_filter() for _ in range(length)]
