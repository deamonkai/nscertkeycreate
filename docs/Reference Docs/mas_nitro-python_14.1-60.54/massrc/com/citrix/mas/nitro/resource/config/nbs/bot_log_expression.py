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


import os
import logging
from logging import handlers, Formatter
from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for Bot Logexpression resource
'''

class bot_log_expression(base_resource):
	_bot_log_expr_value= ""
	_bot_attack_offset_len= ""
	_bot_log_expr_name= ""
	_bot_log_expr_comment= ""
	_bot_attack_offset= ""
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/macro/v1/security/bot_log_expression"
		except Exception as e :
			raise e

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
			return "bot_log_expression"
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
			return "bot_log_expressions"
		except Exception as e :
			raise e



	'''
	get Log Expression Value
	'''
	@property
	def bot_log_expr_value(self) :
		try:
			return self._bot_log_expr_value
		except Exception as e :
			raise e
	'''
	set Log Expression Value
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
	get Attack Offset Length
	'''
	@property
	def bot_attack_offset_len(self) :
		try:
			return self._bot_attack_offset_len
		except Exception as e :
			raise e
	'''
	set Attack Offset Length
	'''
	@bot_attack_offset_len.setter
	def bot_attack_offset_len(self,bot_attack_offset_len):
		try :
			if not isinstance(bot_attack_offset_len,long):
				raise TypeError("bot_attack_offset_len must be set to long value")
			self._bot_attack_offset_len = bot_attack_offset_len
		except Exception as e :
			raise e


	'''
	get Log Expression Name
	'''
	@property
	def bot_log_expr_name(self) :
		try:
			return self._bot_log_expr_name
		except Exception as e :
			raise e
	'''
	set Log Expression Name
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
	get Log Expression Comment
	'''
	@property
	def bot_log_expr_comment(self) :
		try:
			return self._bot_log_expr_comment
		except Exception as e :
			raise e
	'''
	set Log Expression Comment
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
	get Attack Offset
	'''
	@property
	def bot_attack_offset(self) :
		try:
			return self._bot_attack_offset
		except Exception as e :
			raise e
	'''
	set Attack Offset
	'''
	@bot_attack_offset.setter
	def bot_attack_offset(self,bot_attack_offset):
		try :
			if not isinstance(bot_attack_offset,long):
				raise TypeError("bot_attack_offset must be set to long value")
			self._bot_attack_offset = bot_attack_offset
		except Exception as e :
			raise e

	'''
	Bot LogExpression Details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			response=""
			if not resource :
				bot_log_expression_obj=bot_log_expression()
				response = bot_log_expression_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of bot_log_expression resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			bot_log_expression_obj = bot_log_expression()
			option_ = options()
			option_._filter=filter_
			return bot_log_expression_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the bot_log_expression resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			bot_log_expression_obj = bot_log_expression()
			option_ = options()
			option_._count=True
			response = bot_log_expression_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of bot_log_expression resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			#Resetting request and response params from last operation
			cls._request_params = []
			cls._response_params = []
			bot_log_expression_obj = bot_log_expression()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = bot_log_expression_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(bot_log_expression_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.bot_log_expression
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(bot_log_expression_responses, response, "bot_log_expression_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.bot_log_expression_response_array
				i=0
				error = [bot_log_expression() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.bot_log_expression_response_array
			i=0
			bot_log_expression_objs = [bot_log_expression() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_bot_log_expression'):
					for props in obj._bot_log_expression:
						result = service.payload_formatter.string_to_bulk_resource(bot_log_expression_response,self.__class__.__name__,props)
						bot_log_expression_objs[i] = result.bot_log_expression
						i=i+1
			return bot_log_expression_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(bot_log_expression,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class bot_log_expression_response(base_response):
	def __init__(self,length=1) :
		self.bot_log_expression= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.bot_log_expression= [ bot_log_expression() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class bot_log_expression_responses(base_response):
	def __init__(self,length=1) :
		self.bot_log_expression_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.bot_log_expression_response_array = [ bot_log_expression() for _ in range(length)]
