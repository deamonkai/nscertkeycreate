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
Configuration for Venafi certificate policy resource
'''

class certificate_policy(base_resource):
	_is_csr_generation_locked= ""
	_ca= ""
	_org= ""
	_is_key_value_locked= ""
	_is_org_locked= ""
	_state= ""
	_wildcards_allowed= ""
	_tp_renewal= ""
	_is_city_locked= ""
	_is_ca_locked= ""
	_is_keypair_algorithm_locked= ""
	_is_state_locked= ""
	_tp_renewal_locked= ""
	_csr_generation= ""
	_subjaltname_ip_allowed= ""
	_management_type= ""
	_is_key_generation_locked= ""
	_key_value= ""
	_policy= ""
	_country= ""
	_city= ""
	_name= ""
	_org_unit=[]
	_is_org_unit_locked= ""
	_key_generation= ""
	_is_country_locked= ""
	_subjaltname_upn_allowed= ""
	_keypair_algorithm= ""
	_subjaltname_email_allowed= ""
	_subjaltname_uri_allowed= ""
	_is_management_type_locked= ""
	_subjaltname_dns_allowed= ""
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
			return "certificate_policy"
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
			return "certificate_policys"
		except Exception as e :
			raise e



	'''
	get Indicates if the CsrGeneration value is locked in the policy
	'''
	@property
	def is_csr_generation_locked(self) :
		try:
			return self._is_csr_generation_locked
		except Exception as e :
			raise e
	'''
	set Indicates if the CsrGeneration value is locked in the policy
	'''
	@is_csr_generation_locked.setter
	def is_csr_generation_locked(self,is_csr_generation_locked):
		try :
			if not isinstance(is_csr_generation_locked,bool):
				raise TypeError("is_csr_generation_locked must be set to bool value")
			self._is_csr_generation_locked = is_csr_generation_locked
		except Exception as e :
			raise e


	'''
	get Certificate Authority
	'''
	@property
	def ca(self) :
		try:
			return self._ca
		except Exception as e :
			raise e
	'''
	set Certificate Authority
	'''
	@ca.setter
	def ca(self,ca):
		try :
			if not isinstance(ca,str):
				raise TypeError("ca must be set to str value")
			self._ca = ca
		except Exception as e :
			raise e


	'''
	get Organization
	'''
	@property
	def org(self) :
		try:
			return self._org
		except Exception as e :
			raise e
	'''
	set Organization
	'''
	@org.setter
	def org(self,org):
		try :
			if not isinstance(org,str):
				raise TypeError("org must be set to str value")
			self._org = org
		except Exception as e :
			raise e


	'''
	get Indicates if the algorithm property value is locked in the policy
	'''
	@property
	def is_key_value_locked(self) :
		try:
			return self._is_key_value_locked
		except Exception as e :
			raise e
	'''
	set Indicates if the algorithm property value is locked in the policy
	'''
	@is_key_value_locked.setter
	def is_key_value_locked(self,is_key_value_locked):
		try :
			if not isinstance(is_key_value_locked,bool):
				raise TypeError("is_key_value_locked must be set to bool value")
			self._is_key_value_locked = is_key_value_locked
		except Exception as e :
			raise e


	'''
	get Indicates if the organization value is locked
	'''
	@property
	def is_org_locked(self) :
		try:
			return self._is_org_locked
		except Exception as e :
			raise e
	'''
	set Indicates if the organization value is locked
	'''
	@is_org_locked.setter
	def is_org_locked(self,is_org_locked):
		try :
			if not isinstance(is_org_locked,bool):
				raise TypeError("is_org_locked must be set to bool value")
			self._is_org_locked = is_org_locked
		except Exception as e :
			raise e


	'''
	get State
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set State
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
		except Exception as e :
			raise e


	'''
	get Indicates if wild cards is allowed
	'''
	@property
	def wildcards_allowed(self) :
		try:
			return self._wildcards_allowed
		except Exception as e :
			raise e
	'''
	set Indicates if wild cards is allowed
	'''
	@wildcards_allowed.setter
	def wildcards_allowed(self,wildcards_allowed):
		try :
			if not isinstance(wildcards_allowed,bool):
				raise TypeError("wildcards_allowed must be set to bool value")
			self._wildcards_allowed = wildcards_allowed
		except Exception as e :
			raise e


	'''
	get set to True, if automatic renewal is enabled in Venafi
	'''
	@property
	def tp_renewal(self) :
		try:
			return self._tp_renewal
		except Exception as e :
			raise e
	'''
	set set to True, if automatic renewal is enabled in Venafi
	'''
	@tp_renewal.setter
	def tp_renewal(self,tp_renewal):
		try :
			if not isinstance(tp_renewal,bool):
				raise TypeError("tp_renewal must be set to bool value")
			self._tp_renewal = tp_renewal
		except Exception as e :
			raise e


	'''
	get Indicates if the city value is locked
	'''
	@property
	def is_city_locked(self) :
		try:
			return self._is_city_locked
		except Exception as e :
			raise e
	'''
	set Indicates if the city value is locked
	'''
	@is_city_locked.setter
	def is_city_locked(self,is_city_locked):
		try :
			if not isinstance(is_city_locked,bool):
				raise TypeError("is_city_locked must be set to bool value")
			self._is_city_locked = is_city_locked
		except Exception as e :
			raise e


	'''
	get Indicates if the CA value is locked in the policy
	'''
	@property
	def is_ca_locked(self) :
		try:
			return self._is_ca_locked
		except Exception as e :
			raise e
	'''
	set Indicates if the CA value is locked in the policy
	'''
	@is_ca_locked.setter
	def is_ca_locked(self,is_ca_locked):
		try :
			if not isinstance(is_ca_locked,bool):
				raise TypeError("is_ca_locked must be set to bool value")
			self._is_ca_locked = is_ca_locked
		except Exception as e :
			raise e


	'''
	get Indicates if the key pair algorithm value is locked in the policy
	'''
	@property
	def is_keypair_algorithm_locked(self) :
		try:
			return self._is_keypair_algorithm_locked
		except Exception as e :
			raise e
	'''
	set Indicates if the key pair algorithm value is locked in the policy
	'''
	@is_keypair_algorithm_locked.setter
	def is_keypair_algorithm_locked(self,is_keypair_algorithm_locked):
		try :
			if not isinstance(is_keypair_algorithm_locked,bool):
				raise TypeError("is_keypair_algorithm_locked must be set to bool value")
			self._is_keypair_algorithm_locked = is_keypair_algorithm_locked
		except Exception as e :
			raise e


	'''
	get Indicates if the state value is locked
	'''
	@property
	def is_state_locked(self) :
		try:
			return self._is_state_locked
		except Exception as e :
			raise e
	'''
	set Indicates if the state value is locked
	'''
	@is_state_locked.setter
	def is_state_locked(self,is_state_locked):
		try :
			if not isinstance(is_state_locked,bool):
				raise TypeError("is_state_locked must be set to bool value")
			self._is_state_locked = is_state_locked
		except Exception as e :
			raise e


	'''
	get Indicates if TpRenewal is locked
	'''
	@property
	def tp_renewal_locked(self) :
		try:
			return self._tp_renewal_locked
		except Exception as e :
			raise e
	'''
	set Indicates if TpRenewal is locked
	'''
	@tp_renewal_locked.setter
	def tp_renewal_locked(self,tp_renewal_locked):
		try :
			if not isinstance(tp_renewal_locked,bool):
				raise TypeError("tp_renewal_locked must be set to bool value")
			self._tp_renewal_locked = tp_renewal_locked
		except Exception as e :
			raise e


	'''
	get CSR generation.Possible values: ServiceGenerated, UserGenerated
	'''
	@property
	def csr_generation(self) :
		try:
			return self._csr_generation
		except Exception as e :
			raise e
	'''
	set CSR generation.Possible values: ServiceGenerated, UserGenerated
	'''
	@csr_generation.setter
	def csr_generation(self,csr_generation):
		try :
			if not isinstance(csr_generation,str):
				raise TypeError("csr_generation must be set to str value")
			self._csr_generation = csr_generation
		except Exception as e :
			raise e


	'''
	get Indicates if IP subject alternative names allowed
	'''
	@property
	def subjaltname_ip_allowed(self) :
		try:
			return self._subjaltname_ip_allowed
		except Exception as e :
			raise e
	'''
	set Indicates if IP subject alternative names allowed
	'''
	@subjaltname_ip_allowed.setter
	def subjaltname_ip_allowed(self,subjaltname_ip_allowed):
		try :
			if not isinstance(subjaltname_ip_allowed,bool):
				raise TypeError("subjaltname_ip_allowed must be set to bool value")
			self._subjaltname_ip_allowed = subjaltname_ip_allowed
		except Exception as e :
			raise e


	'''
	get Management Type
	'''
	@property
	def management_type(self) :
		try:
			return self._management_type
		except Exception as e :
			raise e
	'''
	set Management Type
	'''
	@management_type.setter
	def management_type(self,management_type):
		try :
			if not isinstance(management_type,str):
				raise TypeError("management_type must be set to str value")
			self._management_type = management_type
		except Exception as e :
			raise e


	'''
	get Indicates if the key generation value is locked in the policy
	'''
	@property
	def is_key_generation_locked(self) :
		try:
			return self._is_key_generation_locked
		except Exception as e :
			raise e
	'''
	set Indicates if the key generation value is locked in the policy
	'''
	@is_key_generation_locked.setter
	def is_key_generation_locked(self,is_key_generation_locked):
		try :
			if not isinstance(is_key_generation_locked,bool):
				raise TypeError("is_key_generation_locked must be set to bool value")
			self._is_key_generation_locked = is_key_generation_locked
		except Exception as e :
			raise e


	'''
	get Key strength if algorithm is RSA. EllipticCurve ,if the algorithm is ECC 
	'''
	@property
	def key_value(self) :
		try:
			return self._key_value
		except Exception as e :
			raise e
	'''
	set Key strength if algorithm is RSA. EllipticCurve ,if the algorithm is ECC 
	'''
	@key_value.setter
	def key_value(self,key_value):
		try :
			if not isinstance(key_value,str):
				raise TypeError("key_value must be set to str value")
			self._key_value = key_value
		except Exception as e :
			raise e


	'''
	get Policy folder path which determines the certificate attributes.
	'''
	@property
	def policy(self) :
		try:
			return self._policy
		except Exception as e :
			raise e
	'''
	set Policy folder path which determines the certificate attributes.
	'''
	@policy.setter
	def policy(self,policy):
		try :
			if not isinstance(policy,str):
				raise TypeError("policy must be set to str value")
			self._policy = policy
		except Exception as e :
			raise e


	'''
	get country
	'''
	@property
	def country(self) :
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	set country
	'''
	@country.setter
	def country(self,country):
		try :
			if not isinstance(country,str):
				raise TypeError("country must be set to str value")
			self._country = country
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
	get Name of the Venafi server configured.
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the Venafi server configured.
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
	get Organization Unit
	'''
	@property
	def org_unit(self) :
		try:
			return self._org_unit
		except Exception as e :
			raise e
	'''
	set Organization Unit
	'''
	@org_unit.setter
	def org_unit(self,org_unit) :
		try :
			if not isinstance(org_unit,list):
				raise TypeError("org_unit must be set to array of str value")
			for item in org_unit :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._org_unit = org_unit
		except Exception as e :
			raise e


	'''
	get Indicates if the organization unit value is locked
	'''
	@property
	def is_org_unit_locked(self) :
		try:
			return self._is_org_unit_locked
		except Exception as e :
			raise e
	'''
	set Indicates if the organization unit value is locked
	'''
	@is_org_unit_locked.setter
	def is_org_unit_locked(self,is_org_unit_locked):
		try :
			if not isinstance(is_org_unit_locked,bool):
				raise TypeError("is_org_unit_locked must be set to bool value")
			self._is_org_unit_locked = is_org_unit_locked
		except Exception as e :
			raise e


	'''
	get Key generation value
	'''
	@property
	def key_generation(self) :
		try:
			return self._key_generation
		except Exception as e :
			raise e
	'''
	set Key generation value
	'''
	@key_generation.setter
	def key_generation(self,key_generation):
		try :
			if not isinstance(key_generation,str):
				raise TypeError("key_generation must be set to str value")
			self._key_generation = key_generation
		except Exception as e :
			raise e


	'''
	get Indicates if the country value is locked
	'''
	@property
	def is_country_locked(self) :
		try:
			return self._is_country_locked
		except Exception as e :
			raise e
	'''
	set Indicates if the country value is locked
	'''
	@is_country_locked.setter
	def is_country_locked(self,is_country_locked):
		try :
			if not isinstance(is_country_locked,bool):
				raise TypeError("is_country_locked must be set to bool value")
			self._is_country_locked = is_country_locked
		except Exception as e :
			raise e


	'''
	get Indicates if UPN subject alternative names allowed
	'''
	@property
	def subjaltname_upn_allowed(self) :
		try:
			return self._subjaltname_upn_allowed
		except Exception as e :
			raise e
	'''
	set Indicates if UPN subject alternative names allowed
	'''
	@subjaltname_upn_allowed.setter
	def subjaltname_upn_allowed(self,subjaltname_upn_allowed):
		try :
			if not isinstance(subjaltname_upn_allowed,bool):
				raise TypeError("subjaltname_upn_allowed must be set to bool value")
			self._subjaltname_upn_allowed = subjaltname_upn_allowed
		except Exception as e :
			raise e


	'''
	get Algorithm for generating the key. Possible values: ECC, RSA
	'''
	@property
	def keypair_algorithm(self) :
		try:
			return self._keypair_algorithm
		except Exception as e :
			raise e
	'''
	set Algorithm for generating the key. Possible values: ECC, RSA
	'''
	@keypair_algorithm.setter
	def keypair_algorithm(self,keypair_algorithm):
		try :
			if not isinstance(keypair_algorithm,str):
				raise TypeError("keypair_algorithm must be set to str value")
			self._keypair_algorithm = keypair_algorithm
		except Exception as e :
			raise e


	'''
	get Indicates if Email subject alternative names allowed
	'''
	@property
	def subjaltname_email_allowed(self) :
		try:
			return self._subjaltname_email_allowed
		except Exception as e :
			raise e
	'''
	set Indicates if Email subject alternative names allowed
	'''
	@subjaltname_email_allowed.setter
	def subjaltname_email_allowed(self,subjaltname_email_allowed):
		try :
			if not isinstance(subjaltname_email_allowed,bool):
				raise TypeError("subjaltname_email_allowed must be set to bool value")
			self._subjaltname_email_allowed = subjaltname_email_allowed
		except Exception as e :
			raise e


	'''
	get Indicates if URI subject alternative names allowed
	'''
	@property
	def subjaltname_uri_allowed(self) :
		try:
			return self._subjaltname_uri_allowed
		except Exception as e :
			raise e
	'''
	set Indicates if URI subject alternative names allowed
	'''
	@subjaltname_uri_allowed.setter
	def subjaltname_uri_allowed(self,subjaltname_uri_allowed):
		try :
			if not isinstance(subjaltname_uri_allowed,bool):
				raise TypeError("subjaltname_uri_allowed must be set to bool value")
			self._subjaltname_uri_allowed = subjaltname_uri_allowed
		except Exception as e :
			raise e


	'''
	get Indicates if management type is locked
	'''
	@property
	def is_management_type_locked(self) :
		try:
			return self._is_management_type_locked
		except Exception as e :
			raise e
	'''
	set Indicates if management type is locked
	'''
	@is_management_type_locked.setter
	def is_management_type_locked(self,is_management_type_locked):
		try :
			if not isinstance(is_management_type_locked,bool):
				raise TypeError("is_management_type_locked must be set to bool value")
			self._is_management_type_locked = is_management_type_locked
		except Exception as e :
			raise e


	'''
	get Indicates if DNS subject alternative names allowed
	'''
	@property
	def subjaltname_dns_allowed(self) :
		try:
			return self._subjaltname_dns_allowed
		except Exception as e :
			raise e
	'''
	set Indicates if DNS subject alternative names allowed
	'''
	@subjaltname_dns_allowed.setter
	def subjaltname_dns_allowed(self,subjaltname_dns_allowed):
		try :
			if not isinstance(subjaltname_dns_allowed,bool):
				raise TypeError("subjaltname_dns_allowed must be set to bool value")
			self._subjaltname_dns_allowed = subjaltname_dns_allowed
		except Exception as e :
			raise e

	'''
	Use this operation to get a Venafi certificate policy.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				certificate_policy_obj=certificate_policy()
				response = certificate_policy_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of certificate_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			certificate_policy_obj = certificate_policy()
			option_ = options()
			option_._filter=filter_
			return certificate_policy_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the certificate_policy resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			certificate_policy_obj = certificate_policy()
			option_ = options()
			option_._count=True
			response = certificate_policy_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of certificate_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			certificate_policy_obj = certificate_policy()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = certificate_policy_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(certificate_policy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.certificate_policy
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(certificate_policy_responses, response, "certificate_policy_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.certificate_policy_response_array
				i=0
				error = [certificate_policy() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.certificate_policy_response_array
			i=0
			certificate_policy_objs = [certificate_policy() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_certificate_policy'):
					for props in obj._certificate_policy:
						result = service.payload_formatter.string_to_bulk_resource(certificate_policy_response,self.__class__.__name__,props)
						certificate_policy_objs[i] = result.certificate_policy
						i=i+1
			return certificate_policy_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(certificate_policy,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class certificate_policy_response(base_response):
	def __init__(self,length=1) :
		self.certificate_policy= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.certificate_policy= [ certificate_policy() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class certificate_policy_responses(base_response):
	def __init__(self,length=1) :
		self.certificate_policy_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.certificate_policy_response_array = [ certificate_policy() for _ in range(length)]
