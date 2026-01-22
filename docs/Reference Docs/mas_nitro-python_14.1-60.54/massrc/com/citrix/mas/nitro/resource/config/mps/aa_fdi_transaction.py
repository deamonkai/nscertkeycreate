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
Configuration for NetScaler Txn Information resource
'''

class aa_fdi_transaction(base_resource):
	_transactionId= ""
	_appfwFDIFormSubmissionTime= ""
	_nsPartitionId= ""
	_sourceIPv4AddressRx= ""
	_appfwFDIUserAgent= ""
	_exportingProcessId= ""
	_appfwFDIReqUrl= ""
	_appNameLs= ""
	_appfwFDISessionId= ""
	_WAFFormData= ""
	_observationPointId= ""
	_recType= ""
	_actualtemplatecode= ""
	_appfwFDIResponseCode= ""
	_appNameVserverLs= ""
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
			return "aa_fdi_transaction"
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
			return "aa_fdi_transactions"
		except Exception as e :
			raise e



	'''
	get transactionId
	'''
	@property
	def transactionId(self) :
		try:
			return self._transactionId
		except Exception as e :
			raise e
	'''
	set transactionId
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
	get appfwFDIFormSubmissionTime
	'''
	@property
	def appfwFDIFormSubmissionTime(self) :
		try:
			return self._appfwFDIFormSubmissionTime
		except Exception as e :
			raise e
	'''
	set appfwFDIFormSubmissionTime
	'''
	@appfwFDIFormSubmissionTime.setter
	def appfwFDIFormSubmissionTime(self,appfwFDIFormSubmissionTime):
		try :
			if not isinstance(appfwFDIFormSubmissionTime,long):
				raise TypeError("appfwFDIFormSubmissionTime must be set to long value")
			self._appfwFDIFormSubmissionTime = appfwFDIFormSubmissionTime
		except Exception as e :
			raise e


	'''
	get nsPartitionId
	'''
	@property
	def nsPartitionId(self) :
		try:
			return self._nsPartitionId
		except Exception as e :
			raise e
	'''
	set nsPartitionId
	'''
	@nsPartitionId.setter
	def nsPartitionId(self,nsPartitionId):
		try :
			if not isinstance(nsPartitionId,long):
				raise TypeError("nsPartitionId must be set to long value")
			self._nsPartitionId = nsPartitionId
		except Exception as e :
			raise e


	'''
	get sourceIPv4AddressRx
	'''
	@property
	def sourceIPv4AddressRx(self) :
		try:
			return self._sourceIPv4AddressRx
		except Exception as e :
			raise e
	'''
	set sourceIPv4AddressRx
	'''
	@sourceIPv4AddressRx.setter
	def sourceIPv4AddressRx(self,sourceIPv4AddressRx):
		try :
			if not isinstance(sourceIPv4AddressRx,long):
				raise TypeError("sourceIPv4AddressRx must be set to long value")
			self._sourceIPv4AddressRx = sourceIPv4AddressRx
		except Exception as e :
			raise e


	'''
	get User Agent
	'''
	@property
	def appfwFDIUserAgent(self) :
		try:
			return self._appfwFDIUserAgent
		except Exception as e :
			raise e
	'''
	set User Agent
	'''
	@appfwFDIUserAgent.setter
	def appfwFDIUserAgent(self,appfwFDIUserAgent):
		try :
			if not isinstance(appfwFDIUserAgent,str):
				raise TypeError("appfwFDIUserAgent must be set to str value")
			self._appfwFDIUserAgent = appfwFDIUserAgent
		except Exception as e :
			raise e


	'''
	get exportingProcessId 
	'''
	@property
	def exportingProcessId(self) :
		try:
			return self._exportingProcessId
		except Exception as e :
			raise e
	'''
	set exportingProcessId 
	'''
	@exportingProcessId.setter
	def exportingProcessId(self,exportingProcessId):
		try :
			if not isinstance(exportingProcessId,long):
				raise TypeError("exportingProcessId must be set to long value")
			self._exportingProcessId = exportingProcessId
		except Exception as e :
			raise e


	'''
	get appfwFDIReqUrl
	'''
	@property
	def appfwFDIReqUrl(self) :
		try:
			return self._appfwFDIReqUrl
		except Exception as e :
			raise e
	'''
	set appfwFDIReqUrl
	'''
	@appfwFDIReqUrl.setter
	def appfwFDIReqUrl(self,appfwFDIReqUrl):
		try :
			if not isinstance(appfwFDIReqUrl,str):
				raise TypeError("appfwFDIReqUrl must be set to str value")
			self._appfwFDIReqUrl = appfwFDIReqUrl
		except Exception as e :
			raise e


	'''
	get App Name Vsver ls
	'''
	@property
	def appNameLs(self) :
		try:
			return self._appNameLs
		except Exception as e :
			raise e
	'''
	set App Name Vsver ls
	'''
	@appNameLs.setter
	def appNameLs(self,appNameLs):
		try :
			if not isinstance(appNameLs,str):
				raise TypeError("appNameLs must be set to str value")
			self._appNameLs = appNameLs
		except Exception as e :
			raise e


	'''
	get appfwFDISessionId
	'''
	@property
	def appfwFDISessionId(self) :
		try:
			return self._appfwFDISessionId
		except Exception as e :
			raise e
	'''
	set appfwFDISessionId
	'''
	@appfwFDISessionId.setter
	def appfwFDISessionId(self,appfwFDISessionId):
		try :
			if not isinstance(appfwFDISessionId,str):
				raise TypeError("appfwFDISessionId must be set to str value")
			self._appfwFDISessionId = appfwFDISessionId
		except Exception as e :
			raise e


	'''
	get WAFFormData
	'''
	@property
	def WAFFormData(self) :
		try:
			return self._WAFFormData
		except Exception as e :
			raise e
	'''
	set WAFFormData
	'''
	@WAFFormData.setter
	def WAFFormData(self,WAFFormData):
		try :
			if not isinstance(WAFFormData,str):
				raise TypeError("WAFFormData must be set to str value")
			self._WAFFormData = WAFFormData
		except Exception as e :
			raise e


	'''
	get observationPointId
	'''
	@property
	def observationPointId(self) :
		try:
			return self._observationPointId
		except Exception as e :
			raise e
	'''
	set observationPointId
	'''
	@observationPointId.setter
	def observationPointId(self,observationPointId):
		try :
			if not isinstance(observationPointId,long):
				raise TypeError("observationPointId must be set to long value")
			self._observationPointId = observationPointId
		except Exception as e :
			raise e


	'''
	get recType
	'''
	@property
	def recType(self) :
		try:
			return self._recType
		except Exception as e :
			raise e
	'''
	set recType
	'''
	@recType.setter
	def recType(self,recType):
		try :
			if not isinstance(recType,str):
				raise TypeError("recType must be set to str value")
			self._recType = recType
		except Exception as e :
			raise e


	'''
	get actualtemplatecode
	'''
	@property
	def actualtemplatecode(self) :
		try:
			return self._actualtemplatecode
		except Exception as e :
			raise e
	'''
	set actualtemplatecode
	'''
	@actualtemplatecode.setter
	def actualtemplatecode(self,actualtemplatecode):
		try :
			if not isinstance(actualtemplatecode,int):
				raise TypeError("actualtemplatecode must be set to int value")
			self._actualtemplatecode = actualtemplatecode
		except Exception as e :
			raise e


	'''
	get appfwFDIResponseCode
	'''
	@property
	def appfwFDIResponseCode(self) :
		try:
			return self._appfwFDIResponseCode
		except Exception as e :
			raise e
	'''
	set appfwFDIResponseCode
	'''
	@appfwFDIResponseCode.setter
	def appfwFDIResponseCode(self,appfwFDIResponseCode):
		try :
			if not isinstance(appfwFDIResponseCode,int):
				raise TypeError("appfwFDIResponseCode must be set to int value")
			self._appfwFDIResponseCode = appfwFDIResponseCode
		except Exception as e :
			raise e


	'''
	get appNameVserverLs
	'''
	@property
	def appNameVserverLs(self) :
		try:
			return self._appNameVserverLs
		except Exception as e :
			raise e
	'''
	set appNameVserverLs
	'''
	@appNameVserverLs.setter
	def appNameVserverLs(self,appNameVserverLs):
		try :
			if not isinstance(appNameVserverLs,str):
				raise TypeError("appNameVserverLs must be set to str value")
			self._appNameVserverLs = appNameVserverLs
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_fdi_transaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aa_fdi_transaction
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aa_fdi_transaction_responses, response, "aa_fdi_transaction_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aa_fdi_transaction_response_array
				i=0
				error = [aa_fdi_transaction() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aa_fdi_transaction_response_array
			i=0
			aa_fdi_transaction_objs = [aa_fdi_transaction() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_aa_fdi_transaction'):
					for props in obj._aa_fdi_transaction:
						result = service.payload_formatter.string_to_bulk_resource(aa_fdi_transaction_response,self.__class__.__name__,props)
						aa_fdi_transaction_objs[i] = result.aa_fdi_transaction
						i=i+1
			return aa_fdi_transaction_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aa_fdi_transaction,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aa_fdi_transaction_response(base_response):
	def __init__(self,length=1) :
		self.aa_fdi_transaction= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aa_fdi_transaction= [ aa_fdi_transaction() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aa_fdi_transaction_responses(base_response):
	def __init__(self,length=1) :
		self.aa_fdi_transaction_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aa_fdi_transaction_response_array = [ aa_fdi_transaction() for _ in range(length)]
