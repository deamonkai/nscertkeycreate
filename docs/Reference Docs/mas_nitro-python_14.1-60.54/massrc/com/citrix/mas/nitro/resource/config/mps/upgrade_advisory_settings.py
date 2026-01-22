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
Configuration for upgrade advisory settings resource
'''

class upgrade_advisory_settings(base_resource):
	_version= ""
	_id= ""
	_build= ""
	_builds=[]
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
			return "upgrade_advisory_settings"
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
			return "upgrade_advisory_settingss"
		except Exception as e :
			raise e



	'''
	get version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set version
	'''
	@version.setter
	def version(self,version):
		try :
			if not isinstance(version,str):
				raise TypeError("version must be set to str value")
			self._version = version
		except Exception as e :
			raise e


	'''
	get Id is system generated key for upgrade advisory settings
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for upgrade advisory settings
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
	get build
	'''
	@property
	def build(self) :
		try:
			return self._build
		except Exception as e :
			raise e
	'''
	set build
	'''
	@build.setter
	def build(self,build):
		try :
			if not isinstance(build,str):
				raise TypeError("build must be set to str value")
			self._build = build
		except Exception as e :
			raise e

	'''
	builds
	'''
	@property
	def builds(self) :
		try:
			return self._builds
		except Exception as e :
			raise e
	'''
	builds
	'''
	@builds.setter
	def builds(self,builds) :
		try :
			if not isinstance(builds,list):
				raise TypeError("builds must be set to array of str value")
			for item in builds :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._builds = builds
		except Exception as e :
			raise e

	'''
	Use this operation to get Upgrade Advisory settings..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				upgrade_advisory_settings_obj=upgrade_advisory_settings()
				response = upgrade_advisory_settings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify Upgrade Advisory settings..
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
			else :
				upgrade_advisory_settings_obj=upgrade_advisory_settings()
				return cls.update_bulk_request(client,resource,upgrade_advisory_settings_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of upgrade_advisory_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			upgrade_advisory_settings_obj = upgrade_advisory_settings()
			option_ = options()
			option_._filter=filter_
			return upgrade_advisory_settings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the upgrade_advisory_settings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			upgrade_advisory_settings_obj = upgrade_advisory_settings()
			option_ = options()
			option_._count=True
			response = upgrade_advisory_settings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of upgrade_advisory_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			upgrade_advisory_settings_obj = upgrade_advisory_settings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = upgrade_advisory_settings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(upgrade_advisory_settings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.upgrade_advisory_settings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(upgrade_advisory_settings_responses, response, "upgrade_advisory_settings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.upgrade_advisory_settings_response_array
				i=0
				error = [upgrade_advisory_settings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.upgrade_advisory_settings_response_array
			i=0
			upgrade_advisory_settings_objs = [upgrade_advisory_settings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_upgrade_advisory_settings'):
					for props in obj._upgrade_advisory_settings:
						result = service.payload_formatter.string_to_bulk_resource(upgrade_advisory_settings_response,self.__class__.__name__,props)
						upgrade_advisory_settings_objs[i] = result.upgrade_advisory_settings
						i=i+1
			return upgrade_advisory_settings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(upgrade_advisory_settings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class upgrade_advisory_settings_response(base_response):
	def __init__(self,length=1) :
		self.upgrade_advisory_settings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.upgrade_advisory_settings= [ upgrade_advisory_settings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class upgrade_advisory_settings_responses(base_response):
	def __init__(self,length=1) :
		self.upgrade_advisory_settings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.upgrade_advisory_settings_response_array = [ upgrade_advisory_settings() for _ in range(length)]
