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
Configuration for Device Score Setting resource
'''

class instance_score_threshold(base_resource):
	_id= ""
	_indicator_low= ""
	_instance_type= ""
	_platform= ""
	_persistent_factor= ""
	_indicator_weight= ""
	_indicator_high= ""
	_indicator= ""
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
			return "instance_score_threshold"
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
			return "instance_score_thresholds"
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
	get Indicator low threshold value
	'''
	@property
	def indicator_low(self) :
		try:
			return self._indicator_low
		except Exception as e :
			raise e
	'''
	set Indicator low threshold value
	'''
	@indicator_low.setter
	def indicator_low(self,indicator_low):
		try :
			if not isinstance(indicator_low,float):
				raise TypeError("indicator_low must be set to float value")
			self._indicator_low = indicator_low
		except Exception as e :
			raise e


	'''
	get Instance type
	'''
	@property
	def instance_type(self) :
		try:
			return self._instance_type
		except Exception as e :
			raise e
	'''
	set Instance type
	'''
	@instance_type.setter
	def instance_type(self,instance_type):
		try :
			if not isinstance(instance_type,str):
				raise TypeError("instance_type must be set to str value")
			self._instance_type = instance_type
		except Exception as e :
			raise e


	'''
	get Instance Platform
	'''
	@property
	def platform(self) :
		try:
			return self._platform
		except Exception as e :
			raise e
	'''
	set Instance Platform
	'''
	@platform.setter
	def platform(self,platform):
		try :
			if not isinstance(platform,str):
				raise TypeError("platform must be set to str value")
			self._platform = platform
		except Exception as e :
			raise e


	'''
	get Indicator persistent factor
	'''
	@property
	def persistent_factor(self) :
		try:
			return self._persistent_factor
		except Exception as e :
			raise e
	'''
	set Indicator persistent factor
	'''
	@persistent_factor.setter
	def persistent_factor(self,persistent_factor):
		try :
			if not isinstance(persistent_factor,float):
				raise TypeError("persistent_factor must be set to float value")
			self._persistent_factor = persistent_factor
		except Exception as e :
			raise e


	'''
	get Indicator weight
	'''
	@property
	def indicator_weight(self) :
		try:
			return self._indicator_weight
		except Exception as e :
			raise e
	'''
	set Indicator weight
	'''
	@indicator_weight.setter
	def indicator_weight(self,indicator_weight):
		try :
			if not isinstance(indicator_weight,float):
				raise TypeError("indicator_weight must be set to float value")
			self._indicator_weight = indicator_weight
		except Exception as e :
			raise e


	'''
	get Indicator high threshold value
	'''
	@property
	def indicator_high(self) :
		try:
			return self._indicator_high
		except Exception as e :
			raise e
	'''
	set Indicator high threshold value
	'''
	@indicator_high.setter
	def indicator_high(self,indicator_high):
		try :
			if not isinstance(indicator_high,float):
				raise TypeError("indicator_high must be set to float value")
			self._indicator_high = indicator_high
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
	Use this operation to get device score threshold.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				instance_score_threshold_obj=instance_score_threshold()
				response = instance_score_threshold_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of instance_score_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			instance_score_threshold_obj = instance_score_threshold()
			option_ = options()
			option_._filter=filter_
			return instance_score_threshold_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the instance_score_threshold resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			instance_score_threshold_obj = instance_score_threshold()
			option_ = options()
			option_._count=True
			response = instance_score_threshold_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of instance_score_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			instance_score_threshold_obj = instance_score_threshold()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = instance_score_threshold_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(instance_score_threshold_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.instance_score_threshold
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(instance_score_threshold_responses, response, "instance_score_threshold_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.instance_score_threshold_response_array
				i=0
				error = [instance_score_threshold() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.instance_score_threshold_response_array
			i=0
			instance_score_threshold_objs = [instance_score_threshold() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_instance_score_threshold'):
					for props in obj._instance_score_threshold:
						result = service.payload_formatter.string_to_bulk_resource(instance_score_threshold_response,self.__class__.__name__,props)
						instance_score_threshold_objs[i] = result.instance_score_threshold
						i=i+1
			return instance_score_threshold_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(instance_score_threshold,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class instance_score_threshold_response(base_response):
	def __init__(self,length=1) :
		self.instance_score_threshold= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.instance_score_threshold= [ instance_score_threshold() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class instance_score_threshold_responses(base_response):
	def __init__(self,length=1) :
		self.instance_score_threshold_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.instance_score_threshold_response_array = [ instance_score_threshold() for _ in range(length)]
