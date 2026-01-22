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
Configuration for Session Hop Distribution Report resource
'''

class session_hop_distribution(base_resource):
	_latency= ""
	___count= ""
	_rpt_sample_time= ""
	_exporter_id= ""
	_source_type= ""
	_id= ""
	_hop_count= ""
	_source= ""
	_target_type= ""
	_target= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "session_hop_distribution"
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
			return "session_hop_distributions"
		except Exception as e :
			raise e


	'''
	ica session client latency.
	'''
	@property
	def latency(self):
		try:
			return self._latency
		except Exception as e :
			raise e
	'''
	ica session client latency.
	'''
	@latency.setter
	def latency(self,latency):
		try :
			if not isinstance(latency,float):
				raise TypeError("latency must be set to float value")
			self._latency = latency
		except Exception as e :
			raise e

	'''
	count.
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	count.
	'''
	@__count.setter
	def __count(self,__count):
		try :
			if not isinstance(__count,float):
				raise TypeError("__count must be set to float value")
			self.___count = __count
		except Exception as e :
			raise e

	'''
	ReportSampletime.
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	ReportSampletime.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,float):
				raise TypeError("rpt_sample_time must be set to float value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e

	'''
	Exported ID.
	'''
	@property
	def exporter_id(self):
		try:
			return self._exporter_id
		except Exception as e :
			raise e
	'''
	Exported ID.
	'''
	@exporter_id.setter
	def exporter_id(self,exporter_id):
		try :
			if not isinstance(exporter_id,str):
				raise TypeError("exporter_id must be set to str value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e

	'''
	Type of the source, this will decide the icon to show in the UI for source [Client, NetScaler, Server, etc.] 
	'''
	@property
	def source_type(self):
		try:
			return self._source_type
		except Exception as e :
			raise e
	'''
	Type of the source, this will decide the icon to show in the UI for source [Client, NetScaler, Server, etc.] 
	'''
	@source_type.setter
	def source_type(self,source_type):
		try :
			if not isinstance(source_type,str):
				raise TypeError("source_type must be set to str value")
			self._source_type = source_type
		except Exception as e :
			raise e

	'''
	Id is ICA Session ID
	'''
	@property
	def id(self):
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	Id is ICA Session ID
	'''
	@id.setter
	def id(self,id):
		try :
			if not isinstance(id,str):
				raise TypeError("id must be set to str value")
			self._id = id
		except Exception as e :
			raise e

	'''
	Index of the hop [1, 2, 3, etc.] 
	'''
	@property
	def hop_count(self):
		try:
			return self._hop_count
		except Exception as e :
			raise e
	'''
	Index of the hop [1, 2, 3, etc.] 
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
	Text to display for the source [e.g.: User name, NetScaler IP, Server IP, etc.]
	'''
	@property
	def source(self):
		try:
			return self._source
		except Exception as e :
			raise e
	'''
	Text to display for the source [e.g.: User name, NetScaler IP, Server IP, etc.]
	'''
	@source.setter
	def source(self,source):
		try :
			if not isinstance(source,str):
				raise TypeError("source must be set to str value")
			self._source = source
		except Exception as e :
			raise e

	'''
	Type of the source, this will decide the icon to show in the UI for source [Client, NetScaler, Server, etc.]
	'''
	@property
	def target_type(self):
		try:
			return self._target_type
		except Exception as e :
			raise e
	'''
	Type of the source, this will decide the icon to show in the UI for source [Client, NetScaler, Server, etc.]
	'''
	@target_type.setter
	def target_type(self,target_type):
		try :
			if not isinstance(target_type,str):
				raise TypeError("target_type must be set to str value")
			self._target_type = target_type
		except Exception as e :
			raise e

	'''
	Text to display for the target [e.g.: User name, NetScaler IP, Server IP, etc.]
	'''
	@property
	def target(self):
		try:
			return self._target
		except Exception as e :
			raise e
	'''
	Text to display for the target [e.g.: User name, NetScaler IP, Server IP, etc.]
	'''
	@target.setter
	def target(self,target):
		try :
			if not isinstance(target,str):
				raise TypeError("target must be set to str value")
			self._target = target
		except Exception as e :
			raise e

	'''
	AfReportforTopURLbeingCountManagedbythisAFCollector.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				session_hop_distribution_obj=session_hop_distribution()
				response = session_hop_distribution_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of session_hop_distribution resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			session_hop_distribution_obj = session_hop_distribution()
			option_ = options()
			option_._filter=filter_
			return session_hop_distribution_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the session_hop_distribution resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			session_hop_distribution_obj = session_hop_distribution()
			option_ = options()
			option_._count=True
			response = session_hop_distribution_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of session_hop_distribution resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			session_hop_distribution_obj = session_hop_distribution()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = session_hop_distribution_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(session_hop_distribution_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.session_hop_distribution
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(session_hop_distribution_responses, response, "session_hop_distribution_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.session_hop_distribution_response_array
				i=0
				error = [session_hop_distribution() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.session_hop_distribution_response_array
			i=0
			session_hop_distribution_objs = [session_hop_distribution() for _ in range(len(response))]
			for obj in response :
				for props in obj._session_hop_distribution:
					result = service.payload_formatter.string_to_bulk_resource(session_hop_distribution_response,self.__class__.__name__,props)
					session_hop_distribution_objs[i] = result.session_hop_distribution
					i=i+1
			return session_hop_distribution_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(session_hop_distribution,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class session_hop_distribution_response(base_response):
	def __init__(self,length=1) :
		self.session_hop_distribution= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.session_hop_distribution= [ session_hop_distribution() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class session_hop_distribution_responses(base_response):
	def __init__(self,length=1) :
		self.session_hop_distribution_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.session_hop_distribution_response_array = [ session_hop_distribution() for _ in range(length)]
