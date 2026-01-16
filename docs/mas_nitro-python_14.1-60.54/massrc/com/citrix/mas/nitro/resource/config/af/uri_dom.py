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
Configuration for AF URL dom Report table for Level 1 resource
'''

class uri_dom(base_resource):
	_http_resp_status_name= ""
	_server_ip_address= ""
	_is_embedded_object= ""
	_request_processing_time= ""
	_rpt_sample_time= ""
	_embedded_object_count= ""
	_load_time= ""
	_complete_rendering_time= ""
	___count= ""
	_application_response_time= ""
	_x_scale= ""
	_operating_system_name= ""
	_device_ip_address= ""
	_request_time_to_first_byte= ""
	_client_ip_address= ""
	_user_agent_name= ""
	_id= ""
	_app_unit_name= ""
	_url= ""
	_domain_name= ""
	_response_send_time= ""
	_render_time= ""
	_max_transaction_time= ""
	_http_req_method_name= ""
	_start_rendering_time= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "uri_dom"
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
			return "uri_doms"
		except Exception as e :
			raise e


	'''
	HTTP Response Status Method.
	'''
	@property
	def http_resp_status_name(self):
		try:
			return self._http_resp_status_name
		except Exception as e :
			raise e
	'''
	HTTP Response Status Method.
	'''
	@http_resp_status_name.setter
	def http_resp_status_name(self,http_resp_status_name):
		try :
			if not isinstance(http_resp_status_name,str):
				raise TypeError("http_resp_status_name must be set to str value")
			self._http_resp_status_name = http_resp_status_name
		except Exception as e :
			raise e

	'''
	Server Source IP Address
	'''
	@property
	def server_ip_address(self):
		try:
			return self._server_ip_address
		except Exception as e :
			raise e
	'''
	Server Source IP Address
	'''
	@server_ip_address.setter
	def server_ip_address(self,server_ip_address):
		try :
			if not isinstance(server_ip_address,str):
				raise TypeError("server_ip_address must be set to str value")
			self._server_ip_address = server_ip_address
		except Exception as e :
			raise e

	'''
	is_embedded_object
	'''
	@property
	def is_embedded_object(self):
		try:
			return self._is_embedded_object
		except Exception as e :
			raise e
	'''
	is_embedded_object
	'''
	@is_embedded_object.setter
	def is_embedded_object(self,is_embedded_object):
		try :
			if not isinstance(is_embedded_object,float):
				raise TypeError("is_embedded_object must be set to float value")
			self._is_embedded_object = is_embedded_object
		except Exception as e :
			raise e

	'''
	request_processing_time
	'''
	@property
	def request_processing_time(self):
		try:
			return self._request_processing_time
		except Exception as e :
			raise e
	'''
	request_processing_time
	'''
	@request_processing_time.setter
	def request_processing_time(self,request_processing_time):
		try :
			if not isinstance(request_processing_time,float):
				raise TypeError("request_processing_time must be set to float value")
			self._request_processing_time = request_processing_time
		except Exception as e :
			raise e

	'''
	Report Sample time.
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	Report Sample time.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,float):
				raise TypeError("rpt_sample_time must be set to float value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e

	'''
	embedded_object_count
	'''
	@property
	def embedded_object_count(self):
		try:
			return self._embedded_object_count
		except Exception as e :
			raise e
	'''
	embedded_object_count
	'''
	@embedded_object_count.setter
	def embedded_object_count(self,embedded_object_count):
		try :
			if not isinstance(embedded_object_count,float):
				raise TypeError("embedded_object_count must be set to float value")
			self._embedded_object_count = embedded_object_count
		except Exception as e :
			raise e

	'''
	URI Load time.
	'''
	@property
	def load_time(self):
		try:
			return self._load_time
		except Exception as e :
			raise e
	'''
	URI Load time.
	'''
	@load_time.setter
	def load_time(self,load_time):
		try :
			if not isinstance(load_time,float):
				raise TypeError("load_time must be set to float value")
			self._load_time = load_time
		except Exception as e :
			raise e

	'''
	Render time.
	'''
	@property
	def complete_rendering_time(self):
		try:
			return self._complete_rendering_time
		except Exception as e :
			raise e
	'''
	Render time.
	'''
	@complete_rendering_time.setter
	def complete_rendering_time(self,complete_rendering_time):
		try :
			if not isinstance(complete_rendering_time,float):
				raise TypeError("complete_rendering_time must be set to float value")
			self._complete_rendering_time = complete_rendering_time
		except Exception as e :
			raise e

	'''
	count.
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	count.
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
	Application Response Time.
	'''
	@property
	def application_response_time(self):
		try:
			return self._application_response_time
		except Exception as e :
			raise e
	'''
	Application Response Time.
	'''
	@application_response_time.setter
	def application_response_time(self,application_response_time):
		try :
			if not isinstance(application_response_time,float):
				raise TypeError("application_response_time must be set to float value")
			self._application_response_time = application_response_time
		except Exception as e :
			raise e

	'''
	x_scale
	'''
	@property
	def x_scale(self):
		try:
			return self._x_scale
		except Exception as e :
			raise e
	'''
	x_scale
	'''
	@x_scale.setter
	def x_scale(self,x_scale):
		try :
			if not isinstance(x_scale,float):
				raise TypeError("x_scale must be set to float value")
			self._x_scale = x_scale
		except Exception as e :
			raise e

	'''
	Client Operating System Name.
	'''
	@property
	def operating_system_name(self):
		try:
			return self._operating_system_name
		except Exception as e :
			raise e
	'''
	Client Operating System Name.
	'''
	@operating_system_name.setter
	def operating_system_name(self,operating_system_name):
		try :
			if not isinstance(operating_system_name,str):
				raise TypeError("operating_system_name must be set to str value")
			self._operating_system_name = operating_system_name
		except Exception as e :
			raise e

	'''
	NetScaler IP Address.
	'''
	@property
	def device_ip_address(self):
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address.
	'''
	@device_ip_address.setter
	def device_ip_address(self,device_ip_address):
		try :
			if not isinstance(device_ip_address,str):
				raise TypeError("device_ip_address must be set to str value")
			self._device_ip_address = device_ip_address
		except Exception as e :
			raise e

	'''
	request_time_to_first_byte
	'''
	@property
	def request_time_to_first_byte(self):
		try:
			return self._request_time_to_first_byte
		except Exception as e :
			raise e
	'''
	request_time_to_first_byte
	'''
	@request_time_to_first_byte.setter
	def request_time_to_first_byte(self,request_time_to_first_byte):
		try :
			if not isinstance(request_time_to_first_byte,float):
				raise TypeError("request_time_to_first_byte must be set to float value")
			self._request_time_to_first_byte = request_time_to_first_byte
		except Exception as e :
			raise e

	'''
	Client Source IP Address
	'''
	@property
	def client_ip_address(self):
		try:
			return self._client_ip_address
		except Exception as e :
			raise e
	'''
	Client Source IP Address
	'''
	@client_ip_address.setter
	def client_ip_address(self,client_ip_address):
		try :
			if not isinstance(client_ip_address,str):
				raise TypeError("client_ip_address must be set to str value")
			self._client_ip_address = client_ip_address
		except Exception as e :
			raise e

	'''
	User Agent Name.
	'''
	@property
	def user_agent_name(self):
		try:
			return self._user_agent_name
		except Exception as e :
			raise e
	'''
	User Agent Name.
	'''
	@user_agent_name.setter
	def user_agent_name(self,user_agent_name):
		try :
			if not isinstance(user_agent_name,str):
				raise TypeError("user_agent_name must be set to str value")
			self._user_agent_name = user_agent_name
		except Exception as e :
			raise e

	'''
	Id is URL Dom.
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is URL Dom.
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
	AppName
	'''
	@property
	def app_unit_name(self):
		try:
			return self._app_unit_name
		except Exception as e :
			raise e
	'''
	AppName
	'''
	@app_unit_name.setter
	def app_unit_name(self,app_unit_name):
		try :
			if not isinstance(app_unit_name,str):
				raise TypeError("app_unit_name must be set to str value")
			self._app_unit_name = app_unit_name
		except Exception as e :
			raise e

	'''
	HTTP Request URL.
	'''
	@property
	def url(self):
		try:
			return self._url
		except Exception as e :
			raise e
	'''
	HTTP Request URL.
	'''
	@url.setter
	def url(self,url):
		try :
			if not isinstance(url,str):
				raise TypeError("url must be set to str value")
			self._url = url
		except Exception as e :
			raise e

	'''
	Domain Name.
	'''
	@property
	def domain_name(self):
		try:
			return self._domain_name
		except Exception as e :
			raise e
	'''
	Domain Name.
	'''
	@domain_name.setter
	def domain_name(self,domain_name):
		try :
			if not isinstance(domain_name,str):
				raise TypeError("domain_name must be set to str value")
			self._domain_name = domain_name
		except Exception as e :
			raise e

	'''
	response_send_time
	'''
	@property
	def response_send_time(self):
		try:
			return self._response_send_time
		except Exception as e :
			raise e
	'''
	response_send_time
	'''
	@response_send_time.setter
	def response_send_time(self,response_send_time):
		try :
			if not isinstance(response_send_time,float):
				raise TypeError("response_send_time must be set to float value")
			self._response_send_time = response_send_time
		except Exception as e :
			raise e

	'''
	Render time.
	'''
	@property
	def render_time(self):
		try:
			return self._render_time
		except Exception as e :
			raise e
	'''
	Render time.
	'''
	@render_time.setter
	def render_time(self,render_time):
		try :
			if not isinstance(render_time,float):
				raise TypeError("render_time must be set to float value")
			self._render_time = render_time
		except Exception as e :
			raise e

	'''
	Last Transaction Time for this URL in the sampled timeframe.
	'''
	@property
	def max_transaction_time(self):
		try:
			return self._max_transaction_time
		except Exception as e :
			raise e
	'''
	Last Transaction Time for this URL in the sampled timeframe.
	'''
	@max_transaction_time.setter
	def max_transaction_time(self,max_transaction_time):
		try :
			if not isinstance(max_transaction_time,float):
				raise TypeError("max_transaction_time must be set to float value")
			self._max_transaction_time = max_transaction_time
		except Exception as e :
			raise e

	'''
	HTTP Request Method.
	'''
	@property
	def http_req_method_name(self):
		try:
			return self._http_req_method_name
		except Exception as e :
			raise e
	'''
	HTTP Request Method.
	'''
	@http_req_method_name.setter
	def http_req_method_name(self,http_req_method_name):
		try :
			if not isinstance(http_req_method_name,str):
				raise TypeError("http_req_method_name must be set to str value")
			self._http_req_method_name = http_req_method_name
		except Exception as e :
			raise e

	'''
	Render time.
	'''
	@property
	def start_rendering_time(self):
		try:
			return self._start_rendering_time
		except Exception as e :
			raise e
	'''
	Render time.
	'''
	@start_rendering_time.setter
	def start_rendering_time(self,start_rendering_time):
		try :
			if not isinstance(start_rendering_time,float):
				raise TypeError("start_rendering_time must be set to float value")
			self._start_rendering_time = start_rendering_time
		except Exception as e :
			raise e

	'''
	Af Report for Top URL being Count Managed by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				uri_dom_obj=uri_dom()
				response = uri_dom_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of uri_dom resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			uri_dom_obj = uri_dom()
			option_ = options()
			option_._filter=filter_
			return uri_dom_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the uri_dom resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			uri_dom_obj = uri_dom()
			option_ = options()
			option_._count=True
			response = uri_dom_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of uri_dom resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			uri_dom_obj = uri_dom()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = uri_dom_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(uri_dom_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.uri_dom
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(uri_dom_responses, response, "uri_dom_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.uri_dom_response_array
				i=0
				error = [uri_dom() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.uri_dom_response_array
			i=0
			uri_dom_objs = [uri_dom() for _ in range(len(response))]
			for obj in response :
				for props in obj._uri_dom:
					result = service.payload_formatter.string_to_bulk_resource(uri_dom_response,self.__class__.__name__,props)
					uri_dom_objs[i] = result.uri_dom
					i=i+1
			return uri_dom_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(uri_dom,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class uri_dom_response(base_response):
	def __init__(self,length=1) :
		self.uri_dom= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.uri_dom= [ uri_dom() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class uri_dom_responses(base_response):
	def __init__(self,length=1) :
		self.uri_dom_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.uri_dom_response_array = [ uri_dom() for _ in range(length)]
