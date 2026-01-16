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
from massrc.com.citrix.mas.nitro.resource.config.mps.acme_access_parameters import acme_access_parameters
from massrc.com.citrix.mas.nitro.resource.config.mps.acme_dns_cert_map import acme_dns_cert_map


'''
Configuration for ACME DNS provider configuration resource
'''

class acme_dns_provider_config(base_resource):
	_domain_pattern= ""
	_acme_dns_name= ""
	_dns_provider_name= ""
	_is_default= ""
	_dns_credentials_map=[]
	_dns_max_retries= ""
	_dns_sleep_time= ""
	_id= ""
	_is_active= ""
	_domain_info_required= ""
	_domain_count_required= ""
	_certificate_list=[]
	_certificate_count= ""
	_acme_ca_config_id= ""
	_renew_mode= ""
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
			return "acme_dns_provider_config"
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
			return "acme_dns_provider_configs"
		except Exception as e :
			raise e



	'''
	get Domain pattern for which this DNS provider is applicable. Example: *.example.com
	'''
	@property
	def domain_pattern(self) :
		try:
			return self._domain_pattern
		except Exception as e :
			raise e
	'''
	set Domain pattern for which this DNS provider is applicable. Example: *.example.com
	'''
	@domain_pattern.setter
	def domain_pattern(self,domain_pattern):
		try :
			if not isinstance(domain_pattern,str):
				raise TypeError("domain_pattern must be set to str value")
			self._domain_pattern = domain_pattern
		except Exception as e :
			raise e


	'''
	get ACME DNS name. This is the name used by acme.sh client to identify the DNS provider in ACME challenges.
	'''
	@property
	def acme_dns_name(self) :
		try:
			return self._acme_dns_name
		except Exception as e :
			raise e
	'''
	set ACME DNS name. This is the name used by acme.sh client to identify the DNS provider in ACME challenges.
	'''
	@acme_dns_name.setter
	def acme_dns_name(self,acme_dns_name):
		try :
			if not isinstance(acme_dns_name,str):
				raise TypeError("acme_dns_name must be set to str value")
			self._acme_dns_name = acme_dns_name
		except Exception as e :
			raise e


	'''
	get DNS Provider name. Values: 1.AWS_Route53, 2. Google_Cloud_DNS, 3. Azure_DNS
	'''
	@property
	def dns_provider_name(self) :
		try:
			return self._dns_provider_name
		except Exception as e :
			raise e
	'''
	set DNS Provider name. Values: 1.AWS_Route53, 2. Google_Cloud_DNS, 3. Azure_DNS
	'''
	@dns_provider_name.setter
	def dns_provider_name(self,dns_provider_name):
		try :
			if not isinstance(dns_provider_name,str):
				raise TypeError("dns_provider_name must be set to str value")
			self._dns_provider_name = dns_provider_name
		except Exception as e :
			raise e


	'''
	get Indicates if this is the default DNS Provider configuration
	'''
	@property
	def is_default(self) :
		try:
			return self._is_default
		except Exception as e :
			raise e
	'''
	set Indicates if this is the default DNS Provider configuration
	'''
	@is_default.setter
	def is_default(self,is_default):
		try :
			if not isinstance(is_default,bool):
				raise TypeError("is_default must be set to bool value")
			self._is_default = is_default
		except Exception as e :
			raise e


	'''
	get Array of key and value for DNS credentials. The key is the credential name and the value is the credential value.
	'''
	@property
	def dns_credentials_map(self) :
		try:
			return self._dns_credentials_map
		except Exception as e :
			raise e
	'''
	set Array of key and value for DNS credentials. The key is the credential name and the value is the credential value.
	'''
	@dns_credentials_map.setter
	def dns_credentials_map(self,dns_credentials_map) :
		try :
			if not isinstance(dns_credentials_map,list):
				raise TypeError("dns_credentials_map must be set to array of acme_access_parameters value")
			for item in dns_credentials_map :
				if not isinstance(item,acme_access_parameters):
					raise TypeError("item must be set to acme_access_parameters value")
			self._dns_credentials_map = dns_credentials_map
		except Exception as e :
			raise e


	'''
	get Maximum number of attempts to check for DNS record existence during ACME challenge verification.
	'''
	@property
	def dns_max_retries(self) :
		try:
			return self._dns_max_retries
		except Exception as e :
			raise e
	'''
	set Maximum number of attempts to check for DNS record existence during ACME challenge verification.
	'''
	@dns_max_retries.setter
	def dns_max_retries(self,dns_max_retries):
		try :
			if not isinstance(dns_max_retries,int):
				raise TypeError("dns_max_retries must be set to int value")
			self._dns_max_retries = dns_max_retries
		except Exception as e :
			raise e


	'''
	get One-time sleep duration (in seconds) to wait after creating DNS records before starting ACME challenge verification for all domains.
	'''
	@property
	def dns_sleep_time(self) :
		try:
			return self._dns_sleep_time
		except Exception as e :
			raise e
	'''
	set One-time sleep duration (in seconds) to wait after creating DNS records before starting ACME challenge verification for all domains.
	'''
	@dns_sleep_time.setter
	def dns_sleep_time(self,dns_sleep_time):
		try :
			if not isinstance(dns_sleep_time,int):
				raise TypeError("dns_sleep_time must be set to int value")
			self._dns_sleep_time = dns_sleep_time
		except Exception as e :
			raise e


	'''
	get Id is system generated key for DNS provider configuration.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for DNS provider configuration.
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
	get Indicates if this DNS Provider configuration is active (configuration is complete). If false, it will not be used for ACME challenges.
	'''
	@property
	def is_active(self) :
		try:
			return self._is_active
		except Exception as e :
			raise e
	'''
	set Indicates if this DNS Provider configuration is active (configuration is complete). If false, it will not be used for ACME challenges.
	'''
	@is_active.setter
	def is_active(self,is_active):
		try :
			if not isinstance(is_active,bool):
				raise TypeError("is_active must be set to bool value")
			self._is_active = is_active
		except Exception as e :
			raise e

	'''
	Set to true, if the DNS provider requires domain information to be provided for each DNS Provider
	'''
	@property
	def domain_info_required(self):
		try:
			return self._domain_info_required
		except Exception as e :
			raise e
	'''
	Set to true, if the DNS provider requires domain information to be provided for each DNS Provider
	'''
	@domain_info_required.setter
	def domain_info_required(self,domain_info_required):
		try :
			if not isinstance(domain_info_required,bool):
				raise TypeError("domain_info_required must be set to bool value")
			self._domain_info_required = domain_info_required
		except Exception as e :
			raise e

	'''
	Set to true, if the DNS provider requires domain count to be provided for each DNS Provider
	'''
	@property
	def domain_count_required(self):
		try:
			return self._domain_count_required
		except Exception as e :
			raise e
	'''
	Set to true, if the DNS provider requires domain count to be provided for each DNS Provider
	'''
	@domain_count_required.setter
	def domain_count_required(self,domain_count_required):
		try :
			if not isinstance(domain_count_required,bool):
				raise TypeError("domain_count_required must be set to bool value")
			self._domain_count_required = domain_count_required
		except Exception as e :
			raise e

	'''
	Array of certificate IDs associated with this DNS Provider configuration. This is used to link the DNS Provider with the certificates that use it for ACME challenges.
	'''
	@property
	def certificate_list(self) :
		try:
			return self._certificate_list
		except Exception as e :
			raise e
	'''
	Array of certificate IDs associated with this DNS Provider configuration. This is used to link the DNS Provider with the certificates that use it for ACME challenges.
	'''
	@certificate_list.setter
	def certificate_list(self,certificate_list) :
		try :
			if not isinstance(certificate_list,list):
				raise TypeError("certificate_list must be set to array of acme_dns_cert_map value")
			for item in certificate_list :
				if not isinstance(item,acme_dns_cert_map):
					raise TypeError("item must be set to acme_dns_cert_map value")
			self._certificate_list = certificate_list
		except Exception as e :
			raise e

	'''
	Number of certificates/domain associated with this DNS Provider configuration
	'''
	@property
	def certificate_count(self):
		try:
			return self._certificate_count
		except Exception as e :
			raise e
	'''
	Number of certificates/domain associated with this DNS Provider configuration
	'''
	@certificate_count.setter
	def certificate_count(self,certificate_count):
		try :
			if not isinstance(certificate_count,int):
				raise TypeError("certificate_count must be set to int value")
			self._certificate_count = certificate_count
		except Exception as e :
			raise e

	'''
	ID for CA Configuration
	'''
	@property
	def acme_ca_config_id(self):
		try:
			return self._acme_ca_config_id
		except Exception as e :
			raise e
	'''
	ID for CA Configuration
	'''
	@acme_ca_config_id.setter
	def acme_ca_config_id(self,acme_ca_config_id):
		try :
			if not isinstance(acme_ca_config_id,str):
				raise TypeError("acme_ca_config_id must be set to str value")
			self._acme_ca_config_id = acme_ca_config_id
		except Exception as e :
			raise e

	'''
	Renew mode for the certificate. It can be MANUAL or AUTO.
	'''
	@property
	def renew_mode(self):
		try:
			return self._renew_mode
		except Exception as e :
			raise e
	'''
	Renew mode for the certificate. It can be MANUAL or AUTO.
	'''
	@renew_mode.setter
	def renew_mode(self,renew_mode):
		try :
			if not isinstance(renew_mode,str):
				raise TypeError("renew_mode must be set to str value")
			self._renew_mode = renew_mode
		except Exception as e :
			raise e

	'''
	Delete ACME DNS vs Domain mapping configuration.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.delete_resource(client)
				return res
			else :
					acme_dns_provider_config_obj=acme_dns_provider_config()
					return cls.delete_bulk_request(client,resource,acme_dns_provider_config_obj)
		except Exception as e :
			raise e

	'''
	Update ACME DNS vs Domain mapping configuration.
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
				acme_dns_provider_config_obj=acme_dns_provider_config()
				return cls.update_bulk_request(client,resource,acme_dns_provider_config_obj)
		except Exception as e :
			raise e

	'''
	get DNS vs Domain mapping configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				acme_dns_provider_config_obj=acme_dns_provider_config()
				response = acme_dns_provider_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of acme_dns_provider_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			acme_dns_provider_config_obj = acme_dns_provider_config()
			option_ = options()
			option_._filter=filter_
			return acme_dns_provider_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the acme_dns_provider_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			acme_dns_provider_config_obj = acme_dns_provider_config()
			option_ = options()
			option_._count=True
			response = acme_dns_provider_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of acme_dns_provider_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			acme_dns_provider_config_obj = acme_dns_provider_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = acme_dns_provider_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(acme_dns_provider_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.acme_dns_provider_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(acme_dns_provider_config_responses, response, "acme_dns_provider_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.acme_dns_provider_config_response_array
				i=0
				error = [acme_dns_provider_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.acme_dns_provider_config_response_array
			i=0
			acme_dns_provider_config_objs = [acme_dns_provider_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_acme_dns_provider_config'):
					for props in obj._acme_dns_provider_config:
						result = service.payload_formatter.string_to_bulk_resource(acme_dns_provider_config_response,self.__class__.__name__,props)
						acme_dns_provider_config_objs[i] = result.acme_dns_provider_config
						i=i+1
			return acme_dns_provider_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(acme_dns_provider_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class acme_dns_provider_config_response(base_response):
	def __init__(self,length=1) :
		self.acme_dns_provider_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.acme_dns_provider_config= [ acme_dns_provider_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class acme_dns_provider_config_responses(base_response):
	def __init__(self,length=1) :
		self.acme_dns_provider_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.acme_dns_provider_config_response_array = [ acme_dns_provider_config() for _ in range(length)]
