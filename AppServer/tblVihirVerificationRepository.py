from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *

class MstVihirVerification(SQLObject):

    mstVihirId = IntCol()
    ncharAadharNumber = StringCol(length=50)
    ncharMobileNumber = StringCol(length=50)
    ncharWitness1 = StringCol(length=50)
    ncharWitness2 = StringCol(length=50)

    #must included
    ncharDescription = StringCol(length=500, default=None)
    dtDateOfCreation = DateTimeCol(default=datetime.datetime.now())
    dtDateOfModification = DateTimeCol(default=None)
    ynDeleted = BoolCol(default=False)


def GetVihirVerification():
    try:
        Res = MstVihirVerification.select(AND(MstVihirVerification.q.ynDeleted == False))
        return Res
    except:
        print("error in MstVihirVerificationRepository.getVihirVerification", sys.exc_info()[1])

def GetVihirVerificationById(Jid):
    try:
        row = MstVihirVerification.get(Jid)
        return row
    except:
        print("error in MstApplicationRepository.GetApplicationById", sys.exc_info()[1])


def saveVihirVerification(JsonString):
    try:
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        oRepository = MstVihirVerification(**obj)
        return oRepository
    except:
        print("error in MstVihirVerificationRepository.saveVihirVerification", sys.exc_info()[1])


def editVihirVerification(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        oMstVihirVerificationRepository = MstVihirVerification.get(JsonString['id'])


        oMstVihirVerificationRepository.mstVihirId = JsonString['mstVihirId']
        oMstVihirVerificationRepository.ncharAadharNumber = JsonString['ncharAadharNumber']
        oMstVihirVerificationRepository.ncharMobileNumber = JsonString['ncharMobileNumber']
        oMstVihirVerificationRepository.ncharWitness1 = JsonString['ncharWitness1']
        oMstVihirVerificationRepository.ncharWitness2 = JsonString['ncharWitness2']

        oMstVihirVerificationRepository.dtDateOfModification = datetime.datetime.now()
        return oMstVihirVerificationRepository
    except:
        print("error in MstVihirVerificationRepository.editVihirVerification", sys.exc_info()[1])



def deleteVihirVerification(JsonString):
    try:
        oRepository = MstVihirVerification.get(JsonString['id'])
        oRepository.ynDeleted = True
        return oRepository
    except:
        print("error in MstVihirVerificationRepository.deleteVihirVerification", sys.exc_info()[1])


sqlhub.processConnection = connectionForURI('sqlite:./FormSystem.db')
MstVihirVerification.createTable(ifNotExists=True)