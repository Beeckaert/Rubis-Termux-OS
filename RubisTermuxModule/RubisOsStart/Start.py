# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import

# Rubis Module

# Init
from ..RubisOSInit import init

# Main Function

def RubisOsPreload(RubisRequest, RubisResponce):
    if(RubisRequest == "RunAPP"):
        if(RubisResponce == "Init"):
            init.Display.RubisLoadInterface("RunAPP")
    elif(RubisRequest == "CreeSession"):
        if(RubisResponce == "Init"):
            init.Display.RubisLoadInterface("CreeSession")
        elif(ActionRequest == "Return"):
            if(init.ObjectData.SetupData.PseudoTemp == "*Non Fournie"):
                if(init.ObjectData.SetupData.PasswordTemp == "*Non Fournie"):
                    init.Display.RubisLoadInterface("Root")
            elif(init.ObjectData.SetupData.PseudoTemp != "*Non Fournie"):
                if(init.ObjectData.SetupData.PasswordTemp == "*Non Fournie"):
                    init.Display.RubisLoadInterface("CreeSession")
    elif(RubisRequest == "ConfirmSession"):
        if(RubisResponce == "Init"):
            init.Display.RubisLoadInterface("ConfirmSession")
    elif(RubisRequest == "Option"):
        if(RubisResponce == "Init"):
            init.Display.RubisLoadInterface("Option")
        elif(RubisResponce == "Return"):
            init.Display.RubisLoadInterface("Root")


def RubisOsUpdate(RubisRequest, ActionRequest):
    if(RubisRequest == "RunAPP"):
            init.NavigationSheel.RubisNavigationInput("RunAPP")
    elif(RubisRequest == "CreeSession"):
        if(ActionRequest == "InputMenu"):
            init.NavigationSheel.RubisNavigationInput("CreeSession")
    elif(RubisRequest == "Option"):
        if(ActionRequest == "InputMenu"):
            init.NavigationSheel.RubisNavigationInput("Option")
        if(ActionRequest == "InputReturn"):
            init.NavigationSheel.RubisNavigationInput("Option")

def RubisOsConstructor(RubisRequest, RubisResponce):
    if(RubisRequest == "Input"):
        if(RubisResponce == "Update"):
            if(init.ObjectData.SetupData.InputContent == "CreeSession"):
                if(init.ObjectData.SetupData.PasswordTemp == "*Non Fournie"):
                    RubisOsPreload("CreeSession", "Init")
                    RubisOsUpdate("CreeSession", "InputMenu")
                else:
                    RubisOsPreload("ConfirmSession", "Init")
                    RubisOsUpdate("CreeSession", "InputMenu")
            elif(init.ObjectData.SetupData.InputContent == "Option"):
                    RubisOsPreload("Option", "Init")
                    RubisOsUpdate("Option", "InputMenu")
        elif(RubisResponce == "Return"):
            if(init.ObjectData.SetupData.InputContent == "Root"):
                RubisOsPreload("Option", "Return")
                RubisOsUpdate("Option", "InputReturn")

def RubisStart(RubisPowerStatue):
    if(RubisPowerStatue == "ON"):
        RubisOsPreload("RunAPP", "Init")
        RubisOsUpdate("RunAPP", "InputMenu")