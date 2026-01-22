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
Configuration for AF VPN Session Report table for Level 3 resource
'''

class af_vpn_active_session_count_l3(base_resource):
	_rpt_sample_time= ""
	_appname= ""
	_ip_address= ""
	_country_name= ""
	_ctnsappname= ""
	_username= ""
	_city_name= ""
	_session_count= ""
	_region_name= ""
	_exporter_id= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_vpn_active_session_count_l3"
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
			return "af_vpn_active_session_count_l3s"
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
	get Application Name.
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set Application Name.
	'''
	@appname.setter
	def appname(self,appname):
		try :
			if not isinstance(appname,str):
				raise TypeError("appname must be set to str value")
			self._appname = appname
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
	get Country Name
	'''
	@property
	def country_name(self) :
		try:
			return self._country_name
		except Exception as e :
			raise e
	'''
	set Country Name
	'''
	@country_name.setter
	def country_name(self,country_name):
		try :
			if not isinstance(country_name,str):
				raise TypeError("country_name must be set to str value")
			self._country_name = country_name
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
	get User Name.
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set User Name.
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e


	'''
	get City Name
	'''
	@property
	def city_name(self) :
		try:
			return self._city_name
		except Exception as e :
			raise e
	'''
	set City Name
	'''
	@city_name.setter
	def city_name(self,city_name):
		try :
			if not isinstance(city_name,str):
				raise TypeError("city_name must be set to str value")
			self._city_name = city_name
		except Exception as e :
			raise e


	'''
	get Active Session count
	'''
	@property
	def session_count(self) :
		try:
			return self._session_count
		except Exception as e :
			raise e
	'''
	set Active Session count
	'''
	@session_count.setter
	def session_count(self,session_count):
		try :
			if not isinstance(session_count,long):
				raise TypeError("session_count must be set to long value")
			self._session_count = session_count
		except Exception as e :
			raise e


	'''
	get Region Name
	'''
	@property
	def region_name(self) :
		try:
			return self._region_name
		except Exception as e :
			raise e
	'''
	set Region Name
	'''
	@region_name.setter
	def region_name(self,region_name):
		try :
			if not isinstance(region_name,str):
				raise TypeError("region_name must be set to str value")
			self._region_name = region_name
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
	Af HDX Report for Session information collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_vpn_active_session_count_l3_obj=af_vpn_active_session_count_l3()
				response = af_vpn_active_session_count_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_vpn_active_session_count_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_vpn_active_session_count_l3_obj = af_vpn_active_session_count_l3()
			option_ = options()
			option_._filter=filter_
			return af_vpn_active_session_count_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_vpn_active_session_count_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_vpn_active_session_count_l3_obj = af_vpn_active_session_count_l3()
			option_ = options()
			option_._count=True
			response = af_vpn_active_session_count_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_vpn_active_session_count_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_vpn_active_session_count_l3_obj = af_vpn_active_session_count_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_vpn_active_session_count_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_vpn_active_session_count_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_vpn_active_session_count_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_vpn_active_session_count_l3_responses, response, "af_vpn_active_session_count_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_vpn_active_session_count_l3_response_array
				i=0
				error = [af_vpn_active_session_count_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_vpn_active_session_count_l3_response_array
			i=0
			af_vpn_active_session_count_l3_objs = [af_vpn_active_session_count_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_vpn_active_session_count_l3:
					result = service.payload_formatter.string_to_bulk_resource(af_vpn_active_session_count_l3_response,self.__class__.__name__,props)
					af_vpn_active_session_count_l3_objs[i] = result.af_vpn_active_session_count_l3
					i=i+1
			return af_vpn_active_session_count_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_vpn_active_session_count_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_vpn_active_session_count_l3_response(base_response):
	def __init__(self,length=1) :
		self.af_vpn_active_session_count_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_vpn_active_session_count_l3= [ af_vpn_active_session_count_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_vpn_active_session_count_l3_responses(base_response):
	def __init__(self,length=1) :
		self.af_vpn_active_session_count_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_vpn_active_session_count_l3_response_array = [ af_vpn_active_session_count_l3() for _ in range(length)]
