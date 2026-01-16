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
Configuration for NetScaler Info Parameters resource
'''

class adc_params(base_resource):
	_httpxforwardedfor= ""
	_geo_support= ""
	_ns_ip_address= ""
	_httpquerywithurl= ""
	_httpcookie= ""
	_id= ""
	_gateway_deployment= ""
	_template_interval= ""
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
			return "adc_params"
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
			return "adc_paramss"
		except Exception as e :
			raise e


	'''
	HTTP x-Forwarded for header flag.
	'''
	@property
	def httpxforwardedfor(self):
		try:
			return self._httpxforwardedfor
		except Exception as e :
			raise e
	'''
	HTTP x-Forwarded for header flag.
	'''
	@httpxforwardedfor.setter
	def httpxforwardedfor(self,httpxforwardedfor):
		try :
			if not isinstance(httpxforwardedfor,str):
				raise TypeError("httpxforwardedfor must be set to str value")
			self._httpxforwardedfor = httpxforwardedfor
		except Exception as e :
			raise e

	'''
	Is this device configured to support GEO location.
	'''
	@property
	def geo_support(self):
		try:
			return self._geo_support
		except Exception as e :
			raise e
	'''
	Is this device configured to support GEO location.
	'''
	@geo_support.setter
	def geo_support(self,geo_support):
		try :
			if not isinstance(geo_support,bool):
				raise TypeError("geo_support must be set to bool value")
			self._geo_support = geo_support
		except Exception as e :
			raise e

	'''
	NetScaler IP Address
	'''
	@property
	def ns_ip_address(self):
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address
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
	URL query param flag.
	'''
	@property
	def httpquerywithurl(self):
		try:
			return self._httpquerywithurl
		except Exception as e :
			raise e
	'''
	URL query param flag.
	'''
	@httpquerywithurl.setter
	def httpquerywithurl(self,httpquerywithurl):
		try :
			if not isinstance(httpquerywithurl,str):
				raise TypeError("httpquerywithurl must be set to str value")
			self._httpquerywithurl = httpquerywithurl
		except Exception as e :
			raise e

	'''
	Cookie-Header flag.
	'''
	@property
	def httpcookie(self):
		try:
			return self._httpcookie
		except Exception as e :
			raise e
	'''
	Cookie-Header flag.
	'''
	@httpcookie.setter
	def httpcookie(self,httpcookie):
		try :
			if not isinstance(httpcookie,str):
				raise TypeError("httpcookie must be set to str value")
			self._httpcookie = httpcookie
		except Exception as e :
			raise e

	'''
	Netscaler ID.
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Netscaler ID.
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
	Is this device acting as Gateway.
	'''
	@property
	def gateway_deployment(self):
		try:
			return self._gateway_deployment
		except Exception as e :
			raise e
	'''
	Is this device acting as Gateway.
	'''
	@gateway_deployment.setter
	def gateway_deployment(self,gateway_deployment):
		try :
			if not isinstance(gateway_deployment,bool):
				raise TypeError("gateway_deployment must be set to bool value")
			self._gateway_deployment = gateway_deployment
		except Exception as e :
			raise e

	'''
	Template refresh interval
	'''
	@property
	def template_interval(self):
		try:
			return self._template_interval
		except Exception as e :
			raise e
	'''
	Template refresh interval
	'''
	@template_interval.setter
	def template_interval(self,template_interval):
		try :
			if not isinstance(template_interval,int):
				raise TypeError("template_interval must be set to int value")
			self._template_interval = template_interval
		except Exception as e :
			raise e

	'''
	Add NetScaler Info params..
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
				adc_params_obj= adc_params()
				return cls.perform_operation_bulk_request(service,resource,adc_params_obj)
		except Exception as e :
			raise e

	'''
	modify NetScaler Info params..
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
				adc_params_obj=adc_params()
				return cls.update_bulk_request(client,resource,adc_params_obj)
		except Exception as e :
			raise e

	'''
	get NetScaler Info params.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adc_params_obj=adc_params()
				response = adc_params_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	delete NetScaler Info params..
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
					adc_params_obj=adc_params()
					return cls.delete_bulk_request(client,resource,adc_params_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adc_params resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adc_params_obj = adc_params()
			option_ = options()
			option_._filter=filter_
			return adc_params_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adc_params resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adc_params_obj = adc_params()
			option_ = options()
			option_._count=True
			response = adc_params_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adc_params resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adc_params_obj = adc_params()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adc_params_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adc_params_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_params
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_params_responses, response, "adc_params_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_params_response_array
				i=0
				error = [adc_params() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_params_response_array
			i=0
			adc_params_objs = [adc_params() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_params'):
					for props in obj._adc_params:
						result = service.payload_formatter.string_to_bulk_resource(adc_params_response,self.__class__.__name__,props)
						adc_params_objs[i] = result.adc_params
						i=i+1
			return adc_params_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_params,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_params_response(base_response):
	def __init__(self,length=1) :
		self.adc_params= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_params= [ adc_params() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_params_responses(base_response):
	def __init__(self,length=1) :
		self.adc_params_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_params_response_array = [ adc_params() for _ in range(length)]
