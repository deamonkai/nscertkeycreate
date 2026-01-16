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
Configuration for NetScaler Agent Image resource
'''

class mas_agent_image(base_resource):
	_file_name= ""
	_file_size= ""
	_file_last_modified_epoch= ""
	_file_last_modified= ""
	_file_location_path= ""
	_k8_yaml_filename= ""
	_proxy_server_port= ""
	_proxy_server_ip_address= ""
	_application_id= ""
	_k8_helmchart= ""
	_proxy_server_username= ""
	_proxy_server_password= ""
	_k8_agent_version= ""
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
			return "mas_agent_image"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._file_name
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
			return "mas_agent_images"
		except Exception as e :
			raise e



	'''
	get File Name
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set File Name
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
	get file_size
	'''
	@property
	def file_size(self) :
		try:
			return self._file_size
		except Exception as e :
			raise e


	'''
	get Last Modified (Epoch)
	'''
	@property
	def file_last_modified_epoch(self) :
		try:
			return self._file_last_modified_epoch
		except Exception as e :
			raise e


	'''
	get Last Modified
	'''
	@property
	def file_last_modified(self) :
		try:
			return self._file_last_modified
		except Exception as e :
			raise e


	'''
	get File Location on Client for upload/download
	'''
	@property
	def file_location_path(self) :
		try:
			return self._file_location_path
		except Exception as e :
			raise e
	'''
	set File Location on Client for upload/download
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
	k8 yaml filename
	'''
	@property
	def k8_yaml_filename(self):
		try:
			return self._k8_yaml_filename
		except Exception as e :
			raise e
	'''
	k8 yaml filename
	'''
	@k8_yaml_filename.setter
	def k8_yaml_filename(self,k8_yaml_filename):
		try :
			if not isinstance(k8_yaml_filename,str):
				raise TypeError("k8_yaml_filename must be set to str value")
			self._k8_yaml_filename = k8_yaml_filename
		except Exception as e :
			raise e

	'''
	Port number of proxy server
	'''
	@property
	def proxy_server_port(self):
		try:
			return self._proxy_server_port
		except Exception as e :
			raise e
	'''
	Port number of proxy server
	'''
	@proxy_server_port.setter
	def proxy_server_port(self,proxy_server_port):
		try :
			if not isinstance(proxy_server_port,int):
				raise TypeError("proxy_server_port must be set to int value")
			self._proxy_server_port = proxy_server_port
		except Exception as e :
			raise e

	'''
	IP address of proxy server
	'''
	@property
	def proxy_server_ip_address(self):
		try:
			return self._proxy_server_ip_address
		except Exception as e :
			raise e
	'''
	IP address of proxy server
	'''
	@proxy_server_ip_address.setter
	def proxy_server_ip_address(self,proxy_server_ip_address):
		try :
			if not isinstance(proxy_server_ip_address,str):
				raise TypeError("proxy_server_ip_address must be set to str value")
			self._proxy_server_ip_address = proxy_server_ip_address
		except Exception as e :
			raise e

	'''
	Agent application ID
	'''
	@property
	def application_id(self):
		try:
			return self._application_id
		except Exception as e :
			raise e
	'''
	Agent application ID
	'''
	@application_id.setter
	def application_id(self,application_id):
		try :
			if not isinstance(application_id,str):
				raise TypeError("application_id must be set to str value")
			self._application_id = application_id
		except Exception as e :
			raise e

	'''
	k8 helm chart
	'''
	@property
	def k8_helmchart(self):
		try:
			return self._k8_helmchart
		except Exception as e :
			raise e
	'''
	k8 helm chart
	'''
	@k8_helmchart.setter
	def k8_helmchart(self,k8_helmchart):
		try :
			if not isinstance(k8_helmchart,str):
				raise TypeError("k8_helmchart must be set to str value")
			self._k8_helmchart = k8_helmchart
		except Exception as e :
			raise e

	'''
	Username for proxy server
	'''
	@property
	def proxy_server_username(self):
		try:
			return self._proxy_server_username
		except Exception as e :
			raise e
	'''
	Username for proxy server
	'''
	@proxy_server_username.setter
	def proxy_server_username(self,proxy_server_username):
		try :
			if not isinstance(proxy_server_username,str):
				raise TypeError("proxy_server_username must be set to str value")
			self._proxy_server_username = proxy_server_username
		except Exception as e :
			raise e

	'''
	Password for proxy server
	'''
	@property
	def proxy_server_password(self):
		try:
			return self._proxy_server_password
		except Exception as e :
			raise e
	'''
	Password for proxy server
	'''
	@proxy_server_password.setter
	def proxy_server_password(self,proxy_server_password):
		try :
			if not isinstance(proxy_server_password,str):
				raise TypeError("proxy_server_password must be set to str value")
			self._proxy_server_password = proxy_server_password
		except Exception as e :
			raise e

	'''
	Kubernetes Agent Version
	'''
	@property
	def k8_agent_version(self):
		try:
			return self._k8_agent_version
		except Exception as e :
			raise e
	'''
	Kubernetes Agent Version
	'''
	@k8_agent_version.setter
	def k8_agent_version(self,k8_agent_version):
		try :
			if not isinstance(k8_agent_version,str):
				raise TypeError("k8_agent_version must be set to str value")
			self._k8_agent_version = k8_agent_version
		except Exception as e :
			raise e

	'''
	Agent password
	'''
	@property
	def password(self):
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	Agent password
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
	Use this operation to delete NetScaler Agent Image file.
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
					mas_agent_image_obj=mas_agent_image()
					return cls.delete_bulk_request(client,resource,mas_agent_image_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to download NetScaler Agent Image file.
	'''

	'''
	Use this operation to download NetScaler Agent Image file.
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
	Use this operation to upload NetScaler Agent Image file.
	'''

	'''
	Use this operation to upload NetScaler Agent Image file.
	'''
	@classmethod
	def upload(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.upload_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this operation to generate k8s agent yaml file.
	'''
	@classmethod
	def generate_k8s_agent_yaml_file(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"generate_k8s_agent_yaml_file")
				return res
			else : 
				mas_agent_image_obj= mas_agent_image()
				return cls.perform_operation_bulk_request(service,"generate_k8s_agent_yaml_file",resource,mas_agent_image_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler Agent Image file.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				mas_agent_image_obj=mas_agent_image()
				response = mas_agent_image_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mas_agent_image resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mas_agent_image_obj = mas_agent_image()
			option_ = options()
			option_._filter=filter_
			return mas_agent_image_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mas_agent_image resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mas_agent_image_obj = mas_agent_image()
			option_ = options()
			option_._count=True
			response = mas_agent_image_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mas_agent_image resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mas_agent_image_obj = mas_agent_image()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mas_agent_image_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mas_agent_image_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mas_agent_image
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mas_agent_image_responses, response, "mas_agent_image_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mas_agent_image_response_array
				i=0
				error = [mas_agent_image() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mas_agent_image_response_array
			i=0
			mas_agent_image_objs = [mas_agent_image() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mas_agent_image'):
					for props in obj._mas_agent_image:
						result = service.payload_formatter.string_to_bulk_resource(mas_agent_image_response,self.__class__.__name__,props)
						mas_agent_image_objs[i] = result.mas_agent_image
						i=i+1
			return mas_agent_image_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mas_agent_image,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mas_agent_image_response(base_response):
	def __init__(self,length=1) :
		self.mas_agent_image= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mas_agent_image= [ mas_agent_image() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mas_agent_image_responses(base_response):
	def __init__(self,length=1) :
		self.mas_agent_image_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mas_agent_image_response_array = [ mas_agent_image() for _ in range(length)]
