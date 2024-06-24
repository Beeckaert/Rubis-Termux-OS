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

DefaultValue =""



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

def RubisOsTemplateInterface(RubisOsBody, RubisOsDynamicValue):
    if(RubisOsDynamicValue == "none"):
        if(RubisOsBody == "BodyRoot"):
            print(Header, BodyRoot, Flooter)
        elif(RubisOsBody == "CrerSession"):
            print(Header, BodyCrerSession, Flooter)
    else:
        if(RubisOsBody == "PseudoDefini"):
            BodyCrerSessionPseudoDefini = f"""

     ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

     Pseudo: {RubisOsDynamicValue}

     Mot de Passe: *non Founie

     ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

     r/:Return q/: Exit app

"""
            print(Header, BodyCrerSessionPseudoDefini, Flooter)


def RubisOsInterface(RubisOsIdDisplay, RubisOsDynamicValue):
    if(RubisOsDynamicValue == "none"):
        if(RubisOsIdDisplay == "RootDisplay"):
            RubisOsTemplateInterface("BodyRoot", "none")
        elif(RubisOsIdDisplay == "CrerSessionDisplay", "none"):
            RubisOsTemplateInterface("CrerSession", "none")
        elif(RubisOsIdDisplay == "PseudoDefini", "none"):
            RubisOsTemplateInterface("PseudoDefini", "none")
    else:
        if(RubisOsIdDisplay == "PseudoDefini"):
            RubisOsTemplateInterface("PseudoDefini", RubisOsDynamicValue)