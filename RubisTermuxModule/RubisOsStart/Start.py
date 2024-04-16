# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import

# Rubis Module

# Init
from ..RubisOSInit import init

# Main Function

def RubisOsPreload(RubisOsRequest, ActionRequest):
    if(RubisOsRequest == "RunRootAPP"):
        if(ActionRequest == "RunAPP"):
            init.Display.RubisOsInterface("RootDisplay")

def RubisOsUpdate(RubisOsRequest, ActionRequest):
    if(RubisOsRequest == "RunAPP"):
        if(ActionRequest == "RootAPP"):
            init.NavigationSheel.RubisOsInputNavigation("Root")

def RubisOsRunapp(Preloder, updater):
    if(Preloder == "RunAPP"):
        if(updater == "RootAPP"):
            init.Start.RubisOsPreload("RunRootAPP", "RunAPP")
            init.Start.RubisOsUpdate("RunAPP","RootAPP")