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
Configuration for SSL Server Non A-Plus Details resource
'''

class nssslvserver_rating_details(base_resource):
	_display_name= ""
	_issue_ids= ""
	_ns_ip_address= ""
	_vsrvr_name= ""
	_issue_type= ""
	_issue_type_id= ""
	_id= ""
	_msg= ""
	_action= ""
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
			return "nssslvserver_rating_details"
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
			return "nssslvserver_rating_detailss"
		except Exception as e :
			raise e



	'''
	get Display Name
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e


	'''
	get issue_id
	'''
	@property
	def issue_ids(self) :
		try:
			return self._issue_ids
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e


	'''
	get VServer Name
	'''
	@property
	def vsrvr_name(self) :
		try:
			return self._vsrvr_name
		except Exception as e :
			raise e
	'''
	set VServer Name
	'''
	@vsrvr_name.setter
	def vsrvr_name(self,vsrvr_name):
		try :
			if not isinstance(vsrvr_name,str):
				raise TypeError("vsrvr_name must be set to str value")
			self._vsrvr_name = vsrvr_name
		except Exception as e :
			raise e


	'''
	This property is no longer used
	get Category of issue that occured
	'''
	@property
	def issue_type(self) :
		try:
			return self._issue_type
		except Exception as e :
			raise e
	'''
	This property is no longer used
	set Category of issue that occured
	'''
	@issue_type.setter
	def issue_type(self,issue_type):
		try :
			if not isinstance(issue_type,str):
				raise TypeError("issue_type must be set to str value")
			self._issue_type = issue_type
		except Exception as e :
			raise e


	'''
	get issue_type_id
	'''
	@property
	def issue_type_id(self) :
		try:
			return self._issue_type_id
		except Exception as e :
			raise e


	'''
	get Id is system generated PRIMARY_KEY
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated PRIMARY_KEY
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
	This property is no longer used
	get Diagnosis Message
	'''
	@property
	def msg(self) :
		try:
			return self._msg
		except Exception as e :
			raise e
	'''
	This property is no longer used
	set Diagnosis Message
	'''
	@msg.setter
	def msg(self,msg):
		try :
			if not isinstance(msg,str):
				raise TypeError("msg must be set to str value")
			self._msg = msg
		except Exception as e :
			raise e


	'''
	This property is no longer used
	get Diagnosis Message
	'''
	@property
	def action(self) :
		try:
			return self._action
		except Exception as e :
			raise e
	'''
	This property is no longer used
	set Diagnosis Message
	'''
	@action.setter
	def action(self,action):
		try :
			if not isinstance(action,str):
				raise TypeError("action must be set to str value")
			self._action = action
		except Exception as e :
			raise e

	'''
	Use this operation to get SSL Server Non A-Plus Details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				nssslvserver_rating_details_obj=nssslvserver_rating_details()
				response = nssslvserver_rating_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of nssslvserver_rating_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			nssslvserver_rating_details_obj = nssslvserver_rating_details()
			option_ = options()
			option_._filter=filter_
			return nssslvserver_rating_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the nssslvserver_rating_details resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			nssslvserver_rating_details_obj = nssslvserver_rating_details()
			option_ = options()
			option_._count=True
			response = nssslvserver_rating_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of nssslvserver_rating_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			nssslvserver_rating_details_obj = nssslvserver_rating_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = nssslvserver_rating_details_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(nssslvserver_rating_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nssslvserver_rating_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(nssslvserver_rating_details_responses, response, "nssslvserver_rating_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.nssslvserver_rating_details_response_array
				i=0
				error = [nssslvserver_rating_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.nssslvserver_rating_details_response_array
			i=0
			nssslvserver_rating_details_objs = [nssslvserver_rating_details() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_nssslvserver_rating_details'):
					for props in obj._nssslvserver_rating_details:
						result = service.payload_formatter.string_to_bulk_resource(nssslvserver_rating_details_response,self.__class__.__name__,props)
						nssslvserver_rating_details_objs[i] = result.nssslvserver_rating_details
						i=i+1
			return nssslvserver_rating_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(nssslvserver_rating_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class nssslvserver_rating_details_response(base_response):
	def __init__(self,length=1) :
		self.nssslvserver_rating_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.nssslvserver_rating_details= [ nssslvserver_rating_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class nssslvserver_rating_details_responses(base_response):
	def __init__(self,length=1) :
		self.nssslvserver_rating_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.nssslvserver_rating_details_response_array = [ nssslvserver_rating_details() for _ in range(length)]
