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
from massrc.com.citrix.mas.nitro.resource.config.mps.db_cipher_suite import db_cipher_suite


'''
Configuration for Database Cipher Suites resource
'''

class db_cipher_suites(base_resource):
	_cipher_suites=[]
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
			return "db_cipher_suites"
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
			return "db_cipher_suitess"
		except Exception as e :
			raise e



	'''
	get List of database cipher suites
	'''
	@property
	def cipher_suites(self) :
		try:
			return self._cipher_suites
		except Exception as e :
			raise e
	'''
	set List of database cipher suites
	'''
	@cipher_suites.setter
	def cipher_suites(self,cipher_suites) :
		try :
			if not isinstance(cipher_suites,list):
				raise TypeError("cipher_suites must be set to array of db_cipher_suite value")
			for item in cipher_suites :
				if not isinstance(item,db_cipher_suite):
					raise TypeError("item must be set to db_cipher_suite value")
			self._cipher_suites = cipher_suites
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
				db_cipher_suites_obj=db_cipher_suites()
				response = db_cipher_suites_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	modify the cipher suite of the database.
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
				db_cipher_suites_obj=db_cipher_suites()
				return cls.update_bulk_request(client,resource,db_cipher_suites_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of db_cipher_suites resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			db_cipher_suites_obj = db_cipher_suites()
			option_ = options()
			option_._filter=filter_
			return db_cipher_suites_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the db_cipher_suites resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			db_cipher_suites_obj = db_cipher_suites()
			option_ = options()
			option_._count=True
			response = db_cipher_suites_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of db_cipher_suites resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			db_cipher_suites_obj = db_cipher_suites()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = db_cipher_suites_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(db_cipher_suites_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.db_cipher_suites
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(db_cipher_suites_responses, response, "db_cipher_suites_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.db_cipher_suites_response_array
				i=0
				error = [db_cipher_suites() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.db_cipher_suites_response_array
			i=0
			db_cipher_suites_objs = [db_cipher_suites() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_db_cipher_suites'):
					for props in obj._db_cipher_suites:
						result = service.payload_formatter.string_to_bulk_resource(db_cipher_suites_response,self.__class__.__name__,props)
						db_cipher_suites_objs[i] = result.db_cipher_suites
						i=i+1
			return db_cipher_suites_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(db_cipher_suites,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class db_cipher_suites_response(base_response):
	def __init__(self,length=1) :
		self.db_cipher_suites= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.db_cipher_suites= [ db_cipher_suites() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class db_cipher_suites_responses(base_response):
	def __init__(self,length=1) :
		self.db_cipher_suites_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.db_cipher_suites_response_array = [ db_cipher_suites() for _ in range(length)]
