# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:03:49 2024

@author: Burhan

    Windows İşletim Sisteminde Bilgisayar bilgilerini öğrenme

"""

import platform

b = platform.uname()
print(b)
print("""
    System   : {} {}
    Node     : {}
    Release  : {}
    Version  : {}
""".format(
    b[0], b[4],  # sysname
    b[1],   # Nodename 
    b[2], #Relase
    b[3])) #Version