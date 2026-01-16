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
Configuration for ADC Feature Usage Information resource
'''

class adc_feature_usage(base_resource):
	_icaproxy= ""
	_waf= ""
	_sslvpn= ""
	_ip_address= ""
	_timestamp= ""
	_id= ""
	_bot= ""
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
			return "adc_feature_usage"
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
			return "adc_feature_usages"
		except Exception as e :
			raise e



	'''
	get ICAProxy feature config is present or not
	'''
	@property
	def icaproxy(self) :
		try:
			return self._icaproxy
		except Exception as e :
			raise e
	'''
	set ICAProxy feature config is present or not
	'''
	@icaproxy.setter
	def icaproxy(self,icaproxy):
		try :
			if not isinstance(icaproxy,bool):
				raise TypeError("icaproxy must be set to bool value")
			self._icaproxy = icaproxy
		except Exception as e :
			raise e


	'''
	get WAF feature config is present or not
	'''
	@property
	def waf(self) :
		try:
			return self._waf
		except Exception as e :
			raise e
	'''
	set WAF feature config is present or not
	'''
	@waf.setter
	def waf(self,waf):
		try :
			if not isinstance(waf,bool):
				raise TypeError("waf must be set to bool value")
			self._waf = waf
		except Exception as e :
			raise e


	'''
	get SSLVPN feature config is present or not
	'''
	@property
	def sslvpn(self) :
		try:
			return self._sslvpn
		except Exception as e :
			raise e
	'''
	set SSLVPN feature config is present or not
	'''
	@sslvpn.setter
	def sslvpn(self,sslvpn):
		try :
			if not isinstance(sslvpn,bool):
				raise TypeError("sslvpn must be set to bool value")
			self._sslvpn = sslvpn
		except Exception as e :
			raise e


	'''
	get IP address of device
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e


	'''
	get Timestamp of the feature details
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
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
	get BOT feature config is present or not
	'''
	@property
	def bot(self) :
		try:
			return self._bot
		except Exception as e :
			raise e
	'''
	set BOT feature config is present or not
	'''
	@bot.setter
	def bot(self,bot):
		try :
			if not isinstance(bot,bool):
				raise TypeError("bot must be set to bool value")
			self._bot = bot
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_feature_usage_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_feature_usage
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_feature_usage_responses, response, "adc_feature_usage_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_feature_usage_response_array
				i=0
				error = [adc_feature_usage() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_feature_usage_response_array
			i=0
			adc_feature_usage_objs = [adc_feature_usage() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_feature_usage'):
					for props in obj._adc_feature_usage:
						result = service.payload_formatter.string_to_bulk_resource(adc_feature_usage_response,self.__class__.__name__,props)
						adc_feature_usage_objs[i] = result.adc_feature_usage
						i=i+1
			return adc_feature_usage_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_feature_usage,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_feature_usage_response(base_response):
	def __init__(self,length=1) :
		self.adc_feature_usage= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_feature_usage= [ adc_feature_usage() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_feature_usage_responses(base_response):
	def __init__(self,length=1) :
		self.adc_feature_usage_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_feature_usage_response_array = [ adc_feature_usage() for _ in range(length)]
