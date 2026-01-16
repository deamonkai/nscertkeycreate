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
Configuration for Instance Group resource
'''

class device_group(base_resource):
	_static_device_list= ""
	_lock_acquire_time= ""
	_tenant_id= ""
	_upgrade_lock= ""
	_maintenance_window_start= ""
	_criteria_type= ""
	_name= ""
	_device_family= ""
	_criteria_condn= ""
	_upgrade_version= ""
	_criteria_value= ""
	_id= ""
	_duration= ""
	_disable_upgrade= ""
	_lock_acquiring_device= ""
	_category= ""
	_static_device_list_arr=[]
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
			return "device_group"
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
			return "device_groups"
		except Exception as e :
			raise e



	'''
	get Devices in the group
	'''
	@property
	def static_device_list(self) :
		try:
			return self._static_device_list
		except Exception as e :
			raise e
	'''
	set Devices in the group
	'''
	@static_device_list.setter
	def static_device_list(self,static_device_list):
		try :
			if not isinstance(static_device_list,str):
				raise TypeError("static_device_list must be set to str value")
			self._static_device_list = static_device_list
		except Exception as e :
			raise e


	'''
	get Upgrade Lock acquiring time
	'''
	@property
	def lock_acquire_time(self) :
		try:
			return self._lock_acquire_time
		except Exception as e :
			raise e
	'''
	set Upgrade Lock acquiring time
	'''
	@lock_acquire_time.setter
	def lock_acquire_time(self,lock_acquire_time):
		try :
			if not isinstance(lock_acquire_time,str):
				raise TypeError("lock_acquire_time must be set to str value")
			self._lock_acquire_time = lock_acquire_time
		except Exception as e :
			raise e


	'''
	get Tenant Id
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Lock to be acquired before upgrading device group
	'''
	@property
	def upgrade_lock(self) :
		try:
			return self._upgrade_lock
		except Exception as e :
			raise e
	'''
	set Lock to be acquired before upgrading device group
	'''
	@upgrade_lock.setter
	def upgrade_lock(self,upgrade_lock):
		try :
			if not isinstance(upgrade_lock,bool):
				raise TypeError("upgrade_lock must be set to bool value")
			self._upgrade_lock = upgrade_lock
		except Exception as e :
			raise e


	'''
	get Maintenance window start time for groups of category upgrade
	'''
	@property
	def maintenance_window_start(self) :
		try:
			return self._maintenance_window_start
		except Exception as e :
			raise e
	'''
	set Maintenance window start time for groups of category upgrade
	'''
	@maintenance_window_start.setter
	def maintenance_window_start(self,maintenance_window_start):
		try :
			if not isinstance(maintenance_window_start,str):
				raise TypeError("maintenance_window_start must be set to str value")
			self._maintenance_window_start = maintenance_window_start
		except Exception as e :
			raise e


	'''
	get Device Group Criteria
	'''
	@property
	def criteria_type(self) :
		try:
			return self._criteria_type
		except Exception as e :
			raise e
	'''
	set Device Group Criteria
	'''
	@criteria_type.setter
	def criteria_type(self,criteria_type):
		try :
			if not isinstance(criteria_type,str):
				raise TypeError("criteria_type must be set to str value")
			self._criteria_type = criteria_type
		except Exception as e :
			raise e


	'''
	get Device Group Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Device Group Name
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
	get Device Family
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device Family
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
		except Exception as e :
			raise e


	'''
	get Tenant
	'''
	@property
	def criteria_condn(self) :
		try:
			return self._criteria_condn
		except Exception as e :
			raise e
	'''
	set Tenant
	'''
	@criteria_condn.setter
	def criteria_condn(self,criteria_condn):
		try :
			if not isinstance(criteria_condn,str):
				raise TypeError("criteria_condn must be set to str value")
			self._criteria_condn = criteria_condn
		except Exception as e :
			raise e


	'''
	get New Available upgrade version for devices
	'''
	@property
	def upgrade_version(self) :
		try:
			return self._upgrade_version
		except Exception as e :
			raise e
	'''
	set New Available upgrade version for devices
	'''
	@upgrade_version.setter
	def upgrade_version(self,upgrade_version):
		try :
			if not isinstance(upgrade_version,str):
				raise TypeError("upgrade_version must be set to str value")
			self._upgrade_version = upgrade_version
		except Exception as e :
			raise e


	'''
	get Criteria Value
	'''
	@property
	def criteria_value(self) :
		try:
			return self._criteria_value
		except Exception as e :
			raise e
	'''
	set Criteria Value
	'''
	@criteria_value.setter
	def criteria_value(self,criteria_value):
		try :
			if not isinstance(criteria_value,str):
				raise TypeError("criteria_value must be set to str value")
			self._criteria_value = criteria_value
		except Exception as e :
			raise e


	'''
	get Id is system generated key for agent registered with NMX Cloud.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for agent registered with NMX Cloud.
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
	get Duration of Maintenance window for groups of category upgrade
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e
	'''
	set Duration of Maintenance window for groups of category upgrade
	'''
	@duration.setter
	def duration(self,duration):
		try :
			if not isinstance(duration,int):
				raise TypeError("duration must be set to int value")
			self._duration = duration
		except Exception as e :
			raise e


	'''
	get Setting to disable agent upgrades
	'''
	@property
	def disable_upgrade(self) :
		try:
			return self._disable_upgrade
		except Exception as e :
			raise e
	'''
	set Setting to disable agent upgrades
	'''
	@disable_upgrade.setter
	def disable_upgrade(self,disable_upgrade):
		try :
			if not isinstance(disable_upgrade,bool):
				raise TypeError("disable_upgrade must be set to bool value")
			self._disable_upgrade = disable_upgrade
		except Exception as e :
			raise e


	'''
	get Upgrade Lock acquiring device
	'''
	@property
	def lock_acquiring_device(self) :
		try:
			return self._lock_acquiring_device
		except Exception as e :
			raise e
	'''
	set Upgrade Lock acquiring device
	'''
	@lock_acquiring_device.setter
	def lock_acquiring_device(self,lock_acquiring_device):
		try :
			if not isinstance(lock_acquiring_device,str):
				raise TypeError("lock_acquiring_device must be set to str value")
			self._lock_acquiring_device = lock_acquiring_device
		except Exception as e :
			raise e


	'''
	get Device group category. Will be default/upgrade.
	'''
	@property
	def category(self) :
		try:
			return self._category
		except Exception as e :
			raise e
	'''
	set Device group category. Will be default/upgrade.
	'''
	@category.setter
	def category(self,category):
		try :
			if not isinstance(category,str):
				raise TypeError("category must be set to str value")
			self._category = category
		except Exception as e :
			raise e

	'''
	Static Device List
	'''
	@property
	def static_device_list_arr(self) :
		try:
			return self._static_device_list_arr
		except Exception as e :
			raise e
	'''
	Static Device List
	'''
	@static_device_list_arr.setter
	def static_device_list_arr(self,static_device_list_arr) :
		try :
			if not isinstance(static_device_list_arr,list):
				raise TypeError("static_device_list_arr must be set to array of str value")
			for item in static_device_list_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._static_device_list_arr = static_device_list_arr
		except Exception as e :
			raise e

	'''
	Use this operation to delete device_group.
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
					device_group_obj=device_group()
					return cls.delete_bulk_request(client,resource,device_group_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify device_group.
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
				device_group_obj=device_group()
				return cls.update_bulk_request(client,resource,device_group_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add device_group.
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
				device_group_obj= device_group()
				return cls.perform_operation_bulk_request(service,resource,device_group_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to device group.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				device_group_obj=device_group()
				response = device_group_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of device_group resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			device_group_obj = device_group()
			option_ = options()
			option_._filter=filter_
			return device_group_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the device_group resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			device_group_obj = device_group()
			option_ = options()
			option_._count=True
			response = device_group_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of device_group resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			device_group_obj = device_group()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = device_group_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(device_group_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_group
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_group_responses, response, "device_group_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_group_response_array
				i=0
				error = [device_group() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_group_response_array
			i=0
			device_group_objs = [device_group() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_group'):
					for props in obj._device_group:
						result = service.payload_formatter.string_to_bulk_resource(device_group_response,self.__class__.__name__,props)
						device_group_objs[i] = result.device_group
						i=i+1
			return device_group_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_group,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_group_response(base_response):
	def __init__(self,length=1) :
		self.device_group= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_group= [ device_group() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_group_responses(base_response):
	def __init__(self,length=1) :
		self.device_group_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_group_response_array = [ device_group() for _ in range(length)]
