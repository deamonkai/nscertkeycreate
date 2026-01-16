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
Configuration for SWG Transaction Report table for Level 1 resource
'''

class af_swg_domain_summary_l2(base_resource):
	_protocol= ""
	_user_agent= ""
	_exporter_id= ""
	_total_bytes_out= ""
	_operating_system= ""
	_domain_name= ""
	_ctnsappname= ""
	_total_ssl_intercepts= ""
	_port= ""
	_total_bytes_in= ""
	_url_group_category= ""
	_url_reputation= ""
	_rpt_sample_time= ""
	_total_requests= ""
	_ip_address= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_swg_domain_summary_l2"
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
			return "af_swg_domain_summary_l2s"
		except Exception as e :
			raise e



	'''
	get protocol used
	'''
	@property
	def protocol(self) :
		try:
			return self._protocol
		except Exception as e :
			raise e
	'''
	set protocol used
	'''
	@protocol.setter
	def protocol(self,protocol):
		try :
			if not isinstance(protocol,int):
				raise TypeError("protocol must be set to int value")
			self._protocol = protocol
		except Exception as e :
			raise e


	'''
	get User Agent Name.
	'''
	@property
	def user_agent(self) :
		try:
			return self._user_agent
		except Exception as e :
			raise e
	'''
	set User Agent Name.
	'''
	@user_agent.setter
	def user_agent(self,user_agent):
		try :
			if not isinstance(user_agent,int):
				raise TypeError("user_agent must be set to int value")
			self._user_agent = user_agent
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
	get Total bytes out
	'''
	@property
	def total_bytes_out(self) :
		try:
			return self._total_bytes_out
		except Exception as e :
			raise e
	'''
	set Total bytes out
	'''
	@total_bytes_out.setter
	def total_bytes_out(self,total_bytes_out):
		try :
			if not isinstance(total_bytes_out,long):
				raise TypeError("total_bytes_out must be set to long value")
			self._total_bytes_out = total_bytes_out
		except Exception as e :
			raise e


	'''
	get Client Operating System Name.
	'''
	@property
	def operating_system(self) :
		try:
			return self._operating_system
		except Exception as e :
			raise e
	'''
	set Client Operating System Name.
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
	get Domain Name
	'''
	@property
	def domain_name(self) :
		try:
			return self._domain_name
		except Exception as e :
			raise e
	'''
	set Domain Name
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
	get Total Intercepts
	'''
	@property
	def total_ssl_intercepts(self) :
		try:
			return self._total_ssl_intercepts
		except Exception as e :
			raise e
	'''
	set Total Intercepts
	'''
	@total_ssl_intercepts.setter
	def total_ssl_intercepts(self,total_ssl_intercepts):
		try :
			if not isinstance(total_ssl_intercepts,long):
				raise TypeError("total_ssl_intercepts must be set to long value")
			self._total_ssl_intercepts = total_ssl_intercepts
		except Exception as e :
			raise e


	'''
	get protocol used
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set protocol used
	'''
	@port.setter
	def port(self,port):
		try :
			if not isinstance(port,int):
				raise TypeError("port must be set to int value")
			self._port = port
		except Exception as e :
			raise e


	'''
	get Total bytes in
	'''
	@property
	def total_bytes_in(self) :
		try:
			return self._total_bytes_in
		except Exception as e :
			raise e
	'''
	set Total bytes in
	'''
	@total_bytes_in.setter
	def total_bytes_in(self,total_bytes_in):
		try :
			if not isinstance(total_bytes_in,long):
				raise TypeError("total_bytes_in must be set to long value")
			self._total_bytes_in = total_bytes_in
		except Exception as e :
			raise e


	'''
	get URL Group Category
	'''
	@property
	def url_group_category(self) :
		try:
			return self._url_group_category
		except Exception as e :
			raise e
	'''
	set URL Group Category
	'''
	@url_group_category.setter
	def url_group_category(self,url_group_category):
		try :
			if not isinstance(url_group_category,int):
				raise TypeError("url_group_category must be set to int value")
			self._url_group_category = url_group_category
		except Exception as e :
			raise e


	'''
	get URL reputation
	'''
	@property
	def url_reputation(self) :
		try:
			return self._url_reputation
		except Exception as e :
			raise e
	'''
	set URL reputation
	'''
	@url_reputation.setter
	def url_reputation(self,url_reputation):
		try :
			if not isinstance(url_reputation,int):
				raise TypeError("url_reputation must be set to int value")
			self._url_reputation = url_reputation
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
	get Total transactions
	'''
	@property
	def total_requests(self) :
		try:
			return self._total_requests
		except Exception as e :
			raise e
	'''
	set Total transactions
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
	Af Report for Top URL being Count Managed by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_swg_domain_summary_l2_obj=af_swg_domain_summary_l2()
				response = af_swg_domain_summary_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_swg_domain_summary_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_swg_domain_summary_l2_obj = af_swg_domain_summary_l2()
			option_ = options()
			option_._filter=filter_
			return af_swg_domain_summary_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_swg_domain_summary_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_swg_domain_summary_l2_obj = af_swg_domain_summary_l2()
			option_ = options()
			option_._count=True
			response = af_swg_domain_summary_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_swg_domain_summary_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_swg_domain_summary_l2_obj = af_swg_domain_summary_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_swg_domain_summary_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_swg_domain_summary_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_swg_domain_summary_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_swg_domain_summary_l2_responses, response, "af_swg_domain_summary_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_swg_domain_summary_l2_response_array
				i=0
				error = [af_swg_domain_summary_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_swg_domain_summary_l2_response_array
			i=0
			af_swg_domain_summary_l2_objs = [af_swg_domain_summary_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_swg_domain_summary_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_swg_domain_summary_l2_response,self.__class__.__name__,props)
					af_swg_domain_summary_l2_objs[i] = result.af_swg_domain_summary_l2
					i=i+1
			return af_swg_domain_summary_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_swg_domain_summary_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_swg_domain_summary_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_swg_domain_summary_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_swg_domain_summary_l2= [ af_swg_domain_summary_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_swg_domain_summary_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_swg_domain_summary_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_swg_domain_summary_l2_response_array = [ af_swg_domain_summary_l2() for _ in range(length)]
