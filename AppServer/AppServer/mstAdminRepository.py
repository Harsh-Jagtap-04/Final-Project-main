# mstAdminRepository.py

from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *

class MstAdmin(SQLObject):
    ncharFullName = StringCol(length=100, default=None)
    ncharUsername = StringCol(length=50, default=None)
    ncharPassword = StringCol(length=100, default=None)
    ncharMobileNumber = StringCol(length=20, default=None)
    ncharAdharNumber = StringCol(length=20, default=None)
    ncharEmail = StringCol(length=100, default=None)
    ncharDesignation = StringCol(length=100, default=None)
    ncharDepartment = StringCol(length=100, default=None)

    ncharZillhaParishad = StringCol(length=100, default=None)
    ncharPanchayatSamiti = StringCol(length=100, default=None)
    ncharGramPanchayat = StringCol(length=100, default=None)

    bGrampanchayatOperatorAuthoraties = BoolCol(default=False)
    bGrampanchayatAuthorisationAuthorities = BoolCol(default=False)
    bPanchayatSamitiOperatorAuthoraties = BoolCol(default=False)
    bPanchayatSamitiAuthorisationAuthorities = BoolCol(default=False)
    bZillhaParishadAuthorities = BoolCol(default=False)

    dtDateOfCreation = DateTimeCol(default=datetime.datetime.now())
    dtDateOfModification = DateTimeCol(default=None)
    ynDeleted = BoolCol(default=False)

def GetAdmin():
    try:
        Res = MstAdmin.select(AND(MstAdmin.q.ynDeleted == False))
        return Res
    except:
        print("error in MstAdminRepository.GetAdmin", sys.exc_info()[1])

def GetAdminById(Jid):
    try:
        row = MstAdmin.get(Jid)
        return row
    except:
        print("error in MstAdminRepository.GetAdminById", sys.exc_info()[1])

def saveAdmin(JsonString):
    try:
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        oRepository = MstAdmin(**obj)
        return oRepository
    except:
        print("error in MstAdminRepository.saveAdmin", sys.exc_info()[1])

def editAdmin(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        oMstAdminRepository = MstAdmin.get(JsonString['id'])
        oMstAdminRepository.ncharFullName = JsonString['ncharFullName']
        oMstAdminRepository.ncharUsername = JsonString['ncharUsername']
        oMstAdminRepository.ncharPassword = JsonString['ncharPassword']
        oMstAdminRepository.ncharMobileNumber = JsonString['ncharMobileNumber']
        oMstAdminRepository.ncharAdharNumber = JsonString['ncharAdharNumber']
        oMstAdminRepository.ncharEmail = JsonString['ncharEmail']
        oMstAdminRepository.ncharDesignation = JsonString['ncharDesignation']
        oMstAdminRepository.ncharDepartment = JsonString['ncharDepartment']
        oMstAdminRepository.ncharZillhaParishad = JsonString['ncharZillhaParishad']
        oMstAdminRepository.ncharPanchayatSamiti = JsonString['ncharPanchayatSamiti']
        oMstAdminRepository.ncharGramPanchayat = JsonString['ncharGramPanchayat']
        oMstAdminRepository.bGrampanchayatOperatorAuthoraties = JsonString['bGrampanchayatOperatorAuthoraties']
        oMstAdminRepository.bGrampanchayatAuthorisationAuthorities = JsonString['bGrampanchayatAuthorisationAuthorities']
        oMstAdminRepository.bPanchayatSamitiOperatorAuthoraties = JsonString['bPanchayatSamitiOperatorAuthoraties']
        oMstAdminRepository.bPanchayatSamitiAuthorisationAuthorities = JsonString['bPanchayatSamitiAuthorisationAuthorities']
        oMstAdminRepository.bZillhaParishadAuthorities = JsonString['bZillhaParishadAuthorities']
        oMstAdminRepository.dtDateOfModification = datetime.datetime.now()
        return oMstAdminRepository
    except:
        print("error in MstAdminRepository.editAdmin", sys.exc_info()[1])

def deleteAdmin(JsonString):
    try:
        print(JsonString)
        oRepository = MstAdmin.get(JsonString['id'])
        oRepository.ynDeleted = True
        return oRepository
    except:
        print("error in MstAdminRepository.deleteAdmin", sys.exc_info()[1])

def checkAdminEmailExists(email):
    try:
        # Use a query to check if the email exists in the database
        exists_query = MstAdmin.selectBy(ncharEmail=email)

        if exists_query.count() > 0:
            # If the email exists, get the first matching admin object
            admin = exists_query[0]
            admin_data = {
                "id": admin.id,
                "ncharFullName": admin.ncharFullName,
                "ncharUsername": admin.ncharUsername,
                "ncharPassword": admin.ncharPassword,
                "ncharMobileNumber": admin.ncharMobileNumber,
                "ncharAdharNumber": admin.ncharAdharNumber,
                "ncharEmail": admin.ncharEmail,
                "ncharDesignation": admin.ncharDesignation,
                "ncharDepartment": admin.ncharDepartment,
                "ncharZillhaParishad": admin.ncharZillhaParishad,
                "ncharPanchayatSamiti": admin.ncharPanchayatSamiti,
                "ncharGramPanchayat": admin.ncharGramPanchayat,
                "bGrampanchayatOperatorAuthoraties": admin.bGrampanchayatOperatorAuthoraties,
                "bGrampanchayatAuthorisationAuthorities": admin.bGrampanchayatAuthorisationAuthorities,
                "bPanchayatSamitiOperatorAuthoraties": admin.bPanchayatSamitiOperatorAuthoraties,
                "bPanchayatSamitiAuthorisationAuthorities": admin.bPanchayatSamitiAuthorisationAuthorities,
                "bZillhaParishadAuthorities": admin.bZillhaParishadAuthorities
            }
            return True, admin_data

        return False, None  # Return False if email doesn't exist

    except Exception as e:
        print("Error in MstRegisterUserRepository.checkEmailExists:", str(e))
        return False, None

def getAdminByEmail(email):
    try:
        admin_row = MstAdmin.get(ncharEmail=email)

        return admin_row

    except Exception as e:
        print("Error in getAdminByEmail:", str(e))
        return None


sqlhub.processConnection = connectionForURI('sqlite:./FormSystem.db')
MstAdmin.createTable(ifNotExists=True)
