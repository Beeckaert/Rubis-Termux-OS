# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import

# Rubis Module

# Init
from ..RubisOSInit import init

# Main Function

def RubisOsPreload(RubisRequest, RubisResponce):
    if(RubisRequest == "StartAPP"):
        if(RubisResponce == "Init"):
            init.Display.RubisOsInterface("StartAPP", "Default"),

def RubisOsUpdate(RubisOsRequest, ActionRequest):
    if(RubisOsRequest == "RunAPP"):
        if(ActionRequest == "RootAPP"):
            init.NavigationSheel.RubisOsInputNavigation("Root")

def RubisStart(RubisPowerStatue):
    if(RubisPowerStatue == "ON"):
        RubisOsPreload("StartAPP", "Init")