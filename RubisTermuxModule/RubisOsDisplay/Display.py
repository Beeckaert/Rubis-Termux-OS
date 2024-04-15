# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import Rubis Module

# Variable Dynamique
HeaderTitle ="Rubis Termux os"
APPVersion ="V:-0.0.0.0.1"

PseudoTemp = "Non Fournie*"
PasswordTemp = "Non Fournie*"

BodyContent ="None"
BodyFooter ="None"

# Variable Display

Header = f"""

    • ═ ═ ═══ • ═══ ═ ═ •

        {HeaderTitle}

    • ═ ═ ═══ • ═══ ═ ═ •
    

        {APPVersion}

"""

Body = f"""

     ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

      {BodyContent}

     ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

      {BodyFooter}

"""

Flooter = """

    • ═ ═ ═══ • ═══ ═ ═ •

    *create By Systeme Rubis

"""

# Main Function

def RubisOsTemplateInterface():
    print(Header, Body, Flooter)

def RubisOsInterface(RubisOsIdDisplay):
    if(RubisOsIdDisplay == "RootDisplay"):
        RubisOsTemplateInterface()
