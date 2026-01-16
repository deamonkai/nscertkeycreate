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
Configuration for public ip block lookup cache on db level. resource
'''

class public_ip_block_lookup(base_resource):
	_region= ""
	_city= ""
	_ipaddress= ""
	_latitude= ""
	_longitude= ""
	_country_code= ""
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
			return "public_ip_block_lookup"
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
			return "public_ip_block_lookups"
		except Exception as e :
			raise e



	'''
	get region
	'''
	@property
	def region(self) :
		try:
			return self._region
		except Exception as e :
			raise e
	'''
	set region
	'''
	@region.setter
	def region(self,region):
		try :
			if not isinstance(region,str):
				raise TypeError("region must be set to str value")
			self._region = region
		except Exception as e :
			raise e


	'''
	get city
	'''
	@property
	def city(self) :
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	set city
	'''
	@city.setter
	def city(self,city):
		try :
			if not isinstance(city,str):
				raise TypeError("city must be set to str value")
			self._city = city
		except Exception as e :
			raise e


	'''
	get ipaddress in numeric format
	'''
	@property
	def ipaddress(self) :
		try:
			return self._ipaddress
		except Exception as e :
			raise e
	'''
	set ipaddress in numeric format
	'''
	@ipaddress.setter
	def ipaddress(self,ipaddress):
		try :
			if not isinstance(ipaddress,long):
				raise TypeError("ipaddress must be set to long value")
			self._ipaddress = ipaddress
		except Exception as e :
			raise e


	'''
	get latitude
	'''
	@property
	def latitude(self) :
		try:
			return self._latitude
		except Exception as e :
			raise e
	'''
	set latitude
	'''
	@latitude.setter
	def latitude(self,latitude):
		try :
			if not isinstance(latitude,float):
				raise TypeError("latitude must be set to float value")
			self._latitude = latitude
		except Exception as e :
			raise e


	'''
	get longitude
	'''
	@property
	def longitude(self) :
		try:
			return self._longitude
		except Exception as e :
			raise e
	'''
	set longitude
	'''
	@longitude.setter
	def longitude(self,longitude):
		try :
			if not isinstance(longitude,float):
				raise TypeError("longitude must be set to float value")
			self._longitude = longitude
		except Exception as e :
			raise e


	'''
	get country_code
	'''
	@property
	def country_code(self) :
		try:
			return self._country_code
		except Exception as e :
			raise e
	'''
	set country_code
	'''
	@country_code.setter
	def country_code(self,country_code):
		try :
			if not isinstance(country_code,str):
				raise TypeError("country_code must be set to str value")
			self._country_code = country_code
		except Exception as e :
			raise e

	'''
	Use this operation to get ip block.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				public_ip_block_lookup_obj=public_ip_block_lookup()
				response = public_ip_block_lookup_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of public_ip_block_lookup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			public_ip_block_lookup_obj = public_ip_block_lookup()
			option_ = options()
			option_._filter=filter_
			return public_ip_block_lookup_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the public_ip_block_lookup resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			public_ip_block_lookup_obj = public_ip_block_lookup()
			option_ = options()
			option_._count=True
			response = public_ip_block_lookup_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of public_ip_block_lookup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			public_ip_block_lookup_obj = public_ip_block_lookup()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = public_ip_block_lookup_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(public_ip_block_lookup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.public_ip_block_lookup
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(public_ip_block_lookup_responses, response, "public_ip_block_lookup_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.public_ip_block_lookup_response_array
				i=0
				error = [public_ip_block_lookup() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.public_ip_block_lookup_response_array
			i=0
			public_ip_block_lookup_objs = [public_ip_block_lookup() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_public_ip_block_lookup'):
					for props in obj._public_ip_block_lookup:
						result = service.payload_formatter.string_to_bulk_resource(public_ip_block_lookup_response,self.__class__.__name__,props)
						public_ip_block_lookup_objs[i] = result.public_ip_block_lookup
						i=i+1
			return public_ip_block_lookup_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(public_ip_block_lookup,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class public_ip_block_lookup_response(base_response):
	def __init__(self,length=1) :
		self.public_ip_block_lookup= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.public_ip_block_lookup= [ public_ip_block_lookup() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class public_ip_block_lookup_responses(base_response):
	def __init__(self,length=1) :
		self.public_ip_block_lookup_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.public_ip_block_lookup_response_array = [ public_ip_block_lookup() for _ in range(length)]
