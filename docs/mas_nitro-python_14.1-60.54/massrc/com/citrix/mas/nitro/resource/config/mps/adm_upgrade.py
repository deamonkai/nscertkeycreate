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
Configuration for NetScaler Console Upgrade resource
'''

class adm_upgrade(base_resource):
	_do_cleanup= ""
	_file_name= ""
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
			return "adm_upgrade"
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
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file component name.
	'''
	@property
	def file_component_value(self) :
		try :
			return "adm_upgrades"
		except Exception as e :
			raise e



	'''
	get True, if user wants to clean the image files once upgrade is completed successfully
	'''
	@property
	def do_cleanup(self) :
		try:
			return self._do_cleanup
		except Exception as e :
			raise e
	'''
	set True, if user wants to clean the image files once upgrade is completed successfully
	'''
	@do_cleanup.setter
	def do_cleanup(self,do_cleanup):
		try :
			if not isinstance(do_cleanup,bool):
				raise TypeError("do_cleanup must be set to bool value")
			self._do_cleanup = do_cleanup
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
	Use this operation to upgrade NetScaler Console.
	'''
	@classmethod
	def upgrade(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service,"upgrade")
				return res
			else : 
				adm_upgrade_obj= adm_upgrade()
				return cls.perform_operation_bulk_request(service,"upgrade",resource,adm_upgrade_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adm_upgrade_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adm_upgrade
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adm_upgrade_responses, response, "adm_upgrade_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adm_upgrade_response_array
				i=0
				error = [adm_upgrade() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adm_upgrade_response_array
			i=0
			adm_upgrade_objs = [adm_upgrade() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adm_upgrade'):
					for props in obj._adm_upgrade:
						result = service.payload_formatter.string_to_bulk_resource(adm_upgrade_response,self.__class__.__name__,props)
						adm_upgrade_objs[i] = result.adm_upgrade
						i=i+1
			return adm_upgrade_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adm_upgrade,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adm_upgrade_response(base_response):
	def __init__(self,length=1) :
		self.adm_upgrade= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adm_upgrade= [ adm_upgrade() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adm_upgrade_responses(base_response):
	def __init__(self,length=1) :
		self.adm_upgrade_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adm_upgrade_response_array = [ adm_upgrade() for _ in range(length)]
