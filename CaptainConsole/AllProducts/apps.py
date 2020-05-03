from django.apps import AppConfig


class AllproductsConfig(AppConfig):
    name = 'AllProducts'

#INSERTPRODUCT CLASS

class InsertProduct():
    def __init__(self):
        pass

    def DeleteProduct(self):
        pass

    def ChangeProduct(self):
        pass

#ekki alveg viss í hvaða packages þetta þarf að fara, svo skal ég setja það hér

#CUSTOMER CLASS
###################
###################

class Customer():
    def __init__(self):
        pass

    def Login(self):
        pass

    def signUp(self):
        pass
#vantar að bætta við search history og payment info í cutomer

#CAPTAINCONSOLE CLASS
#####################

class CaptainConsole():
    def __init__(self):
        pass

    def filterByType(self):
        pass

    def search(self):
        pass

    def orderByName(self):
        pass

    def orderByPrice(self):
        pass

#ADMIN CLASS
############

class Admin():
    def __init__(self):
        pass

    def login(self):
        pass

#PROFILE CLASS
##############

class Profile():
    def __init__(self):
        pass

    def setUserName(self):
        pass

    def setImage(self):
        pass