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
Configuration for Agent certificate resource
'''

class agent_cert_upload(base_resource):
	_password= ""
	_agent_id= ""
	_cert_name= ""
	_key_name= ""
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
			return "agent_cert_upload"
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
			return "agent_cert_uploads"
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
	agent id
	'''
	@property
	def agent_id(self):
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	agent id
	'''
	@agent_id.setter
	def agent_id(self,agent_id):
		try :
			if not isinstance(agent_id,str):
				raise TypeError("agent_id must be set to str value")
			self._agent_id = agent_id
		except Exception as e :
			raise e

	'''
	cert name
	'''
	@property
	def cert_name(self):
		try:
			return self._cert_name
		except Exception as e :
			raise e
	'''
	cert name
	'''
	@cert_name.setter
	def cert_name(self,cert_name):
		try :
			if not isinstance(cert_name,str):
				raise TypeError("cert_name must be set to str value")
			self._cert_name = cert_name
		except Exception as e :
			raise e

	'''
	key name
	'''
	@property
	def key_name(self):
		try:
			return self._key_name
		except Exception as e :
			raise e
	'''
	key name
	'''
	@key_name.setter
	def key_name(self,key_name):
		try :
			if not isinstance(key_name,str):
				raise TypeError("key_name must be set to str value")
			self._key_name = key_name
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(agent_cert_upload_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.agent_cert_upload
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(agent_cert_upload_responses, response, "agent_cert_upload_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.agent_cert_upload_response_array
				i=0
				error = [agent_cert_upload() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.agent_cert_upload_response_array
			i=0
			agent_cert_upload_objs = [agent_cert_upload() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_agent_cert_upload'):
					for props in obj._agent_cert_upload:
						result = service.payload_formatter.string_to_bulk_resource(agent_cert_upload_response,self.__class__.__name__,props)
						agent_cert_upload_objs[i] = result.agent_cert_upload
						i=i+1
			return agent_cert_upload_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(agent_cert_upload,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class agent_cert_upload_response(base_response):
	def __init__(self,length=1) :
		self.agent_cert_upload= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.agent_cert_upload= [ agent_cert_upload() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class agent_cert_upload_responses(base_response):
	def __init__(self,length=1) :
		self.agent_cert_upload_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.agent_cert_upload_response_array = [ agent_cert_upload() for _ in range(length)]
