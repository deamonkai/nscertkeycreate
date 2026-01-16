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


'''
Configuration for ACME Certificate Issuance and Renewal History resource
'''

class acme_cert_renewal_history(base_resource):
	_renewal_status= ""
	_last_renewed_at= ""
	_cert_id= ""
	_name= ""
	_log_message= ""
	_id= ""
	_zero_touch_certificate= ""
	_renewed_by_ca_config= ""
	_domain= ""
	_renew_mode= ""
	_username= ""
	_duration= ""
	_action= ""
	_status_summary_map=[]
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
			return "acme_cert_renewal_history"
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
			return "acme_cert_renewal_historys"
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
	get Id of the certificate which is renewed. This is the same as the ID of the certificate in cert store.
	'''
	@property
	def cert_id(self) :
		try:
			return self._cert_id
		except Exception as e :
			raise e
	'''
	set Id of the certificate which is renewed. This is the same as the ID of the certificate in cert store.
	'''
	@cert_id.setter
	def cert_id(self,cert_id):
		try :
			if not isinstance(cert_id,str):
				raise TypeError("cert_id must be set to str value")
			self._cert_id = cert_id
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
	get Log message for the last renewal operation. This is applicable when the certificate is renewed manually/anutomatically.
	'''
	@property
	def log_message(self) :
		try:
			return self._log_message
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all certificate renewal history entries.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all certificate renewal history entries.
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
	get Name of the CA configuration which is used to renew this certificate. This is the same as the name of the CA configuration in acme_ca_config table.
	'''
	@property
	def renewed_by_ca_config(self) :
		try:
			return self._renewed_by_ca_config
		except Exception as e :
			raise e
	'''
	set Name of the CA configuration which is used to renew this certificate. This is the same as the name of the CA configuration in acme_ca_config table.
	'''
	@renewed_by_ca_config.setter
	def renewed_by_ca_config(self,renewed_by_ca_config):
		try :
			if not isinstance(renewed_by_ca_config,str):
				raise TypeError("renewed_by_ca_config must be set to str value")
			self._renewed_by_ca_config = renewed_by_ca_config
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
	get User who performed the renewal/issuance operation. This is applicable when the certificate is renewed manually. For auto renewal, it will be system.
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set User who performed the renewal/issuance operation. This is applicable when the certificate is renewed manually. For auto renewal, it will be system.
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e

	'''
	Duration to filter the certificate renewal issuance/history. It can be 'last_24_hours', 'last_7_days', 'last_30_days', 'last_90_days', 'last_365_days' or 'all'.
	'''
	@property
	def duration(self):
		try:
			return self._duration
		except Exception as e :
			raise e
	'''
	Duration to filter the certificate renewal issuance/history. It can be 'last_24_hours', 'last_7_days', 'last_30_days', 'last_90_days', 'last_365_days' or 'all'.
	'''
	@duration.setter
	def duration(self,duration):
		try :
			if not isinstance(duration,str):
				raise TypeError("duration must be set to str value")
			self._duration = duration
		except Exception as e :
			raise e

	'''
	Action to get the summary of the certificate renewal issuance/history
	'''
	@property
	def action(self):
		try:
			return self._action
		except Exception as e :
			raise e
	'''
	Action to get the summary of the certificate renewal issuance/history
	'''
	@action.setter
	def action(self,action):
		try :
			if not isinstance(action,str):
				raise TypeError("action must be set to str value")
			self._action = action
		except Exception as e :
			raise e

	'''
	Array of tag_name and tag_value pair assocaited with an entity
	'''
	@property
	def status_summary_map(self) :
		try:
			return self._status_summary_map
		except Exception as e :
			raise e
	'''
	Array of tag_name and tag_value pair assocaited with an entity
	'''
	@status_summary_map.setter
	def status_summary_map(self,status_summary_map) :
		try :
			if not isinstance(status_summary_map,list):
				raise TypeError("status_summary_map must be set to array of property_map value")
			for item in status_summary_map :
				if not isinstance(item,property_map):
					raise TypeError("item must be set to property_map value")
			self._status_summary_map = status_summary_map
		except Exception as e :
			raise e

	'''
	Use this operation to get the ACME certificate renewal history.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				acme_cert_renewal_history_obj=acme_cert_renewal_history()
				response = acme_cert_renewal_history_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of acme_cert_renewal_history resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			acme_cert_renewal_history_obj = acme_cert_renewal_history()
			option_ = options()
			option_._filter=filter_
			return acme_cert_renewal_history_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the acme_cert_renewal_history resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			acme_cert_renewal_history_obj = acme_cert_renewal_history()
			option_ = options()
			option_._count=True
			response = acme_cert_renewal_history_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of acme_cert_renewal_history resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			acme_cert_renewal_history_obj = acme_cert_renewal_history()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = acme_cert_renewal_history_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(acme_cert_renewal_history_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.acme_cert_renewal_history
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(acme_cert_renewal_history_responses, response, "acme_cert_renewal_history_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.acme_cert_renewal_history_response_array
				i=0
				error = [acme_cert_renewal_history() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.acme_cert_renewal_history_response_array
			i=0
			acme_cert_renewal_history_objs = [acme_cert_renewal_history() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_acme_cert_renewal_history'):
					for props in obj._acme_cert_renewal_history:
						result = service.payload_formatter.string_to_bulk_resource(acme_cert_renewal_history_response,self.__class__.__name__,props)
						acme_cert_renewal_history_objs[i] = result.acme_cert_renewal_history
						i=i+1
			return acme_cert_renewal_history_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(acme_cert_renewal_history,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class acme_cert_renewal_history_response(base_response):
	def __init__(self,length=1) :
		self.acme_cert_renewal_history= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.acme_cert_renewal_history= [ acme_cert_renewal_history() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class acme_cert_renewal_history_responses(base_response):
	def __init__(self,length=1) :
		self.acme_cert_renewal_history_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.acme_cert_renewal_history_response_array = [ acme_cert_renewal_history() for _ in range(length)]
