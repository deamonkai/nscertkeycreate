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
Configuration for Holds information regarding VIP and thirdparty VIP autoselection preference. resource
'''

class autoselection_preference(base_resource):
	_enable_non_access_vserver= ""
	_type= ""
	_enable_auto_tp_vserver_selection= ""
	_enable_auto_vip_selection= ""
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
			return "autoselection_preference"
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
			return "autoselection_preferences"
		except Exception as e :
			raise e



	'''
	get Enable auto selection of non Accesible Vservers
	'''
	@property
	def enable_non_access_vserver(self) :
		try:
			return self._enable_non_access_vserver
		except Exception as e :
			raise e
	'''
	set Enable auto selection of non Accesible Vservers
	'''
	@enable_non_access_vserver.setter
	def enable_non_access_vserver(self,enable_non_access_vserver):
		try :
			if not isinstance(enable_non_access_vserver,bool):
				raise TypeError("enable_non_access_vserver must be set to bool value")
			self._enable_non_access_vserver = enable_non_access_vserver
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set 
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Enable auto selection of Third Party Vservers
	'''
	@property
	def enable_auto_tp_vserver_selection(self) :
		try:
			return self._enable_auto_tp_vserver_selection
		except Exception as e :
			raise e
	'''
	set Enable auto selection of Third Party Vservers
	'''
	@enable_auto_tp_vserver_selection.setter
	def enable_auto_tp_vserver_selection(self,enable_auto_tp_vserver_selection):
		try :
			if not isinstance(enable_auto_tp_vserver_selection,bool):
				raise TypeError("enable_auto_tp_vserver_selection must be set to bool value")
			self._enable_auto_tp_vserver_selection = enable_auto_tp_vserver_selection
		except Exception as e :
			raise e


	'''
	get Enable auto selection of vips
	'''
	@property
	def enable_auto_vip_selection(self) :
		try:
			return self._enable_auto_vip_selection
		except Exception as e :
			raise e
	'''
	set Enable auto selection of vips
	'''
	@enable_auto_vip_selection.setter
	def enable_auto_vip_selection(self,enable_auto_vip_selection):
		try :
			if not isinstance(enable_auto_vip_selection,bool):
				raise TypeError("enable_auto_vip_selection must be set to bool value")
			self._enable_auto_vip_selection = enable_auto_vip_selection
		except Exception as e :
			raise e


	'''
	get Primary key for this table.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Primary key for this table.
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
	Use this operation to modify vip_autoselection_preference.
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
				autoselection_preference_obj=autoselection_preference()
				return cls.update_bulk_request(client,resource,autoselection_preference_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get vip_autoselection_preference.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				autoselection_preference_obj=autoselection_preference()
				response = autoselection_preference_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of autoselection_preference resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			autoselection_preference_obj = autoselection_preference()
			option_ = options()
			option_._filter=filter_
			return autoselection_preference_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the autoselection_preference resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			autoselection_preference_obj = autoselection_preference()
			option_ = options()
			option_._count=True
			response = autoselection_preference_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of autoselection_preference resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			autoselection_preference_obj = autoselection_preference()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = autoselection_preference_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(autoselection_preference_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.autoselection_preference
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(autoselection_preference_responses, response, "autoselection_preference_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.autoselection_preference_response_array
				i=0
				error = [autoselection_preference() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.autoselection_preference_response_array
			i=0
			autoselection_preference_objs = [autoselection_preference() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_autoselection_preference'):
					for props in obj._autoselection_preference:
						result = service.payload_formatter.string_to_bulk_resource(autoselection_preference_response,self.__class__.__name__,props)
						autoselection_preference_objs[i] = result.autoselection_preference
						i=i+1
			return autoselection_preference_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(autoselection_preference,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class autoselection_preference_response(base_response):
	def __init__(self,length=1) :
		self.autoselection_preference= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.autoselection_preference= [ autoselection_preference() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class autoselection_preference_responses(base_response):
	def __init__(self,length=1) :
		self.autoselection_preference_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.autoselection_preference_response_array = [ autoselection_preference() for _ in range(length)]
