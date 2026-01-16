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
Configuration for Get line graph for top N servers/clients for given metric type, ordering metric, application name, vserver name and time frame resource
'''

class af_top_n_line_graph(base_resource):
	_vserver_name= ""
	_server_response_time= ""
	_limit= ""
	_render_time= ""
	_network_latency_client_side= ""
	_server_ip_address= ""
	_total_requests= ""
	_total_bytes= ""
	_application_name= ""
	_rpt_sample_time= ""
	_client_ip_address= ""
	_network_latency_server_side= ""
	_entity_type= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_top_n_line_graph"
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
			return "af_top_n_line_graphs"
		except Exception as e :
			raise e


	'''
	Vserver name
	'''
	@property
	def vserver_name(self):
		try:
			return self._vserver_name
		except Exception as e :
			raise e
	'''
	Vserver name
	'''
	@vserver_name.setter
	def vserver_name(self,vserver_name):
		try :
			if not isinstance(vserver_name,str):
				raise TypeError("vserver_name must be set to str value")
			self._vserver_name = vserver_name
		except Exception as e :
			raise e

	'''
	Avg. server response time in given sampled time frame
	'''
	@property
	def server_response_time(self):
		try:
			return self._server_response_time
		except Exception as e :
			raise e
	'''
	Avg. server response time in given sampled time frame
	'''
	@server_response_time.setter
	def server_response_time(self,server_response_time):
		try :
			if not isinstance(server_response_time,long):
				raise TypeError("server_response_time must be set to long value")
			self._server_response_time = server_response_time
		except Exception as e :
			raise e

	'''
	Value of N
	'''
	@property
	def limit(self):
		try:
			return self._limit
		except Exception as e :
			raise e
	'''
	Value of N
	'''
	@limit.setter
	def limit(self,limit):
		try :
			if not isinstance(limit,str):
				raise TypeError("limit must be set to str value")
			self._limit = limit
		except Exception as e :
			raise e

	'''
	Avg. render time in given sampled time frame
	'''
	@property
	def render_time(self):
		try:
			return self._render_time
		except Exception as e :
			raise e
	'''
	Avg. render time in given sampled time frame
	'''
	@render_time.setter
	def render_time(self,render_time):
		try :
			if not isinstance(render_time,long):
				raise TypeError("render_time must be set to long value")
			self._render_time = render_time
		except Exception as e :
			raise e

	'''
	Avg. network latency client side in given sampled time frame
	'''
	@property
	def network_latency_client_side(self):
		try:
			return self._network_latency_client_side
		except Exception as e :
			raise e
	'''
	Avg. network latency client side in given sampled time frame
	'''
	@network_latency_client_side.setter
	def network_latency_client_side(self,network_latency_client_side):
		try :
			if not isinstance(network_latency_client_side,long):
				raise TypeError("network_latency_client_side must be set to long value")
			self._network_latency_client_side = network_latency_client_side
		except Exception as e :
			raise e

	'''
	Server IP address
	'''
	@property
	def server_ip_address(self):
		try:
			return self._server_ip_address
		except Exception as e :
			raise e
	'''
	Server IP address
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
	Total request made by server of this application in given sampled time frame
	'''
	@property
	def total_requests(self):
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	Total request made by server of this application in given sampled time frame
	'''
	@total_requests.setter
	def total_requests(self,total_requests):
		try :
			if not isinstance(total_requests,long):
				raise TypeError("total_requests must be set to long value")
			self._total_requests = total_requests
		except Exception as e :
			raise e

	'''
	Total bytes in given sampled time frame
	'''
	@property
	def total_bytes(self):
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	Total bytes in given sampled time frame
	'''
	@total_bytes.setter
	def total_bytes(self,total_bytes):
		try :
			if not isinstance(total_bytes,long):
				raise TypeError("total_bytes must be set to long value")
			self._total_bytes = total_bytes
		except Exception as e :
			raise e

	'''
	vserver_name
	'''
	@property
	def application_name(self):
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	vserver_name
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
	Report Sample time
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	Report Sample time
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
	Client IP address
	'''
	@property
	def client_ip_address(self):
		try:
			return self._client_ip_address
		except Exception as e :
			raise e
	'''
	Client IP address
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
	Avg. network latency server side in given sampled time frame
	'''
	@property
	def network_latency_server_side(self):
		try:
			return self._network_latency_server_side
		except Exception as e :
			raise e
	'''
	Avg. network latency server side in given sampled time frame
	'''
	@network_latency_server_side.setter
	def network_latency_server_side(self,network_latency_server_side):
		try :
			if not isinstance(network_latency_server_side,long):
				raise TypeError("network_latency_server_side must be set to long value")
			self._network_latency_server_side = network_latency_server_side
		except Exception as e :
			raise e

	'''
	Whether the entity is client or server
	'''
	@property
	def entity_type(self):
		try:
			return self._entity_type
		except Exception as e :
			raise e
	'''
	Whether the entity is client or server
	'''
	@entity_type.setter
	def entity_type(self,entity_type):
		try :
			if not isinstance(entity_type,str):
				raise TypeError("entity_type must be set to str value")
			self._entity_type = entity_type
		except Exception as e :
			raise e

	'''
	Get line graph data for top N servers based on some metric for given application and time frame.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_top_n_line_graph_obj=af_top_n_line_graph()
				response = af_top_n_line_graph_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_top_n_line_graph resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_top_n_line_graph_obj = af_top_n_line_graph()
			option_ = options()
			option_._filter=filter_
			return af_top_n_line_graph_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_top_n_line_graph resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_top_n_line_graph_obj = af_top_n_line_graph()
			option_ = options()
			option_._count=True
			response = af_top_n_line_graph_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_top_n_line_graph resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_top_n_line_graph_obj = af_top_n_line_graph()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_top_n_line_graph_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0;
		except Exception as e :
			raise e

	'''
	Set Query Parameter - report_end_time
	'''
	@classmethod
	def set_queryparam_report_end_time(cls, option, value):
		option.add_queryparam("report_end_time",value)

	'''
	Set Query Parameter - duration
	'''
	@classmethod
	def set_queryparam_duration(cls, option, value):
		option.add_queryparam("duration",value)

	'''
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_top_n_line_graph_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_top_n_line_graph
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_top_n_line_graph_responses, response, "af_top_n_line_graph_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_top_n_line_graph_response_array
				i=0
				error = [af_top_n_line_graph() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_top_n_line_graph_response_array
			i=0
			af_top_n_line_graph_objs = [af_top_n_line_graph() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_top_n_line_graph:
					result = service.payload_formatter.string_to_bulk_resource(af_top_n_line_graph_response,self.__class__.__name__,props)
					af_top_n_line_graph_objs[i] = result.af_top_n_line_graph
					i=i+1
			return af_top_n_line_graph_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_top_n_line_graph,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_top_n_line_graph_response(base_response):
	def __init__(self,length=1) :
		self.af_top_n_line_graph= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_top_n_line_graph= [ af_top_n_line_graph() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_top_n_line_graph_responses(base_response):
	def __init__(self,length=1) :
		self.af_top_n_line_graph_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_top_n_line_graph_response_array = [ af_top_n_line_graph() for _ in range(length)]
