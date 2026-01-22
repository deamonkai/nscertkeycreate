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
from massrc.com.citrix.mas.nitro.resource.config.mps.gslb_cluster_nodes import gslb_cluster_nodes


'''
Configuration for GSLB Cluster Group resource
'''

class gslb_cluster_group(base_resource):
	_id= ""
	_name= ""
	_is_enabled= ""
	_gslb_cluster_instances=[]
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
			return "gslb_cluster_group"
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
			return "gslb_cluster_groups"
		except Exception as e :
			raise e



	'''
	get Id is system generated key for the GSLB Cluster Group
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for the GSLB Cluster Group
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
	get GSLB Cluster Group Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set GSLB Cluster Group Name
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
	get Status of GSLB Cluster Group (Enable/Disable)
	'''
	@property
	def is_enabled(self) :
		try:
			return self._is_enabled
		except Exception as e :
			raise e
	'''
	set Status of GSLB Cluster Group (Enable/Disable)
	'''
	@is_enabled.setter
	def is_enabled(self,is_enabled):
		try :
			if not isinstance(is_enabled,bool):
				raise TypeError("is_enabled must be set to bool value")
			self._is_enabled = is_enabled
		except Exception as e :
			raise e


	'''
	get GSLB Cluster Nodes
	'''
	@property
	def gslb_cluster_instances(self) :
		try:
			return self._gslb_cluster_instances
		except Exception as e :
			raise e
	'''
	set GSLB Cluster Nodes
	'''
	@gslb_cluster_instances.setter
	def gslb_cluster_instances(self,gslb_cluster_instances) :
		try :
			if not isinstance(gslb_cluster_instances,list):
				raise TypeError("gslb_cluster_instances must be set to array of gslb_cluster_nodes value")
			for item in gslb_cluster_instances :
				if not isinstance(item,gslb_cluster_nodes):
					raise TypeError("item must be set to gslb_cluster_nodes value")
			self._gslb_cluster_instances = gslb_cluster_instances
		except Exception as e :
			raise e

	'''
	Use this operation to delete GSLB Cluster Group.
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
					gslb_cluster_group_obj=gslb_cluster_group()
					return cls.delete_bulk_request(client,resource,gslb_cluster_group_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify GSLB Cluster Group.
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
				gslb_cluster_group_obj=gslb_cluster_group()
				return cls.update_bulk_request(client,resource,gslb_cluster_group_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add GSLB Cluster Group.
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
				gslb_cluster_group_obj= gslb_cluster_group()
				return cls.perform_operation_bulk_request(service,resource,gslb_cluster_group_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get GSLB Cluster Group.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				gslb_cluster_group_obj=gslb_cluster_group()
				response = gslb_cluster_group_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of gslb_cluster_group resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			gslb_cluster_group_obj = gslb_cluster_group()
			option_ = options()
			option_._filter=filter_
			return gslb_cluster_group_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the gslb_cluster_group resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			gslb_cluster_group_obj = gslb_cluster_group()
			option_ = options()
			option_._count=True
			response = gslb_cluster_group_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of gslb_cluster_group resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			gslb_cluster_group_obj = gslb_cluster_group()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = gslb_cluster_group_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(gslb_cluster_group_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslb_cluster_group
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(gslb_cluster_group_responses, response, "gslb_cluster_group_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.gslb_cluster_group_response_array
				i=0
				error = [gslb_cluster_group() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.gslb_cluster_group_response_array
			i=0
			gslb_cluster_group_objs = [gslb_cluster_group() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_gslb_cluster_group'):
					for props in obj._gslb_cluster_group:
						result = service.payload_formatter.string_to_bulk_resource(gslb_cluster_group_response,self.__class__.__name__,props)
						gslb_cluster_group_objs[i] = result.gslb_cluster_group
						i=i+1
			return gslb_cluster_group_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(gslb_cluster_group,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class gslb_cluster_group_response(base_response):
	def __init__(self,length=1) :
		self.gslb_cluster_group= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.gslb_cluster_group= [ gslb_cluster_group() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class gslb_cluster_group_responses(base_response):
	def __init__(self,length=1) :
		self.gslb_cluster_group_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.gslb_cluster_group_response_array = [ gslb_cluster_group() for _ in range(length)]
