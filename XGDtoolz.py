
###### XGDork original code by ViraX (E4rr0r4)
from random import randint
###### This program is a 'total' free software: you can redistribute it and/or modify
## GNU General Public License v3.0 ##



def     gen_dork (out):
    
    d_npage = ""
    d_ext = ""
    d_param = ""
    d_data = ""
    d_keyword = ""
    size = 0

    nfile = file
    nfile = open("gd_namespage.txt", 'r')
    size = len(nfile.readlines())-1
    nfile.close
    nfile = open("gd_namespage.txt",'r')
    d_npage = str(nfile.readlines()[randint(0,size)].replace('\n',''))
    nfile.close()

    nfile = file
    nfile = open("gd_ext.txt", 'r')
    size = len(nfile.readlines())-1
    nfile.close()
    nfile = open("gd_ext.txt", 'r')
    d_ext = str(nfile.readlines()[randint(0,size)].replace('\n', ''))
    nfile.close()

    nfile = file
    nfile = open("gd_params.txt",'r')
    size = len(nfile.readlines())-1
    nfile.close()
    nfile = open("gd_params.txt", 'r')
    d_param = str(nfile.readlines()[randint(0,size)].replace('\n', ''))
    nfile.close()

    nfile = file
    nfile = open("gd_data.txt", 'r')
    size = len(nfile.readlines())-1
    nfile.close()
    nfile = open("gd_data.txt", 'r')
    d_data = str(nfile.readlines()[randint(0,size)].replace('\n', ''))
    nfile.close()

    #nfile = file
    #nfile = open("gd_keywords.txt", 'r')
    #size = len(nfile.readlines())-1
    #nfile.close()
    #nfile = open("gd_keywords.txt", 'r')
    #d_keyword = str(nfile.readlines()[randint(0,size)].replace('\n', ''))
    #nfile.close()

    gdork = str("inurl:"+d_npage+d_ext+d_param)#"+d_keyword)

    if (out == 1):
        print gdork

    return gdork

