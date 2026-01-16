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
Configuration for AF Web Report for Level 3 resource
'''

class af_web_uuid_report_first_l3(base_resource):
	_other_metrics_4_value= ""
	_ip_address= ""
	_other_metrics_3_value= ""
	_application_name= ""
	_rpt_sample_time= ""
	_other_metrics_6_value= ""
	_other_metrics_5_value= ""
	_report_id= ""
	_attribute= ""
	_ctnsappname= ""
	_other_metrics_2_value= ""
	_exporter_id= ""
	_other_metrics_7_value= ""
	_order_by_metrics_value= ""
	_other_metrics_1_value= ""
	__count=""

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "af_web_uuid_report_first_l3"
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
			return "af_web_uuid_report_first_l3s"
		except Exception as e :
			raise e



	'''
	get Other Metrics 4 Value
	'''
	@property
	def other_metrics_4_value(self) :
		try:
			return self._other_metrics_4_value
		except Exception as e :
			raise e
	'''
	set Other Metrics 4 Value
	'''
	@other_metrics_4_value.setter
	def other_metrics_4_value(self,other_metrics_4_value):
		try :
			if not isinstance(other_metrics_4_value,long):
				raise TypeError("other_metrics_4_value must be set to long value")
			self._other_metrics_4_value = other_metrics_4_value
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
	get Other Metrics 3 Value
	'''
	@property
	def other_metrics_3_value(self) :
		try:
			return self._other_metrics_3_value
		except Exception as e :
			raise e
	'''
	set Other Metrics 3 Value
	'''
	@other_metrics_3_value.setter
	def other_metrics_3_value(self,other_metrics_3_value):
		try :
			if not isinstance(other_metrics_3_value,long):
				raise TypeError("other_metrics_3_value must be set to long value")
			self._other_metrics_3_value = other_metrics_3_value
		except Exception as e :
			raise e


	'''
	get Application Name
	'''
	@property
	def application_name(self) :
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	set Application Name
	'''
	@application_name.setter
	def application_name(self,application_name):
		try :
			if not isinstance(application_name,str):
				raise TypeError("application_name must be set to str value")
			self._application_name = application_name
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
	get Other Metrics 6 Value
	'''
	@property
	def other_metrics_6_value(self) :
		try:
			return self._other_metrics_6_value
		except Exception as e :
			raise e
	'''
	set Other Metrics 6 Value
	'''
	@other_metrics_6_value.setter
	def other_metrics_6_value(self,other_metrics_6_value):
		try :
			if not isinstance(other_metrics_6_value,long):
				raise TypeError("other_metrics_6_value must be set to long value")
			self._other_metrics_6_value = other_metrics_6_value
		except Exception as e :
			raise e


	'''
	get Other Metrics 5 Value
	'''
	@property
	def other_metrics_5_value(self) :
		try:
			return self._other_metrics_5_value
		except Exception as e :
			raise e
	'''
	set Other Metrics 5 Value
	'''
	@other_metrics_5_value.setter
	def other_metrics_5_value(self,other_metrics_5_value):
		try :
			if not isinstance(other_metrics_5_value,long):
				raise TypeError("other_metrics_5_value must be set to long value")
			self._other_metrics_5_value = other_metrics_5_value
		except Exception as e :
			raise e


	'''
	get Report ID
	'''
	@property
	def report_id(self) :
		try:
			return self._report_id
		except Exception as e :
			raise e
	'''
	set Report ID
	'''
	@report_id.setter
	def report_id(self,report_id):
		try :
			if not isinstance(report_id,long):
				raise TypeError("report_id must be set to long value")
			self._report_id = report_id
		except Exception as e :
			raise e


	'''
	get Attribute value
	'''
	@property
	def attribute(self) :
		try:
			return self._attribute
		except Exception as e :
			raise e
	'''
	set Attribute value
	'''
	@attribute.setter
	def attribute(self,attribute):
		try :
			if not isinstance(attribute,str):
				raise TypeError("attribute must be set to str value")
			self._attribute = attribute
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
	get Other Metrics 2 Value
	'''
	@property
	def other_metrics_2_value(self) :
		try:
			return self._other_metrics_2_value
		except Exception as e :
			raise e
	'''
	set Other Metrics 2 Value
	'''
	@other_metrics_2_value.setter
	def other_metrics_2_value(self,other_metrics_2_value):
		try :
			if not isinstance(other_metrics_2_value,long):
				raise TypeError("other_metrics_2_value must be set to long value")
			self._other_metrics_2_value = other_metrics_2_value
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
	get Other Metrics 7 Value
	'''
	@property
	def other_metrics_7_value(self) :
		try:
			return self._other_metrics_7_value
		except Exception as e :
			raise e
	'''
	set Other Metrics 7 Value
	'''
	@other_metrics_7_value.setter
	def other_metrics_7_value(self,other_metrics_7_value):
		try :
			if not isinstance(other_metrics_7_value,long):
				raise TypeError("other_metrics_7_value must be set to long value")
			self._other_metrics_7_value = other_metrics_7_value
		except Exception as e :
			raise e


	'''
	get Order By Metrics Value
	'''
	@property
	def order_by_metrics_value(self) :
		try:
			return self._order_by_metrics_value
		except Exception as e :
			raise e
	'''
	set Order By Metrics Value
	'''
	@order_by_metrics_value.setter
	def order_by_metrics_value(self,order_by_metrics_value):
		try :
			if not isinstance(order_by_metrics_value,long):
				raise TypeError("order_by_metrics_value must be set to long value")
			self._order_by_metrics_value = order_by_metrics_value
		except Exception as e :
			raise e


	'''
	get Other Metrics 1 Value
	'''
	@property
	def other_metrics_1_value(self) :
		try:
			return self._other_metrics_1_value
		except Exception as e :
			raise e
	'''
	set Other Metrics 1 Value
	'''
	@other_metrics_1_value.setter
	def other_metrics_1_value(self,other_metrics_1_value):
		try :
			if not isinstance(other_metrics_1_value,long):
				raise TypeError("other_metrics_1_value must be set to long value")
			self._other_metrics_1_value = other_metrics_1_value
		except Exception as e :
			raise e

	'''
	Af Report for Web First STRING..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_web_uuid_report_first_l3_obj=af_web_uuid_report_first_l3()
				response = af_web_uuid_report_first_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_web_uuid_report_first_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_web_uuid_report_first_l3_obj = af_web_uuid_report_first_l3()
			option_ = options()
			option_._filter=filter_
			return af_web_uuid_report_first_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_web_uuid_report_first_l3 resources configured on NetScaler SDX.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_web_uuid_report_first_l3_obj = af_web_uuid_report_first_l3()
			option_ = options()
			option_._count=True
			response = af_web_uuid_report_first_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['__count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_web_uuid_report_first_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_web_uuid_report_first_l3_obj = af_web_uuid_report_first_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_web_uuid_report_first_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_web_uuid_report_first_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_web_uuid_report_first_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_web_uuid_report_first_l3_responses, response, "af_web_uuid_report_first_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_web_uuid_report_first_l3_response_array
				i=0
				error = [af_web_uuid_report_first_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_web_uuid_report_first_l3_response_array
			i=0
			af_web_uuid_report_first_l3_objs = [af_web_uuid_report_first_l3() for _ in range(len(response))]
			for obj in response :
				for props in obj._af_web_uuid_report_first_l3:
					result = service.payload_formatter.string_to_bulk_resource(af_web_uuid_report_first_l3_response,self.__class__.__name__,props)
					af_web_uuid_report_first_l3_objs[i] = result.af_web_uuid_report_first_l3
					i=i+1
			return af_web_uuid_report_first_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_web_uuid_report_first_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_web_uuid_report_first_l3_response(base_response):
	def __init__(self,length=1) :
		self.af_web_uuid_report_first_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_web_uuid_report_first_l3= [ af_web_uuid_report_first_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_web_uuid_report_first_l3_responses(base_response):
	def __init__(self,length=1) :
		self.af_web_uuid_report_first_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_web_uuid_report_first_l3_response_array = [ af_web_uuid_report_first_l3() for _ in range(length)]
