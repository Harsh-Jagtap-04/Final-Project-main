from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *
import base64
import json

class MstVihirDocuments(SQLObject):

    mstVihirId = IntCol()
    blobExtract712 = StringCol()  # Use StringCol for text data
    blobForm8A = StringCol()      # Use StringCol for text data
    blobJobCard = StringCol()     # Use StringCol for text data
    blobAdditionalLandAffidavit = StringCol()  # Use StringCol for text data
    blobWaterUsageAgreement = StringCol()      # Use StringCol for text data

    # Must include
    ncharDescription = StringCol(length=500, default=None)
    dtDateOfCreation = DateTimeCol(default=datetime.datetime.now())
    dtDateOfModification = DateTimeCol(default=None)
    ynDeleted = BoolCol(default=False)

def GetVihirDocuments():
    try:
        Res = MstVihirDocuments.select(AND(MstVihirDocuments.q.ynDeleted == False))
        return Res
    except:
        print("error in MstVihirDocumentsRepository.getVihirDocuments", sys.exc_info()[1])

def GetVihirDocumentsById(Jid):
    try:
        row = MstVihirDocuments.get(Jid)
        return row
    except:
        print("error in MstApplicationRepository.GetApplicationById", sys.exc_info()[1])



def saveVihirDocuments(JsonString):
    try:
        print(JsonString)
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        oRepository = MstVihirDocuments(**obj)
        return oRepository
    except:
        print("error in MstVihirDocumentsRepository.saveVihirDocuments", sys.exc_info()[1])

def editVihirDocuments(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        oMstVihirDocumentsRepository = MstVihirDocuments.get(JsonString['id'])

        # Update blob fields if needed
        oMstVihirDocumentsRepository.mstVihirId = JsonString['mstVihirId']
        oMstVihirDocumentsRepository.blobExtract712 = JsonString['blobExtract712']
        oMstVihirDocumentsRepository.blobForm8A = JsonString['blobForm8A']
        oMstVihirDocumentsRepository.blobJobCard = JsonString['blobJobCard']
        oMstVihirDocumentsRepository.blobAdditionalLandAffidavit = JsonString['blobAdditionalLandAffidavit']
        oMstVihirDocumentsRepository.blobWaterUsageAgreement = JsonString['blobWaterUsageAgreement']

        oMstVihirDocumentsRepository.dtDateOfModification = datetime.datetime.now()
        return oMstVihirDocumentsRepository
    except:
        print("error in MstVihirDocumentsRepository.editVihirDocuments", sys.exc_info()[1])

def deleteVihirDocuments(JsonString):
    try:
        oRepository = MstVihirDocuments.get(JsonString['id'])
        oRepository.ynDeleted = True
        return oRepository
    except:
        print("error in MstVihirDocumentsRepository.deleteVihirDocuments", sys.exc_info()[1])


sqlhub.processConnection = connectionForURI('sqlite:./FormSystem.db')
MstVihirDocuments.createTable(ifNotExists=True)