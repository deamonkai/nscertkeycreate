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
Configuration for To check if policies exist for a particular event_name resource
'''

class apf_policy_info(base_resource):
	_event_name= ""
	_does_policy_exist= ""
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
			return "apf_policy_info"
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
			return "apf_policy_infos"
		except Exception as e :
			raise e



	'''
	get APF event_name
	'''
	@property
	def event_name(self) :
		try:
			return self._event_name
		except Exception as e :
			raise e
	'''
	set APF event_name
	'''
	@event_name.setter
	def event_name(self,event_name):
		try :
			if not isinstance(event_name,str):
				raise TypeError("event_name must be set to str value")
			self._event_name = event_name
		except Exception as e :
			raise e


	'''
	get Flag indicating policies exist or not
	'''
	@property
	def does_policy_exist(self) :
		try:
			return self._does_policy_exist
		except Exception as e :
			raise e
	'''
	set Flag indicating policies exist or not
	'''
	@does_policy_exist.setter
	def does_policy_exist(self,does_policy_exist):
		try :
			if not isinstance(does_policy_exist,bool):
				raise TypeError("does_policy_exist must be set to bool value")
			self._does_policy_exist = does_policy_exist
		except Exception as e :
			raise e

	'''
	Use this operation to get flag.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				apf_policy_info_obj=apf_policy_info()
				response = apf_policy_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of apf_policy_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			apf_policy_info_obj = apf_policy_info()
			option_ = options()
			option_._filter=filter_
			return apf_policy_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the apf_policy_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			apf_policy_info_obj = apf_policy_info()
			option_ = options()
			option_._count=True
			response = apf_policy_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of apf_policy_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			apf_policy_info_obj = apf_policy_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = apf_policy_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(apf_policy_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.apf_policy_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(apf_policy_info_responses, response, "apf_policy_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.apf_policy_info_response_array
				i=0
				error = [apf_policy_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.apf_policy_info_response_array
			i=0
			apf_policy_info_objs = [apf_policy_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_apf_policy_info'):
					for props in obj._apf_policy_info:
						result = service.payload_formatter.string_to_bulk_resource(apf_policy_info_response,self.__class__.__name__,props)
						apf_policy_info_objs[i] = result.apf_policy_info
						i=i+1
			return apf_policy_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(apf_policy_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class apf_policy_info_response(base_response):
	def __init__(self,length=1) :
		self.apf_policy_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.apf_policy_info= [ apf_policy_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class apf_policy_info_responses(base_response):
	def __init__(self,length=1) :
		self.apf_policy_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.apf_policy_info_response_array = [ apf_policy_info() for _ in range(length)]
