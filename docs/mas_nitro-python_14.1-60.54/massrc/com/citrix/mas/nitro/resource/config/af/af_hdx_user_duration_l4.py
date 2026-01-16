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
Configuration for AF HDX User Duration Update table for Level 4 resource
'''

class af_hdx_user_duration_l4(base_resource):
	_is_desktop= ""
	_usage_duration= ""
	_rpt_sample_time= ""
	_exporter_id= ""
	_username= ""
	_active_duration= ""
	_desktop_name= ""
	_ip_address= ""
	_ctnsappname= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_hdx_user_duration_l4"
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
			return "af_hdx_user_duration_l4s"
		except Exception as e :
			raise e



	'''
	get Is Desktop.
	'''
	@property
	def is_desktop(self) :
		try:
			return self._is_desktop
		except Exception as e :
			raise e
	'''
	set Is Desktop.
	'''
	@is_desktop.setter
	def is_desktop(self,is_desktop):
		try :
			if not isinstance(is_desktop,long):
				raise TypeError("is_desktop must be set to long value")
			self._is_desktop = is_desktop
		except Exception as e :
			raise e


	'''
	get Usage Duration.
	'''
	@property
	def usage_duration(self) :
		try:
			return self._usage_duration
		except Exception as e :
			raise e
	'''
	set Usage Duration.
	'''
	@usage_duration.setter
	def usage_duration(self,usage_duration):
		try :
			if not isinstance(usage_duration,long):
				raise TypeError("usage_duration must be set to long value")
			self._usage_duration = usage_duration
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
	get Active Duration.
	'''
	@property
	def active_duration(self) :
		try:
			return self._active_duration
		except Exception as e :
			raise e
	'''
	set Active Duration.
	'''
	@active_duration.setter
	def active_duration(self,active_duration):
		try :
			if not isinstance(active_duration,long):
				raise TypeError("active_duration must be set to long value")
			self._active_duration = active_duration
		except Exception as e :
			raise e


	'''
	get Desktop name which this session belongs.
	'''
	@property
	def desktop_name(self) :
		try:
			return self._desktop_name
		except Exception as e :
			raise e
	'''
	set Desktop name which this session belongs.
	'''
	@desktop_name.setter
	def desktop_name(self,desktop_name):
		try :
			if not isinstance(desktop_name,str):
				raise TypeError("desktop_name must be set to str value")
			self._desktop_name = desktop_name
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
	Af HDX Report for ICA User Duration update collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_hdx_user_duration_l4_obj=af_hdx_user_duration_l4()
				response = af_hdx_user_duration_l4_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_hdx_user_duration_l4 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_hdx_user_duration_l4_obj = af_hdx_user_duration_l4()
			option_ = options()
			option_._filter=filter_
			return af_hdx_user_duration_l4_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_hdx_user_duration_l4 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_hdx_user_duration_l4_obj = af_hdx_user_duration_l4()
			option_ = options()
			option_._count=True
			response = af_hdx_user_duration_l4_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_hdx_user_duration_l4 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_hdx_user_duration_l4_obj = af_hdx_user_duration_l4()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_hdx_user_duration_l4_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_hdx_user_duration_l4_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_hdx_user_duration_l4
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_hdx_user_duration_l4_responses, response, "af_hdx_user_duration_l4_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_hdx_user_duration_l4_response_array
				i=0
				error = [af_hdx_user_duration_l4() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_hdx_user_duration_l4_response_array
			i=0
			af_hdx_user_duration_l4_objs = [af_hdx_user_duration_l4() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_hdx_user_duration_l4:
					result = service.payload_formatter.string_to_bulk_resource(af_hdx_user_duration_l4_response,self.__class__.__name__,props)
					af_hdx_user_duration_l4_objs[i] = result.af_hdx_user_duration_l4
					i=i+1
			return af_hdx_user_duration_l4_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_hdx_user_duration_l4,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_hdx_user_duration_l4_response(base_response):
	def __init__(self,length=1) :
		self.af_hdx_user_duration_l4= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_hdx_user_duration_l4= [ af_hdx_user_duration_l4() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_hdx_user_duration_l4_responses(base_response):
	def __init__(self,length=1) :
		self.af_hdx_user_duration_l4_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_hdx_user_duration_l4_response_array = [ af_hdx_user_duration_l4() for _ in range(length)]
