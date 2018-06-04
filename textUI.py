import docs
import socket
import json
from client import makeSocket
from getIdentity import getIdentity
class interface():
    def __init__(self, status):
        self.status = status
        self.interface_ = None

    def changeStatus(self, change):  #  (STARTMSG/ADD/MENU/DOCS)
        self.status = change
    def createTab(self):
        interface_ = open ('Interface.txt', 'w')
    def readCommand(self):
        self.interface_.readlines()
    def addToContacts(self, personInfo):
        with open ('/Volumes/PATRIOT/Python/messager/MOCK_DATA.json') as data_file:
            json.load(data_file)
            data_file += personInfo
    def startMessage(self, person):
         #makeSocket(getIdentity(person)[6])
         makeSocket(person)
    def decideAction(self):
        #if self.status = ("STARTMSG"):
            self.status = START

        #if self.status = ("ADD"):
            #thing
        # if self.status = ("DOCS"):
            # thing
        # if self.status = ("MENU"):
            # thing





    #def readCommand():

    #def UserAccount():
        #def saveUser

    #def addContact

    #def reset