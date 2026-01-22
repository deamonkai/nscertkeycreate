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
Configuration for API used to report the global service graph for multi apps. resource
'''

class global_service_graph_node_edges(base_resource):
	_id= ""
	_destination= ""
	_source_type= ""
	_destination_type= ""
	_source= ""
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
			return "global_service_graph_node_edges"
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
			return "global_service_graph_node_edgess"
		except Exception as e :
			raise e



	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get CS VServer Name
	'''
	@property
	def destination(self) :
		try:
			return self._destination
		except Exception as e :
			raise e
	'''
	set CS VServer Name
	'''
	@destination.setter
	def destination(self,destination):
		try :
			if not isinstance(destination,str):
				raise TypeError("destination must be set to str value")
			self._destination = destination
		except Exception as e :
			raise e


	'''
	get LB VServer Name
	'''
	@property
	def source_type(self) :
		try:
			return self._source_type
		except Exception as e :
			raise e
	'''
	set LB VServer Name
	'''
	@source_type.setter
	def source_type(self,source_type):
		try :
			if not isinstance(source_type,str):
				raise TypeError("source_type must be set to str value")
			self._source_type = source_type
		except Exception as e :
			raise e


	'''
	get Service Name
	'''
	@property
	def destination_type(self) :
		try:
			return self._destination_type
		except Exception as e :
			raise e
	'''
	set Service Name
	'''
	@destination_type.setter
	def destination_type(self,destination_type):
		try :
			if not isinstance(destination_type,str):
				raise TypeError("destination_type must be set to str value")
			self._destination_type = destination_type
		except Exception as e :
			raise e


	'''
	get Source Node
	'''
	@property
	def source(self) :
		try:
			return self._source
		except Exception as e :
			raise e
	'''
	set Source Node
	'''
	@source.setter
	def source(self,source):
		try :
			if not isinstance(source,str):
				raise TypeError("source must be set to str value")
			self._source = source
		except Exception as e :
			raise e

	'''
	Reports the global service graph for multi apps.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				global_service_graph_node_edges_obj=global_service_graph_node_edges()
				response = global_service_graph_node_edges_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of global_service_graph_node_edges resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			global_service_graph_node_edges_obj = global_service_graph_node_edges()
			option_ = options()
			option_._filter=filter_
			return global_service_graph_node_edges_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the global_service_graph_node_edges resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			global_service_graph_node_edges_obj = global_service_graph_node_edges()
			option_ = options()
			option_._count=True
			response = global_service_graph_node_edges_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of global_service_graph_node_edges resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			global_service_graph_node_edges_obj = global_service_graph_node_edges()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = global_service_graph_node_edges_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(global_service_graph_node_edges_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.global_service_graph_node_edges
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(global_service_graph_node_edges_responses, response, "global_service_graph_node_edges_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.global_service_graph_node_edges_response_array
				i=0
				error = [global_service_graph_node_edges() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.global_service_graph_node_edges_response_array
			i=0
			global_service_graph_node_edges_objs = [global_service_graph_node_edges() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_global_service_graph_node_edges'):
					for props in obj._global_service_graph_node_edges:
						result = service.payload_formatter.string_to_bulk_resource(global_service_graph_node_edges_response,self.__class__.__name__,props)
						global_service_graph_node_edges_objs[i] = result.global_service_graph_node_edges
						i=i+1
			return global_service_graph_node_edges_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(global_service_graph_node_edges,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class global_service_graph_node_edges_response(base_response):
	def __init__(self,length=1) :
		self.global_service_graph_node_edges= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.global_service_graph_node_edges= [ global_service_graph_node_edges() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class global_service_graph_node_edges_responses(base_response):
	def __init__(self,length=1) :
		self.global_service_graph_node_edges_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.global_service_graph_node_edges_response_array = [ global_service_graph_node_edges() for _ in range(length)]
