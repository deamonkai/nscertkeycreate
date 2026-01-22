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
Configuration for NetScaler db certificate File resource
'''

class db_cert(base_resource):
	_version= ""
	_public_key_size= ""
	_valid_to= ""
	_subjaltname= ""
	_days_to_expiry= ""
	_db_root_cert= ""
	_db_server_key= ""
	_serial_number= ""
	_issuer= ""
	_status= ""
	_db_server_cert= ""
	_signature_algorithm= ""
	_fingerprint= ""
	_public_key_algorithm= ""
	_subject= ""
	_valid_from= ""
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
			return "db_cert"
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
			return "db_certs"
		except Exception as e :
			raise e



	'''
	get Version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e


	'''
	get Public Key Size
	'''
	@property
	def public_key_size(self) :
		try:
			return self._public_key_size
		except Exception as e :
			raise e


	'''
	get Valid To
	'''
	@property
	def valid_to(self) :
		try:
			return self._valid_to
		except Exception as e :
			raise e


	'''
	get Comma separated Subject Alternative Names
	'''
	@property
	def subjaltname(self) :
		try:
			return self._subjaltname
		except Exception as e :
			raise e


	'''
	get Days before database certificate expires
	'''
	@property
	def days_to_expiry(self) :
		try:
			return self._days_to_expiry
		except Exception as e :
			raise e


	'''
	get Server Certificate Name
	'''
	@property
	def db_root_cert(self) :
		try:
			return self._db_root_cert
		except Exception as e :
			raise e
	'''
	set Server Certificate Name
	'''
	@db_root_cert.setter
	def db_root_cert(self,db_root_cert):
		try :
			if not isinstance(db_root_cert,str):
				raise TypeError("db_root_cert must be set to str value")
			self._db_root_cert = db_root_cert
		except Exception as e :
			raise e


	'''
	get Server Key
	'''
	@property
	def db_server_key(self) :
		try:
			return self._db_server_key
		except Exception as e :
			raise e
	'''
	set Server Key
	'''
	@db_server_key.setter
	def db_server_key(self,db_server_key):
		try :
			if not isinstance(db_server_key,str):
				raise TypeError("db_server_key must be set to str value")
			self._db_server_key = db_server_key
		except Exception as e :
			raise e


	'''
	get Serial Number
	'''
	@property
	def serial_number(self) :
		try:
			return self._serial_number
		except Exception as e :
			raise e


	'''
	get Issuer
	'''
	@property
	def issuer(self) :
		try:
			return self._issuer
		except Exception as e :
			raise e


	'''
	get Tells whether the certificate is still valid or not
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e


	'''
	get Server Certificate Name
	'''
	@property
	def db_server_cert(self) :
		try:
			return self._db_server_cert
		except Exception as e :
			raise e
	'''
	set Server Certificate Name
	'''
	@db_server_cert.setter
	def db_server_cert(self,db_server_cert):
		try :
			if not isinstance(db_server_cert,str):
				raise TypeError("db_server_cert must be set to str value")
			self._db_server_cert = db_server_cert
		except Exception as e :
			raise e


	'''
	get Signature Algorithm
	'''
	@property
	def signature_algorithm(self) :
		try:
			return self._signature_algorithm
		except Exception as e :
			raise e


	'''
	get SHA-1 Fingerprint of NetScaler Console database Certificate
	'''
	@property
	def fingerprint(self) :
		try:
			return self._fingerprint
		except Exception as e :
			raise e
	'''
	set SHA-1 Fingerprint of NetScaler Console database Certificate
	'''
	@fingerprint.setter
	def fingerprint(self,fingerprint):
		try :
			if not isinstance(fingerprint,str):
				raise TypeError("fingerprint must be set to str value")
			self._fingerprint = fingerprint
		except Exception as e :
			raise e


	'''
	get Public Key Algorithm
	'''
	@property
	def public_key_algorithm(self) :
		try:
			return self._public_key_algorithm
		except Exception as e :
			raise e


	'''
	get Subject
	'''
	@property
	def subject(self) :
		try:
			return self._subject
		except Exception as e :
			raise e


	'''
	get Valid From
	'''
	@property
	def valid_from(self) :
		try:
			return self._valid_from
		except Exception as e :
			raise e

	'''
	Use this operation to get db certificate file.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				db_cert_obj=db_cert()
				response = db_cert_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of db_cert resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			db_cert_obj = db_cert()
			option_ = options()
			option_._filter=filter_
			return db_cert_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the db_cert resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			db_cert_obj = db_cert()
			option_ = options()
			option_._count=True
			response = db_cert_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of db_cert resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			db_cert_obj = db_cert()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = db_cert_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(db_cert_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.db_cert
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(db_cert_responses, response, "db_cert_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.db_cert_response_array
				i=0
				error = [db_cert() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.db_cert_response_array
			i=0
			db_cert_objs = [db_cert() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_db_cert'):
					for props in obj._db_cert:
						result = service.payload_formatter.string_to_bulk_resource(db_cert_response,self.__class__.__name__,props)
						db_cert_objs[i] = result.db_cert
						i=i+1
			return db_cert_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(db_cert,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class db_cert_response(base_response):
	def __init__(self,length=1) :
		self.db_cert= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.db_cert= [ db_cert() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class db_cert_responses(base_response):
	def __init__(self,length=1) :
		self.db_cert_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.db_cert_response_array = [ db_cert() for _ in range(length)]
