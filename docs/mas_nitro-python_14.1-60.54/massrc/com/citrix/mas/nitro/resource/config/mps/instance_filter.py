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
Configuration for A Filter of group of instances resource
'''

class instance_filter(base_resource):
	_instances=[]
	_name= ""
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
			return "instance_filter"
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
			return "instance_filters"
		except Exception as e :
			raise e


	'''
	List of instances Names part of filter
	'''
	@property
	def instances(self) :
		try:
			return self._instances
		except Exception as e :
			raise e
	'''
	List of instances Names part of filter
	'''
	@instances.setter
	def instances(self,instances) :
		try :
			if not isinstance(instances,list):
				raise TypeError("instances must be set to array of str value")
			for item in instances :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._instances = instances
		except Exception as e :
			raise e

	'''
	Name of the filter
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Name of the filter
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
	Use this operation to delete filter.
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
					instance_filter_obj=instance_filter()
					return cls.delete_bulk_request(client,resource,instance_filter_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify filter.
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
				instance_filter_obj=instance_filter()
				return cls.update_bulk_request(client,resource,instance_filter_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get filter.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				instance_filter_obj=instance_filter()
				response = instance_filter_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to add filter.
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
				instance_filter_obj= instance_filter()
				return cls.perform_operation_bulk_request(service,resource,instance_filter_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of instance_filter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			instance_filter_obj = instance_filter()
			option_ = options()
			option_._filter=filter_
			return instance_filter_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the instance_filter resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			instance_filter_obj = instance_filter()
			option_ = options()
			option_._count=True
			response = instance_filter_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of instance_filter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			instance_filter_obj = instance_filter()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = instance_filter_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(instance_filter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.instance_filter
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(instance_filter_responses, response, "instance_filter_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.instance_filter_response_array
				i=0
				error = [instance_filter() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.instance_filter_response_array
			i=0
			instance_filter_objs = [instance_filter() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_instance_filter'):
					for props in obj._instance_filter:
						result = service.payload_formatter.string_to_bulk_resource(instance_filter_response,self.__class__.__name__,props)
						instance_filter_objs[i] = result.instance_filter
						i=i+1
			return instance_filter_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(instance_filter,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class instance_filter_response(base_response):
	def __init__(self,length=1) :
		self.instance_filter= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.instance_filter= [ instance_filter() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class instance_filter_responses(base_response):
	def __init__(self,length=1) :
		self.instance_filter_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.instance_filter_response_array = [ instance_filter() for _ in range(length)]
