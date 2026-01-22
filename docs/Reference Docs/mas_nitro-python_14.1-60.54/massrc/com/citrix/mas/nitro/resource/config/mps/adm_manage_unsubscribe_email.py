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
Configuration for Unsubscribe Email resource
'''

class adm_manage_unsubscribe_email(base_resource):
	_unsubscribe_email_notification= ""
	_id= ""
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
			return "adm_manage_unsubscribe_email"
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
			return "adm_manage_unsubscribe_emails"
		except Exception as e :
			raise e



	'''
	get Set the value to true if the customer doesn't want to receive email notification.
	'''
	@property
	def unsubscribe_email_notification(self) :
		try:
			return self._unsubscribe_email_notification
		except Exception as e :
			raise e
	'''
	set Set the value to true if the customer doesn't want to receive email notification.
	'''
	@unsubscribe_email_notification.setter
	def unsubscribe_email_notification(self,unsubscribe_email_notification):
		try :
			if not isinstance(unsubscribe_email_notification,bool):
				raise TypeError("unsubscribe_email_notification must be set to bool value")
			self._unsubscribe_email_notification = unsubscribe_email_notification
		except Exception as e :
			raise e


	'''
	get Id is system generated key for adm_manage_unsubscribe_email 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for adm_manage_unsubscribe_email 
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adm_manage_unsubscribe_email_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adm_manage_unsubscribe_email
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adm_manage_unsubscribe_email_responses, response, "adm_manage_unsubscribe_email_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adm_manage_unsubscribe_email_response_array
				i=0
				error = [adm_manage_unsubscribe_email() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adm_manage_unsubscribe_email_response_array
			i=0
			adm_manage_unsubscribe_email_objs = [adm_manage_unsubscribe_email() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adm_manage_unsubscribe_email'):
					for props in obj._adm_manage_unsubscribe_email:
						result = service.payload_formatter.string_to_bulk_resource(adm_manage_unsubscribe_email_response,self.__class__.__name__,props)
						adm_manage_unsubscribe_email_objs[i] = result.adm_manage_unsubscribe_email
						i=i+1
			return adm_manage_unsubscribe_email_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adm_manage_unsubscribe_email,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adm_manage_unsubscribe_email_response(base_response):
	def __init__(self,length=1) :
		self.adm_manage_unsubscribe_email= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adm_manage_unsubscribe_email= [ adm_manage_unsubscribe_email() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adm_manage_unsubscribe_email_responses(base_response):
	def __init__(self,length=1) :
		self.adm_manage_unsubscribe_email_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adm_manage_unsubscribe_email_response_array = [ adm_manage_unsubscribe_email() for _ in range(length)]
