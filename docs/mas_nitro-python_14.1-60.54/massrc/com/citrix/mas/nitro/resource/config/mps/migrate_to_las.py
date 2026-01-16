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
from massrc.com.citrix.mas.nitro.resource.config.mps.ns_for_las import ns_for_las
from massrc.com.citrix.mas.nitro.resource.config.mps.ns_for_las import ns_for_las
from massrc.com.citrix.mas.nitro.resource.config.mps.ns_for_las import ns_for_las
from massrc.com.citrix.mas.nitro.resource.config.mps.ns_for_las import ns_for_las
from massrc.com.citrix.mas.nitro.resource.config.mps.ns_for_las import ns_for_las
from massrc.com.citrix.mas.nitro.resource.config.mps.ns_for_las import ns_for_las


'''
Configuration for get-post migrate to las resource
'''

class migrate_to_las(base_resource):
	_las_licensed_count= ""
	_first_time_las_lic_count= ""
	_las_migration_instances_list=[]
	_ns_require_upgrade_devices=[]
	_las_licensed_list=[]
	_las_migration_completed_instances_count= ""
	_las_eligible_count= ""
	_licensed_dev_list=[]
	_las_migration_applied_instances_count= ""
	_licensed_dev_count= ""
	_first_time_las_lic_devices=[]
	_ns_require_upgrade_count= ""
	_las_eligible_list=[]
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
			return "migrate_to_las"
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
			return "migrate_to_lass"
		except Exception as e :
			raise e


	'''
	Las Licensed Managed Device Count
	'''
	@property
	def las_licensed_count(self):
		try:
			return self._las_licensed_count
		except Exception as e :
			raise e
	'''
	Las Licensed Managed Device Count
	'''
	@las_licensed_count.setter
	def las_licensed_count(self,las_licensed_count):
		try :
			if not isinstance(las_licensed_count,int):
				raise TypeError("las_licensed_count must be set to int value")
			self._las_licensed_count = las_licensed_count
		except Exception as e :
			raise e

	'''
	Count of devices that can be licensed using PUSH model
	'''
	@property
	def first_time_las_lic_count(self):
		try:
			return self._first_time_las_lic_count
		except Exception as e :
			raise e
	'''
	Count of devices that can be licensed using PUSH model
	'''
	@first_time_las_lic_count.setter
	def first_time_las_lic_count(self,first_time_las_lic_count):
		try :
			if not isinstance(first_time_las_lic_count,int):
				raise TypeError("first_time_las_lic_count must be set to int value")
			self._first_time_las_lic_count = first_time_las_lic_count
		except Exception as e :
			raise e

	'''
	Las Migration Device List
	'''
	@property
	def las_migration_instances_list(self) :
		try:
			return self._las_migration_instances_list
		except Exception as e :
			raise e
	'''
	Las Migration Device List
	'''
	@las_migration_instances_list.setter
	def las_migration_instances_list(self,las_migration_instances_list) :
		try :
			if not isinstance(las_migration_instances_list,list):
				raise TypeError("las_migration_instances_list must be set to array of ns_for_las value")
			for item in las_migration_instances_list :
				if not isinstance(item,ns_for_las):
					raise TypeError("item must be set to ns_for_las value")
			self._las_migration_instances_list = las_migration_instances_list
		except Exception as e :
			raise e

	'''
	List of devices that need to be upgraded before LAS
	'''
	@property
	def ns_require_upgrade_devices(self) :
		try:
			return self._ns_require_upgrade_devices
		except Exception as e :
			raise e
	'''
	List of devices that need to be upgraded before LAS
	'''
	@ns_require_upgrade_devices.setter
	def ns_require_upgrade_devices(self,ns_require_upgrade_devices) :
		try :
			if not isinstance(ns_require_upgrade_devices,list):
				raise TypeError("ns_require_upgrade_devices must be set to array of ns_for_las value")
			for item in ns_require_upgrade_devices :
				if not isinstance(item,ns_for_las):
					raise TypeError("item must be set to ns_for_las value")
			self._ns_require_upgrade_devices = ns_require_upgrade_devices
		except Exception as e :
			raise e

	'''
	Las Licensed Managed Device List
	'''
	@property
	def las_licensed_list(self) :
		try:
			return self._las_licensed_list
		except Exception as e :
			raise e
	'''
	Las Licensed Managed Device List
	'''
	@las_licensed_list.setter
	def las_licensed_list(self,las_licensed_list) :
		try :
			if not isinstance(las_licensed_list,list):
				raise TypeError("las_licensed_list must be set to array of ns_for_las value")
			for item in las_licensed_list :
				if not isinstance(item,ns_for_las):
					raise TypeError("item must be set to ns_for_las value")
			self._las_licensed_list = las_licensed_list
		except Exception as e :
			raise e

	'''
	Completed Instances
	'''
	@property
	def las_migration_completed_instances_count(self):
		try:
			return self._las_migration_completed_instances_count
		except Exception as e :
			raise e
	'''
	Completed Instances
	'''
	@las_migration_completed_instances_count.setter
	def las_migration_completed_instances_count(self,las_migration_completed_instances_count):
		try :
			if not isinstance(las_migration_completed_instances_count,int):
				raise TypeError("las_migration_completed_instances_count must be set to int value")
			self._las_migration_completed_instances_count = las_migration_completed_instances_count
		except Exception as e :
			raise e

	'''
	Las Eligible Managed Device Count
	'''
	@property
	def las_eligible_count(self):
		try:
			return self._las_eligible_count
		except Exception as e :
			raise e
	'''
	Las Eligible Managed Device Count
	'''
	@las_eligible_count.setter
	def las_eligible_count(self,las_eligible_count):
		try :
			if not isinstance(las_eligible_count,int):
				raise TypeError("las_eligible_count must be set to int value")
			self._las_eligible_count = las_eligible_count
		except Exception as e :
			raise e

	'''
	License Managed Device List
	'''
	@property
	def licensed_dev_list(self) :
		try:
			return self._licensed_dev_list
		except Exception as e :
			raise e
	'''
	License Managed Device List
	'''
	@licensed_dev_list.setter
	def licensed_dev_list(self,licensed_dev_list) :
		try :
			if not isinstance(licensed_dev_list,list):
				raise TypeError("licensed_dev_list must be set to array of ns_for_las value")
			for item in licensed_dev_list :
				if not isinstance(item,ns_for_las):
					raise TypeError("item must be set to ns_for_las value")
			self._licensed_dev_list = licensed_dev_list
		except Exception as e :
			raise e

	'''
	Total Instances
	'''
	@property
	def las_migration_applied_instances_count(self):
		try:
			return self._las_migration_applied_instances_count
		except Exception as e :
			raise e
	'''
	Total Instances
	'''
	@las_migration_applied_instances_count.setter
	def las_migration_applied_instances_count(self,las_migration_applied_instances_count):
		try :
			if not isinstance(las_migration_applied_instances_count,int):
				raise TypeError("las_migration_applied_instances_count must be set to int value")
			self._las_migration_applied_instances_count = las_migration_applied_instances_count
		except Exception as e :
			raise e

	'''
	License Managed Device Count
	'''
	@property
	def licensed_dev_count(self):
		try:
			return self._licensed_dev_count
		except Exception as e :
			raise e
	'''
	License Managed Device Count
	'''
	@licensed_dev_count.setter
	def licensed_dev_count(self,licensed_dev_count):
		try :
			if not isinstance(licensed_dev_count,int):
				raise TypeError("licensed_dev_count must be set to int value")
			self._licensed_dev_count = licensed_dev_count
		except Exception as e :
			raise e

	'''
	List of devices that can be licensed using PUSH model
	'''
	@property
	def first_time_las_lic_devices(self) :
		try:
			return self._first_time_las_lic_devices
		except Exception as e :
			raise e
	'''
	List of devices that can be licensed using PUSH model
	'''
	@first_time_las_lic_devices.setter
	def first_time_las_lic_devices(self,first_time_las_lic_devices) :
		try :
			if not isinstance(first_time_las_lic_devices,list):
				raise TypeError("first_time_las_lic_devices must be set to array of ns_for_las value")
			for item in first_time_las_lic_devices :
				if not isinstance(item,ns_for_las):
					raise TypeError("item must be set to ns_for_las value")
			self._first_time_las_lic_devices = first_time_las_lic_devices
		except Exception as e :
			raise e

	'''
	Count of devices that need to be upgraded before LAS
	'''
	@property
	def ns_require_upgrade_count(self):
		try:
			return self._ns_require_upgrade_count
		except Exception as e :
			raise e
	'''
	Count of devices that need to be upgraded before LAS
	'''
	@ns_require_upgrade_count.setter
	def ns_require_upgrade_count(self,ns_require_upgrade_count):
		try :
			if not isinstance(ns_require_upgrade_count,int):
				raise TypeError("ns_require_upgrade_count must be set to int value")
			self._ns_require_upgrade_count = ns_require_upgrade_count
		except Exception as e :
			raise e

	'''
	Las Eligible Managed Device List
	'''
	@property
	def las_eligible_list(self) :
		try:
			return self._las_eligible_list
		except Exception as e :
			raise e
	'''
	Las Eligible Managed Device List
	'''
	@las_eligible_list.setter
	def las_eligible_list(self,las_eligible_list) :
		try :
			if not isinstance(las_eligible_list,list):
				raise TypeError("las_eligible_list must be set to array of ns_for_las value")
			for item in las_eligible_list :
				if not isinstance(item,ns_for_las):
					raise TypeError("item must be set to ns_for_las value")
			self._las_eligible_list = las_eligible_list
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(migrate_to_las_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.migrate_to_las
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(migrate_to_las_responses, response, "migrate_to_las_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.migrate_to_las_response_array
				i=0
				error = [migrate_to_las() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.migrate_to_las_response_array
			i=0
			migrate_to_las_objs = [migrate_to_las() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_migrate_to_las'):
					for props in obj._migrate_to_las:
						result = service.payload_formatter.string_to_bulk_resource(migrate_to_las_response,self.__class__.__name__,props)
						migrate_to_las_objs[i] = result.migrate_to_las
						i=i+1
			return migrate_to_las_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(migrate_to_las,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class migrate_to_las_response(base_response):
	def __init__(self,length=1) :
		self.migrate_to_las= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.migrate_to_las= [ migrate_to_las() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class migrate_to_las_responses(base_response):
	def __init__(self,length=1) :
		self.migrate_to_las_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.migrate_to_las_response_array = [ migrate_to_las() for _ in range(length)]
