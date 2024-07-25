# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import

# Init

from ..RubisOSInit import init

# MAin Variable 

# Main Function

def RubisNavigationInput(RubisTermuxSetup):
    if(RubisTermuxSetup == "RunAPP"):
        while( init.ObjectData.SetupData.InputContent == "Root"):
            MainInput = input("Root//:")
            if(MainInput == "1"):
                init.MainProcess.RubisClearProcess()
                init.ObjectData.SetupData.InputContent = "CreeSession"
                init.Start.RubisOsConstructor("Input", "Update")
            elif(MainInput == "2"):
                init.MainProcess.RubisClearProcess()
                init.ObjectData.SetupData.InputContent = "Option"
                init.Start.RubisOsConstructor("Input", "Update")
            elif(MainInput == "q"):
                init.MainProcess.RubisClearProcess()
                quit()
    elif(RubisTermuxSetup == "CreeSession"):
        while(init.ObjectData.SetupData.InputContent == "CreeSession"):
            if(init.ObjectData.SetupData.PseudoTemp == "*Non Fournie"):
                MainInput = input("CreeSession//:Entrer un pseudo:")
                if(MainInput == "q"):
                    init.MainProcess.RubisClearProcess()
                    quit()
                elif(MainInput == "p"):
                    init.MainProcess.RubisClearProcess()
                    init.ObjectData.SetupData.InputContent = "Root"
                    init.Start.RubisOsConstructor("Input", "Return")
                else:
                    init.MainProcess.RubisClearProcess()
                    init.ObjectData.SetupData.PseudoTemp = MainInput
                    init.Start.RubisOsConstructor("Input", "Update")
            elif(init.ObjectData.SetupData.PasswordTemp == "*Non Fournie"):
                MainInput = input("CreeSession//:Entrer un mot de passe:")
                if(MainInput == "q"):
                    init.MainProcess.RubisClearProcess()
                    quit()
                elif(MainInput == "p"):
                    init.MainProcess.RubisClearProcess()
                    init.ObjectData.SetupData.InputContent = "Root"
                    init.Start.RubisOsConstructor("Input", "Return")
                else:
                    init.MainProcess.RubisClearProcess()
                    init.ObjectData.SetupData.PasswordTemp = MainInput
                    init.Start.RubisOsConstructor("Input", "Update")
            else:
                MainInput = input("CreeSession//:valider la session?:")
                if(MainInput == "q"):
                    init.MainProcess.RubisClearProcess()
                    quit()
                else:
                    init.MainProcess.RubisClearProcess()
                    init.Start.RubisOsConstructor("Input", "Update")
    elif(RubisTermuxSetup == "Option"):
        while(init.ObjectData.SetupData.InputContent == "Option"):
            MainInput = input("Option//:Tapez votre commende:")
            if(MainInput == "p"):
                    init.MainProcess.RubisClearProcess()
                    init.ObjectData.SetupData.InputContent = "Root"
                    init.Start.RubisOsConstructor("Input", "Return")
            elif(MainInput == "q"):
                    init.MainProcess.RubisClearProcess()
                    quit()