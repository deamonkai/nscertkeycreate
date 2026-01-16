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
Configuration for Temporary table for AA Web Anomaly IQR limits resource
'''

class aa_web_anomaly_limits_l2(base_resource):
	_iqr_ctnsappname= ""
	_spt_lower_lim= ""
	_spt_upper_lim= ""
	_iqr_ip_address= ""
	_iqr_application_name= ""
	_apt_lower_lim= ""
	_cnl_upper_lim= ""
	_apt_upper_lim= ""
	_cnl_lower_lim= ""
	_snl_lower_lim= ""
	_snl_upper_lim= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "aa_web_anomaly_limits_l2"
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
			return "aa_web_anomaly_limits_l2s"
		except Exception as e :
			raise e



	'''
	get AppName
	'''
	@property
	def iqr_ctnsappname(self) :
		try:
			return self._iqr_ctnsappname
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@iqr_ctnsappname.setter
	def iqr_ctnsappname(self,iqr_ctnsappname):
		try :
			if not isinstance(iqr_ctnsappname,str):
				raise TypeError("iqr_ctnsappname must be set to str value")
			self._iqr_ctnsappname = iqr_ctnsappname
		except Exception as e :
			raise e


	'''
	get Server Processing Time Lower Limit
	'''
	@property
	def spt_lower_lim(self) :
		try:
			return self._spt_lower_lim
		except Exception as e :
			raise e
	'''
	set Server Processing Time Lower Limit
	'''
	@spt_lower_lim.setter
	def spt_lower_lim(self,spt_lower_lim):
		try :
			if not isinstance(spt_lower_lim,float):
				raise TypeError("spt_lower_lim must be set to float value")
			self._spt_lower_lim = spt_lower_lim
		except Exception as e :
			raise e


	'''
	get Server Processing Time Upper Limit
	'''
	@property
	def spt_upper_lim(self) :
		try:
			return self._spt_upper_lim
		except Exception as e :
			raise e
	'''
	set Server Processing Time Upper Limit
	'''
	@spt_upper_lim.setter
	def spt_upper_lim(self,spt_upper_lim):
		try :
			if not isinstance(spt_upper_lim,float):
				raise TypeError("spt_upper_lim must be set to float value")
			self._spt_upper_lim = spt_upper_lim
		except Exception as e :
			raise e


	'''
	get IP Address
	'''
	@property
	def iqr_ip_address(self) :
		try:
			return self._iqr_ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
	'''
	@iqr_ip_address.setter
	def iqr_ip_address(self,iqr_ip_address):
		try :
			if not isinstance(iqr_ip_address,str):
				raise TypeError("iqr_ip_address must be set to str value")
			self._iqr_ip_address = iqr_ip_address
		except Exception as e :
			raise e


	'''
	get Application Name
	'''
	@property
	def iqr_application_name(self) :
		try:
			return self._iqr_application_name
		except Exception as e :
			raise e
	'''
	set Application Name
	'''
	@iqr_application_name.setter
	def iqr_application_name(self,iqr_application_name):
		try :
			if not isinstance(iqr_application_name,str):
				raise TypeError("iqr_application_name must be set to str value")
			self._iqr_application_name = iqr_application_name
		except Exception as e :
			raise e


	'''
	get App Processing Time Lower Limit
	'''
	@property
	def apt_lower_lim(self) :
		try:
			return self._apt_lower_lim
		except Exception as e :
			raise e
	'''
	set App Processing Time Lower Limit
	'''
	@apt_lower_lim.setter
	def apt_lower_lim(self,apt_lower_lim):
		try :
			if not isinstance(apt_lower_lim,float):
				raise TypeError("apt_lower_lim must be set to float value")
			self._apt_lower_lim = apt_lower_lim
		except Exception as e :
			raise e


	'''
	get Client Network Latency Time Upper Limit
	'''
	@property
	def cnl_upper_lim(self) :
		try:
			return self._cnl_upper_lim
		except Exception as e :
			raise e
	'''
	set Client Network Latency Time Upper Limit
	'''
	@cnl_upper_lim.setter
	def cnl_upper_lim(self,cnl_upper_lim):
		try :
			if not isinstance(cnl_upper_lim,float):
				raise TypeError("cnl_upper_lim must be set to float value")
			self._cnl_upper_lim = cnl_upper_lim
		except Exception as e :
			raise e


	'''
	get App Processing Time Upper Limit
	'''
	@property
	def apt_upper_lim(self) :
		try:
			return self._apt_upper_lim
		except Exception as e :
			raise e
	'''
	set App Processing Time Upper Limit
	'''
	@apt_upper_lim.setter
	def apt_upper_lim(self,apt_upper_lim):
		try :
			if not isinstance(apt_upper_lim,float):
				raise TypeError("apt_upper_lim must be set to float value")
			self._apt_upper_lim = apt_upper_lim
		except Exception as e :
			raise e


	'''
	get Client Network Latency Time Lower Limit
	'''
	@property
	def cnl_lower_lim(self) :
		try:
			return self._cnl_lower_lim
		except Exception as e :
			raise e
	'''
	set Client Network Latency Time Lower Limit
	'''
	@cnl_lower_lim.setter
	def cnl_lower_lim(self,cnl_lower_lim):
		try :
			if not isinstance(cnl_lower_lim,float):
				raise TypeError("cnl_lower_lim must be set to float value")
			self._cnl_lower_lim = cnl_lower_lim
		except Exception as e :
			raise e


	'''
	get Server Network Latency Time Lower Limit
	'''
	@property
	def snl_lower_lim(self) :
		try:
			return self._snl_lower_lim
		except Exception as e :
			raise e
	'''
	set Server Network Latency Time Lower Limit
	'''
	@snl_lower_lim.setter
	def snl_lower_lim(self,snl_lower_lim):
		try :
			if not isinstance(snl_lower_lim,float):
				raise TypeError("snl_lower_lim must be set to float value")
			self._snl_lower_lim = snl_lower_lim
		except Exception as e :
			raise e


	'''
	get Server Network Latency Time Upper Limit
	'''
	@property
	def snl_upper_lim(self) :
		try:
			return self._snl_upper_lim
		except Exception as e :
			raise e
	'''
	set Server Network Latency Time Upper Limit
	'''
	@snl_upper_lim.setter
	def snl_upper_lim(self,snl_upper_lim):
		try :
			if not isinstance(snl_upper_lim,float):
				raise TypeError("snl_upper_lim must be set to float value")
			self._snl_upper_lim = snl_upper_lim
		except Exception as e :
			raise e

	'''
	Af Web Anomaly IQR limits for Web Insight Data.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				aa_web_anomaly_limits_l2_obj=aa_web_anomaly_limits_l2()
				response = aa_web_anomaly_limits_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aa_web_anomaly_limits_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aa_web_anomaly_limits_l2_obj = aa_web_anomaly_limits_l2()
			option_ = options()
			option_._filter=filter_
			return aa_web_anomaly_limits_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aa_web_anomaly_limits_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aa_web_anomaly_limits_l2_obj = aa_web_anomaly_limits_l2()
			option_ = options()
			option_._count=True
			response = aa_web_anomaly_limits_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aa_web_anomaly_limits_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aa_web_anomaly_limits_l2_obj = aa_web_anomaly_limits_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aa_web_anomaly_limits_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aa_web_anomaly_limits_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_web_anomaly_limits_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_web_anomaly_limits_l2_responses, response, "aa_web_anomaly_limits_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_web_anomaly_limits_l2_response_array
				i=0
				error = [aa_web_anomaly_limits_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_web_anomaly_limits_l2_response_array
			i=0
			aa_web_anomaly_limits_l2_objs = [aa_web_anomaly_limits_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._aa_web_anomaly_limits_l2:
					result = service.payload_formatter.string_to_bulk_resource(aa_web_anomaly_limits_l2_response,self.__class__.__name__,props)
					aa_web_anomaly_limits_l2_objs[i] = result.aa_web_anomaly_limits_l2
					i=i+1
			return aa_web_anomaly_limits_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_web_anomaly_limits_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_web_anomaly_limits_l2_response(base_response):
	def __init__(self,length=1) :
		self.aa_web_anomaly_limits_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_web_anomaly_limits_l2= [ aa_web_anomaly_limits_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_web_anomaly_limits_l2_responses(base_response):
	def __init__(self,length=1) :
		self.aa_web_anomaly_limits_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_web_anomaly_limits_l2_response_array = [ aa_web_anomaly_limits_l2() for _ in range(length)]
