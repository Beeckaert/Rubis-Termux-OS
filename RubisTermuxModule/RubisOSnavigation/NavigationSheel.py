# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import

# Init

from ..RubisOSInit import init

# MAin Variable 

# Main Function

def RubisOsRooterNavigation(RubisOsRooter):
    if(RubisOsRooter == "creerSession"):
        init.Display.RubisOsInterface("CrerSessionDysplay")

def RubisOsInputNavigation(RubisOsParentPage):
    BoolMainMenu = True
    MainInput = "Root:>"
    while(BoolMainMenu == True):
        if(RubisOsParentPage == "Root"):
            MenuStartInput = input(MainInput)
            if(MenuStartInput == "1"):
                init.MainProcess.RubisOsClearProcess()
                MainInput = "CrerSession:>"
                init.NavigationSheel.RubisOsRooterNavigation("creerSession")
            elif(MenuStartInput =="2"):
                init.MainProcess.RubisOsClearProcess()
            elif(MenuStartInput == "q"):
                init.MainProcess.RubisOsClearProcess()
                quit()
        