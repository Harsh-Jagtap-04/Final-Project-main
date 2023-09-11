from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *

class MstRegisterUser(SQLObject):
    ncharRegisterUserName = StringCol(length=50, default=None)
    ncharAadharNumber = StringCol(length=20, default=None)  # New field for adhar number
    ncharEmail = StringCol(length=100, default=None)  # New field for email
    ncharMobileNumber = StringCol(length=20, default=None)  # New field for mobile number
    ncharDescription = StringCol(length=500, default=None)
    dtDateOfCreation = DateTimeCol(default=datetime.datetime.now())
    dtDateOfModification = DateTimeCol(default=None)
    ynDeleted = BoolCol(default=False)

def GetRegisterUser():
    try:
        Res = MstRegisterUser.select(AND(MstRegisterUser.q.ynDeleted == False))
        return Res
    except:
        print("error in MstRegisterUserRepository.GetRegisterUser", sys.exc_info()[1])


def GetRegisterUserById(Jid):
    try:
        row = MstRegisterUser.get(Jid)
        return row
    except:
        print("error in MstRegisterUserRepository.GetRegisterUserById", sys.exc_info()[1])


def saveRegisterUser(JsonString):
    try:
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        oRepository = MstRegisterUser(**obj)
        return oRepository
    except:
        print("error in MstRegisterUserRepository.saveRegisterUser", sys.exc_info()[1])

def checkEmailExists(email):
    try:
        # Use a query to check if the email exists in the database
        exists_query = MstRegisterUser.selectBy(ncharEmail=email)
        print(email)

        if exists_query.count() > 0:
            print("Email exists")
        else:
            print("Email does not exist")

        return exists_query.count() > 0  # Returns True if email exists, else False
    except Exception as e:
        print("Error in MstRegisterUserRepository.checkEmailExists:", str(e))
        return False

def editRegisterUser(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        oMstRegisterUserRepository = MstRegisterUser.get(JsonString['id'])
        oMstRegisterUserRepository.ncharRegisterUserName = JsonString['ncharRegisterUserName']
        oMstRegisterUserRepository.ncharAadharNumber = JsonString['ncharAadharNumber']
        oMstRegisterUserRepository.ncharEmail = JsonString['ncharEmail']
        oMstRegisterUserRepository.ncharMobileNumber = JsonString['ncharMobileNumber']
        oMstRegisterUserRepository.ncharDescription = JsonString['ncharDescription']
        oMstRegisterUserRepository.dtDateOfModification = datetime.datetime.now()
        return oMstRegisterUserRepository
    except:
        print("error in MstRegisterUserRepository.editRegisterUser", sys.exc_info()[1])


def deleteRegisterUser(JsonString):
    try:
        oRepository = MstRegisterUser.get(JsonString['id'])
        oRepository.ynDeleted = True
        return oRepository
    except:
        print("error in MstRegisterUserRepository.deleteRegisterUser", sys.exc_info()[1])


sqlhub.processConnection = connectionForURI('sqlite:./FormSystem.db')
MstRegisterUser.createTable(ifNotExists=True)
