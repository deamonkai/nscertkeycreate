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
Configuration for Holds information regarding count of vips per analytics feature enabled resource
'''

class analytics_feature_summary(base_resource):
	_client_side_measurement= ""
	_bot_insights= ""
	_waf_insights= ""
	_web_insights= ""
	_gateway_insights= ""
	_hdx_insights= ""
	_security_insights= ""
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
			return "analytics_feature_summary"
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
			return "analytics_feature_summarys"
		except Exception as e :
			raise e



	'''
	get vip count with ClientSideMeasurement enabled
	'''
	@property
	def client_side_measurement(self) :
		try:
			return self._client_side_measurement
		except Exception as e :
			raise e
	'''
	set vip count with ClientSideMeasurement enabled
	'''
	@client_side_measurement.setter
	def client_side_measurement(self,client_side_measurement):
		try :
			if not isinstance(client_side_measurement,int):
				raise TypeError("client_side_measurement must be set to int value")
			self._client_side_measurement = client_side_measurement
		except Exception as e :
			raise e


	'''
	get vip count with bot insights enableds
	'''
	@property
	def bot_insights(self) :
		try:
			return self._bot_insights
		except Exception as e :
			raise e
	'''
	set vip count with bot insights enableds
	'''
	@bot_insights.setter
	def bot_insights(self,bot_insights):
		try :
			if not isinstance(bot_insights,int):
				raise TypeError("bot_insights must be set to int value")
			self._bot_insights = bot_insights
		except Exception as e :
			raise e


	'''
	get vip count with waf insights enabled
	'''
	@property
	def waf_insights(self) :
		try:
			return self._waf_insights
		except Exception as e :
			raise e
	'''
	set vip count with waf insights enabled
	'''
	@waf_insights.setter
	def waf_insights(self,waf_insights):
		try :
			if not isinstance(waf_insights,int):
				raise TypeError("waf_insights must be set to int value")
			self._waf_insights = waf_insights
		except Exception as e :
			raise e


	'''
	get vip count with web insights enabled
	'''
	@property
	def web_insights(self) :
		try:
			return self._web_insights
		except Exception as e :
			raise e
	'''
	set vip count with web insights enabled
	'''
	@web_insights.setter
	def web_insights(self,web_insights):
		try :
			if not isinstance(web_insights,int):
				raise TypeError("web_insights must be set to int value")
			self._web_insights = web_insights
		except Exception as e :
			raise e


	'''
	get vip count with gateway insights enabled
	'''
	@property
	def gateway_insights(self) :
		try:
			return self._gateway_insights
		except Exception as e :
			raise e
	'''
	set vip count with gateway insights enabled
	'''
	@gateway_insights.setter
	def gateway_insights(self,gateway_insights):
		try :
			if not isinstance(gateway_insights,int):
				raise TypeError("gateway_insights must be set to int value")
			self._gateway_insights = gateway_insights
		except Exception as e :
			raise e


	'''
	get vip count with HDX insights enabled
	'''
	@property
	def hdx_insights(self) :
		try:
			return self._hdx_insights
		except Exception as e :
			raise e
	'''
	set vip count with HDX insights enabled
	'''
	@hdx_insights.setter
	def hdx_insights(self,hdx_insights):
		try :
			if not isinstance(hdx_insights,int):
				raise TypeError("hdx_insights must be set to int value")
			self._hdx_insights = hdx_insights
		except Exception as e :
			raise e


	'''
	get vip count with security insights enabled
	'''
	@property
	def security_insights(self) :
		try:
			return self._security_insights
		except Exception as e :
			raise e
	'''
	set vip count with security insights enabled
	'''
	@security_insights.setter
	def security_insights(self,security_insights):
		try :
			if not isinstance(security_insights,int):
				raise TypeError("security_insights must be set to int value")
			self._security_insights = security_insights
		except Exception as e :
			raise e

	'''
	Use this operation to get analytics_feature_summary.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				analytics_feature_summary_obj=analytics_feature_summary()
				response = analytics_feature_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of analytics_feature_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			analytics_feature_summary_obj = analytics_feature_summary()
			option_ = options()
			option_._filter=filter_
			return analytics_feature_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the analytics_feature_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			analytics_feature_summary_obj = analytics_feature_summary()
			option_ = options()
			option_._count=True
			response = analytics_feature_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of analytics_feature_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			analytics_feature_summary_obj = analytics_feature_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = analytics_feature_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(analytics_feature_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.analytics_feature_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(analytics_feature_summary_responses, response, "analytics_feature_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.analytics_feature_summary_response_array
				i=0
				error = [analytics_feature_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.analytics_feature_summary_response_array
			i=0
			analytics_feature_summary_objs = [analytics_feature_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_analytics_feature_summary'):
					for props in obj._analytics_feature_summary:
						result = service.payload_formatter.string_to_bulk_resource(analytics_feature_summary_response,self.__class__.__name__,props)
						analytics_feature_summary_objs[i] = result.analytics_feature_summary
						i=i+1
			return analytics_feature_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(analytics_feature_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class analytics_feature_summary_response(base_response):
	def __init__(self,length=1) :
		self.analytics_feature_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.analytics_feature_summary= [ analytics_feature_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class analytics_feature_summary_responses(base_response):
	def __init__(self,length=1) :
		self.analytics_feature_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.analytics_feature_summary_response_array = [ analytics_feature_summary() for _ in range(length)]
