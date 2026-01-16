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
from massrc.com.citrix.mas.nitro.resource.config.mps.instance_score_threshold import instance_score_threshold


'''
Configuration for Device Score Setting resource
'''

class instance_score_settings(base_resource):
	_thresholds=[]
	_indicator_value= ""
	_indicator_category= ""
	_indicator= ""
	_indicator_notifications_enabled= ""
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
			return "instance_score_settings"
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
			return "instance_score_settingss"
		except Exception as e :
			raise e



	'''
	get Thresholds associated with a device score indicator
	'''
	@property
	def thresholds(self) :
		try:
			return self._thresholds
		except Exception as e :
			raise e
	'''
	set Thresholds associated with a device score indicator
	'''
	@thresholds.setter
	def thresholds(self,thresholds) :
		try :
			if not isinstance(thresholds,list):
				raise TypeError("thresholds must be set to array of instance_score_threshold value")
			for item in thresholds :
				if not isinstance(item,instance_score_threshold):
					raise TypeError("item must be set to instance_score_threshold value")
			self._thresholds = thresholds
		except Exception as e :
			raise e


	'''
	get Indicator Value
	'''
	@property
	def indicator_value(self) :
		try:
			return self._indicator_value
		except Exception as e :
			raise e
	'''
	set Indicator Value
	'''
	@indicator_value.setter
	def indicator_value(self,indicator_value):
		try :
			if not isinstance(indicator_value,str):
				raise TypeError("indicator_value must be set to str value")
			self._indicator_value = indicator_value
		except Exception as e :
			raise e


	'''
	get Category of indicator
	'''
	@property
	def indicator_category(self) :
		try:
			return self._indicator_category
		except Exception as e :
			raise e
	'''
	set Category of indicator
	'''
	@indicator_category.setter
	def indicator_category(self,indicator_category):
		try :
			if not isinstance(indicator_category,str):
				raise TypeError("indicator_category must be set to str value")
			self._indicator_category = indicator_category
		except Exception as e :
			raise e


	'''
	get Property or indicator name
	'''
	@property
	def indicator(self) :
		try:
			return self._indicator
		except Exception as e :
			raise e
	'''
	set Property or indicator name
	'''
	@indicator.setter
	def indicator(self,indicator):
		try :
			if not isinstance(indicator,str):
				raise TypeError("indicator must be set to str value")
			self._indicator = indicator
		except Exception as e :
			raise e


	'''
	get Flag to check if notifications are enabled
	'''
	@property
	def indicator_notifications_enabled(self) :
		try:
			return self._indicator_notifications_enabled
		except Exception as e :
			raise e
	'''
	set Flag to check if notifications are enabled
	'''
	@indicator_notifications_enabled.setter
	def indicator_notifications_enabled(self,indicator_notifications_enabled):
		try :
			if not isinstance(indicator_notifications_enabled,str):
				raise TypeError("indicator_notifications_enabled must be set to str value")
			self._indicator_notifications_enabled = indicator_notifications_enabled
		except Exception as e :
			raise e

	'''
	Use this operation to get instance score settings.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				instance_score_settings_obj=instance_score_settings()
				response = instance_score_settings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to update instance score settings.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				instance_score_settings_obj=instance_score_settings()
				return cls.update_bulk_request(client,resource,instance_score_settings_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of instance_score_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			instance_score_settings_obj = instance_score_settings()
			option_ = options()
			option_._filter=filter_
			return instance_score_settings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the instance_score_settings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			instance_score_settings_obj = instance_score_settings()
			option_ = options()
			option_._count=True
			response = instance_score_settings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of instance_score_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			instance_score_settings_obj = instance_score_settings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = instance_score_settings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(instance_score_settings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.instance_score_settings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(instance_score_settings_responses, response, "instance_score_settings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.instance_score_settings_response_array
				i=0
				error = [instance_score_settings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.instance_score_settings_response_array
			i=0
			instance_score_settings_objs = [instance_score_settings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_instance_score_settings'):
					for props in obj._instance_score_settings:
						result = service.payload_formatter.string_to_bulk_resource(instance_score_settings_response,self.__class__.__name__,props)
						instance_score_settings_objs[i] = result.instance_score_settings
						i=i+1
			return instance_score_settings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(instance_score_settings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class instance_score_settings_response(base_response):
	def __init__(self,length=1) :
		self.instance_score_settings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.instance_score_settings= [ instance_score_settings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class instance_score_settings_responses(base_response):
	def __init__(self,length=1) :
		self.instance_score_settings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.instance_score_settings_response_array = [ instance_score_settings() for _ in range(length)]
