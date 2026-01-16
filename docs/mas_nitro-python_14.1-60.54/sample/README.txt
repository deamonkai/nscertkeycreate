This document provides description for each of the sample files on what they are used for.

* add_mps_ssl_certkey - is used to install SSL Certificate on NetScaler Console using the SSL Key and SSL certificate file.

* add_ntp_server - is used to add a new NTP server and enabling synchronization for the server using ntp_sync resource.ss

* add_snmp_view - is used to create a new snmp view on NetScaler Console. This requires two mandatory parameters namely, snmp view name and valid subtree.

* config_job - is used to create a Configuration Job on NetScaler Console. Particularly, the config job that is created is "show ns config". This job displays the configuration details of the specified NetScaler instance.

* external_auth - is used to add a new LDAP server for external authentication and enabling the server using aaa_server resource.

* get_inventory - is used to perform rediscovery for a device added to the NetScaler Console. It fetches the activity ID of the rediscovery process.

* get_license_file - is used to fetch the details of a license file. It displays file size and file last modified details of the given license file after fecthing. You can modify it to display any other details of the license file.

* get_ns_device_profile - is used to fetch details of a NetScaler device profile. It displays is_default and ID fields of the given NetScaler device profile.

* get_ns_ns_running_config - is used to fetch the running configuration details of a NetScaler instance.

* get_nssdx - is used to get the list of all NetScaler SDX instances managed by NetScaler Console. It diplays name and ID of each SDX instance.

* get_snmp_manager - is used to fetch the details of a particular snmp manager. It displays community and netmask details of the given snmp manager.

* get_snmp_trap - is used to fetch the details of a particular snmp trap. It displays community, version and user_name of the given snmp trap.

* get_stylebooks - is used to get the list of all stylebooks managed. It diplays name and source of each stylebooks.

* get_system_settings - is used to get system settings of the NetScaler Console. It displays svm_ns_comm, session_timeout and id of the NetScaler Console system.

* get_techsupport - is used to fetch the details of a tech support file. It displays mode, fil size and activity id of the given techsupport

* get_traceroute - is used to perform traceroute function for a device associated with the NetScaler Console. It dsiplays the device ip address and status of the traceroute operation for the given device.

* getcount_docker_host - is used to retrieve the count for the number of docker hosts that are associated with NetScaler Console.

* managed_device - is used to perform add, get and delete operation on devices managed by NetScaler Console. It adds a managed device by uploading csv file using add_device operation and deletes a managed device identified by its ID. 

* modify_ns_lbvserver - is used to enable/disable a given NetScaler Load Balancing Virtual Server through NetScaler Console.

* mps_data_center - is used to add and delete a datacenter with NetScaler Console. To add a datacenter, name and lat-long values are required and to delete a datacenter, name of the dataceneter is required.

* mps_group - is used to create a new user group on NetScaler Console. Every group has certain permissions and list of users belonging to that group. 

* mps_user - is used to update the details of a system user. It updates the password of a user named "nsroot" by first fetching the ID of the user.

* notifications - is used to set the notifications for certain event categories. Different actions can be used to indicate notifications such as send mail, send sms, send trap, run command, execute job, suppress action. The sample code is creating smtp and sms servers and corresponding profiles for setting those as the action for the events DeviceRebootState, DeviceDelete, DeviceChang, UserLogin.sss

* poll_ns_ssl_certkey_policy - is used to poll a NetScaler SSL Certkey policy and update the polling interval of the policy. It displays the poll interval of the policy. 

*reboot_ns - is used to reboot an instance identified by the given ID with NetScaler Console.

* system_session - is used to get the details of a user session with NetScaler Console. It displays the session ID and the duration after which the session expires after fetching.

* system_version - is used to get the details of NetScaler Console. It displays the product and build number of the NetScaler Console System. 

* track_activity - is used to fetch the details about a particular activity from the NetScaler Console.

* update_prune_policy - is used to modify a particular prune policy. It modifies the "days" field of the prune policy named "mps_policy_prune".

* upload_ns_ssl_cert - is used to upload a NetScaler SSL Certificate on NetScaler Console. It requires certificate filename and file location path.