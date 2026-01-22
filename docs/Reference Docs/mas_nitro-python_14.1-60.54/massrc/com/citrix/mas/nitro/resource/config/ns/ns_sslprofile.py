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
Configuration for NetScaler SSL Profile resource
'''

class ns_sslprofile(base_resource):
	_ns_ip_address= ""
	_prevsessionkeylifetime= ""
	_ersa= ""
	_dhcount= ""
	_skipclientcertpolicycheck= ""
	_sessionticketkeydata= ""
	_zerorttearlydata= ""
	_ssliocspcheck= ""
	_tls12= ""
	_dhekeyexchangewithpsk= ""
	_commonname= ""
	_redirectportrewrite= ""
	_clientauthuseboundcachain= ""
	_sessionticketlifetime= ""
	_sendclosenotify= ""
	_preload= ""
	_clientauth= ""
	_poll_time= ""
	_dhfile= ""
	_ssltriggertimeout= ""
	_tls13sessionticketsperauthcontext= ""
	_display_name= ""
	_partition_name= ""
	_dh= ""
	_ssl3= ""
	_snienable= ""
	_ssllogprofile= ""
	_serverauth= ""
	_insertionencoding= ""
	_cipherurl= ""
	_tls13= ""
	_includesubdomains= ""
	_hsts= ""
	_tls10= ""
	_sessionticket= ""
	_sslinterception= ""
	_clientcert= ""
	_sslireneg= ""
	_sessionticketkeyrefresh= ""
	_tls11= ""
	_strictsigdigestcheck= ""
	_sslredirect= ""
	_cipherredirect= ""
	_alpnprotocol= ""
	_sessreuse= ""
	_pushflag= ""
	_encrypttriggerpktcount= ""
	_pushenctriggertimeout= ""
	_ocspstapling= ""
	_snihttphostmatch= ""
	_sesstimeout= ""
	_allowextendedmastersecret= ""
	_ssl2= ""
	_pushenctrigger= ""
	_name= ""
	_quantumsize= ""
	_denysslreneg= ""
	_maxage= ""
	_dropreqwithnohostheader= ""
	_ersacount= ""
	_strictcachecks= ""
	_sessionkeylifetime= ""
	_id= ""
	_dhkeyexpsizelimit= ""
	_sslimaxsessperserver= ""
	_cleartextport= ""
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
			return "ns_sslprofile"
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
			return "ns_sslprofiles"
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
	get prevsessionkeylifetime
	'''
	@property
	def prevsessionkeylifetime(self) :
		try:
			return self._prevsessionkeylifetime
		except Exception as e :
			raise e
	'''
	set prevsessionkeylifetime
	'''
	@prevsessionkeylifetime.setter
	def prevsessionkeylifetime(self,prevsessionkeylifetime):
		try :
			if not isinstance(prevsessionkeylifetime,int):
				raise TypeError("prevsessionkeylifetime must be set to int value")
			self._prevsessionkeylifetime = prevsessionkeylifetime
		except Exception as e :
			raise e


	'''
	get ersa
	'''
	@property
	def ersa(self) :
		try:
			return self._ersa
		except Exception as e :
			raise e
	'''
	set ersa
	'''
	@ersa.setter
	def ersa(self,ersa):
		try :
			if not isinstance(ersa,bool):
				raise TypeError("ersa must be set to bool value")
			self._ersa = ersa
		except Exception as e :
			raise e


	'''
	get dhcount
	'''
	@property
	def dhcount(self) :
		try:
			return self._dhcount
		except Exception as e :
			raise e
	'''
	set dhcount
	'''
	@dhcount.setter
	def dhcount(self,dhcount):
		try :
			if not isinstance(dhcount,int):
				raise TypeError("dhcount must be set to int value")
			self._dhcount = dhcount
		except Exception as e :
			raise e


	'''
	get skipclientcertpolicycheck
	'''
	@property
	def skipclientcertpolicycheck(self) :
		try:
			return self._skipclientcertpolicycheck
		except Exception as e :
			raise e
	'''
	set skipclientcertpolicycheck
	'''
	@skipclientcertpolicycheck.setter
	def skipclientcertpolicycheck(self,skipclientcertpolicycheck):
		try :
			if not isinstance(skipclientcertpolicycheck,str):
				raise TypeError("skipclientcertpolicycheck must be set to str value")
			self._skipclientcertpolicycheck = skipclientcertpolicycheck
		except Exception as e :
			raise e


	'''
	get sessionticketkeydata
	'''
	@property
	def sessionticketkeydata(self) :
		try:
			return self._sessionticketkeydata
		except Exception as e :
			raise e
	'''
	set sessionticketkeydata
	'''
	@sessionticketkeydata.setter
	def sessionticketkeydata(self,sessionticketkeydata):
		try :
			if not isinstance(sessionticketkeydata,str):
				raise TypeError("sessionticketkeydata must be set to str value")
			self._sessionticketkeydata = sessionticketkeydata
		except Exception as e :
			raise e


	'''
	get zerorttearlydata
	'''
	@property
	def zerorttearlydata(self) :
		try:
			return self._zerorttearlydata
		except Exception as e :
			raise e
	'''
	set zerorttearlydata
	'''
	@zerorttearlydata.setter
	def zerorttearlydata(self,zerorttearlydata):
		try :
			if not isinstance(zerorttearlydata,str):
				raise TypeError("zerorttearlydata must be set to str value")
			self._zerorttearlydata = zerorttearlydata
		except Exception as e :
			raise e


	'''
	get ssliocspcheck
	'''
	@property
	def ssliocspcheck(self) :
		try:
			return self._ssliocspcheck
		except Exception as e :
			raise e
	'''
	set ssliocspcheck
	'''
	@ssliocspcheck.setter
	def ssliocspcheck(self,ssliocspcheck):
		try :
			if not isinstance(ssliocspcheck,str):
				raise TypeError("ssliocspcheck must be set to str value")
			self._ssliocspcheck = ssliocspcheck
		except Exception as e :
			raise e


	'''
	get tls12
	'''
	@property
	def tls12(self) :
		try:
			return self._tls12
		except Exception as e :
			raise e
	'''
	set tls12
	'''
	@tls12.setter
	def tls12(self,tls12):
		try :
			if not isinstance(tls12,bool):
				raise TypeError("tls12 must be set to bool value")
			self._tls12 = tls12
		except Exception as e :
			raise e


	'''
	get dhekeyexchangewithpsk
	'''
	@property
	def dhekeyexchangewithpsk(self) :
		try:
			return self._dhekeyexchangewithpsk
		except Exception as e :
			raise e
	'''
	set dhekeyexchangewithpsk
	'''
	@dhekeyexchangewithpsk.setter
	def dhekeyexchangewithpsk(self,dhekeyexchangewithpsk):
		try :
			if not isinstance(dhekeyexchangewithpsk,str):
				raise TypeError("dhekeyexchangewithpsk must be set to str value")
			self._dhekeyexchangewithpsk = dhekeyexchangewithpsk
		except Exception as e :
			raise e


	'''
	get commonname
	'''
	@property
	def commonname(self) :
		try:
			return self._commonname
		except Exception as e :
			raise e
	'''
	set commonname
	'''
	@commonname.setter
	def commonname(self,commonname):
		try :
			if not isinstance(commonname,str):
				raise TypeError("commonname must be set to str value")
			self._commonname = commonname
		except Exception as e :
			raise e


	'''
	get redirectportrewrite
	'''
	@property
	def redirectportrewrite(self) :
		try:
			return self._redirectportrewrite
		except Exception as e :
			raise e
	'''
	set redirectportrewrite
	'''
	@redirectportrewrite.setter
	def redirectportrewrite(self,redirectportrewrite):
		try :
			if not isinstance(redirectportrewrite,str):
				raise TypeError("redirectportrewrite must be set to str value")
			self._redirectportrewrite = redirectportrewrite
		except Exception as e :
			raise e


	'''
	get clientauthuseboundcachain
	'''
	@property
	def clientauthuseboundcachain(self) :
		try:
			return self._clientauthuseboundcachain
		except Exception as e :
			raise e
	'''
	set clientauthuseboundcachain
	'''
	@clientauthuseboundcachain.setter
	def clientauthuseboundcachain(self,clientauthuseboundcachain):
		try :
			if not isinstance(clientauthuseboundcachain,str):
				raise TypeError("clientauthuseboundcachain must be set to str value")
			self._clientauthuseboundcachain = clientauthuseboundcachain
		except Exception as e :
			raise e


	'''
	get sessionticketlifetime
	'''
	@property
	def sessionticketlifetime(self) :
		try:
			return self._sessionticketlifetime
		except Exception as e :
			raise e
	'''
	set sessionticketlifetime
	'''
	@sessionticketlifetime.setter
	def sessionticketlifetime(self,sessionticketlifetime):
		try :
			if not isinstance(sessionticketlifetime,int):
				raise TypeError("sessionticketlifetime must be set to int value")
			self._sessionticketlifetime = sessionticketlifetime
		except Exception as e :
			raise e


	'''
	get sendclosenotify
	'''
	@property
	def sendclosenotify(self) :
		try:
			return self._sendclosenotify
		except Exception as e :
			raise e
	'''
	set sendclosenotify
	'''
	@sendclosenotify.setter
	def sendclosenotify(self,sendclosenotify):
		try :
			if not isinstance(sendclosenotify,str):
				raise TypeError("sendclosenotify must be set to str value")
			self._sendclosenotify = sendclosenotify
		except Exception as e :
			raise e


	'''
	get preload
	'''
	@property
	def preload(self) :
		try:
			return self._preload
		except Exception as e :
			raise e
	'''
	set preload
	'''
	@preload.setter
	def preload(self,preload):
		try :
			if not isinstance(preload,str):
				raise TypeError("preload must be set to str value")
			self._preload = preload
		except Exception as e :
			raise e


	'''
	get clientauth
	'''
	@property
	def clientauth(self) :
		try:
			return self._clientauth
		except Exception as e :
			raise e
	'''
	set clientauth
	'''
	@clientauth.setter
	def clientauth(self,clientauth):
		try :
			if not isinstance(clientauth,str):
				raise TypeError("clientauth must be set to str value")
			self._clientauth = clientauth
		except Exception as e :
			raise e


	'''
	get Last Polling Time
	'''
	@property
	def poll_time(self) :
		try:
			return self._poll_time
		except Exception as e :
			raise e


	'''
	get dhfile
	'''
	@property
	def dhfile(self) :
		try:
			return self._dhfile
		except Exception as e :
			raise e
	'''
	set dhfile
	'''
	@dhfile.setter
	def dhfile(self,dhfile):
		try :
			if not isinstance(dhfile,str):
				raise TypeError("dhfile must be set to str value")
			self._dhfile = dhfile
		except Exception as e :
			raise e


	'''
	get ssltriggertimeout
	'''
	@property
	def ssltriggertimeout(self) :
		try:
			return self._ssltriggertimeout
		except Exception as e :
			raise e
	'''
	set ssltriggertimeout
	'''
	@ssltriggertimeout.setter
	def ssltriggertimeout(self,ssltriggertimeout):
		try :
			if not isinstance(ssltriggertimeout,int):
				raise TypeError("ssltriggertimeout must be set to int value")
			self._ssltriggertimeout = ssltriggertimeout
		except Exception as e :
			raise e


	'''
	get tls13sessionticketsperauthcontext
	'''
	@property
	def tls13sessionticketsperauthcontext(self) :
		try:
			return self._tls13sessionticketsperauthcontext
		except Exception as e :
			raise e
	'''
	set tls13sessionticketsperauthcontext
	'''
	@tls13sessionticketsperauthcontext.setter
	def tls13sessionticketsperauthcontext(self,tls13sessionticketsperauthcontext):
		try :
			if not isinstance(tls13sessionticketsperauthcontext,int):
				raise TypeError("tls13sessionticketsperauthcontext must be set to int value")
			self._tls13sessionticketsperauthcontext = tls13sessionticketsperauthcontext
		except Exception as e :
			raise e


	'''
	get Display Name
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e


	'''
	get Partition Name
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
		except Exception as e :
			raise e


	'''
	get dh
	'''
	@property
	def dh(self) :
		try:
			return self._dh
		except Exception as e :
			raise e
	'''
	set dh
	'''
	@dh.setter
	def dh(self,dh):
		try :
			if not isinstance(dh,bool):
				raise TypeError("dh must be set to bool value")
			self._dh = dh
		except Exception as e :
			raise e


	'''
	get ssl3
	'''
	@property
	def ssl3(self) :
		try:
			return self._ssl3
		except Exception as e :
			raise e
	'''
	set ssl3
	'''
	@ssl3.setter
	def ssl3(self,ssl3):
		try :
			if not isinstance(ssl3,bool):
				raise TypeError("ssl3 must be set to bool value")
			self._ssl3 = ssl3
		except Exception as e :
			raise e


	'''
	get snienable
	'''
	@property
	def snienable(self) :
		try:
			return self._snienable
		except Exception as e :
			raise e
	'''
	set snienable
	'''
	@snienable.setter
	def snienable(self,snienable):
		try :
			if not isinstance(snienable,str):
				raise TypeError("snienable must be set to str value")
			self._snienable = snienable
		except Exception as e :
			raise e


	'''
	get ssllogprofile
	'''
	@property
	def ssllogprofile(self) :
		try:
			return self._ssllogprofile
		except Exception as e :
			raise e
	'''
	set ssllogprofile
	'''
	@ssllogprofile.setter
	def ssllogprofile(self,ssllogprofile):
		try :
			if not isinstance(ssllogprofile,str):
				raise TypeError("ssllogprofile must be set to str value")
			self._ssllogprofile = ssllogprofile
		except Exception as e :
			raise e


	'''
	get serverauth
	'''
	@property
	def serverauth(self) :
		try:
			return self._serverauth
		except Exception as e :
			raise e
	'''
	set serverauth
	'''
	@serverauth.setter
	def serverauth(self,serverauth):
		try :
			if not isinstance(serverauth,str):
				raise TypeError("serverauth must be set to str value")
			self._serverauth = serverauth
		except Exception as e :
			raise e


	'''
	get insertionencoding
	'''
	@property
	def insertionencoding(self) :
		try:
			return self._insertionencoding
		except Exception as e :
			raise e
	'''
	set insertionencoding
	'''
	@insertionencoding.setter
	def insertionencoding(self,insertionencoding):
		try :
			if not isinstance(insertionencoding,str):
				raise TypeError("insertionencoding must be set to str value")
			self._insertionencoding = insertionencoding
		except Exception as e :
			raise e


	'''
	get cipherurl
	'''
	@property
	def cipherurl(self) :
		try:
			return self._cipherurl
		except Exception as e :
			raise e
	'''
	set cipherurl
	'''
	@cipherurl.setter
	def cipherurl(self,cipherurl):
		try :
			if not isinstance(cipherurl,str):
				raise TypeError("cipherurl must be set to str value")
			self._cipherurl = cipherurl
		except Exception as e :
			raise e


	'''
	get tls13
	'''
	@property
	def tls13(self) :
		try:
			return self._tls13
		except Exception as e :
			raise e
	'''
	set tls13
	'''
	@tls13.setter
	def tls13(self,tls13):
		try :
			if not isinstance(tls13,bool):
				raise TypeError("tls13 must be set to bool value")
			self._tls13 = tls13
		except Exception as e :
			raise e


	'''
	get includesubdomains
	'''
	@property
	def includesubdomains(self) :
		try:
			return self._includesubdomains
		except Exception as e :
			raise e
	'''
	set includesubdomains
	'''
	@includesubdomains.setter
	def includesubdomains(self,includesubdomains):
		try :
			if not isinstance(includesubdomains,bool):
				raise TypeError("includesubdomains must be set to bool value")
			self._includesubdomains = includesubdomains
		except Exception as e :
			raise e


	'''
	get hsts
	'''
	@property
	def hsts(self) :
		try:
			return self._hsts
		except Exception as e :
			raise e
	'''
	set hsts
	'''
	@hsts.setter
	def hsts(self,hsts):
		try :
			if not isinstance(hsts,bool):
				raise TypeError("hsts must be set to bool value")
			self._hsts = hsts
		except Exception as e :
			raise e


	'''
	get tls1
	'''
	@property
	def tls10(self) :
		try:
			return self._tls10
		except Exception as e :
			raise e
	'''
	set tls1
	'''
	@tls10.setter
	def tls10(self,tls10):
		try :
			if not isinstance(tls10,bool):
				raise TypeError("tls10 must be set to bool value")
			self._tls10 = tls10
		except Exception as e :
			raise e


	'''
	get sessionticket
	'''
	@property
	def sessionticket(self) :
		try:
			return self._sessionticket
		except Exception as e :
			raise e
	'''
	set sessionticket
	'''
	@sessionticket.setter
	def sessionticket(self,sessionticket):
		try :
			if not isinstance(sessionticket,str):
				raise TypeError("sessionticket must be set to str value")
			self._sessionticket = sessionticket
		except Exception as e :
			raise e


	'''
	get sslinterception
	'''
	@property
	def sslinterception(self) :
		try:
			return self._sslinterception
		except Exception as e :
			raise e
	'''
	set sslinterception
	'''
	@sslinterception.setter
	def sslinterception(self,sslinterception):
		try :
			if not isinstance(sslinterception,str):
				raise TypeError("sslinterception must be set to str value")
			self._sslinterception = sslinterception
		except Exception as e :
			raise e


	'''
	get clientcert
	'''
	@property
	def clientcert(self) :
		try:
			return self._clientcert
		except Exception as e :
			raise e
	'''
	set clientcert
	'''
	@clientcert.setter
	def clientcert(self,clientcert):
		try :
			if not isinstance(clientcert,str):
				raise TypeError("clientcert must be set to str value")
			self._clientcert = clientcert
		except Exception as e :
			raise e


	'''
	get sslireneg
	'''
	@property
	def sslireneg(self) :
		try:
			return self._sslireneg
		except Exception as e :
			raise e
	'''
	set sslireneg
	'''
	@sslireneg.setter
	def sslireneg(self,sslireneg):
		try :
			if not isinstance(sslireneg,str):
				raise TypeError("sslireneg must be set to str value")
			self._sslireneg = sslireneg
		except Exception as e :
			raise e


	'''
	get sessionticketkeyrefresh
	'''
	@property
	def sessionticketkeyrefresh(self) :
		try:
			return self._sessionticketkeyrefresh
		except Exception as e :
			raise e
	'''
	set sessionticketkeyrefresh
	'''
	@sessionticketkeyrefresh.setter
	def sessionticketkeyrefresh(self,sessionticketkeyrefresh):
		try :
			if not isinstance(sessionticketkeyrefresh,str):
				raise TypeError("sessionticketkeyrefresh must be set to str value")
			self._sessionticketkeyrefresh = sessionticketkeyrefresh
		except Exception as e :
			raise e


	'''
	get tls11
	'''
	@property
	def tls11(self) :
		try:
			return self._tls11
		except Exception as e :
			raise e
	'''
	set tls11
	'''
	@tls11.setter
	def tls11(self,tls11):
		try :
			if not isinstance(tls11,bool):
				raise TypeError("tls11 must be set to bool value")
			self._tls11 = tls11
		except Exception as e :
			raise e


	'''
	get strictsigdigestcheck
	'''
	@property
	def strictsigdigestcheck(self) :
		try:
			return self._strictsigdigestcheck
		except Exception as e :
			raise e
	'''
	set strictsigdigestcheck
	'''
	@strictsigdigestcheck.setter
	def strictsigdigestcheck(self,strictsigdigestcheck):
		try :
			if not isinstance(strictsigdigestcheck,bool):
				raise TypeError("strictsigdigestcheck must be set to bool value")
			self._strictsigdigestcheck = strictsigdigestcheck
		except Exception as e :
			raise e


	'''
	get sslredirect
	'''
	@property
	def sslredirect(self) :
		try:
			return self._sslredirect
		except Exception as e :
			raise e
	'''
	set sslredirect
	'''
	@sslredirect.setter
	def sslredirect(self,sslredirect):
		try :
			if not isinstance(sslredirect,str):
				raise TypeError("sslredirect must be set to str value")
			self._sslredirect = sslredirect
		except Exception as e :
			raise e


	'''
	get cipherredirect
	'''
	@property
	def cipherredirect(self) :
		try:
			return self._cipherredirect
		except Exception as e :
			raise e
	'''
	set cipherredirect
	'''
	@cipherredirect.setter
	def cipherredirect(self,cipherredirect):
		try :
			if not isinstance(cipherredirect,str):
				raise TypeError("cipherredirect must be set to str value")
			self._cipherredirect = cipherredirect
		except Exception as e :
			raise e


	'''
	get alpnprotocol
	'''
	@property
	def alpnprotocol(self) :
		try:
			return self._alpnprotocol
		except Exception as e :
			raise e
	'''
	set alpnprotocol
	'''
	@alpnprotocol.setter
	def alpnprotocol(self,alpnprotocol):
		try :
			if not isinstance(alpnprotocol,str):
				raise TypeError("alpnprotocol must be set to str value")
			self._alpnprotocol = alpnprotocol
		except Exception as e :
			raise e


	'''
	get sessreuse
	'''
	@property
	def sessreuse(self) :
		try:
			return self._sessreuse
		except Exception as e :
			raise e
	'''
	set sessreuse
	'''
	@sessreuse.setter
	def sessreuse(self,sessreuse):
		try :
			if not isinstance(sessreuse,str):
				raise TypeError("sessreuse must be set to str value")
			self._sessreuse = sessreuse
		except Exception as e :
			raise e


	'''
	get pushflag
	'''
	@property
	def pushflag(self) :
		try:
			return self._pushflag
		except Exception as e :
			raise e
	'''
	set pushflag
	'''
	@pushflag.setter
	def pushflag(self,pushflag):
		try :
			if not isinstance(pushflag,int):
				raise TypeError("pushflag must be set to int value")
			self._pushflag = pushflag
		except Exception as e :
			raise e


	'''
	get encrypttriggerpktcount
	'''
	@property
	def encrypttriggerpktcount(self) :
		try:
			return self._encrypttriggerpktcount
		except Exception as e :
			raise e
	'''
	set encrypttriggerpktcount
	'''
	@encrypttriggerpktcount.setter
	def encrypttriggerpktcount(self,encrypttriggerpktcount):
		try :
			if not isinstance(encrypttriggerpktcount,int):
				raise TypeError("encrypttriggerpktcount must be set to int value")
			self._encrypttriggerpktcount = encrypttriggerpktcount
		except Exception as e :
			raise e


	'''
	get pushenctriggertimeout
	'''
	@property
	def pushenctriggertimeout(self) :
		try:
			return self._pushenctriggertimeout
		except Exception as e :
			raise e
	'''
	set pushenctriggertimeout
	'''
	@pushenctriggertimeout.setter
	def pushenctriggertimeout(self,pushenctriggertimeout):
		try :
			if not isinstance(pushenctriggertimeout,int):
				raise TypeError("pushenctriggertimeout must be set to int value")
			self._pushenctriggertimeout = pushenctriggertimeout
		except Exception as e :
			raise e


	'''
	get ocspstapling
	'''
	@property
	def ocspstapling(self) :
		try:
			return self._ocspstapling
		except Exception as e :
			raise e
	'''
	set ocspstapling
	'''
	@ocspstapling.setter
	def ocspstapling(self,ocspstapling):
		try :
			if not isinstance(ocspstapling,str):
				raise TypeError("ocspstapling must be set to str value")
			self._ocspstapling = ocspstapling
		except Exception as e :
			raise e


	'''
	get snihttphostmatch
	'''
	@property
	def snihttphostmatch(self) :
		try:
			return self._snihttphostmatch
		except Exception as e :
			raise e
	'''
	set snihttphostmatch
	'''
	@snihttphostmatch.setter
	def snihttphostmatch(self,snihttphostmatch):
		try :
			if not isinstance(snihttphostmatch,str):
				raise TypeError("snihttphostmatch must be set to str value")
			self._snihttphostmatch = snihttphostmatch
		except Exception as e :
			raise e


	'''
	get sesstimeout
	'''
	@property
	def sesstimeout(self) :
		try:
			return self._sesstimeout
		except Exception as e :
			raise e
	'''
	set sesstimeout
	'''
	@sesstimeout.setter
	def sesstimeout(self,sesstimeout):
		try :
			if not isinstance(sesstimeout,int):
				raise TypeError("sesstimeout must be set to int value")
			self._sesstimeout = sesstimeout
		except Exception as e :
			raise e


	'''
	get allowextendedmastersecret
	'''
	@property
	def allowextendedmastersecret(self) :
		try:
			return self._allowextendedmastersecret
		except Exception as e :
			raise e
	'''
	set allowextendedmastersecret
	'''
	@allowextendedmastersecret.setter
	def allowextendedmastersecret(self,allowextendedmastersecret):
		try :
			if not isinstance(allowextendedmastersecret,str):
				raise TypeError("allowextendedmastersecret must be set to str value")
			self._allowextendedmastersecret = allowextendedmastersecret
		except Exception as e :
			raise e


	'''
	get ssl2
	'''
	@property
	def ssl2(self) :
		try:
			return self._ssl2
		except Exception as e :
			raise e
	'''
	set ssl2
	'''
	@ssl2.setter
	def ssl2(self,ssl2):
		try :
			if not isinstance(ssl2,bool):
				raise TypeError("ssl2 must be set to bool value")
			self._ssl2 = ssl2
		except Exception as e :
			raise e


	'''
	get pushenctrigger
	'''
	@property
	def pushenctrigger(self) :
		try:
			return self._pushenctrigger
		except Exception as e :
			raise e
	'''
	set pushenctrigger
	'''
	@pushenctrigger.setter
	def pushenctrigger(self,pushenctrigger):
		try :
			if not isinstance(pushenctrigger,str):
				raise TypeError("pushenctrigger must be set to str value")
			self._pushenctrigger = pushenctrigger
		except Exception as e :
			raise e


	'''
	get Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get quantumsize
	'''
	@property
	def quantumsize(self) :
		try:
			return self._quantumsize
		except Exception as e :
			raise e
	'''
	set quantumsize
	'''
	@quantumsize.setter
	def quantumsize(self,quantumsize):
		try :
			if not isinstance(quantumsize,int):
				raise TypeError("quantumsize must be set to int value")
			self._quantumsize = quantumsize
		except Exception as e :
			raise e


	'''
	get denysslreneg
	'''
	@property
	def denysslreneg(self) :
		try:
			return self._denysslreneg
		except Exception as e :
			raise e
	'''
	set denysslreneg
	'''
	@denysslreneg.setter
	def denysslreneg(self,denysslreneg):
		try :
			if not isinstance(denysslreneg,str):
				raise TypeError("denysslreneg must be set to str value")
			self._denysslreneg = denysslreneg
		except Exception as e :
			raise e


	'''
	get maxage
	'''
	@property
	def maxage(self) :
		try:
			return self._maxage
		except Exception as e :
			raise e
	'''
	set maxage
	'''
	@maxage.setter
	def maxage(self,maxage):
		try :
			if not isinstance(maxage,int):
				raise TypeError("maxage must be set to int value")
			self._maxage = maxage
		except Exception as e :
			raise e


	'''
	get dropreqwithnohostheader
	'''
	@property
	def dropreqwithnohostheader(self) :
		try:
			return self._dropreqwithnohostheader
		except Exception as e :
			raise e
	'''
	set dropreqwithnohostheader
	'''
	@dropreqwithnohostheader.setter
	def dropreqwithnohostheader(self,dropreqwithnohostheader):
		try :
			if not isinstance(dropreqwithnohostheader,str):
				raise TypeError("dropreqwithnohostheader must be set to str value")
			self._dropreqwithnohostheader = dropreqwithnohostheader
		except Exception as e :
			raise e


	'''
	get ersacount
	'''
	@property
	def ersacount(self) :
		try:
			return self._ersacount
		except Exception as e :
			raise e
	'''
	set ersacount
	'''
	@ersacount.setter
	def ersacount(self,ersacount):
		try :
			if not isinstance(ersacount,int):
				raise TypeError("ersacount must be set to int value")
			self._ersacount = ersacount
		except Exception as e :
			raise e


	'''
	get strictcachecks
	'''
	@property
	def strictcachecks(self) :
		try:
			return self._strictcachecks
		except Exception as e :
			raise e
	'''
	set strictcachecks
	'''
	@strictcachecks.setter
	def strictcachecks(self,strictcachecks):
		try :
			if not isinstance(strictcachecks,str):
				raise TypeError("strictcachecks must be set to str value")
			self._strictcachecks = strictcachecks
		except Exception as e :
			raise e


	'''
	get sessionkeylifetime
	'''
	@property
	def sessionkeylifetime(self) :
		try:
			return self._sessionkeylifetime
		except Exception as e :
			raise e
	'''
	set sessionkeylifetime
	'''
	@sessionkeylifetime.setter
	def sessionkeylifetime(self,sessionkeylifetime):
		try :
			if not isinstance(sessionkeylifetime,int):
				raise TypeError("sessionkeylifetime must be set to int value")
			self._sessionkeylifetime = sessionkeylifetime
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
	get dhkeyexpsizelimit
	'''
	@property
	def dhkeyexpsizelimit(self) :
		try:
			return self._dhkeyexpsizelimit
		except Exception as e :
			raise e
	'''
	set dhkeyexpsizelimit
	'''
	@dhkeyexpsizelimit.setter
	def dhkeyexpsizelimit(self,dhkeyexpsizelimit):
		try :
			if not isinstance(dhkeyexpsizelimit,str):
				raise TypeError("dhkeyexpsizelimit must be set to str value")
			self._dhkeyexpsizelimit = dhkeyexpsizelimit
		except Exception as e :
			raise e


	'''
	get sslimaxsessperserver
	'''
	@property
	def sslimaxsessperserver(self) :
		try:
			return self._sslimaxsessperserver
		except Exception as e :
			raise e
	'''
	set sslimaxsessperserver
	'''
	@sslimaxsessperserver.setter
	def sslimaxsessperserver(self,sslimaxsessperserver):
		try :
			if not isinstance(sslimaxsessperserver,int):
				raise TypeError("sslimaxsessperserver must be set to int value")
			self._sslimaxsessperserver = sslimaxsessperserver
		except Exception as e :
			raise e


	'''
	get cleartextport
	'''
	@property
	def cleartextport(self) :
		try:
			return self._cleartextport
		except Exception as e :
			raise e
	'''
	set cleartextport
	'''
	@cleartextport.setter
	def cleartextport(self,cleartextport):
		try :
			if not isinstance(cleartextport,str):
				raise TypeError("cleartextport must be set to str value")
			self._cleartextport = cleartextport
		except Exception as e :
			raise e

	'''
	Use this operation to get profile Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_sslprofile_obj=ns_sslprofile()
				response = ns_sslprofile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_sslprofile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_sslprofile_obj = ns_sslprofile()
			option_ = options()
			option_._filter=filter_
			return ns_sslprofile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_sslprofile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_sslprofile_obj = ns_sslprofile()
			option_ = options()
			option_._count=True
			response = ns_sslprofile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_sslprofile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_sslprofile_obj = ns_sslprofile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_sslprofile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_sslprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_sslprofile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_sslprofile_responses, response, "ns_sslprofile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_sslprofile_response_array
				i=0
				error = [ns_sslprofile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_sslprofile_response_array
			i=0
			ns_sslprofile_objs = [ns_sslprofile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_sslprofile'):
					for props in obj._ns_sslprofile:
						result = service.payload_formatter.string_to_bulk_resource(ns_sslprofile_response,self.__class__.__name__,props)
						ns_sslprofile_objs[i] = result.ns_sslprofile
						i=i+1
			return ns_sslprofile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_sslprofile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_sslprofile_response(base_response):
	def __init__(self,length=1) :
		self.ns_sslprofile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_sslprofile= [ ns_sslprofile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_sslprofile_responses(base_response):
	def __init__(self,length=1) :
		self.ns_sslprofile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_sslprofile_response_array = [ ns_sslprofile() for _ in range(length)]
