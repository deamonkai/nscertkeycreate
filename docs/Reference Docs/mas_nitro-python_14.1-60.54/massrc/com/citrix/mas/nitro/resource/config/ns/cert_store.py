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
from massrc.com.citrix.mas.nitro.resource.config.ns.cert_store_data import cert_store_data
from massrc.com.citrix.mas.nitro.resource.config.ns.cert_store_data import cert_store_data


'''
Configuration for SSL certificate store on NetScaler Console resource
'''

class cert_store(base_resource):
	_cert_format= ""
	_subject= ""
	_serial_number= ""
	_issuer= ""
	_acme_ca_config_id= ""
	_valid_from= ""
	_valid_to= ""
	_updated_time= ""
	_renewal_status= ""
	_domain= ""
	_password_sync_required= ""
	_version= ""
	_subjaltname= ""
	_store_code= ""
	_created_time= ""
	_name= ""
	_hash_code= ""
	_managed_by= ""
	_dns_provider_name= ""
	_mode= ""
	_csr_data= ""
	_zero_touch_certificate= ""
	_cert_type= ""
	_signature_algorithm= ""
	_is_issued_from_csr= ""
	_certchain_file_id= ""
	_revision_number= ""
	_renew_mode= ""
	_public_key_algorithm= ""
	_issued_by_org= ""
	_id= ""
	_last_renewed_at= ""
	_key_file= ""
	_public_key_size= ""
	_update_cert_chain= ""
	_cert_keysize_type= ""
	_days_to_expiry= ""
	_acme_ca_config_name= ""
	_key_data= ""
	_update_password_only= ""
	_cert_id_array=[]
	_cert_signing_type= ""
	_activity_id= ""
	_cert_used_type= ""
	_end_renew_time= ""
	_bound_entities_number= ""
	_cert_info_required= ""
	_cert_issuer_type= ""
	_update_cert_on_devices= ""
	_certificate_ids=[]
	_cert_data= ""
	_no_domain_check= ""
	_start_renew_time= ""
	_cert_signature_algo_type= ""
	_certchain_data=[]
	_status= ""
	_save_config= ""
	_update_cert_and_key= ""
	_is_acme_feature= ""
	_password= ""
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
			return "cert_store"
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
			return "cert_stores"
		except Exception as e :
			raise e



	'''
	get Certificate Format
	'''
	@property
	def cert_format(self) :
		try:
			return self._cert_format
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
	get ID of the CA config that is used to renew the certificate
	'''
	@property
	def acme_ca_config_id(self) :
		try:
			return self._acme_ca_config_id
		except Exception as e :
			raise e
	'''
	set ID of the CA config that is used to renew the certificate
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
	get Valid From
	'''
	@property
	def valid_from(self) :
		try:
			return self._valid_from
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
	get Recent status updated time for this activity in seconds
	'''
	@property
	def updated_time(self) :
		try:
			return self._updated_time
		except Exception as e :
			raise e
	'''
	set Recent status updated time for this activity in seconds
	'''
	@updated_time.setter
	def updated_time(self,updated_time):
		try :
			if not isinstance(updated_time,float):
				raise TypeError("updated_time must be set to float value")
			self._updated_time = updated_time
		except Exception as e :
			raise e


	'''
	get Last renewal status (SUCCESS/FAILED) for this certificate. This is applicable when the certificate is enabled for auto renewal.
	'''
	@property
	def renewal_status(self) :
		try:
			return self._renewal_status
		except Exception as e :
			raise e
	'''
	set Last renewal status (SUCCESS/FAILED) for this certificate. This is applicable when the certificate is enabled for auto renewal.
	'''
	@renewal_status.setter
	def renewal_status(self,renewal_status):
		try :
			if not isinstance(renewal_status,str):
				raise TypeError("renewal_status must be set to str value")
			self._renewal_status = renewal_status
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
	get Set to true, if the password update is required for this certificate. This is applicable when the certificate is discovered from ADC.
	'''
	@property
	def password_sync_required(self) :
		try:
			return self._password_sync_required
		except Exception as e :
			raise e
	'''
	set Set to true, if the password update is required for this certificate. This is applicable when the certificate is discovered from ADC.
	'''
	@password_sync_required.setter
	def password_sync_required(self,password_sync_required):
		try :
			if not isinstance(password_sync_required,bool):
				raise TypeError("password_sync_required must be set to bool value")
			self._password_sync_required = password_sync_required
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
	get Comma separated Subject Alternative Names
	'''
	@property
	def subjaltname(self) :
		try:
			return self._subjaltname
		except Exception as e :
			raise e


	'''
	get 0 indicates no error.100: Failure in storing Server certificate file.200: Failure in storing key file. 300:Failure in storing password.400: Failure in storing certificate chain
	'''
	@property
	def store_code(self) :
		try:
			return self._store_code
		except Exception as e :
			raise e


	'''
	get Creation time for this activity in seconds
	'''
	@property
	def created_time(self) :
		try:
			return self._created_time
		except Exception as e :
			raise e
	'''
	set Creation time for this activity in seconds
	'''
	@created_time.setter
	def created_time(self,created_time):
		try :
			if not isinstance(created_time,float):
				raise TypeError("created_time must be set to float value")
			self._created_time = created_time
		except Exception as e :
			raise e


	'''
	get Name or alias which identifies certificate and key pair
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name or alias which identifies certificate and key pair
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
	get Zero touch: MD5sum(hash code) of the complete certificate (certificates, key and chain certiticates) or key content
	'''
	@property
	def hash_code(self) :
		try:
			return self._hash_code
		except Exception as e :
			raise e


	'''
	get Indicates the CA provider if the certificate is managed by a ACME CA provider.
	'''
	@property
	def managed_by(self) :
		try:
			return self._managed_by
		except Exception as e :
			raise e
	'''
	set Indicates the CA provider if the certificate is managed by a ACME CA provider.
	'''
	@managed_by.setter
	def managed_by(self,managed_by):
		try :
			if not isinstance(managed_by,str):
				raise TypeError("managed_by must be set to str value")
			self._managed_by = managed_by
		except Exception as e :
			raise e


	'''
	get DNS Provider of the domain name from the issuer certificate.
	'''
	@property
	def dns_provider_name(self) :
		try:
			return self._dns_provider_name
		except Exception as e :
			raise e
	'''
	set DNS Provider of the domain name from the issuer certificate.
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
	get To identify if the certificate is added manually or discovred from NetScaler (1.Manual/2.Discovered)
	'''
	@property
	def mode(self) :
		try:
			return self._mode
		except Exception as e :
			raise e
	'''
	set To identify if the certificate is added manually or discovred from NetScaler (1.Manual/2.Discovered)
	'''
	@mode.setter
	def mode(self,mode):
		try :
			if not isinstance(mode,int):
				raise TypeError("mode must be set to int value")
			self._mode = mode
		except Exception as e :
			raise e


	'''
	get Base64 encoded CSR file contents.
	'''
	@property
	def csr_data(self) :
		try:
			return self._csr_data
		except Exception as e :
			raise e
	'''
	set Base64 encoded CSR file contents.
	'''
	@csr_data.setter
	def csr_data(self,csr_data):
		try :
			if not isinstance(csr_data,str):
				raise TypeError("csr_data must be set to str value")
			self._csr_data = csr_data
		except Exception as e :
			raise e


	'''
	get Set to true, if the certificate is uploaded for zero touch ssl certificate repository purpose.
	'''
	@property
	def zero_touch_certificate(self) :
		try:
			return self._zero_touch_certificate
		except Exception as e :
			raise e
	'''
	set Set to true, if the certificate is uploaded for zero touch ssl certificate repository purpose.
	'''
	@zero_touch_certificate.setter
	def zero_touch_certificate(self,zero_touch_certificate):
		try :
			if not isinstance(zero_touch_certificate,bool):
				raise TypeError("zero_touch_certificate must be set to bool value")
			self._zero_touch_certificate = zero_touch_certificate
		except Exception as e :
			raise e


	'''
	get Type/kind of the certificate. 1) server_cert, 2) intermediate_cert, 3) root_cert, 4) key. This is applicable for zero_touch files. For cert_store, it will be always server_cert.
	'''
	@property
	def cert_type(self) :
		try:
			return self._cert_type
		except Exception as e :
			raise e
	'''
	set Type/kind of the certificate. 1) server_cert, 2) intermediate_cert, 3) root_cert, 4) key. This is applicable for zero_touch files. For cert_store, it will be always server_cert.
	'''
	@cert_type.setter
	def cert_type(self,cert_type):
		try :
			if not isinstance(cert_type,str):
				raise TypeError("cert_type must be set to str value")
			self._cert_type = cert_type
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
	get Set to true, if the certificate is issued from CSR.
	'''
	@property
	def is_issued_from_csr(self) :
		try:
			return self._is_issued_from_csr
		except Exception as e :
			raise e
	'''
	set Set to true, if the certificate is issued from CSR.
	'''
	@is_issued_from_csr.setter
	def is_issued_from_csr(self,is_issued_from_csr):
		try :
			if not isinstance(is_issued_from_csr,bool):
				raise TypeError("is_issued_from_csr must be set to bool value")
			self._is_issued_from_csr = is_issued_from_csr
		except Exception as e :
			raise e


	'''
	get Comma separated list of IDs against which cert chain contents are stored in cert_store_data table
	'''
	@property
	def certchain_file_id(self) :
		try:
			return self._certchain_file_id
		except Exception as e :
			raise e
	'''
	set Comma separated list of IDs against which cert chain contents are stored in cert_store_data table
	'''
	@certchain_file_id.setter
	def certchain_file_id(self,certchain_file_id):
		try :
			if not isinstance(certchain_file_id,str):
				raise TypeError("certchain_file_id must be set to str value")
			self._certchain_file_id = certchain_file_id
		except Exception as e :
			raise e


	'''
	get Certificate revision number
	'''
	@property
	def revision_number(self) :
		try:
			return self._revision_number
		except Exception as e :
			raise e


	'''
	get Renew mode for the certificate. It can be MANUAL or AUTO. If it is set to AUTO, then the certificate will be auto renewed based on the CA config associated with this certificate.
	'''
	@property
	def renew_mode(self) :
		try:
			return self._renew_mode
		except Exception as e :
			raise e
	'''
	set Renew mode for the certificate. It can be MANUAL or AUTO. If it is set to AUTO, then the certificate will be auto renewed based on the CA config associated with this certificate.
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
	get Public Key Algorithm
	'''
	@property
	def public_key_algorithm(self) :
		try:
			return self._public_key_algorithm
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
	get Id is system generated key for all certificate story entries. 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all certificate story entries. 
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
	get Last renewal time for this certificate in seconds. This is applicable when the certificate is enabled for auto renewal.
	'''
	@property
	def last_renewed_at(self) :
		try:
			return self._last_renewed_at
		except Exception as e :
			raise e
	'''
	set Last renewal time for this certificate in seconds. This is applicable when the certificate is enabled for auto renewal.
	'''
	@last_renewed_at.setter
	def last_renewed_at(self,last_renewed_at):
		try :
			if not isinstance(last_renewed_at,long):
				raise TypeError("last_renewed_at must be set to long value")
			self._last_renewed_at = last_renewed_at
		except Exception as e :
			raise e


	'''
	get Key file name
	'''
	@property
	def key_file(self) :
		try:
			return self._key_file
		except Exception as e :
			raise e
	'''
	set Key file name
	'''
	@key_file.setter
	def key_file(self,key_file):
		try :
			if not isinstance(key_file,str):
				raise TypeError("key_file must be set to str value")
			self._key_file = key_file
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
	Set to true,if certificate chain needs to be updated during update operation
	'''
	@property
	def update_cert_chain(self):
		try:
			return self._update_cert_chain
		except Exception as e :
			raise e
	'''
	Set to true,if certificate chain needs to be updated during update operation
	'''
	@update_cert_chain.setter
	def update_cert_chain(self,update_cert_chain):
		try :
			if not isinstance(update_cert_chain,bool):
				raise TypeError("update_cert_chain must be set to bool value")
			self._update_cert_chain = update_cert_chain
		except Exception as e :
			raise e

	'''
	Size of the public key
	'''
	@property
	def cert_keysize_type(self):
		try:
			return self._cert_keysize_type
		except Exception as e :
			raise e
	'''
	Size of the public key
	'''
	@cert_keysize_type.setter
	def cert_keysize_type(self,cert_keysize_type):
		try :
			if not isinstance(cert_keysize_type,str):
				raise TypeError("cert_keysize_type must be set to str value")
			self._cert_keysize_type = cert_keysize_type
		except Exception as e :
			raise e

	'''
	Days before SSL certificate expires
	'''
	@property
	def days_to_expiry(self):
		try:
			return self._days_to_expiry
		except Exception as e :
			raise e

	'''
	Name of the CA config that is used to renew the certificate
	'''
	@property
	def acme_ca_config_name(self):
		try:
			return self._acme_ca_config_name
		except Exception as e :
			raise e
	'''
	Name of the CA config that is used to renew the certificate
	'''
	@acme_ca_config_name.setter
	def acme_ca_config_name(self,acme_ca_config_name):
		try :
			if not isinstance(acme_ca_config_name,str):
				raise TypeError("acme_ca_config_name must be set to str value")
			self._acme_ca_config_name = acme_ca_config_name
		except Exception as e :
			raise e

	'''
	Base64 encoded key file contents.
	'''
	@property
	def key_data(self):
		try:
			return self._key_data
		except Exception as e :
			raise e
	'''
	Base64 encoded key file contents.
	'''
	@key_data.setter
	def key_data(self,key_data):
		try :
			if not isinstance(key_data,str):
				raise TypeError("key_data must be set to str value")
			self._key_data = key_data
		except Exception as e :
			raise e

	'''
	Set to true, if only password needs to be updated during update operation
	'''
	@property
	def update_password_only(self):
		try:
			return self._update_password_only
		except Exception as e :
			raise e
	'''
	Set to true, if only password needs to be updated during update operation
	'''
	@update_password_only.setter
	def update_password_only(self,update_password_only):
		try :
			if not isinstance(update_password_only,bool):
				raise TypeError("update_password_only must be set to bool value")
			self._update_password_only = update_password_only
		except Exception as e :
			raise e

	'''
	Array of cert store IDs
	'''
	@property
	def cert_id_array(self) :
		try:
			return self._cert_id_array
		except Exception as e :
			raise e
	'''
	Array of cert store IDs
	'''
	@cert_id_array.setter
	def cert_id_array(self,cert_id_array) :
		try :
			if not isinstance(cert_id_array,list):
				raise TypeError("cert_id_array must be set to array of str value")
			for item in cert_id_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._cert_id_array = cert_id_array
		except Exception as e :
			raise e

	'''
	Certificate signature
	'''
	@property
	def cert_signing_type(self):
		try:
			return self._cert_signing_type
		except Exception as e :
			raise e
	'''
	Certificate signature
	'''
	@cert_signing_type.setter
	def cert_signing_type(self,cert_signing_type):
		try :
			if not isinstance(cert_signing_type,str):
				raise TypeError("cert_signing_type must be set to str value")
			self._cert_signing_type = cert_signing_type
		except Exception as e :
			raise e

	'''
	Activity Id used to track the progress of certificate operations.
	'''
	@property
	def activity_id(self):
		try:
			return self._activity_id
		except Exception as e :
			raise e

	'''
	The cert is used or not used
	'''
	@property
	def cert_used_type(self):
		try:
			return self._cert_used_type
		except Exception as e :
			raise e
	'''
	The cert is used or not used
	'''
	@cert_used_type.setter
	def cert_used_type(self,cert_used_type):
		try :
			if not isinstance(cert_used_type,str):
				raise TypeError("cert_used_type must be set to str value")
			self._cert_used_type = cert_used_type
		except Exception as e :
			raise e

	'''
	End time of certificate renew in seconds
	'''
	@property
	def end_renew_time(self):
		try:
			return self._end_renew_time
		except Exception as e :
			raise e
	'''
	End time of certificate renew in seconds
	'''
	@end_renew_time.setter
	def end_renew_time(self,end_renew_time):
		try :
			if not isinstance(end_renew_time,float):
				raise TypeError("end_renew_time must be set to float value")
			self._end_renew_time = end_renew_time
		except Exception as e :
			raise e

	'''
	Number of entities to which a certificate in store is bound
	'''
	@property
	def bound_entities_number(self):
		try:
			return self._bound_entities_number
		except Exception as e :
			raise e
	'''
	Number of entities to which a certificate in store is bound
	'''
	@bound_entities_number.setter
	def bound_entities_number(self,bound_entities_number):
		try :
			if not isinstance(bound_entities_number,int):
				raise TypeError("bound_entities_number must be set to int value")
			self._bound_entities_number = bound_entities_number
		except Exception as e :
			raise e

	'''
	This will return detailed certificate info like issues, algorithm, used/unused, etc
	'''
	@property
	def cert_info_required(self):
		try:
			return self._cert_info_required
		except Exception as e :
			raise e
	'''
	This will return detailed certificate info like issues, algorithm, used/unused, etc
	'''
	@cert_info_required.setter
	def cert_info_required(self,cert_info_required):
		try :
			if not isinstance(cert_info_required,bool):
				raise TypeError("cert_info_required must be set to bool value")
			self._cert_info_required = cert_info_required
		except Exception as e :
			raise e

	'''
	Issuer of the certificate
	'''
	@property
	def cert_issuer_type(self):
		try:
			return self._cert_issuer_type
		except Exception as e :
			raise e
	'''
	Issuer of the certificate
	'''
	@cert_issuer_type.setter
	def cert_issuer_type(self,cert_issuer_type):
		try :
			if not isinstance(cert_issuer_type,str):
				raise TypeError("cert_issuer_type must be set to str value")
			self._cert_issuer_type = cert_issuer_type
		except Exception as e :
			raise e

	'''
	The certificate will be applied on all the associated NetScaler(s)when this flag is set to true
	'''
	@property
	def update_cert_on_devices(self):
		try:
			return self._update_cert_on_devices
		except Exception as e :
			raise e
	'''
	The certificate will be applied on all the associated NetScaler(s)when this flag is set to true
	'''
	@update_cert_on_devices.setter
	def update_cert_on_devices(self,update_cert_on_devices):
		try :
			if not isinstance(update_cert_on_devices,bool):
				raise TypeError("update_cert_on_devices must be set to bool value")
			self._update_cert_on_devices = update_cert_on_devices
		except Exception as e :
			raise e

	'''
	Array of certificate IDs
	'''
	@property
	def certificate_ids(self) :
		try:
			return self._certificate_ids
		except Exception as e :
			raise e
	'''
	Array of certificate IDs
	'''
	@certificate_ids.setter
	def certificate_ids(self,certificate_ids) :
		try :
			if not isinstance(certificate_ids,list):
				raise TypeError("certificate_ids must be set to array of str value")
			for item in certificate_ids :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._certificate_ids = certificate_ids
		except Exception as e :
			raise e

	'''
	Base64 encoded certificate file contents.
	'''
	@property
	def cert_data(self):
		try:
			return self._cert_data
		except Exception as e :
			raise e
	'''
	Base64 encoded certificate file contents.
	'''
	@cert_data.setter
	def cert_data(self,cert_data):
		try :
			if not isinstance(cert_data,cert_store_data):
				raise TypeError("cert_data must be set to cert_store_data value")
			self._cert_data = cert_data
		except Exception as e :
			raise e

	'''
	Specify this option to override the check for matching domain names during certificate update operation
	'''
	@property
	def no_domain_check(self):
		try:
			return self._no_domain_check
		except Exception as e :
			raise e
	'''
	Specify this option to override the check for matching domain names during certificate update operation
	'''
	@no_domain_check.setter
	def no_domain_check(self,no_domain_check):
		try :
			if not isinstance(no_domain_check,bool):
				raise TypeError("no_domain_check must be set to bool value")
			self._no_domain_check = no_domain_check
		except Exception as e :
			raise e

	'''
	Start time of certificate renew in seconds
	'''
	@property
	def start_renew_time(self):
		try:
			return self._start_renew_time
		except Exception as e :
			raise e
	'''
	Start time of certificate renew in seconds
	'''
	@start_renew_time.setter
	def start_renew_time(self,start_renew_time):
		try :
			if not isinstance(start_renew_time,float):
				raise TypeError("start_renew_time must be set to float value")
			self._start_renew_time = start_renew_time
		except Exception as e :
			raise e

	'''
	Certificate algorithm
	'''
	@property
	def cert_signature_algo_type(self):
		try:
			return self._cert_signature_algo_type
		except Exception as e :
			raise e
	'''
	Certificate algorithm
	'''
	@cert_signature_algo_type.setter
	def cert_signature_algo_type(self,cert_signature_algo_type):
		try :
			if not isinstance(cert_signature_algo_type,str):
				raise TypeError("cert_signature_algo_type must be set to str value")
			self._cert_signature_algo_type = cert_signature_algo_type
		except Exception as e :
			raise e

	'''
	An array of Base64 encoded certificate chain contents.
	'''
	@property
	def certchain_data(self) :
		try:
			return self._certchain_data
		except Exception as e :
			raise e
	'''
	An array of Base64 encoded certificate chain contents.
	'''
	@certchain_data.setter
	def certchain_data(self,certchain_data) :
		try :
			if not isinstance(certchain_data,list):
				raise TypeError("certchain_data must be set to array of cert_store_data value")
			for item in certchain_data :
				if not isinstance(item,cert_store_data):
					raise TypeError("item must be set to cert_store_data value")
			self._certchain_data = certchain_data
		except Exception as e :
			raise e

	'''
	Tells whether the certificate is still valid or not
	'''
	@property
	def status(self):
		try:
			return self._status
		except Exception as e :
			raise e

	'''
	true, if save config is required
	'''
	@property
	def save_config(self):
		try:
			return self._save_config
		except Exception as e :
			raise e
	'''
	true, if save config is required
	'''
	@save_config.setter
	def save_config(self,save_config):
		try :
			if not isinstance(save_config,bool):
				raise TypeError("save_config must be set to bool value")
			self._save_config = save_config
		except Exception as e :
			raise e

	'''
	Set to true,if certificate and key files needs to be updated during update operation
	'''
	@property
	def update_cert_and_key(self):
		try:
			return self._update_cert_and_key
		except Exception as e :
			raise e
	'''
	Set to true,if certificate and key files needs to be updated during update operation
	'''
	@update_cert_and_key.setter
	def update_cert_and_key(self,update_cert_and_key):
		try :
			if not isinstance(update_cert_and_key,bool):
				raise TypeError("update_cert_and_key must be set to bool value")
			self._update_cert_and_key = update_cert_and_key
		except Exception as e :
			raise e

	'''
	This is to identify the ACME workflow and returns only the server certificates (skips IC, CA and Keys) from the cert store and zero-touch certificate repository
	'''
	@property
	def is_acme_feature(self):
		try:
			return self._is_acme_feature
		except Exception as e :
			raise e
	'''
	This is to identify the ACME workflow and returns only the server certificates (skips IC, CA and Keys) from the cert store and zero-touch certificate repository
	'''
	@is_acme_feature.setter
	def is_acme_feature(self,is_acme_feature):
		try :
			if not isinstance(is_acme_feature,bool):
				raise TypeError("is_acme_feature must be set to bool value")
			self._is_acme_feature = is_acme_feature
		except Exception as e :
			raise e

	'''
	The pass-phrase that was used to encrypt the private-key.
	'''
	@property
	def password(self):
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	The pass-phrase that was used to encrypt the private-key.
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e

	'''
	Use this operation to delete certificates on cert store.
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
					cert_store_obj=cert_store()
					return cls.delete_bulk_request(client,resource,cert_store_obj)
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
				cert_store_obj=cert_store()
				response = cert_store_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify certificates on cert store.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				cert_store_obj=cert_store()
				return cls.update_bulk_request(client,resource,cert_store_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add certificate file to cert store.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				return res
			else : 
				cert_store_obj= cert_store()
				return cls.perform_operation_bulk_request(service,resource,cert_store_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cert_store resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cert_store_obj = cert_store()
			option_ = options()
			option_._filter=filter_
			return cert_store_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cert_store resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cert_store_obj = cert_store()
			option_ = options()
			option_._count=True
			response = cert_store_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cert_store resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cert_store_obj = cert_store()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cert_store_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cert_store_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cert_store
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cert_store_responses, response, "cert_store_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cert_store_response_array
				i=0
				error = [cert_store() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cert_store_response_array
			i=0
			cert_store_objs = [cert_store() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cert_store'):
					for props in obj._cert_store:
						result = service.payload_formatter.string_to_bulk_resource(cert_store_response,self.__class__.__name__,props)
						cert_store_objs[i] = result.cert_store
						i=i+1
			return cert_store_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cert_store,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cert_store_response(base_response):
	def __init__(self,length=1) :
		self.cert_store= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cert_store= [ cert_store() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cert_store_responses(base_response):
	def __init__(self,length=1) :
		self.cert_store_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cert_store_response_array = [ cert_store() for _ in range(length)]
