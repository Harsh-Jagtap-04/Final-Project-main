from datetime import datetime
import sqlite3
import sys
from sqlobject import *
import json
from CommonFunction import *


class MstCompany(SQLObject):
    ncharCompanyName = StringCol(length=50, default=None)
    ncharCompanyAddress = StringCol(length=500, default=None)
    ncharDescription = StringCol(length=500, default=None)
    dtDateOfCreation = DateTimeCol(default=datetime.datetime.now())
    dtDateOfModification = DateTimeCol(default=None)
    ynDeleted = BoolCol(default=False)


def GetCompany():
    try:
        Res = MstCompany.select(AND(MstCompany.q.ynDeleted == False))
        return Res
    except:
        print("error in MstCompanyRepository.MstCompany", sys.exc_info()[1])


def GetCompanyById(Jid):
    try:
        row = MstCompany.get(Jid)
        return row
    except:
        print("error in MstCompanyRepository.GetCompanyById", sys.exc_info()[1])


def saveCompany(JsonString):
    try:
        jstr = json.dumps(JsonString)
        obj = json.loads(jstr, object_hook=datetime_decoder)
        oRepository = MstCompany(**obj)
        return oRepository
    except:
        print("error in MstCompanyRepository.saveCompany", sys.exc_info()[1])


def editCompany(JsonString1):
    try:
        jstr = json.dumps(JsonString1)
        JsonString = json.loads(jstr, object_hook=datetime_decoder)
        oMstCompanyRepository = MstCompany.get(JsonString['id'])
        oMstCompanyRepository.ncharCompanyName = JsonString['ncharCompanyName']
        oMstCompanyRepository.ncharCompanyAddress = JsonString['ncharCompanyAddress']
        oMstCompanyRepository.ncharDescription = JsonString['ncharDescription']
        oMstCompanyRepository.dtDateOfModification = datetime.datetime.now()
        return oMstCompanyRepository
    except:
        print("error in MstCompanyRepository.editCompany", sys.exc_info()[1])


def deleteCompany(JsonString):
    try:
        oRepository = MstCompany.get(JsonString['id'])
        oRepository.ynDeleted = True
        return oRepository
    except:
        print("error in MstCompanyRepository.deleteCompany", sys.exc_info()[1])


sqlhub.processConnection = connectionForURI('sqlite:./RGPDBLite.db')
MstCompany.createTable(ifNotExists=True)
