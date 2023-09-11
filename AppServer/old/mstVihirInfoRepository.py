from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *

class MstVihirInfo(SQLObject):
    ncharFirstName = StringCol(length=50)
    ncharMiddleName = StringCol(length=50)
    ncharLastName = StringCol(length=50)
    ncharResidingAt = StringCol(length=500)
    ncharTaluka = StringCol(length=50)
    ncharDistrict = StringCol(length=50)
    intBPLNumber = IntCol()
    intGroupNumber = IntCol()
    floatTotalLand = FloatCol()
    ncharCategory = StringCol(length=50)
    ncharCategorized = StringCol(length=50)
    ncharIrrigationFacility = StringCol(length=500)
    ncharFormNumber = StringCol(length=50)
    intYear = IntCol()
    dtSubmittedDateTime = DateTimeCol(default=None)
    ynVihirInfoClose = BoolCol(default=False)
    ynGramPanchayatAuthorized = BoolCol(default=False)
    dtGramPanchayatAuthDate = DateTimeCol(default=None)
    ynPanchayatSamitiAuthorized = BoolCol(default=False)
    dtPanchayatSamitiAuthDate = DateTimeCol(default=None)
    ynZillhaParishadAuthorized = BoolCol(default=False)
    dtZillhaParishadAuthDate = DateTimeCol(default=None)
    ynRejectionStatus = BoolCol(default=False)
    ncharRejectionLevel = StringCol(length=500, default=None)
    ynVihirInfoFinalised = BoolCol(default=False)
    ncharDescription = StringCol(length=500, default=None)
    dtDateOfCreation = DateTimeCol(default=datetime.datetime.now())
    dtDateOfModification = DateTimeCol(default=None)
    ynDeleted = BoolCol(default=False)


def GetVihirInfo():
    try:
        Res = MstVihirInfo.select(AND(MstVihirInfo.q.ynDeleted == False))
        return Res
    except:
        print("error in MstVihirInfoRepository.MstVihirInfo", sys.exc_info()[1])


def GetVihirInfoById(Jid):
    try:
        row = MstVihirInfo.get(Jid)
        return row
    except:
        print("error in MstVihirInfoRepository.GetVihirInfoById", sys.exc_info()[1])


def saveVihirInfo(JsonString):
    try:
        print(JsonString)
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        oRepository = MstVihirInfo(**obj)
        return oRepository
    except:
        print("error in MstVihirInfoRepository.saveVihirInfo", sys.exc_info()[1])


def editVihirInfo(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        oMstVihirInfoRepository = MstVihirInfo.get(JsonString['id'])
        oMstVihirInfoRepository.ncharFirstName = JsonString['ncharFirstName']
        oMstVihirInfoRepository.ncharMiddleName = JsonString['ncharMiddleName']
        oMstVihirInfoRepository.ncharLastName = JsonString['ncharLastName']
        oMstVihirInfoRepository.ncharResidingAt = JsonString['ncharResidingAt']
        oMstVihirInfoRepository.ncharTaluka = JsonString['ncharTaluka']
        oMstVihirInfoRepository.ncharDistrict = JsonString['ncharDistrict']
        oMstVihirInfoRepository.intBPLNumber = JsonString['intBPLNumber']
        oMstVihirInfoRepository.intGroupNumber = JsonString['intGroupNumber']
        oMstVihirInfoRepository.floatTotalLand = JsonString['floatTotalLand']
        oMstVihirInfoRepository.ncharCategory = JsonString['ncharCategory']
        oMstVihirInfoRepository.ncharCategorized = JsonString['ncharCategorized']
        oMstVihirInfoRepository.ncharIrrigationFacility = JsonString['ncharIrrigationFacility']
        oMstVihirInfoRepository.ncharFormNumber = JsonString['ncharFormNumber']
        oMstVihirInfoRepository.intYear = JsonString['intYear']
        oMstVihirInfoRepository.dtDateOfModification = datetime.datetime.now()
        return oMstVihirInfoRepository
    except:
        print("error in MstVihirInfoRepository.editVihirInfo", sys.exc_info()[1])


def deleteVihirInfo(JsonString):
    try:
        oRepository = MstVihirInfo.get(JsonString['id'])
        oRepository.ynDeleted = True
        return oRepository
    except:
        print("error in MstVihirInfoRepository.deleteVihirInfo", sys.exc_info()[1])


def authorizeGramPanchayat(application_id):
    try:
        oRepository = MstVihirInfo.get(application_id)
        oRepository.ynGramPanchayatAuthorized = True
        oRepository.dtPanchayatSamitiAuthDate = None
        oRepository.dtGramPanchayatAuthDate = datetime.datetime.now()
        return oRepository
    except:
        print("error in MstVihirInfoRepository.authorizeGramPanchayat", sys.exc_info()[1])

def rejectGramPanchayat(application_id):
    try:
        oRepository = MstVihirInfo.get(application_id)
        oRepository.ynGramPanchayatAuthorized = False
        oRepository.dtGramPanchayatAuthDate = datetime.datetime.now()
        return oRepository
    except:
        print("error in MstVihirInfoRepository.rejectGramPanchayat", sys.exc_info()[1])


def authorizePanchayatSamiti(application_id):
    try:
        oRepository = MstVihirInfo.get(application_id)
        oRepository.ynPanchayatSamitiAuthorized = True
        oRepository.dtZillhaParishadAuthDate = None
        oRepository.dtPanchayatSamitiAuthDate  = datetime.datetime.now()

        return oRepository
    except:
        print("error in MstVihirInfoRepository.authorizeGramPanchayat", sys.exc_info()[1])

def rejectPanchayatSamiti(application_id):
    try:
        oRepository = MstVihirInfo.get(application_id)
        oRepository.ynGramPanchayatAuthorized = False
        oRepository.dtPanchayatSamitiAuthDate  = datetime.datetime.now()
        oRepository.ynGramPanchayatAuthorized = False  # Update to the correct field name
        oRepository.dtGramPanchayatAuthDate = None  # Set dtPanchayatSamitiAuthDate to None
        return oRepository
    except:
        print("error in MstVihirInfoRepository.rejectGramPanchayat", sys.exc_info()[1])

def authorizeZillhaParishad(application_id):
    try:
        oRepository = MstVihirInfo.get(application_id)
        oRepository.ynZillhaParishadAuthorized = True
        oRepository.dtZillhaParishadAuthDate = datetime.datetime.now()
        return oRepository
    except:
        print("error in MstVihirInfoRepository.authorizeGramPanchayat", sys.exc_info()[1])

def rejectZillhaParishad(application_id):
    try:
        oRepository = MstVihirInfo.get(application_id)
        oRepository.ynZillhaParishadAuthorized = False
        oRepository.dtPanchayatSamitiAuthDate = None
        oRepository.dtZillhaParishadAuthDate = datetime.datetime.now()
        return oRepository
    except:
        print("error in MstVihirInfoRepository.rejectGramPanchayat", sys.exc_info()[1])


sqlhub.processConnection = connectionForURI('sqlite:./FormSystem.db')
MstVihirInfo.createTable(ifNotExists=True)
