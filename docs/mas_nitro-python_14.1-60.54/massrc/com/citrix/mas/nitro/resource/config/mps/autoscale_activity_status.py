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
Configuration for Activity Status for the Autoscale operations resource
'''

class autoscale_activity_status(base_resource):
	_status= ""
	_activity_id= ""
	_errorcode= ""
	_is_last= ""
	_asg_id= ""
	_message= ""
	_activity= ""
	_id= ""
	_starttime= ""
	_severity= ""
	_availability_zone= ""
	_az_activity_id= ""
	_task_id= ""
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
			return "autoscale_activity_status"
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
			return "autoscale_activity_statuss"
		except Exception as e :
			raise e



	'''
	get Status of the operation
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of the operation
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
	get Parent Activity Id: Same for all the parallel provisioning processes for a particular autoscale group
	'''
	@property
	def activity_id(self) :
		try:
			return self._activity_id
		except Exception as e :
			raise e
	'''
	set Parent Activity Id: Same for all the parallel provisioning processes for a particular autoscale group
	'''
	@activity_id.setter
	def activity_id(self,activity_id):
		try :
			if not isinstance(activity_id,str):
				raise TypeError("activity_id must be set to str value")
			self._activity_id = activity_id
		except Exception as e :
			raise e


	'''
	get Error code in case of failure
	'''
	@property
	def errorcode(self) :
		try:
			return self._errorcode
		except Exception as e :
			raise e
	'''
	set Error code in case of failure
	'''
	@errorcode.setter
	def errorcode(self,errorcode):
		try :
			if not isinstance(errorcode,int):
				raise TypeError("errorcode must be set to int value")
			self._errorcode = errorcode
		except Exception as e :
			raise e


	'''
	get Enabled for the last operation
	'''
	@property
	def is_last(self) :
		try:
			return self._is_last
		except Exception as e :
			raise e


	'''
	get AutoSclae group ID to which the cluster is associated
	'''
	@property
	def asg_id(self) :
		try:
			return self._asg_id
		except Exception as e :
			raise e
	'''
	set AutoSclae group ID to which the cluster is associated
	'''
	@asg_id.setter
	def asg_id(self,asg_id):
		try :
			if not isinstance(asg_id,str):
				raise TypeError("asg_id must be set to str value")
			self._asg_id = asg_id
		except Exception as e :
			raise e


	'''
	get Message provided during the operation
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e


	'''
	get Activity details
	'''
	@property
	def activity(self) :
		try:
			return self._activity
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the task logs
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the task logs
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
	get Start Time in microseconds
	'''
	@property
	def starttime(self) :
		try:
			return self._starttime
		except Exception as e :
			raise e
	'''
	set Start Time in microseconds
	'''
	@starttime.setter
	def starttime(self,starttime):
		try :
			if not isinstance(starttime,float):
				raise TypeError("starttime must be set to float value")
			self._starttime = starttime
		except Exception as e :
			raise e


	'''
	get Error severity
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e


	'''
	get Availability Zone
	'''
	@property
	def availability_zone(self) :
		try:
			return self._availability_zone
		except Exception as e :
			raise e
	'''
	set Availability Zone
	'''
	@availability_zone.setter
	def availability_zone(self,availability_zone):
		try :
			if not isinstance(availability_zone,str):
				raise TypeError("availability_zone must be set to str value")
			self._availability_zone = availability_zone
		except Exception as e :
			raise e


	'''
	get Availability Zone Activity Id
	'''
	@property
	def az_activity_id(self) :
		try:
			return self._az_activity_id
		except Exception as e :
			raise e
	'''
	set Availability Zone Activity Id
	'''
	@az_activity_id.setter
	def az_activity_id(self,az_activity_id):
		try :
			if not isinstance(az_activity_id,str):
				raise TypeError("az_activity_id must be set to str value")
			self._az_activity_id = az_activity_id
		except Exception as e :
			raise e


	'''
	get task_id returned from other component like Provisioning/Stylebook/DistMgr
	'''
	@property
	def task_id(self) :
		try:
			return self._task_id
		except Exception as e :
			raise e
	'''
	set task_id returned from other component like Provisioning/Stylebook/DistMgr
	'''
	@task_id.setter
	def task_id(self,task_id):
		try :
			if not isinstance(task_id,str):
				raise TypeError("task_id must be set to str value")
			self._task_id = task_id
		except Exception as e :
			raise e

	'''
	Use this operation to get the autoscale activity status.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				autoscale_activity_status_obj=autoscale_activity_status()
				response = autoscale_activity_status_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of autoscale_activity_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			autoscale_activity_status_obj = autoscale_activity_status()
			option_ = options()
			option_._filter=filter_
			return autoscale_activity_status_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the autoscale_activity_status resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			autoscale_activity_status_obj = autoscale_activity_status()
			option_ = options()
			option_._count=True
			response = autoscale_activity_status_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of autoscale_activity_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			autoscale_activity_status_obj = autoscale_activity_status()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = autoscale_activity_status_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(autoscale_activity_status_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.autoscale_activity_status
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(autoscale_activity_status_responses, response, "autoscale_activity_status_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.autoscale_activity_status_response_array
				i=0
				error = [autoscale_activity_status() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.autoscale_activity_status_response_array
			i=0
			autoscale_activity_status_objs = [autoscale_activity_status() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_autoscale_activity_status'):
					for props in obj._autoscale_activity_status:
						result = service.payload_formatter.string_to_bulk_resource(autoscale_activity_status_response,self.__class__.__name__,props)
						autoscale_activity_status_objs[i] = result.autoscale_activity_status
						i=i+1
			return autoscale_activity_status_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(autoscale_activity_status,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class autoscale_activity_status_response(base_response):
	def __init__(self,length=1) :
		self.autoscale_activity_status= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.autoscale_activity_status= [ autoscale_activity_status() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class autoscale_activity_status_responses(base_response):
	def __init__(self,length=1) :
		self.autoscale_activity_status_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.autoscale_activity_status_response_array = [ autoscale_activity_status() for _ in range(length)]
