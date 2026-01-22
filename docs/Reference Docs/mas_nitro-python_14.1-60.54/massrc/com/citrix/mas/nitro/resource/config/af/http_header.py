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
Configuration for Enable/Disable HTTP header info for user_agent, http_req_method, http_resp_status, operating_system as 1st level tree nodes. resource
'''

class http_header(base_resource):
	_http_req_method= ""
	_domain= ""
	_http_resp_status= ""
	_operating_system= ""
	_ic_nostore_reason= ""
	_http_content_type= ""
	_http_media_type= ""
	_user_agent= ""
	___count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "http_header"
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
			return "http_headers"
		except Exception as e :
			raise e



	'''
	get Enable/Disable http req method report
	'''
	@property
	def http_req_method(self) :
		try:
			return self._http_req_method
		except Exception as e :
			raise e
	'''
	set Enable/Disable http req method report
	'''
	@http_req_method.setter
	def http_req_method(self,http_req_method):
		try :
			if not isinstance(http_req_method,bool):
				raise TypeError("http_req_method must be set to bool value")
			self._http_req_method = http_req_method
		except Exception as e :
			raise e


	'''
	get Enable/Disbale Domain report 
	'''
	@property
	def domain(self) :
		try:
			return self._domain
		except Exception as e :
			raise e
	'''
	set Enable/Disbale Domain report 
	'''
	@domain.setter
	def domain(self,domain):
		try :
			if not isinstance(domain,bool):
				raise TypeError("domain must be set to bool value")
			self._domain = domain
		except Exception as e :
			raise e


	'''
	get Enable/Disable Http Resp Status report
	'''
	@property
	def http_resp_status(self) :
		try:
			return self._http_resp_status
		except Exception as e :
			raise e
	'''
	set Enable/Disable Http Resp Status report
	'''
	@http_resp_status.setter
	def http_resp_status(self,http_resp_status):
		try :
			if not isinstance(http_resp_status,bool):
				raise TypeError("http_resp_status must be set to bool value")
			self._http_resp_status = http_resp_status
		except Exception as e :
			raise e


	'''
	get Enable/Disbale Operating System report 
	'''
	@property
	def operating_system(self) :
		try:
			return self._operating_system
		except Exception as e :
			raise e
	'''
	set Enable/Disbale Operating System report 
	'''
	@operating_system.setter
	def operating_system(self,operating_system):
		try :
			if not isinstance(operating_system,bool):
				raise TypeError("operating_system must be set to bool value")
			self._operating_system = operating_system
		except Exception as e :
			raise e


	'''
	get Enable/Disable Cache No Store Reason report
	'''
	@property
	def ic_nostore_reason(self) :
		try:
			return self._ic_nostore_reason
		except Exception as e :
			raise e
	'''
	set Enable/Disable Cache No Store Reason report
	'''
	@ic_nostore_reason.setter
	def ic_nostore_reason(self,ic_nostore_reason):
		try :
			if not isinstance(ic_nostore_reason,bool):
				raise TypeError("ic_nostore_reason must be set to bool value")
			self._ic_nostore_reason = ic_nostore_reason
		except Exception as e :
			raise e


	'''
	get Enable/Disable Http Content Type report
	'''
	@property
	def http_content_type(self) :
		try:
			return self._http_content_type
		except Exception as e :
			raise e
	'''
	set Enable/Disable Http Content Type report
	'''
	@http_content_type.setter
	def http_content_type(self,http_content_type):
		try :
			if not isinstance(http_content_type,bool):
				raise TypeError("http_content_type must be set to bool value")
			self._http_content_type = http_content_type
		except Exception as e :
			raise e


	'''
	get Enable/Disable Http Media Type report
	'''
	@property
	def http_media_type(self) :
		try:
			return self._http_media_type
		except Exception as e :
			raise e
	'''
	set Enable/Disable Http Media Type report
	'''
	@http_media_type.setter
	def http_media_type(self,http_media_type):
		try :
			if not isinstance(http_media_type,bool):
				raise TypeError("http_media_type must be set to bool value")
			self._http_media_type = http_media_type
		except Exception as e :
			raise e


	'''
	get Enable/Disable user agent report
	'''
	@property
	def user_agent(self) :
		try:
			return self._user_agent
		except Exception as e :
			raise e
	'''
	set Enable/Disable user agent report
	'''
	@user_agent.setter
	def user_agent(self,user_agent):
		try :
			if not isinstance(user_agent,bool):
				raise TypeError("user_agent must be set to bool value")
			self._user_agent = user_agent
		except Exception as e :
			raise e


	'''
	get Count.
	'''
	@property
	def __count(self) :
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	set Count.
	'''
	@__count.setter
	def __count(self,__count):
		try :
			if not isinstance(__count,float):
				raise TypeError("__count must be set to float value")
			self.___count = __count
		except Exception as e :
			raise e

	'''
	To get http header value.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				http_header_obj=http_header()
				response = http_header_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	To set http header value.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				http_header_obj=http_header()
				return cls.update_bulk_request(client,resource,http_header_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of http_header resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			http_header_obj = http_header()
			option_ = options()
			option_._filter=filter_
			return http_header_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the http_header resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			http_header_obj = http_header()
			option_ = options()
			option_._count=True
			response = http_header_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of http_header resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			http_header_obj = http_header()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = http_header_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(http_header_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.http_header
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(http_header_responses, response, "http_header_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.http_header_response_array
				i=0
				error = [http_header() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.http_header_response_array
			i=0
			http_header_objs = [http_header() for _ in range(len(response))]
			for obj in response :
				for props in obj._http_header:
					result = service.payload_formatter.string_to_bulk_resource(http_header_response,self.__class__.__name__,props)
					http_header_objs[i] = result.http_header
					i=i+1
			return http_header_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(http_header,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class http_header_response(base_response):
	def __init__(self,length=1) :
		self.http_header= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.http_header= [ http_header() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class http_header_responses(base_response):
	def __init__(self,length=1) :
		self.http_header_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.http_header_response_array = [ http_header() for _ in range(length)]
