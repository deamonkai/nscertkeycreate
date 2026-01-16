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
Configuration for Execute the Appflow Info Query through Remote Proxy Handler resource
'''

class adc_update_appflow_info(base_resource):
	_webinsight= ""
	_metricslog= ""
	_appflowlog_effective= ""
	_analytics_managed= ""
	_securityinsight= ""
	_vsvr_name= ""
	_action= ""
	_transport= ""
	_collectors= ""
	_agent_list= ""
	_transactionlog= ""
	_collector_ip= ""
	_type= ""
	_videoanalytics= ""
	_icalog= ""
	_clientsidemeasurements= ""
	_ns_ip_address= ""
	_policy_name= ""
	_export_option= ""
	_rule= ""
	_priority= ""
	_appflow_policy_rule= ""
	_es4nslog= ""
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
			return "adc_update_appflow_info"
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
			return "adc_update_appflow_infos"
		except Exception as e :
			raise e



	'''
	get webinsight
	'''
	@property
	def webinsight(self) :
		try:
			return self._webinsight
		except Exception as e :
			raise e
	'''
	set webinsight
	'''
	@webinsight.setter
	def webinsight(self,webinsight):
		try :
			if not isinstance(webinsight,str):
				raise TypeError("webinsight must be set to str value")
			self._webinsight = webinsight
		except Exception as e :
			raise e


	'''
	get metricslog
	'''
	@property
	def metricslog(self) :
		try:
			return self._metricslog
		except Exception as e :
			raise e
	'''
	set metricslog
	'''
	@metricslog.setter
	def metricslog(self,metricslog):
		try :
			if not isinstance(metricslog,bool):
				raise TypeError("metricslog must be set to bool value")
			self._metricslog = metricslog
		except Exception as e :
			raise e


	'''
	get Appflowlog effective (validating AppFlow config) enabled or disabled
	'''
	@property
	def appflowlog_effective(self) :
		try:
			return self._appflowlog_effective
		except Exception as e :
			raise e
	'''
	set Appflowlog effective (validating AppFlow config) enabled or disabled
	'''
	@appflowlog_effective.setter
	def appflowlog_effective(self,appflowlog_effective):
		try :
			if not isinstance(appflowlog_effective,str):
				raise TypeError("appflowlog_effective must be set to str value")
			self._appflowlog_effective = appflowlog_effective
		except Exception as e :
			raise e


	'''
	get analytics is user/auto enabled/disabled
	'''
	@property
	def analytics_managed(self) :
		try:
			return self._analytics_managed
		except Exception as e :
			raise e
	'''
	set analytics is user/auto enabled/disabled
	'''
	@analytics_managed.setter
	def analytics_managed(self,analytics_managed):
		try :
			if not isinstance(analytics_managed,str):
				raise TypeError("analytics_managed must be set to str value")
			self._analytics_managed = analytics_managed
		except Exception as e :
			raise e


	'''
	get securityinsight
	'''
	@property
	def securityinsight(self) :
		try:
			return self._securityinsight
		except Exception as e :
			raise e
	'''
	set securityinsight
	'''
	@securityinsight.setter
	def securityinsight(self,securityinsight):
		try :
			if not isinstance(securityinsight,str):
				raise TypeError("securityinsight must be set to str value")
			self._securityinsight = securityinsight
		except Exception as e :
			raise e


	'''
	get Vserver name
	'''
	@property
	def vsvr_name(self) :
		try:
			return self._vsvr_name
		except Exception as e :
			raise e
	'''
	set Vserver name
	'''
	@vsvr_name.setter
	def vsvr_name(self,vsvr_name):
		try :
			if not isinstance(vsvr_name,str):
				raise TypeError("vsvr_name must be set to str value")
			self._vsvr_name = vsvr_name
		except Exception as e :
			raise e


	'''
	get action
	'''
	@property
	def action(self) :
		try:
			return self._action
		except Exception as e :
			raise e
	'''
	set action
	'''
	@action.setter
	def action(self,action):
		try :
			if not isinstance(action,str):
				raise TypeError("action must be set to str value")
			self._action = action
		except Exception as e :
			raise e


	'''
	get Transport type.
	'''
	@property
	def transport(self) :
		try:
			return self._transport
		except Exception as e :
			raise e
	'''
	set Transport type.
	'''
	@transport.setter
	def transport(self,transport):
		try :
			if not isinstance(transport,str):
				raise TypeError("transport must be set to str value")
			self._transport = transport
		except Exception as e :
			raise e


	'''
	get collectors
	'''
	@property
	def collectors(self) :
		try:
			return self._collectors
		except Exception as e :
			raise e
	'''
	set collectors
	'''
	@collectors.setter
	def collectors(self,collectors):
		try :
			if not isinstance(collectors,str):
				raise TypeError("collectors must be set to str value")
			self._collectors = collectors
		except Exception as e :
			raise e


	'''
	get Agent List, on which traffic will flow
	'''
	@property
	def agent_list(self) :
		try:
			return self._agent_list
		except Exception as e :
			raise e
	'''
	set Agent List, on which traffic will flow
	'''
	@agent_list.setter
	def agent_list(self,agent_list):
		try :
			if not isinstance(agent_list,str):
				raise TypeError("agent_list must be set to str value")
			self._agent_list = agent_list
		except Exception as e :
			raise e


	'''
	get transactionlog
	'''
	@property
	def transactionlog(self) :
		try:
			return self._transactionlog
		except Exception as e :
			raise e
	'''
	set transactionlog
	'''
	@transactionlog.setter
	def transactionlog(self,transactionlog):
		try :
			if not isinstance(transactionlog,str):
				raise TypeError("transactionlog must be set to str value")
			self._transactionlog = transactionlog
		except Exception as e :
			raise e


	'''
	get Collector IP Address
	'''
	@property
	def collector_ip(self) :
		try:
			return self._collector_ip
		except Exception as e :
			raise e
	'''
	set Collector IP Address
	'''
	@collector_ip.setter
	def collector_ip(self,collector_ip):
		try :
			if not isinstance(collector_ip,str):
				raise TypeError("collector_ip must be set to str value")
			self._collector_ip = collector_ip
		except Exception as e :
			raise e


	'''
	get type
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set type
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get videoanalytics
	'''
	@property
	def videoanalytics(self) :
		try:
			return self._videoanalytics
		except Exception as e :
			raise e
	'''
	set videoanalytics
	'''
	@videoanalytics.setter
	def videoanalytics(self,videoanalytics):
		try :
			if not isinstance(videoanalytics,str):
				raise TypeError("videoanalytics must be set to str value")
			self._videoanalytics = videoanalytics
		except Exception as e :
			raise e


	'''
	get ICA log
	'''
	@property
	def icalog(self) :
		try:
			return self._icalog
		except Exception as e :
			raise e
	'''
	set ICA log
	'''
	@icalog.setter
	def icalog(self,icalog):
		try :
			if not isinstance(icalog,str):
				raise TypeError("icalog must be set to str value")
			self._icalog = icalog
		except Exception as e :
			raise e


	'''
	get clientsidemeasurements
	'''
	@property
	def clientsidemeasurements(self) :
		try:
			return self._clientsidemeasurements
		except Exception as e :
			raise e
	'''
	set clientsidemeasurements
	'''
	@clientsidemeasurements.setter
	def clientsidemeasurements(self,clientsidemeasurements):
		try :
			if not isinstance(clientsidemeasurements,str):
				raise TypeError("clientsidemeasurements must be set to str value")
			self._clientsidemeasurements = clientsidemeasurements
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e


	'''
	get policy_name
	'''
	@property
	def policy_name(self) :
		try:
			return self._policy_name
		except Exception as e :
			raise e
	'''
	set policy_name
	'''
	@policy_name.setter
	def policy_name(self,policy_name):
		try :
			if not isinstance(policy_name,str):
				raise TypeError("policy_name must be set to str value")
			self._policy_name = policy_name
		except Exception as e :
			raise e


	'''
	get Export Options: TCP, ICA
	'''
	@property
	def export_option(self) :
		try:
			return self._export_option
		except Exception as e :
			raise e
	'''
	set Export Options: TCP, ICA
	'''
	@export_option.setter
	def export_option(self,export_option):
		try :
			if not isinstance(export_option,str):
				raise TypeError("export_option must be set to str value")
			self._export_option = export_option
		except Exception as e :
			raise e


	'''
	get Rule
	'''
	@property
	def rule(self) :
		try:
			return self._rule
		except Exception as e :
			raise e
	'''
	set Rule
	'''
	@rule.setter
	def rule(self,rule):
		try :
			if not isinstance(rule,str):
				raise TypeError("rule must be set to str value")
			self._rule = rule
		except Exception as e :
			raise e


	'''
	get priority
	'''
	@property
	def priority(self) :
		try:
			return self._priority
		except Exception as e :
			raise e
	'''
	set priority
	'''
	@priority.setter
	def priority(self,priority):
		try :
			if not isinstance(priority,str):
				raise TypeError("priority must be set to str value")
			self._priority = priority
		except Exception as e :
			raise e


	'''
	get Appflow policy rule
	'''
	@property
	def appflow_policy_rule(self) :
		try:
			return self._appflow_policy_rule
		except Exception as e :
			raise e
	'''
	set Appflow policy rule
	'''
	@appflow_policy_rule.setter
	def appflow_policy_rule(self,appflow_policy_rule):
		try :
			if not isinstance(appflow_policy_rule,str):
				raise TypeError("appflow_policy_rule must be set to str value")
			self._appflow_policy_rule = appflow_policy_rule
		except Exception as e :
			raise e


	'''
	get ESNS enable
	'''
	@property
	def es4nslog(self) :
		try:
			return self._es4nslog
		except Exception as e :
			raise e
	'''
	set ESNS enable
	'''
	@es4nslog.setter
	def es4nslog(self,es4nslog):
		try :
			if not isinstance(es4nslog,str):
				raise TypeError("es4nslog must be set to str value")
			self._es4nslog = es4nslog
		except Exception as e :
			raise e

	'''
	Use this operation to fetch the result related to appflow info of the vserver..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				adc_update_appflow_info_obj=adc_update_appflow_info()
				response = adc_update_appflow_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adc_update_appflow_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adc_update_appflow_info_obj = adc_update_appflow_info()
			option_ = options()
			option_._filter=filter_
			return adc_update_appflow_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adc_update_appflow_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adc_update_appflow_info_obj = adc_update_appflow_info()
			option_ = options()
			option_._count=True
			response = adc_update_appflow_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adc_update_appflow_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adc_update_appflow_info_obj = adc_update_appflow_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adc_update_appflow_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adc_update_appflow_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adc_update_appflow_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adc_update_appflow_info_responses, response, "adc_update_appflow_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adc_update_appflow_info_response_array
				i=0
				error = [adc_update_appflow_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adc_update_appflow_info_response_array
			i=0
			adc_update_appflow_info_objs = [adc_update_appflow_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adc_update_appflow_info'):
					for props in obj._adc_update_appflow_info:
						result = service.payload_formatter.string_to_bulk_resource(adc_update_appflow_info_response,self.__class__.__name__,props)
						adc_update_appflow_info_objs[i] = result.adc_update_appflow_info
						i=i+1
			return adc_update_appflow_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adc_update_appflow_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adc_update_appflow_info_response(base_response):
	def __init__(self,length=1) :
		self.adc_update_appflow_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adc_update_appflow_info= [ adc_update_appflow_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adc_update_appflow_info_responses(base_response):
	def __init__(self,length=1) :
		self.adc_update_appflow_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adc_update_appflow_info_response_array = [ adc_update_appflow_info() for _ in range(length)]
