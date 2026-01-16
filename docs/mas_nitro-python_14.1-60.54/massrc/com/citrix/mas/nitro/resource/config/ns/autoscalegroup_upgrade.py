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
Configuration for Upgrade support for AutoScaleGroup resource
'''

class autoscalegroup_upgrade(base_resource):
	_adc_cloud_image_id= ""
	_autoscalegroup_id= ""
	_is_force_upgrade= ""
	_activity_id= ""
	_adc_cloud_image_version= ""
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
			return "autoscalegroup_upgrade"
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
			return "autoscalegroup_upgrades"
		except Exception as e :
			raise e



	'''
	get NetScaler Cloud Image ID to which AutoScaleGroup(s) is/are to be upgraded
	'''
	@property
	def adc_cloud_image_id(self) :
		try:
			return self._adc_cloud_image_id
		except Exception as e :
			raise e
	'''
	set NetScaler Cloud Image ID to which AutoScaleGroup(s) is/are to be upgraded
	'''
	@adc_cloud_image_id.setter
	def adc_cloud_image_id(self,adc_cloud_image_id):
		try :
			if not isinstance(adc_cloud_image_id,str):
				raise TypeError("adc_cloud_image_id must be set to str value")
			self._adc_cloud_image_id = adc_cloud_image_id
		except Exception as e :
			raise e


	'''
	get AutoScaleGroup ID
	'''
	@property
	def autoscalegroup_id(self) :
		try:
			return self._autoscalegroup_id
		except Exception as e :
			raise e
	'''
	set AutoScaleGroup ID
	'''
	@autoscalegroup_id.setter
	def autoscalegroup_id(self,autoscalegroup_id):
		try :
			if not isinstance(autoscalegroup_id,str):
				raise TypeError("autoscalegroup_id must be set to str value")
			self._autoscalegroup_id = autoscalegroup_id
		except Exception as e :
			raise e


	'''
	get Force upgrade of AutoScaleGroup would mean to ignore Drain connection timeout
	'''
	@property
	def is_force_upgrade(self) :
		try:
			return self._is_force_upgrade
		except Exception as e :
			raise e
	'''
	set Force upgrade of AutoScaleGroup would mean to ignore Drain connection timeout
	'''
	@is_force_upgrade.setter
	def is_force_upgrade(self,is_force_upgrade):
		try :
			if not isinstance(is_force_upgrade,bool):
				raise TypeError("is_force_upgrade must be set to bool value")
			self._is_force_upgrade = is_force_upgrade
		except Exception as e :
			raise e


	'''
	get Most recent activity_id of this autoscalegroup
	'''
	@property
	def activity_id(self) :
		try:
			return self._activity_id
		except Exception as e :
			raise e
	'''
	set Most recent activity_id of this autoscalegroup
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
	get NetScaler Cloud Image Version to which AutoScaleGroup(s) is/are to be upgraded
	'''
	@property
	def adc_cloud_image_version(self) :
		try:
			return self._adc_cloud_image_version
		except Exception as e :
			raise e
	'''
	set NetScaler Cloud Image Version to which AutoScaleGroup(s) is/are to be upgraded
	'''
	@adc_cloud_image_version.setter
	def adc_cloud_image_version(self,adc_cloud_image_version):
		try :
			if not isinstance(adc_cloud_image_version,str):
				raise TypeError("adc_cloud_image_version must be set to str value")
			self._adc_cloud_image_version = adc_cloud_image_version
		except Exception as e :
			raise e

	'''
	Use this operation to get image names for the corresponding NetScaler Cloud Images..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				autoscalegroup_upgrade_obj=autoscalegroup_upgrade()
				response = autoscalegroup_upgrade_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to upgrade autoscalegroup cluster(s).
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
				autoscalegroup_upgrade_obj= autoscalegroup_upgrade()
				return cls.perform_operation_bulk_request(service,"upgrade",resource,autoscalegroup_upgrade_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of autoscalegroup_upgrade resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			autoscalegroup_upgrade_obj = autoscalegroup_upgrade()
			option_ = options()
			option_._filter=filter_
			return autoscalegroup_upgrade_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the autoscalegroup_upgrade resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			autoscalegroup_upgrade_obj = autoscalegroup_upgrade()
			option_ = options()
			option_._count=True
			response = autoscalegroup_upgrade_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of autoscalegroup_upgrade resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			autoscalegroup_upgrade_obj = autoscalegroup_upgrade()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = autoscalegroup_upgrade_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(autoscalegroup_upgrade_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.autoscalegroup_upgrade
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(autoscalegroup_upgrade_responses, response, "autoscalegroup_upgrade_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.autoscalegroup_upgrade_response_array
				i=0
				error = [autoscalegroup_upgrade() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.autoscalegroup_upgrade_response_array
			i=0
			autoscalegroup_upgrade_objs = [autoscalegroup_upgrade() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_autoscalegroup_upgrade'):
					for props in obj._autoscalegroup_upgrade:
						result = service.payload_formatter.string_to_bulk_resource(autoscalegroup_upgrade_response,self.__class__.__name__,props)
						autoscalegroup_upgrade_objs[i] = result.autoscalegroup_upgrade
						i=i+1
			return autoscalegroup_upgrade_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(autoscalegroup_upgrade,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class autoscalegroup_upgrade_response(base_response):
	def __init__(self,length=1) :
		self.autoscalegroup_upgrade= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.autoscalegroup_upgrade= [ autoscalegroup_upgrade() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class autoscalegroup_upgrade_responses(base_response):
	def __init__(self,length=1) :
		self.autoscalegroup_upgrade_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.autoscalegroup_upgrade_response_array = [ autoscalegroup_upgrade() for _ in range(length)]
