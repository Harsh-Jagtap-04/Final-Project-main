from flask import Flask, render_template, Response, jsonify, request
from tblVihirDocumentsRepository import *
from CommonFunction import *

def GetVihirDocuments1():
    lst = GetVihirDocuments()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr

def GetVihirDocumentsById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetVihirDocumentsById(Jid)
    return to_json(lst, Jid)

def saveVihirDocuments1():
    JsonString = request.get_json()
    ret = saveVihirDocuments(JsonString)
    return to_json(ret, ret.id)


def editVihirDocuments1():
    JsonString = request.get_json()
    
    #editEditApplications(JsonString)

    ret = editVihirDocuments(JsonString)
    return to_json(ret, ret.id)


def deleteVihirDocuments1():
    JsonString = request.get_json()
    ret = deleteVihirDocuments(JsonString)
    return to_json(ret, ret.id)