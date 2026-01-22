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
from massrc.com.citrix.mas.nitro.resource.config.mps.property_map import property_map


'''
Configuration for Dynamic Tasks resource
'''

class dynamic_tasks(base_resource):
	_categories= ""
	_entities_hash= ""
	_weightage= ""
	_content=[]
	_last_modified_time= ""
	_task_name= ""
	_poll_now= ""
	_activity_id= ""
	_categories_array=[]
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
			return "dynamic_tasks"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._task_name
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
			return "dynamic_taskss"
		except Exception as e :
			raise e



	'''
	get Task Category
	'''
	@property
	def categories(self) :
		try:
			return self._categories
		except Exception as e :
			raise e
	'''
	set Task Category
	'''
	@categories.setter
	def categories(self,categories):
		try :
			if not isinstance(categories,str):
				raise TypeError("categories must be set to str value")
			self._categories = categories
		except Exception as e :
			raise e


	'''
	get The string obtained by hashing the entities of the task. Used for managing notification
	'''
	@property
	def entities_hash(self) :
		try:
			return self._entities_hash
		except Exception as e :
			raise e
	'''
	set The string obtained by hashing the entities of the task. Used for managing notification
	'''
	@entities_hash.setter
	def entities_hash(self,entities_hash):
		try :
			if not isinstance(entities_hash,str):
				raise TypeError("entities_hash must be set to str value")
			self._entities_hash = entities_hash
		except Exception as e :
			raise e


	'''
	get Weight of the task
	'''
	@property
	def weightage(self) :
		try:
			return self._weightage
		except Exception as e :
			raise e
	'''
	set Weight of the task
	'''
	@weightage.setter
	def weightage(self,weightage):
		try :
			if not isinstance(weightage,int):
				raise TypeError("weightage must be set to int value")
			self._weightage = weightage
		except Exception as e :
			raise e


	'''
	get List of content in prop_key/prop_value pairs
	'''
	@property
	def content(self) :
		try:
			return self._content
		except Exception as e :
			raise e
	'''
	set List of content in prop_key/prop_value pairs
	'''
	@content.setter
	def content(self,content) :
		try :
			if not isinstance(content,list):
				raise TypeError("content must be set to array of property_map value")
			for item in content :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._content = content
		except Exception as e :
			raise e


	'''
	get Last modified time (epoch time)
	'''
	@property
	def last_modified_time(self) :
		try:
			return self._last_modified_time
		except Exception as e :
			raise e
	'''
	set Last modified time (epoch time)
	'''
	@last_modified_time.setter
	def last_modified_time(self,last_modified_time):
		try :
			if not isinstance(last_modified_time,long):
				raise TypeError("last_modified_time must be set to long value")
			self._last_modified_time = last_modified_time
		except Exception as e :
			raise e


	'''
	get The name of the task
	'''
	@property
	def task_name(self) :
		try:
			return self._task_name
		except Exception as e :
			raise e
	'''
	set The name of the task
	'''
	@task_name.setter
	def task_name(self,task_name):
		try :
			if not isinstance(task_name,str):
				raise TypeError("task_name must be set to str value")
			self._task_name = task_name
		except Exception as e :
			raise e

	'''
	Option to trigger poll now
	'''
	@property
	def poll_now(self):
		try:
			return self._poll_now
		except Exception as e :
			raise e
	'''
	Option to trigger poll now
	'''
	@poll_now.setter
	def poll_now(self,poll_now):
		try :
			if not isinstance(poll_now,bool):
				raise TypeError("poll_now must be set to bool value")
			self._poll_now = poll_now
		except Exception as e :
			raise e

	'''
	Activity ID is used to infrom about the status of polling
	'''
	@property
	def activity_id(self):
		try:
			return self._activity_id
		except Exception as e :
			raise e
	'''
	Activity ID is used to infrom about the status of polling
	'''
	@activity_id.setter
	def activity_id(self,activity_id):
		try :
			if not isinstance(activity_id,str):
				raise TypeError("activity_id must be set to str value")
			self._activity_id = activity_id
		except Exception as e :
			raise e

	'''
	Task Category in array format
	'''
	@property
	def categories_array(self) :
		try:
			return self._categories_array
		except Exception as e :
			raise e
	'''
	Task Category in array format
	'''
	@categories_array.setter
	def categories_array(self,categories_array) :
		try :
			if not isinstance(categories_array,list):
				raise TypeError("categories_array must be set to array of str value")
			for item in categories_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._categories_array = categories_array
		except Exception as e :
			raise e

	'''
	Get the Dynamic Tasks.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				dynamic_tasks_obj=dynamic_tasks()
				response = dynamic_tasks_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of dynamic_tasks resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			dynamic_tasks_obj = dynamic_tasks()
			option_ = options()
			option_._filter=filter_
			return dynamic_tasks_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the dynamic_tasks resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			dynamic_tasks_obj = dynamic_tasks()
			option_ = options()
			option_._count=True
			response = dynamic_tasks_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of dynamic_tasks resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			dynamic_tasks_obj = dynamic_tasks()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = dynamic_tasks_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(dynamic_tasks_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dynamic_tasks
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(dynamic_tasks_responses, response, "dynamic_tasks_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.dynamic_tasks_response_array
				i=0
				error = [dynamic_tasks() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.dynamic_tasks_response_array
			i=0
			dynamic_tasks_objs = [dynamic_tasks() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_dynamic_tasks'):
					for props in obj._dynamic_tasks:
						result = service.payload_formatter.string_to_bulk_resource(dynamic_tasks_response,self.__class__.__name__,props)
						dynamic_tasks_objs[i] = result.dynamic_tasks
						i=i+1
			return dynamic_tasks_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(dynamic_tasks,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class dynamic_tasks_response(base_response):
	def __init__(self,length=1) :
		self.dynamic_tasks= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.dynamic_tasks= [ dynamic_tasks() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class dynamic_tasks_responses(base_response):
	def __init__(self,length=1) :
		self.dynamic_tasks_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.dynamic_tasks_response_array = [ dynamic_tasks() for _ in range(length)]
