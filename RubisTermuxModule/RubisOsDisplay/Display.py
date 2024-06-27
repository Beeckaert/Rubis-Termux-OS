# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import Rubis Module

# Variable Dynamique

# Header
HeaderTitle ="RUBIS TERMUX OS"
APPVersion ="V:-0.0.0.0.1"

# body

ContentBody = """

    1/:  créer session

    2/: Option

"""

PseudoTemp = "Non Fournie*"
PasswordTemp = "Non Fournie*"

WidjetBody = "P: précédent • q: quitter"

# Variable Display

# Header / Flooter

Header = f"""

    • ═ ═ ═══ • ═══ ═ ═ •

        {HeaderTitle}

    • ═ ═ ═══ • ═══ ═ ═ •
    

        {APPVersion}

"""

Flooter = """

    • ═ ═ ═══ • ═══ ═ ═ •

    *create By Systeme Rubis

"""

# Body

Body = f"""

     ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

     {ContentBody}

     ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

      {WidjetBody}

"""

# Main Function

def RubisOsDisplayInterface(RubisWhileCursor, RubisArg):
    if(RubisWhileCursor == "StartAPP"):
        if(RubisArg == "Default"):
            print(Header, Body, Flooter)


def RubisOsInterface(RubisOsIdDisplay, RubisOsDynamicValue):
    if(RubisOsIdDisplay == "RootDisplay"):
        RubisOsTemplateInterface("BodyRoot", "none")