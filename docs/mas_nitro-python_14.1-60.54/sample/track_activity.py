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
import operator
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.resource.config.mps.inventory_status import inventory_status
from massrc.com.citrix.mas.nitro.resource.config.mps.activity_status import activity_status
from massrc.com.citrix.mas.nitro.service.nitro_service import nitro_service


class track_activity :
    def __init__(self):
        ipaddress=""
        username=""
        password=""


    @staticmethod
    def main(cls, args_):
        if(len(args_) < 3):
            print("Usage: run.bat <ip> <username> <password>")
            return
        config = track_activity()
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
        self.track_act(client,"aedbc3fc-5e10-44ae-a8fb-d3e24bc09cb1",["is_last","status"])

    def track_act(self,client,act_id,details_to_fetch) :
        '''
        This function fetches details about a particular activity from the NetScaler Console.
        Args:
            client: [mandatory] The nitro service object using which the operation will be performed
            act_id: [mandatory] [str] The ID of the activity to be tracked
            details_to_fetch: [mandatory] [list] A list of attributes about the activity that is needed. 
                The attributes are attributes of the activity_status.py SDK
                Example - ['is_last', 'status']
        Returns:
            return_dict: A dictionary where the keys are the attributes that need to be fetched, with corresponding values.
            Example - {'is_last': False, 'status': 'In Progress'}
        '''
        json_filter = "act_id:" + act_id
        
        # when you add a vpx, activity status and inventory status table gets populated
        # when you add an sdx, only activity status table gets populated but not inventory
        simplelist = inventory_status.get_filtered(client, json_filter)

        if not simplelist:
            #when you rediscover a vpx as well as an sdx, inventory status table gets populated
            simplelist = activity_status.get_filtered(client, json_filter)

        try:
            print "--------------"
            print "Response Came :"
            print "--------------"
            for detail in details_to_fetch:
                detail_value = (operator.attrgetter(detail)(simplelist[0]))
                print(detail +": " + detail_value)                                
            print("track activity - Done")
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
            track_activity().main(track_activity(),sys.argv)



    except SystemExit:
        print("Exception::Usage: Sample.py <directory path of Nitro.py> <nsip> <username> <password>")



