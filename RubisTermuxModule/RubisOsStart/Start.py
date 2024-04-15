# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import

# Rubis Module

# Init

from ..RubisOSInit.init import 

# Main Function

def RubisOsPreload(RubisOsRequest, ActionRequest):
    if(RubisOsRequest == "LoadPrint"):
        if(ActionRequest == "RootRunAPP"):
            RubisOSInterface("RootDisplay")

def RubisOsUpdate(RubisOsRequest, ActionRequest):
    if(RubisOsRequest == "NavigationUpdate"):
        if(ActionRequest == "InputRequest"):


def RubisOsapp(RubisOsRequest, ActionRequest):
    if(RubisOsRequest == "Run"):
        if(ActionRequest == "OpenRootAPP"):
            RubisOSPreload("LoadPrint", "RootRunAPP")