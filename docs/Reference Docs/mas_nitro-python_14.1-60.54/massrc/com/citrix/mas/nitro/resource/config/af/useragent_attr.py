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
Configuration for AF User Agent Report table resource
'''

class useragent_attr(base_resource):
	_total_requests= ""
	_total_bytes= ""
	_operating_system_name= ""
	_device_ip_address= ""
	_uri_url= ""
	_rpt_sample_time= ""
	_ctnsappname_b= ""
	_app_unit_name= ""
	_id= ""
	_browser_name= ""
	_load_time= ""
	_render_time= ""
	_app_unit_ip_address= ""
	___count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "useragent_attr"
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
			return "useragent_attrs"
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
	HTTP Request URL.
	'''
	@property
	def uri_url(self):
		try:
			return self._uri_url
		except Exception as e :
			raise e
	'''
	HTTP Request URL.
	'''
	@uri_url.setter
	def uri_url(self,uri_url):
		try :
			if not isinstance(uri_url,str):
				raise TypeError("uri_url must be set to str value")
			self._uri_url = uri_url
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
	Vserver Name
	'''
	@property
	def app_unit_name(self):
		try:
			return self._app_unit_name
		except Exception as e :
			raise e
	'''
	Vserver Name
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
	Id is User Agent.
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is User Agent.
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
	User Agent Name.
	'''
	@property
	def browser_name(self):
		try:
			return self._browser_name
		except Exception as e :
			raise e
	'''
	User Agent Name.
	'''
	@browser_name.setter
	def browser_name(self,browser_name):
		try :
			if not isinstance(browser_name,str):
				raise TypeError("browser_name must be set to str value")
			self._browser_name = browser_name
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
	Vserver IP Address.
	'''
	@property
	def app_unit_ip_address(self):
		try:
			return self._app_unit_ip_address
		except Exception as e :
			raise e
	'''
	Vserver IP Address.
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
	Af Report for Top URL being Count Managed by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				useragent_attr_obj=useragent_attr()
				response = useragent_attr_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of useragent_attr resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			useragent_attr_obj = useragent_attr()
			option_ = options()
			option_._filter=filter_
			return useragent_attr_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the useragent_attr resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			useragent_attr_obj = useragent_attr()
			option_ = options()
			option_._count=True
			response = useragent_attr_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of useragent_attr resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			useragent_attr_obj = useragent_attr()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = useragent_attr_obj.getfiltered(service, option_)
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
	Set Query Parameter - asc
	'''
	@classmethod
	def set_queryparam_asc(cls, option, value):
		option.add_queryparam("asc",value)

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(useragent_attr_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.useragent_attr
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(useragent_attr_responses, response, "useragent_attr_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.useragent_attr_response_array
				i=0
				error = [useragent_attr() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.useragent_attr_response_array
			i=0
			useragent_attr_objs = [useragent_attr() for _ in range(len(response))]
			for obj in response :
				for props in obj._useragent_attr:
					result = service.payload_formatter.string_to_bulk_resource(useragent_attr_response,self.__class__.__name__,props)
					useragent_attr_objs[i] = result.useragent_attr
					i=i+1
			return useragent_attr_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(useragent_attr,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class useragent_attr_response(base_response):
	def __init__(self,length=1) :
		self.useragent_attr= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.useragent_attr= [ useragent_attr() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class useragent_attr_responses(base_response):
	def __init__(self,length=1) :
		self.useragent_attr_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.useragent_attr_response_array = [ useragent_attr() for _ in range(length)]
