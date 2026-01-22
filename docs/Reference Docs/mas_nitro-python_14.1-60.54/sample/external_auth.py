#!/usr/bin/env python
'''
* Copyright (c) 2008-2025 Citrix Systems, Inc.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*    http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
'''
import sys
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.resource.config.mps.ldap_server import ldap_server
from massrc.com.citrix.mas.nitro.resource.config.mps.aaa_server import aaa_server
from massrc.com.citrix.mas.nitro.service.nitro_service import nitro_service


class external_auth :
    def __init__(self):
        ipaddress=""
        username=""
        password=""


    @staticmethod
    def main(cls, args_):
        if(len(args_) < 3):
            print("Usage: run.bat <ip> <username> <password>")
            return
        config = external_auth()
        config.ip = args_[1]
        config.username = args_[2]
        config.password = args_[3]


        try :
            client = nitro_service(config.ip,"http")
            #client.isCloud = True          #uncomment this line for NetScaler Console       
            client.set_credential(config.username,config.password) #For Service, username and password are treated as ID and secret
            client.timeout = 1800
            client.login()
            config.run_sample(client)
            client.logout()
        except nitro_exception as  e:
            print("Exception::errorcode="+str(e.errorcode)+",message="+ e.message)
        except Exception as e:
            print("Exception::message="+str(e.args))
        return



    def run_sample(self, client) :
        self.add_ldap_server(client)
        self.enable_aaa_server(client)

    def add_ldap_server(self,client) :
        try:
            my_ldap_server = ldap_server()
            my_ldap_server.name = "MyLDAPServer"
            my_ldap_server.ip_address = "10.140.50.5"
            my_ldap_server.type = "AD"
            my_ldap_server.sec_type = "PLAINTEXT"
            my_ldap_server.base_dn = "DC=citrite,DC=net"
            my_ldap_server.bind_dn = "arunkumara@citrite.net"
            my_ldap_server.bind_passwd = "OmSai@@(18"
            ldap_server.add(client, my_ldap_server)			
            print "--------------"
            print "Response Came :"
            print "--------------"
            print("add_ldap_server - Done")
        except nitro_exception as e :
            print "--------------"
            print "Exception :"
            print "--------------"
            print "ErrorCode : "+ str(e.errorcode)
            print "Message : " +e.message

        except Exception as e:
            raise e

    def enable_aaa_server(self,client) :
        try:
            my_aaa_server = aaa_server()
            my_aaa_server.primary_server_type = "LDAP"
            my_aaa_server.primary_server_name = "MyLDAPServer"
            my_aaa_server.fallback_local_authentication = True
            aaa_server.update(client, my_aaa_server)			
            print "--------------"
            print "Response Came :"
            print "--------------"
            print("enable_aaa_server - Done")
        except nitro_exception as e :
            print "--------------"
            print "Exception :"
            print "--------------"
            print "ErrorCode : "+ str(e.errorcode)
            print "Message : " +e.message

        except Exception as e:
            raise e

#
# Main thread of execution
#

if __name__ == '__main__':
    try:
        print len(sys.argv)
        if len(sys.argv) < 3:
            sys.exit()
        else:
            ipaddress=sys.argv[1]
            username=sys.argv[2]
            password=sys.argv[3]
            external_auth().main(external_auth(),sys.argv)



    except SystemExit:
        print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")



