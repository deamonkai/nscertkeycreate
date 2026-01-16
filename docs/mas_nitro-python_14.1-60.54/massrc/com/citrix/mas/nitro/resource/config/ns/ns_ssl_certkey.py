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
from massrc.com.citrix.mas.nitro.resource.config.ns.ns_sslcertkey_binding import ns_sslcertkey_binding
from massrc.com.citrix.mas.nitro.resource.config.ns.certkey_chain_link import certkey_chain_link
from massrc.com.citrix.mas.nitro.resource.config.ns.cert_store_data import cert_store_data


'''
Configuration for SSL certificate on NetScaler resource
'''

class ns_ssl_certkey(base_resource):
	_no_of_bound_entities= ""
	_managed_by= ""
	_certificate_source= ""
	_poll_time= ""
	_no_domain_check= ""
	_status= ""
	_display_name= ""
	_partition_name= ""
	_certificate_data= ""
	_ssl_certificate= ""
	_public_key_algorithm= ""
	_public_key_size= ""
	_id= ""
	_certkey_status= ""
	_certificate_dn= ""
	_signature_algorithm= ""
	_serial_number= ""
	_issuer= ""
	_ns_ip_address= ""
	_days_to_expiry= ""
	_hostname= ""
	_certkeypair_name= ""
	_valid_from= ""
	_device_name= ""
	_cert_format= ""
	_subject= ""
	_subjaltname= ""
	_file_location_path= ""
	_key_data= ""
	_linkcertkeyname= ""
	_valid_to= ""
	_ssl_key= ""
	_version= ""
	_days_to_expiry_str= ""
	_key_file_name= ""
	_entity_binding_arr=[]
	_datacenter_id= ""
	_issuer_cn= ""
	_entity_name= ""
	_csr= ""
	_domain= ""
	_activity_id= ""
	_cert_ids=[]
	_snicert= ""
	_certkeypair_arr=[]
	_ns_ip_address_arr=[]
	_deleteCertKeyFilesOnRemoval= ""
	_cert_store_id= ""
	_certchainbinding=[]
	_file_name= ""
	_source_certificate= ""
	_app_name= ""
	_certificate_file_name= ""
	_source_ipaddress= ""
	_certkeychain=[]
	_password= ""
	_certchain_data=[]
	_save_config= ""
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
			return "ns_ssl_certkey"
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
			return self._file_location_path
		except Exception as e :
			raise e

	'''
	Returns the value of object file component name.
	'''
	@property
	def file_component_value(self) :
		try :
			return "ns_ssl_certkeys"
		except Exception as e :
			raise e



	'''
	get no_of_bound_entities
	'''
	@property
	def no_of_bound_entities(self) :
		try:
			return self._no_of_bound_entities
		except Exception as e :
			raise e


	'''
	get Indicates if the certificate is managed by a third party certificate management provider.
	'''
	@property
	def managed_by(self) :
		try:
			return self._managed_by
		except Exception as e :
			raise e
	'''
	set Indicates if the certificate is managed by a third party certificate management provider.
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
	get This will have the source(LOCAL/REMOTE) of the certificate. Zero touch certificates will have the source as REMOTE.
	'''
	@property
	def certificate_source(self) :
		try:
			return self._certificate_source
		except Exception as e :
			raise e
	'''
	set This will have the source(LOCAL/REMOTE) of the certificate. Zero touch certificates will have the source as REMOTE.
	'''
	@certificate_source.setter
	def certificate_source(self,certificate_source):
		try :
			if not isinstance(certificate_source,str):
				raise TypeError("certificate_source must be set to str value")
			self._certificate_source = certificate_source
		except Exception as e :
			raise e


	'''
	get Last Polling Time
	'''
	@property
	def poll_time(self) :
		try:
			return self._poll_time
		except Exception as e :
			raise e


	'''
	get Specify this option to override the check for matching domain names during certificate update operation
	'''
	@property
	def no_domain_check(self) :
		try:
			return self._no_domain_check
		except Exception as e :
			raise e
	'''
	set Specify this option to override the check for matching domain names during certificate update operation
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
	get Tells whether the certificate is still valid or not
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e


	'''
	get Display Name of the device
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e


	'''
	get Name of Admin Partition. Blank means Default Partition
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
		except Exception as e :
			raise e


	'''
	get Certificate Data
	'''
	@property
	def certificate_data(self) :
		try:
			return self._certificate_data
		except Exception as e :
			raise e
	'''
	set Certificate Data
	'''
	@certificate_data.setter
	def certificate_data(self,certificate_data):
		try :
			if not isinstance(certificate_data,str):
				raise TypeError("certificate_data must be set to str value")
			self._certificate_data = certificate_data
		except Exception as e :
			raise e


	'''
	get Certificate
	'''
	@property
	def ssl_certificate(self) :
		try:
			return self._ssl_certificate
		except Exception as e :
			raise e
	'''
	set Certificate
	'''
	@ssl_certificate.setter
	def ssl_certificate(self,ssl_certificate):
		try :
			if not isinstance(ssl_certificate,str):
				raise TypeError("ssl_certificate must be set to str value")
			self._ssl_certificate = ssl_certificate
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
	get Public Key Size
	'''
	@property
	def public_key_size(self) :
		try:
			return self._public_key_size
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all ssl cert-keys entries. For download operation "id" must be provided in the format <adc_ip_address>_<certkeypair_name>.tgz
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all ssl cert-keys entries. For download operation "id" must be provided in the format <adc_ip_address>_<certkeypair_name>.tgz
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
	get Status(ACTIVE/INACTIVE) of certkey based on its traffic.
	'''
	@property
	def certkey_status(self) :
		try:
			return self._certkey_status
		except Exception as e :
			raise e
	'''
	set Status(ACTIVE/INACTIVE) of certkey based on its traffic.
	'''
	@certkey_status.setter
	def certkey_status(self,certkey_status):
		try :
			if not isinstance(certkey_status,str):
				raise TypeError("certkey_status must be set to str value")
			self._certkey_status = certkey_status
		except Exception as e :
			raise e


	'''
	get For certificates created by Venafi,this property indicates the certificate distinguished name.
	'''
	@property
	def certificate_dn(self) :
		try:
			return self._certificate_dn
		except Exception as e :
			raise e
	'''
	set For certificates created by Venafi,this property indicates the certificate distinguished name.
	'''
	@certificate_dn.setter
	def certificate_dn(self,certificate_dn):
		try :
			if not isinstance(certificate_dn,str):
				raise TypeError("certificate_dn must be set to str value")
			self._certificate_dn = certificate_dn
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
	get List of NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set List of NetScaler IP Address
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e


	'''
	get Days before SSL certificate expires
	'''
	@property
	def days_to_expiry(self) :
		try:
			return self._days_to_expiry
		except Exception as e :
			raise e


	'''
	get Host Name of the device
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
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
	set Cert Key Pair Name
	'''
	@certkeypair_name.setter
	def certkeypair_name(self,certkeypair_name):
		try :
			if not isinstance(certkeypair_name,str):
				raise TypeError("certkeypair_name must be set to str value")
			self._certkeypair_name = certkeypair_name
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
	get Name of the device
	'''
	@property
	def device_name(self) :
		try:
			return self._device_name
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
	set Certificate Format
	'''
	@cert_format.setter
	def cert_format(self,cert_format):
		try :
			if not isinstance(cert_format,str):
				raise TypeError("cert_format must be set to str value")
			self._cert_format = cert_format
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
	get Comma separated Subject Alternative Names
	'''
	@property
	def subjaltname(self) :
		try:
			return self._subjaltname
		except Exception as e :
			raise e


	'''
	get File Location on Client for download
	'''
	@property
	def file_location_path(self) :
		try:
			return self._file_location_path
		except Exception as e :
			raise e
	'''
	set File Location on Client for download
	'''
	@file_location_path.setter
	def file_location_path(self,file_location_path):
		try :
			if not isinstance(file_location_path,str):
				raise TypeError("file_location_path must be set to str value")
			self._file_location_path = file_location_path
		except Exception as e :
			raise e


	'''
	get Key Data
	'''
	@property
	def key_data(self) :
		try:
			return self._key_data
		except Exception as e :
			raise e
	'''
	set Key Data
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
	get For certificates having an intermediate certificate, it will provide the linked certificate key pair name
	'''
	@property
	def linkcertkeyname(self) :
		try:
			return self._linkcertkeyname
		except Exception as e :
			raise e
	'''
	set For certificates having an intermediate certificate, it will provide the linked certificate key pair name
	'''
	@linkcertkeyname.setter
	def linkcertkeyname(self,linkcertkeyname):
		try :
			if not isinstance(linkcertkeyname,str):
				raise TypeError("linkcertkeyname must be set to str value")
			self._linkcertkeyname = linkcertkeyname
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
	get Key
	'''
	@property
	def ssl_key(self) :
		try:
			return self._ssl_key
		except Exception as e :
			raise e
	'''
	set Key
	'''
	@ssl_key.setter
	def ssl_key(self,ssl_key):
		try :
			if not isinstance(ssl_key,str):
				raise TypeError("ssl_key must be set to str value")
			self._ssl_key = ssl_key
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
	Days to expire in years and days
	'''
	@property
	def days_to_expiry_str(self):
		try:
			return self._days_to_expiry_str
		except Exception as e :
			raise e
	'''
	Days to expire in years and days
	'''
	@days_to_expiry_str.setter
	def days_to_expiry_str(self,days_to_expiry_str):
		try :
			if not isinstance(days_to_expiry_str,str):
				raise TypeError("days_to_expiry_str must be set to str value")
			self._days_to_expiry_str = days_to_expiry_str
		except Exception as e :
			raise e

	'''
	Key File Name
	'''
	@property
	def key_file_name(self):
		try:
			return self._key_file_name
		except Exception as e :
			raise e
	'''
	Key File Name
	'''
	@key_file_name.setter
	def key_file_name(self,key_file_name):
		try :
			if not isinstance(key_file_name,str):
				raise TypeError("key_file_name must be set to str value")
			self._key_file_name = key_file_name
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def entity_binding_arr(self) :
		try:
			return self._entity_binding_arr
		except Exception as e :
			raise e
	'''
	
	'''
	@entity_binding_arr.setter
	def entity_binding_arr(self,entity_binding_arr) :
		try :
			if not isinstance(entity_binding_arr,list):
				raise TypeError("entity_binding_arr must be set to array of ns_sslcertkey_binding value")
			for item in entity_binding_arr :
				if not isinstance(item,ns_sslcertkey_binding):
					raise TypeError("item must be set to ns_sslcertkey_binding value")
			self._entity_binding_arr = entity_binding_arr
		except Exception as e :
			raise e

	'''
	Datacenter Id 
	'''
	@property
	def datacenter_id(self):
		try:
			return self._datacenter_id
		except Exception as e :
			raise e

	'''
	CN of issuer
	'''
	@property
	def issuer_cn(self):
		try:
			return self._issuer_cn
		except Exception as e :
			raise e
	'''
	CN of issuer
	'''
	@issuer_cn.setter
	def issuer_cn(self,issuer_cn):
		try :
			if not isinstance(issuer_cn,str):
				raise TypeError("issuer_cn must be set to str value")
			self._issuer_cn = issuer_cn
		except Exception as e :
			raise e

	'''
	entity name
	'''
	@property
	def entity_name(self):
		try:
			return self._entity_name
		except Exception as e :
			raise e
	'''
	entity name
	'''
	@entity_name.setter
	def entity_name(self,entity_name):
		try :
			if not isinstance(entity_name,str):
				raise TypeError("entity_name must be set to str value")
			self._entity_name = entity_name
		except Exception as e :
			raise e

	'''
	Certificate Signing Request
	'''
	@property
	def csr(self):
		try:
			return self._csr
		except Exception as e :
			raise e

	'''
	Domain name for certificate issuer
	'''
	@property
	def domain(self):
		try:
			return self._domain
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
	Array of SSL certificate IDs
	'''
	@property
	def cert_ids(self) :
		try:
			return self._cert_ids
		except Exception as e :
			raise e
	'''
	Array of SSL certificate IDs
	'''
	@cert_ids.setter
	def cert_ids(self,cert_ids) :
		try :
			if not isinstance(cert_ids,list):
				raise TypeError("cert_ids must be set to array of str value")
			for item in cert_ids :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._cert_ids = cert_ids
		except Exception as e :
			raise e

	'''
	Indicates server certificate for SNI. Used in cert binding operation.
	'''
	@property
	def snicert(self):
		try:
			return self._snicert
		except Exception as e :
			raise e
	'''
	Indicates server certificate for SNI. Used in cert binding operation.
	'''
	@snicert.setter
	def snicert(self,snicert):
		try :
			if not isinstance(snicert,bool):
				raise TypeError("snicert must be set to bool value")
			self._snicert = snicert
		except Exception as e :
			raise e

	'''
	List of certkeypair_name.Used in cert binding operation.
	'''
	@property
	def certkeypair_arr(self) :
		try:
			return self._certkeypair_arr
		except Exception as e :
			raise e
	'''
	List of certkeypair_name.Used in cert binding operation.
	'''
	@certkeypair_arr.setter
	def certkeypair_arr(self,certkeypair_arr) :
		try :
			if not isinstance(certkeypair_arr,list):
				raise TypeError("certkeypair_arr must be set to array of str value")
			for item in certkeypair_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._certkeypair_arr = certkeypair_arr
		except Exception as e :
			raise e

	'''
	List of NetScaler IP Address
	'''
	@property
	def ns_ip_address_arr(self) :
		try:
			return self._ns_ip_address_arr
		except Exception as e :
			raise e
	'''
	List of NetScaler IP Address
	'''
	@ns_ip_address_arr.setter
	def ns_ip_address_arr(self,ns_ip_address_arr) :
		try :
			if not isinstance(ns_ip_address_arr,list):
				raise TypeError("ns_ip_address_arr must be set to array of str value")
			for item in ns_ip_address_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_ip_address_arr = ns_ip_address_arr
		except Exception as e :
			raise e

	'''
	Argument to remove certkey files from NS along with certificate configuration based on the option selected by the user
	'''
	@property
	def deleteCertKeyFilesOnRemoval(self):
		try:
			return self._deleteCertKeyFilesOnRemoval
		except Exception as e :
			raise e
	'''
	Argument to remove certkey files from NS along with certificate configuration based on the option selected by the user
	'''
	@deleteCertKeyFilesOnRemoval.setter
	def deleteCertKeyFilesOnRemoval(self,deleteCertKeyFilesOnRemoval):
		try :
			if not isinstance(deleteCertKeyFilesOnRemoval,str):
				raise TypeError("deleteCertKeyFilesOnRemoval must be set to str value")
			self._deleteCertKeyFilesOnRemoval = deleteCertKeyFilesOnRemoval
		except Exception as e :
			raise e

	'''
	Cert Store Id 
	'''
	@property
	def cert_store_id(self):
		try:
			return self._cert_store_id
		except Exception as e :
			raise e

	'''
	Certificate Chain binding.
	'''
	@property
	def certchainbinding(self) :
		try:
			return self._certchainbinding
		except Exception as e :
			raise e
	'''
	Certificate Chain binding.
	'''
	@certchainbinding.setter
	def certchainbinding(self,certchainbinding) :
		try :
			if not isinstance(certchainbinding,list):
				raise TypeError("certchainbinding must be set to array of str value")
			for item in certchainbinding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._certchainbinding = certchainbinding
		except Exception as e :
			raise e

	'''
	File Name
	'''
	@property
	def file_name(self):
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	File Name
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
	CertKeyPair Name of the certificate that needs to installed in another instance
	'''
	@property
	def source_certificate(self):
		try:
			return self._source_certificate
		except Exception as e :
			raise e
	'''
	CertKeyPair Name of the certificate that needs to installed in another instance
	'''
	@source_certificate.setter
	def source_certificate(self,source_certificate):
		try :
			if not isinstance(source_certificate,str):
				raise TypeError("source_certificate must be set to str value")
			self._source_certificate = source_certificate
		except Exception as e :
			raise e

	'''
	Application name.Used for tracking task logs created for a specific application
	'''
	@property
	def app_name(self):
		try:
			return self._app_name
		except Exception as e :
			raise e
	'''
	Application name.Used for tracking task logs created for a specific application
	'''
	@app_name.setter
	def app_name(self,app_name):
		try :
			if not isinstance(app_name,str):
				raise TypeError("app_name must be set to str value")
			self._app_name = app_name
		except Exception as e :
			raise e

	'''
	Certificate File Name
	'''
	@property
	def certificate_file_name(self):
		try:
			return self._certificate_file_name
		except Exception as e :
			raise e
	'''
	Certificate File Name
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
	NetScaler IP of the certificate that needs to installed in another instance
	'''
	@property
	def source_ipaddress(self):
		try:
			return self._source_ipaddress
		except Exception as e :
			raise e
	'''
	NetScaler IP of the certificate that needs to installed in another instance
	'''
	@source_ipaddress.setter
	def source_ipaddress(self,source_ipaddress):
		try :
			if not isinstance(source_ipaddress,str):
				raise TypeError("source_ipaddress must be set to str value")
			self._source_ipaddress = source_ipaddress
		except Exception as e :
			raise e

	'''
	Array of linked certificates details
	'''
	@property
	def certkeychain(self) :
		try:
			return self._certkeychain
		except Exception as e :
			raise e
	'''
	Array of linked certificates details
	'''
	@certkeychain.setter
	def certkeychain(self,certkeychain) :
		try :
			if not isinstance(certkeychain,list):
				raise TypeError("certkeychain must be set to array of certkey_chain_link value")
			for item in certkeychain :
				if not isinstance(item,certkey_chain_link):
					raise TypeError("item must be set to certkey_chain_link value")
			self._certkeychain = certkeychain
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
	Use this operation to modify certificates on NetScaler Instance(s).
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
				ns_ssl_certkey_obj=ns_ssl_certkey()
				return cls.update_bulk_request(client,resource,ns_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to bind a certificate to a SSL vserver.Required properties certkeypair_arr,display_name,entity_name.
	'''
	@classmethod
	def bind_cert(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"bind_cert")
				return res
			else : 
				ns_ssl_certkey_obj= ns_ssl_certkey()
				return cls.perform_operation_bulk_request(service,"bind_cert",resource,ns_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to install certificates on NetScaler Instance(s).
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
				ns_ssl_certkey_obj= ns_ssl_certkey()
				return cls.perform_operation_bulk_request(service,resource,ns_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete certificates on NetScaler Instance(s).
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
					ns_ssl_certkey_obj=ns_ssl_certkey()
					return cls.delete_bulk_request(client,resource,ns_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get certificates bound to vservers, service groups and services.
	'''
	@classmethod
	def list_entity_cert(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"list_entity_cert")
				return res
			else : 
				ns_ssl_certkey_obj= ns_ssl_certkey()
				return cls.perform_operation_bulk_request(service,"list_entity_cert",resource,ns_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to do inventory.
	'''
	@classmethod
	def inventory(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"inventory")
				return res
			else : 
				ns_ssl_certkey_obj= ns_ssl_certkey()
				return cls.perform_operation_bulk_request(service,"inventory",resource,ns_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get certificates on NetScaler Instance(s).
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_ssl_certkey_obj=ns_ssl_certkey()
				response = ns_ssl_certkey_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to generate CSR for the certificate.
	'''

	'''
	Use this operation to generate CSR for the certificate.
	'''
	@classmethod
	def gen_csr(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"gen_csr")
			else : 
				ns_ssl_certkey_obj= ns_ssl_certkey()
				return cls.perform_operation_bulk_request(service,"gen_csr", resource,ns_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to download certificates.
	'''

	'''
	Use this operation to download certificates.
	'''
	@classmethod
	def download(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.download_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_ssl_certkey resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_ssl_certkey_obj = ns_ssl_certkey()
			option_ = options()
			option_._filter=filter_
			return ns_ssl_certkey_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_ssl_certkey resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_ssl_certkey_obj = ns_ssl_certkey()
			option_ = options()
			option_._count=True
			response = ns_ssl_certkey_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_ssl_certkey resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_ssl_certkey_obj = ns_ssl_certkey()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_ssl_certkey_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_ssl_certkey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ssl_certkey
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ssl_certkey_responses, response, "ns_ssl_certkey_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ssl_certkey_response_array
				i=0
				error = [ns_ssl_certkey() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ssl_certkey_response_array
			i=0
			ns_ssl_certkey_objs = [ns_ssl_certkey() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ssl_certkey'):
					for props in obj._ns_ssl_certkey:
						result = service.payload_formatter.string_to_bulk_resource(ns_ssl_certkey_response,self.__class__.__name__,props)
						ns_ssl_certkey_objs[i] = result.ns_ssl_certkey
						i=i+1
			return ns_ssl_certkey_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ssl_certkey,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ssl_certkey_response(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_certkey= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ssl_certkey= [ ns_ssl_certkey() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ssl_certkey_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_certkey_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ssl_certkey_response_array = [ ns_ssl_certkey() for _ in range(length)]
