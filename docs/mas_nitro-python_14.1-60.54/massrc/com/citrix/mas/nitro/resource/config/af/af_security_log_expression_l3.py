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
Configuration for Log Expression data table for Level 3 resource
'''

class af_security_log_expression_l3(base_resource):
	_rpt_sample_time= ""
	_appfwattackoffset= ""
	_transactionId= ""
	_appfwLogExprName= ""
	_ip_address= ""
	_backend_appname= ""
	_src_ip_address_str= ""
	_appfwLogExprValue= ""
	_appfwLogExprComment= ""
	_source_ip_address= ""
	_appname= ""
	_appfwviolationtype= ""
	_exporter_id= ""
	_ctnsappname= ""
	_backend_vserver= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_security_log_expression_l3"
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
			return "af_security_log_expression_l3s"
		except Exception as e :
			raise e



	'''
	get Report Sample time.
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time.
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
	get appfwattackoffset
	'''
	@property
	def appfwattackoffset(self) :
		try:
			return self._appfwattackoffset
		except Exception as e :
			raise e
	'''
	set appfwattackoffset
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
	get Transaction Id
	'''
	@property
	def transactionId(self) :
		try:
			return self._transactionId
		except Exception as e :
			raise e
	'''
	set Transaction Id
	'''
	@transactionId.setter
	def transactionId(self,transactionId):
		try :
			if not isinstance(transactionId,long):
				raise TypeError("transactionId must be set to long value")
			self._transactionId = transactionId
		except Exception as e :
			raise e


	'''
	get appfwLogExprName
	'''
	@property
	def appfwLogExprName(self) :
		try:
			return self._appfwLogExprName
		except Exception as e :
			raise e
	'''
	set appfwLogExprName
	'''
	@appfwLogExprName.setter
	def appfwLogExprName(self,appfwLogExprName):
		try :
			if not isinstance(appfwLogExprName,str):
				raise TypeError("appfwLogExprName must be set to str value")
			self._appfwLogExprName = appfwLogExprName
		except Exception as e :
			raise e


	'''
	get Field to store the ip address as it is along with any extension
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Field to store the ip address as it is along with any extension
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get Backend AppName
	'''
	@property
	def backend_appname(self) :
		try:
			return self._backend_appname
		except Exception as e :
			raise e
	'''
	set Backend AppName
	'''
	@backend_appname.setter
	def backend_appname(self,backend_appname):
		try :
			if not isinstance(backend_appname,str):
				raise TypeError("backend_appname must be set to str value")
			self._backend_appname = backend_appname
		except Exception as e :
			raise e


	'''
	get Field to store the Client ip address as IP Address format
	'''
	@property
	def src_ip_address_str(self) :
		try:
			return self._src_ip_address_str
		except Exception as e :
			raise e
	'''
	set Field to store the Client ip address as IP Address format
	'''
	@src_ip_address_str.setter
	def src_ip_address_str(self,src_ip_address_str):
		try :
			if not isinstance(src_ip_address_str,str):
				raise TypeError("src_ip_address_str must be set to str value")
			self._src_ip_address_str = src_ip_address_str
		except Exception as e :
			raise e


	'''
	get appfwLogExprValue
	'''
	@property
	def appfwLogExprValue(self) :
		try:
			return self._appfwLogExprValue
		except Exception as e :
			raise e
	'''
	set appfwLogExprValue
	'''
	@appfwLogExprValue.setter
	def appfwLogExprValue(self,appfwLogExprValue):
		try :
			if not isinstance(appfwLogExprValue,str):
				raise TypeError("appfwLogExprValue must be set to str value")
			self._appfwLogExprValue = appfwLogExprValue
		except Exception as e :
			raise e


	'''
	get appfwLogExprValue
	'''
	@property
	def appfwLogExprComment(self) :
		try:
			return self._appfwLogExprComment
		except Exception as e :
			raise e
	'''
	set appfwLogExprValue
	'''
	@appfwLogExprComment.setter
	def appfwLogExprComment(self,appfwLogExprComment):
		try :
			if not isinstance(appfwLogExprComment,str):
				raise TypeError("appfwLogExprComment must be set to str value")
			self._appfwLogExprComment = appfwLogExprComment
		except Exception as e :
			raise e


	'''
	get Server Source IP Address
	'''
	@property
	def source_ip_address(self) :
		try:
			return self._source_ip_address
		except Exception as e :
			raise e
	'''
	set Server Source IP Address
	'''
	@source_ip_address.setter
	def source_ip_address(self,source_ip_address):
		try :
			if not isinstance(source_ip_address,long):
				raise TypeError("source_ip_address must be set to long value")
			self._source_ip_address = source_ip_address
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@appname.setter
	def appname(self,appname):
		try :
			if not isinstance(appname,str):
				raise TypeError("appname must be set to str value")
			self._appname = appname
		except Exception as e :
			raise e


	'''
	get appfwviolationtype
	'''
	@property
	def appfwviolationtype(self) :
		try:
			return self._appfwviolationtype
		except Exception as e :
			raise e
	'''
	set appfwviolationtype
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
	get Exporter ID
	'''
	@property
	def exporter_id(self) :
		try:
			return self._exporter_id
		except Exception as e :
			raise e
	'''
	set Exporter ID
	'''
	@exporter_id.setter
	def exporter_id(self,exporter_id):
		try :
			if not isinstance(exporter_id,long):
				raise TypeError("exporter_id must be set to long value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set AppName
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
	get Backend Vserver
	'''
	@property
	def backend_vserver(self) :
		try:
			return self._backend_vserver
		except Exception as e :
			raise e
	'''
	set Backend Vserver
	'''
	@backend_vserver.setter
	def backend_vserver(self,backend_vserver):
		try :
			if not isinstance(backend_vserver,str):
				raise TypeError("backend_vserver must be set to str value")
			self._backend_vserver = backend_vserver
		except Exception as e :
			raise e

	'''
	Af Report for Threat Data..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_security_log_expression_l3_obj=af_security_log_expression_l3()
				response = af_security_log_expression_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_security_log_expression_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_security_log_expression_l3_obj = af_security_log_expression_l3()
			option_ = options()
			option_._filter=filter_
			return af_security_log_expression_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_security_log_expression_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_security_log_expression_l3_obj = af_security_log_expression_l3()
			option_ = options()
			option_._count=True
			response = af_security_log_expression_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_security_log_expression_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_security_log_expression_l3_obj = af_security_log_expression_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_security_log_expression_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_security_log_expression_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_security_log_expression_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_security_log_expression_l3_responses, response, "af_security_log_expression_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_security_log_expression_l3_response_array
				i=0
				error = [af_security_log_expression_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_security_log_expression_l3_response_array
			i=0
			af_security_log_expression_l3_objs = [af_security_log_expression_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_security_log_expression_l3:
					result = service.payload_formatter.string_to_bulk_resource(af_security_log_expression_l3_response,self.__class__.__name__,props)
					af_security_log_expression_l3_objs[i] = result.af_security_log_expression_l3
					i=i+1
			return af_security_log_expression_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_security_log_expression_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_security_log_expression_l3_response(base_response):
	def __init__(self,length=1) :
		self.af_security_log_expression_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_security_log_expression_l3= [ af_security_log_expression_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_security_log_expression_l3_responses(base_response):
	def __init__(self,length=1) :
		self.af_security_log_expression_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_security_log_expression_l3_response_array = [ af_security_log_expression_l3() for _ in range(length)]
