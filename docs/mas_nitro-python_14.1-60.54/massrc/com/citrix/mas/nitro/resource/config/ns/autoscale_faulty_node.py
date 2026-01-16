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
Configuration for AutoScale Group Cluster State Information resource
'''

class autoscale_faulty_node(base_resource):
	_cluster_ip_address= ""
	_availability_zone= ""
	_id= ""
	_cluster_node_ip_address= ""
	_timestamp= ""
	_asg_id= ""
	_is_delete_allowed= ""
	_cluster_id= ""
	_node_id= ""
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
			return "autoscale_faulty_node"
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
			return "autoscale_faulty_nodes"
		except Exception as e :
			raise e



	'''
	get Cluster IP Address
	'''
	@property
	def cluster_ip_address(self) :
		try:
			return self._cluster_ip_address
		except Exception as e :
			raise e
	'''
	set Cluster IP Address
	'''
	@cluster_ip_address.setter
	def cluster_ip_address(self,cluster_ip_address):
		try :
			if not isinstance(cluster_ip_address,str):
				raise TypeError("cluster_ip_address must be set to str value")
			self._cluster_ip_address = cluster_ip_address
		except Exception as e :
			raise e


	'''
	get availability_zone
	'''
	@property
	def availability_zone(self) :
		try:
			return self._availability_zone
		except Exception as e :
			raise e
	'''
	set availability_zone
	'''
	@availability_zone.setter
	def availability_zone(self,availability_zone):
		try :
			if not isinstance(availability_zone,str):
				raise TypeError("availability_zone must be set to str value")
			self._availability_zone = availability_zone
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the stats
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the stats
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
	get Cluster Node IP Address
	'''
	@property
	def cluster_node_ip_address(self) :
		try:
			return self._cluster_node_ip_address
		except Exception as e :
			raise e
	'''
	set Cluster Node IP Address
	'''
	@cluster_node_ip_address.setter
	def cluster_node_ip_address(self,cluster_node_ip_address):
		try :
			if not isinstance(cluster_node_ip_address,str):
				raise TypeError("cluster_node_ip_address must be set to str value")
			self._cluster_node_ip_address = cluster_node_ip_address
		except Exception as e :
			raise e


	'''
	get timestamp in seconds
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e
	'''
	set timestamp in seconds
	'''
	@timestamp.setter
	def timestamp(self,timestamp):
		try :
			if not isinstance(timestamp,float):
				raise TypeError("timestamp must be set to float value")
			self._timestamp = timestamp
		except Exception as e :
			raise e


	'''
	get Autoscalegroup name to which the cluster is associated
	'''
	@property
	def asg_id(self) :
		try:
			return self._asg_id
		except Exception as e :
			raise e
	'''
	set Autoscalegroup name to which the cluster is associated
	'''
	@asg_id.setter
	def asg_id(self,asg_id):
		try :
			if not isinstance(asg_id,str):
				raise TypeError("asg_id must be set to str value")
			self._asg_id = asg_id
		except Exception as e :
			raise e

	'''
	Deployment status of this node.
	'''
	@property
	def is_delete_allowed(self):
		try:
			return self._is_delete_allowed
		except Exception as e :
			raise e
	'''
	Deployment status of this node.
	'''
	@is_delete_allowed.setter
	def is_delete_allowed(self,is_delete_allowed):
		try :
			if not isinstance(is_delete_allowed,bool):
				raise TypeError("is_delete_allowed must be set to bool value")
			self._is_delete_allowed = is_delete_allowed
		except Exception as e :
			raise e

	'''
	managed device id
	'''
	@property
	def cluster_id(self):
		try:
			return self._cluster_id
		except Exception as e :
			raise e
	'''
	managed device id
	'''
	@cluster_id.setter
	def cluster_id(self,cluster_id):
		try :
			if not isinstance(cluster_id,str):
				raise TypeError("cluster_id must be set to str value")
			self._cluster_id = cluster_id
		except Exception as e :
			raise e

	'''
	managed device id
	'''
	@property
	def node_id(self):
		try:
			return self._node_id
		except Exception as e :
			raise e
	'''
	managed device id
	'''
	@node_id.setter
	def node_id(self,node_id):
		try :
			if not isinstance(node_id,str):
				raise TypeError("node_id must be set to str value")
			self._node_id = node_id
		except Exception as e :
			raise e

	'''
	Use this operation to get all the stats records for all the clusters of autoscale groups.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				autoscale_faulty_node_obj=autoscale_faulty_node()
				response = autoscale_faulty_node_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of autoscale_faulty_node resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			autoscale_faulty_node_obj = autoscale_faulty_node()
			option_ = options()
			option_._filter=filter_
			return autoscale_faulty_node_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the autoscale_faulty_node resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			autoscale_faulty_node_obj = autoscale_faulty_node()
			option_ = options()
			option_._count=True
			response = autoscale_faulty_node_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of autoscale_faulty_node resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			autoscale_faulty_node_obj = autoscale_faulty_node()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = autoscale_faulty_node_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(autoscale_faulty_node_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.autoscale_faulty_node
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(autoscale_faulty_node_responses, response, "autoscale_faulty_node_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.autoscale_faulty_node_response_array
				i=0
				error = [autoscale_faulty_node() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.autoscale_faulty_node_response_array
			i=0
			autoscale_faulty_node_objs = [autoscale_faulty_node() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_autoscale_faulty_node'):
					for props in obj._autoscale_faulty_node:
						result = service.payload_formatter.string_to_bulk_resource(autoscale_faulty_node_response,self.__class__.__name__,props)
						autoscale_faulty_node_objs[i] = result.autoscale_faulty_node
						i=i+1
			return autoscale_faulty_node_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(autoscale_faulty_node,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class autoscale_faulty_node_response(base_response):
	def __init__(self,length=1) :
		self.autoscale_faulty_node= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.autoscale_faulty_node= [ autoscale_faulty_node() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class autoscale_faulty_node_responses(base_response):
	def __init__(self,length=1) :
		self.autoscale_faulty_node_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.autoscale_faulty_node_response_array = [ autoscale_faulty_node() for _ in range(length)]
