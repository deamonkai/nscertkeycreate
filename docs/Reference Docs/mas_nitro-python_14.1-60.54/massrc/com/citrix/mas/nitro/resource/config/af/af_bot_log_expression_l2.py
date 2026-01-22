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
Configuration for Log Expression data table for Level 2 resource
'''

class af_bot_log_expression_l2(base_resource):
	_src_ip_address_str= ""
	_bot_attack_offset_len= ""
	_bot_attack_offset= ""
	_bot_log_expr_name= ""
	_bot_log_expr_comment= ""
	_rpt_sample_time= ""
	_source_ip_address= ""
	_transaction_id= ""
	_bot_log_expr_value= ""
	_ip_address= ""
	_ctnsappname= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_bot_log_expression_l2"
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
			return "af_bot_log_expression_l2s"
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
	get Bot Attack Offset Len.
	'''
	@property
	def bot_attack_offset_len(self) :
		try:
			return self._bot_attack_offset_len
		except Exception as e :
			raise e
	'''
	set Bot Attack Offset Len.
	'''
	@bot_attack_offset_len.setter
	def bot_attack_offset_len(self,bot_attack_offset_len):
		try :
			if not isinstance(bot_attack_offset_len,int):
				raise TypeError("bot_attack_offset_len must be set to int value")
			self._bot_attack_offset_len = bot_attack_offset_len
		except Exception as e :
			raise e


	'''
	get Bot Attack Offset.
	'''
	@property
	def bot_attack_offset(self) :
		try:
			return self._bot_attack_offset
		except Exception as e :
			raise e
	'''
	set Bot Attack Offset.
	'''
	@bot_attack_offset.setter
	def bot_attack_offset(self,bot_attack_offset):
		try :
			if not isinstance(bot_attack_offset,int):
				raise TypeError("bot_attack_offset must be set to int value")
			self._bot_attack_offset = bot_attack_offset
		except Exception as e :
			raise e


	'''
	get bot_log_expr_name
	'''
	@property
	def bot_log_expr_name(self) :
		try:
			return self._bot_log_expr_name
		except Exception as e :
			raise e
	'''
	set bot_log_expr_name
	'''
	@bot_log_expr_name.setter
	def bot_log_expr_name(self,bot_log_expr_name):
		try :
			if not isinstance(bot_log_expr_name,str):
				raise TypeError("bot_log_expr_name must be set to str value")
			self._bot_log_expr_name = bot_log_expr_name
		except Exception as e :
			raise e


	'''
	get bot_log_expr_comment
	'''
	@property
	def bot_log_expr_comment(self) :
		try:
			return self._bot_log_expr_comment
		except Exception as e :
			raise e
	'''
	set bot_log_expr_comment
	'''
	@bot_log_expr_comment.setter
	def bot_log_expr_comment(self,bot_log_expr_comment):
		try :
			if not isinstance(bot_log_expr_comment,str):
				raise TypeError("bot_log_expr_comment must be set to str value")
			self._bot_log_expr_comment = bot_log_expr_comment
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
	get Transaction Id
	'''
	@property
	def transaction_id(self) :
		try:
			return self._transaction_id
		except Exception as e :
			raise e
	'''
	set Transaction Id
	'''
	@transaction_id.setter
	def transaction_id(self,transaction_id):
		try :
			if not isinstance(transaction_id,long):
				raise TypeError("transaction_id must be set to long value")
			self._transaction_id = transaction_id
		except Exception as e :
			raise e


	'''
	get bot_log_expr_value
	'''
	@property
	def bot_log_expr_value(self) :
		try:
			return self._bot_log_expr_value
		except Exception as e :
			raise e
	'''
	set bot_log_expr_value
	'''
	@bot_log_expr_value.setter
	def bot_log_expr_value(self,bot_log_expr_value):
		try :
			if not isinstance(bot_log_expr_value,str):
				raise TypeError("bot_log_expr_value must be set to str value")
			self._bot_log_expr_value = bot_log_expr_value
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
	get ctnsappname
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set ctnsappname
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
	Af Report for Bot Log Expression..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_bot_log_expression_l2_obj=af_bot_log_expression_l2()
				response = af_bot_log_expression_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_bot_log_expression_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_bot_log_expression_l2_obj = af_bot_log_expression_l2()
			option_ = options()
			option_._filter=filter_
			return af_bot_log_expression_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_bot_log_expression_l2 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_bot_log_expression_l2_obj = af_bot_log_expression_l2()
			option_ = options()
			option_._count=True
			response = af_bot_log_expression_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_bot_log_expression_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_bot_log_expression_l2_obj = af_bot_log_expression_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_bot_log_expression_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_bot_log_expression_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_bot_log_expression_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_bot_log_expression_l2_responses, response, "af_bot_log_expression_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_bot_log_expression_l2_response_array
				i=0
				error = [af_bot_log_expression_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_bot_log_expression_l2_response_array
			i=0
			af_bot_log_expression_l2_objs = [af_bot_log_expression_l2() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_bot_log_expression_l2:
					result = service.payload_formatter.string_to_bulk_resource(af_bot_log_expression_l2_response,self.__class__.__name__,props)
					af_bot_log_expression_l2_objs[i] = result.af_bot_log_expression_l2
					i=i+1
			return af_bot_log_expression_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_bot_log_expression_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_bot_log_expression_l2_response(base_response):
	def __init__(self,length=1) :
		self.af_bot_log_expression_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_bot_log_expression_l2= [ af_bot_log_expression_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_bot_log_expression_l2_responses(base_response):
	def __init__(self,length=1) :
		self.af_bot_log_expression_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_bot_log_expression_l2_response_array = [ af_bot_log_expression_l2() for _ in range(length)]
