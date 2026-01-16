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
Configuration for AF Saftey exporter  data table for Level 2 resource
'''

class af_profile_safety_data_l2(base_resource):
	_profile_block_count= ""
	_exporter_id= ""
	_profile_sig_name= ""
	_profile_check_safety_index= ""
	_profile_sig_enable_count= ""
	_sig_safety_index= ""
	_ctnsappname= ""
	_profile_sig_disable_count= ""
	_sig_block_count= ""
	_profile_none_count= ""
	_profile_not_block_count= ""
	_appname= ""
	_profile_type= ""
	_is_sig_auto_update= ""
	_iprep_safety_index= ""
	_ip_address= ""
	_sig_log_count= ""
	_profile_safety_index= ""
	_app_safety_index= ""
	_rpt_sample_time= ""
	_profile_name= ""
	_sig_stat_count= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_profile_safety_data_l2"
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
			return "af_profile_safety_data_l2s"
		except Exception as e :
			raise e



	'''
	get block_count.
	'''
	@property
	def profile_block_count(self) :
		try:
			return self._profile_block_count
		except Exception as e :
			raise e
	'''
	set block_count.
	'''
	@profile_block_count.setter
	def profile_block_count(self,profile_block_count):
		try :
			if not isinstance(profile_block_count,long):
				raise TypeError("profile_block_count must be set to long value")
			self._profile_block_count = profile_block_count
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
	get profile_sig_name
	'''
	@property
	def profile_sig_name(self) :
		try:
			return self._profile_sig_name
		except Exception as e :
			raise e
	'''
	set profile_sig_name
	'''
	@profile_sig_name.setter
	def profile_sig_name(self,profile_sig_name):
		try :
			if not isinstance(profile_sig_name,str):
				raise TypeError("profile_sig_name must be set to str value")
			self._profile_sig_name = profile_sig_name
		except Exception as e :
			raise e


	'''
	get profile check safety index.
	'''
	@property
	def profile_check_safety_index(self) :
		try:
			return self._profile_check_safety_index
		except Exception as e :
			raise e
	'''
	set profile check safety index.
	'''
	@profile_check_safety_index.setter
	def profile_check_safety_index(self,profile_check_safety_index):
		try :
			if not isinstance(profile_check_safety_index,int):
				raise TypeError("profile_check_safety_index must be set to int value")
			self._profile_check_safety_index = profile_check_safety_index
		except Exception as e :
			raise e


	'''
	get sig_enable_count
	'''
	@property
	def profile_sig_enable_count(self) :
		try:
			return self._profile_sig_enable_count
		except Exception as e :
			raise e
	'''
	set sig_enable_count
	'''
	@profile_sig_enable_count.setter
	def profile_sig_enable_count(self,profile_sig_enable_count):
		try :
			if not isinstance(profile_sig_enable_count,long):
				raise TypeError("profile_sig_enable_count must be set to long value")
			self._profile_sig_enable_count = profile_sig_enable_count
		except Exception as e :
			raise e


	'''
	get signature safety index.
	'''
	@property
	def sig_safety_index(self) :
		try:
			return self._sig_safety_index
		except Exception as e :
			raise e
	'''
	set signature safety index.
	'''
	@sig_safety_index.setter
	def sig_safety_index(self,sig_safety_index):
		try :
			if not isinstance(sig_safety_index,int):
				raise TypeError("sig_safety_index must be set to int value")
			self._sig_safety_index = sig_safety_index
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
	get profile_sig_disable_count
	'''
	@property
	def profile_sig_disable_count(self) :
		try:
			return self._profile_sig_disable_count
		except Exception as e :
			raise e
	'''
	set profile_sig_disable_count
	'''
	@profile_sig_disable_count.setter
	def profile_sig_disable_count(self,profile_sig_disable_count):
		try :
			if not isinstance(profile_sig_disable_count,long):
				raise TypeError("profile_sig_disable_count must be set to long value")
			self._profile_sig_disable_count = profile_sig_disable_count
		except Exception as e :
			raise e


	'''
	get sig_block_count
	'''
	@property
	def sig_block_count(self) :
		try:
			return self._sig_block_count
		except Exception as e :
			raise e
	'''
	set sig_block_count
	'''
	@sig_block_count.setter
	def sig_block_count(self,sig_block_count):
		try :
			if not isinstance(sig_block_count,long):
				raise TypeError("sig_block_count must be set to long value")
			self._sig_block_count = sig_block_count
		except Exception as e :
			raise e


	'''
	get none_count.
	'''
	@property
	def profile_none_count(self) :
		try:
			return self._profile_none_count
		except Exception as e :
			raise e
	'''
	set none_count.
	'''
	@profile_none_count.setter
	def profile_none_count(self,profile_none_count):
		try :
			if not isinstance(profile_none_count,long):
				raise TypeError("profile_none_count must be set to long value")
			self._profile_none_count = profile_none_count
		except Exception as e :
			raise e


	'''
	get not_block_count.
	'''
	@property
	def profile_not_block_count(self) :
		try:
			return self._profile_not_block_count
		except Exception as e :
			raise e
	'''
	set not_block_count.
	'''
	@profile_not_block_count.setter
	def profile_not_block_count(self,profile_not_block_count):
		try :
			if not isinstance(profile_not_block_count,long):
				raise TypeError("profile_not_block_count must be set to long value")
			self._profile_not_block_count = profile_not_block_count
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
	get Profile Typex.
	'''
	@property
	def profile_type(self) :
		try:
			return self._profile_type
		except Exception as e :
			raise e
	'''
	set Profile Typex.
	'''
	@profile_type.setter
	def profile_type(self,profile_type):
		try :
			if not isinstance(profile_type,int):
				raise TypeError("profile_type must be set to int value")
			self._profile_type = profile_type
		except Exception as e :
			raise e


	'''
	get auto update signature or not
	'''
	@property
	def is_sig_auto_update(self) :
		try:
			return self._is_sig_auto_update
		except Exception as e :
			raise e
	'''
	set auto update signature or not
	'''
	@is_sig_auto_update.setter
	def is_sig_auto_update(self,is_sig_auto_update):
		try :
			if not isinstance(is_sig_auto_update,int):
				raise TypeError("is_sig_auto_update must be set to int value")
			self._is_sig_auto_update = is_sig_auto_update
		except Exception as e :
			raise e


	'''
	get IP Reputation safety index.
	'''
	@property
	def iprep_safety_index(self) :
		try:
			return self._iprep_safety_index
		except Exception as e :
			raise e
	'''
	set IP Reputation safety index.
	'''
	@iprep_safety_index.setter
	def iprep_safety_index(self,iprep_safety_index):
		try :
			if not isinstance(iprep_safety_index,int):
				raise TypeError("iprep_safety_index must be set to int value")
			self._iprep_safety_index = iprep_safety_index
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
	get sig_log_count
	'''
	@property
	def sig_log_count(self) :
		try:
			return self._sig_log_count
		except Exception as e :
			raise e
	'''
	set sig_log_count
	'''
	@sig_log_count.setter
	def sig_log_count(self,sig_log_count):
		try :
			if not isinstance(sig_log_count,long):
				raise TypeError("sig_log_count must be set to long value")
			self._sig_log_count = sig_log_count
		except Exception as e :
			raise e


	'''
	get profile safety index.
	'''
	@property
	def profile_safety_index(self) :
		try:
			return self._profile_safety_index
		except Exception as e :
			raise e
	'''
	set profile safety index.
	'''
	@profile_safety_index.setter
	def profile_safety_index(self,profile_safety_index):
		try :
			if not isinstance(profile_safety_index,int):
				raise TypeError("profile_safety_index must be set to int value")
			self._profile_safety_index = profile_safety_index
		except Exception as e :
			raise e


	'''
	get Safety index.
	'''
	@property
	def app_safety_index(self) :
		try:
			return self._app_safety_index
		except Exception as e :
			raise e
	'''
	set Safety index.
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
	get profile_name
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set profile_name
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e


	'''
	get sig_stat_count
	'''
	@property
	def sig_stat_count(self) :
		try:
			return self._sig_stat_count
		except Exception as e :
			raise e
	'''
	set sig_stat_count
	'''
	@sig_stat_count.setter
	def sig_stat_count(self,sig_stat_count):
		try :
			if not isinstance(sig_stat_count,long):
				raise TypeError("sig_stat_count must be set to long value")
			self._sig_stat_count = sig_stat_count
		except Exception as e :
			raise e

	'''
	Af Report for Profile Saftey Index Data..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_profile_safety_data_l2_obj=af_profile_safety_data_l2()
				response = af_profile_safety_data_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_profile_safety_data_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_profile_safety_data_l2_obj = af_profile_safety_data_l2()
			option_ = options()
			option_._filter=filter_
			return af_profile_safety_data_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_profile_safety_data_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_profile_safety_data_l2_obj = af_profile_safety_data_l2()
			option_ = options()
			option_._count=True
			response = af_profile_safety_data_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_profile_safety_data_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_profile_safety_data_l2_obj = af_profile_safety_data_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_profile_safety_data_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_profile_safety_data_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_profile_safety_data_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_profile_safety_data_l2_responses, response, "af_profile_safety_data_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_profile_safety_data_l2_response_array
				i=0
				error = [af_profile_safety_data_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_profile_safety_data_l2_response_array
			i=0
			af_profile_safety_data_l2_objs = [af_profile_safety_data_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_profile_safety_data_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_profile_safety_data_l2_response,self.__class__.__name__,props)
					af_profile_safety_data_l2_objs[i] = result.af_profile_safety_data_l2
					i=i+1
			return af_profile_safety_data_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_profile_safety_data_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_profile_safety_data_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_profile_safety_data_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_profile_safety_data_l2= [ af_profile_safety_data_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_profile_safety_data_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_profile_safety_data_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_profile_safety_data_l2_response_array = [ af_profile_safety_data_l2() for _ in range(length)]
