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
from massrc.com.citrix.mas.nitro.resource.config.mps.dynamic_tasks_info import dynamic_tasks_info


'''
Configuration for Dynamic Task Notification Message resource
'''

class dynamic_tasks_notification(base_resource):
	_tasks_info=[]
	_total_count= ""
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
			return "dynamic_tasks_notification"
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
			return "dynamic_tasks_notifications"
		except Exception as e :
			raise e



	'''
	get Tasks objects
	'''
	@property
	def tasks_info(self) :
		try:
			return self._tasks_info
		except Exception as e :
			raise e
	'''
	set Tasks objects
	'''
	@tasks_info.setter
	def tasks_info(self,tasks_info) :
		try :
			if not isinstance(tasks_info,list):
				raise TypeError("tasks_info must be set to array of dynamic_tasks_info value")
			for item in tasks_info :
				if not isinstance(item,dynamic_tasks_info):
					raise TypeError("item must be set to dynamic_tasks_info value")
			self._tasks_info = tasks_info
		except Exception as e :
			raise e


	'''
	get total_count
	'''
	@property
	def total_count(self) :
		try:
			return self._total_count
		except Exception as e :
			raise e
	'''
	set total_count
	'''
	@total_count.setter
	def total_count(self,total_count):
		try :
			if not isinstance(total_count,int):
				raise TypeError("total_count must be set to int value")
			self._total_count = total_count
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(dynamic_tasks_notification_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dynamic_tasks_notification
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(dynamic_tasks_notification_responses, response, "dynamic_tasks_notification_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.dynamic_tasks_notification_response_array
				i=0
				error = [dynamic_tasks_notification() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.dynamic_tasks_notification_response_array
			i=0
			dynamic_tasks_notification_objs = [dynamic_tasks_notification() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_dynamic_tasks_notification'):
					for props in obj._dynamic_tasks_notification:
						result = service.payload_formatter.string_to_bulk_resource(dynamic_tasks_notification_response,self.__class__.__name__,props)
						dynamic_tasks_notification_objs[i] = result.dynamic_tasks_notification
						i=i+1
			return dynamic_tasks_notification_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(dynamic_tasks_notification,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class dynamic_tasks_notification_response(base_response):
	def __init__(self,length=1) :
		self.dynamic_tasks_notification= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.dynamic_tasks_notification= [ dynamic_tasks_notification() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class dynamic_tasks_notification_responses(base_response):
	def __init__(self,length=1) :
		self.dynamic_tasks_notification_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.dynamic_tasks_notification_response_array = [ dynamic_tasks_notification() for _ in range(length)]
