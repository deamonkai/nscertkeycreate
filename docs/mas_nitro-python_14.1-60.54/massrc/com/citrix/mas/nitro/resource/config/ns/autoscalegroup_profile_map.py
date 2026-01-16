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
Configuration for Auto-Scale Group provision details for each availability zone resource
'''

class autoscalegroup_profile_map(base_resource):
	_is_availability_set= ""
	_retry_count= ""
	_azure_resource_group_name= ""
	_provision_profile_id= ""
	_node_id= ""
	_parent_name= ""
	_az_version= ""
	_error_message= ""
	_cluster_ip_address= ""
	_id= ""
	_provision_request_id= ""
	_retry_err_type= ""
	_cluster_id= ""
	_is_active_node_prov= ""
	_activity_id= ""
	_provision_job_id= ""
	_node_count= ""
	_az_type= ""
	_bandwidth_limit= ""
	_parent_id= ""
	_availability_zone= ""
	_autoscalegroup_name= ""
	_delay= ""
	_error_type= ""
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
			return "autoscalegroup_profile_map"
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
			return "autoscalegroup_profile_maps"
		except Exception as e :
			raise e



	'''
	get Azure: If this profile belongs to availability set
	'''
	@property
	def is_availability_set(self) :
		try:
			return self._is_availability_set
		except Exception as e :
			raise e
	'''
	set Azure: If this profile belongs to availability set
	'''
	@is_availability_set.setter
	def is_availability_set(self,is_availability_set):
		try :
			if not isinstance(is_availability_set,bool):
				raise TypeError("is_availability_set must be set to bool value")
			self._is_availability_set = is_availability_set
		except Exception as e :
			raise e


	'''
	get current auto retry count for a retryable error in a cluster.
	'''
	@property
	def retry_count(self) :
		try:
			return self._retry_count
		except Exception as e :
			raise e
	'''
	set current auto retry count for a retryable error in a cluster.
	'''
	@retry_count.setter
	def retry_count(self,retry_count):
		try :
			if not isinstance(retry_count,int):
				raise TypeError("retry_count must be set to int value")
			self._retry_count = retry_count
		except Exception as e :
			raise e


	'''
	get Resource group name for Azure
	'''
	@property
	def azure_resource_group_name(self) :
		try:
			return self._azure_resource_group_name
		except Exception as e :
			raise e
	'''
	set Resource group name for Azure
	'''
	@azure_resource_group_name.setter
	def azure_resource_group_name(self,azure_resource_group_name):
		try :
			if not isinstance(azure_resource_group_name,str):
				raise TypeError("azure_resource_group_name must be set to str value")
			self._azure_resource_group_name = azure_resource_group_name
		except Exception as e :
			raise e


	'''
	get ID of provision profile
	'''
	@property
	def provision_profile_id(self) :
		try:
			return self._provision_profile_id
		except Exception as e :
			raise e
	'''
	set ID of provision profile
	'''
	@provision_profile_id.setter
	def provision_profile_id(self,provision_profile_id):
		try :
			if not isinstance(provision_profile_id,str):
				raise TypeError("provision_profile_id must be set to str value")
			self._provision_profile_id = provision_profile_id
		except Exception as e :
			raise e


	'''
	get The managed_device id which has reference to the node provisioned or to be deprovisioned
	'''
	@property
	def node_id(self) :
		try:
			return self._node_id
		except Exception as e :
			raise e
	'''
	set The managed_device id which has reference to the node provisioned or to be deprovisioned
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
	get Parent name of autoscale group
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set Parent name of autoscale group
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
	get Version of availabilty_zone/cluster. Auto generated.
	'''
	@property
	def az_version(self) :
		try:
			return self._az_version
		except Exception as e :
			raise e
	'''
	set Version of availabilty_zone/cluster. Auto generated.
	'''
	@az_version.setter
	def az_version(self,az_version):
		try :
			if not isinstance(az_version,str):
				raise TypeError("az_version must be set to str value")
			self._az_version = az_version
		except Exception as e :
			raise e


	'''
	get Provision error message
	'''
	@property
	def error_message(self) :
		try:
			return self._error_message
		except Exception as e :
			raise e
	'''
	set Provision error message
	'''
	@error_message.setter
	def error_message(self,error_message):
		try :
			if not isinstance(error_message,str):
				raise TypeError("error_message must be set to str value")
			self._error_message = error_message
		except Exception as e :
			raise e


	'''
	get NetScaler Cluster IP Address
	'''
	@property
	def cluster_ip_address(self) :
		try:
			return self._cluster_ip_address
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the profiles
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the profiles
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
	get The request id generated for provisoning of cluster from provisioning service
	'''
	@property
	def provision_request_id(self) :
		try:
			return self._provision_request_id
		except Exception as e :
			raise e
	'''
	set The request id generated for provisoning of cluster from provisioning service
	'''
	@provision_request_id.setter
	def provision_request_id(self,provision_request_id):
		try :
			if not isinstance(provision_request_id,str):
				raise TypeError("provision_request_id must be set to str value")
			self._provision_request_id = provision_request_id
		except Exception as e :
			raise e


	'''
	get Enable/Disable provisioning retry
	'''
	@property
	def retry_err_type(self) :
		try:
			return self._retry_err_type
		except Exception as e :
			raise e
	'''
	set Enable/Disable provisioning retry
	'''
	@retry_err_type.setter
	def retry_err_type(self,retry_err_type):
		try :
			if not isinstance(retry_err_type,str):
				raise TypeError("retry_err_type must be set to str value")
			self._retry_err_type = retry_err_type
		except Exception as e :
			raise e


	'''
	get NetScaler Cluster ID for the availability zone
	'''
	@property
	def cluster_id(self) :
		try:
			return self._cluster_id
		except Exception as e :
			raise e
	'''
	set NetScaler Cluster ID for the availability zone
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
	get This is to refer if the provisioning inprogress/failed/success is on active/passive node
	'''
	@property
	def is_active_node_prov(self) :
		try:
			return self._is_active_node_prov
		except Exception as e :
			raise e
	'''
	set This is to refer if the provisioning inprogress/failed/success is on active/passive node
	'''
	@is_active_node_prov.setter
	def is_active_node_prov(self,is_active_node_prov):
		try :
			if not isinstance(is_active_node_prov,bool):
				raise TypeError("is_active_node_prov must be set to bool value")
			self._is_active_node_prov = is_active_node_prov
		except Exception as e :
			raise e


	'''
	get Most recent activity_id of this availability_zone/cluster
	'''
	@property
	def activity_id(self) :
		try:
			return self._activity_id
		except Exception as e :
			raise e
	'''
	set Most recent activity_id of this availability_zone/cluster
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
	get The job id generated for provisoning of failed node from provisioning service
	'''
	@property
	def provision_job_id(self) :
		try:
			return self._provision_job_id
		except Exception as e :
			raise e
	'''
	set The job id generated for provisoning of failed node from provisioning service
	'''
	@provision_job_id.setter
	def provision_job_id(self,provision_job_id):
		try :
			if not isinstance(provision_job_id,str):
				raise TypeError("provision_job_id must be set to str value")
			self._provision_job_id = provision_job_id
		except Exception as e :
			raise e


	'''
	get Number of nodes to be provisioned in the cluster
	'''
	@property
	def node_count(self) :
		try:
			return self._node_count
		except Exception as e :
			raise e
	'''
	set Number of nodes to be provisioned in the cluster
	'''
	@node_count.setter
	def node_count(self,node_count):
		try :
			if not isinstance(node_count,int):
				raise TypeError("node_count must be set to int value")
			self._node_count = node_count
		except Exception as e :
			raise e


	'''
	get Type of availabilty_zone/cluster (1.ORIGINAL, 2.BACKUP)
	'''
	@property
	def az_type(self) :
		try:
			return self._az_type
		except Exception as e :
			raise e
	'''
	set Type of availabilty_zone/cluster (1.ORIGINAL, 2.BACKUP)
	'''
	@az_type.setter
	def az_type(self,az_type):
		try :
			if not isinstance(az_type,int):
				raise TypeError("az_type must be set to int value")
			self._az_type = az_type
		except Exception as e :
			raise e


	'''
	get Bandwidth limit per ADC
	'''
	@property
	def bandwidth_limit(self) :
		try:
			return self._bandwidth_limit
		except Exception as e :
			raise e
	'''
	set Bandwidth limit per ADC
	'''
	@bandwidth_limit.setter
	def bandwidth_limit(self,bandwidth_limit):
		try :
			if not isinstance(bandwidth_limit,int):
				raise TypeError("bandwidth_limit must be set to int value")
			self._bandwidth_limit = bandwidth_limit
		except Exception as e :
			raise e


	'''
	get Parent Id of autoscalegroup
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set Parent Id of autoscalegroup
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
	get availability_zone of autoscalegroup
	'''
	@property
	def availability_zone(self) :
		try:
			return self._availability_zone
		except Exception as e :
			raise e
	'''
	set availability_zone of autoscalegroup
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
	Auto-Scale Group Name
	'''
	@property
	def autoscalegroup_name(self):
		try:
			return self._autoscalegroup_name
		except Exception as e :
			raise e
	'''
	Auto-Scale Group Name
	'''
	@autoscalegroup_name.setter
	def autoscalegroup_name(self,autoscalegroup_name):
		try :
			if not isinstance(autoscalegroup_name,str):
				raise TypeError("autoscalegroup_name must be set to str value")
			self._autoscalegroup_name = autoscalegroup_name
		except Exception as e :
			raise e

	'''
	For mock test: Delay in seconds introduced to get the response.
	'''
	@property
	def delay(self):
		try:
			return self._delay
		except Exception as e :
			raise e
	'''
	For mock test: Delay in seconds introduced to get the response.
	'''
	@delay.setter
	def delay(self,delay):
		try :
			if not isinstance(delay,int):
				raise TypeError("delay must be set to int value")
			self._delay = delay
		except Exception as e :
			raise e

	'''
	For mock test: simulates response type. 0-success,1-failed,2-validation failed with no delay
	'''
	@property
	def error_type(self):
		try:
			return self._error_type
		except Exception as e :
			raise e
	'''
	For mock test: simulates response type. 0-success,1-failed,2-validation failed with no delay
	'''
	@error_type.setter
	def error_type(self,error_type):
		try :
			if not isinstance(error_type,int):
				raise TypeError("error_type must be set to int value")
			self._error_type = error_type
		except Exception as e :
			raise e

	'''
	Use this operation to add new availability_zone.
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
				autoscalegroup_profile_map_obj= autoscalegroup_profile_map()
				return cls.perform_operation_bulk_request(service,resource,autoscalegroup_profile_map_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify the properties of availability_zone.
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
				autoscalegroup_profile_map_obj=autoscalegroup_profile_map()
				return cls.update_bulk_request(client,resource,autoscalegroup_profile_map_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete the availability_zone.
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
					autoscalegroup_profile_map_obj=autoscalegroup_profile_map()
					return cls.delete_bulk_request(client,resource,autoscalegroup_profile_map_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get autoscale cluster/availability_zones.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				autoscalegroup_profile_map_obj=autoscalegroup_profile_map()
				response = autoscalegroup_profile_map_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of autoscalegroup_profile_map resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			autoscalegroup_profile_map_obj = autoscalegroup_profile_map()
			option_ = options()
			option_._filter=filter_
			return autoscalegroup_profile_map_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the autoscalegroup_profile_map resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			autoscalegroup_profile_map_obj = autoscalegroup_profile_map()
			option_ = options()
			option_._count=True
			response = autoscalegroup_profile_map_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of autoscalegroup_profile_map resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			autoscalegroup_profile_map_obj = autoscalegroup_profile_map()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = autoscalegroup_profile_map_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(autoscalegroup_profile_map_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.autoscalegroup_profile_map
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(autoscalegroup_profile_map_responses, response, "autoscalegroup_profile_map_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.autoscalegroup_profile_map_response_array
				i=0
				error = [autoscalegroup_profile_map() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.autoscalegroup_profile_map_response_array
			i=0
			autoscalegroup_profile_map_objs = [autoscalegroup_profile_map() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_autoscalegroup_profile_map'):
					for props in obj._autoscalegroup_profile_map:
						result = service.payload_formatter.string_to_bulk_resource(autoscalegroup_profile_map_response,self.__class__.__name__,props)
						autoscalegroup_profile_map_objs[i] = result.autoscalegroup_profile_map
						i=i+1
			return autoscalegroup_profile_map_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(autoscalegroup_profile_map,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class autoscalegroup_profile_map_response(base_response):
	def __init__(self,length=1) :
		self.autoscalegroup_profile_map= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.autoscalegroup_profile_map= [ autoscalegroup_profile_map() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class autoscalegroup_profile_map_responses(base_response):
	def __init__(self,length=1) :
		self.autoscalegroup_profile_map_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.autoscalegroup_profile_map_response_array = [ autoscalegroup_profile_map() for _ in range(length)]
