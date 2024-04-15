# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import

from ..RubisOSInit.init import RubisOSInterface

# Main Function

def RubisOsInputNavigation(RubisOsParentPage):
    BoolMainMenu = True
    while(BoolMainMenu == True):
        if(RubisOsParentPage == "Root"):
            MenuStartInput = input("Root;>:")
            if(MenuStartInput == "1"):
                
            elif(MenuStartInput =="2"):
                AutoClearMenuProcess("DisplayMain_StatMenu", "2")
            elif(MenuStartInput == "q"):
                AutoClearMenuProcess("DisplayExitApp", "q")
                quit()
        elif(IdPage == "creerSession"):
            MenuStartInput = input("Crer une session;>:")
            AutoClearMenuProcess("DisplayMain_CrerSession", "ClavierOutput")