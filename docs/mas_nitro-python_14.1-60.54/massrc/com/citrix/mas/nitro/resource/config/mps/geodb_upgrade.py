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
Configuration for GeoDB database upgrade resource
'''

class geodb_upgrade(base_resource):
	_id= ""
	_act_id= ""
	_converted_file_name= ""
	_username= ""
	_provider_format= ""
	_timestamp= ""
	_schedule_time_epoch= ""
	_status= ""
	_file_name= ""
	_is_ipv6= ""
	_message= ""
	_tasklog_id= ""
	_filesize= ""
	_is_file_details= ""
	_device_groups=[]
	_instance_not_started_count= ""
	_instance_pending_count= ""
	_instance_completed_count= ""
	_percent_completed= ""
	_upload_time= ""
	_instance_total_count= ""
	_instance_failed_count= ""
	_devices=[]
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
			return "geodb_upgrade"
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
			return "geodb_upgrades"
		except Exception as e :
			raise e



	'''
	get Unique Id for geodb upgrade process. This is for internal use only, ignore when calling the POST API.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Unique Id for geodb upgrade process. This is for internal use only, ignore when calling the POST API.
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
	get Used to internally store activity Id of the geodb upgrade process
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e


	'''
	get This is used to store the converted file name in NetScaler format
	'''
	@property
	def converted_file_name(self) :
		try:
			return self._converted_file_name
		except Exception as e :
			raise e
	'''
	set This is used to store the converted file name in NetScaler format
	'''
	@converted_file_name.setter
	def converted_file_name(self,converted_file_name):
		try :
			if not isinstance(converted_file_name,str):
				raise TypeError("converted_file_name must be set to str value")
			self._converted_file_name = converted_file_name
		except Exception as e :
			raise e


	'''
	get User Name who is executing the geodb upgrade. This is for internal use only, ignore when calling the POST API.
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e


	'''
	get Geodb upgrade supported provider format maxmind and NetScaler.
	'''
	@property
	def provider_format(self) :
		try:
			return self._provider_format
		except Exception as e :
			raise e
	'''
	set Geodb upgrade supported provider format maxmind and NetScaler.
	'''
	@provider_format.setter
	def provider_format(self,provider_format):
		try :
			if not isinstance(provider_format,str):
				raise TypeError("provider_format must be set to str value")
			self._provider_format = provider_format
		except Exception as e :
			raise e


	'''
	get Time of Creation of geodb upgrade. This is for internal use only, ignore when calling the POST API.
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e


	'''
	get Schedule time UTC epoch (string representation of 11 digit numbers).
	'''
	@property
	def schedule_time_epoch(self) :
		try:
			return self._schedule_time_epoch
		except Exception as e :
			raise e
	'''
	set Schedule time UTC epoch (string representation of 11 digit numbers).
	'''
	@schedule_time_epoch.setter
	def schedule_time_epoch(self,schedule_time_epoch):
		try :
			if not isinstance(schedule_time_epoch,str):
				raise TypeError("schedule_time_epoch must be set to str value")
			self._schedule_time_epoch = schedule_time_epoch
		except Exception as e :
			raise e


	'''
	get Status of Job In-Progress, Completed, Failed, Scheduled 
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of Job In-Progress, Completed, Failed, Scheduled 
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get Geodb file name
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set Geodb file name
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e


	'''
	get True if select ipv6 block file to convert to NetScaler format
	'''
	@property
	def is_ipv6(self) :
		try:
			return self._is_ipv6
		except Exception as e :
			raise e
	'''
	set True if select ipv6 block file to convert to NetScaler format
	'''
	@is_ipv6.setter
	def is_ipv6(self,is_ipv6):
		try :
			if not isinstance(is_ipv6,bool):
				raise TypeError("is_ipv6 must be set to bool value")
			self._is_ipv6 = is_ipv6
		except Exception as e :
			raise e


	'''
	get This is used to show an error message if the upgrade fails
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e
	'''
	set This is used to show an error message if the upgrade fails
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
	get Task Log Id of the geodb upgrade process. This is for internal use only, ignore when calling the POST API.
	'''
	@property
	def tasklog_id(self) :
		try:
			return self._tasklog_id
		except Exception as e :
			raise e

	'''
	Geodb file size in bytes
	'''
	@property
	def filesize(self):
		try:
			return self._filesize
		except Exception as e :
			raise e
	'''
	Geodb file size in bytes
	'''
	@filesize.setter
	def filesize(self,filesize):
		try :
			if not isinstance(filesize,int):
				raise TypeError("filesize must be set to int value")
			self._filesize = filesize
		except Exception as e :
			raise e

	'''
	True if required geodb file details
	'''
	@property
	def is_file_details(self):
		try:
			return self._is_file_details
		except Exception as e :
			raise e
	'''
	True if required geodb file details
	'''
	@is_file_details.setter
	def is_file_details(self,is_file_details):
		try :
			if not isinstance(is_file_details,bool):
				raise TypeError("is_file_details must be set to bool value")
			self._is_file_details = is_file_details
		except Exception as e :
			raise e

	'''
	Device Group Array on which for which job is run
	'''
	@property
	def device_groups(self) :
		try:
			return self._device_groups
		except Exception as e :
			raise e
	'''
	Device Group Array on which for which job is run
	'''
	@device_groups.setter
	def device_groups(self,device_groups) :
		try :
			if not isinstance(device_groups,list):
				raise TypeError("device_groups must be set to array of str value")
			for item in device_groups :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._device_groups = device_groups
		except Exception as e :
			raise e

	'''
	Instances not yet started count
	'''
	@property
	def instance_not_started_count(self):
		try:
			return self._instance_not_started_count
		except Exception as e :
			raise e
	'''
	Instances not yet started count
	'''
	@instance_not_started_count.setter
	def instance_not_started_count(self,instance_not_started_count):
		try :
			if not isinstance(instance_not_started_count,int):
				raise TypeError("instance_not_started_count must be set to int value")
			self._instance_not_started_count = instance_not_started_count
		except Exception as e :
			raise e

	'''
	Instance Pending Count
	'''
	@property
	def instance_pending_count(self):
		try:
			return self._instance_pending_count
		except Exception as e :
			raise e
	'''
	Instance Pending Count
	'''
	@instance_pending_count.setter
	def instance_pending_count(self,instance_pending_count):
		try :
			if not isinstance(instance_pending_count,int):
				raise TypeError("instance_pending_count must be set to int value")
			self._instance_pending_count = instance_pending_count
		except Exception as e :
			raise e

	'''
	Instance Completed Count
	'''
	@property
	def instance_completed_count(self):
		try:
			return self._instance_completed_count
		except Exception as e :
			raise e
	'''
	Instance Completed Count
	'''
	@instance_completed_count.setter
	def instance_completed_count(self,instance_completed_count):
		try :
			if not isinstance(instance_completed_count,int):
				raise TypeError("instance_completed_count must be set to int value")
			self._instance_completed_count = instance_completed_count
		except Exception as e :
			raise e

	'''
	Percentage completed upgrade
	'''
	@property
	def percent_completed(self):
		try:
			return self._percent_completed
		except Exception as e :
			raise e
	'''
	Percentage completed upgrade
	'''
	@percent_completed.setter
	def percent_completed(self,percent_completed):
		try :
			if not isinstance(percent_completed,float):
				raise TypeError("percent_completed must be set to float value")
			self._percent_completed = percent_completed
		except Exception as e :
			raise e

	'''
	Geodb file upload time to appliance
	'''
	@property
	def upload_time(self):
		try:
			return self._upload_time
		except Exception as e :
			raise e
	'''
	Geodb file upload time to appliance
	'''
	@upload_time.setter
	def upload_time(self,upload_time):
		try :
			if not isinstance(upload_time,str):
				raise TypeError("upload_time must be set to str value")
			self._upload_time = upload_time
		except Exception as e :
			raise e

	'''
	Instance Total Count
	'''
	@property
	def instance_total_count(self):
		try:
			return self._instance_total_count
		except Exception as e :
			raise e
	'''
	Instance Total Count
	'''
	@instance_total_count.setter
	def instance_total_count(self,instance_total_count):
		try :
			if not isinstance(instance_total_count,int):
				raise TypeError("instance_total_count must be set to int value")
			self._instance_total_count = instance_total_count
		except Exception as e :
			raise e

	'''
	Instance Failed Count
	'''
	@property
	def instance_failed_count(self):
		try:
			return self._instance_failed_count
		except Exception as e :
			raise e
	'''
	Instance Failed Count
	'''
	@instance_failed_count.setter
	def instance_failed_count(self,instance_failed_count):
		try :
			if not isinstance(instance_failed_count,int):
				raise TypeError("instance_failed_count must be set to int value")
			self._instance_failed_count = instance_failed_count
		except Exception as e :
			raise e

	'''
	Device IP Address Array on which job is run
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e
	'''
	Device IP Address Array on which job is run
	'''
	@devices.setter
	def devices(self,devices) :
		try :
			if not isinstance(devices,list):
				raise TypeError("devices must be set to array of str value")
			for item in devices :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._devices = devices
		except Exception as e :
			raise e

	'''
	Use this operation to delete geodb file.
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
					geodb_upgrade_obj=geodb_upgrade()
					return cls.delete_bulk_request(client,resource,geodb_upgrade_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to update geodb file.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				geodb_upgrade_obj=geodb_upgrade()
				return cls.update_bulk_request(client,resource,geodb_upgrade_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get geodb file.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				geodb_upgrade_obj=geodb_upgrade()
				response = geodb_upgrade_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add geodb file.
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
				geodb_upgrade_obj= geodb_upgrade()
				return cls.perform_operation_bulk_request(service,resource,geodb_upgrade_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of geodb_upgrade resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			geodb_upgrade_obj = geodb_upgrade()
			option_ = options()
			option_._filter=filter_
			return geodb_upgrade_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the geodb_upgrade resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			geodb_upgrade_obj = geodb_upgrade()
			option_ = options()
			option_._count=True
			response = geodb_upgrade_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of geodb_upgrade resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			geodb_upgrade_obj = geodb_upgrade()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = geodb_upgrade_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(geodb_upgrade_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.geodb_upgrade
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(geodb_upgrade_responses, response, "geodb_upgrade_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.geodb_upgrade_response_array
				i=0
				error = [geodb_upgrade() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.geodb_upgrade_response_array
			i=0
			geodb_upgrade_objs = [geodb_upgrade() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_geodb_upgrade'):
					for props in obj._geodb_upgrade:
						result = service.payload_formatter.string_to_bulk_resource(geodb_upgrade_response,self.__class__.__name__,props)
						geodb_upgrade_objs[i] = result.geodb_upgrade
						i=i+1
			return geodb_upgrade_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(geodb_upgrade,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class geodb_upgrade_response(base_response):
	def __init__(self,length=1) :
		self.geodb_upgrade= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.geodb_upgrade= [ geodb_upgrade() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class geodb_upgrade_responses(base_response):
	def __init__(self,length=1) :
		self.geodb_upgrade_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.geodb_upgrade_response_array = [ geodb_upgrade() for _ in range(length)]
