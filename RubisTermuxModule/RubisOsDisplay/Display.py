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

Header = """

    • ═ ═ ═══ • ═══ ═ ═ •

        RUBIS TERMUX OS

    • ═ ═ ═══ • ═══ ═ ═ •
    

         V:-0.0.0.0.1

"""

Flooter = """

    • ═ ═ ═══ • ═══ ═ ═ •

    *create By Systeme Rubis

"""

BodyRoot = """

     ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

     1/: Crer une session

     2/: Option

     ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

      q/: Exit app

"""

BodyCrerSession = """

     ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

     Pseudo: *non Fournie

     Mot de Passe: *non Founie

     ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

     r/:Return q/: Exit app

"""

# Main Function

def RubisOsTemplateInterface(RubisOsBody):
    if(RubisOsBody == "BodyRoot"):
        print(Header, BodyRoot, Flooter)
    elif(RubisOsBody == "CrerSession"):
        print(Header, BodyCrerSession, Flooter)


def RubisOsInterface(RubisOsIdDisplay):
    if(RubisOsIdDisplay == "RootDisplay"):
        RubisOsTemplateInterface("BodyRoot")
    elif(RubisOsIdDisplay == "CrerSessionDysplay"):
        RubisOsTemplateInterface("CrerSession")
