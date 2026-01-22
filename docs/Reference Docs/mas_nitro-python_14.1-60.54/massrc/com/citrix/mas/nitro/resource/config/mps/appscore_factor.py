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
Configuration for Factors contributing in appscore calculation resource
'''

class appscore_factor(base_resource):
	_id= ""
	_contribute= ""
	_factor_id= ""
	_factor_name= ""
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
			return "appscore_factor"
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
			return "appscore_factors"
		except Exception as e :
			raise e



	'''
	get Id
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e


	'''
	get Flag to check if factor is going to contribute in appscore.
	'''
	@property
	def contribute(self) :
		try:
			return self._contribute
		except Exception as e :
			raise e
	'''
	set Flag to check if factor is going to contribute in appscore.
	'''
	@contribute.setter
	def contribute(self,contribute):
		try :
			if not isinstance(contribute,bool):
				raise TypeError("contribute must be set to bool value")
			self._contribute = contribute
		except Exception as e :
			raise e


	'''
	get Factor If.
	'''
	@property
	def factor_id(self) :
		try:
			return self._factor_id
		except Exception as e :
			raise e
	'''
	set Factor If.
	'''
	@factor_id.setter
	def factor_id(self,factor_id):
		try :
			if not isinstance(factor_id,int):
				raise TypeError("factor_id must be set to int value")
			self._factor_id = factor_id
		except Exception as e :
			raise e


	'''
	get Factor Name.
	'''
	@property
	def factor_name(self) :
		try:
			return self._factor_name
		except Exception as e :
			raise e
	'''
	set Factor Name.
	'''
	@factor_name.setter
	def factor_name(self,factor_name):
		try :
			if not isinstance(factor_name,str):
				raise TypeError("factor_name must be set to str value")
			self._factor_name = factor_name
		except Exception as e :
			raise e

	'''
	Use this operation to choose the factor to contibute in app score calculation.
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
				appscore_factor_obj=appscore_factor()
				return cls.update_bulk_request(client,resource,appscore_factor_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get all factors.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				appscore_factor_obj=appscore_factor()
				response = appscore_factor_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of appscore_factor resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			appscore_factor_obj = appscore_factor()
			option_ = options()
			option_._filter=filter_
			return appscore_factor_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the appscore_factor resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			appscore_factor_obj = appscore_factor()
			option_ = options()
			option_._count=True
			response = appscore_factor_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of appscore_factor resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			appscore_factor_obj = appscore_factor()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = appscore_factor_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(appscore_factor_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appscore_factor
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(appscore_factor_responses, response, "appscore_factor_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.appscore_factor_response_array
				i=0
				error = [appscore_factor() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.appscore_factor_response_array
			i=0
			appscore_factor_objs = [appscore_factor() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_appscore_factor'):
					for props in obj._appscore_factor:
						result = service.payload_formatter.string_to_bulk_resource(appscore_factor_response,self.__class__.__name__,props)
						appscore_factor_objs[i] = result.appscore_factor
						i=i+1
			return appscore_factor_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(appscore_factor,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class appscore_factor_response(base_response):
	def __init__(self,length=1) :
		self.appscore_factor= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.appscore_factor= [ appscore_factor() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class appscore_factor_responses(base_response):
	def __init__(self,length=1) :
		self.appscore_factor_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.appscore_factor_response_array = [ appscore_factor() for _ in range(length)]
