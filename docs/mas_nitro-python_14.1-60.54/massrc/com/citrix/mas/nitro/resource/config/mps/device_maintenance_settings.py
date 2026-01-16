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
Configuration for Device maintenance settings resource
'''

class device_maintenance_settings(base_resource):
	_comments= ""
	_active_status= ""
	_to_time= ""
	_last_update_time= ""
	_from_time= ""
	_managed_device_id= ""
	_id= ""
	_created_by= ""
	_created_time= ""
	_managed_device_id_list=[]
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
			return "device_maintenance_settings"
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
			return "device_maintenance_settingss"
		except Exception as e :
			raise e



	'''
	get device specific comment for the device maintenance window setting
	'''
	@property
	def comments(self) :
		try:
			return self._comments
		except Exception as e :
			raise e
	'''
	set device specific comment for the device maintenance window setting
	'''
	@comments.setter
	def comments(self,comments):
		try :
			if not isinstance(comments,str):
				raise TypeError("comments must be set to str value")
			self._comments = comments
		except Exception as e :
			raise e


	'''
	get whether the device is still within the maintenance window or if it has been completed, possible values are scheduled, in-progress, completed
	'''
	@property
	def active_status(self) :
		try:
			return self._active_status
		except Exception as e :
			raise e
	'''
	set whether the device is still within the maintenance window or if it has been completed, possible values are scheduled, in-progress, completed
	'''
	@active_status.setter
	def active_status(self,active_status):
		try :
			if not isinstance(active_status,str):
				raise TypeError("active_status must be set to str value")
			self._active_status = active_status
		except Exception as e :
			raise e


	'''
	get End time of the maintenance window in seconds since the Unix Epoch
	'''
	@property
	def to_time(self) :
		try:
			return self._to_time
		except Exception as e :
			raise e
	'''
	set End time of the maintenance window in seconds since the Unix Epoch
	'''
	@to_time.setter
	def to_time(self,to_time):
		try :
			if not isinstance(to_time,int):
				raise TypeError("to_time must be set to int value")
			self._to_time = to_time
		except Exception as e :
			raise e


	'''
	get Time when the maintenance window setting was last updated in epoch
	'''
	@property
	def last_update_time(self) :
		try:
			return self._last_update_time
		except Exception as e :
			raise e
	'''
	set Time when the maintenance window setting was last updated in epoch
	'''
	@last_update_time.setter
	def last_update_time(self,last_update_time):
		try :
			if not isinstance(last_update_time,int):
				raise TypeError("last_update_time must be set to int value")
			self._last_update_time = last_update_time
		except Exception as e :
			raise e


	'''
	get Start time of the maintenance window in seconds since the Unix Epoch
	'''
	@property
	def from_time(self) :
		try:
			return self._from_time
		except Exception as e :
			raise e
	'''
	set Start time of the maintenance window in seconds since the Unix Epoch
	'''
	@from_time.setter
	def from_time(self,from_time):
		try :
			if not isinstance(from_time,int):
				raise TypeError("from_time must be set to int value")
			self._from_time = from_time
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all entries.
	'''
	@property
	def managed_device_id(self) :
		try:
			return self._managed_device_id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all entries.
	'''
	@managed_device_id.setter
	def managed_device_id(self,managed_device_id):
		try :
			if not isinstance(managed_device_id,str):
				raise TypeError("managed_device_id must be set to str value")
			self._managed_device_id = managed_device_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all entries.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all entries.
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
	get info of user who configured the maintenance window
	'''
	@property
	def created_by(self) :
		try:
			return self._created_by
		except Exception as e :
			raise e
	'''
	set info of user who configured the maintenance window
	'''
	@created_by.setter
	def created_by(self,created_by):
		try :
			if not isinstance(created_by,str):
				raise TypeError("created_by must be set to str value")
			self._created_by = created_by
		except Exception as e :
			raise e


	'''
	get Time when the maintenance window setting was created in epoch
	'''
	@property
	def created_time(self) :
		try:
			return self._created_time
		except Exception as e :
			raise e
	'''
	set Time when the maintenance window setting was created in epoch
	'''
	@created_time.setter
	def created_time(self,created_time):
		try :
			if not isinstance(created_time,int):
				raise TypeError("created_time must be set to int value")
			self._created_time = created_time
		except Exception as e :
			raise e

	'''
	Id is system generated key for all entries.
	'''
	@property
	def managed_device_id_list(self) :
		try:
			return self._managed_device_id_list
		except Exception as e :
			raise e
	'''
	Id is system generated key for all entries.
	'''
	@managed_device_id_list.setter
	def managed_device_id_list(self,managed_device_id_list) :
		try :
			if not isinstance(managed_device_id_list,list):
				raise TypeError("managed_device_id_list must be set to array of str value")
			for item in managed_device_id_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._managed_device_id_list = managed_device_id_list
		except Exception as e :
			raise e

	'''
	Use this operation to delete a maintenance window setting.
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
					device_maintenance_settings_obj=device_maintenance_settings()
					return cls.delete_bulk_request(client,resource,device_maintenance_settings_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify a maintenance window setting.
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
				device_maintenance_settings_obj=device_maintenance_settings()
				return cls.update_bulk_request(client,resource,device_maintenance_settings_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add a maintenance window setting.
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
				device_maintenance_settings_obj= device_maintenance_settings()
				return cls.perform_operation_bulk_request(service,resource,device_maintenance_settings_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get details of a maintenance window setting.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				device_maintenance_settings_obj=device_maintenance_settings()
				response = device_maintenance_settings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of device_maintenance_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			device_maintenance_settings_obj = device_maintenance_settings()
			option_ = options()
			option_._filter=filter_
			return device_maintenance_settings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the device_maintenance_settings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			device_maintenance_settings_obj = device_maintenance_settings()
			option_ = options()
			option_._count=True
			response = device_maintenance_settings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of device_maintenance_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			device_maintenance_settings_obj = device_maintenance_settings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = device_maintenance_settings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(device_maintenance_settings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_maintenance_settings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_maintenance_settings_responses, response, "device_maintenance_settings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_maintenance_settings_response_array
				i=0
				error = [device_maintenance_settings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_maintenance_settings_response_array
			i=0
			device_maintenance_settings_objs = [device_maintenance_settings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_maintenance_settings'):
					for props in obj._device_maintenance_settings:
						result = service.payload_formatter.string_to_bulk_resource(device_maintenance_settings_response,self.__class__.__name__,props)
						device_maintenance_settings_objs[i] = result.device_maintenance_settings
						i=i+1
			return device_maintenance_settings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_maintenance_settings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_maintenance_settings_response(base_response):
	def __init__(self,length=1) :
		self.device_maintenance_settings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_maintenance_settings= [ device_maintenance_settings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_maintenance_settings_responses(base_response):
	def __init__(self,length=1) :
		self.device_maintenance_settings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_maintenance_settings_response_array = [ device_maintenance_settings() for _ in range(length)]
