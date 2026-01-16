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
Configuration for get applied darksite las lic info resource
'''

class las_lic_darksite_info(base_resource):
	_nbf= ""
	_orgid= ""
	_status= ""
	_cn= ""
	_entitlement_expiry= ""
	_lsid= ""
	_exp= ""
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
			return "las_lic_darksite_info"
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
			return "las_lic_darksite_infos"
		except Exception as e :
			raise e


	'''
	nbf of current las license
	'''
	@property
	def nbf(self):
		try:
			return self._nbf
		except Exception as e :
			raise e
	'''
	nbf of current las license
	'''
	@nbf.setter
	def nbf(self,nbf):
		try :
			if not isinstance(nbf,long):
				raise TypeError("nbf must be set to long value")
			self._nbf = nbf
		except Exception as e :
			raise e

	'''
	orgid of current las license
	'''
	@property
	def orgid(self):
		try:
			return self._orgid
		except Exception as e :
			raise e
	'''
	orgid of current las license
	'''
	@orgid.setter
	def orgid(self,orgid):
		try :
			if not isinstance(orgid,str):
				raise TypeError("orgid must be set to str value")
			self._orgid = orgid
		except Exception as e :
			raise e

	'''
	status of current las license
	'''
	@property
	def status(self):
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	status of current las license
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e

	'''
	cn of current las license
	'''
	@property
	def cn(self):
		try:
			return self._cn
		except Exception as e :
			raise e
	'''
	cn of current las license
	'''
	@cn.setter
	def cn(self,cn):
		try :
			if not isinstance(cn,str):
				raise TypeError("cn must be set to str value")
			self._cn = cn
		except Exception as e :
			raise e

	'''
	entitlement_expiry date
	'''
	@property
	def entitlement_expiry(self):
		try:
			return self._entitlement_expiry
		except Exception as e :
			raise e
	'''
	entitlement_expiry date
	'''
	@entitlement_expiry.setter
	def entitlement_expiry(self,entitlement_expiry):
		try :
			if not isinstance(entitlement_expiry,str):
				raise TypeError("entitlement_expiry must be set to str value")
			self._entitlement_expiry = entitlement_expiry
		except Exception as e :
			raise e

	'''
	lsid of current las license
	'''
	@property
	def lsid(self):
		try:
			return self._lsid
		except Exception as e :
			raise e
	'''
	lsid of current las license
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
	exp of current las license
	'''
	@property
	def exp(self):
		try:
			return self._exp
		except Exception as e :
			raise e
	'''
	exp of current las license
	'''
	@exp.setter
	def exp(self,exp):
		try :
			if not isinstance(exp,long):
				raise TypeError("exp must be set to long value")
			self._exp = exp
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_lic_darksite_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.las_lic_darksite_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_lic_darksite_info_responses, response, "las_lic_darksite_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.las_lic_darksite_info_response_array
				i=0
				error = [las_lic_darksite_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.las_lic_darksite_info_response_array
			i=0
			las_lic_darksite_info_objs = [las_lic_darksite_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_las_lic_darksite_info'):
					for props in obj._las_lic_darksite_info:
						result = service.payload_formatter.string_to_bulk_resource(las_lic_darksite_info_response,self.__class__.__name__,props)
						las_lic_darksite_info_objs[i] = result.las_lic_darksite_info
						i=i+1
			return las_lic_darksite_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(las_lic_darksite_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class las_lic_darksite_info_response(base_response):
	def __init__(self,length=1) :
		self.las_lic_darksite_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.las_lic_darksite_info= [ las_lic_darksite_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class las_lic_darksite_info_responses(base_response):
	def __init__(self,length=1) :
		self.las_lic_darksite_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.las_lic_darksite_info_response_array = [ las_lic_darksite_info() for _ in range(length)]
