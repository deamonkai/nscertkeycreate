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
Configuration for Test mail. resource
'''

class test_mail(base_resource):
	_failed_message= ""
	_profile_name= ""
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
			return "test_mail"
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
			return "test_mails"
		except Exception as e :
			raise e



	'''
	get Subject of the mail sent.
	'''
	@property
	def failed_message(self) :
		try:
			return self._failed_message
		except Exception as e :
			raise e
	'''
	set Subject of the mail sent.
	'''
	@failed_message.setter
	def failed_message(self,failed_message):
		try :
			if not isinstance(failed_message,str):
				raise TypeError("failed_message must be set to str value")
			self._failed_message = failed_message
		except Exception as e :
			raise e


	'''
	get Profile name through which mail sent.
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile name through which mail sent.
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e


	'''
	get Id is system generated key for test id
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for test id
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
	Test mail.
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
				test_mail_obj= test_mail()
				return cls.perform_operation_bulk_request(service,resource,test_mail_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(test_mail_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.test_mail
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(test_mail_responses, response, "test_mail_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.test_mail_response_array
				i=0
				error = [test_mail() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.test_mail_response_array
			i=0
			test_mail_objs = [test_mail() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_test_mail'):
					for props in obj._test_mail:
						result = service.payload_formatter.string_to_bulk_resource(test_mail_response,self.__class__.__name__,props)
						test_mail_objs[i] = result.test_mail
						i=i+1
			return test_mail_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(test_mail,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class test_mail_response(base_response):
	def __init__(self,length=1) :
		self.test_mail= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.test_mail= [ test_mail() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class test_mail_responses(base_response):
	def __init__(self,length=1) :
		self.test_mail_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.test_mail_response_array = [ test_mail() for _ in range(length)]
