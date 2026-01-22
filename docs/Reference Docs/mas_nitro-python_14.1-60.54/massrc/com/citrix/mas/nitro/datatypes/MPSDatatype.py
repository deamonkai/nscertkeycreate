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

from abc import ABCMeta, abstractmethod, abstractproperty
from massrc.com.citrix.mas.nitro.datatypes.MPSConstants import MPSConstants

class MPSDatatype:
	__metaclass__ = ABCMeta

	@abstractmethod
	def validate(self, operationType, _value,label):
		pass

	def getConstraintType(operationType):

		if operationType == "upload" :
			return MPSConstants.UPLOAD_CONSTRAINT
		if operationType == "modify" :
			return MPSConstants.MODIFY_CONSTRAINT
		if operationType == "get" :
			return MPSConstants.GET_CONSTRAINT
		if operationType == "delete" :
			return MPSConstants.DELETE_CONSTRAINT
		if operationType == "add" :
			return MPSConstants.ADD_CONSTRAINT
		if operationType == "custom" :
			return MPSConstants.CUSTOM_CONSTRAINT
		if operationType == "download" :
			return MPSConstants.DOWNLOAD_CONSTRAINT
		if operationType == "shutdown" :
			return MPSConstants.SHUTDOWN_CONSTRAINT
		if operationType == "reboot" :
			return MPSConstants.REBOOT_CONSTRAINT
		if operationType == "annotate" :
			return MPSConstants.ANNOTATE_CONSTRAINT
		if operationType == "mastools_restart" :
			return MPSConstants.MASTOOLS_RESTART_CONSTRAINT
		if operationType == "async_delete" :
			return MPSConstants.ASYNC_DELETE_CONSTRAINT
		if operationType == "allocate_license" :
			return MPSConstants.ALLOCATE_LICENSE_CONSTRAINT
		if operationType == "allocate_vcpu_license" :
			return MPSConstants.ALLOCATE_VCPU_LICENSE_CONSTRAINT
		if operationType == "add_device" :
			return MPSConstants.ADD_DEVICE_CONSTRAINT
		if operationType == "managementserviceincludinginstances" :
			return MPSConstants.MANAGEMENTSERVICEINCLUDINGINSTANCES_CONSTRAINT
		if operationType == "xenserver" :
			return MPSConstants.XENSERVER_CONSTRAINT
		if operationType == "managementserviceandxen" :
			return MPSConstants.MANAGEMENTSERVICEANDXEN_CONSTRAINT
		if operationType == "applianceincludinginstances" :
			return MPSConstants.APPLIANCEINCLUDINGINSTANCES_CONSTRAINT
		if operationType == "managementservice" :
			return MPSConstants.MANAGEMENTSERVICE_CONSTRAINT
		if operationType == "update_status" :
			return MPSConstants.UPDATE_STATUS_CONSTRAINT
		if operationType == "sync_secondary" :
			return MPSConstants.SYNC_SECONDARY_CONSTRAINT
		if operationType == "force_failover" :
			return MPSConstants.FORCE_FAILOVER_CONSTRAINT
		if operationType == "import_pre_upgrade_script_file" :
			return MPSConstants.IMPORT_PRE_UPGRADE_SCRIPT_FILE_CONSTRAINT
		if operationType == "import_post_upgrade_script_file" :
			return MPSConstants.IMPORT_POST_UPGRADE_SCRIPT_FILE_CONSTRAINT
		if operationType == "import_post_upgrade_pre_failover_script_file" :
			return MPSConstants.IMPORT_POST_UPGRADE_PRE_FAILOVER_SCRIPT_FILE_CONSTRAINT
		if operationType == "save" :
			return MPSConstants.SAVE_CONSTRAINT
		if operationType == "restart" :
			return MPSConstants.RESTART_CONSTRAINT
		if operationType == "generate_k8s_agent_yaml_file" :
			return MPSConstants.GENERATE_K8S_AGENT_YAML_FILE_CONSTRAINT
		if operationType == "devicebackup" :
			return MPSConstants.DEVICEBACKUP_CONSTRAINT
		if operationType == "devicerestore" :
			return MPSConstants.DEVICERESTORE_CONSTRAINT
		if operationType == "run" :
			return MPSConstants.RUN_CONSTRAINT
		if operationType == "devicetechsupport" :
			return MPSConstants.DEVICETECHSUPPORT_CONSTRAINT
		if operationType == "post" :
			return MPSConstants.POST_CONSTRAINT
		if operationType == "truncate" :
			return MPSConstants.TRUNCATE_CONSTRAINT
		if operationType == "guided" :
			return MPSConstants.GUIDED_CONSTRAINT
		if operationType == "acknowledged" :
			return MPSConstants.ACKNOWLEDGED_CONSTRAINT
		if operationType == "completed" :
			return MPSConstants.COMPLETED_CONSTRAINT
		if operationType == "generate" :
			return MPSConstants.GENERATE_CONSTRAINT
		if operationType == "unmanage" :
			return MPSConstants.UNMANAGE_CONSTRAINT
		if operationType == "manage" :
			return MPSConstants.MANAGE_CONSTRAINT
		if operationType == "enable" :
			return MPSConstants.ENABLE_CONSTRAINT
		if operationType == "poll" :
			return MPSConstants.POLL_CONSTRAINT
		if operationType == "disable" :
			return MPSConstants.DISABLE_CONSTRAINT
		if operationType == "renew_certificate" :
			return MPSConstants.RENEW_CERTIFICATE_CONSTRAINT
		if operationType == "create_certificate" :
			return MPSConstants.CREATE_CERTIFICATE_CONSTRAINT
		if operationType == "link" :
			return MPSConstants.LINK_CONSTRAINT
		if operationType == "unlink" :
			return MPSConstants.UNLINK_CONSTRAINT
		if operationType == "bind_cert" :
			return MPSConstants.BIND_CERT_CONSTRAINT
		if operationType == "list_entity_cert" :
			return MPSConstants.LIST_ENTITY_CERT_CONSTRAINT
		if operationType == "inventory" :
			return MPSConstants.INVENTORY_CONSTRAINT
		if operationType == "gen_csr" :
			return MPSConstants.GEN_CSR_CONSTRAINT
		if operationType == "get_policy_folders" :
			return MPSConstants.GET_POLICY_FOLDERS_CONSTRAINT
		if operationType == "form_cluster" :
			return MPSConstants.FORM_CLUSTER_CONSTRAINT
		if operationType == "join" :
			return MPSConstants.JOIN_CONSTRAINT
		if operationType == "modify_password" :
			return MPSConstants.MODIFY_PASSWORD_CONSTRAINT
		if operationType == "remove" :
			return MPSConstants.REMOVE_CONSTRAINT
		if operationType == "remove_node" :
			return MPSConstants.REMOVE_NODE_CONSTRAINT
		if operationType == "set" :
			return MPSConstants.SET_CONSTRAINT
		if operationType == "do_poll" :
			return MPSConstants.DO_POLL_CONSTRAINT
		if operationType == "download_conf" :
			return MPSConstants.DOWNLOAD_CONF_CONSTRAINT
		if operationType == "diff_table" :
			return MPSConstants.DIFF_TABLE_CONSTRAINT
		if operationType == "diff_table_report" :
			return MPSConstants.DIFF_TABLE_REPORT_CONSTRAINT
		if operationType == "gen_batch" :
			return MPSConstants.GEN_BATCH_CONSTRAINT
		if operationType == "do_diff" :
			return MPSConstants.DO_DIFF_CONSTRAINT
		if operationType == "preview" :
			return MPSConstants.PREVIEW_CONSTRAINT
		if operationType == "import_variables_file" :
			return MPSConstants.IMPORT_VARIABLES_FILE_CONSTRAINT
		if operationType == "create" :
			return MPSConstants.CREATE_CONSTRAINT
		if operationType == "clean_disk_space" :
			return MPSConstants.CLEAN_DISK_SPACE_CONSTRAINT
		if operationType == "check_disk_space" :
			return MPSConstants.CHECK_DISK_SPACE_CONSTRAINT
		return MPSConstants.INVALID_CONSTRAINT
