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
Configuration for NetScaler Agent Version History resource
'''

class mas_agent_version_history(base_resource):
	_version= ""
	_serial_no= ""
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
			return "mas_agent_version_history"
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
			return "mas_agent_version_historys"
		except Exception as e :
			raise e



	'''
	get mas agent version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e


	'''
	get Serial Number
	'''
	@property
	def serial_no(self) :
		try:
			return self._serial_no
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler Agent versions history.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				mas_agent_version_history_obj=mas_agent_version_history()
				response = mas_agent_version_history_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mas_agent_version_history resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mas_agent_version_history_obj = mas_agent_version_history()
			option_ = options()
			option_._filter=filter_
			return mas_agent_version_history_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mas_agent_version_history resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mas_agent_version_history_obj = mas_agent_version_history()
			option_ = options()
			option_._count=True
			response = mas_agent_version_history_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mas_agent_version_history resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mas_agent_version_history_obj = mas_agent_version_history()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mas_agent_version_history_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mas_agent_version_history_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mas_agent_version_history
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mas_agent_version_history_responses, response, "mas_agent_version_history_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mas_agent_version_history_response_array
				i=0
				error = [mas_agent_version_history() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mas_agent_version_history_response_array
			i=0
			mas_agent_version_history_objs = [mas_agent_version_history() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mas_agent_version_history'):
					for props in obj._mas_agent_version_history:
						result = service.payload_formatter.string_to_bulk_resource(mas_agent_version_history_response,self.__class__.__name__,props)
						mas_agent_version_history_objs[i] = result.mas_agent_version_history
						i=i+1
			return mas_agent_version_history_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mas_agent_version_history,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mas_agent_version_history_response(base_response):
	def __init__(self,length=1) :
		self.mas_agent_version_history= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mas_agent_version_history= [ mas_agent_version_history() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mas_agent_version_history_responses(base_response):
	def __init__(self,length=1) :
		self.mas_agent_version_history_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mas_agent_version_history_response_array = [ mas_agent_version_history() for _ in range(length)]
