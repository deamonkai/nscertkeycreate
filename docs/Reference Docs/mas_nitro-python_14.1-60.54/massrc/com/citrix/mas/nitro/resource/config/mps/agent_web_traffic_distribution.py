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
Configuration for Getting Web Traffic Distribution based on number of webinsight enabled vservers resource
'''

class agent_web_traffic_distribution(base_resource):
	_traffic_dist_multiplier= ""
	_agent_id= ""
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
			return "agent_web_traffic_distribution"
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
			return "agent_web_traffic_distributions"
		except Exception as e :
			raise e



	'''
	get Traffic Distribution Multiplier
	'''
	@property
	def traffic_dist_multiplier(self) :
		try:
			return self._traffic_dist_multiplier
		except Exception as e :
			raise e
	'''
	set Traffic Distribution Multiplier
	'''
	@traffic_dist_multiplier.setter
	def traffic_dist_multiplier(self,traffic_dist_multiplier):
		try :
			if not isinstance(traffic_dist_multiplier,float):
				raise TypeError("traffic_dist_multiplier must be set to float value")
			self._traffic_dist_multiplier = traffic_dist_multiplier
		except Exception as e :
			raise e


	'''
	get Agent Id
	'''
	@property
	def agent_id(self) :
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	set Agent Id
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
	Use this operation to get traffic distribution.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				agent_web_traffic_distribution_obj=agent_web_traffic_distribution()
				response = agent_web_traffic_distribution_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of agent_web_traffic_distribution resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			agent_web_traffic_distribution_obj = agent_web_traffic_distribution()
			option_ = options()
			option_._filter=filter_
			return agent_web_traffic_distribution_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the agent_web_traffic_distribution resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			agent_web_traffic_distribution_obj = agent_web_traffic_distribution()
			option_ = options()
			option_._count=True
			response = agent_web_traffic_distribution_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of agent_web_traffic_distribution resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			agent_web_traffic_distribution_obj = agent_web_traffic_distribution()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = agent_web_traffic_distribution_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(agent_web_traffic_distribution_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.agent_web_traffic_distribution
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(agent_web_traffic_distribution_responses, response, "agent_web_traffic_distribution_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.agent_web_traffic_distribution_response_array
				i=0
				error = [agent_web_traffic_distribution() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.agent_web_traffic_distribution_response_array
			i=0
			agent_web_traffic_distribution_objs = [agent_web_traffic_distribution() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_agent_web_traffic_distribution'):
					for props in obj._agent_web_traffic_distribution:
						result = service.payload_formatter.string_to_bulk_resource(agent_web_traffic_distribution_response,self.__class__.__name__,props)
						agent_web_traffic_distribution_objs[i] = result.agent_web_traffic_distribution
						i=i+1
			return agent_web_traffic_distribution_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(agent_web_traffic_distribution,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class agent_web_traffic_distribution_response(base_response):
	def __init__(self,length=1) :
		self.agent_web_traffic_distribution= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.agent_web_traffic_distribution= [ agent_web_traffic_distribution() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class agent_web_traffic_distribution_responses(base_response):
	def __init__(self,length=1) :
		self.agent_web_traffic_distribution_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.agent_web_traffic_distribution_response_array = [ agent_web_traffic_distribution() for _ in range(length)]
