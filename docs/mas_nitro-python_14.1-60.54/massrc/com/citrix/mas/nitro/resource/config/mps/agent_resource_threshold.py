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

from massrc.com.citrix.mas.nitro.resource.config.mps.threshold import threshold

'''
Configuration for Agent Resource Utilization Threshold resource
'''

class agent_resource_threshold(threshold):
	_cpu_usage_threshold= ""
	_disk_usage_threshold= ""
	_memory_usage_threshold= ""
	_agent_ip_address= ""
	_cpu_usage= ""
	_disk_usage= ""
	_memory_usage= ""
	_memory_count= ""
	_cpu_count= ""
	_disk_count= ""
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
			return "agent_resource_threshold"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(agent_resource_threshold,self).get_object_id()
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
			return "agent_resource_thresholds"
		except Exception as e :
			raise e



	'''
	get CPU usage threshold
	'''
	@property
	def cpu_usage_threshold(self) :
		try:
			return self._cpu_usage_threshold
		except Exception as e :
			raise e
	'''
	set CPU usage threshold
	'''
	@cpu_usage_threshold.setter
	def cpu_usage_threshold(self,cpu_usage_threshold):
		try :
			if not isinstance(cpu_usage_threshold,int):
				raise TypeError("cpu_usage_threshold must be set to int value")
			self._cpu_usage_threshold = cpu_usage_threshold
		except Exception as e :
			raise e


	'''
	get Disk usage threshold
	'''
	@property
	def disk_usage_threshold(self) :
		try:
			return self._disk_usage_threshold
		except Exception as e :
			raise e
	'''
	set Disk usage threshold
	'''
	@disk_usage_threshold.setter
	def disk_usage_threshold(self,disk_usage_threshold):
		try :
			if not isinstance(disk_usage_threshold,int):
				raise TypeError("disk_usage_threshold must be set to int value")
			self._disk_usage_threshold = disk_usage_threshold
		except Exception as e :
			raise e


	'''
	get Memory usage threshold
	'''
	@property
	def memory_usage_threshold(self) :
		try:
			return self._memory_usage_threshold
		except Exception as e :
			raise e
	'''
	set Memory usage threshold
	'''
	@memory_usage_threshold.setter
	def memory_usage_threshold(self,memory_usage_threshold):
		try :
			if not isinstance(memory_usage_threshold,int):
				raise TypeError("memory_usage_threshold must be set to int value")
			self._memory_usage_threshold = memory_usage_threshold
		except Exception as e :
			raise e

	'''
	Agent IP Address for this threshold breach
	'''
	@property
	def agent_ip_address(self):
		try:
			return self._agent_ip_address
		except Exception as e :
			raise e
	'''
	Agent IP Address for this threshold breach
	'''
	@agent_ip_address.setter
	def agent_ip_address(self,agent_ip_address):
		try :
			if not isinstance(agent_ip_address,str):
				raise TypeError("agent_ip_address must be set to str value")
			self._agent_ip_address = agent_ip_address
		except Exception as e :
			raise e

	'''
	Total CPU usage.
	'''
	@property
	def cpu_usage(self):
		try:
			return self._cpu_usage
		except Exception as e :
			raise e
	'''
	Total CPU usage.
	'''
	@cpu_usage.setter
	def cpu_usage(self,cpu_usage):
		try :
			if not isinstance(cpu_usage,float):
				raise TypeError("cpu_usage must be set to float value")
			self._cpu_usage = cpu_usage
		except Exception as e :
			raise e

	'''
	Total disk space usage.
	'''
	@property
	def disk_usage(self):
		try:
			return self._disk_usage
		except Exception as e :
			raise e
	'''
	Total disk space usage.
	'''
	@disk_usage.setter
	def disk_usage(self,disk_usage):
		try :
			if not isinstance(disk_usage,long):
				raise TypeError("disk_usage must be set to long value")
			self._disk_usage = disk_usage
		except Exception as e :
			raise e

	'''
	Total memory usage.
	'''
	@property
	def memory_usage(self):
		try:
			return self._memory_usage
		except Exception as e :
			raise e
	'''
	Total memory usage.
	'''
	@memory_usage.setter
	def memory_usage(self,memory_usage):
		try :
			if not isinstance(memory_usage,long):
				raise TypeError("memory_usage must be set to long value")
			self._memory_usage = memory_usage
		except Exception as e :
			raise e

	'''
	Shows for how long agent memory threshold breach, each value of count increases after every 5 minutes
	'''
	@property
	def memory_count(self):
		try:
			return self._memory_count
		except Exception as e :
			raise e
	'''
	Shows for how long agent memory threshold breach, each value of count increases after every 5 minutes
	'''
	@memory_count.setter
	def memory_count(self,memory_count):
		try :
			if not isinstance(memory_count,int):
				raise TypeError("memory_count must be set to int value")
			self._memory_count = memory_count
		except Exception as e :
			raise e

	'''
	Shows for how long agent cpu threshold breach, each value of count increases after every 5 minutes
	'''
	@property
	def cpu_count(self):
		try:
			return self._cpu_count
		except Exception as e :
			raise e
	'''
	Shows for how long agent cpu threshold breach, each value of count increases after every 5 minutes
	'''
	@cpu_count.setter
	def cpu_count(self,cpu_count):
		try :
			if not isinstance(cpu_count,int):
				raise TypeError("cpu_count must be set to int value")
			self._cpu_count = cpu_count
		except Exception as e :
			raise e

	'''
	Shows for how long agent disk threshold breach, each value of count increases after every 5 minutes
	'''
	@property
	def disk_count(self):
		try:
			return self._disk_count
		except Exception as e :
			raise e
	'''
	Shows for how long agent disk threshold breach, each value of count increases after every 5 minutes
	'''
	@disk_count.setter
	def disk_count(self,disk_count):
		try :
			if not isinstance(disk_count,int):
				raise TypeError("disk_count must be set to int value")
			self._disk_count = disk_count
		except Exception as e :
			raise e

	'''
	Use this operation to modify agent resource utilization threshold.
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
				agent_resource_threshold_obj=agent_resource_threshold()
				return cls.update_bulk_request(client,resource,agent_resource_threshold_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get agent resource utilization threshold.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				agent_resource_threshold_obj=agent_resource_threshold()
				response = agent_resource_threshold_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of agent_resource_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			agent_resource_threshold_obj = agent_resource_threshold()
			option_ = options()
			option_._filter=filter_
			return agent_resource_threshold_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the agent_resource_threshold resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			agent_resource_threshold_obj = agent_resource_threshold()
			option_ = options()
			option_._count=True
			response = agent_resource_threshold_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of agent_resource_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			agent_resource_threshold_obj = agent_resource_threshold()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = agent_resource_threshold_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(agent_resource_threshold_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.agent_resource_threshold
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(agent_resource_threshold_responses, response, "agent_resource_threshold_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.agent_resource_threshold_response_array
				i=0
				error = [agent_resource_threshold() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.agent_resource_threshold_response_array
			i=0
			agent_resource_threshold_objs = [agent_resource_threshold() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_agent_resource_threshold'):
					for props in obj._agent_resource_threshold:
						result = service.payload_formatter.string_to_bulk_resource(agent_resource_threshold_response,self.__class__.__name__,props)
						agent_resource_threshold_objs[i] = result.agent_resource_threshold
						i=i+1
			return agent_resource_threshold_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(agent_resource_threshold,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class agent_resource_threshold_response(base_response):
	def __init__(self,length=1) :
		self.agent_resource_threshold= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.agent_resource_threshold= [ agent_resource_threshold() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class agent_resource_threshold_responses(base_response):
	def __init__(self,length=1) :
		self.agent_resource_threshold_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.agent_resource_threshold_response_array = [ agent_resource_threshold() for _ in range(length)]
