# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import


from ..RubisOSInit import init

# Main Function

def RubisClearProcess():
    init.subprocess.run('clear', shell=True)
