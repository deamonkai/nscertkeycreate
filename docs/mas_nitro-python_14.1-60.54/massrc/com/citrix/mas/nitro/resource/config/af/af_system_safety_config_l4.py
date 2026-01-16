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
Configuration for AF System Security data table for Level 4 resource
'''

class af_system_safety_config_l4(base_resource):
	_ip_address= ""
	_exporter_id= ""
	_compliant= ""
	_sub_group= ""
	_system_safety_index= ""
	_recommended_action= ""
	_rpt_sample_time= ""
	_not_compliant= ""
	_sys_group= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_system_safety_config_l4"
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
			return "af_system_safety_config_l4s"
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
	get compliant.
	'''
	@property
	def compliant(self) :
		try:
			return self._compliant
		except Exception as e :
			raise e
	'''
	set compliant.
	'''
	@compliant.setter
	def compliant(self,compliant):
		try :
			if not isinstance(compliant,long):
				raise TypeError("compliant must be set to long value")
			self._compliant = compliant
		except Exception as e :
			raise e


	'''
	get sub_group.
	'''
	@property
	def sub_group(self) :
		try:
			return self._sub_group
		except Exception as e :
			raise e
	'''
	set sub_group.
	'''
	@sub_group.setter
	def sub_group(self,sub_group):
		try :
			if not isinstance(sub_group,long):
				raise TypeError("sub_group must be set to long value")
			self._sub_group = sub_group
		except Exception as e :
			raise e


	'''
	get System Safety Index
	'''
	@property
	def system_safety_index(self) :
		try:
			return self._system_safety_index
		except Exception as e :
			raise e
	'''
	set System Safety Index
	'''
	@system_safety_index.setter
	def system_safety_index(self,system_safety_index):
		try :
			if not isinstance(system_safety_index,long):
				raise TypeError("system_safety_index must be set to long value")
			self._system_safety_index = system_safety_index
		except Exception as e :
			raise e


	'''
	get recommended_action.
	'''
	@property
	def recommended_action(self) :
		try:
			return self._recommended_action
		except Exception as e :
			raise e
	'''
	set recommended_action.
	'''
	@recommended_action.setter
	def recommended_action(self,recommended_action):
		try :
			if not isinstance(recommended_action,long):
				raise TypeError("recommended_action must be set to long value")
			self._recommended_action = recommended_action
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
	get not_compliant.
	'''
	@property
	def not_compliant(self) :
		try:
			return self._not_compliant
		except Exception as e :
			raise e
	'''
	set not_compliant.
	'''
	@not_compliant.setter
	def not_compliant(self,not_compliant):
		try :
			if not isinstance(not_compliant,long):
				raise TypeError("not_compliant must be set to long value")
			self._not_compliant = not_compliant
		except Exception as e :
			raise e


	'''
	get sys_group
	'''
	@property
	def sys_group(self) :
		try:
			return self._sys_group
		except Exception as e :
			raise e
	'''
	set sys_group
	'''
	@sys_group.setter
	def sys_group(self,sys_group):
		try :
			if not isinstance(sys_group,long):
				raise TypeError("sys_group must be set to long value")
			self._sys_group = sys_group
		except Exception as e :
			raise e

	'''
	Af Report for Saftey Index Data..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_system_safety_config_l4_obj=af_system_safety_config_l4()
				response = af_system_safety_config_l4_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_system_safety_config_l4 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_system_safety_config_l4_obj = af_system_safety_config_l4()
			option_ = options()
			option_._filter=filter_
			return af_system_safety_config_l4_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_system_safety_config_l4 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_system_safety_config_l4_obj = af_system_safety_config_l4()
			option_ = options()
			option_._count=True
			response = af_system_safety_config_l4_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_system_safety_config_l4 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_system_safety_config_l4_obj = af_system_safety_config_l4()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_system_safety_config_l4_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_system_safety_config_l4_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_system_safety_config_l4
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_system_safety_config_l4_responses, response, "af_system_safety_config_l4_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_system_safety_config_l4_response_array
				i=0
				error = [af_system_safety_config_l4() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_system_safety_config_l4_response_array
			i=0
			af_system_safety_config_l4_objs = [af_system_safety_config_l4() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_system_safety_config_l4:
					result = service.payload_formatter.string_to_bulk_resource(af_system_safety_config_l4_response,self.__class__.__name__,props)
					af_system_safety_config_l4_objs[i] = result.af_system_safety_config_l4
					i=i+1
			return af_system_safety_config_l4_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_system_safety_config_l4,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_system_safety_config_l4_response(base_response):
	def __init__(self,length=1) :
		self.af_system_safety_config_l4= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_system_safety_config_l4= [ af_system_safety_config_l4() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_system_safety_config_l4_responses(base_response):
	def __init__(self,length=1) :
		self.af_system_safety_config_l4_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_system_safety_config_l4_response_array = [ af_system_safety_config_l4() for _ in range(length)]
