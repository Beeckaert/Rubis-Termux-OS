# Dev by systeme rubis

# -*- coding: utf-8 -*-

# Import

from ..RubisOSInit import init

# Main Function


def RubisMainDisplay(RubisTermuxSetup):
    if(RubisTermuxSetup == "SetupHeader"):
        HeaderTitle ="RUBIS TERMUX OS"
        APPVersion ="V:-0.0.0.0.1"
        Header = f"""

    • ═ ═ ═══ • ═══ ═ ═ •

        {HeaderTitle}

    • ═ ═ ═══ • ═══ ═ ═ •
    

        {APPVersion}
        """
        print(Header);
    elif(RubisTermuxSetup == "SetupBody"):
        ContentBody = """
    1/: créer session

    2/: Option
    """
        WidjetBody = """
        q: quitter
        """
        Body = f"""
    ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

    {ContentBody}

    ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄
    {WidjetBody}
    """
        print(Body)
    elif(RubisTermuxSetup == "SetupFlooter"):
        Flooter = """
    • ═ ═ ═══ • ═══ ═ ═ •

  *create By Systeme Rubis
    """
        print(Flooter);

def RubisCreateSessionDisplay(RubisTermuxSetup):
    if(RubisTermuxSetup == "CreeSession:Update"):
        init.ObjectData.SetupData.PseudoTemp
        init.ObjectData.SetupData.PasswordTemp

        ContentBody = f"""
    Pseudo:  {init.ObjectData.SetupData.PseudoTemp} 
        
    Mot De Passe:  {init.ObjectData.SetupData.PasswordTemp}
    """
        WidjetBody = """
        p: précédent

        q: quitter
        """

        Body = f"""
    ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

    {ContentBody}

    ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄
    {WidjetBody}
        """
        print(Body)

    elif(RubisTermuxSetup == "ConfirmSession"):
        init.ObjectData.SetupData.PseudoTemp
        init.ObjectData.SetupData.PasswordTemp
        ContentBody = f"""
    Pseudo:  {init.ObjectData.SetupData.PseudoTemp} 
        
    Mot De Passe:  {init.ObjectData.SetupData.PasswordTemp}
    """
        WidjetBody = """
        p: précédent

        q: quitter
        """

        Body = f"""
    ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

    {ContentBody}

         ═══ • ═══

   v: valider la session

   x: Recommencer

    ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄
    {WidjetBody}
        """
        print(Body)

def RubisOptionRootDisplay(RubisTermuxSetup):
    if(RubisTermuxSetup == "Option"):
        WidjetBody = """
        p: précédent

        q: quitter
        """
        ContentBody = f"""
    Chemin des packet [RubisTermux]:  
    {init.ObjectData.SetupData.PathPacket} 
        
    Interface [consoles]:  
    {init.ObjectData.SetupData.InterfaceConsole}
    """
        WidjetBody = """
        p: précédent

        q: quitter
        """
        Body = f"""
    ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄

    {ContentBody}

    ▄▄▄▄▄▄▄▄ • ▄▄▄▄▄▄▄▄
    {WidjetBody}
        """
        print(Body)

def RubisLoadInterface(RubisTermuxSetup):
    if(RubisTermuxSetup == "RunAPP"):
        init.ObjectData.SetupData.PowerStatue = "ON"
        RubisMainDisplay("SetupHeader")
        RubisMainDisplay("SetupBody")
        RubisMainDisplay("SetupFlooter")
    elif(RubisTermuxSetup == "CreeSession"):
        RubisMainDisplay("SetupHeader")
        RubisCreateSessionDisplay("CreeSession:Update")
        RubisMainDisplay("SetupFlooter")
    elif(RubisTermuxSetup == "ConfirmSession"):
        RubisMainDisplay("SetupHeader")
        RubisCreateSessionDisplay("ConfirmSession")
        RubisMainDisplay("SetupFlooter")
    elif(RubisTermuxSetup == "Option"):
        RubisMainDisplay("SetupHeader")
        RubisOptionRootDisplay("Option")
        RubisMainDisplay("SetupFlooter")
    elif(RubisTermuxSetup == "Root"):
        RubisMainDisplay("SetupHeader")
        RubisMainDisplay("SetupBody")
        RubisMainDisplay("SetupFlooter")