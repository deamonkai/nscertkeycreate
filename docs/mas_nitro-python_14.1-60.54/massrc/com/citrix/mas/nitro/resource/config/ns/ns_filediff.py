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
Configuration for monitoring file list diff present in nsconfig folder of NetScaler instances resource
'''

class ns_filediff(base_resource):
	_id= ""
	_display_name= ""
	_latest_filelist_details= ""
	_diff_summary= ""
	_host_name= ""
	_diff_exists= ""
	_latest_polled_timestamp= ""
	_previous_polled_timestamp= ""
	_previous_filelist_details= ""
	_ip_address= ""
	_diff_status= ""
	_last_modified= ""
	_file_name= ""
	_filediff_count= ""
	_total_count= ""
	_filediff_na_count= ""
	__count=""
	'''
	get the resource id
	'''
	def get_resource_id(self) :
		try:
			if hasattr(self, 'id'):
				return self.id 
			else:
				return None 
		except Exception as e :
			raise e

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "ns_filediff"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._id
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
			return "ns_filediffs"
		except Exception as e :
			raise e



	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get display name 
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e
	'''
	set display name 
	'''
	@display_name.setter
	def display_name(self,display_name):
		try :
			if not isinstance(display_name,str):
				raise TypeError("display_name must be set to str value")
			self._display_name = display_name
		except Exception as e :
			raise e


	'''
	get Comma separated list of files under nsconfig folder found in latest poll
	'''
	@property
	def latest_filelist_details(self) :
		try:
			return self._latest_filelist_details
		except Exception as e :
			raise e
	'''
	set Comma separated list of files under nsconfig folder found in latest poll
	'''
	@latest_filelist_details.setter
	def latest_filelist_details(self,latest_filelist_details):
		try :
			if not isinstance(latest_filelist_details,str):
				raise TypeError("latest_filelist_details must be set to str value")
			self._latest_filelist_details = latest_filelist_details
		except Exception as e :
			raise e


	'''
	get diff summary
	'''
	@property
	def diff_summary(self) :
		try:
			return self._diff_summary
		except Exception as e :
			raise e
	'''
	set diff summary
	'''
	@diff_summary.setter
	def diff_summary(self,diff_summary):
		try :
			if not isinstance(diff_summary,str):
				raise TypeError("diff_summary must be set to str value")
			self._diff_summary = diff_summary
		except Exception as e :
			raise e


	'''
	get host name
	'''
	@property
	def host_name(self) :
		try:
			return self._host_name
		except Exception as e :
			raise e
	'''
	set host name
	'''
	@host_name.setter
	def host_name(self,host_name):
		try :
			if not isinstance(host_name,str):
				raise TypeError("host_name must be set to str value")
			self._host_name = host_name
		except Exception as e :
			raise e


	'''
	get Diff exists. Possible values No Diff,NA,Diff Exists
	'''
	@property
	def diff_exists(self) :
		try:
			return self._diff_exists
		except Exception as e :
			raise e
	'''
	set Diff exists. Possible values No Diff,NA,Diff Exists
	'''
	@diff_exists.setter
	def diff_exists(self,diff_exists):
		try :
			if not isinstance(diff_exists,str):
				raise TypeError("diff_exists must be set to str value")
			self._diff_exists = diff_exists
		except Exception as e :
			raise e


	'''
	get Latest polled timestamp
	'''
	@property
	def latest_polled_timestamp(self) :
		try:
			return self._latest_polled_timestamp
		except Exception as e :
			raise e


	'''
	get Previous polled timestamp
	'''
	@property
	def previous_polled_timestamp(self) :
		try:
			return self._previous_polled_timestamp
		except Exception as e :
			raise e


	'''
	get Comma separated list of files under nsconfig folder found in previous poll
	'''
	@property
	def previous_filelist_details(self) :
		try:
			return self._previous_filelist_details
		except Exception as e :
			raise e
	'''
	set Comma separated list of files under nsconfig folder found in previous poll
	'''
	@previous_filelist_details.setter
	def previous_filelist_details(self,previous_filelist_details):
		try :
			if not isinstance(previous_filelist_details,str):
				raise TypeError("previous_filelist_details must be set to str value")
			self._previous_filelist_details = previous_filelist_details
		except Exception as e :
			raise e


	'''
	get IP Address of NetScaler device
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e

	'''
	diff status of the file. Possible values: added,modified,deleted
	'''
	@property
	def diff_status(self):
		try:
			return self._diff_status
		except Exception as e :
			raise e
	'''
	diff status of the file. Possible values: added,modified,deleted
	'''
	@diff_status.setter
	def diff_status(self,diff_status):
		try :
			if not isinstance(diff_status,str):
				raise TypeError("diff_status must be set to str value")
			self._diff_status = diff_status
		except Exception as e :
			raise e

	'''
	last modified timestamp of the file
	'''
	@property
	def last_modified(self):
		try:
			return self._last_modified
		except Exception as e :
			raise e
	'''
	last modified timestamp of the file
	'''
	@last_modified.setter
	def last_modified(self,last_modified):
		try :
			if not isinstance(last_modified,long):
				raise TypeError("last_modified must be set to long value")
			self._last_modified = last_modified
		except Exception as e :
			raise e

	'''
	file name
	'''
	@property
	def file_name(self):
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	file name
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e

	'''
	Total file diff count 
	'''
	@property
	def filediff_count(self):
		try:
			return self._filediff_count
		except Exception as e :
			raise e
	'''
	Total file diff count 
	'''
	@filediff_count.setter
	def filediff_count(self,filediff_count):
		try :
			if not isinstance(filediff_count,int):
				raise TypeError("filediff_count must be set to int value")
			self._filediff_count = filediff_count
		except Exception as e :
			raise e

	'''
	Total count available 
	'''
	@property
	def total_count(self):
		try:
			return self._total_count
		except Exception as e :
			raise e
	'''
	Total count available 
	'''
	@total_count.setter
	def total_count(self,total_count):
		try :
			if not isinstance(total_count,int):
				raise TypeError("total_count must be set to int value")
			self._total_count = total_count
		except Exception as e :
			raise e

	'''
	Total file diff not applicable count 
	'''
	@property
	def filediff_na_count(self):
		try:
			return self._filediff_na_count
		except Exception as e :
			raise e
	'''
	Total file diff not applicable count 
	'''
	@filediff_na_count.setter
	def filediff_na_count(self,filediff_na_count):
		try :
			if not isinstance(filediff_na_count,int):
				raise TypeError("filediff_na_count must be set to int value")
			self._filediff_na_count = filediff_na_count
		except Exception as e :
			raise e

	'''
	Use this operation to get file list present in nsconfig folder of ADC.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_filediff_obj=ns_filediff()
				response = ns_filediff_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_filediff resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_filediff_obj = ns_filediff()
			option_ = options()
			option_._filter=filter_
			return ns_filediff_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_filediff resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_filediff_obj = ns_filediff()
			option_ = options()
			option_._count=True
			response = ns_filediff_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_filediff resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_filediff_obj = ns_filediff()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_filediff_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_filediff_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_filediff
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_filediff_responses, response, "ns_filediff_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_filediff_response_array
				i=0
				error = [ns_filediff() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_filediff_response_array
			i=0
			ns_filediff_objs = [ns_filediff() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_filediff'):
					for props in obj._ns_filediff:
						result = service.payload_formatter.string_to_bulk_resource(ns_filediff_response,self.__class__.__name__,props)
						ns_filediff_objs[i] = result.ns_filediff
						i=i+1
			return ns_filediff_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_filediff,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_filediff_response(base_response):
	def __init__(self,length=1) :
		self.ns_filediff= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_filediff= [ ns_filediff() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_filediff_responses(base_response):
	def __init__(self,length=1) :
		self.ns_filediff_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_filediff_response_array = [ ns_filediff() for _ in range(length)]
