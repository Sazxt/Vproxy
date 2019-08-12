#/!usr/bin/python2
# Coding By SazXt
import requests as req
import json;import os as x
from requests.exceptions import ConnectionError
# warna <--->
p = '\x1b[0m'
m = '\x1b[91m'
i = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
class _eVolp_:
	def _bith_(self):
		self._VicE = lambda _SysMBol:"\x1b[92m[\x1b[91m+\x1b[92m] \x1b[0m"+_SysMBol
		self.proxy = "http://proxycheck.io/v2/{}?key=111111-222222-333333-444444&vpn=1&asn=1&node=1&time=1&inf=0&risk=1&port=1&seen=1&days=7&tag=msg"
		self.nigthe_ = str(raw_input(self._VicE("Proxy > ")))
	def _InProxy_(self):
		self._Liproxy = "https://www.proxy-list.download/api/v1/get?type=http&anon=elite&country={}"
		print "Ex : us,id,ru,my"
		self._AnsW_ = str(raw_input("\x1b[92m[\x1b[91m+\x1b[92m] \x1b[0m"+"country >> "))
	def _bunc_Checking(self):
		_SenDing = req.get(self.proxy.format(self.nigthe_))
		ic_ = json.loads(_SenDing.text)
		print self._VicE("status : "+str(ic_["status"]))
		print self._VicE("node : "+str(ic_["node"]))
		print self._VicE("city : "+str(ic_[self.nigthe_]["city"]))
		print self._VicE("latitude : "+str(ic_[self.nigthe_]["latitude"]))
		print self._VicE("longitude : "+str(ic_[self.nigthe_]["longitude"]))
		print self._VicE("proxy : "+str(ic_[self.nigthe_]["proxy"]))
		print self._VicE("asn : "+str(ic_[self.nigthe_]["asn"]))
		print self._VicE("isocode : "+str(ic_[self.nigthe_]["isocode"]))
		print self._VicE("type : "+str(ic_[self.nigthe_]["type"]))
		print self._VicE("provider : "+str(ic_[self.nigthe_]["provider"]))
		print self._VicE("risk : "+str(ic_[self.nigthe_]["risk"]))
		print self._VicE("country : "+str(ic_[self.nigthe_]["country"]))
		print self._VicE("port : "+str(ic_[self.nigthe_]["port"]))
		print self._VicE("last seen human : "+str(ic_[self.nigthe_]["last seen human"]))
		print self._VicE("last seen unix : "+str(ic_[self.nigthe_]["last seen unix"]))
		print self._VicE("query time : "+str(ic_["query time"]))
	def _ShowProxy (self):
		self.GetData = req.get(self._Liproxy.format(self._AnsW_)).text
		print self.GetData
def _main_():
	try:
		x.system("clear")
		print "\n         \x1b[34m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mAuthor   \x1b[37m: Sazxt\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mMy Team  \x1b[37m: Black Coder Crush\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mwhatsapp \x1b[37m: 083892081021\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mCodeName \x1b[37m: \x1b[36mVProxy \x1b[0;1mv1.1\n         \x1b[34m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n"
		print "    "+i+'\xe2\x96\x82'*40+p
		print "   "+i+"[ "+p+"1 "+i+"]"+p+" Proxy Checker "
		print "   "+i+"[ "+p+"2 "+i+"]"+p+" Proxy List By country"
		print "    "+i+'\xe2\x96\x82'*40+p
		_ShideIru = raw_input("[+] Chose >> ")
		if _ShideIru == "1":
			try:
				EvAol = _eVolp_()
				EvAol._bith_()
				EvAol._bunc_Checking()
			except KeyError:
				raw_input("Back > ")
				_main_()
		elif _ShideIru == "2":
			print p+'\xe2\x96\x82'*40
			SAte = _eVolp_()
			SAte._InProxy_()
			SAte._ShowProxy()
			print p+'\xe2\x96\x82'*40
			raw_input("Back >> ")
			_main_()
	except KeyboardInterrupt:
		exit("[+] Exit..")
	except EOFError:
		exit("[!] Exit ...")
	except ConnectionError:
		exit("[!] Enable Data ! ")
if __name__ == "__main__":
	_main_()