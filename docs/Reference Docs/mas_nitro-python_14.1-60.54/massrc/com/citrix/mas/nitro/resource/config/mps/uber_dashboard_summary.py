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
Configuration for Uber Dashboard Summary resource
'''

class uber_dashboard_summary(base_resource):
	_title= ""
	_is_guided= ""
	_task_name= ""
	_last_modified_time= ""
	_id= ""
	_content=[]
	_document_link= ""
	_is_completed= ""
	_is_acknowledged= ""
	_weightage= ""
	_categories= ""
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
			return "uber_dashboard_summary"
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
			return "uber_dashboard_summarys"
		except Exception as e :
			raise e



	'''
	get Task Name
	'''
	@property
	def title(self) :
		try:
			return self._title
		except Exception as e :
			raise e


	'''
	get Guided
	'''
	@property
	def is_guided(self) :
		try:
			return self._is_guided
		except Exception as e :
			raise e
	'''
	set Guided
	'''
	@is_guided.setter
	def is_guided(self,is_guided):
		try :
			if not isinstance(is_guided,bool):
				raise TypeError("is_guided must be set to bool value")
			self._is_guided = is_guided
		except Exception as e :
			raise e


	'''
	get Task Name
	'''
	@property
	def task_name(self) :
		try:
			return self._task_name
		except Exception as e :
			raise e


	'''
	get Last modified time in seconds
	'''
	@property
	def last_modified_time(self) :
		try:
			return self._last_modified_time
		except Exception as e :
			raise e
	'''
	set Last modified time in seconds
	'''
	@last_modified_time.setter
	def last_modified_time(self,last_modified_time):
		try :
			if not isinstance(last_modified_time,float):
				raise TypeError("last_modified_time must be set to float value")
			self._last_modified_time = last_modified_time
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the tasks
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the tasks
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
	get List of content in key/value
	'''
	@property
	def content(self) :
		try:
			return self._content
		except Exception as e :
			raise e
	'''
	set List of content in key/value
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
	get Document Link
	'''
	@property
	def document_link(self) :
		try:
			return self._document_link
		except Exception as e :
			raise e
	'''
	set Document Link
	'''
	@document_link.setter
	def document_link(self,document_link):
		try :
			if not isinstance(document_link,str):
				raise TypeError("document_link must be set to str value")
			self._document_link = document_link
		except Exception as e :
			raise e


	'''
	get completed
	'''
	@property
	def is_completed(self) :
		try:
			return self._is_completed
		except Exception as e :
			raise e
	'''
	set completed
	'''
	@is_completed.setter
	def is_completed(self,is_completed):
		try :
			if not isinstance(is_completed,bool):
				raise TypeError("is_completed must be set to bool value")
			self._is_completed = is_completed
		except Exception as e :
			raise e


	'''
	get Acknowledged
	'''
	@property
	def is_acknowledged(self) :
		try:
			return self._is_acknowledged
		except Exception as e :
			raise e
	'''
	set Acknowledged
	'''
	@is_acknowledged.setter
	def is_acknowledged(self,is_acknowledged):
		try :
			if not isinstance(is_acknowledged,bool):
				raise TypeError("is_acknowledged must be set to bool value")
			self._is_acknowledged = is_acknowledged
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
	Activity ID is used when polled to get the update
	'''
	@property
	def activity_id(self):
		try:
			return self._activity_id
		except Exception as e :
			raise e
	'''
	Activity ID is used when polled to get the update
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
	Use this operation to mark the uber task as guided.
	'''

	'''
	Use this operation to mark the uber task as guided.
	'''
	@classmethod
	def guided(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"guided")
			else : 
				uber_dashboard_summary_obj= uber_dashboard_summary()
				return cls.perform_operation_bulk_request(service,"guided", resource,uber_dashboard_summary_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to mark the uber task as acknowledged.
	'''

	'''
	Use this operation to mark the uber task as acknowledged.
	'''
	@classmethod
	def acknowledged(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"acknowledged")
			else : 
				uber_dashboard_summary_obj= uber_dashboard_summary()
				return cls.perform_operation_bulk_request(service,"acknowledged", resource,uber_dashboard_summary_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to the summary of uber dashboard.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				uber_dashboard_summary_obj=uber_dashboard_summary()
				response = uber_dashboard_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to mark the uber task as completed.
	'''

	'''
	Use this operation to mark the uber task as completed.
	'''
	@classmethod
	def completed(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"completed")
			else : 
				uber_dashboard_summary_obj= uber_dashboard_summary()
				return cls.perform_operation_bulk_request(service,"completed", resource,uber_dashboard_summary_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of uber_dashboard_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			uber_dashboard_summary_obj = uber_dashboard_summary()
			option_ = options()
			option_._filter=filter_
			return uber_dashboard_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the uber_dashboard_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			uber_dashboard_summary_obj = uber_dashboard_summary()
			option_ = options()
			option_._count=True
			response = uber_dashboard_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of uber_dashboard_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			uber_dashboard_summary_obj = uber_dashboard_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = uber_dashboard_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(uber_dashboard_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.uber_dashboard_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(uber_dashboard_summary_responses, response, "uber_dashboard_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.uber_dashboard_summary_response_array
				i=0
				error = [uber_dashboard_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.uber_dashboard_summary_response_array
			i=0
			uber_dashboard_summary_objs = [uber_dashboard_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_uber_dashboard_summary'):
					for props in obj._uber_dashboard_summary:
						result = service.payload_formatter.string_to_bulk_resource(uber_dashboard_summary_response,self.__class__.__name__,props)
						uber_dashboard_summary_objs[i] = result.uber_dashboard_summary
						i=i+1
			return uber_dashboard_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(uber_dashboard_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class uber_dashboard_summary_response(base_response):
	def __init__(self,length=1) :
		self.uber_dashboard_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.uber_dashboard_summary= [ uber_dashboard_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class uber_dashboard_summary_responses(base_response):
	def __init__(self,length=1) :
		self.uber_dashboard_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.uber_dashboard_summary_response_array = [ uber_dashboard_summary() for _ in range(length)]
