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
Configuration for Details of linked certificate resource
'''

class certkey_chain_link(base_resource):
	_linked_to= ""
	_valid_from= ""
	_certificate_file_name= ""
	_issuer= ""
	_cert_name= ""
	_valid_to= ""
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
			return "certkey_chain_link"
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
			return "certkey_chain_links"
		except Exception as e :
			raise e



	'''
	get Name of certificate to which the certificate is linked
	'''
	@property
	def linked_to(self) :
		try:
			return self._linked_to
		except Exception as e :
			raise e
	'''
	set Name of certificate to which the certificate is linked
	'''
	@linked_to.setter
	def linked_to(self,linked_to):
		try :
			if not isinstance(linked_to,str):
				raise TypeError("linked_to must be set to str value")
			self._linked_to = linked_to
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
	set Valid From
	'''
	@valid_from.setter
	def valid_from(self,valid_from):
		try :
			if not isinstance(valid_from,str):
				raise TypeError("valid_from must be set to str value")
			self._valid_from = valid_from
		except Exception as e :
			raise e


	'''
	get Certificate File Name
	'''
	@property
	def certificate_file_name(self) :
		try:
			return self._certificate_file_name
		except Exception as e :
			raise e
	'''
	set Certificate File Name
	'''
	@certificate_file_name.setter
	def certificate_file_name(self,certificate_file_name):
		try :
			if not isinstance(certificate_file_name,str):
				raise TypeError("certificate_file_name must be set to str value")
			self._certificate_file_name = certificate_file_name
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
	set Issuer
	'''
	@issuer.setter
	def issuer(self,issuer):
		try :
			if not isinstance(issuer,str):
				raise TypeError("issuer must be set to str value")
			self._issuer = issuer
		except Exception as e :
			raise e


	'''
	get Certificate name
	'''
	@property
	def cert_name(self) :
		try:
			return self._cert_name
		except Exception as e :
			raise e
	'''
	set Certificate name
	'''
	@cert_name.setter
	def cert_name(self,cert_name):
		try :
			if not isinstance(cert_name,str):
				raise TypeError("cert_name must be set to str value")
			self._cert_name = cert_name
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
	set Valid To
	'''
	@valid_to.setter
	def valid_to(self,valid_to):
		try :
			if not isinstance(valid_to,str):
				raise TypeError("valid_to must be set to str value")
			self._valid_to = valid_to
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(certkey_chain_link_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.certkey_chain_link
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(certkey_chain_link_responses, response, "certkey_chain_link_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.certkey_chain_link_response_array
				i=0
				error = [certkey_chain_link() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.certkey_chain_link_response_array
			i=0
			certkey_chain_link_objs = [certkey_chain_link() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_certkey_chain_link'):
					for props in obj._certkey_chain_link:
						result = service.payload_formatter.string_to_bulk_resource(certkey_chain_link_response,self.__class__.__name__,props)
						certkey_chain_link_objs[i] = result.certkey_chain_link
						i=i+1
			return certkey_chain_link_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(certkey_chain_link,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class certkey_chain_link_response(base_response):
	def __init__(self,length=1) :
		self.certkey_chain_link= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.certkey_chain_link= [ certkey_chain_link() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class certkey_chain_link_responses(base_response):
	def __init__(self,length=1) :
		self.certkey_chain_link_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.certkey_chain_link_response_array = [ certkey_chain_link() for _ in range(length)]
