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
from massrc.com.citrix.mas.nitro.resource.config.ns.cert_store_list import cert_store_list


'''
Configuration for Zero touch certificate resource
'''

class zero_touch_certs(base_resource):
	_file_name= ""
	_csr_data= ""
	_cert_store_lists=[]
	_file_data= ""
	_managed_by= ""
	_dns_provider_name= ""
	_hash_code= ""
	_is_issued_from_csr= ""
	_is_active= ""
	_password= ""
	_last_renewed_at= ""
	_id= ""
	_file_type= ""
	_renew_mode= ""
	_file_upload_time= ""
	_cert_format= ""
	_is_auto_renewal_enabled= ""
	_valid_from= ""
	_acme_ca_config_id= ""
	_days_to_expiry= ""
	_file_size= ""
	_is_cert= ""
	_renewal_status= ""
	_activity_id= ""
	_valid_to= ""
	_cert_id_array=[]
	_subjaltname= ""
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
			return "zero_touch_certs"
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
			return "zero_touch_certss"
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
	get List of cert_store objects
	'''
	@property
	def cert_store_lists(self) :
		try:
			return self._cert_store_lists
		except Exception as e :
			raise e
	'''
	set List of cert_store objects
	'''
	@cert_store_lists.setter
	def cert_store_lists(self,cert_store_lists) :
		try :
			if not isinstance(cert_store_lists,list):
				raise TypeError("cert_store_lists must be set to array of cert_store_list value")
			for item in cert_store_lists :
				if not isinstance(item,cert_store_list):
					raise TypeError("item must be set to cert_store_list value")
			self._cert_store_lists = cert_store_lists
		except Exception as e :
			raise e


	'''
	get Base64 encoded cert/key file contents.
	'''
	@property
	def file_data(self) :
		try:
			return self._file_data
		except Exception as e :
			raise e
	'''
	set Base64 encoded cert/key file contents.
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
	get Zero touch: MD5sum(hash code) of the complete certificate (certificates, key and chain certiticates) or key content
	'''
	@property
	def hash_code(self) :
		try:
			return self._hash_code
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
	get Set to true, if the certificate is valid and not expired
	'''
	@property
	def is_active(self) :
		try:
			return self._is_active
		except Exception as e :
			raise e
	'''
	set Set to true, if the certificate is valid and not expired
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
	get The pass-phrase that was used to encrypt the private-key.
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set The pass-phrase that was used to encrypt the private-key.
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
			if not isinstance(last_renewed_at,float):
				raise TypeError("last_renewed_at must be set to float value")
			self._last_renewed_at = last_renewed_at
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
	get Type of file (Certificate/Key)
	'''
	@property
	def file_type(self) :
		try:
			return self._file_type
		except Exception as e :
			raise e
	'''
	set Type of file (Certificate/Key)
	'''
	@file_type.setter
	def file_type(self,file_type):
		try :
			if not isinstance(file_type,str):
				raise TypeError("file_type must be set to str value")
			self._file_type = file_type
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
	get Creation time for this activity in seconds
	'''
	@property
	def file_upload_time(self) :
		try:
			return self._file_upload_time
		except Exception as e :
			raise e
	'''
	set Creation time for this activity in seconds
	'''
	@file_upload_time.setter
	def file_upload_time(self,file_upload_time):
		try :
			if not isinstance(file_upload_time,float):
				raise TypeError("file_upload_time must be set to float value")
			self._file_upload_time = file_upload_time
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
	get Set to true, if the certificate is enabled for auto renewal.
	'''
	@property
	def is_auto_renewal_enabled(self) :
		try:
			return self._is_auto_renewal_enabled
		except Exception as e :
			raise e
	'''
	set Set to true, if the certificate is enabled for auto renewal.
	'''
	@is_auto_renewal_enabled.setter
	def is_auto_renewal_enabled(self,is_auto_renewal_enabled):
		try :
			if not isinstance(is_auto_renewal_enabled,bool):
				raise TypeError("is_auto_renewal_enabled must be set to bool value")
			self._is_auto_renewal_enabled = is_auto_renewal_enabled
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
	get Days before SSL certificate expires
	'''
	@property
	def days_to_expiry(self) :
		try:
			return self._days_to_expiry
		except Exception as e :
			raise e
	'''
	set Days before SSL certificate expires
	'''
	@days_to_expiry.setter
	def days_to_expiry(self,days_to_expiry):
		try :
			if not isinstance(days_to_expiry,int):
				raise TypeError("days_to_expiry must be set to int value")
			self._days_to_expiry = days_to_expiry
		except Exception as e :
			raise e


	'''
	get Size of the file in bytes
	'''
	@property
	def file_size(self) :
		try:
			return self._file_size
		except Exception as e :
			raise e
	'''
	set Size of the file in bytes
	'''
	@file_size.setter
	def file_size(self,file_size):
		try :
			if not isinstance(file_size,int):
				raise TypeError("file_size must be set to int value")
			self._file_size = file_size
		except Exception as e :
			raise e


	'''
	get Set to true, if the file is of certificate type
	'''
	@property
	def is_cert(self) :
		try:
			return self._is_cert
		except Exception as e :
			raise e
	'''
	set Set to true, if the file is of certificate type
	'''
	@is_cert.setter
	def is_cert(self,is_cert):
		try :
			if not isinstance(is_cert,bool):
				raise TypeError("is_cert must be set to bool value")
			self._is_cert = is_cert
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
	get Activity Id used to track the progress of all the certificate operations.
	'''
	@property
	def activity_id(self) :
		try:
			return self._activity_id
		except Exception as e :
			raise e
	'''
	set Activity Id used to track the progress of all the certificate operations.
	'''
	@activity_id.setter
	def activity_id(self,activity_id):
		try :
			if not isinstance(activity_id,str):
				raise TypeError("activity_id must be set to str value")
			self._activity_id = activity_id
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
	get Array of cert store IDs
	'''
	@property
	def cert_id_array(self) :
		try:
			return self._cert_id_array
		except Exception as e :
			raise e
	'''
	set Array of cert store IDs
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
	get Comma separated Subject Alternative Names
	'''
	@property
	def subjaltname(self) :
		try:
			return self._subjaltname
		except Exception as e :
			raise e
	'''
	set Comma separated Subject Alternative Names
	'''
	@subjaltname.setter
	def subjaltname(self,subjaltname):
		try :
			if not isinstance(subjaltname,str):
				raise TypeError("subjaltname must be set to str value")
			self._subjaltname = subjaltname
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
				zero_touch_certs_obj= zero_touch_certs()
				return cls.perform_operation_bulk_request(service,resource,zero_touch_certs_obj)
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
				zero_touch_certs_obj=zero_touch_certs()
				response = zero_touch_certs_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
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
					zero_touch_certs_obj=zero_touch_certs()
					return cls.delete_bulk_request(client,resource,zero_touch_certs_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of zero_touch_certs resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			zero_touch_certs_obj = zero_touch_certs()
			option_ = options()
			option_._filter=filter_
			return zero_touch_certs_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the zero_touch_certs resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			zero_touch_certs_obj = zero_touch_certs()
			option_ = options()
			option_._count=True
			response = zero_touch_certs_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of zero_touch_certs resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			zero_touch_certs_obj = zero_touch_certs()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = zero_touch_certs_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(zero_touch_certs_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.zero_touch_certs
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(zero_touch_certs_responses, response, "zero_touch_certs_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.zero_touch_certs_response_array
				i=0
				error = [zero_touch_certs() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.zero_touch_certs_response_array
			i=0
			zero_touch_certs_objs = [zero_touch_certs() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_zero_touch_certs'):
					for props in obj._zero_touch_certs:
						result = service.payload_formatter.string_to_bulk_resource(zero_touch_certs_response,self.__class__.__name__,props)
						zero_touch_certs_objs[i] = result.zero_touch_certs
						i=i+1
			return zero_touch_certs_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(zero_touch_certs,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class zero_touch_certs_response(base_response):
	def __init__(self,length=1) :
		self.zero_touch_certs= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.zero_touch_certs= [ zero_touch_certs() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class zero_touch_certs_responses(base_response):
	def __init__(self,length=1) :
		self.zero_touch_certs_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.zero_touch_certs_response_array = [ zero_touch_certs() for _ in range(length)]
