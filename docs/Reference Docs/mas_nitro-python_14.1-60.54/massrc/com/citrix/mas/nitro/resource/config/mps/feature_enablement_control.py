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
Configuration for Opt out from feature resource
'''

class feature_enablement_control(base_resource):
	_autoenable_gw= ""
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
			return "feature_enablement_control"
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
			return "feature_enablement_controls"
		except Exception as e :
			raise e



	'''
	get Ops toggle will be controlled with this flag if user has required permissions to edit.
	'''
	@property
	def autoenable_gw(self) :
		try:
			return self._autoenable_gw
		except Exception as e :
			raise e
	'''
	set Ops toggle will be controlled with this flag if user has required permissions to edit.
	'''
	@autoenable_gw.setter
	def autoenable_gw(self,autoenable_gw):
		try :
			if not isinstance(autoenable_gw,bool):
				raise TypeError("autoenable_gw must be set to bool value")
			self._autoenable_gw = autoenable_gw
		except Exception as e :
			raise e

	'''
	Use this operation to get feature toggles status..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				feature_enablement_control_obj=feature_enablement_control()
				response = feature_enablement_control_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify a feature toggle..
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
				feature_enablement_control_obj=feature_enablement_control()
				return cls.update_bulk_request(client,resource,feature_enablement_control_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of feature_enablement_control resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			feature_enablement_control_obj = feature_enablement_control()
			option_ = options()
			option_._filter=filter_
			return feature_enablement_control_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the feature_enablement_control resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			feature_enablement_control_obj = feature_enablement_control()
			option_ = options()
			option_._count=True
			response = feature_enablement_control_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of feature_enablement_control resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			feature_enablement_control_obj = feature_enablement_control()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = feature_enablement_control_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(feature_enablement_control_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.feature_enablement_control
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(feature_enablement_control_responses, response, "feature_enablement_control_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.feature_enablement_control_response_array
				i=0
				error = [feature_enablement_control() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.feature_enablement_control_response_array
			i=0
			feature_enablement_control_objs = [feature_enablement_control() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_feature_enablement_control'):
					for props in obj._feature_enablement_control:
						result = service.payload_formatter.string_to_bulk_resource(feature_enablement_control_response,self.__class__.__name__,props)
						feature_enablement_control_objs[i] = result.feature_enablement_control
						i=i+1
			return feature_enablement_control_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(feature_enablement_control,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class feature_enablement_control_response(base_response):
	def __init__(self,length=1) :
		self.feature_enablement_control= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.feature_enablement_control= [ feature_enablement_control() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class feature_enablement_control_responses(base_response):
	def __init__(self,length=1) :
		self.feature_enablement_control_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.feature_enablement_control_response_array = [ feature_enablement_control() for _ in range(length)]
