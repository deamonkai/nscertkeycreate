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
Configuration for LAS License Feature Information resource
'''

class las_license_info(base_resource):
	_token_exp= ""
	_licensesavailable= ""
	_licenseproductname= ""
	_localizedlicenseproductname= ""
	_licensetype= ""
	_licenseexpdate= ""
	_id= ""
	_pem= ""
	_licensesadate= ""
	_token_nbf= ""
	_uniq_param= ""
	_vendorstring= ""
	_licenseedition= ""
	_licensemodel= ""
	_localizedlicenseedition= ""
	_localizedlicensetype= ""
	_licenseoverdraft= ""
	_localizedlicensemodel= ""
	_licensesinuse= ""
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
			return "las_license_info"
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
			return "las_license_infos"
		except Exception as e :
			raise e



	'''
	get Token Exp
	'''
	@property
	def token_exp(self) :
		try:
			return self._token_exp
		except Exception as e :
			raise e
	'''
	set Token Exp
	'''
	@token_exp.setter
	def token_exp(self,token_exp):
		try :
			if not isinstance(token_exp,str):
				raise TypeError("token_exp must be set to str value")
			self._token_exp = token_exp
		except Exception as e :
			raise e


	'''
	get Licenses Available
	'''
	@property
	def licensesavailable(self) :
		try:
			return self._licensesavailable
		except Exception as e :
			raise e
	'''
	set Licenses Available
	'''
	@licensesavailable.setter
	def licensesavailable(self,licensesavailable):
		try :
			if not isinstance(licensesavailable,int):
				raise TypeError("licensesavailable must be set to int value")
			self._licensesavailable = licensesavailable
		except Exception as e :
			raise e


	'''
	get License Product Name
	'''
	@property
	def licenseproductname(self) :
		try:
			return self._licenseproductname
		except Exception as e :
			raise e
	'''
	set License Product Name
	'''
	@licenseproductname.setter
	def licenseproductname(self,licenseproductname):
		try :
			if not isinstance(licenseproductname,str):
				raise TypeError("licenseproductname must be set to str value")
			self._licenseproductname = licenseproductname
		except Exception as e :
			raise e


	'''
	get Localized License Product Name
	'''
	@property
	def localizedlicenseproductname(self) :
		try:
			return self._localizedlicenseproductname
		except Exception as e :
			raise e
	'''
	set Localized License Product Name
	'''
	@localizedlicenseproductname.setter
	def localizedlicenseproductname(self,localizedlicenseproductname):
		try :
			if not isinstance(localizedlicenseproductname,str):
				raise TypeError("localizedlicenseproductname must be set to str value")
			self._localizedlicenseproductname = localizedlicenseproductname
		except Exception as e :
			raise e


	'''
	get License Type
	'''
	@property
	def licensetype(self) :
		try:
			return self._licensetype
		except Exception as e :
			raise e
	'''
	set License Type
	'''
	@licensetype.setter
	def licensetype(self,licensetype):
		try :
			if not isinstance(licensetype,str):
				raise TypeError("licensetype must be set to str value")
			self._licensetype = licensetype
		except Exception as e :
			raise e


	'''
	get License Expiration Date
	'''
	@property
	def licenseexpdate(self) :
		try:
			return self._licenseexpdate
		except Exception as e :
			raise e
	'''
	set License Expiration Date
	'''
	@licenseexpdate.setter
	def licenseexpdate(self,licenseexpdate):
		try :
			if not isinstance(licenseexpdate,str):
				raise TypeError("licenseexpdate must be set to str value")
			self._licenseexpdate = licenseexpdate
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
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
	get PEM
	'''
	@property
	def pem(self) :
		try:
			return self._pem
		except Exception as e :
			raise e
	'''
	set PEM
	'''
	@pem.setter
	def pem(self,pem):
		try :
			if not isinstance(pem,str):
				raise TypeError("pem must be set to str value")
			self._pem = pem
		except Exception as e :
			raise e


	'''
	get License Subscription Advantage Date
	'''
	@property
	def licensesadate(self) :
		try:
			return self._licensesadate
		except Exception as e :
			raise e
	'''
	set License Subscription Advantage Date
	'''
	@licensesadate.setter
	def licensesadate(self,licensesadate):
		try :
			if not isinstance(licensesadate,str):
				raise TypeError("licensesadate must be set to str value")
			self._licensesadate = licensesadate
		except Exception as e :
			raise e


	'''
	get Token Nbf
	'''
	@property
	def token_nbf(self) :
		try:
			return self._token_nbf
		except Exception as e :
			raise e
	'''
	set Token Nbf
	'''
	@token_nbf.setter
	def token_nbf(self,token_nbf):
		try :
			if not isinstance(token_nbf,str):
				raise TypeError("token_nbf must be set to str value")
			self._token_nbf = token_nbf
		except Exception as e :
			raise e


	'''
	get uniq_param combination of pem, licenseexpirydate and licensetype
	'''
	@property
	def uniq_param(self) :
		try:
			return self._uniq_param
		except Exception as e :
			raise e
	'''
	set uniq_param combination of pem, licenseexpirydate and licensetype
	'''
	@uniq_param.setter
	def uniq_param(self,uniq_param):
		try :
			if not isinstance(uniq_param,str):
				raise TypeError("uniq_param must be set to str value")
			self._uniq_param = uniq_param
		except Exception as e :
			raise e


	'''
	get Vendor String
	'''
	@property
	def vendorstring(self) :
		try:
			return self._vendorstring
		except Exception as e :
			raise e
	'''
	set Vendor String
	'''
	@vendorstring.setter
	def vendorstring(self,vendorstring):
		try :
			if not isinstance(vendorstring,str):
				raise TypeError("vendorstring must be set to str value")
			self._vendorstring = vendorstring
		except Exception as e :
			raise e


	'''
	get License Edition
	'''
	@property
	def licenseedition(self) :
		try:
			return self._licenseedition
		except Exception as e :
			raise e
	'''
	set License Edition
	'''
	@licenseedition.setter
	def licenseedition(self,licenseedition):
		try :
			if not isinstance(licenseedition,str):
				raise TypeError("licenseedition must be set to str value")
			self._licenseedition = licenseedition
		except Exception as e :
			raise e


	'''
	get License Model
	'''
	@property
	def licensemodel(self) :
		try:
			return self._licensemodel
		except Exception as e :
			raise e
	'''
	set License Model
	'''
	@licensemodel.setter
	def licensemodel(self,licensemodel):
		try :
			if not isinstance(licensemodel,str):
				raise TypeError("licensemodel must be set to str value")
			self._licensemodel = licensemodel
		except Exception as e :
			raise e

	'''
	Localized License Edition
	'''
	@property
	def localizedlicenseedition(self):
		try:
			return self._localizedlicenseedition
		except Exception as e :
			raise e
	'''
	Localized License Edition
	'''
	@localizedlicenseedition.setter
	def localizedlicenseedition(self,localizedlicenseedition):
		try :
			if not isinstance(localizedlicenseedition,str):
				raise TypeError("localizedlicenseedition must be set to str value")
			self._localizedlicenseedition = localizedlicenseedition
		except Exception as e :
			raise e

	'''
	localized License Type
	'''
	@property
	def localizedlicensetype(self):
		try:
			return self._localizedlicensetype
		except Exception as e :
			raise e
	'''
	localized License Type
	'''
	@localizedlicensetype.setter
	def localizedlicensetype(self,localizedlicensetype):
		try :
			if not isinstance(localizedlicensetype,str):
				raise TypeError("localizedlicensetype must be set to str value")
			self._localizedlicensetype = localizedlicensetype
		except Exception as e :
			raise e

	'''
	License Overdraft
	'''
	@property
	def licenseoverdraft(self):
		try:
			return self._licenseoverdraft
		except Exception as e :
			raise e
	'''
	License Overdraft
	'''
	@licenseoverdraft.setter
	def licenseoverdraft(self,licenseoverdraft):
		try :
			if not isinstance(licenseoverdraft,int):
				raise TypeError("licenseoverdraft must be set to int value")
			self._licenseoverdraft = licenseoverdraft
		except Exception as e :
			raise e

	'''
	Localized License Model
	'''
	@property
	def localizedlicensemodel(self):
		try:
			return self._localizedlicensemodel
		except Exception as e :
			raise e
	'''
	Localized License Model
	'''
	@localizedlicensemodel.setter
	def localizedlicensemodel(self,localizedlicensemodel):
		try :
			if not isinstance(localizedlicensemodel,str):
				raise TypeError("localizedlicensemodel must be set to str value")
			self._localizedlicensemodel = localizedlicensemodel
		except Exception as e :
			raise e

	'''
	Licenses In Use
	'''
	@property
	def licensesinuse(self):
		try:
			return self._licensesinuse
		except Exception as e :
			raise e
	'''
	Licenses In Use
	'''
	@licensesinuse.setter
	def licensesinuse(self,licensesinuse):
		try :
			if not isinstance(licensesinuse,int):
				raise TypeError("licensesinuse must be set to int value")
			self._licensesinuse = licensesinuse
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_license_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.las_license_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_license_info_responses, response, "las_license_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.las_license_info_response_array
				i=0
				error = [las_license_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.las_license_info_response_array
			i=0
			las_license_info_objs = [las_license_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_las_license_info'):
					for props in obj._las_license_info:
						result = service.payload_formatter.string_to_bulk_resource(las_license_info_response,self.__class__.__name__,props)
						las_license_info_objs[i] = result.las_license_info
						i=i+1
			return las_license_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(las_license_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class las_license_info_response(base_response):
	def __init__(self,length=1) :
		self.las_license_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.las_license_info= [ las_license_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class las_license_info_responses(base_response):
	def __init__(self,length=1) :
		self.las_license_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.las_license_info_response_array = [ las_license_info() for _ in range(length)]
