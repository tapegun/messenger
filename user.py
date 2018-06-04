from client import makeSocket
from getIdentity import getIdentity
import socket
import json

class User:
    def getYourIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        thing = s.getsockname()[0]
        return(s.getsockname()[0])
    def __init__(self, yourIp, otherIpList, firstName, lastName):
        self.yourIp = yourIp
        self.otherIpList = otherIpList
        self.firstName = firstName
        self.lastName = lastName
    def __init__(self, yourIp, firstName, lastName ):
        self.yourIp = yourIp
        self.firstName = firstName
        self.lastName = lastName
    def __init__(self, firstName, lastName):
        self.yourIp = self.getYourIp()
        self.firstName = firstName
        self.lastName = lastName


    # def selfServer:

    def getOtherIp(self, theirName):
        return getIdentity(theirName)["ip_address"]

    # def addToContacts(self, personInfo):
    #     with open ('/Volumes/PATRIOT/Python/messager/MOCK_DATA.json') as data_file:
    #         json.load(data_file)
    #         data_file+=personInfo


    def startMessage(self, person):

        # makeSocket(getIdentity(person)[6])
        makeSocket(person)

    # def requestFriend(self, ip):
    #     # middleManRequest




# user = User("Saarth", "Bonde")
# print(user.getYourIp())
# contact = input("enter the last name of your recipient: ")

# Algo to access ip without direct contact to person using makeshift database
# user.startMessage(str(user.getOtherIp(contact)))
# print ("success")

user = User("Saarth", "Bonde")

user.startMessage("192.168.1.227")
print ("success")
