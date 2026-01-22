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
Configuration for Bulk configuration of analytics resource
'''

class bulk_configure_analytics(base_resource):
	_id= ""
	_act_id= ""
	_hdx_insights= ""
	_auto_enable_analytics= ""
	_gateway_insights= ""
	_bot_insights= ""
	_ctnsappname_regex= ""
	_type= ""
	_security_insights= ""
	_policy_name= ""
	_waf_insights= ""
	_ns_ip_address_regex= ""
	_web_insights= ""
	_client_side_measurement= ""
	_gw_enablement= ""
	_analytics_op= ""
	_ns_ip_address_arr=[]
	_ns_ip_address= ""
	_tenant_id= ""
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
			return "bulk_configure_analytics"
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
			return "bulk_configure_analyticss"
		except Exception as e :
			raise e



	'''
	get Primary key for this table.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Primary key for this table.
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
	get Activity Id
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e


	'''
	get Configure HDX Insights for all vips
	'''
	@property
	def hdx_insights(self) :
		try:
			return self._hdx_insights
		except Exception as e :
			raise e
	'''
	set Configure HDX Insights for all vips
	'''
	@hdx_insights.setter
	def hdx_insights(self,hdx_insights):
		try :
			if not isinstance(hdx_insights,bool):
				raise TypeError("hdx_insights must be set to bool value")
			self._hdx_insights = hdx_insights
		except Exception as e :
			raise e


	'''
	get Save and apply this config for all the future discovered applicable vservers
	'''
	@property
	def auto_enable_analytics(self) :
		try:
			return self._auto_enable_analytics
		except Exception as e :
			raise e
	'''
	set Save and apply this config for all the future discovered applicable vservers
	'''
	@auto_enable_analytics.setter
	def auto_enable_analytics(self,auto_enable_analytics):
		try :
			if not isinstance(auto_enable_analytics,bool):
				raise TypeError("auto_enable_analytics must be set to bool value")
			self._auto_enable_analytics = auto_enable_analytics
		except Exception as e :
			raise e


	'''
	get Configure Gateway Insights for all vips
	'''
	@property
	def gateway_insights(self) :
		try:
			return self._gateway_insights
		except Exception as e :
			raise e
	'''
	set Configure Gateway Insights for all vips
	'''
	@gateway_insights.setter
	def gateway_insights(self,gateway_insights):
		try :
			if not isinstance(gateway_insights,bool):
				raise TypeError("gateway_insights must be set to bool value")
			self._gateway_insights = gateway_insights
		except Exception as e :
			raise e


	'''
	get Configure Bot Insights for all vips
	'''
	@property
	def bot_insights(self) :
		try:
			return self._bot_insights
		except Exception as e :
			raise e
	'''
	set Configure Bot Insights for all vips
	'''
	@bot_insights.setter
	def bot_insights(self,bot_insights):
		try :
			if not isinstance(bot_insights,bool):
				raise TypeError("bot_insights must be set to bool value")
			self._bot_insights = bot_insights
		except Exception as e :
			raise e


	'''
	get ctnsappname_Regex
	'''
	@property
	def ctnsappname_regex(self) :
		try:
			return self._ctnsappname_regex
		except Exception as e :
			raise e
	'''
	set ctnsappname_Regex
	'''
	@ctnsappname_regex.setter
	def ctnsappname_regex(self,ctnsappname_regex):
		try :
			if not isinstance(ctnsappname_regex,str):
				raise TypeError("ctnsappname_regex must be set to str value")
			self._ctnsappname_regex = ctnsappname_regex
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set 
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Configure Security Insights for all vips
	'''
	@property
	def security_insights(self) :
		try:
			return self._security_insights
		except Exception as e :
			raise e
	'''
	set Configure Security Insights for all vips
	'''
	@security_insights.setter
	def security_insights(self,security_insights):
		try :
			if not isinstance(security_insights,bool):
				raise TypeError("security_insights must be set to bool value")
			self._security_insights = security_insights
		except Exception as e :
			raise e


	'''
	get Policy Name used for naming a Global Analytics config
	'''
	@property
	def policy_name(self) :
		try:
			return self._policy_name
		except Exception as e :
			raise e
	'''
	set Policy Name used for naming a Global Analytics config
	'''
	@policy_name.setter
	def policy_name(self,policy_name):
		try :
			if not isinstance(policy_name,str):
				raise TypeError("policy_name must be set to str value")
			self._policy_name = policy_name
		except Exception as e :
			raise e


	'''
	get Configure WAF Insights for all vips
	'''
	@property
	def waf_insights(self) :
		try:
			return self._waf_insights
		except Exception as e :
			raise e
	'''
	set Configure WAF Insights for all vips
	'''
	@waf_insights.setter
	def waf_insights(self,waf_insights):
		try :
			if not isinstance(waf_insights,bool):
				raise TypeError("waf_insights must be set to bool value")
			self._waf_insights = waf_insights
		except Exception as e :
			raise e


	'''
	get ns_ip_address_Regex
	'''
	@property
	def ns_ip_address_regex(self) :
		try:
			return self._ns_ip_address_regex
		except Exception as e :
			raise e
	'''
	set ns_ip_address_Regex
	'''
	@ns_ip_address_regex.setter
	def ns_ip_address_regex(self,ns_ip_address_regex):
		try :
			if not isinstance(ns_ip_address_regex,str):
				raise TypeError("ns_ip_address_regex must be set to str value")
			self._ns_ip_address_regex = ns_ip_address_regex
		except Exception as e :
			raise e


	'''
	get Configure WebInsights for all vips
	'''
	@property
	def web_insights(self) :
		try:
			return self._web_insights
		except Exception as e :
			raise e
	'''
	set Configure WebInsights for all vips
	'''
	@web_insights.setter
	def web_insights(self,web_insights):
		try :
			if not isinstance(web_insights,bool):
				raise TypeError("web_insights must be set to bool value")
			self._web_insights = web_insights
		except Exception as e :
			raise e


	'''
	get Configure Client Side Measurement for all vips
	'''
	@property
	def client_side_measurement(self) :
		try:
			return self._client_side_measurement
		except Exception as e :
			raise e
	'''
	set Configure Client Side Measurement for all vips
	'''
	@client_side_measurement.setter
	def client_side_measurement(self,client_side_measurement):
		try :
			if not isinstance(client_side_measurement,bool):
				raise TypeError("client_side_measurement must be set to bool value")
			self._client_side_measurement = client_side_measurement
		except Exception as e :
			raise e

	'''
	Flag to indicate if request is for GW Analytics
	'''
	@property
	def gw_enablement(self):
		try:
			return self._gw_enablement
		except Exception as e :
			raise e
	'''
	Flag to indicate if request is for GW Analytics
	'''
	@gw_enablement.setter
	def gw_enablement(self,gw_enablement):
		try :
			if not isinstance(gw_enablement,bool):
				raise TypeError("gw_enablement must be set to bool value")
			self._gw_enablement = gw_enablement
		except Exception as e :
			raise e

	'''
	Analytics operation enable/disable
	'''
	@property
	def analytics_op(self):
		try:
			return self._analytics_op
		except Exception as e :
			raise e
	'''
	Analytics operation enable/disable
	'''
	@analytics_op.setter
	def analytics_op(self,analytics_op):
		try :
			if not isinstance(analytics_op,str):
				raise TypeError("analytics_op must be set to str value")
			self._analytics_op = analytics_op
		except Exception as e :
			raise e

	'''
	List of NetScaler IP Address
	'''
	@property
	def ns_ip_address_arr(self) :
		try:
			return self._ns_ip_address_arr
		except Exception as e :
			raise e
	'''
	List of NetScaler IP Address
	'''
	@ns_ip_address_arr.setter
	def ns_ip_address_arr(self,ns_ip_address_arr) :
		try :
			if not isinstance(ns_ip_address_arr,list):
				raise TypeError("ns_ip_address_arr must be set to array of str value")
			for item in ns_ip_address_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_ip_address_arr = ns_ip_address_arr
		except Exception as e :
			raise e

	'''
	NS IP Address
	'''
	@property
	def ns_ip_address(self):
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	NS IP Address
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e

	'''
	Tenant ID
	'''
	@property
	def tenant_id(self):
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	Tenant ID
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e

	'''
	Use this operation to modify bulk_configure_analytics.
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
				bulk_configure_analytics_obj=bulk_configure_analytics()
				return cls.update_bulk_request(client,resource,bulk_configure_analytics_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add bulk_configure_analytics.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				return res
			else : 
				bulk_configure_analytics_obj= bulk_configure_analytics()
				return cls.perform_operation_bulk_request(service,resource,bulk_configure_analytics_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete bulk_configure_analytics.
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
					bulk_configure_analytics_obj=bulk_configure_analytics()
					return cls.delete_bulk_request(client,resource,bulk_configure_analytics_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get bulk_configure_analytics.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				bulk_configure_analytics_obj=bulk_configure_analytics()
				response = bulk_configure_analytics_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of bulk_configure_analytics resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			bulk_configure_analytics_obj = bulk_configure_analytics()
			option_ = options()
			option_._filter=filter_
			return bulk_configure_analytics_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the bulk_configure_analytics resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			bulk_configure_analytics_obj = bulk_configure_analytics()
			option_ = options()
			option_._count=True
			response = bulk_configure_analytics_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of bulk_configure_analytics resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			bulk_configure_analytics_obj = bulk_configure_analytics()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = bulk_configure_analytics_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(bulk_configure_analytics_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.bulk_configure_analytics
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(bulk_configure_analytics_responses, response, "bulk_configure_analytics_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.bulk_configure_analytics_response_array
				i=0
				error = [bulk_configure_analytics() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.bulk_configure_analytics_response_array
			i=0
			bulk_configure_analytics_objs = [bulk_configure_analytics() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_bulk_configure_analytics'):
					for props in obj._bulk_configure_analytics:
						result = service.payload_formatter.string_to_bulk_resource(bulk_configure_analytics_response,self.__class__.__name__,props)
						bulk_configure_analytics_objs[i] = result.bulk_configure_analytics
						i=i+1
			return bulk_configure_analytics_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(bulk_configure_analytics,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class bulk_configure_analytics_response(base_response):
	def __init__(self,length=1) :
		self.bulk_configure_analytics= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.bulk_configure_analytics= [ bulk_configure_analytics() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class bulk_configure_analytics_responses(base_response):
	def __init__(self,length=1) :
		self.bulk_configure_analytics_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.bulk_configure_analytics_response_array = [ bulk_configure_analytics() for _ in range(length)]
