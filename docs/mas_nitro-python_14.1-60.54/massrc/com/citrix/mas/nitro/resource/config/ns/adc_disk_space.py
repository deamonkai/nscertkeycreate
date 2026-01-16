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
from massrc.com.citrix.mas.nitro.resource.config.ns.adc_disk_space_details import adc_disk_space_details


'''
Configuration for Disk space for NetScaler resource
'''

class adc_disk_space(base_resource):
	_space_details=[]
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
			return "adc_disk_space"
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
			return "adc_disk_spaces"
		except Exception as e :
			raise e



	'''
	get List of NetScaler disk space details for folder space check and disk clean up
	'''
	@property
	def space_details(self) :
		try:
			return self._space_details
		except Exception as e :
			raise e
	'''
	set List of NetScaler disk space details for folder space check and disk clean up
	'''
	@space_details.setter
	def space_details(self,space_details) :
		try :
			if not isinstance(space_details,list):
				raise TypeError("space_details must be set to array of adc_disk_space_details value")
			for item in space_details :
				if not isinstance(item,adc_disk_space_details):
					raise TypeError("item must be set to adc_disk_space_details value")
			self._space_details = space_details
		except Exception as e :
			raise e


	'''
	get Id is Activity Id
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is Activity Id
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
	Use this operation to clean disk space.
	'''
	@classmethod
	def clean_disk_space(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"clean_disk_space")
				return res
			else : 
				adc_disk_space_obj= adc_disk_space()
				return cls.perform_operation_bulk_request(service,"clean_disk_space",resource,adc_disk_space_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler disk space details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adc_disk_space_obj=adc_disk_space()
				response = adc_disk_space_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to check disk space.
	'''
	@classmethod
	def check_disk_space(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"check_disk_space")
				return res
			else : 
				adc_disk_space_obj= adc_disk_space()
				return cls.perform_operation_bulk_request(service,"check_disk_space",resource,adc_disk_space_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adc_disk_space resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adc_disk_space_obj = adc_disk_space()
			option_ = options()
			option_._filter=filter_
			return adc_disk_space_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adc_disk_space resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adc_disk_space_obj = adc_disk_space()
			option_ = options()
			option_._count=True
			response = adc_disk_space_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adc_disk_space resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adc_disk_space_obj = adc_disk_space()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adc_disk_space_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adc_disk_space_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_disk_space
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_disk_space_responses, response, "adc_disk_space_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_disk_space_response_array
				i=0
				error = [adc_disk_space() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_disk_space_response_array
			i=0
			adc_disk_space_objs = [adc_disk_space() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_disk_space'):
					for props in obj._adc_disk_space:
						result = service.payload_formatter.string_to_bulk_resource(adc_disk_space_response,self.__class__.__name__,props)
						adc_disk_space_objs[i] = result.adc_disk_space
						i=i+1
			return adc_disk_space_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_disk_space,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_disk_space_response(base_response):
	def __init__(self,length=1) :
		self.adc_disk_space= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_disk_space= [ adc_disk_space() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_disk_space_responses(base_response):
	def __init__(self,length=1) :
		self.adc_disk_space_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_disk_space_response_array = [ adc_disk_space() for _ in range(length)]
