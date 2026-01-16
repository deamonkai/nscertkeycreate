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
Configuration for Security advisory details on NetScaler Console resource
'''

class ns_security_advisory(base_resource):
	_overall_scan_status= ""
	_id= ""
	_secure_config_advisory_status= ""
	_end_time= ""
	_start_time= ""
	_file_integrity_monitoring_status= ""
	_scan_recurrence= ""
	_cve_detection_status= ""
	_ns_ip_addresses_list= ""
	_scan_all_devices= ""
	_scan_type= ""
	_scan_initiated_by= ""
	_scan_execution_time= ""
	_file_integrity_monitoring= ""
	_secure_config_advisory= ""
	_cve_detection= ""
	_enable_file_integrity_monitoring_system_scan= ""
	_next_scan_time= ""
	_enable_secure_config_advisory_system_scan= ""
	_ns_ip_addresses=[]
	_enable_cve_detection_system_scan= ""
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
			return "ns_security_advisory"
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
			return "ns_security_advisorys"
		except Exception as e :
			raise e



	'''
	get Overall status of the scan
	'''
	@property
	def overall_scan_status(self) :
		try:
			return self._overall_scan_status
		except Exception as e :
			raise e
	'''
	set Overall status of the scan
	'''
	@overall_scan_status.setter
	def overall_scan_status(self,overall_scan_status):
		try :
			if not isinstance(overall_scan_status,str):
				raise TypeError("overall_scan_status must be set to str value")
			self._overall_scan_status = overall_scan_status
		except Exception as e :
			raise e


	'''
	get ID of Security Advisory scan
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set ID of Security Advisory scan
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
	get Secure Config Advisory Status
	'''
	@property
	def secure_config_advisory_status(self) :
		try:
			return self._secure_config_advisory_status
		except Exception as e :
			raise e
	'''
	set Secure Config Advisory Status
	'''
	@secure_config_advisory_status.setter
	def secure_config_advisory_status(self,secure_config_advisory_status):
		try :
			if not isinstance(secure_config_advisory_status,str):
				raise TypeError("secure_config_advisory_status must be set to str value")
			self._secure_config_advisory_status = secure_config_advisory_status
		except Exception as e :
			raise e


	'''
	get Scan end time
	'''
	@property
	def end_time(self) :
		try:
			return self._end_time
		except Exception as e :
			raise e
	'''
	set Scan end time
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
	get Scan start time
	'''
	@property
	def start_time(self) :
		try:
			return self._start_time
		except Exception as e :
			raise e
	'''
	set Scan start time
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
	get File Integrity Monitoring Status
	'''
	@property
	def file_integrity_monitoring_status(self) :
		try:
			return self._file_integrity_monitoring_status
		except Exception as e :
			raise e
	'''
	set File Integrity Monitoring Status
	'''
	@file_integrity_monitoring_status.setter
	def file_integrity_monitoring_status(self,file_integrity_monitoring_status):
		try :
			if not isinstance(file_integrity_monitoring_status,str):
				raise TypeError("file_integrity_monitoring_status must be set to str value")
			self._file_integrity_monitoring_status = file_integrity_monitoring_status
		except Exception as e :
			raise e


	'''
	get Scan recurrence
	'''
	@property
	def scan_recurrence(self) :
		try:
			return self._scan_recurrence
		except Exception as e :
			raise e
	'''
	set Scan recurrence
	'''
	@scan_recurrence.setter
	def scan_recurrence(self,scan_recurrence):
		try :
			if not isinstance(scan_recurrence,str):
				raise TypeError("scan_recurrence must be set to str value")
			self._scan_recurrence = scan_recurrence
		except Exception as e :
			raise e


	'''
	get CVE Detection Status
	'''
	@property
	def cve_detection_status(self) :
		try:
			return self._cve_detection_status
		except Exception as e :
			raise e
	'''
	set CVE Detection Status
	'''
	@cve_detection_status.setter
	def cve_detection_status(self,cve_detection_status):
		try :
			if not isinstance(cve_detection_status,str):
				raise TypeError("cve_detection_status must be set to str value")
			self._cve_detection_status = cve_detection_status
		except Exception as e :
			raise e


	'''
	get List of NetScaler IP Address
	'''
	@property
	def ns_ip_addresses_list(self) :
		try:
			return self._ns_ip_addresses_list
		except Exception as e :
			raise e
	'''
	set List of NetScaler IP Address
	'''
	@ns_ip_addresses_list.setter
	def ns_ip_addresses_list(self,ns_ip_addresses_list):
		try :
			if not isinstance(ns_ip_addresses_list,str):
				raise TypeError("ns_ip_addresses_list must be set to str value")
			self._ns_ip_addresses_list = ns_ip_addresses_list
		except Exception as e :
			raise e


	'''
	get Boolean to indicate if scan has to be run on all devices
	'''
	@property
	def scan_all_devices(self) :
		try:
			return self._scan_all_devices
		except Exception as e :
			raise e
	'''
	set Boolean to indicate if scan has to be run on all devices
	'''
	@scan_all_devices.setter
	def scan_all_devices(self,scan_all_devices):
		try :
			if not isinstance(scan_all_devices,bool):
				raise TypeError("scan_all_devices must be set to bool value")
			self._scan_all_devices = scan_all_devices
		except Exception as e :
			raise e


	'''
	get Type of scan
	'''
	@property
	def scan_type(self) :
		try:
			return self._scan_type
		except Exception as e :
			raise e
	'''
	set Type of scan
	'''
	@scan_type.setter
	def scan_type(self,scan_type):
		try :
			if not isinstance(scan_type,str):
				raise TypeError("scan_type must be set to str value")
			self._scan_type = scan_type
		except Exception as e :
			raise e


	'''
	get User who initiated the scan
	'''
	@property
	def scan_initiated_by(self) :
		try:
			return self._scan_initiated_by
		except Exception as e :
			raise e
	'''
	set User who initiated the scan
	'''
	@scan_initiated_by.setter
	def scan_initiated_by(self,scan_initiated_by):
		try :
			if not isinstance(scan_initiated_by,str):
				raise TypeError("scan_initiated_by must be set to str value")
			self._scan_initiated_by = scan_initiated_by
		except Exception as e :
			raise e


	'''
	get Scan execution time given by the user
	'''
	@property
	def scan_execution_time(self) :
		try:
			return self._scan_execution_time
		except Exception as e :
			raise e
	'''
	set Scan execution time given by the user
	'''
	@scan_execution_time.setter
	def scan_execution_time(self,scan_execution_time):
		try :
			if not isinstance(scan_execution_time,long):
				raise TypeError("scan_execution_time must be set to long value")
			self._scan_execution_time = scan_execution_time
		except Exception as e :
			raise e

	'''
	File Integrity Monitoring
	'''
	@property
	def file_integrity_monitoring(self):
		try:
			return self._file_integrity_monitoring
		except Exception as e :
			raise e
	'''
	File Integrity Monitoring
	'''
	@file_integrity_monitoring.setter
	def file_integrity_monitoring(self,file_integrity_monitoring):
		try :
			if not isinstance(file_integrity_monitoring,bool):
				raise TypeError("file_integrity_monitoring must be set to bool value")
			self._file_integrity_monitoring = file_integrity_monitoring
		except Exception as e :
			raise e

	'''
	Secure config advisory
	'''
	@property
	def secure_config_advisory(self):
		try:
			return self._secure_config_advisory
		except Exception as e :
			raise e
	'''
	Secure config advisory
	'''
	@secure_config_advisory.setter
	def secure_config_advisory(self,secure_config_advisory):
		try :
			if not isinstance(secure_config_advisory,bool):
				raise TypeError("secure_config_advisory must be set to bool value")
			self._secure_config_advisory = secure_config_advisory
		except Exception as e :
			raise e

	'''
	CVE Detection
	'''
	@property
	def cve_detection(self):
		try:
			return self._cve_detection
		except Exception as e :
			raise e
	'''
	CVE Detection
	'''
	@cve_detection.setter
	def cve_detection(self,cve_detection):
		try :
			if not isinstance(cve_detection,bool):
				raise TypeError("cve_detection must be set to bool value")
			self._cve_detection = cve_detection
		except Exception as e :
			raise e

	'''
	Enable File Integrity Monitoring System Scan
	'''
	@property
	def enable_file_integrity_monitoring_system_scan(self):
		try:
			return self._enable_file_integrity_monitoring_system_scan
		except Exception as e :
			raise e
	'''
	Enable File Integrity Monitoring System Scan
	'''
	@enable_file_integrity_monitoring_system_scan.setter
	def enable_file_integrity_monitoring_system_scan(self,enable_file_integrity_monitoring_system_scan):
		try :
			if not isinstance(enable_file_integrity_monitoring_system_scan,bool):
				raise TypeError("enable_file_integrity_monitoring_system_scan must be set to bool value")
			self._enable_file_integrity_monitoring_system_scan = enable_file_integrity_monitoring_system_scan
		except Exception as e :
			raise e

	'''
	Next System Scan Time
	'''
	@property
	def next_scan_time(self):
		try:
			return self._next_scan_time
		except Exception as e :
			raise e
	'''
	Next System Scan Time
	'''
	@next_scan_time.setter
	def next_scan_time(self,next_scan_time):
		try :
			if not isinstance(next_scan_time,long):
				raise TypeError("next_scan_time must be set to long value")
			self._next_scan_time = next_scan_time
		except Exception as e :
			raise e

	'''
	Enable Secure Config Advisory System Scan
	'''
	@property
	def enable_secure_config_advisory_system_scan(self):
		try:
			return self._enable_secure_config_advisory_system_scan
		except Exception as e :
			raise e
	'''
	Enable Secure Config Advisory System Scan
	'''
	@enable_secure_config_advisory_system_scan.setter
	def enable_secure_config_advisory_system_scan(self,enable_secure_config_advisory_system_scan):
		try :
			if not isinstance(enable_secure_config_advisory_system_scan,bool):
				raise TypeError("enable_secure_config_advisory_system_scan must be set to bool value")
			self._enable_secure_config_advisory_system_scan = enable_secure_config_advisory_system_scan
		except Exception as e :
			raise e

	'''
	NetScaler IP Addresses
	'''
	@property
	def ns_ip_addresses(self) :
		try:
			return self._ns_ip_addresses
		except Exception as e :
			raise e
	'''
	NetScaler IP Addresses
	'''
	@ns_ip_addresses.setter
	def ns_ip_addresses(self,ns_ip_addresses) :
		try :
			if not isinstance(ns_ip_addresses,list):
				raise TypeError("ns_ip_addresses must be set to array of str value")
			for item in ns_ip_addresses :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_ip_addresses = ns_ip_addresses
		except Exception as e :
			raise e

	'''
	Enable CVE Detection System Scan
	'''
	@property
	def enable_cve_detection_system_scan(self):
		try:
			return self._enable_cve_detection_system_scan
		except Exception as e :
			raise e
	'''
	Enable CVE Detection System Scan
	'''
	@enable_cve_detection_system_scan.setter
	def enable_cve_detection_system_scan(self,enable_cve_detection_system_scan):
		try :
			if not isinstance(enable_cve_detection_system_scan,bool):
				raise TypeError("enable_cve_detection_system_scan must be set to bool value")
			self._enable_cve_detection_system_scan = enable_cve_detection_system_scan
		except Exception as e :
			raise e

	'''
	To get details of Security Advisory.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			cls._op_by_primary_key_name = ""
			response=""
			if not resource :
				ns_security_advisory_obj=ns_security_advisory()
				response = ns_security_advisory_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to schedule on-demand scan..
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.perform_operation(service)
				return res
			else : 
				ns_security_advisory_obj= ns_security_advisory()
				return cls.perform_operation_bulk_request(service,resource,ns_security_advisory_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify system scan settings using action OptSystemScan..
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			cls._op_by_primary_key_name = ""
			cls._url_filter = ""
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				res = resource.update_resource(client)
				return res
			else :
				ns_security_advisory_obj=ns_security_advisory()
				return cls.update_bulk_request(client,resource,ns_security_advisory_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_security_advisory resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_security_advisory_obj = ns_security_advisory()
			option_ = options()
			option_._filter=filter_
			return ns_security_advisory_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_security_advisory resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_security_advisory_obj = ns_security_advisory()
			option_ = options()
			option_._count=True
			response = ns_security_advisory_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_security_advisory resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_security_advisory_obj = ns_security_advisory()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_security_advisory_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_security_advisory_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_security_advisory
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_security_advisory_responses, response, "ns_security_advisory_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_security_advisory_response_array
				i=0
				error = [ns_security_advisory() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_security_advisory_response_array
			i=0
			ns_security_advisory_objs = [ns_security_advisory() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_security_advisory'):
					for props in obj._ns_security_advisory:
						result = service.payload_formatter.string_to_bulk_resource(ns_security_advisory_response,self.__class__.__name__,props)
						ns_security_advisory_objs[i] = result.ns_security_advisory
						i=i+1
			return ns_security_advisory_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_security_advisory,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_security_advisory_response(base_response):
	def __init__(self,length=1) :
		self.ns_security_advisory= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_security_advisory= [ ns_security_advisory() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_security_advisory_responses(base_response):
	def __init__(self,length=1) :
		self.ns_security_advisory_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_security_advisory_response_array = [ ns_security_advisory() for _ in range(length)]
