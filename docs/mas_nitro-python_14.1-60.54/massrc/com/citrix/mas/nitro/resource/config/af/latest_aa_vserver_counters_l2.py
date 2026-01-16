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
Configuration for temp table to store apps with latest rpt_sample_time resource
'''

class latest_aa_vserver_counters_l2(base_resource):
	_lat_ip_address= ""
	_lat_rpt_sample_time= ""
	_lat_ctnsappname= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "latest_aa_vserver_counters_l2"
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
			return "latest_aa_vserver_counters_l2s"
		except Exception as e :
			raise e



	'''
	get Latest  ip_address
	'''
	@property
	def lat_ip_address(self) :
		try:
			return self._lat_ip_address
		except Exception as e :
			raise e
	'''
	set Latest  ip_address
	'''
	@lat_ip_address.setter
	def lat_ip_address(self,lat_ip_address):
		try :
			if not isinstance(lat_ip_address,str):
				raise TypeError("lat_ip_address must be set to str value")
			self._lat_ip_address = lat_ip_address
		except Exception as e :
			raise e


	'''
	get Latest Report Sample time.
	'''
	@property
	def lat_rpt_sample_time(self) :
		try:
			return self._lat_rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Latest Report Sample time.
	'''
	@lat_rpt_sample_time.setter
	def lat_rpt_sample_time(self,lat_rpt_sample_time):
		try :
			if not isinstance(lat_rpt_sample_time,long):
				raise TypeError("lat_rpt_sample_time must be set to long value")
			self._lat_rpt_sample_time = lat_rpt_sample_time
		except Exception as e :
			raise e


	'''
	get Latest  Vserver Name
	'''
	@property
	def lat_ctnsappname(self) :
		try:
			return self._lat_ctnsappname
		except Exception as e :
			raise e
	'''
	set Latest  Vserver Name
	'''
	@lat_ctnsappname.setter
	def lat_ctnsappname(self,lat_ctnsappname):
		try :
			if not isinstance(lat_ctnsappname,str):
				raise TypeError("lat_ctnsappname must be set to str value")
			self._lat_ctnsappname = lat_ctnsappname
		except Exception as e :
			raise e

	'''
	Af Report for App information collected by this AF Collector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				latest_aa_vserver_counters_l2_obj=latest_aa_vserver_counters_l2()
				response = latest_aa_vserver_counters_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of latest_aa_vserver_counters_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			latest_aa_vserver_counters_l2_obj = latest_aa_vserver_counters_l2()
			option_ = options()
			option_._filter=filter_
			return latest_aa_vserver_counters_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the latest_aa_vserver_counters_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			latest_aa_vserver_counters_l2_obj = latest_aa_vserver_counters_l2()
			option_ = options()
			option_._count=True
			response = latest_aa_vserver_counters_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of latest_aa_vserver_counters_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			latest_aa_vserver_counters_l2_obj = latest_aa_vserver_counters_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = latest_aa_vserver_counters_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(latest_aa_vserver_counters_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.latest_aa_vserver_counters_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(latest_aa_vserver_counters_l2_responses, response, "latest_aa_vserver_counters_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.latest_aa_vserver_counters_l2_response_array
				i=0
				error = [latest_aa_vserver_counters_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.latest_aa_vserver_counters_l2_response_array
			i=0
			latest_aa_vserver_counters_l2_objs = [latest_aa_vserver_counters_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._latest_aa_vserver_counters_l2:
					result = service.payload_formatter.string_to_bulk_resource(latest_aa_vserver_counters_l2_response,self.__class__.__name__,props)
					latest_aa_vserver_counters_l2_objs[i] = result.latest_aa_vserver_counters_l2
					i=i+1
			return latest_aa_vserver_counters_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(latest_aa_vserver_counters_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class latest_aa_vserver_counters_l2_response(base_response):
	def __init__(self,length=1) :
		self.latest_aa_vserver_counters_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.latest_aa_vserver_counters_l2= [ latest_aa_vserver_counters_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class latest_aa_vserver_counters_l2_responses(base_response):
	def __init__(self,length=1) :
		self.latest_aa_vserver_counters_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.latest_aa_vserver_counters_l2_response_array = [ latest_aa_vserver_counters_l2() for _ in range(length)]
