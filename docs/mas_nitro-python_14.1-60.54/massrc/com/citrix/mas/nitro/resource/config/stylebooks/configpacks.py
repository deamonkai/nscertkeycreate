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
Configuration for Configpack Configuration resource
'''

class configpacks(base_resource):
	_parameters= ""
	_target_devices_json= ""
	_id= ""
	_name= ""
	_job_id= ""
	_config_id= ""
	_namespace= ""
	_version= ""
	_created_datetime= ""
	_targets= ""
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
	 wait for async job to be finished 
	'''
	def wait_for_job(self,client,res):
		from massrc.com.citrix.mas.nitro.resource.config.stylebooks.jobs import jobs
		import time
		try:
			job_id = res[0].job_id
			jobs_obj = jobs()
			jobs_obj.__dict__ = self.__dict__
			jobs_obj.job_id = str(job_id)
			if client._logger:
				client._logger.debug("Waiting for JOB %s to be finished" % (str(job_id)))
			iter = 1
			max_iter = 600
			error_message = [] 
			is_completed = False 
			while iter < max_iter:
				res_j = jobs.get(client, jobs_obj)
				for job_obj in res_j[0]._progress_info:
					if client._logger:
						client._logger.debug("STATUS:" + str(job_obj.status))
					if job_obj["status"] == "failed":
						error_message.append(job_obj["message"])
					if job_obj["is_last"] == "true" or job_obj["is_last"] == True:
						is_completed = True;
						break;
				if len(error_message) > 1:
					message = ",".join([str(str_v) for str_v in error_message])
					raise Exception("Error in operation." + message)
				if is_completed == True:
					return
				time.sleep(1)
				iter = iter + 1
			else:
				raise Exception("Current Job is taking too long time for job:" + str(jobs_obj.job_id))
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
			object_types_list = ["stylebooks","configpacks"]
			object_ids_list = [[self.namespace,self.version,self.name],[self.config_id]]
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
			return "configpacks"
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
			return "configpackss"
		except Exception as e :
			raise e



	'''
	get Parameters used to instantiate the configuration for the stylebook. Please refer to the schema api to view the supported parameters for any stylebook
	'''
	@property
	def parameters(self) :
		try:
			return self._parameters
		except Exception as e :
			raise e
	'''
	set Parameters used to instantiate the configuration for the stylebook. Please refer to the schema api to view the supported parameters for any stylebook
	'''
	@parameters.setter
	def parameters(self,parameters):
		try :
			self._parameters = parameters
		except Exception as e :
			raise e


	'''
	get Target devices that are used to instantiate the StyleBook
	'''
	@property
	def target_devices_json(self) :
		try:
			return self._target_devices_json
		except Exception as e :
			raise e
	'''
	set Target devices that are used to instantiate the StyleBook
	'''
	@target_devices_json.setter
	def target_devices_json(self,target_devices_json):
		try :
			self._target_devices_json = target_devices_json
		except Exception as e :
			raise e


	'''
	get Config ID for the config pack
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Config ID for the config pack
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
	get Config ID for the config pack
	'''
	@property
	def job_id(self) :
		try:
			return self._job_id
		except Exception as e :
			raise e
	'''
	set Config ID for the config pack
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
	get Config ID for the config pack
	'''
	@property
	def config_id(self) :
		try:
			return self._config_id
		except Exception as e :
			raise e
	'''
	set Config ID for the config pack
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
	get Datetime the configuration for a stylebook was created
	'''
	@property
	def created_datetime(self) :
		try:
			return self._created_datetime
		except Exception as e :
			raise e
	'''
	set Datetime the configuration for a stylebook was created
	'''
	@created_datetime.setter
	def created_datetime(self,created_datetime):
		try :
			if not isinstance(created_datetime,str):
				raise TypeError("created_datetime must be set to str value")
			self._created_datetime = created_datetime
		except Exception as e :
			raise e


	'''
	get Target devices that are used to instantiate the StyleBook
	'''
	@property
	def targets(self) :
		try:
			return self._targets
		except Exception as e :
			raise e
	'''
	set Target devices that are used to instantiate the StyleBook
	'''
	@targets.setter
	def targets(self,targets):
		try :
			self._targets = targets
		except Exception as e :
			raise e

	'''
	Use this operation to remove configpack details.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._op_by_primary_key_name = "configpack"
			cls._url_filter = ""
			cls._url_filter = "mode=async"
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			cls._response_params = ["config_id","job_id"]
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				resource.wait_for_job(client,res)
				res[0].config_id = str(res[0].job_id)
				return res
			else :
					configpacks_obj=configpacks()
					return cls.delete_bulk_request(client,resource,configpacks_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify configpack details.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._op_by_primary_key_name = "configpack"
			cls._url_filter = ""
			cls._url_filter = "mode=async"
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			cls._request_params = ["parameters","targets"]
			cls._response_params = ["config_id","job_id"]
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				resource.wait_for_job(client,res)
				res[0].config_id = str(res[0].job_id)
				return res
			else :
				configpacks_obj=configpacks()
				return cls.update_bulk_request(client,resource,configpacks_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get configpack details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			cls._op_by_primary_key_name = "configpack"
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			response=""
			if not resource :
				configpacks_obj=configpacks()
				response = configpacks_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to create configpack details.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._op_by_primary_key_name = "configpack"
			cls._url_filter = ""
			cls._url_filter = "mode=async"
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			cls._request_params = ["parameters","targets"]
			cls._response_params = ["config_id","job_id"]
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				resource.wait_for_job(service,res)
				res[0].config_id = str(res[0].job_id)
				return res
			else : 
				configpacks_obj= configpacks()
				return cls.perform_operation_bulk_request(service,resource,configpacks_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of configpacks resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			cls._request_params = ["parameters","targets"]
			cls._response_params = ["config_id","job_id"]
			configpacks_obj = configpacks()
			option_ = options()
			option_._filter=filter_
			return configpacks_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the configpacks resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			cls._request_params = ["parameters","targets"]
			cls._response_params = ["config_id","job_id"]
			configpacks_obj = configpacks()
			option_ = options()
			option_._count=True
			response = configpacks_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of configpacks resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			cls._request_params = ["parameters","targets"]
			cls._response_params = ["config_id","job_id"]
			configpacks_obj = configpacks()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = configpacks_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(configpacks_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.configpacks
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(configpacks_responses, response, "configpacks_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.configpacks_response_array
				i=0
				error = [configpacks() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.configpacks_response_array
			i=0
			configpacks_objs = [configpacks() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_configpacks'):
					for props in obj._configpacks:
						result = service.payload_formatter.string_to_bulk_resource(configpacks_response,self.__class__.__name__,props)
						configpacks_objs[i] = result.configpacks
						i=i+1
			return configpacks_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(configpacks,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class configpacks_response(base_response):
	def __init__(self,length=1) :
		self.configpacks= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.configpacks= [ configpacks() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class configpacks_responses(base_response):
	def __init__(self,length=1) :
		self.configpacks_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.configpacks_response_array = [ configpacks() for _ in range(length)]
