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
Configuration for secret_server_details resource.
'''

class secret_server_details(base_resource):
	_server_ip= ""
	_start_server= ""
	_hsm_server_health= ""
	_password= ""
	_id= ""
	_username= ""
	_hsm_port= ""
	_protocol= ""
	_is_password_changed= ""
	_hostid= ""
	_material= ""
	_serial_number= ""
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
			return "secret_server_details"
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
			return "secret_server_detailss"
		except Exception as e :
			raise e



	'''
	get server ip
	'''
	@property
	def server_ip(self) :
		try:
			return self._server_ip
		except Exception as e :
			raise e
	'''
	set server ip
	'''
	@server_ip.setter
	def server_ip(self,server_ip):
		try :
			if not isinstance(server_ip,str):
				raise TypeError("server_ip must be set to str value")
			self._server_ip = server_ip
		except Exception as e :
			raise e


	'''
	get start unauthenticated server
	'''
	@property
	def start_server(self) :
		try:
			return self._start_server
		except Exception as e :
			raise e
	'''
	set start unauthenticated server
	'''
	@start_server.setter
	def start_server(self,start_server):
		try :
			if not isinstance(start_server,bool):
				raise TypeError("start_server must be set to bool value")
			self._start_server = start_server
		except Exception as e :
			raise e


	'''
	get HSM server health
	'''
	@property
	def hsm_server_health(self) :
		try:
			return self._hsm_server_health
		except Exception as e :
			raise e
	'''
	set HSM server health
	'''
	@hsm_server_health.setter
	def hsm_server_health(self,hsm_server_health):
		try :
			if not isinstance(hsm_server_health,str):
				raise TypeError("hsm_server_health must be set to str value")
			self._hsm_server_health = hsm_server_health
		except Exception as e :
			raise e


	'''
	get password for communication with Instances
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set password for communication with Instances
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
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get username
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set username
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
	get HSM server port
	'''
	@property
	def hsm_port(self) :
		try:
			return self._hsm_port
		except Exception as e :
			raise e
	'''
	set HSM server port
	'''
	@hsm_port.setter
	def hsm_port(self,hsm_port):
		try :
			if not isinstance(hsm_port,int):
				raise TypeError("hsm_port must be set to int value")
			self._hsm_port = hsm_port
		except Exception as e :
			raise e


	'''
	get communication protocol
	'''
	@property
	def protocol(self) :
		try:
			return self._protocol
		except Exception as e :
			raise e
	'''
	set communication protocol
	'''
	@protocol.setter
	def protocol(self,protocol):
		try :
			if not isinstance(protocol,str):
				raise TypeError("protocol must be set to str value")
			self._protocol = protocol
		except Exception as e :
			raise e

	'''
	is_password_changed
	'''
	@property
	def is_password_changed(self):
		try:
			return self._is_password_changed
		except Exception as e :
			raise e
	'''
	is_password_changed
	'''
	@is_password_changed.setter
	def is_password_changed(self,is_password_changed):
		try :
			if not isinstance(is_password_changed,bool):
				raise TypeError("is_password_changed must be set to bool value")
			self._is_password_changed = is_password_changed
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def hostid(self):
		try:
			return self._hostid
		except Exception as e :
			raise e
	'''
	
	'''
	@hostid.setter
	def hostid(self,hostid):
		try :
			if not isinstance(hostid,str):
				raise TypeError("hostid must be set to str value")
			self._hostid = hostid
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def material(self):
		try:
			return self._material
		except Exception as e :
			raise e
	'''
	
	'''
	@material.setter
	def material(self,material):
		try :
			if not isinstance(material,str):
				raise TypeError("material must be set to str value")
			self._material = material
		except Exception as e :
			raise e

	'''
	serial_number
	'''
	@property
	def serial_number(self):
		try:
			return self._serial_number
		except Exception as e :
			raise e
	'''
	serial_number
	'''
	@serial_number.setter
	def serial_number(self,serial_number):
		try :
			if not isinstance(serial_number,str):
				raise TypeError("serial_number must be set to str value")
			self._serial_number = serial_number
		except Exception as e :
			raise e

	'''
	Use this operation to get system settings.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				secret_server_details_obj=secret_server_details()
				response = secret_server_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify system settings.
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
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of secret_server_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			secret_server_details_obj = secret_server_details()
			option_ = options()
			option_._filter=filter_
			return secret_server_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the secret_server_details resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			secret_server_details_obj = secret_server_details()
			option_ = options()
			option_._count=True
			response = secret_server_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of secret_server_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			secret_server_details_obj = secret_server_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = secret_server_details_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(secret_server_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.secret_server_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(secret_server_details_responses, response, "secret_server_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.secret_server_details_response_array
				i=0
				error = [secret_server_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.secret_server_details_response_array
			i=0
			secret_server_details_objs = [secret_server_details() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_secret_server_details'):
					for props in obj._secret_server_details:
						result = service.payload_formatter.string_to_bulk_resource(secret_server_details_response,self.__class__.__name__,props)
						secret_server_details_objs[i] = result.secret_server_details
						i=i+1
			return secret_server_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(secret_server_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class secret_server_details_response(base_response):
	def __init__(self,length=1) :
		self.secret_server_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.secret_server_details= [ secret_server_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class secret_server_details_responses(base_response):
	def __init__(self,length=1) :
		self.secret_server_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.secret_server_details_response_array = [ secret_server_details() for _ in range(length)]
