# -*- coding: iso-8859-1 -*-

######
import sys
from XGDlib import virax_search_engine, rand_dork
from termcolor import colored
import time
######


argc = len(sys.argv)
iargs = 1
error = 0
check = 0
help_p = 0

data_dork = ""
data_npage = ""
data_debug = 0
data_SQLi = ""
data_outfile = ""
data_timeout = 0


if (argc == 1):
    print colored("!!! Error no args !!!", 'red')
    exit()
if (argc == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help")):
    help_p = 1

    print colored("\n [XGDork - Scanner]", 'green')
    print (" USE : XGDork.py -d 'your_dork' -p 'page_number' -o 'out_file' \n")

    print ("  -d or --dork 'your_dork'    :add your dork, for search")
    print ("   e,g: -d .php?id= ")
    print ("    [OR]  ")
    print ("  -rd or --randork    :add a dork generated, for search")
    print ("   e,g: -rd \n")

    print ("  -p or --page 'page_number'    :add pages max number")
    print ("   e,g: -p 10 \n")

    print ("  -o or --outfile 'out_file'    :save results")
    print ("   e,g: -o urls_sqli \n")

    print ("  --SQLi    :stress url test, force error, detect simple SECURITY and dump infos")
    print ("   e,g: --SQLi id=      :if you only want to focus on this parameter")
    print ("    [OR]  ")
    print ("   e,g: --SQLi =      :all parameters found \n")

    print ("  -t or --timeout n    :add timeout for requests/SQLparser(Reading) [! if you use SQLi option you must add a timeout !]")
    print ("   e,g: -t 5 \n")

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
        if (data_SQLi == ""):
            data_SQLi = "="
    if (sys.argv[iargs] == "-o" or sys.argv[iargs] == "--outfile"):
        data_outfile = str(sys.argv[iargs+1])
    if (sys.argv[iargs] == "-t" or sys.argv[iargs] == "--timeout"):
        data_timeout = int(sys.argv[iargs+1])


    if (sys.argv[iargs] == "-rd" or sys.argv[iargs] == "--randork"):
        data_dork = rand_dork()
        check += 1        


    iargs += 1



if (data_dork != "" and data_npage != 0 and check == 2 and help_p != 1):

    print        ("\n\n")
    print colored("  __  ______ ____    42       _     ", 'blue')
    print colored("  \ \/ / ___|  _ \  ___  _ __| | __ ", 'blue')
    print colored("   \  / |  _| | | |/ _ \| '__| |/ / ", 'blue')
    print colored("   /  \ |_| | |_| | (_) | |  |   <  ", 'blue')
    print colored("  /_/\_\____|____/ \___/|_|  |_|\_\ \n", 'blue')
    print colored("--- ² ViraX Google Dork Scanner ² --- \n", 'cyan')

    print        ("  Original code by ViraX")
    print        ("  Version: [²] beta-20112021 FreeSoftware for Python 2.7")
    print        ("  Compatible Mobile - Android (NoRoot) - Termux \n")

    print colored("  Contributor(s)/Source(s)", 'cyan')
    print        ("  - SQLmap ('agents file') - https://github.com/sqlmapproject/ ")
    print        ("  - ")
    print        ("\n")

    print colored(" [!] DISCLAIMER: A simple 'naive' tool to find SQLi Vulnerable websites in the wild", 'green')
    print colored(" I am not responsible for illegal acts that you would do with this program !, only educational . [!] \n", 'green')


    print colored("\n [!] XGDork Start ["+str(time.ctime())+"] ... [!] \n", 'blue')
    print colored("\n [*] Let's try with ["+data_dork+"] - good hunt ! ;)", 'cyan')
    virax_search_engine(data_dork, data_npage, data_debug, data_SQLi, data_outfile, data_timeout)
    print colored("\n [!] XGDork End ["+str(time.ctime())+"] ... [!] \n", 'blue')
    exit()
elif (help_p == 1):
    exit()
else:
    print colored("Error args 3", 'red')
    exit()






