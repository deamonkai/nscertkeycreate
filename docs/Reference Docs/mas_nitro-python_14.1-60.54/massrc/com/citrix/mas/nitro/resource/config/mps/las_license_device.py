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
Configuration for LAS License Device resource
'''

class las_license_device(base_resource):
	_failure_reason= ""
	_token_nbf= ""
	_sdx_inst_allocated= ""
	_token_exp= ""
	_first_activation_ts= ""
	_lpeid= ""
	_vpx_inst_allocated= ""
	_activation_id= ""
	_id= ""
	_std_bw_total= ""
	_nstype= ""
	_nsip= ""
	_hostname= ""
	_activation_status= ""
	_products= ""
	_vpx_fips_inst_allocated= ""
	_adm_signed_token= ""
	_plt_bw_total= ""
	_is_las_licensed= ""
	_mpx_inst_allocated= ""
	_ent_bw_total= ""
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
			return "las_license_device"
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
			return "las_license_devices"
		except Exception as e :
			raise e



	'''
	get Reason for token activation failure on NS
	'''
	@property
	def failure_reason(self) :
		try:
			return self._failure_reason
		except Exception as e :
			raise e
	'''
	set Reason for token activation failure on NS
	'''
	@failure_reason.setter
	def failure_reason(self,failure_reason):
		try :
			if not isinstance(failure_reason,str):
				raise TypeError("failure_reason must be set to str value")
			self._failure_reason = failure_reason
		except Exception as e :
			raise e


	'''
	get token nbf
	'''
	@property
	def token_nbf(self) :
		try:
			return self._token_nbf
		except Exception as e :
			raise e
	'''
	set token nbf
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
	get sdx_inst_allocated
	'''
	@property
	def sdx_inst_allocated(self) :
		try:
			return self._sdx_inst_allocated
		except Exception as e :
			raise e
	'''
	set sdx_inst_allocated
	'''
	@sdx_inst_allocated.setter
	def sdx_inst_allocated(self,sdx_inst_allocated):
		try :
			if not isinstance(sdx_inst_allocated,int):
				raise TypeError("sdx_inst_allocated must be set to int value")
			self._sdx_inst_allocated = sdx_inst_allocated
		except Exception as e :
			raise e


	'''
	get token expiry
	'''
	@property
	def token_exp(self) :
		try:
			return self._token_exp
		except Exception as e :
			raise e
	'''
	set token expiry
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
	get First LAS activation timestamp
	'''
	@property
	def first_activation_ts(self) :
		try:
			return self._first_activation_ts
		except Exception as e :
			raise e
	'''
	set First LAS activation timestamp
	'''
	@first_activation_ts.setter
	def first_activation_ts(self,first_activation_ts):
		try :
			if not isinstance(first_activation_ts,str):
				raise TypeError("first_activation_ts must be set to str value")
			self._first_activation_ts = first_activation_ts
		except Exception as e :
			raise e


	'''
	get device_uuid from managed device
	'''
	@property
	def lpeid(self) :
		try:
			return self._lpeid
		except Exception as e :
			raise e
	'''
	set device_uuid from managed device
	'''
	@lpeid.setter
	def lpeid(self,lpeid):
		try :
			if not isinstance(lpeid,str):
				raise TypeError("lpeid must be set to str value")
			self._lpeid = lpeid
		except Exception as e :
			raise e


	'''
	get vpx_inst_allocated
	'''
	@property
	def vpx_inst_allocated(self) :
		try:
			return self._vpx_inst_allocated
		except Exception as e :
			raise e
	'''
	set vpx_inst_allocated
	'''
	@vpx_inst_allocated.setter
	def vpx_inst_allocated(self,vpx_inst_allocated):
		try :
			if not isinstance(vpx_inst_allocated,int):
				raise TypeError("vpx_inst_allocated must be set to int value")
			self._vpx_inst_allocated = vpx_inst_allocated
		except Exception as e :
			raise e


	'''
	get LAS activation ID for NS
	'''
	@property
	def activation_id(self) :
		try:
			return self._activation_id
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
	get LAS Capacity STD Bandwidth
	'''
	@property
	def std_bw_total(self) :
		try:
			return self._std_bw_total
		except Exception as e :
			raise e
	'''
	set LAS Capacity STD Bandwidth
	'''
	@std_bw_total.setter
	def std_bw_total(self,std_bw_total):
		try :
			if not isinstance(std_bw_total,int):
				raise TypeError("std_bw_total must be set to int value")
			self._std_bw_total = std_bw_total
		except Exception as e :
			raise e


	'''
	get NS Param: Netscaler Form Factor
	'''
	@property
	def nstype(self) :
		try:
			return self._nstype
		except Exception as e :
			raise e


	'''
	get NSIP of NS
	'''
	@property
	def nsip(self) :
		try:
			return self._nsip
		except Exception as e :
			raise e
	'''
	set NSIP of NS
	'''
	@nsip.setter
	def nsip(self,nsip):
		try :
			if not isinstance(nsip,str):
				raise TypeError("nsip must be set to str value")
			self._nsip = nsip
		except Exception as e :
			raise e


	'''
	get NS Param: host name
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e


	'''
	get Activation status for this LPEID
	'''
	@property
	def activation_status(self) :
		try:
			return self._activation_status
		except Exception as e :
			raise e
	'''
	set Activation status for this LPEID
	'''
	@activation_status.setter
	def activation_status(self,activation_status):
		try :
			if not isinstance(activation_status,str):
				raise TypeError("activation_status must be set to str value")
			self._activation_status = activation_status
		except Exception as e :
			raise e


	'''
	get NS Param: product
	'''
	@property
	def products(self) :
		try:
			return self._products
		except Exception as e :
			raise e


	'''
	get vpx_fips_inst_allocated
	'''
	@property
	def vpx_fips_inst_allocated(self) :
		try:
			return self._vpx_fips_inst_allocated
		except Exception as e :
			raise e
	'''
	set vpx_fips_inst_allocated
	'''
	@vpx_fips_inst_allocated.setter
	def vpx_fips_inst_allocated(self,vpx_fips_inst_allocated):
		try :
			if not isinstance(vpx_fips_inst_allocated,int):
				raise TypeError("vpx_fips_inst_allocated must be set to int value")
			self._vpx_fips_inst_allocated = vpx_fips_inst_allocated
		except Exception as e :
			raise e


	'''
	get Full JWT adm signed token
	'''
	@property
	def adm_signed_token(self) :
		try:
			return self._adm_signed_token
		except Exception as e :
			raise e
	'''
	set Full JWT adm signed token
	'''
	@adm_signed_token.setter
	def adm_signed_token(self,adm_signed_token):
		try :
			if not isinstance(adm_signed_token,str):
				raise TypeError("adm_signed_token must be set to str value")
			self._adm_signed_token = adm_signed_token
		except Exception as e :
			raise e


	'''
	get LAS Capacity Bandwidth
	'''
	@property
	def plt_bw_total(self) :
		try:
			return self._plt_bw_total
		except Exception as e :
			raise e
	'''
	set LAS Capacity Bandwidth
	'''
	@plt_bw_total.setter
	def plt_bw_total(self,plt_bw_total):
		try :
			if not isinstance(plt_bw_total,int):
				raise TypeError("plt_bw_total must be set to int value")
			self._plt_bw_total = plt_bw_total
		except Exception as e :
			raise e


	'''
	get is the device las licensed
	'''
	@property
	def is_las_licensed(self) :
		try:
			return self._is_las_licensed
		except Exception as e :
			raise e
	'''
	set is the device las licensed
	'''
	@is_las_licensed.setter
	def is_las_licensed(self,is_las_licensed):
		try :
			if not isinstance(is_las_licensed,bool):
				raise TypeError("is_las_licensed must be set to bool value")
			self._is_las_licensed = is_las_licensed
		except Exception as e :
			raise e


	'''
	get mpx_inst_allocated
	'''
	@property
	def mpx_inst_allocated(self) :
		try:
			return self._mpx_inst_allocated
		except Exception as e :
			raise e
	'''
	set mpx_inst_allocated
	'''
	@mpx_inst_allocated.setter
	def mpx_inst_allocated(self,mpx_inst_allocated):
		try :
			if not isinstance(mpx_inst_allocated,int):
				raise TypeError("mpx_inst_allocated must be set to int value")
			self._mpx_inst_allocated = mpx_inst_allocated
		except Exception as e :
			raise e


	'''
	get LAS Capacity ENT Bandwidth
	'''
	@property
	def ent_bw_total(self) :
		try:
			return self._ent_bw_total
		except Exception as e :
			raise e
	'''
	set LAS Capacity ENT Bandwidth
	'''
	@ent_bw_total.setter
	def ent_bw_total(self,ent_bw_total):
		try :
			if not isinstance(ent_bw_total,int):
				raise TypeError("ent_bw_total must be set to int value")
			self._ent_bw_total = ent_bw_total
		except Exception as e :
			raise e

	'''
	Use this operation to get LAS license device.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				las_license_device_obj=las_license_device()
				response = las_license_device_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of las_license_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			las_license_device_obj = las_license_device()
			option_ = options()
			option_._filter=filter_
			return las_license_device_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the las_license_device resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			las_license_device_obj = las_license_device()
			option_ = options()
			option_._count=True
			response = las_license_device_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of las_license_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			las_license_device_obj = las_license_device()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = las_license_device_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(las_license_device_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.las_license_device
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(las_license_device_responses, response, "las_license_device_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.las_license_device_response_array
				i=0
				error = [las_license_device() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.las_license_device_response_array
			i=0
			las_license_device_objs = [las_license_device() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_las_license_device'):
					for props in obj._las_license_device:
						result = service.payload_formatter.string_to_bulk_resource(las_license_device_response,self.__class__.__name__,props)
						las_license_device_objs[i] = result.las_license_device
						i=i+1
			return las_license_device_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(las_license_device,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class las_license_device_response(base_response):
	def __init__(self,length=1) :
		self.las_license_device= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.las_license_device= [ las_license_device() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class las_license_device_responses(base_response):
	def __init__(self,length=1) :
		self.las_license_device_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.las_license_device_response_array = [ las_license_device() for _ in range(length)]
