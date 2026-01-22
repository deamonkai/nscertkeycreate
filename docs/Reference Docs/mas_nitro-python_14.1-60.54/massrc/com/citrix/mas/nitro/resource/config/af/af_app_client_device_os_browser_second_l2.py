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
Configuration for AF User Agent Report table for Level 2 resource
'''

class af_app_client_device_os_browser_second_l2(base_resource):
	_exporter_id= ""
	_netscaler_processing_time= ""
	_server_response_time_max= ""
	_server_response_time= ""
	_ctnssource_ip_address= ""
	_device= ""
	_render_time= ""
	_application_name= ""
	_application_response_time= ""
	_total_requests= ""
	_total_bytes= ""
	_vservername= ""
	_ip_address= ""
	_browser= ""
	_ic_hits= ""
	_operating_system= ""
	_stnssource_ip_address= ""
	_ctnsappname= ""
	_load_time= ""
	_network_latency_server_side_max= ""
	_ctnssource_ip_address_str= ""
	_stnssource_ip_address_str= ""
	_network_latency_client_side= ""
	_ic_miss= ""
	_network_latency_server_side= ""
	_network_latency_client_side_max= ""
	_rpt_sample_time= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_app_client_device_os_browser_second_l2"
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
			return "af_app_client_device_os_browser_second_l2s"
		except Exception as e :
			raise e



	'''
	get Exporter ID
	'''
	@property
	def exporter_id(self) :
		try:
			return self._exporter_id
		except Exception as e :
			raise e
	'''
	set Exporter ID
	'''
	@exporter_id.setter
	def exporter_id(self,exporter_id):
		try :
			if not isinstance(exporter_id,long):
				raise TypeError("exporter_id must be set to long value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e


	'''
	get NetScaler Processing Time.
	'''
	@property
	def netscaler_processing_time(self) :
		try:
			return self._netscaler_processing_time
		except Exception as e :
			raise e
	'''
	set NetScaler Processing Time.
	'''
	@netscaler_processing_time.setter
	def netscaler_processing_time(self,netscaler_processing_time):
		try :
			if not isinstance(netscaler_processing_time,long):
				raise TypeError("netscaler_processing_time must be set to long value")
			self._netscaler_processing_time = netscaler_processing_time
		except Exception as e :
			raise e


	'''
	get Max value of Server Response Time for given duration.
	'''
	@property
	def server_response_time_max(self) :
		try:
			return self._server_response_time_max
		except Exception as e :
			raise e
	'''
	set Max value of Server Response Time for given duration.
	'''
	@server_response_time_max.setter
	def server_response_time_max(self,server_response_time_max):
		try :
			if not isinstance(server_response_time_max,long):
				raise TypeError("server_response_time_max must be set to long value")
			self._server_response_time_max = server_response_time_max
		except Exception as e :
			raise e


	'''
	get Server Response Time.
	'''
	@property
	def server_response_time(self) :
		try:
			return self._server_response_time
		except Exception as e :
			raise e
	'''
	set Server Response Time.
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
	get Client Source IP Address
	'''
	@property
	def ctnssource_ip_address(self) :
		try:
			return self._ctnssource_ip_address
		except Exception as e :
			raise e
	'''
	set Client Source IP Address
	'''
	@ctnssource_ip_address.setter
	def ctnssource_ip_address(self,ctnssource_ip_address):
		try :
			if not isinstance(ctnssource_ip_address,long):
				raise TypeError("ctnssource_ip_address must be set to long value")
			self._ctnssource_ip_address = ctnssource_ip_address
		except Exception as e :
			raise e


	'''
	get Client Device.
	'''
	@property
	def device(self) :
		try:
			return self._device
		except Exception as e :
			raise e
	'''
	set Client Device.
	'''
	@device.setter
	def device(self,device):
		try :
			if not isinstance(device,int):
				raise TypeError("device must be set to int value")
			self._device = device
		except Exception as e :
			raise e


	'''
	get Render time.
	'''
	@property
	def render_time(self) :
		try:
			return self._render_time
		except Exception as e :
			raise e
	'''
	set Render time.
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
	get Application Name
	'''
	@property
	def application_name(self) :
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	set Application Name
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
	get Application Response Time.
	'''
	@property
	def application_response_time(self) :
		try:
			return self._application_response_time
		except Exception as e :
			raise e
	'''
	set Application Response Time.
	'''
	@application_response_time.setter
	def application_response_time(self,application_response_time):
		try :
			if not isinstance(application_response_time,long):
				raise TypeError("application_response_time must be set to long value")
			self._application_response_time = application_response_time
		except Exception as e :
			raise e


	'''
	get Total Requests for this device in given sampled timeframe.
	'''
	@property
	def total_requests(self) :
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	set Total Requests for this device in given sampled timeframe.
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
	get Total bytes accounted by this URL in sampled timeframe.
	'''
	@property
	def total_bytes(self) :
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	set Total bytes accounted by this URL in sampled timeframe.
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
	get Backend Vserver
	'''
	@property
	def vservername(self) :
		try:
			return self._vservername
		except Exception as e :
			raise e
	'''
	set Backend Vserver
	'''
	@vservername.setter
	def vservername(self,vservername):
		try :
			if not isinstance(vservername,str):
				raise TypeError("vservername must be set to str value")
			self._vservername = vservername
		except Exception as e :
			raise e


	'''
	get Field to store the ip address as it is along with any extension
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Field to store the ip address as it is along with any extension
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
	get Browser.
	'''
	@property
	def browser(self) :
		try:
			return self._browser
		except Exception as e :
			raise e
	'''
	set Browser.
	'''
	@browser.setter
	def browser(self,browser):
		try :
			if not isinstance(browser,int):
				raise TypeError("browser must be set to int value")
			self._browser = browser
		except Exception as e :
			raise e


	'''
	get Total IC hits accounted in sampled timeframe.
	'''
	@property
	def ic_hits(self) :
		try:
			return self._ic_hits
		except Exception as e :
			raise e
	'''
	set Total IC hits accounted in sampled timeframe.
	'''
	@ic_hits.setter
	def ic_hits(self,ic_hits):
		try :
			if not isinstance(ic_hits,long):
				raise TypeError("ic_hits must be set to long value")
			self._ic_hits = ic_hits
		except Exception as e :
			raise e


	'''
	get Operating System.
	'''
	@property
	def operating_system(self) :
		try:
			return self._operating_system
		except Exception as e :
			raise e
	'''
	set Operating System.
	'''
	@operating_system.setter
	def operating_system(self,operating_system):
		try :
			if not isinstance(operating_system,int):
				raise TypeError("operating_system must be set to int value")
			self._operating_system = operating_system
		except Exception as e :
			raise e


	'''
	get Server Source IP Address
	'''
	@property
	def stnssource_ip_address(self) :
		try:
			return self._stnssource_ip_address
		except Exception as e :
			raise e
	'''
	set Server Source IP Address
	'''
	@stnssource_ip_address.setter
	def stnssource_ip_address(self,stnssource_ip_address):
		try :
			if not isinstance(stnssource_ip_address,long):
				raise TypeError("stnssource_ip_address must be set to long value")
			self._stnssource_ip_address = stnssource_ip_address
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@ctnsappname.setter
	def ctnsappname(self,ctnsappname):
		try :
			if not isinstance(ctnsappname,str):
				raise TypeError("ctnsappname must be set to str value")
			self._ctnsappname = ctnsappname
		except Exception as e :
			raise e


	'''
	get URI Load time.
	'''
	@property
	def load_time(self) :
		try:
			return self._load_time
		except Exception as e :
			raise e
	'''
	set URI Load time.
	'''
	@load_time.setter
	def load_time(self,load_time):
		try :
			if not isinstance(load_time,long):
				raise TypeError("load_time must be set to long value")
			self._load_time = load_time
		except Exception as e :
			raise e


	'''
	get Network Latency Client server Time.
	'''
	@property
	def network_latency_server_side_max(self) :
		try:
			return self._network_latency_server_side_max
		except Exception as e :
			raise e
	'''
	set Network Latency Client server Time.
	'''
	@network_latency_server_side_max.setter
	def network_latency_server_side_max(self,network_latency_server_side_max):
		try :
			if not isinstance(network_latency_server_side_max,long):
				raise TypeError("network_latency_server_side_max must be set to long value")
			self._network_latency_server_side_max = network_latency_server_side_max
		except Exception as e :
			raise e


	'''
	get Client Source IP Address String
	'''
	@property
	def ctnssource_ip_address_str(self) :
		try:
			return self._ctnssource_ip_address_str
		except Exception as e :
			raise e
	'''
	set Client Source IP Address String
	'''
	@ctnssource_ip_address_str.setter
	def ctnssource_ip_address_str(self,ctnssource_ip_address_str):
		try :
			if not isinstance(ctnssource_ip_address_str,str):
				raise TypeError("ctnssource_ip_address_str must be set to str value")
			self._ctnssource_ip_address_str = ctnssource_ip_address_str
		except Exception as e :
			raise e


	'''
	get Server Source IP Address String
	'''
	@property
	def stnssource_ip_address_str(self) :
		try:
			return self._stnssource_ip_address_str
		except Exception as e :
			raise e
	'''
	set Server Source IP Address String
	'''
	@stnssource_ip_address_str.setter
	def stnssource_ip_address_str(self,stnssource_ip_address_str):
		try :
			if not isinstance(stnssource_ip_address_str,str):
				raise TypeError("stnssource_ip_address_str must be set to str value")
			self._stnssource_ip_address_str = stnssource_ip_address_str
		except Exception as e :
			raise e


	'''
	get Network Latency Client side Time.
	'''
	@property
	def network_latency_client_side(self) :
		try:
			return self._network_latency_client_side
		except Exception as e :
			raise e
	'''
	set Network Latency Client side Time.
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
	get Total IC miss accounted in sampled timeframe.
	'''
	@property
	def ic_miss(self) :
		try:
			return self._ic_miss
		except Exception as e :
			raise e
	'''
	set Total IC miss accounted in sampled timeframe.
	'''
	@ic_miss.setter
	def ic_miss(self,ic_miss):
		try :
			if not isinstance(ic_miss,long):
				raise TypeError("ic_miss must be set to long value")
			self._ic_miss = ic_miss
		except Exception as e :
			raise e


	'''
	get Network Latency Client server Time.
	'''
	@property
	def network_latency_server_side(self) :
		try:
			return self._network_latency_server_side
		except Exception as e :
			raise e
	'''
	set Network Latency Client server Time.
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
	get Max value Network Latency Client side in given duration.
	'''
	@property
	def network_latency_client_side_max(self) :
		try:
			return self._network_latency_client_side_max
		except Exception as e :
			raise e
	'''
	set Max value Network Latency Client side in given duration.
	'''
	@network_latency_client_side_max.setter
	def network_latency_client_side_max(self,network_latency_client_side_max):
		try :
			if not isinstance(network_latency_client_side_max,long):
				raise TypeError("network_latency_client_side_max must be set to long value")
			self._network_latency_client_side_max = network_latency_client_side_max
		except Exception as e :
			raise e


	'''
	get Report Sample time.
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time.
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
	Report for Client Device, OS, Browser.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_app_client_device_os_browser_second_l2_obj=af_app_client_device_os_browser_second_l2()
				response = af_app_client_device_os_browser_second_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_app_client_device_os_browser_second_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_app_client_device_os_browser_second_l2_obj = af_app_client_device_os_browser_second_l2()
			option_ = options()
			option_._filter=filter_
			return af_app_client_device_os_browser_second_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_app_client_device_os_browser_second_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_app_client_device_os_browser_second_l2_obj = af_app_client_device_os_browser_second_l2()
			option_ = options()
			option_._count=True
			response = af_app_client_device_os_browser_second_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_app_client_device_os_browser_second_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_app_client_device_os_browser_second_l2_obj = af_app_client_device_os_browser_second_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_app_client_device_os_browser_second_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_app_client_device_os_browser_second_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_app_client_device_os_browser_second_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_app_client_device_os_browser_second_l2_responses, response, "af_app_client_device_os_browser_second_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_app_client_device_os_browser_second_l2_response_array
				i=0
				error = [af_app_client_device_os_browser_second_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_app_client_device_os_browser_second_l2_response_array
			i=0
			af_app_client_device_os_browser_second_l2_objs = [af_app_client_device_os_browser_second_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_app_client_device_os_browser_second_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_app_client_device_os_browser_second_l2_response,self.__class__.__name__,props)
					af_app_client_device_os_browser_second_l2_objs[i] = result.af_app_client_device_os_browser_second_l2
					i=i+1
			return af_app_client_device_os_browser_second_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_app_client_device_os_browser_second_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_app_client_device_os_browser_second_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_app_client_device_os_browser_second_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_app_client_device_os_browser_second_l2= [ af_app_client_device_os_browser_second_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_app_client_device_os_browser_second_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_app_client_device_os_browser_second_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_app_client_device_os_browser_second_l2_response_array = [ af_app_client_device_os_browser_second_l2() for _ in range(length)]
