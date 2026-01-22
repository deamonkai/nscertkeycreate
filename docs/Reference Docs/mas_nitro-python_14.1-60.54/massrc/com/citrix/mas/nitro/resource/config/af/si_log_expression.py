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

from massrc.com.citrix.mas.nitro.resource.config.mps.af_generic_api import af_generic_api

'''
Configuration for Log Expression Data Report table resource
'''

class si_log_expression(af_generic_api):
	_appfwlogexprcomment= ""
	_appfwlogexprvalue= ""
	_appfwviolationtype= ""
	_transactionid= ""
	_appfwlogexprname= ""
	_ctnsappname= ""
	_si_device_ip_address= ""
	_rpt_sample_time= ""
	___count= ""
	_appfwattackoffset= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "si_log_expression"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(si_log_expression,self).get_object_id()
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
			return "si_log_expressions"
		except Exception as e :
			raise e


	'''
	AppFw Log Expr Comment
	'''
	@property
	def appfwlogexprcomment(self):
		try:
			return self._appfwlogexprcomment
		except Exception as e :
			raise e
	'''
	AppFw Log Expr Comment
	'''
	@appfwlogexprcomment.setter
	def appfwlogexprcomment(self,appfwlogexprcomment):
		try :
			if not isinstance(appfwlogexprcomment,str):
				raise TypeError("appfwlogexprcomment must be set to str value")
			self._appfwlogexprcomment = appfwlogexprcomment
		except Exception as e :
			raise e

	'''
	AppFw Log Expr value
	'''
	@property
	def appfwlogexprvalue(self):
		try:
			return self._appfwlogexprvalue
		except Exception as e :
			raise e
	'''
	AppFw Log Expr value
	'''
	@appfwlogexprvalue.setter
	def appfwlogexprvalue(self,appfwlogexprvalue):
		try :
			if not isinstance(appfwlogexprvalue,str):
				raise TypeError("appfwlogexprvalue must be set to str value")
			self._appfwlogexprvalue = appfwlogexprvalue
		except Exception as e :
			raise e

	'''
	appfwviolationtype
	'''
	@property
	def appfwviolationtype(self):
		try:
			return self._appfwviolationtype
		except Exception as e :
			raise e
	'''
	appfwviolationtype
	'''
	@appfwviolationtype.setter
	def appfwviolationtype(self,appfwviolationtype):
		try :
			if not isinstance(appfwviolationtype,int):
				raise TypeError("appfwviolationtype must be set to int value")
			self._appfwviolationtype = appfwviolationtype
		except Exception as e :
			raise e

	'''
	transactionid
	'''
	@property
	def transactionid(self):
		try:
			return self._transactionid
		except Exception as e :
			raise e
	'''
	transactionid
	'''
	@transactionid.setter
	def transactionid(self,transactionid):
		try :
			if not isinstance(transactionid,long):
				raise TypeError("transactionid must be set to long value")
			self._transactionid = transactionid
		except Exception as e :
			raise e

	'''
	AppFw Log Expr Name
	'''
	@property
	def appfwlogexprname(self):
		try:
			return self._appfwlogexprname
		except Exception as e :
			raise e
	'''
	AppFw Log Expr Name
	'''
	@appfwlogexprname.setter
	def appfwlogexprname(self,appfwlogexprname):
		try :
			if not isinstance(appfwlogexprname,str):
				raise TypeError("appfwlogexprname must be set to str value")
			self._appfwlogexprname = appfwlogexprname
		except Exception as e :
			raise e

	'''
	App Name
	'''
	@property
	def ctnsappname(self):
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	App Name
	'''
	@ctnsappname.setter
	def ctnsappname(self,ctnsappname):
		try :
			if not isinstance(ctnsappname,str):
				raise TypeError("ctnsappname must be set to str value")
			self._ctnsappname = ctnsappname
		except Exception as e :
			raise e

	'''
	NetScaler IP Address.
	'''
	@property
	def si_device_ip_address(self):
		try:
			return self._si_device_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address.
	'''
	@si_device_ip_address.setter
	def si_device_ip_address(self,si_device_ip_address):
		try :
			if not isinstance(si_device_ip_address,str):
				raise TypeError("si_device_ip_address must be set to str value")
			self._si_device_ip_address = si_device_ip_address
		except Exception as e :
			raise e

	'''
	Report time
	'''
	@property
	def rpt_sample_time(self):
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	Report time
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,long):
				raise TypeError("rpt_sample_time must be set to long value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e

	'''
	Number of records
	'''
	@property
	def __count(self):
		try:
			return self.___count
		except Exception as e :
			raise e
	'''
	Number of records
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
	appfwattackoffset
	'''
	@property
	def appfwattackoffset(self):
		try:
			return self._appfwattackoffset
		except Exception as e :
			raise e
	'''
	appfwattackoffset
	'''
	@appfwattackoffset.setter
	def appfwattackoffset(self,appfwattackoffset):
		try :
			if not isinstance(appfwattackoffset,int):
				raise TypeError("appfwattackoffset must be set to int value")
			self._appfwattackoffset = appfwattackoffset
		except Exception as e :
			raise e

	'''
	Af Report for Security Insight Device..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				si_log_expression_obj=si_log_expression()
				response = si_log_expression_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of si_log_expression resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			si_log_expression_obj = si_log_expression()
			option_ = options()
			option_._filter=filter_
			return si_log_expression_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the si_log_expression resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			si_log_expression_obj = si_log_expression()
			option_ = options()
			option_._count=True
			response = si_log_expression_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of si_log_expression resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			si_log_expression_obj = si_log_expression()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = si_log_expression_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(si_log_expression_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.si_log_expression
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(si_log_expression_responses, response, "si_log_expression_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.si_log_expression_response_array
				i=0
				error = [si_log_expression() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.si_log_expression_response_array
			i=0
			si_log_expression_objs = [si_log_expression() for _ in range(len(response))]
			for obj in response :
				for props in obj._si_log_expression:
					result = service.payload_formatter.string_to_bulk_resource(si_log_expression_response,self.__class__.__name__,props)
					si_log_expression_objs[i] = result.si_log_expression
					i=i+1
			return si_log_expression_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(si_log_expression,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class si_log_expression_response(base_response):
	def __init__(self,length=1) :
		self.si_log_expression= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.si_log_expression= [ si_log_expression() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class si_log_expression_responses(base_response):
	def __init__(self,length=1) :
		self.si_log_expression_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.si_log_expression_response_array = [ si_log_expression() for _ in range(length)]
