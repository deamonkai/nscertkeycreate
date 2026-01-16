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
from massrc.com.citrix.mas.nitro.resource.config.mps.property_map import property_map
from massrc.com.citrix.mas.nitro.resource.config.mps.property_map import property_map
from massrc.com.citrix.mas.nitro.resource.config.mps.property_map import property_map
from massrc.com.citrix.mas.nitro.resource.config.mps.property_map import property_map
from massrc.com.citrix.mas.nitro.resource.config.mps.property_map import property_map
from massrc.com.citrix.mas.nitro.resource.config.mps.property_map import property_map
from massrc.com.citrix.mas.nitro.resource.config.mps.property_map import property_map


'''
Configuration for SSL certificate store summary on NetScaler Console resource
'''

class cert_store_summary(base_resource):
	_cert_sign=[]
	_cert_expiry=[]
	_cert_algorithm=[]
	_cert_issuer=[]
	_cert_bound_apps=[]
	_cert_usage=[]
	_total_certs= ""
	_cert_key=[]
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
			return "cert_store_summary"
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
			return "cert_store_summarys"
		except Exception as e :
			raise e



	'''
	get Certificates by signing(self/ca)
	'''
	@property
	def cert_sign(self) :
		try:
			return self._cert_sign
		except Exception as e :
			raise e
	'''
	set Certificates by signing(self/ca)
	'''
	@cert_sign.setter
	def cert_sign(self,cert_sign) :
		try :
			if not isinstance(cert_sign,list):
				raise TypeError("cert_sign must be set to array of property_map value")
			for item in cert_sign :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._cert_sign = cert_sign
		except Exception as e :
			raise e


	'''
	get Certificates by expiry
	'''
	@property
	def cert_expiry(self) :
		try:
			return self._cert_expiry
		except Exception as e :
			raise e
	'''
	set Certificates by expiry
	'''
	@cert_expiry.setter
	def cert_expiry(self,cert_expiry) :
		try :
			if not isinstance(cert_expiry,list):
				raise TypeError("cert_expiry must be set to array of property_map value")
			for item in cert_expiry :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._cert_expiry = cert_expiry
		except Exception as e :
			raise e


	'''
	get Certificates by signature algorithm
	'''
	@property
	def cert_algorithm(self) :
		try:
			return self._cert_algorithm
		except Exception as e :
			raise e
	'''
	set Certificates by signature algorithm
	'''
	@cert_algorithm.setter
	def cert_algorithm(self,cert_algorithm) :
		try :
			if not isinstance(cert_algorithm,list):
				raise TypeError("cert_algorithm must be set to array of property_map value")
			for item in cert_algorithm :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._cert_algorithm = cert_algorithm
		except Exception as e :
			raise e


	'''
	get Certificate by issuer
	'''
	@property
	def cert_issuer(self) :
		try:
			return self._cert_issuer
		except Exception as e :
			raise e
	'''
	set Certificate by issuer
	'''
	@cert_issuer.setter
	def cert_issuer(self,cert_issuer) :
		try :
			if not isinstance(cert_issuer,list):
				raise TypeError("cert_issuer must be set to array of property_map value")
			for item in cert_issuer :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._cert_issuer = cert_issuer
		except Exception as e :
			raise e


	'''
	get Applications bound to each certificate
	'''
	@property
	def cert_bound_apps(self) :
		try:
			return self._cert_bound_apps
		except Exception as e :
			raise e
	'''
	set Applications bound to each certificate
	'''
	@cert_bound_apps.setter
	def cert_bound_apps(self,cert_bound_apps) :
		try :
			if not isinstance(cert_bound_apps,list):
				raise TypeError("cert_bound_apps must be set to array of property_map value")
			for item in cert_bound_apps :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._cert_bound_apps = cert_bound_apps
		except Exception as e :
			raise e


	'''
	get Certificate by its usage
	'''
	@property
	def cert_usage(self) :
		try:
			return self._cert_usage
		except Exception as e :
			raise e
	'''
	set Certificate by its usage
	'''
	@cert_usage.setter
	def cert_usage(self,cert_usage) :
		try :
			if not isinstance(cert_usage,list):
				raise TypeError("cert_usage must be set to array of property_map value")
			for item in cert_usage :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._cert_usage = cert_usage
		except Exception as e :
			raise e


	'''
	get Total number of certificates
	'''
	@property
	def total_certs(self) :
		try:
			return self._total_certs
		except Exception as e :
			raise e


	'''
	get Certificates by key strength
	'''
	@property
	def cert_key(self) :
		try:
			return self._cert_key
		except Exception as e :
			raise e
	'''
	set Certificates by key strength
	'''
	@cert_key.setter
	def cert_key(self,cert_key) :
		try :
			if not isinstance(cert_key,list):
				raise TypeError("cert_key must be set to array of property_map value")
			for item in cert_key :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._cert_key = cert_key
		except Exception as e :
			raise e

	'''
	Use this operation to get details of a certificate stored in cert store.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				cert_store_summary_obj=cert_store_summary()
				response = cert_store_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cert_store_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cert_store_summary_obj = cert_store_summary()
			option_ = options()
			option_._filter=filter_
			return cert_store_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cert_store_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cert_store_summary_obj = cert_store_summary()
			option_ = options()
			option_._count=True
			response = cert_store_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cert_store_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cert_store_summary_obj = cert_store_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cert_store_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cert_store_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cert_store_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cert_store_summary_responses, response, "cert_store_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cert_store_summary_response_array
				i=0
				error = [cert_store_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cert_store_summary_response_array
			i=0
			cert_store_summary_objs = [cert_store_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cert_store_summary'):
					for props in obj._cert_store_summary:
						result = service.payload_formatter.string_to_bulk_resource(cert_store_summary_response,self.__class__.__name__,props)
						cert_store_summary_objs[i] = result.cert_store_summary
						i=i+1
			return cert_store_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cert_store_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cert_store_summary_response(base_response):
	def __init__(self,length=1) :
		self.cert_store_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cert_store_summary= [ cert_store_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cert_store_summary_responses(base_response):
	def __init__(self,length=1) :
		self.cert_store_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cert_store_summary_response_array = [ cert_store_summary() for _ in range(length)]
