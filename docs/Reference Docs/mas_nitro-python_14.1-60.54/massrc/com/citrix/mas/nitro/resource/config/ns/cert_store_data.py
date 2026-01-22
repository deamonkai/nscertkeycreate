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
Configuration for SSL certificate file store on NetScaler Console resource
'''

class cert_store_data(base_resource):
	_certkeypair_name= ""
	_file_data= ""
	_id= ""
	_file_name= ""
	_fingerprint= ""
	_referenced_ic_cert_count= ""
	_is_installed= ""
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
			return "cert_store_data"
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
			return "cert_store_datas"
		except Exception as e :
			raise e



	'''
	get Cert Key Pair Name
	'''
	@property
	def certkeypair_name(self) :
		try:
			return self._certkeypair_name
		except Exception as e :
			raise e


	'''
	get Base64 encoded certificate file contents.
	'''
	@property
	def file_data(self) :
		try:
			return self._file_data
		except Exception as e :
			raise e
	'''
	set Base64 encoded certificate file contents.
	'''
	@file_data.setter
	def file_data(self,file_data):
		try :
			if not isinstance(file_data,str):
				raise TypeError("file_data must be set to str value")
			self._file_data = file_data
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all certificate store data entries. 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all certificate store data entries. 
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
	get Certificate file name.
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set Certificate file name.
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e


	'''
	get Fingerprint of certificate file
	'''
	@property
	def fingerprint(self) :
		try:
			return self._fingerprint
		except Exception as e :
			raise e

	'''
	Number of certificates(cert_store) referring this intermediate certificate across instances
	'''
	@property
	def referenced_ic_cert_count(self):
		try:
			return self._referenced_ic_cert_count
		except Exception as e :
			raise e
	'''
	Number of certificates(cert_store) referring this intermediate certificate across instances
	'''
	@referenced_ic_cert_count.setter
	def referenced_ic_cert_count(self,referenced_ic_cert_count):
		try :
			if not isinstance(referenced_ic_cert_count,int):
				raise TypeError("referenced_ic_cert_count must be set to int value")
			self._referenced_ic_cert_count = referenced_ic_cert_count
		except Exception as e :
			raise e

	'''
	Indicates if a cert is installed in an ADC,when display_name and action parameter are set in filter query
	'''
	@property
	def is_installed(self):
		try:
			return self._is_installed
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cert_store_data_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cert_store_data
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cert_store_data_responses, response, "cert_store_data_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cert_store_data_response_array
				i=0
				error = [cert_store_data() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cert_store_data_response_array
			i=0
			cert_store_data_objs = [cert_store_data() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cert_store_data'):
					for props in obj._cert_store_data:
						result = service.payload_formatter.string_to_bulk_resource(cert_store_data_response,self.__class__.__name__,props)
						cert_store_data_objs[i] = result.cert_store_data
						i=i+1
			return cert_store_data_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cert_store_data,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cert_store_data_response(base_response):
	def __init__(self,length=1) :
		self.cert_store_data= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cert_store_data= [ cert_store_data() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cert_store_data_responses(base_response):
	def __init__(self,length=1) :
		self.cert_store_data_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cert_store_data_response_array = [ cert_store_data() for _ in range(length)]
