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
from massrc.com.citrix.mas.nitro.resource.config.mps.mps_agent import mps_agent


'''
Configuration for Maintenance window for NetScaler Console agent resource
'''

class agent_maintenance_wndw(base_resource):
	_agent_id= ""
	_image_name= ""
	_cust_id= ""
	_agent_array=[]
	_agent_upgrade_time= ""
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
			return "agent_maintenance_wndw"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._cust_id
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
			return "agent_maintenance_wndws"
		except Exception as e :
			raise e



	'''
	get Agent Id.
	'''
	@property
	def agent_id(self) :
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	set Agent Id.
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
	get Image Name
	'''
	@property
	def image_name(self) :
		try:
			return self._image_name
		except Exception as e :
			raise e
	'''
	set Image Name
	'''
	@image_name.setter
	def image_name(self,image_name):
		try :
			if not isinstance(image_name,str):
				raise TypeError("image_name must be set to str value")
			self._image_name = image_name
		except Exception as e :
			raise e


	'''
	get Stores the schema name of the customer.
	'''
	@property
	def cust_id(self) :
		try:
			return self._cust_id
		except Exception as e :
			raise e
	'''
	set Stores the schema name of the customer.
	'''
	@cust_id.setter
	def cust_id(self,cust_id):
		try :
			if not isinstance(cust_id,str):
				raise TypeError("cust_id must be set to str value")
			self._cust_id = cust_id
		except Exception as e :
			raise e


	'''
	get List of mps_agent objects
	'''
	@property
	def agent_array(self) :
		try:
			return self._agent_array
		except Exception as e :
			raise e
	'''
	set List of mps_agent objects
	'''
	@agent_array.setter
	def agent_array(self,agent_array) :
		try :
			if not isinstance(agent_array,list):
				raise TypeError("agent_array must be set to array of mps_agent value")
			for item in agent_array :
				if not isinstance(item,mps_agent):
					raise TypeError("item must be set to mps_agent value")
			self._agent_array = agent_array
		except Exception as e :
			raise e


	'''
	get Stores the agent upgrade start time
	'''
	@property
	def agent_upgrade_time(self) :
		try:
			return self._agent_upgrade_time
		except Exception as e :
			raise e
	'''
	set Stores the agent upgrade start time
	'''
	@agent_upgrade_time.setter
	def agent_upgrade_time(self,agent_upgrade_time):
		try :
			if not isinstance(agent_upgrade_time,str):
				raise TypeError("agent_upgrade_time must be set to str value")
			self._agent_upgrade_time = agent_upgrade_time
		except Exception as e :
			raise e


	'''
	get Id is agent Id.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is agent Id.
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
	Use this operation to get agent upgrade.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				agent_maintenance_wndw_obj=agent_maintenance_wndw()
				response = agent_maintenance_wndw_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to upgrade NetScaler Console Agent.
	'''
	@classmethod
	def upgrade(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"upgrade")
				return res
			else : 
				agent_maintenance_wndw_obj= agent_maintenance_wndw()
				return cls.perform_operation_bulk_request(service,"upgrade",resource,agent_maintenance_wndw_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete agent upgrade.
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
					agent_maintenance_wndw_obj=agent_maintenance_wndw()
					return cls.delete_bulk_request(client,resource,agent_maintenance_wndw_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to update agent upgrade.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				agent_maintenance_wndw_obj=agent_maintenance_wndw()
				return cls.update_bulk_request(client,resource,agent_maintenance_wndw_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of agent_maintenance_wndw resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			agent_maintenance_wndw_obj = agent_maintenance_wndw()
			option_ = options()
			option_._filter=filter_
			return agent_maintenance_wndw_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the agent_maintenance_wndw resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			agent_maintenance_wndw_obj = agent_maintenance_wndw()
			option_ = options()
			option_._count=True
			response = agent_maintenance_wndw_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of agent_maintenance_wndw resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			agent_maintenance_wndw_obj = agent_maintenance_wndw()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = agent_maintenance_wndw_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(agent_maintenance_wndw_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.agent_maintenance_wndw
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(agent_maintenance_wndw_responses, response, "agent_maintenance_wndw_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.agent_maintenance_wndw_response_array
				i=0
				error = [agent_maintenance_wndw() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.agent_maintenance_wndw_response_array
			i=0
			agent_maintenance_wndw_objs = [agent_maintenance_wndw() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_agent_maintenance_wndw'):
					for props in obj._agent_maintenance_wndw:
						result = service.payload_formatter.string_to_bulk_resource(agent_maintenance_wndw_response,self.__class__.__name__,props)
						agent_maintenance_wndw_objs[i] = result.agent_maintenance_wndw
						i=i+1
			return agent_maintenance_wndw_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(agent_maintenance_wndw,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class agent_maintenance_wndw_response(base_response):
	def __init__(self,length=1) :
		self.agent_maintenance_wndw= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.agent_maintenance_wndw= [ agent_maintenance_wndw() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class agent_maintenance_wndw_responses(base_response):
	def __init__(self,length=1) :
		self.agent_maintenance_wndw_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.agent_maintenance_wndw_response_array = [ agent_maintenance_wndw() for _ in range(length)]
