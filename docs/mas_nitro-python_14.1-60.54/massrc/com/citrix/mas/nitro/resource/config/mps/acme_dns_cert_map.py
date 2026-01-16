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
Configuration for ACME DNS Cert Domain mapping configuration resource
'''

class acme_dns_cert_map(base_resource):
	_id= ""
	_issued_by_org= ""
	_name= ""
	_domain= ""
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
			return "acme_dns_cert_map"
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
			return "acme_dns_cert_maps"
		except Exception as e :
			raise e



	'''
	get Id is system generated key for DNS mapping configuration.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for DNS mapping configuration.
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
	get Issued Organization from the subject of the certificate
	'''
	@property
	def issued_by_org(self) :
		try:
			return self._issued_by_org
		except Exception as e :
			raise e
	'''
	set Issued Organization from the subject of the certificate
	'''
	@issued_by_org.setter
	def issued_by_org(self,issued_by_org):
		try :
			if not isinstance(issued_by_org,str):
				raise TypeError("issued_by_org must be set to str value")
			self._issued_by_org = issued_by_org
		except Exception as e :
			raise e


	'''
	get Name of the cert
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the cert
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get Domain name from the subject of the certificate
	'''
	@property
	def domain(self) :
		try:
			return self._domain
		except Exception as e :
			raise e
	'''
	set Domain name from the subject of the certificate
	'''
	@domain.setter
	def domain(self,domain):
		try :
			if not isinstance(domain,str):
				raise TypeError("domain must be set to str value")
			self._domain = domain
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(acme_dns_cert_map_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.acme_dns_cert_map
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(acme_dns_cert_map_responses, response, "acme_dns_cert_map_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.acme_dns_cert_map_response_array
				i=0
				error = [acme_dns_cert_map() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.acme_dns_cert_map_response_array
			i=0
			acme_dns_cert_map_objs = [acme_dns_cert_map() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_acme_dns_cert_map'):
					for props in obj._acme_dns_cert_map:
						result = service.payload_formatter.string_to_bulk_resource(acme_dns_cert_map_response,self.__class__.__name__,props)
						acme_dns_cert_map_objs[i] = result.acme_dns_cert_map
						i=i+1
			return acme_dns_cert_map_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(acme_dns_cert_map,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class acme_dns_cert_map_response(base_response):
	def __init__(self,length=1) :
		self.acme_dns_cert_map= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.acme_dns_cert_map= [ acme_dns_cert_map() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class acme_dns_cert_map_responses(base_response):
	def __init__(self,length=1) :
		self.acme_dns_cert_map_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.acme_dns_cert_map_response_array = [ acme_dns_cert_map() for _ in range(length)]
