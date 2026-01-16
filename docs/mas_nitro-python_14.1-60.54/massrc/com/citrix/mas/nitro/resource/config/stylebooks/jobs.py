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


import os
import logging
from logging import handlers, Formatter
from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for Jobs resource
'''

class jobs(base_resource):
	_name= ""
	_status= ""
	_version= ""
	_namespace= ""
	_config_id= ""
	_job_id= ""
	__count=""

	'''
	get the api_basepath url
	'''
	def get_api_basepath(self) :
		try:
			return "/stylebook/"
		except Exception as e :
			raise e


	'''
	get the namespace_url
	Multilevel object types and object ids are defined as 
	object_types = [<parent level object type>,<child level object type>]
	object_ids = [<parent object id>,<child object id>]
	An object id is list of current object attributes say ["namespace","version"] then it is
	object_ids = [<parent object id>,<child object id>]
	coverted as object str <namespace value>/<version value>
	'''
	def get_namespace_url(self) :
		try:
			namespace_url = ""
			object_types_list = ["stylebooks","jobs"]
			object_ids_list = [[self.namespace,self.version,self.name],[self.job_id]]
			if not( len(object_types_list) == len(object_ids_list)):
				raise  Exception('Invalid Json definition ,mismatched namespace depth and  object ids '+self.__class__.__name__)
			namespace_depth = len(object_types_list)
			depth_count = 0
			for object_type,object_id  in zip(object_types_list,object_ids_list):
				depth_count = depth_count+1
				object_id_str=""
				if all(object_id):
					object_id_str = "/"+"/".join(str(x) for x in object_id)
					namespace_url = namespace_url + "/" + object_type + object_id_str
				elif depth_count == namespace_depth:
					namespace_url = namespace_url+"/"+object_type
				else:
					raise  Exception('Parent object id is missing '+self.__class__.__name__)
			return namespace_url
		except Exception as e :
			raise e
		except Exception as e :
			raise e

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
			return "jobs"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._name
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
			return "jobss"
		except Exception as e :
			raise e



	'''
	get Name of the StyleBook
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the StyleBook
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
	get Status of the Job
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of the Job
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
	get Version of the StyleBook
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set Version of the StyleBook
	'''
	@version.setter
	def version(self,version):
		try :
			if not isinstance(version,str):
				raise TypeError("version must be set to str value")
			self._version = version
		except Exception as e :
			raise e


	'''
	get Namespace of the StyleBook
	'''
	@property
	def namespace(self) :
		try:
			return self._namespace
		except Exception as e :
			raise e
	'''
	set Namespace of the StyleBook
	'''
	@namespace.setter
	def namespace(self,namespace):
		try :
			if not isinstance(namespace,str):
				raise TypeError("namespace must be set to str value")
			self._namespace = namespace
		except Exception as e :
			raise e


	'''
	get config_id
	'''
	@property
	def config_id(self) :
		try:
			return self._config_id
		except Exception as e :
			raise e
	'''
	set config_id
	'''
	@config_id.setter
	def config_id(self,config_id):
		try :
			if not isinstance(config_id,str):
				raise TypeError("config_id must be set to str value")
			self._config_id = config_id
		except Exception as e :
			raise e


	'''
	get Name of the StyleBook
	'''
	@property
	def job_id(self) :
		try:
			return self._job_id
		except Exception as e :
			raise e
	'''
	set Name of the StyleBook
	'''
	@job_id.setter
	def job_id(self,job_id):
		try :
			if not isinstance(job_id,str):
				raise TypeError("job_id must be set to str value")
			self._job_id = job_id
		except Exception as e :
			raise e

	'''
	Use this operation to get AAA server details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				jobs_obj=jobs()
				response = jobs_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of jobs resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			jobs_obj = jobs()
			option_ = options()
			option_._filter=filter_
			return jobs_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the jobs resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			jobs_obj = jobs()
			option_ = options()
			option_._count=True
			response = jobs_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of jobs resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			jobs_obj = jobs()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = jobs_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(jobs_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.jobs
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(jobs_responses, response, "jobs_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.jobs_response_array
				i=0
				error = [jobs() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.jobs_response_array
			i=0
			jobs_objs = [jobs() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_jobs'):
					for props in obj._jobs:
						result = service.payload_formatter.string_to_bulk_resource(jobs_response,self.__class__.__name__,props)
						jobs_objs[i] = result.jobs
						i=i+1
			return jobs_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(jobs,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class jobs_response(base_response):
	def __init__(self,length=1) :
		self.jobs= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.jobs= [ jobs() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class jobs_responses(base_response):
	def __init__(self,length=1) :
		self.jobs_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.jobs_response_array = [ jobs() for _ in range(length)]
