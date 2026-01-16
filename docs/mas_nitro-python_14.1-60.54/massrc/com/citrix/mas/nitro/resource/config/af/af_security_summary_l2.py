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
Configuration for AF Safety summary table for Level 2 resource
'''

class af_security_summary_l2(base_resource):
	_block_flags= ""
	_app_safety_index= ""
	_rpt_sample_time= ""
	_high_safety= ""
	_low_threat= ""
	_ip_address= ""
	_high_threat= ""
	_low_safety= ""
	_appname= ""
	_medium_threat= ""
	_medium_safety= ""
	_total_attacks= ""
	_counter_value= ""
	_app_threat_index= ""
	_ctnsappname= ""
	_exporter_id= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_security_summary_l2"
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
			return "af_security_summary_l2s"
		except Exception as e :
			raise e



	'''
	get block_flags.
	'''
	@property
	def block_flags(self) :
		try:
			return self._block_flags
		except Exception as e :
			raise e
	'''
	set block_flags.
	'''
	@block_flags.setter
	def block_flags(self,block_flags):
		try :
			if not isinstance(block_flags,long):
				raise TypeError("block_flags must be set to long value")
			self._block_flags = block_flags
		except Exception as e :
			raise e


	'''
	get safety index.
	'''
	@property
	def app_safety_index(self) :
		try:
			return self._app_safety_index
		except Exception as e :
			raise e
	'''
	set safety index.
	'''
	@app_safety_index.setter
	def app_safety_index(self,app_safety_index):
		try :
			if not isinstance(app_safety_index,int):
				raise TypeError("app_safety_index must be set to int value")
			self._app_safety_index = app_safety_index
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
	get high_safety count.
	'''
	@property
	def high_safety(self) :
		try:
			return self._high_safety
		except Exception as e :
			raise e
	'''
	set high_safety count.
	'''
	@high_safety.setter
	def high_safety(self,high_safety):
		try :
			if not isinstance(high_safety,long):
				raise TypeError("high_safety must be set to long value")
			self._high_safety = high_safety
		except Exception as e :
			raise e


	'''
	get low_threat. count
	'''
	@property
	def low_threat(self) :
		try:
			return self._low_threat
		except Exception as e :
			raise e
	'''
	set low_threat. count
	'''
	@low_threat.setter
	def low_threat(self,low_threat):
		try :
			if not isinstance(low_threat,long):
				raise TypeError("low_threat must be set to long value")
			self._low_threat = low_threat
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
	get high_threats count.
	'''
	@property
	def high_threat(self) :
		try:
			return self._high_threat
		except Exception as e :
			raise e
	'''
	set high_threats count.
	'''
	@high_threat.setter
	def high_threat(self,high_threat):
		try :
			if not isinstance(high_threat,long):
				raise TypeError("high_threat must be set to long value")
			self._high_threat = high_threat
		except Exception as e :
			raise e


	'''
	get low_safety count.
	'''
	@property
	def low_safety(self) :
		try:
			return self._low_safety
		except Exception as e :
			raise e
	'''
	set low_safety count.
	'''
	@low_safety.setter
	def low_safety(self,low_safety):
		try :
			if not isinstance(low_safety,long):
				raise TypeError("low_safety must be set to long value")
			self._low_safety = low_safety
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set AppName
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
	get medium_threat count.
	'''
	@property
	def medium_threat(self) :
		try:
			return self._medium_threat
		except Exception as e :
			raise e
	'''
	set medium_threat count.
	'''
	@medium_threat.setter
	def medium_threat(self,medium_threat):
		try :
			if not isinstance(medium_threat,long):
				raise TypeError("medium_threat must be set to long value")
			self._medium_threat = medium_threat
		except Exception as e :
			raise e


	'''
	get medium_safety count.
	'''
	@property
	def medium_safety(self) :
		try:
			return self._medium_safety
		except Exception as e :
			raise e
	'''
	set medium_safety count.
	'''
	@medium_safety.setter
	def medium_safety(self,medium_safety):
		try :
			if not isinstance(medium_safety,long):
				raise TypeError("medium_safety must be set to long value")
			self._medium_safety = medium_safety
		except Exception as e :
			raise e


	'''
	get Atttacks .
	'''
	@property
	def total_attacks(self) :
		try:
			return self._total_attacks
		except Exception as e :
			raise e
	'''
	set Atttacks .
	'''
	@total_attacks.setter
	def total_attacks(self,total_attacks):
		try :
			if not isinstance(total_attacks,long):
				raise TypeError("total_attacks must be set to long value")
			self._total_attacks = total_attacks
		except Exception as e :
			raise e


	'''
	get TCP counter values .
	'''
	@property
	def counter_value(self) :
		try:
			return self._counter_value
		except Exception as e :
			raise e
	'''
	set TCP counter values .
	'''
	@counter_value.setter
	def counter_value(self,counter_value):
		try :
			if not isinstance(counter_value,long):
				raise TypeError("counter_value must be set to long value")
			self._counter_value = counter_value
		except Exception as e :
			raise e


	'''
	get threat index.
	'''
	@property
	def app_threat_index(self) :
		try:
			return self._app_threat_index
		except Exception as e :
			raise e
	'''
	set threat index.
	'''
	@app_threat_index.setter
	def app_threat_index(self,app_threat_index):
		try :
			if not isinstance(app_threat_index,int):
				raise TypeError("app_threat_index must be set to int value")
			self._app_threat_index = app_threat_index
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
	Af Report for Secuirty Summary..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_security_summary_l2_obj=af_security_summary_l2()
				response = af_security_summary_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_security_summary_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_security_summary_l2_obj = af_security_summary_l2()
			option_ = options()
			option_._filter=filter_
			return af_security_summary_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_security_summary_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_security_summary_l2_obj = af_security_summary_l2()
			option_ = options()
			option_._count=True
			response = af_security_summary_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_security_summary_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_security_summary_l2_obj = af_security_summary_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_security_summary_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_security_summary_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_security_summary_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_security_summary_l2_responses, response, "af_security_summary_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_security_summary_l2_response_array
				i=0
				error = [af_security_summary_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_security_summary_l2_response_array
			i=0
			af_security_summary_l2_objs = [af_security_summary_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_security_summary_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_security_summary_l2_response,self.__class__.__name__,props)
					af_security_summary_l2_objs[i] = result.af_security_summary_l2
					i=i+1
			return af_security_summary_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_security_summary_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_security_summary_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_security_summary_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_security_summary_l2= [ af_security_summary_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_security_summary_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_security_summary_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_security_summary_l2_response_array = [ af_security_summary_l2() for _ in range(length)]
