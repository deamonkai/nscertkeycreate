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
Configuration for API to persist the pre check when the zero touch certificates are uploaded resource
'''

class cert_precheck_result(base_resource):
	_error_message= ""
	_file_upload_time= ""
	_file_data= ""
	_id= ""
	_file_name= ""
	_activity_id= ""
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
			return "cert_precheck_result"
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
			return "cert_precheck_results"
		except Exception as e :
			raise e



	'''
	get Error message if any
	'''
	@property
	def error_message(self) :
		try:
			return self._error_message
		except Exception as e :
			raise e
	'''
	set Error message if any
	'''
	@error_message.setter
	def error_message(self,error_message):
		try :
			if not isinstance(error_message,str):
				raise TypeError("error_message must be set to str value")
			self._error_message = error_message
		except Exception as e :
			raise e


	'''
	get Creation time for this activity in seconds
	'''
	@property
	def file_upload_time(self) :
		try:
			return self._file_upload_time
		except Exception as e :
			raise e
	'''
	set Creation time for this activity in seconds
	'''
	@file_upload_time.setter
	def file_upload_time(self,file_upload_time):
		try :
			if not isinstance(file_upload_time,float):
				raise TypeError("file_upload_time must be set to float value")
			self._file_upload_time = file_upload_time
		except Exception as e :
			raise e


	'''
	get Encoded cert/key file which has no valid password to decode.
	'''
	@property
	def file_data(self) :
		try:
			return self._file_data
		except Exception as e :
			raise e
	'''
	set Encoded cert/key file which has no valid password to decode.
	'''
	@file_data.setter
	def file_data(self,file_data):
		try :
			if not isinstance(file_data,str):
				raise TypeError("file_data must be set to str value")
			self._file_data = file_data
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all failed cert entries. 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all failed cert entries. 
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
	get Certificate file name.
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set Certificate file name.
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
	get Activity Id used to track the progress of all the certificate operations.
	'''
	@property
	def activity_id(self) :
		try:
			return self._activity_id
		except Exception as e :
			raise e
	'''
	set Activity Id used to track the progress of all the certificate operations.
	'''
	@activity_id.setter
	def activity_id(self,activity_id):
		try :
			if not isinstance(activity_id,str):
				raise TypeError("activity_id must be set to str value")
			self._activity_id = activity_id
		except Exception as e :
			raise e

	'''
	Use this operation to get details of failed zero touch certificate when uploaded.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				cert_precheck_result_obj=cert_precheck_result()
				response = cert_precheck_result_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cert_precheck_result resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cert_precheck_result_obj = cert_precheck_result()
			option_ = options()
			option_._filter=filter_
			return cert_precheck_result_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cert_precheck_result resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cert_precheck_result_obj = cert_precheck_result()
			option_ = options()
			option_._count=True
			response = cert_precheck_result_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cert_precheck_result resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cert_precheck_result_obj = cert_precheck_result()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cert_precheck_result_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cert_precheck_result_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cert_precheck_result
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cert_precheck_result_responses, response, "cert_precheck_result_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cert_precheck_result_response_array
				i=0
				error = [cert_precheck_result() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cert_precheck_result_response_array
			i=0
			cert_precheck_result_objs = [cert_precheck_result() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cert_precheck_result'):
					for props in obj._cert_precheck_result:
						result = service.payload_formatter.string_to_bulk_resource(cert_precheck_result_response,self.__class__.__name__,props)
						cert_precheck_result_objs[i] = result.cert_precheck_result
						i=i+1
			return cert_precheck_result_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cert_precheck_result,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cert_precheck_result_response(base_response):
	def __init__(self,length=1) :
		self.cert_precheck_result= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cert_precheck_result= [ cert_precheck_result() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cert_precheck_result_responses(base_response):
	def __init__(self,length=1) :
		self.cert_precheck_result_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cert_precheck_result_response_array = [ cert_precheck_result() for _ in range(length)]
