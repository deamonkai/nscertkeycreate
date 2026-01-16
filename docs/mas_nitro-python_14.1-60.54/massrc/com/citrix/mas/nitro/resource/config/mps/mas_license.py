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

class mas_license(base_resource):
	_analytics= ""
	_syslog= ""
	_tenantnslictype= ""
	_fips_bw_lic= ""
	_max_vips_val= ""
	_mhc_lic= ""
	_snmp_traps= ""
	_max_tp_vservers= ""
	_max_storage= ""
	_id= ""
	_fips_vcpu_lic= ""
	_lic_type= ""
	_cpx_lic= ""
	_forced_unlicense_timestamp= ""
	_upgrade_time= ""
	_automatic_unlicense_timestamp= ""
	_is_las_enabled= ""
	_rpt_sampletime= ""
	_vcpu_lic= ""
	_pooled_lic= ""
	_vpx_lic= ""
	_perf= ""
	_node_id= ""
	_max_vips= ""
	_adv_analytics= ""
	_ns_csvserver_managed_count= ""
	_vpx_rule_licensed_count= ""
	_total_allowed_tp_vservers= ""
	_get_consumed_db= ""
	_ns_vpnvserver_managed_count= ""
	_ns_crvserver_managed_count= ""
	_total_discovered_tp_vservers= ""
	_total_allowed_vips= ""
	_cpx_rule_max_limit= ""
	_cpx_rule_licensed_count= ""
	_total_licenses_consumed= ""
	_total_discovered_vips= ""
	_vpx_rule_max_limit= ""
	_consumed_db_storage= ""
	_auto_licensed_count= ""
	_ns_lbvserver_count= ""
	_ns_vpnvserver_count= ""
	_ns_authenticationvserver_managed_count= ""
	_ns_lbvserver_managed_count= ""
	_entitled_db_storage= ""
	_ns_crvserver_count= ""
	_ns_authenticationvserver_count= ""
	_ns_csvserver_count= ""
	_total_managed_vips= ""
	_total_managed_tp_vservers= ""
	_ns_gslbvserver_count= ""
	_manual_licensed_count= ""
	_ns_gslbvserver_managed_count= ""
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
			return "mas_license"
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
			return "mas_licenses"
		except Exception as e :
			raise e



	'''
	get Analytics, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def analytics(self) :
		try:
			return self._analytics
		except Exception as e :
			raise e
	'''
	set Analytics, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@analytics.setter
	def analytics(self,analytics):
		try :
			if not isinstance(analytics,int):
				raise TypeError("analytics must be set to int value")
			self._analytics = analytics
		except Exception as e :
			raise e


	'''
	get Syslog, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def syslog(self) :
		try:
			return self._syslog
		except Exception as e :
			raise e
	'''
	set Syslog, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@syslog.setter
	def syslog(self,syslog):
		try :
			if not isinstance(syslog,int):
				raise TypeError("syslog must be set to int value")
			self._syslog = syslog
		except Exception as e :
			raise e


	'''
	get Tenant NS license type
	'''
	@property
	def tenantnslictype(self) :
		try:
			return self._tenantnslictype
		except Exception as e :
			raise e
	'''
	set Tenant NS license type
	'''
	@tenantnslictype.setter
	def tenantnslictype(self,tenantnslictype):
		try :
			if not isinstance(tenantnslictype,str):
				raise TypeError("tenantnslictype must be set to str value")
			self._tenantnslictype = tenantnslictype
		except Exception as e :
			raise e


	'''
	get FIPS BW Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def fips_bw_lic(self) :
		try:
			return self._fips_bw_lic
		except Exception as e :
			raise e
	'''
	set FIPS BW Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@fips_bw_lic.setter
	def fips_bw_lic(self,fips_bw_lic):
		try :
			if not isinstance(fips_bw_lic,int):
				raise TypeError("fips_bw_lic must be set to int value")
			self._fips_bw_lic = fips_bw_lic
		except Exception as e :
			raise e


	'''
	get Maximum VIPs decoded
	'''
	@property
	def max_vips_val(self) :
		try:
			return self._max_vips_val
		except Exception as e :
			raise e
	'''
	set Maximum VIPs decoded
	'''
	@max_vips_val.setter
	def max_vips_val(self,max_vips_val):
		try :
			if not isinstance(max_vips_val,int):
				raise TypeError("max_vips_val must be set to int value")
			self._max_vips_val = max_vips_val
		except Exception as e :
			raise e


	'''
	get Multi Hybrid Cloud Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def mhc_lic(self) :
		try:
			return self._mhc_lic
		except Exception as e :
			raise e
	'''
	set Multi Hybrid Cloud Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@mhc_lic.setter
	def mhc_lic(self,mhc_lic):
		try :
			if not isinstance(mhc_lic,int):
				raise TypeError("mhc_lic must be set to int value")
			self._mhc_lic = mhc_lic
		except Exception as e :
			raise e


	'''
	get SNMP Traps, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def snmp_traps(self) :
		try:
			return self._snmp_traps
		except Exception as e :
			raise e
	'''
	set SNMP Traps, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@snmp_traps.setter
	def snmp_traps(self,snmp_traps):
		try :
			if not isinstance(snmp_traps,int):
				raise TypeError("snmp_traps must be set to int value")
			self._snmp_traps = snmp_traps
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
	get Max Storage
	'''
	@property
	def max_storage(self) :
		try:
			return self._max_storage
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
	get FIPS vCPU Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def fips_vcpu_lic(self) :
		try:
			return self._fips_vcpu_lic
		except Exception as e :
			raise e
	'''
	set FIPS vCPU Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@fips_vcpu_lic.setter
	def fips_vcpu_lic(self,fips_vcpu_lic):
		try :
			if not isinstance(fips_vcpu_lic,int):
				raise TypeError("fips_vcpu_lic must be set to int value")
			self._fips_vcpu_lic = fips_vcpu_lic
		except Exception as e :
			raise e


	'''
	get 0 = Trial Period, 1 = Licensed, 2 = Grace period, 3 = unlicensed
	'''
	@property
	def lic_type(self) :
		try:
			return self._lic_type
		except Exception as e :
			raise e
	'''
	set 0 = Trial Period, 1 = Licensed, 2 = Grace period, 3 = unlicensed
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
	get CPX Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def cpx_lic(self) :
		try:
			return self._cpx_lic
		except Exception as e :
			raise e
	'''
	set CPX Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@cpx_lic.setter
	def cpx_lic(self,cpx_lic):
		try :
			if not isinstance(cpx_lic,int):
				raise TypeError("cpx_lic must be set to int value")
			self._cpx_lic = cpx_lic
		except Exception as e :
			raise e


	'''
	get Timestamp of last force unlicense
	'''
	@property
	def forced_unlicense_timestamp(self) :
		try:
			return self._forced_unlicense_timestamp
		except Exception as e :
			raise e
	'''
	set Timestamp of last force unlicense
	'''
	@forced_unlicense_timestamp.setter
	def forced_unlicense_timestamp(self,forced_unlicense_timestamp):
		try :
			if not isinstance(forced_unlicense_timestamp,str):
				raise TypeError("forced_unlicense_timestamp must be set to str value")
			self._forced_unlicense_timestamp = forced_unlicense_timestamp
		except Exception as e :
			raise e


	'''
	get Last upgraded time when license reduced from 30 to 2
	'''
	@property
	def upgrade_time(self) :
		try:
			return self._upgrade_time
		except Exception as e :
			raise e
	'''
	set Last upgraded time when license reduced from 30 to 2
	'''
	@upgrade_time.setter
	def upgrade_time(self,upgrade_time):
		try :
			if not isinstance(upgrade_time,int):
				raise TypeError("upgrade_time must be set to int value")
			self._upgrade_time = upgrade_time
		except Exception as e :
			raise e


	'''
	get Timestamp of last automatic unlicense
	'''
	@property
	def automatic_unlicense_timestamp(self) :
		try:
			return self._automatic_unlicense_timestamp
		except Exception as e :
			raise e
	'''
	set Timestamp of last automatic unlicense
	'''
	@automatic_unlicense_timestamp.setter
	def automatic_unlicense_timestamp(self,automatic_unlicense_timestamp):
		try :
			if not isinstance(automatic_unlicense_timestamp,str):
				raise TypeError("automatic_unlicense_timestamp must be set to str value")
			self._automatic_unlicense_timestamp = automatic_unlicense_timestamp
		except Exception as e :
			raise e


	'''
	get is las enabled
	'''
	@property
	def is_las_enabled(self) :
		try:
			return self._is_las_enabled
		except Exception as e :
			raise e
	'''
	set is las enabled
	'''
	@is_las_enabled.setter
	def is_las_enabled(self,is_las_enabled):
		try :
			if not isinstance(is_las_enabled,bool):
				raise TypeError("is_las_enabled must be set to bool value")
			self._is_las_enabled = is_las_enabled
		except Exception as e :
			raise e


	'''
	get Time Stamp
	'''
	@property
	def rpt_sampletime(self) :
		try:
			return self._rpt_sampletime
		except Exception as e :
			raise e


	'''
	get vCPU Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def vcpu_lic(self) :
		try:
			return self._vcpu_lic
		except Exception as e :
			raise e
	'''
	set vCPU Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@vcpu_lic.setter
	def vcpu_lic(self,vcpu_lic):
		try :
			if not isinstance(vcpu_lic,int):
				raise TypeError("vcpu_lic must be set to int value")
			self._vcpu_lic = vcpu_lic
		except Exception as e :
			raise e


	'''
	get Pooled Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def pooled_lic(self) :
		try:
			return self._pooled_lic
		except Exception as e :
			raise e
	'''
	set Pooled Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@pooled_lic.setter
	def pooled_lic(self,pooled_lic):
		try :
			if not isinstance(pooled_lic,int):
				raise TypeError("pooled_lic must be set to int value")
			self._pooled_lic = pooled_lic
		except Exception as e :
			raise e


	'''
	get VPX Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def vpx_lic(self) :
		try:
			return self._vpx_lic
		except Exception as e :
			raise e
	'''
	set VPX Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@vpx_lic.setter
	def vpx_lic(self,vpx_lic):
		try :
			if not isinstance(vpx_lic,int):
				raise TypeError("vpx_lic must be set to int value")
			self._vpx_lic = vpx_lic
		except Exception as e :
			raise e


	'''
	get Perf, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def perf(self) :
		try:
			return self._perf
		except Exception as e :
			raise e
	'''
	set Perf, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@perf.setter
	def perf(self,perf):
		try :
			if not isinstance(perf,int):
				raise TypeError("perf must be set to int value")
			self._perf = perf
		except Exception as e :
			raise e


	'''
	get Node ID
	'''
	@property
	def node_id(self) :
		try:
			return self._node_id
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
	get Advanced Analytics, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def adv_analytics(self) :
		try:
			return self._adv_analytics
		except Exception as e :
			raise e
	'''
	set Advanced Analytics, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@adv_analytics.setter
	def adv_analytics(self,adv_analytics):
		try :
			if not isinstance(adv_analytics,int):
				raise TypeError("adv_analytics must be set to int value")
			self._adv_analytics = adv_analytics
		except Exception as e :
			raise e

	'''
	Total licensed ns csvservers in MAS
	'''
	@property
	def ns_csvserver_managed_count(self):
		try:
			return self._ns_csvserver_managed_count
		except Exception as e :
			raise e
	'''
	Total licensed ns csvservers in MAS
	'''
	@ns_csvserver_managed_count.setter
	def ns_csvserver_managed_count(self,ns_csvserver_managed_count):
		try :
			if not isinstance(ns_csvserver_managed_count,int):
				raise TypeError("ns_csvserver_managed_count must be set to int value")
			self._ns_csvserver_managed_count = ns_csvserver_managed_count
		except Exception as e :
			raise e

	'''
	Total vpx-rule based licensed vservers in MAS
	'''
	@property
	def vpx_rule_licensed_count(self):
		try:
			return self._vpx_rule_licensed_count
		except Exception as e :
			raise e
	'''
	Total vpx-rule based licensed vservers in MAS
	'''
	@vpx_rule_licensed_count.setter
	def vpx_rule_licensed_count(self,vpx_rule_licensed_count):
		try :
			if not isinstance(vpx_rule_licensed_count,int):
				raise TypeError("vpx_rule_licensed_count must be set to int value")
			self._vpx_rule_licensed_count = vpx_rule_licensed_count
		except Exception as e :
			raise e

	'''
	Total Allowed Third Party Vservres
	'''
	@property
	def total_allowed_tp_vservers(self):
		try:
			return self._total_allowed_tp_vservers
		except Exception as e :
			raise e

	'''
	Get Consumed DB
	'''
	@property
	def get_consumed_db(self):
		try:
			return self._get_consumed_db
		except Exception as e :
			raise e
	'''
	Get Consumed DB
	'''
	@get_consumed_db.setter
	def get_consumed_db(self,get_consumed_db):
		try :
			if not isinstance(get_consumed_db,bool):
				raise TypeError("get_consumed_db must be set to bool value")
			self._get_consumed_db = get_consumed_db
		except Exception as e :
			raise e

	'''
	Total licensed ns vpnvservers in MAS
	'''
	@property
	def ns_vpnvserver_managed_count(self):
		try:
			return self._ns_vpnvserver_managed_count
		except Exception as e :
			raise e
	'''
	Total licensed ns vpnvservers in MAS
	'''
	@ns_vpnvserver_managed_count.setter
	def ns_vpnvserver_managed_count(self,ns_vpnvserver_managed_count):
		try :
			if not isinstance(ns_vpnvserver_managed_count,int):
				raise TypeError("ns_vpnvserver_managed_count must be set to int value")
			self._ns_vpnvserver_managed_count = ns_vpnvserver_managed_count
		except Exception as e :
			raise e

	'''
	Total licensed ns crvservers in MAS
	'''
	@property
	def ns_crvserver_managed_count(self):
		try:
			return self._ns_crvserver_managed_count
		except Exception as e :
			raise e
	'''
	Total licensed ns crvservers in MAS
	'''
	@ns_crvserver_managed_count.setter
	def ns_crvserver_managed_count(self,ns_crvserver_managed_count):
		try :
			if not isinstance(ns_crvserver_managed_count,int):
				raise TypeError("ns_crvserver_managed_count must be set to int value")
			self._ns_crvserver_managed_count = ns_crvserver_managed_count
		except Exception as e :
			raise e

	'''
	Total discovered Third Party Vservres
	'''
	@property
	def total_discovered_tp_vservers(self):
		try:
			return self._total_discovered_tp_vservers
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
	CPX rule policy max limit in MAS
	'''
	@property
	def cpx_rule_max_limit(self):
		try:
			return self._cpx_rule_max_limit
		except Exception as e :
			raise e
	'''
	CPX rule policy max limit in MAS
	'''
	@cpx_rule_max_limit.setter
	def cpx_rule_max_limit(self,cpx_rule_max_limit):
		try :
			if not isinstance(cpx_rule_max_limit,int):
				raise TypeError("cpx_rule_max_limit must be set to int value")
			self._cpx_rule_max_limit = cpx_rule_max_limit
		except Exception as e :
			raise e

	'''
	Total cpx-rule based licensed vservers in MAS
	'''
	@property
	def cpx_rule_licensed_count(self):
		try:
			return self._cpx_rule_licensed_count
		except Exception as e :
			raise e
	'''
	Total cpx-rule based licensed vservers in MAS
	'''
	@cpx_rule_licensed_count.setter
	def cpx_rule_licensed_count(self,cpx_rule_licensed_count):
		try :
			if not isinstance(cpx_rule_licensed_count,int):
				raise TypeError("cpx_rule_licensed_count must be set to int value")
			self._cpx_rule_licensed_count = cpx_rule_licensed_count
		except Exception as e :
			raise e

	'''
	Total licneses consumed(excluding free licenses)
	'''
	@property
	def total_licenses_consumed(self):
		try:
			return self._total_licenses_consumed
		except Exception as e :
			raise e
	'''
	Total licneses consumed(excluding free licenses)
	'''
	@total_licenses_consumed.setter
	def total_licenses_consumed(self,total_licenses_consumed):
		try :
			if not isinstance(total_licenses_consumed,int):
				raise TypeError("total_licenses_consumed must be set to int value")
			self._total_licenses_consumed = total_licenses_consumed
		except Exception as e :
			raise e

	'''
	Total discovered VIPs
	'''
	@property
	def total_discovered_vips(self):
		try:
			return self._total_discovered_vips
		except Exception as e :
			raise e

	'''
	VPX rule policy max limit in MAS
	'''
	@property
	def vpx_rule_max_limit(self):
		try:
			return self._vpx_rule_max_limit
		except Exception as e :
			raise e
	'''
	VPX rule policy max limit in MAS
	'''
	@vpx_rule_max_limit.setter
	def vpx_rule_max_limit(self,vpx_rule_max_limit):
		try :
			if not isinstance(vpx_rule_max_limit,int):
				raise TypeError("vpx_rule_max_limit must be set to int value")
			self._vpx_rule_max_limit = vpx_rule_max_limit
		except Exception as e :
			raise e

	'''
	Consumed DB storage
	'''
	@property
	def consumed_db_storage(self):
		try:
			return self._consumed_db_storage
		except Exception as e :
			raise e

	'''
	Total auto licensed vservers in MAS
	'''
	@property
	def auto_licensed_count(self):
		try:
			return self._auto_licensed_count
		except Exception as e :
			raise e
	'''
	Total auto licensed vservers in MAS
	'''
	@auto_licensed_count.setter
	def auto_licensed_count(self,auto_licensed_count):
		try :
			if not isinstance(auto_licensed_count,int):
				raise TypeError("auto_licensed_count must be set to int value")
			self._auto_licensed_count = auto_licensed_count
		except Exception as e :
			raise e

	'''
	Total ns lbvservers in the system
	'''
	@property
	def ns_lbvserver_count(self):
		try:
			return self._ns_lbvserver_count
		except Exception as e :
			raise e
	'''
	Total ns lbvservers in the system
	'''
	@ns_lbvserver_count.setter
	def ns_lbvserver_count(self,ns_lbvserver_count):
		try :
			if not isinstance(ns_lbvserver_count,int):
				raise TypeError("ns_lbvserver_count must be set to int value")
			self._ns_lbvserver_count = ns_lbvserver_count
		except Exception as e :
			raise e

	'''
	Total ns vpnvservers in the system
	'''
	@property
	def ns_vpnvserver_count(self):
		try:
			return self._ns_vpnvserver_count
		except Exception as e :
			raise e
	'''
	Total ns vpnvservers in the system
	'''
	@ns_vpnvserver_count.setter
	def ns_vpnvserver_count(self,ns_vpnvserver_count):
		try :
			if not isinstance(ns_vpnvserver_count,int):
				raise TypeError("ns_vpnvserver_count must be set to int value")
			self._ns_vpnvserver_count = ns_vpnvserver_count
		except Exception as e :
			raise e

	'''
	Total licensed ns authenticationvservers in MAS
	'''
	@property
	def ns_authenticationvserver_managed_count(self):
		try:
			return self._ns_authenticationvserver_managed_count
		except Exception as e :
			raise e
	'''
	Total licensed ns authenticationvservers in MAS
	'''
	@ns_authenticationvserver_managed_count.setter
	def ns_authenticationvserver_managed_count(self,ns_authenticationvserver_managed_count):
		try :
			if not isinstance(ns_authenticationvserver_managed_count,int):
				raise TypeError("ns_authenticationvserver_managed_count must be set to int value")
			self._ns_authenticationvserver_managed_count = ns_authenticationvserver_managed_count
		except Exception as e :
			raise e

	'''
	Total licensed ns lbvservers in MAS
	'''
	@property
	def ns_lbvserver_managed_count(self):
		try:
			return self._ns_lbvserver_managed_count
		except Exception as e :
			raise e
	'''
	Total licensed ns lbvservers in MAS
	'''
	@ns_lbvserver_managed_count.setter
	def ns_lbvserver_managed_count(self,ns_lbvserver_managed_count):
		try :
			if not isinstance(ns_lbvserver_managed_count,int):
				raise TypeError("ns_lbvserver_managed_count must be set to int value")
			self._ns_lbvserver_managed_count = ns_lbvserver_managed_count
		except Exception as e :
			raise e

	'''
	Entitled DB storage in GB
	'''
	@property
	def entitled_db_storage(self):
		try:
			return self._entitled_db_storage
		except Exception as e :
			raise e

	'''
	Total ns crvservers in the system
	'''
	@property
	def ns_crvserver_count(self):
		try:
			return self._ns_crvserver_count
		except Exception as e :
			raise e
	'''
	Total ns crvservers in the system
	'''
	@ns_crvserver_count.setter
	def ns_crvserver_count(self,ns_crvserver_count):
		try :
			if not isinstance(ns_crvserver_count,int):
				raise TypeError("ns_crvserver_count must be set to int value")
			self._ns_crvserver_count = ns_crvserver_count
		except Exception as e :
			raise e

	'''
	Total ns authenticationvservers in the system
	'''
	@property
	def ns_authenticationvserver_count(self):
		try:
			return self._ns_authenticationvserver_count
		except Exception as e :
			raise e
	'''
	Total ns authenticationvservers in the system
	'''
	@ns_authenticationvserver_count.setter
	def ns_authenticationvserver_count(self,ns_authenticationvserver_count):
		try :
			if not isinstance(ns_authenticationvserver_count,int):
				raise TypeError("ns_authenticationvserver_count must be set to int value")
			self._ns_authenticationvserver_count = ns_authenticationvserver_count
		except Exception as e :
			raise e

	'''
	Total ns csvservers in the system
	'''
	@property
	def ns_csvserver_count(self):
		try:
			return self._ns_csvserver_count
		except Exception as e :
			raise e
	'''
	Total ns csvservers in the system
	'''
	@ns_csvserver_count.setter
	def ns_csvserver_count(self,ns_csvserver_count):
		try :
			if not isinstance(ns_csvserver_count,int):
				raise TypeError("ns_csvserver_count must be set to int value")
			self._ns_csvserver_count = ns_csvserver_count
		except Exception as e :
			raise e

	'''
	Total managed VIPs
	'''
	@property
	def total_managed_vips(self):
		try:
			return self._total_managed_vips
		except Exception as e :
			raise e

	'''
	Total managed Third Party Vservers
	'''
	@property
	def total_managed_tp_vservers(self):
		try:
			return self._total_managed_tp_vservers
		except Exception as e :
			raise e

	'''
	Total ns gslbvservers in the system
	'''
	@property
	def ns_gslbvserver_count(self):
		try:
			return self._ns_gslbvserver_count
		except Exception as e :
			raise e
	'''
	Total ns gslbvservers in the system
	'''
	@ns_gslbvserver_count.setter
	def ns_gslbvserver_count(self,ns_gslbvserver_count):
		try :
			if not isinstance(ns_gslbvserver_count,int):
				raise TypeError("ns_gslbvserver_count must be set to int value")
			self._ns_gslbvserver_count = ns_gslbvserver_count
		except Exception as e :
			raise e

	'''
	Total manually licensed vservers in MAS
	'''
	@property
	def manual_licensed_count(self):
		try:
			return self._manual_licensed_count
		except Exception as e :
			raise e
	'''
	Total manually licensed vservers in MAS
	'''
	@manual_licensed_count.setter
	def manual_licensed_count(self,manual_licensed_count):
		try :
			if not isinstance(manual_licensed_count,int):
				raise TypeError("manual_licensed_count must be set to int value")
			self._manual_licensed_count = manual_licensed_count
		except Exception as e :
			raise e

	'''
	Total licensed ns gslbvservers in MAS
	'''
	@property
	def ns_gslbvserver_managed_count(self):
		try:
			return self._ns_gslbvserver_managed_count
		except Exception as e :
			raise e
	'''
	Total licensed ns gslbvservers in MAS
	'''
	@ns_gslbvserver_managed_count.setter
	def ns_gslbvserver_managed_count(self,ns_gslbvserver_managed_count):
		try :
			if not isinstance(ns_gslbvserver_managed_count,int):
				raise TypeError("ns_gslbvserver_managed_count must be set to int value")
			self._ns_gslbvserver_managed_count = ns_gslbvserver_managed_count
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
	Use this operation to get NetScaler Console license information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mas_license_obj=mas_license()
				response = mas_license_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mas_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mas_license_obj = mas_license()
			option_ = options()
			option_._filter=filter_
			return mas_license_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mas_license resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mas_license_obj = mas_license()
			option_ = options()
			option_._count=True
			response = mas_license_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mas_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mas_license_obj = mas_license()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mas_license_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mas_license_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mas_license
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mas_license_responses, response, "mas_license_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mas_license_response_array
				i=0
				error = [mas_license() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mas_license_response_array
			i=0
			mas_license_objs = [mas_license() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mas_license'):
					for props in obj._mas_license:
						result = service.payload_formatter.string_to_bulk_resource(mas_license_response,self.__class__.__name__,props)
						mas_license_objs[i] = result.mas_license
						i=i+1
			return mas_license_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mas_license,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mas_license_response(base_response):
	def __init__(self,length=1) :
		self.mas_license= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mas_license= [ mas_license() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mas_license_responses(base_response):
	def __init__(self,length=1) :
		self.mas_license_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mas_license_response_array = [ mas_license() for _ in range(length)]
