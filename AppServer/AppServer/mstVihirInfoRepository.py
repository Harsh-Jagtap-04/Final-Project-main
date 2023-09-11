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


    ynGrampanchayatOperatorAuthorized = BoolCol(default=False)
    dtGrampanchayatOperatorAuthorized = DateTimeCol(default=None)

    ynGrampanchayatOperatorRejection = BoolCol(default=False)
    dtGrampanchayatOperatorRejection = DateTimeCol(default=None)
    nCharGrampanchayatOperatorRemark = StringCol(length=500, default=None)

    ynGrampanchayatAuthorisationAuthorized = BoolCol(default=False)
    dtGrampanchayatAuthorisationAuthorized = DateTimeCol(default=None)

    ynGrampanchayatAuthorisationRejection = BoolCol(default=False)
    dtGrampanchayatAuthorisationRejection = DateTimeCol(default=None)
    nCharGrampanchayatAuthorisationRemark = StringCol(length=500, default=None)

    ynPanchayatSamitiOperatorAuthorized = BoolCol(default=False)
    dtPanchayatSamitiOperatorAuthorized = DateTimeCol(default=None)

    ynPanchayatSamitiOperatorRejection = BoolCol(default=False)
    dtPanchayatSamitiOperatorRejection = DateTimeCol(default=None)
    nCharPanchayatSamitiOperatorRemark = StringCol(length=500, default=None)

    ynPanchayatSamitiAuthorisationAuthorized = BoolCol(default=False)
    dtPanchayatSamitiAuthorisationAuthorized = DateTimeCol(default=None)

    ynPanchayatSamitiAuthorisationRejection = BoolCol(default=False)
    dtPanchayatSamitiAuthorisationRejection = DateTimeCol(default=None)
    nCharPanchayatSamitiAuthorisationRemark = StringCol(length=500, default=None)

    ynZillhaParishadAuthorized = BoolCol(default=False)
    dtZillhaParishadAuthorized = DateTimeCol(default=None)

    ynZillhaParishadRejected = BoolCol(default=False)
    dtZillhaParishadRejected = DateTimeCol(default=None)
    nCharZillhaParishadRemark = StringCol(length=500, default=None)


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
        oRepository.dtDateOfCreation = datetime.datetime.now()
        oRepository.dtSubmittedDateTime = datetime.datetime.now()
        print(oRepository.dtDateOfCreation)

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


def authorizeGrampanchayatOperator(vihir_id):
    try:
        vihir = MstVihirInfo.get(vihir_id)
        vihir.ynGrampanchayatOperatorAuthorized = True
        vihir.dtGrampanchayatOperatorAuthorized = datetime.datetime.now()
        return vihir
    except Exception as e:
        print("Error in authorizeGrampanchayatOperator:", str(e))

def rejectGrampanchayatOperator(vihir_id, remark):
    try:
        vihir = MstVihirInfo.get(vihir_id)
        vihir.ynGrampanchayatOperatorRejection = True
        vihir.dtGrampanchayatOperatorRejection = datetime.datetime.now()
        vihir.nCharGrampanchayatOperatorRemark = remark
        return vihir
    except Exception as e:
        print("Error in rejectGrampanchayatOperator:", str(e))

def authorizeGrampanchayat(vihir_id):
    try:
        vihir = MstVihirInfo.get(vihir_id)
        vihir.ynGrampanchayatAuthorisationAuthorized = True
        vihir.dtGrampanchayatAuthorisationAuthorized = datetime.datetime.now()
        return vihir
    except Exception as e:
        print("Error in authorizeGrampanchayat:", str(e))

def rejectGrampanchayat(vihir_id, remark):
    try:
        vihir = MstVihirInfo.get(vihir_id)
        vihir.ynGrampanchayatAuthorisationRejection = True
        vihir.dtGrampanchayatAuthorisationRejection = datetime.datetime.now()
        vihir.nCharGrampanchayatAuthorisationRemark = remark
        return vihir
    except Exception as e:
        print("Error in rejectGrampanchayat:", str(e))

# Similar functions for Panchayat Samiti Operator authorization and rejection

def authorizePanchayatSamitiOperator(vihir_id):
    try:
        vihir = MstVihirInfo.get(vihir_id)
        vihir.ynPanchayatSamitiOperatorAuthorized = True
        vihir.dtPanchayatSamitiOperatorAuthorized = datetime.datetime.now()
        return vihir
    except Exception as e:
        print("Error in authorizePanchayatSamitiOperator:", str(e))

def rejectPanchayatSamitiOperator(vihir_id, remark):
    try:
        vihir = MstVihirInfo.get(vihir_id)
        vihir.ynPanchayatSamitiOperatorRejection = True
        vihir.dtPanchayatSamitiOperatorRejection = datetime.datetime.now()
        vihir.nCharPanchayatSamitiOperatorRemark = remark
        return vihir
    except Exception as e:
        print("Error in rejectPanchayatSamitiOperator:", str(e))

def authorizePanchayatSamiti(vihir_id):
    try:
        vihir = MstVihirInfo.get(vihir_id)
        vihir.ynPanchayatSamitiAuthorisationAuthorized = True
        vihir.dtPanchayatSamitiAuthorisationAuthorized = datetime.datetime.now()
        return vihir
    except Exception as e:
        print("Error in authorizePanchayatSamiti:", str(e))

def rejectPanchayatSamiti(vihir_id, remark):
    try:
        vihir = MstVihirInfo.get(vihir_id)
        vihir.ynPanchayatSamitiAuthorisationRejection = True
        vihir.dtPanchayatSamitiAuthorisationRejection = datetime.datetime.now()
        vihir.nCharPanchayatSamitiAuthorisationRemark = remark
        return vihir
    except Exception as e:
        print("Error in rejectPanchayatSamiti:", str(e))

# Similar functions for Zillha Parishad authorization and rejection

def authorizeZillhaParishad(vihir_id):
    try:
        vihir = MstVihirInfo.get(vihir_id)
        vihir.ynZillhaParishadAuthorized = True
        vihir.dtZillhaParishadAuthorized = datetime.datetime.now()
        return vihir
    except Exception as e:
        print("Error in authorizeZillhaParishad:", str(e))

def rejectZillhaParishad(vihir_id, remark):
    try:
        vihir = MstVihirInfo.get(vihir_id)
        vihir.ynZillhaParishadRejected = True
        vihir.dtZillhaParishadRejected = datetime.datetime.now()
        vihir.nCharZillhaParishadRemark = remark
        return vihir
    except Exception as e:
        print("Error in rejectZillhaParishad:", str(e))



sqlhub.processConnection = connectionForURI('sqlite:./FormSystem.db')
MstVihirInfo.createTable(ifNotExists=True)
