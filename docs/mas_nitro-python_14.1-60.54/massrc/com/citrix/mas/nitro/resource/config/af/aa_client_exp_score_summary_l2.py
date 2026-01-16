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
Configuration for Client Experience score summary table for Level 2 resource
'''

class aa_client_exp_score_summary_l2(base_resource):
	_ssl_failures_affected_clients= ""
	_load_time_affected_clients= ""
	_rpt_sample_time= ""
	_client_type= ""
	_client_rtt_affected_clients= ""
	_client_failures_affected_clients= ""
	_ip_address= ""
	_total_clients= ""
	_ctnsappname= ""
	_render_time_affected_clients= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "aa_client_exp_score_summary_l2"
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
			return "aa_client_exp_score_summary_l2s"
		except Exception as e :
			raise e



	'''
	get Number of clients affected by ssl_failures issue.
	'''
	@property
	def ssl_failures_affected_clients(self) :
		try:
			return self._ssl_failures_affected_clients
		except Exception as e :
			raise e
	'''
	set Number of clients affected by ssl_failures issue.
	'''
	@ssl_failures_affected_clients.setter
	def ssl_failures_affected_clients(self,ssl_failures_affected_clients):
		try :
			if not isinstance(ssl_failures_affected_clients,int):
				raise TypeError("ssl_failures_affected_clients must be set to int value")
			self._ssl_failures_affected_clients = ssl_failures_affected_clients
		except Exception as e :
			raise e


	'''
	get Number of clients affected by load_time issue.
	'''
	@property
	def load_time_affected_clients(self) :
		try:
			return self._load_time_affected_clients
		except Exception as e :
			raise e
	'''
	set Number of clients affected by load_time issue.
	'''
	@load_time_affected_clients.setter
	def load_time_affected_clients(self,load_time_affected_clients):
		try :
			if not isinstance(load_time_affected_clients,int):
				raise TypeError("load_time_affected_clients must be set to int value")
			self._load_time_affected_clients = load_time_affected_clients
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
	get Type of clients - [ Good, Fair, Bad ] based on their experience score
	'''
	@property
	def client_type(self) :
		try:
			return self._client_type
		except Exception as e :
			raise e
	'''
	set Type of clients - [ Good, Fair, Bad ] based on their experience score
	'''
	@client_type.setter
	def client_type(self,client_type):
		try :
			if not isinstance(client_type,str):
				raise TypeError("client_type must be set to str value")
			self._client_type = client_type
		except Exception as e :
			raise e


	'''
	get Number of clients affected by client_rtt issue.
	'''
	@property
	def client_rtt_affected_clients(self) :
		try:
			return self._client_rtt_affected_clients
		except Exception as e :
			raise e
	'''
	set Number of clients affected by client_rtt issue.
	'''
	@client_rtt_affected_clients.setter
	def client_rtt_affected_clients(self,client_rtt_affected_clients):
		try :
			if not isinstance(client_rtt_affected_clients,int):
				raise TypeError("client_rtt_affected_clients must be set to int value")
			self._client_rtt_affected_clients = client_rtt_affected_clients
		except Exception as e :
			raise e


	'''
	get Number of clients affected by client_failures issue.
	'''
	@property
	def client_failures_affected_clients(self) :
		try:
			return self._client_failures_affected_clients
		except Exception as e :
			raise e
	'''
	set Number of clients affected by client_failures issue.
	'''
	@client_failures_affected_clients.setter
	def client_failures_affected_clients(self,client_failures_affected_clients):
		try :
			if not isinstance(client_failures_affected_clients,int):
				raise TypeError("client_failures_affected_clients must be set to int value")
			self._client_failures_affected_clients = client_failures_affected_clients
		except Exception as e :
			raise e


	'''
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
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
	get Total clients per type.
	'''
	@property
	def total_clients(self) :
		try:
			return self._total_clients
		except Exception as e :
			raise e
	'''
	set Total clients per type.
	'''
	@total_clients.setter
	def total_clients(self,total_clients):
		try :
			if not isinstance(total_clients,int):
				raise TypeError("total_clients must be set to int value")
			self._total_clients = total_clients
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
	get Number of clients affected by render_time issue.
	'''
	@property
	def render_time_affected_clients(self) :
		try:
			return self._render_time_affected_clients
		except Exception as e :
			raise e
	'''
	set Number of clients affected by render_time issue.
	'''
	@render_time_affected_clients.setter
	def render_time_affected_clients(self,render_time_affected_clients):
		try :
			if not isinstance(render_time_affected_clients,int):
				raise TypeError("render_time_affected_clients must be set to int value")
			self._render_time_affected_clients = render_time_affected_clients
		except Exception as e :
			raise e

	'''
	Af Report for Anomaly details for this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				aa_client_exp_score_summary_l2_obj=aa_client_exp_score_summary_l2()
				response = aa_client_exp_score_summary_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_client_exp_score_summary_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_client_exp_score_summary_l2_obj = aa_client_exp_score_summary_l2()
			option_ = options()
			option_._filter=filter_
			return aa_client_exp_score_summary_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_client_exp_score_summary_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_client_exp_score_summary_l2_obj = aa_client_exp_score_summary_l2()
			option_ = options()
			option_._count=True
			response = aa_client_exp_score_summary_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_client_exp_score_summary_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_client_exp_score_summary_l2_obj = aa_client_exp_score_summary_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_client_exp_score_summary_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_client_exp_score_summary_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_client_exp_score_summary_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_client_exp_score_summary_l2_responses, response, "aa_client_exp_score_summary_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_client_exp_score_summary_l2_response_array
				i=0
				error = [aa_client_exp_score_summary_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_client_exp_score_summary_l2_response_array
			i=0
			aa_client_exp_score_summary_l2_objs = [aa_client_exp_score_summary_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._aa_client_exp_score_summary_l2:
					result = service.payload_formatter.string_to_bulk_resource(aa_client_exp_score_summary_l2_response,self.__class__.__name__,props)
					aa_client_exp_score_summary_l2_objs[i] = result.aa_client_exp_score_summary_l2
					i=i+1
			return aa_client_exp_score_summary_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_client_exp_score_summary_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_client_exp_score_summary_l2_response(base_response):
	def __init__(self,length=1) :
		self.aa_client_exp_score_summary_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_client_exp_score_summary_l2= [ aa_client_exp_score_summary_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_client_exp_score_summary_l2_responses(base_response):
	def __init__(self,length=1) :
		self.aa_client_exp_score_summary_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_client_exp_score_summary_l2_response_array = [ aa_client_exp_score_summary_l2() for _ in range(length)]
