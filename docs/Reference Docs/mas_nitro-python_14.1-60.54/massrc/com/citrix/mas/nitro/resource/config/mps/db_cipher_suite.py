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
Configuration for Database Cipher Suite resource
'''

class db_cipher_suite(base_resource):
	_cipher_suite_name= ""
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
			return "db_cipher_suite"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._cipher_suite_name
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
			return "db_cipher_suites"
		except Exception as e :
			raise e



	'''
	get Name of the Cipher Suite
	'''
	@property
	def cipher_suite_name(self) :
		try:
			return self._cipher_suite_name
		except Exception as e :
			raise e
	'''
	set Name of the Cipher Suite
	'''
	@cipher_suite_name.setter
	def cipher_suite_name(self,cipher_suite_name):
		try :
			if not isinstance(cipher_suite_name,str):
				raise TypeError("cipher_suite_name must be set to str value")
			self._cipher_suite_name = cipher_suite_name
		except Exception as e :
			raise e

	'''
	Use this operation to get all the possible cipher suite.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				db_cipher_suite_obj=db_cipher_suite()
				response = db_cipher_suite_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of db_cipher_suite resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			db_cipher_suite_obj = db_cipher_suite()
			option_ = options()
			option_._filter=filter_
			return db_cipher_suite_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the db_cipher_suite resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			db_cipher_suite_obj = db_cipher_suite()
			option_ = options()
			option_._count=True
			response = db_cipher_suite_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of db_cipher_suite resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			db_cipher_suite_obj = db_cipher_suite()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = db_cipher_suite_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(db_cipher_suite_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.db_cipher_suite
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(db_cipher_suite_responses, response, "db_cipher_suite_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.db_cipher_suite_response_array
				i=0
				error = [db_cipher_suite() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.db_cipher_suite_response_array
			i=0
			db_cipher_suite_objs = [db_cipher_suite() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_db_cipher_suite'):
					for props in obj._db_cipher_suite:
						result = service.payload_formatter.string_to_bulk_resource(db_cipher_suite_response,self.__class__.__name__,props)
						db_cipher_suite_objs[i] = result.db_cipher_suite
						i=i+1
			return db_cipher_suite_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(db_cipher_suite,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class db_cipher_suite_response(base_response):
	def __init__(self,length=1) :
		self.db_cipher_suite= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.db_cipher_suite= [ db_cipher_suite() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class db_cipher_suite_responses(base_response):
	def __init__(self,length=1) :
		self.db_cipher_suite_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.db_cipher_suite_response_array = [ db_cipher_suite() for _ in range(length)]
