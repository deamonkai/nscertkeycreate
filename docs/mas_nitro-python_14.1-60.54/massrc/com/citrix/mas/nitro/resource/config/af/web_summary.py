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
Configuration for AF WEB Summary Report table resource
'''

class web_summary(base_resource):
	_ctnsappname_b= ""
	_device_ip_address= ""
	_ssl_error_type= ""
	_ip_address= ""
	_servercertsize_frontend= ""
	_application_response_time= ""
	_total_requests= ""
	_total_bytes= ""
	_application_name= ""
	_render_time= ""
	_server_response_time= ""
	_id= ""
	_app_unit_name= ""
	_total_dist_count= ""
	_rpt_sample_time= ""
	_network_latency_server_side= ""
	_network_latency_client_side= ""
	_cipherstrength_frontend= ""
	_app_unit_ip_address= ""
	___count= ""
	_sslVersion_frontend= ""
	_load_time= ""
	_srvr_cert_hash_frontend= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "web_summary"
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
			return "web_summarys"
		except Exception as e :
			raise e


	'''
	Backend LB vserver
	'''
	@property
	def ctnsappname_b(self):
		try:
			return self._ctnsappname_b
		except Exception as e :
			raise e
	'''
	Backend LB vserver
	'''
	@ctnsappname_b.setter
	def ctnsappname_b(self,ctnsappname_b):
		try :
			if not isinstance(ctnsappname_b,str):
				raise TypeError("ctnsappname_b must be set to str value")
			self._ctnsappname_b = ctnsappname_b
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
	SSL Error Type. frontend=1, backend=2.
	'''
	@property
	def ssl_error_type(self):
		try:
			return self._ssl_error_type
		except Exception as e :
			raise e
	'''
	SSL Error Type. frontend=1, backend=2.
	'''
	@ssl_error_type.setter
	def ssl_error_type(self,ssl_error_type):
		try :
			if not isinstance(ssl_error_type,int):
				raise TypeError("ssl_error_type must be set to int value")
			self._ssl_error_type = ssl_error_type
		except Exception as e :
			raise e

	'''
	Source IP Address
	'''
	@property
	def ip_address(self):
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	Source IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e

	'''
	SSL Error Type. frontend=1, backend=2.
	'''
	@property
	def servercertsize_frontend(self):
		try:
			return self._servercertsize_frontend
		except Exception as e :
			raise e
	'''
	SSL Error Type. frontend=1, backend=2.
	'''
	@servercertsize_frontend.setter
	def servercertsize_frontend(self,servercertsize_frontend):
		try :
			if not isinstance(servercertsize_frontend,int):
				raise TypeError("servercertsize_frontend must be set to int value")
			self._servercertsize_frontend = servercertsize_frontend
		except Exception as e :
			raise e

	'''
	Application response time.
	'''
	@property
	def application_response_time(self):
		try:
			return self._application_response_time
		except Exception as e :
			raise e
	'''
	Application response time.
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
	Count of this URL in given sampled timeframe.
	'''
	@property
	def total_requests(self):
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	Count of this URL in given sampled timeframe.
	'''
	@total_requests.setter
	def total_requests(self,total_requests):
		try :
			if not isinstance(total_requests,float):
				raise TypeError("total_requests must be set to float value")
			self._total_requests = total_requests
		except Exception as e :
			raise e

	'''
	Total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes accounted by this URL in sampled timeframe.
	'''
	@total_bytes.setter
	def total_bytes(self,total_bytes):
		try :
			if not isinstance(total_bytes,float):
				raise TypeError("total_bytes must be set to float value")
			self._total_bytes = total_bytes
		except Exception as e :
			raise e

	'''
	Application Name
	'''
	@property
	def application_name(self):
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	Application Name
	'''
	@application_name.setter
	def application_name(self,application_name):
		try :
			if not isinstance(application_name,str):
				raise TypeError("application_name must be set to str value")
			self._application_name = application_name
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
	Server response time.
	'''
	@property
	def server_response_time(self):
		try:
			return self._server_response_time
		except Exception as e :
			raise e
	'''
	Server response time.
	'''
	@server_response_time.setter
	def server_response_time(self,server_response_time):
		try :
			if not isinstance(server_response_time,float):
				raise TypeError("server_response_time must be set to float value")
			self._server_response_time = server_response_time
		except Exception as e :
			raise e

	'''
	Id is HTTP Req URL.
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is HTTP Req URL.
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
	 Total Distinct entity count
	'''
	@property
	def total_dist_count(self):
		try:
			return self._total_dist_count
		except Exception as e :
			raise e
	'''
	 Total Distinct entity count
	'''
	@total_dist_count.setter
	def total_dist_count(self,total_dist_count):
		try :
			if not isinstance(total_dist_count,long):
				raise TypeError("total_dist_count must be set to long value")
			self._total_dist_count = total_dist_count
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
			if not isinstance(rpt_sample_time,long):
				raise TypeError("rpt_sample_time must be set to long value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e

	'''
	Network latency server side.
	'''
	@property
	def network_latency_server_side(self):
		try:
			return self._network_latency_server_side
		except Exception as e :
			raise e
	'''
	Network latency server side.
	'''
	@network_latency_server_side.setter
	def network_latency_server_side(self,network_latency_server_side):
		try :
			if not isinstance(network_latency_server_side,float):
				raise TypeError("network_latency_server_side must be set to float value")
			self._network_latency_server_side = network_latency_server_side
		except Exception as e :
			raise e

	'''
	Network latency client side.
	'''
	@property
	def network_latency_client_side(self):
		try:
			return self._network_latency_client_side
		except Exception as e :
			raise e
	'''
	Network latency client side.
	'''
	@network_latency_client_side.setter
	def network_latency_client_side(self,network_latency_client_side):
		try :
			if not isinstance(network_latency_client_side,float):
				raise TypeError("network_latency_client_side must be set to float value")
			self._network_latency_client_side = network_latency_client_side
		except Exception as e :
			raise e

	'''
	SSL Error Type. frontend=1, backend=2.
	'''
	@property
	def cipherstrength_frontend(self):
		try:
			return self._cipherstrength_frontend
		except Exception as e :
			raise e
	'''
	SSL Error Type. frontend=1, backend=2.
	'''
	@cipherstrength_frontend.setter
	def cipherstrength_frontend(self,cipherstrength_frontend):
		try :
			if not isinstance(cipherstrength_frontend,int):
				raise TypeError("cipherstrength_frontend must be set to int value")
			self._cipherstrength_frontend = cipherstrength_frontend
		except Exception as e :
			raise e

	'''
	HTTP Request Host.
	'''
	@property
	def app_unit_ip_address(self):
		try:
			return self._app_unit_ip_address
		except Exception as e :
			raise e
	'''
	HTTP Request Host.
	'''
	@app_unit_ip_address.setter
	def app_unit_ip_address(self,app_unit_ip_address):
		try :
			if not isinstance(app_unit_ip_address,str):
				raise TypeError("app_unit_ip_address must be set to str value")
			self._app_unit_ip_address = app_unit_ip_address
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
			if not isinstance(__count,long):
				raise TypeError("__count must be set to long value")
			self.___count = __count
		except Exception as e :
			raise e

	'''
	SSL Error Type. frontend=1, backend=2.
	'''
	@property
	def sslVersion_frontend(self):
		try:
			return self._sslVersion_frontend
		except Exception as e :
			raise e
	'''
	SSL Error Type. frontend=1, backend=2.
	'''
	@sslVersion_frontend.setter
	def sslVersion_frontend(self,sslVersion_frontend):
		try :
			if not isinstance(sslVersion_frontend,int):
				raise TypeError("sslVersion_frontend must be set to int value")
			self._sslVersion_frontend = sslVersion_frontend
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
	SSL Error Type. frontend=1, backend=2.
	'''
	@property
	def srvr_cert_hash_frontend(self):
		try:
			return self._srvr_cert_hash_frontend
		except Exception as e :
			raise e
	'''
	SSL Error Type. frontend=1, backend=2.
	'''
	@srvr_cert_hash_frontend.setter
	def srvr_cert_hash_frontend(self,srvr_cert_hash_frontend):
		try :
			if not isinstance(srvr_cert_hash_frontend,int):
				raise TypeError("srvr_cert_hash_frontend must be set to int value")
			self._srvr_cert_hash_frontend = srvr_cert_hash_frontend
		except Exception as e :
			raise e

	'''
	Af Report for Web Summary being Count Managed by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				web_summary_obj=web_summary()
				response = web_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of web_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			web_summary_obj = web_summary()
			option_ = options()
			option_._filter=filter_
			return web_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the web_summary resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			web_summary_obj = web_summary()
			option_ = options()
			option_._count=True
			response = web_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of web_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			web_summary_obj = web_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = web_summary_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - report_start_time
	'''
	@classmethod
	def set_queryparam_report_start_time(cls, option, value):
		option.add_queryparam("report_start_time",value)

	'''
	Set Query Parameter - order_by
	'''
	@classmethod
	def set_queryparam_order_by(cls, option, value):
		option.add_queryparam("order_by",value)

	'''
	Set Query Parameter - type
	'''
	@classmethod
	def set_queryparam_type(cls, option, value):
		option.add_queryparam("type",value)

	'''
	Set Query Parameter - cr_enabled
	'''
	@classmethod
	def set_queryparam_cr_enabled(cls, option, value):
		option.add_queryparam("cr_enabled",value)

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(web_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.web_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(web_summary_responses, response, "web_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.web_summary_response_array
				i=0
				error = [web_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.web_summary_response_array
			i=0
			web_summary_objs = [web_summary() for _ in range(len(response))]
			for obj in response :
				for props in obj._web_summary:
					result = service.payload_formatter.string_to_bulk_resource(web_summary_response,self.__class__.__name__,props)
					web_summary_objs[i] = result.web_summary
					i=i+1
			return web_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(web_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class web_summary_response(base_response):
	def __init__(self,length=1) :
		self.web_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.web_summary= [ web_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class web_summary_responses(base_response):
	def __init__(self,length=1) :
		self.web_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.web_summary_response_array = [ web_summary() for _ in range(length)]
