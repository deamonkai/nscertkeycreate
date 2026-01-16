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
Configuration for Flex license bundle resource
'''

class flex_bundle(base_resource):
	_name= ""
	_entitled_units= ""
	_spec= ""
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
			return "flex_bundle"
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
			return "flex_bundles"
		except Exception as e :
			raise e



	'''
	get Display name of flex bundle parameter
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e


	'''
	get Entitled free flex license units
	'''
	@property
	def entitled_units(self) :
		try:
			return self._entitled_units
		except Exception as e :
			raise e


	'''
	get Specification of flex license bundle
	'''
	@property
	def spec(self) :
		try:
			return self._spec
		except Exception as e :
			raise e

	'''
	Use this operation to get device license info.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				flex_bundle_obj=flex_bundle()
				response = flex_bundle_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of flex_bundle resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			flex_bundle_obj = flex_bundle()
			option_ = options()
			option_._filter=filter_
			return flex_bundle_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the flex_bundle resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			flex_bundle_obj = flex_bundle()
			option_ = options()
			option_._count=True
			response = flex_bundle_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of flex_bundle resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			flex_bundle_obj = flex_bundle()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = flex_bundle_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(flex_bundle_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.flex_bundle
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(flex_bundle_responses, response, "flex_bundle_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.flex_bundle_response_array
				i=0
				error = [flex_bundle() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.flex_bundle_response_array
			i=0
			flex_bundle_objs = [flex_bundle() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_flex_bundle'):
					for props in obj._flex_bundle:
						result = service.payload_formatter.string_to_bulk_resource(flex_bundle_response,self.__class__.__name__,props)
						flex_bundle_objs[i] = result.flex_bundle
						i=i+1
			return flex_bundle_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(flex_bundle,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class flex_bundle_response(base_response):
	def __init__(self,length=1) :
		self.flex_bundle= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.flex_bundle= [ flex_bundle() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class flex_bundle_responses(base_response):
	def __init__(self,length=1) :
		self.flex_bundle_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.flex_bundle_response_array = [ flex_bundle() for _ in range(length)]
