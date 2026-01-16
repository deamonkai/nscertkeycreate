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
Configuration for Af DB Cache enable resource
'''

class db_cache(base_resource):
	_reset= ""
	_enable= ""
	___count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "db_cache"
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
			return "db_caches"
		except Exception as e :
			raise e



	'''
	get DB cache Reset value
	'''
	@property
	def reset(self) :
		try:
			return self._reset
		except Exception as e :
			raise e
	'''
	set DB cache Reset value
	'''
	@reset.setter
	def reset(self,reset):
		try :
			if not isinstance(reset,bool):
				raise TypeError("reset must be set to bool value")
			self._reset = reset
		except Exception as e :
			raise e


	'''
	get DB cache enable value
	'''
	@property
	def enable(self) :
		try:
			return self._enable
		except Exception as e :
			raise e
	'''
	set DB cache enable value
	'''
	@enable.setter
	def enable(self,enable):
		try :
			if not isinstance(enable,bool):
				raise TypeError("enable must be set to bool value")
			self._enable = enable
		except Exception as e :
			raise e


	'''
	get Number of records
	'''
	@property
	def __count(self) :
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	set Number of records
	'''
	@__count.setter
	def __count(self,__count):
		try :
			if not isinstance(__count,float):
				raise TypeError("__count must be set to float value")
			self.___count = __count
		except Exception as e :
			raise e

	'''
	To set the db cache value.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				db_cache_obj=db_cache()
				return cls.update_bulk_request(client,resource,db_cache_obj)
		except Exception as e :
			raise e

	'''
	To set the db cache value.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service)
			else : 
				db_cache_obj= db_cache()
				return cls.perform_operation_bulk_request(service, resource,db_cache_obj)
		except Exception as e :
			raise e

	'''
	To get the db cache value.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				db_cache_obj=db_cache()
				response = db_cache_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of db_cache resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			db_cache_obj = db_cache()
			option_ = options()
			option_._filter=filter_
			return db_cache_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the db_cache resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			db_cache_obj = db_cache()
			option_ = options()
			option_._count=True
			response = db_cache_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of db_cache resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			db_cache_obj = db_cache()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = db_cache_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(db_cache_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.db_cache
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(db_cache_responses, response, "db_cache_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.db_cache_response_array
				i=0
				error = [db_cache() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.db_cache_response_array
			i=0
			db_cache_objs = [db_cache() for _ in range(len(response))]
			for obj in response :
				for props in obj._db_cache:
					result = service.payload_formatter.string_to_bulk_resource(db_cache_response,self.__class__.__name__,props)
					db_cache_objs[i] = result.db_cache
					i=i+1
			return db_cache_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(db_cache,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class db_cache_response(base_response):
	def __init__(self,length=1) :
		self.db_cache= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.db_cache= [ db_cache() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class db_cache_responses(base_response):
	def __init__(self,length=1) :
		self.db_cache_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.db_cache_response_array = [ db_cache() for _ in range(length)]
