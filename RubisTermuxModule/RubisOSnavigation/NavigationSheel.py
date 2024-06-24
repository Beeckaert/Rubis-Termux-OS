# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import

# Init

from ..RubisOSInit import init

# MAin Variable 

# Main Function

def RubisOsRooterNavigation(RubisOsRooter, RubisOsDynamicValue):
    if(RubisOsDynamicValue == "none"):
        if(RubisOsRooter == "creerSession"):
            init.Display.RubisOsInterface("CrerSessionDisplay", "none")
        elif(RubisOsRooter == "creerSession"):
            init.Display.RubisOsInterface("PseudoDefini", "none");
    else:
        if(RubisOsRooter == "PseudoDefini"):
            dynamicValue = RubisOsDynamicValue
            init.Display.RubisOsInterface("PseudoDefini", dynamicValue)

def RubisOsInputNavigation(RubisOsParentPage):
    MainPaging = 1
    ValueInput = "Root:>"
    while(MainPaging  == 1):
        MainInput = input(ValueInput)
        if(MainInput == "1"):
            init.MainProcess.RubisOsClearProcess()
            MainInput = "CrerSession:>"
            init.Display.RubisOsInterface("CrerSession", "none")
            MainPaging = 2
        elif(MainInput =="2"):
            init.MainProcess.RubisOsClearProcess()  
            quit()
        elif(MainInput == "q"):
            init.MainProcess.RubisOsClearProcess()
            quit()
    while(MainPaging  == 2):
        ValueInput = "Root:>"
        MainInput = input(ValueInput)
        init.MainProcess.RubisOsClearProcess()
        init.Display.RubisOsInterface("PseudoDefini", MainInput)