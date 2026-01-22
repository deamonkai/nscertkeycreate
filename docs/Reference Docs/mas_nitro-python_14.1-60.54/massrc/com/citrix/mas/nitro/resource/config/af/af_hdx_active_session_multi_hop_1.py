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
Configuration for AF HDX Session Multi Hop Info Report table for Level 1 resource
'''

class af_hdx_active_session_multi_hop_1(base_resource):
	_hop_location= ""
	_ip_address= ""
	_hop_count= ""
	_edt= ""
	_rpt_sample_time= ""
	_ctnsappname= ""
	_agent_ip_address= ""
	_client_rtt= ""
	_exporter_id= ""
	_session_id= ""
	_server_rtt= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_hdx_active_session_multi_hop_1"
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
			return "af_hdx_active_session_multi_hop_1s"
		except Exception as e :
			raise e



	'''
	get ica session hop count.
	'''
	@property
	def hop_location(self) :
		try:
			return self._hop_location
		except Exception as e :
			raise e
	'''
	set ica session hop count.
	'''
	@hop_location.setter
	def hop_location(self,hop_location):
		try :
			if not isinstance(hop_location,float):
				raise TypeError("hop_location must be set to float value")
			self._hop_location = hop_location
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
	get Session hop count.
	'''
	@property
	def hop_count(self) :
		try:
			return self._hop_count
		except Exception as e :
			raise e
	'''
	set Session hop count.
	'''
	@hop_count.setter
	def hop_count(self,hop_count):
		try :
			if not isinstance(hop_count,float):
				raise TypeError("hop_count must be set to float value")
			self._hop_count = hop_count
		except Exception as e :
			raise e


	'''
	get Transport Type
	'''
	@property
	def edt(self) :
		try:
			return self._edt
		except Exception as e :
			raise e
	'''
	set Transport Type
	'''
	@edt.setter
	def edt(self,edt):
		try :
			if not isinstance(edt,int):
				raise TypeError("edt must be set to int value")
			self._edt = edt
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
	get Agent IP Address
	'''
	@property
	def agent_ip_address(self) :
		try:
			return self._agent_ip_address
		except Exception as e :
			raise e
	'''
	set Agent IP Address
	'''
	@agent_ip_address.setter
	def agent_ip_address(self,agent_ip_address):
		try :
			if not isinstance(agent_ip_address,str):
				raise TypeError("agent_ip_address must be set to str value")
			self._agent_ip_address = agent_ip_address
		except Exception as e :
			raise e


	'''
	get client RTT.
	'''
	@property
	def client_rtt(self) :
		try:
			return self._client_rtt
		except Exception as e :
			raise e
	'''
	set client RTT.
	'''
	@client_rtt.setter
	def client_rtt(self,client_rtt):
		try :
			if not isinstance(client_rtt,float):
				raise TypeError("client_rtt must be set to float value")
			self._client_rtt = client_rtt
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
			if not isinstance(exporter_id,float):
				raise TypeError("exporter_id must be set to float value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e


	'''
	get Session GUID.
	'''
	@property
	def session_id(self) :
		try:
			return self._session_id
		except Exception as e :
			raise e
	'''
	set Session GUID.
	'''
	@session_id.setter
	def session_id(self,session_id):
		try :
			if not isinstance(session_id,str):
				raise TypeError("session_id must be set to str value")
			self._session_id = session_id
		except Exception as e :
			raise e


	'''
	get Server RTT.
	'''
	@property
	def server_rtt(self) :
		try:
			return self._server_rtt
		except Exception as e :
			raise e
	'''
	set Server RTT.
	'''
	@server_rtt.setter
	def server_rtt(self,server_rtt):
		try :
			if not isinstance(server_rtt,float):
				raise TypeError("server_rtt must be set to float value")
			self._server_rtt = server_rtt
		except Exception as e :
			raise e

	'''
	Af HDX Multi Hop Report for Session information collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_hdx_active_session_multi_hop_1_obj=af_hdx_active_session_multi_hop_1()
				response = af_hdx_active_session_multi_hop_1_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_hdx_active_session_multi_hop_1 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_hdx_active_session_multi_hop_1_obj = af_hdx_active_session_multi_hop_1()
			option_ = options()
			option_._filter=filter_
			return af_hdx_active_session_multi_hop_1_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_hdx_active_session_multi_hop_1 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_hdx_active_session_multi_hop_1_obj = af_hdx_active_session_multi_hop_1()
			option_ = options()
			option_._count=True
			response = af_hdx_active_session_multi_hop_1_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_hdx_active_session_multi_hop_1 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_hdx_active_session_multi_hop_1_obj = af_hdx_active_session_multi_hop_1()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_hdx_active_session_multi_hop_1_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_hdx_active_session_multi_hop_1_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_hdx_active_session_multi_hop_1
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_hdx_active_session_multi_hop_1_responses, response, "af_hdx_active_session_multi_hop_1_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_hdx_active_session_multi_hop_1_response_array
				i=0
				error = [af_hdx_active_session_multi_hop_1() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_hdx_active_session_multi_hop_1_response_array
			i=0
			af_hdx_active_session_multi_hop_1_objs = [af_hdx_active_session_multi_hop_1() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_hdx_active_session_multi_hop_1:
					result = service.payload_formatter.string_to_bulk_resource(af_hdx_active_session_multi_hop_1_response,self.__class__.__name__,props)
					af_hdx_active_session_multi_hop_1_objs[i] = result.af_hdx_active_session_multi_hop_1
					i=i+1
			return af_hdx_active_session_multi_hop_1_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_hdx_active_session_multi_hop_1,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_hdx_active_session_multi_hop_1_response(base_response):
	def __init__(self,length=1) :
		self.af_hdx_active_session_multi_hop_1= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_hdx_active_session_multi_hop_1= [ af_hdx_active_session_multi_hop_1() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_hdx_active_session_multi_hop_1_responses(base_response):
	def __init__(self,length=1) :
		self.af_hdx_active_session_multi_hop_1_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_hdx_active_session_multi_hop_1_response_array = [ af_hdx_active_session_multi_hop_1() for _ in range(length)]
