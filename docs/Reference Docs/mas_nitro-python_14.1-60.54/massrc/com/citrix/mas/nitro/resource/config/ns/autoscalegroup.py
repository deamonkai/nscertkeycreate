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
from massrc.com.citrix.mas.nitro.resource.config.ns.autoscalegroup_profile_map import autoscalegroup_profile_map
from massrc.com.citrix.mas.nitro.resource.config.mps.property_map import property_map


'''
Configuration for Autoscale Group details resource
'''

class autoscalegroup(base_resource):
	_cool_down_period= ""
	_drain_connection_timeout= ""
	_agent_id= ""
	_throughput_max= ""
	_access_profile_id= ""
	_cloud_type= ""
	_cpu_min= ""
	_mem_threshold_enabled= ""
	_ttl_timeout= ""
	_activity_id= ""
	_max_node= ""
	_provision_profile_map=[]
	_throughput_min= ""
	_cpu_threshold_enabled= ""
	_min_node= ""
	_auto_retry_interval= ""
	_is_autoupgrade_enabled= ""
	_mode= ""
	_site_id= ""
	_throughput_threshold_enabled= ""
	_memory_min= ""
	_cpu_max= ""
	_auto_retry_count= ""
	_no_of_cold_nodes= ""
	_name= ""
	_watch_time= ""
	_status= ""
	_enable_cold_node= ""
	_id= ""
	_memory_max= ""
	_tags=[]
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
			return "autoscalegroup"
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
			return "autoscalegroups"
		except Exception as e :
			raise e



	'''
	get Cool Down Period (Waiting time in minutes after triggering scale up/down before initiating next provisioning/de-provisioing
	'''
	@property
	def cool_down_period(self) :
		try:
			return self._cool_down_period
		except Exception as e :
			raise e
	'''
	set Cool Down Period (Waiting time in minutes after triggering scale up/down before initiating next provisioning/de-provisioing
	'''
	@cool_down_period.setter
	def cool_down_period(self,cool_down_period):
		try :
			if not isinstance(cool_down_period,int):
				raise TypeError("cool_down_period must be set to int value")
			self._cool_down_period = cool_down_period
		except Exception as e :
			raise e


	'''
	get Drain Connection Timeout in minutes
	'''
	@property
	def drain_connection_timeout(self) :
		try:
			return self._drain_connection_timeout
		except Exception as e :
			raise e
	'''
	set Drain Connection Timeout in minutes
	'''
	@drain_connection_timeout.setter
	def drain_connection_timeout(self,drain_connection_timeout):
		try :
			if not isinstance(drain_connection_timeout,int):
				raise TypeError("drain_connection_timeout must be set to int value")
			self._drain_connection_timeout = drain_connection_timeout
		except Exception as e :
			raise e


	'''
	get The ID of Agent
	'''
	@property
	def agent_id(self) :
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	set The ID of Agent
	'''
	@agent_id.setter
	def agent_id(self,agent_id):
		try :
			if not isinstance(agent_id,str):
				raise TypeError("agent_id must be set to str value")
			self._agent_id = agent_id
		except Exception as e :
			raise e


	'''
	get Maximum Throughput Threshold Limit
	'''
	@property
	def throughput_max(self) :
		try:
			return self._throughput_max
		except Exception as e :
			raise e
	'''
	set Maximum Throughput Threshold Limit
	'''
	@throughput_max.setter
	def throughput_max(self,throughput_max):
		try :
			if not isinstance(throughput_max,float):
				raise TypeError("throughput_max must be set to float value")
			self._throughput_max = throughput_max
		except Exception as e :
			raise e


	'''
	get The access profile id
	'''
	@property
	def access_profile_id(self) :
		try:
			return self._access_profile_id
		except Exception as e :
			raise e
	'''
	set The access profile id
	'''
	@access_profile_id.setter
	def access_profile_id(self,access_profile_id):
		try :
			if not isinstance(access_profile_id,str):
				raise TypeError("access_profile_id must be set to str value")
			self._access_profile_id = access_profile_id
		except Exception as e :
			raise e


	'''
	get Type of cloud (AWS/Azure)
	'''
	@property
	def cloud_type(self) :
		try:
			return self._cloud_type
		except Exception as e :
			raise e
	'''
	set Type of cloud (AWS/Azure)
	'''
	@cloud_type.setter
	def cloud_type(self,cloud_type):
		try :
			if not isinstance(cloud_type,str):
				raise TypeError("cloud_type must be set to str value")
			self._cloud_type = cloud_type
		except Exception as e :
			raise e


	'''
	get Minimum CPU Threshold Limit
	'''
	@property
	def cpu_min(self) :
		try:
			return self._cpu_min
		except Exception as e :
			raise e
	'''
	set Minimum CPU Threshold Limit
	'''
	@cpu_min.setter
	def cpu_min(self,cpu_min):
		try :
			if not isinstance(cpu_min,float):
				raise TypeError("cpu_min must be set to float value")
			self._cpu_min = cpu_min
		except Exception as e :
			raise e


	'''
	get Status of Memory Threshold Config
	'''
	@property
	def mem_threshold_enabled(self) :
		try:
			return self._mem_threshold_enabled
		except Exception as e :
			raise e
	'''
	set Status of Memory Threshold Config
	'''
	@mem_threshold_enabled.setter
	def mem_threshold_enabled(self,mem_threshold_enabled):
		try :
			if not isinstance(mem_threshold_enabled,bool):
				raise TypeError("mem_threshold_enabled must be set to bool value")
			self._mem_threshold_enabled = mem_threshold_enabled
		except Exception as e :
			raise e


	'''
	get TTL Timeout in seconds
	'''
	@property
	def ttl_timeout(self) :
		try:
			return self._ttl_timeout
		except Exception as e :
			raise e
	'''
	set TTL Timeout in seconds
	'''
	@ttl_timeout.setter
	def ttl_timeout(self,ttl_timeout):
		try :
			if not isinstance(ttl_timeout,int):
				raise TypeError("ttl_timeout must be set to int value")
			self._ttl_timeout = ttl_timeout
		except Exception as e :
			raise e


	'''
	get Most recent activity_id of this autoscalegroup
	'''
	@property
	def activity_id(self) :
		try:
			return self._activity_id
		except Exception as e :
			raise e
	'''
	set Most recent activity_id of this autoscalegroup
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
	get Maximum number of nodes
	'''
	@property
	def max_node(self) :
		try:
			return self._max_node
		except Exception as e :
			raise e
	'''
	set Maximum number of nodes
	'''
	@max_node.setter
	def max_node(self,max_node):
		try :
			if not isinstance(max_node,int):
				raise TypeError("max_node must be set to int value")
			self._max_node = max_node
		except Exception as e :
			raise e


	'''
	get Provision profile map for Availability Zone
	'''
	@property
	def provision_profile_map(self) :
		try:
			return self._provision_profile_map
		except Exception as e :
			raise e
	'''
	set Provision profile map for Availability Zone
	'''
	@provision_profile_map.setter
	def provision_profile_map(self,provision_profile_map) :
		try :
			if not isinstance(provision_profile_map,list):
				raise TypeError("provision_profile_map must be set to array of autoscalegroup_profile_map value")
			for item in provision_profile_map :
				if not isinstance(item,autoscalegroup_profile_map):
					raise TypeError("item must be set to autoscalegroup_profile_map value")
			self._provision_profile_map = provision_profile_map
		except Exception as e :
			raise e


	'''
	get Minimum Throughput Threshold Limit
	'''
	@property
	def throughput_min(self) :
		try:
			return self._throughput_min
		except Exception as e :
			raise e
	'''
	set Minimum Throughput Threshold Limit
	'''
	@throughput_min.setter
	def throughput_min(self,throughput_min):
		try :
			if not isinstance(throughput_min,float):
				raise TypeError("throughput_min must be set to float value")
			self._throughput_min = throughput_min
		except Exception as e :
			raise e


	'''
	get Status of CPU Threshold Config
	'''
	@property
	def cpu_threshold_enabled(self) :
		try:
			return self._cpu_threshold_enabled
		except Exception as e :
			raise e
	'''
	set Status of CPU Threshold Config
	'''
	@cpu_threshold_enabled.setter
	def cpu_threshold_enabled(self,cpu_threshold_enabled):
		try :
			if not isinstance(cpu_threshold_enabled,bool):
				raise TypeError("cpu_threshold_enabled must be set to bool value")
			self._cpu_threshold_enabled = cpu_threshold_enabled
		except Exception as e :
			raise e


	'''
	get Minimum number of nodes
	'''
	@property
	def min_node(self) :
		try:
			return self._min_node
		except Exception as e :
			raise e
	'''
	set Minimum number of nodes
	'''
	@min_node.setter
	def min_node(self,min_node):
		try :
			if not isinstance(min_node,int):
				raise TypeError("min_node must be set to int value")
			self._min_node = min_node
		except Exception as e :
			raise e


	'''
	get Delay between two auto retries in minutes.
	'''
	@property
	def auto_retry_interval(self) :
		try:
			return self._auto_retry_interval
		except Exception as e :
			raise e
	'''
	set Delay between two auto retries in minutes.
	'''
	@auto_retry_interval.setter
	def auto_retry_interval(self,auto_retry_interval):
		try :
			if not isinstance(auto_retry_interval,int):
				raise TypeError("auto_retry_interval must be set to int value")
			self._auto_retry_interval = auto_retry_interval
		except Exception as e :
			raise e


	'''
	get Enabled when autoupgrade for autoscalegroup is in progress.
	'''
	@property
	def is_autoupgrade_enabled(self) :
		try:
			return self._is_autoupgrade_enabled
		except Exception as e :
			raise e
	'''
	set Enabled when autoupgrade for autoscalegroup is in progress.
	'''
	@is_autoupgrade_enabled.setter
	def is_autoupgrade_enabled(self,is_autoupgrade_enabled):
		try :
			if not isinstance(is_autoupgrade_enabled,bool):
				raise TypeError("is_autoupgrade_enabled must be set to bool value")
			self._is_autoupgrade_enabled = is_autoupgrade_enabled
		except Exception as e :
			raise e


	'''
	get Mode (1.DNS/2.NLB/3.ALB/4.GLB)
	'''
	@property
	def mode(self) :
		try:
			return self._mode
		except Exception as e :
			raise e
	'''
	set Mode (1.DNS/2.NLB/3.ALB/4.GLB)
	'''
	@mode.setter
	def mode(self,mode):
		try :
			if not isinstance(mode,int):
				raise TypeError("mode must be set to int value")
			self._mode = mode
		except Exception as e :
			raise e


	'''
	get site
	'''
	@property
	def site_id(self) :
		try:
			return self._site_id
		except Exception as e :
			raise e
	'''
	set site
	'''
	@site_id.setter
	def site_id(self,site_id):
		try :
			if not isinstance(site_id,str):
				raise TypeError("site_id must be set to str value")
			self._site_id = site_id
		except Exception as e :
			raise e


	'''
	get Status of Throughput Threshold Config
	'''
	@property
	def throughput_threshold_enabled(self) :
		try:
			return self._throughput_threshold_enabled
		except Exception as e :
			raise e
	'''
	set Status of Throughput Threshold Config
	'''
	@throughput_threshold_enabled.setter
	def throughput_threshold_enabled(self,throughput_threshold_enabled):
		try :
			if not isinstance(throughput_threshold_enabled,bool):
				raise TypeError("throughput_threshold_enabled must be set to bool value")
			self._throughput_threshold_enabled = throughput_threshold_enabled
		except Exception as e :
			raise e


	'''
	get Minimum Memory Threshold Limit
	'''
	@property
	def memory_min(self) :
		try:
			return self._memory_min
		except Exception as e :
			raise e
	'''
	set Minimum Memory Threshold Limit
	'''
	@memory_min.setter
	def memory_min(self,memory_min):
		try :
			if not isinstance(memory_min,float):
				raise TypeError("memory_min must be set to float value")
			self._memory_min = memory_min
		except Exception as e :
			raise e


	'''
	get Maximum CPU Threshold Limit
	'''
	@property
	def cpu_max(self) :
		try:
			return self._cpu_max
		except Exception as e :
			raise e
	'''
	set Maximum CPU Threshold Limit
	'''
	@cpu_max.setter
	def cpu_max(self,cpu_max):
		try :
			if not isinstance(cpu_max,float):
				raise TypeError("cpu_max must be set to float value")
			self._cpu_max = cpu_max
		except Exception as e :
			raise e


	'''
	get Max auto retry count for retryable errors in an ASG.
	'''
	@property
	def auto_retry_count(self) :
		try:
			return self._auto_retry_count
		except Exception as e :
			raise e
	'''
	set Max auto retry count for retryable errors in an ASG.
	'''
	@auto_retry_count.setter
	def auto_retry_count(self,auto_retry_count):
		try :
			if not isinstance(auto_retry_count,int):
				raise TypeError("auto_retry_count must be set to int value")
			self._auto_retry_count = auto_retry_count
		except Exception as e :
			raise e


	'''
	get No of cold node supported per AutoscaleGroup
	'''
	@property
	def no_of_cold_nodes(self) :
		try:
			return self._no_of_cold_nodes
		except Exception as e :
			raise e
	'''
	set No of cold node supported per AutoscaleGroup
	'''
	@no_of_cold_nodes.setter
	def no_of_cold_nodes(self,no_of_cold_nodes):
		try :
			if not isinstance(no_of_cold_nodes,int):
				raise TypeError("no_of_cold_nodes must be set to int value")
			self._no_of_cold_nodes = no_of_cold_nodes
		except Exception as e :
			raise e


	'''
	get Auto-Scale Group Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Auto-Scale Group Name
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
	get Watch Time (No of intervels before triggering auto scale up/down)
	'''
	@property
	def watch_time(self) :
		try:
			return self._watch_time
		except Exception as e :
			raise e
	'''
	set Watch Time (No of intervels before triggering auto scale up/down)
	'''
	@watch_time.setter
	def watch_time(self,watch_time):
		try :
			if not isinstance(watch_time,int):
				raise TypeError("watch_time must be set to int value")
			self._watch_time = watch_time
		except Exception as e :
			raise e


	'''
	get Status of Auto-Scale Group (Enable/Disable)
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of Auto-Scale Group (Enable/Disable)
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,bool):
				raise TypeError("status must be set to bool value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get Enable/Disable Autoscale cold node support
	'''
	@property
	def enable_cold_node(self) :
		try:
			return self._enable_cold_node
		except Exception as e :
			raise e
	'''
	set Enable/Disable Autoscale cold node support
	'''
	@enable_cold_node.setter
	def enable_cold_node(self,enable_cold_node):
		try :
			if not isinstance(enable_cold_node,bool):
				raise TypeError("enable_cold_node must be set to bool value")
			self._enable_cold_node = enable_cold_node
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the auto-scale groups
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the auto-scale groups
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
	get Maximum Memory Threshold Limit
	'''
	@property
	def memory_max(self) :
		try:
			return self._memory_max
		except Exception as e :
			raise e
	'''
	set Maximum Memory Threshold Limit
	'''
	@memory_max.setter
	def memory_max(self,memory_max):
		try :
			if not isinstance(memory_max,float):
				raise TypeError("memory_max must be set to float value")
			self._memory_max = memory_max
		except Exception as e :
			raise e

	'''
	Array of tag_name and tag_value pair associated with the autoscalegroup
	'''
	@property
	def tags(self) :
		try:
			return self._tags
		except Exception as e :
			raise e
	'''
	Array of tag_name and tag_value pair associated with the autoscalegroup
	'''
	@tags.setter
	def tags(self,tags) :
		try :
			if not isinstance(tags,list):
				raise TypeError("tags must be set to array of property_map value")
			for item in tags :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._tags = tags
		except Exception as e :
			raise e

	'''
	Use this operation to get auto-scale groups.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				autoscalegroup_obj=autoscalegroup()
				response = autoscalegroup_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete auto-scale group(s).
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
					autoscalegroup_obj=autoscalegroup()
					return cls.delete_bulk_request(client,resource,autoscalegroup_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add auto-scale group.
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
				autoscalegroup_obj= autoscalegroup()
				return cls.perform_operation_bulk_request(service,resource,autoscalegroup_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify auto-scale group.
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
				autoscalegroup_obj=autoscalegroup()
				return cls.update_bulk_request(client,resource,autoscalegroup_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of autoscalegroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			autoscalegroup_obj = autoscalegroup()
			option_ = options()
			option_._filter=filter_
			return autoscalegroup_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the autoscalegroup resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			autoscalegroup_obj = autoscalegroup()
			option_ = options()
			option_._count=True
			response = autoscalegroup_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of autoscalegroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			autoscalegroup_obj = autoscalegroup()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = autoscalegroup_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(autoscalegroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.autoscalegroup
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(autoscalegroup_responses, response, "autoscalegroup_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.autoscalegroup_response_array
				i=0
				error = [autoscalegroup() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.autoscalegroup_response_array
			i=0
			autoscalegroup_objs = [autoscalegroup() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_autoscalegroup'):
					for props in obj._autoscalegroup:
						result = service.payload_formatter.string_to_bulk_resource(autoscalegroup_response,self.__class__.__name__,props)
						autoscalegroup_objs[i] = result.autoscalegroup
						i=i+1
			return autoscalegroup_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(autoscalegroup,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class autoscalegroup_response(base_response):
	def __init__(self,length=1) :
		self.autoscalegroup= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.autoscalegroup= [ autoscalegroup() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class autoscalegroup_responses(base_response):
	def __init__(self,length=1) :
		self.autoscalegroup_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.autoscalegroup_response_array = [ autoscalegroup() for _ in range(length)]
