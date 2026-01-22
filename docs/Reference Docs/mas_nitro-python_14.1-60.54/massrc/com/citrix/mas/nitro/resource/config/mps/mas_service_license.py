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
Configuration for NetScaler Console License Information resource
'''

class mas_service_license(base_resource):
	_entitlement_id= ""
	_end_date= ""
	_entitlement_type= ""
	_start_date= ""
	_quantity= ""
	_customer_id= ""
	_id= ""
	_start_time= ""
	_max_vips= ""
	_product_sku= ""
	_lic_type= ""
	_end_time= ""
	_approved= ""
	_max_tp_vservers= ""
	_max_storage= ""
	_serial_numbers= ""
	_days_to_expire= ""
	_total_allowed_tp_vips= ""
	_entitled_db_storage= ""
	_total_allowed_vips= ""
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
			return "mas_service_license"
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
			return "mas_service_licenses"
		except Exception as e :
			raise e



	'''
	get Entitlement Id for the license file
	'''
	@property
	def entitlement_id(self) :
		try:
			return self._entitlement_id
		except Exception as e :
			raise e
	'''
	set Entitlement Id for the license file
	'''
	@entitlement_id.setter
	def entitlement_id(self,entitlement_id):
		try :
			if not isinstance(entitlement_id,str):
				raise TypeError("entitlement_id must be set to str value")
			self._entitlement_id = entitlement_id
		except Exception as e :
			raise e


	'''
	get Expiry date of license subscription
	'''
	@property
	def end_date(self) :
		try:
			return self._end_date
		except Exception as e :
			raise e
	'''
	set Expiry date of license subscription
	'''
	@end_date.setter
	def end_date(self,end_date):
		try :
			if not isinstance(end_date,str):
				raise TypeError("end_date must be set to str value")
			self._end_date = end_date
		except Exception as e :
			raise e


	'''
	get Entitlement Type eg. ProductionTrial
	'''
	@property
	def entitlement_type(self) :
		try:
			return self._entitlement_type
		except Exception as e :
			raise e
	'''
	set Entitlement Type eg. ProductionTrial
	'''
	@entitlement_type.setter
	def entitlement_type(self,entitlement_type):
		try :
			if not isinstance(entitlement_type,str):
				raise TypeError("entitlement_type must be set to str value")
			self._entitlement_type = entitlement_type
		except Exception as e :
			raise e


	'''
	get Start date of license subscription
	'''
	@property
	def start_date(self) :
		try:
			return self._start_date
		except Exception as e :
			raise e
	'''
	set Start date of license subscription
	'''
	@start_date.setter
	def start_date(self,start_date):
		try :
			if not isinstance(start_date,str):
				raise TypeError("start_date must be set to str value")
			self._start_date = start_date
		except Exception as e :
			raise e


	'''
	get Number of Licenses of the type purchased
	'''
	@property
	def quantity(self) :
		try:
			return self._quantity
		except Exception as e :
			raise e
	'''
	set Number of Licenses of the type purchased
	'''
	@quantity.setter
	def quantity(self,quantity):
		try :
			if not isinstance(quantity,str):
				raise TypeError("quantity must be set to str value")
			self._quantity = quantity
		except Exception as e :
			raise e


	'''
	get Customer Id for the tenant who has purchased the license
	'''
	@property
	def customer_id(self) :
		try:
			return self._customer_id
		except Exception as e :
			raise e
	'''
	set Customer Id for the tenant who has purchased the license
	'''
	@customer_id.setter
	def customer_id(self,customer_id):
		try :
			if not isinstance(customer_id,str):
				raise TypeError("customer_id must be set to str value")
			self._customer_id = customer_id
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
	get License validity starts from this timestamp
	'''
	@property
	def start_time(self) :
		try:
			return self._start_time
		except Exception as e :
			raise e
	'''
	set License validity starts from this timestamp
	'''
	@start_time.setter
	def start_time(self,start_time):
		try :
			if not isinstance(start_time,long):
				raise TypeError("start_time must be set to long value")
			self._start_time = start_time
		except Exception as e :
			raise e


	'''
	get Maximum VIPs
	'''
	@property
	def max_vips(self) :
		try:
			return self._max_vips
		except Exception as e :
			raise e


	'''
	get Product SKU of the License which specifies the type of license : VIPs, Storage or ThirdParty VIPS
	'''
	@property
	def product_sku(self) :
		try:
			return self._product_sku
		except Exception as e :
			raise e
	'''
	set Product SKU of the License which specifies the type of license : VIPs, Storage or ThirdParty VIPS
	'''
	@product_sku.setter
	def product_sku(self,product_sku):
		try :
			if not isinstance(product_sku,str):
				raise TypeError("product_sku must be set to str value")
			self._product_sku = product_sku
		except Exception as e :
			raise e


	'''
	get 0 = Trial Period, 1 = Licensed, 2 = Grace period, 3 = Unlicensed, 4 = Canceled
	'''
	@property
	def lic_type(self) :
		try:
			return self._lic_type
		except Exception as e :
			raise e
	'''
	set 0 = Trial Period, 1 = Licensed, 2 = Grace period, 3 = Unlicensed, 4 = Canceled
	'''
	@lic_type.setter
	def lic_type(self,lic_type):
		try :
			if not isinstance(lic_type,int):
				raise TypeError("lic_type must be set to int value")
			self._lic_type = lic_type
		except Exception as e :
			raise e


	'''
	get License expires at this timestamp
	'''
	@property
	def end_time(self) :
		try:
			return self._end_time
		except Exception as e :
			raise e
	'''
	set License expires at this timestamp
	'''
	@end_time.setter
	def end_time(self,end_time):
		try :
			if not isinstance(end_time,long):
				raise TypeError("end_time must be set to long value")
			self._end_time = end_time
		except Exception as e :
			raise e


	'''
	get Approved
	'''
	@property
	def approved(self) :
		try:
			return self._approved
		except Exception as e :
			raise e
	'''
	set Approved
	'''
	@approved.setter
	def approved(self,approved):
		try :
			if not isinstance(approved,bool):
				raise TypeError("approved must be set to bool value")
			self._approved = approved
		except Exception as e :
			raise e


	'''
	get Maximum Third Party Vservers
	'''
	@property
	def max_tp_vservers(self) :
		try:
			return self._max_tp_vservers
		except Exception as e :
			raise e


	'''
	get Maximum Storage for the license in GB
	'''
	@property
	def max_storage(self) :
		try:
			return self._max_storage
		except Exception as e :
			raise e


	'''
	get SerialNumbers
	'''
	@property
	def serial_numbers(self) :
		try:
			return self._serial_numbers
		except Exception as e :
			raise e
	'''
	set SerialNumbers
	'''
	@serial_numbers.setter
	def serial_numbers(self,serial_numbers):
		try :
			if not isinstance(serial_numbers,str):
				raise TypeError("serial_numbers must be set to str value")
			self._serial_numbers = serial_numbers
		except Exception as e :
			raise e

	'''
	Days to expire
	'''
	@property
	def days_to_expire(self):
		try:
			return self._days_to_expire
		except Exception as e :
			raise e

	'''
	Total Allowed Third Party Vservres
	'''
	@property
	def total_allowed_tp_vips(self):
		try:
			return self._total_allowed_tp_vips
		except Exception as e :
			raise e

	'''
	Total entitled DB storage
	'''
	@property
	def entitled_db_storage(self):
		try:
			return self._entitled_db_storage
		except Exception as e :
			raise e

	'''
	Total Allowed VIPs
	'''
	@property
	def total_allowed_vips(self):
		try:
			return self._total_allowed_vips
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler Console license information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mas_service_license_obj=mas_service_license()
				response = mas_service_license_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to enable/disable NetScaler Console system features.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mas_service_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mas_service_license_obj = mas_service_license()
			option_ = options()
			option_._filter=filter_
			return mas_service_license_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mas_service_license resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mas_service_license_obj = mas_service_license()
			option_ = options()
			option_._count=True
			response = mas_service_license_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mas_service_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mas_service_license_obj = mas_service_license()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mas_service_license_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mas_service_license_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mas_service_license
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mas_service_license_responses, response, "mas_service_license_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mas_service_license_response_array
				i=0
				error = [mas_service_license() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mas_service_license_response_array
			i=0
			mas_service_license_objs = [mas_service_license() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mas_service_license'):
					for props in obj._mas_service_license:
						result = service.payload_formatter.string_to_bulk_resource(mas_service_license_response,self.__class__.__name__,props)
						mas_service_license_objs[i] = result.mas_service_license
						i=i+1
			return mas_service_license_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mas_service_license,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mas_service_license_response(base_response):
	def __init__(self,length=1) :
		self.mas_service_license= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mas_service_license= [ mas_service_license() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mas_service_license_responses(base_response):
	def __init__(self,length=1) :
		self.mas_service_license_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mas_service_license_response_array = [ mas_service_license() for _ in range(length)]
