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
Configuration for LAS Signed Identity resource
'''

class las_signed_identity(base_resource):
	_id= ""
	_lsid= ""
	_orgID= ""
	_customerid= ""
	_ls_details_token= ""
	_ls_pubkey_token= ""
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
			return "las_signed_identity"
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
			return "las_signed_identitys"
		except Exception as e :
			raise e



	'''
	get Id is system generated key for all the VM Instances
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the VM Instances
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
	get License Server UUID
	'''
	@property
	def lsid(self) :
		try:
			return self._lsid
		except Exception as e :
			raise e
	'''
	set License Server UUID
	'''
	@lsid.setter
	def lsid(self,lsid):
		try :
			if not isinstance(lsid,str):
				raise TypeError("lsid must be set to str value")
			self._lsid = lsid
		except Exception as e :
			raise e


	'''
	get customerorgid
	'''
	@property
	def orgID(self) :
		try:
			return self._orgID
		except Exception as e :
			raise e
	'''
	set customerorgid
	'''
	@orgID.setter
	def orgID(self,orgID):
		try :
			if not isinstance(orgID,str):
				raise TypeError("orgID must be set to str value")
			self._orgID = orgID
		except Exception as e :
			raise e


	'''
	get customerid
	'''
	@property
	def customerid(self) :
		try:
			return self._customerid
		except Exception as e :
			raise e
	'''
	set customerid
	'''
	@customerid.setter
	def customerid(self,customerid):
		try :
			if not isinstance(customerid,str):
				raise TypeError("customerid must be set to str value")
			self._customerid = customerid
		except Exception as e :
			raise e


	'''
	get ls_details_token
	'''
	@property
	def ls_details_token(self) :
		try:
			return self._ls_details_token
		except Exception as e :
			raise e
	'''
	set ls_details_token
	'''
	@ls_details_token.setter
	def ls_details_token(self,ls_details_token):
		try :
			if not isinstance(ls_details_token,str):
				raise TypeError("ls_details_token must be set to str value")
			self._ls_details_token = ls_details_token
		except Exception as e :
			raise e


	'''
	get ls_pubkey_token
	'''
	@property
	def ls_pubkey_token(self) :
		try:
			return self._ls_pubkey_token
		except Exception as e :
			raise e
	'''
	set ls_pubkey_token
	'''
	@ls_pubkey_token.setter
	def ls_pubkey_token(self,ls_pubkey_token):
		try :
			if not isinstance(ls_pubkey_token,str):
				raise TypeError("ls_pubkey_token must be set to str value")
			self._ls_pubkey_token = ls_pubkey_token
		except Exception as e :
			raise e

	'''
	Use this operation to get LAS signed identity.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				las_signed_identity_obj=las_signed_identity()
				response = las_signed_identity_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of las_signed_identity resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			las_signed_identity_obj = las_signed_identity()
			option_ = options()
			option_._filter=filter_
			return las_signed_identity_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the las_signed_identity resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			las_signed_identity_obj = las_signed_identity()
			option_ = options()
			option_._count=True
			response = las_signed_identity_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of las_signed_identity resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			las_signed_identity_obj = las_signed_identity()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = las_signed_identity_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(las_signed_identity_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.las_signed_identity
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_signed_identity_responses, response, "las_signed_identity_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.las_signed_identity_response_array
				i=0
				error = [las_signed_identity() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.las_signed_identity_response_array
			i=0
			las_signed_identity_objs = [las_signed_identity() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_las_signed_identity'):
					for props in obj._las_signed_identity:
						result = service.payload_formatter.string_to_bulk_resource(las_signed_identity_response,self.__class__.__name__,props)
						las_signed_identity_objs[i] = result.las_signed_identity
						i=i+1
			return las_signed_identity_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(las_signed_identity,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class las_signed_identity_response(base_response):
	def __init__(self,length=1) :
		self.las_signed_identity= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.las_signed_identity= [ las_signed_identity() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class las_signed_identity_responses(base_response):
	def __init__(self,length=1) :
		self.las_signed_identity_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.las_signed_identity_response_array = [ las_signed_identity() for _ in range(length)]
