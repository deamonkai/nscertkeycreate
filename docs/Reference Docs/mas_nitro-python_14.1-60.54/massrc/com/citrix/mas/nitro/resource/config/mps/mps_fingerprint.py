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
Configuration for MPS fingerprint resource
'''

class mps_fingerprint(base_resource):
	_agent_id= ""
	_finger_print= ""
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
			return "mps_fingerprint"
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
			return "mps_fingerprints"
		except Exception as e :
			raise e



	'''
	get agent_id.
	'''
	@property
	def agent_id(self) :
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	set agent_id.
	'''
	@agent_id.setter
	def agent_id(self,agent_id):
		try :
			if not isinstance(agent_id,str):
				raise TypeError("agent_id must be set to str value")
			self._agent_id = agent_id
		except Exception as e :
			raise e


	'''
	get Fingerprint/thumb-print from MAS/agent public certificate for SSL communication
	'''
	@property
	def finger_print(self) :
		try:
			return self._finger_print
		except Exception as e :
			raise e
	'''
	set Fingerprint/thumb-print from MAS/agent public certificate for SSL communication
	'''
	@finger_print.setter
	def finger_print(self,finger_print):
		try :
			if not isinstance(finger_print,str):
				raise TypeError("finger_print must be set to str value")
			self._finger_print = finger_print
		except Exception as e :
			raise e

	'''
	Use this operation to get Agent information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				mps_fingerprint_obj=mps_fingerprint()
				response = mps_fingerprint_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_fingerprint resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_fingerprint_obj = mps_fingerprint()
			option_ = options()
			option_._filter=filter_
			return mps_fingerprint_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_fingerprint resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_fingerprint_obj = mps_fingerprint()
			option_ = options()
			option_._count=True
			response = mps_fingerprint_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_fingerprint resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_fingerprint_obj = mps_fingerprint()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_fingerprint_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_fingerprint_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_fingerprint
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_fingerprint_responses, response, "mps_fingerprint_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_fingerprint_response_array
				i=0
				error = [mps_fingerprint() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_fingerprint_response_array
			i=0
			mps_fingerprint_objs = [mps_fingerprint() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_fingerprint'):
					for props in obj._mps_fingerprint:
						result = service.payload_formatter.string_to_bulk_resource(mps_fingerprint_response,self.__class__.__name__,props)
						mps_fingerprint_objs[i] = result.mps_fingerprint
						i=i+1
			return mps_fingerprint_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_fingerprint,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_fingerprint_response(base_response):
	def __init__(self,length=1) :
		self.mps_fingerprint= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_fingerprint= [ mps_fingerprint() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_fingerprint_responses(base_response):
	def __init__(self,length=1) :
		self.mps_fingerprint_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_fingerprint_response_array = [ mps_fingerprint() for _ in range(length)]
