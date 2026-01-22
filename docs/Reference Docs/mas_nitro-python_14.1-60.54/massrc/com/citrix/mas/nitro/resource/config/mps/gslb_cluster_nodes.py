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
Configuration for NetScaler nodes participating in GSLB Group Cluster resource
'''

class gslb_cluster_nodes(base_resource):
	_parent_id= ""
	_parent_name= ""
	_device_display_name= ""
	_master_node_index= ""
	_id= ""
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
			return "gslb_cluster_nodes"
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
			return "gslb_cluster_nodess"
		except Exception as e :
			raise e



	'''
	get Parent Id of gslb cluster node
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set Parent Id of gslb cluster node
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get Parent name of gslb cluster node
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set Parent name of gslb cluster node
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get device_display_name of gslb cluster node
	'''
	@property
	def device_display_name(self) :
		try:
			return self._device_display_name
		except Exception as e :
			raise e
	'''
	set device_display_name of gslb cluster node
	'''
	@device_display_name.setter
	def device_display_name(self,device_display_name):
		try :
			if not isinstance(device_display_name,str):
				raise TypeError("device_display_name must be set to str value")
			self._device_display_name = device_display_name
		except Exception as e :
			raise e


	'''
	get Indicates the order of master NetScaler node
	'''
	@property
	def master_node_index(self) :
		try:
			return self._master_node_index
		except Exception as e :
			raise e
	'''
	set Indicates the order of master NetScaler node
	'''
	@master_node_index.setter
	def master_node_index(self,master_node_index):
		try :
			if not isinstance(master_node_index,int):
				raise TypeError("master_node_index must be set to int value")
			self._master_node_index = master_node_index
		except Exception as e :
			raise e


	'''
	get Id is system generated key for the gslb cluster node
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for the gslb cluster node
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
	Use this operation to add GSLB cluster nodes.
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
				gslb_cluster_nodes_obj= gslb_cluster_nodes()
				return cls.perform_operation_bulk_request(service,resource,gslb_cluster_nodes_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get GSLB cluster nodes.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				gslb_cluster_nodes_obj=gslb_cluster_nodes()
				response = gslb_cluster_nodes_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify GSLB cluster nodes.
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
				gslb_cluster_nodes_obj=gslb_cluster_nodes()
				return cls.update_bulk_request(client,resource,gslb_cluster_nodes_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to GSLB cluster nodes.
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
					gslb_cluster_nodes_obj=gslb_cluster_nodes()
					return cls.delete_bulk_request(client,resource,gslb_cluster_nodes_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of gslb_cluster_nodes resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			gslb_cluster_nodes_obj = gslb_cluster_nodes()
			option_ = options()
			option_._filter=filter_
			return gslb_cluster_nodes_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the gslb_cluster_nodes resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			gslb_cluster_nodes_obj = gslb_cluster_nodes()
			option_ = options()
			option_._count=True
			response = gslb_cluster_nodes_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of gslb_cluster_nodes resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			gslb_cluster_nodes_obj = gslb_cluster_nodes()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = gslb_cluster_nodes_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(gslb_cluster_nodes_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslb_cluster_nodes
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(gslb_cluster_nodes_responses, response, "gslb_cluster_nodes_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.gslb_cluster_nodes_response_array
				i=0
				error = [gslb_cluster_nodes() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.gslb_cluster_nodes_response_array
			i=0
			gslb_cluster_nodes_objs = [gslb_cluster_nodes() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_gslb_cluster_nodes'):
					for props in obj._gslb_cluster_nodes:
						result = service.payload_formatter.string_to_bulk_resource(gslb_cluster_nodes_response,self.__class__.__name__,props)
						gslb_cluster_nodes_objs[i] = result.gslb_cluster_nodes
						i=i+1
			return gslb_cluster_nodes_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(gslb_cluster_nodes,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class gslb_cluster_nodes_response(base_response):
	def __init__(self,length=1) :
		self.gslb_cluster_nodes= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.gslb_cluster_nodes= [ gslb_cluster_nodes() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class gslb_cluster_nodes_responses(base_response):
	def __init__(self,length=1) :
		self.gslb_cluster_nodes_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.gslb_cluster_nodes_response_array = [ gslb_cluster_nodes() for _ in range(length)]
