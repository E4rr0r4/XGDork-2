# -*- coding: iso-8859-1 -*-

###### XGDork original code by ViraX (E4rr0r4)
import sys
from XGDlib import virax_search_engine, rand_dork, lilo_search_engine
from XGDtoolz import gen_dork
from termcolor import colored
import time
###### This program is a 'total' free software: you can redistribute it and/or modify
## GNU General Public License v3.0 ##


argc = len(sys.argv)
iargs = 1
error = 0
check = 0
help_p = 0
gd_on = 0
gdi = 0
addurls_on = 0
path_urls = ""
co_on = 0
mores_e = 0

data_dork = ""
data_npage = ""
data_debug = 0
data_SQLi = ""
data_outfile = ""
data_timeout = 0
data_addurls = []
data_modesqli = ""
data_oneurl = ""


if (argc == 1):
    print colored("!!! Error no args !!!", 'red')
    exit()
if (argc == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help")):
    help_p = 1

    print colored("\n [XGDork - Scanner]", 'green')
    print ("XGDork usage examples: \n")

    print ("* XGDork.py -d 'your_dork' -p 'page_number' -o 'out_file'")
    print ("    XGDork.py -d \".php?id=\" -p 2 -o urls_sqli \n")

    print ("* XGDork.py -d 'your_dork' -p 'page_number' -o 'out_file' --SQLi 'param' -t 'n'")
    print ("    XGDork.py -d \".php?id=\" -p 2 -o urls_sqli --SQLi = -t 20 \n")

    print ("* XGDork.py -d 'your_dork' -p 'page_number' -co 'out_file' --SQLi 'param' 'option' --timeout 'n'")
    print ("    XGDork.py -d \".php?id=\" -p 2 -co urls_sqli --SQLi = full --timeout 20 \n")

    print ("* XGDork.py --SQLi 'param' 'option' -d 'your_dork' -t 'n' -p 'page_number'")
    print ("    XGDork.py --SQLi id= full -d \".php?id=\" -t 20 -p 2 \n")

    print ("* XGDork.py -ad 'path' --SQLi 'param' 'option' --timeout 'n'")
    print ("    XGDork.py -ad \"urlsfile.txt\" --SQLi = full --timeout 10 \n")

    print ("and so on ... \n")    


    print ("  -d or --dork 'your_dork'    :add your dork, for search")
    print ("   e,g: -d .php?id= ")
    print ("    [OR]  ")
    print ("  -rd or --randork    :add a dork random (xdorks list), for search")
    print ("   e,g: -rd")
    print ("    [OR]  ")
    print ("  -gd or --gendork    :add a dork generated (gd_ multi-list), for search (caution, longer wait to get a working dork)")
    print ("   e,g: -gd \n")


    print ("  -p or --page 'page_number'    :add pages max number")
    print ("   e,g: -p 10 \n")

    print ("  -o or --outfile 'out_file'    :save results (new files)")
    print ("   e,g: -o urls_sqli")
    print ("    [OR]  ")
    print ("  -co or --concatoutfile 'out_file'    :save results (concatenate content, add urls without deleting content) [! the file must exist and have the same name !]")
    print ("   e,g: -co urls_sqli \n")

    print ("  --SQLi 'param' (stress url test only)")
    print ("   e,g: --SQLi id=     :if you only want to focus on this parameter")
    print ("    [OR]  ")
    print ("   e,g: --SQLi =      :all parameters found")
    print ("    [OR]  ")
    print ("  --SQLi 'param' 'option' (stress url test, force error, detect simple SECURITY and dump infos)")
    print ("   e,g: --SQLi id= full     :if you only want to focus on this parameter")
    print ("    [OR]  ")
    print ("   e,g: --SQLi = full      :all parameters found \n")


    print ("  -t or --timeout 'n'    :add timeout for requests/SQLparser(Reading) [! if you use --SQLi option you must add a timeout !]")
    print ("   e,g: -t 6 \n")

    print ("  --mores    :add startpage, searchx and bing for search")
    print ("   e,g: --mores \n")

    print ("  -ad or --addurls 'path'    :import your own urls list and test their vulnerability with Marvin [! you must add a timeout, SQLi and outfile options !]")
    print ("   e,g: -ad urlsfile.txt --SQLi = -t 6 -o urls_sqli \n")

    print ("  -u or --url 'your_url'    :import your own urls list and test their vulnerability with Marvin [! you must add a timeout and SQLi options !]")
    print ("   e,g: --url \"https://www.test.com/index.php?id=1\" --SQLi = full --timeout 10 \n")

    print colored(" [XGDump - Dumper Mod]", 'green')
    print ("please wait for the next update ! \n")

    print colored(" [XGDtoolz - simple Tools]", 'green')
    print ("please wait for the next update ! \n")


elif (argc == 2 and (sys.argv[1] != "-h" or sys.argv[1] != "--help")):
    print colored("!!! Error args !!!", 'red')
    exit()

while (argc > 2 and iargs < argc):
    if (sys.argv[iargs] == "-h" or sys.argv[iargs] == "--help"):
        print colored("!!! Error args 2 !!!", 'red')
        exit()

    if (sys.argv[iargs] == "-d" or sys.argv[iargs] == "--dork"):        
        data_dork = str(sys.argv[iargs+1])
        check += 1
    if (sys.argv[iargs] == "-p" or sys.argv[iargs] == "--npage"):
        data_npage = int(sys.argv[iargs+1])
        check += 1
    if (sys.argv[iargs] == "--debug"):
        data_debug = int(sys.argv[iargs+1])
    if (sys.argv[iargs] == "--SQLi"):
        data_SQLi = str(sys.argv[iargs+1])
        if (sys.argv[iargs+2] == "full" or sys.argv[iargs+2] == "f" or sys.argv[iargs+2] == "Full"):
            data_modesqli = str(sys.argv[iargs+2])
        if (data_SQLi == ""):
            data_SQLi = "="

    if (sys.argv[iargs] == "-o" or sys.argv[iargs] == "--outfile"):
        data_outfile = str(sys.argv[iargs+1])
    if (sys.argv[iargs] == "-co" or sys.argv[iargs] == "--concatoutfile"):
        data_outfile = str(sys.argv[iargs+1])
        co_on = 1

    if (sys.argv[iargs] == "--mores"):
        mores_e = 1

    if (sys.argv[iargs] == "-t" or sys.argv[iargs] == "--timeout"):
        data_timeout = int(sys.argv[iargs+1])

    if (sys.argv[iargs] == "-ad" or sys.argv[iargs] == "--addurls"):
        path_urls = str(sys.argv[iargs+1])
        addurls_on = 1

    if (sys.argv[iargs] == "-u" or sys.argv[iargs] == "--url"):
        data_oneurl = str(sys.argv[iargs+1])

    if (sys.argv[iargs] == "-rd" or sys.argv[iargs] == "--randork"):
        data_dork = rand_dork()
        check += 1
    if (sys.argv[iargs] == "-gd" or sys.argv[iargs] == "--gendork"):
        data_dork = gen_dork(0)
        check += 1
        gd_on = 1

    iargs += 1



if (path_urls != "" and addurls_on == 1):
    file_urls = open(path_urls, 'r')
    data_addurls = file_urls.readlines()
    file_urls.close()

    for element in data_addurls:
        element.replace('\n', '')



if (gd_on == 1):
    while (gd_on == 1 and lilo_search_engine(data_dork, data_npage, data_debug, 1) == "GD_E"):
        data_dork = gen_dork(0)
        gdi += 1



if (data_dork != "" and data_npage != 0 and check == 2 and help_p != 1 or addurls_on == 1 or data_oneurl != ""):

    print        ("\n\n")
    print colored("  __  ______ ____    42       _     ", 'blue')
    print colored("  \ \/ / ___|  _ \  ___  _ __| | __ ", 'blue')
    print colored("   \  / |  _| | | |/ _ \| '__| |/ / ", 'blue')
    print colored("   /  \ |_| | |_| | (_) | |  |   <  ", 'blue')
    print colored("  /_/\_\____|____/ \___/|_|  |_|\_\ \n", 'blue')
    print colored("--- ² ViraX Google Dork Scanner ² --- \n", 'cyan')

    print        ("  Original code by ViraX")
    print        ("  Version: [²] beta-07122021 FreeSoftware for Python 2.7")
    print        ("  Compatible Mobile - Android (NoRoot) - Termux \n")

    print colored("  Contributor(s)/Source(s)", 'cyan')
    print        ("  - SQLmap ('agents file') - https://github.com/sqlmapproject/ ")
    print        ("  - ")
    print        ("\n")

    print colored(" [!] DISCLAIMER: A simple 'naive' tool to find SQLi Vulnerable websites in the wild", 'green')
    print colored(" I am not responsible for illegal acts that you would do with this program !, only educational . [!] \n", 'green')

    print colored("\n [!] XGDork Start ["+str(time.ctime())+"] ... [!] \n", 'blue')
    if (addurls_on != 1):
        print colored("\n [*] Let's try with ["+data_dork+"] - good hunt ! ;)", 'cyan')
    else:
        print colored(" [*] Custom file (URLs) mode", 'red')
    virax_search_engine(data_dork, data_npage, data_debug, data_SQLi, data_outfile, data_timeout, data_addurls, co_on, mores_e, data_modesqli, data_oneurl)
    print colored("\n [!] XGDork End ["+str(time.ctime())+"] ... [!] \n", 'blue')
    exit()
elif (help_p == 1):
    exit()
else:
    print colored("Error args 3", 'red')
    exit()






