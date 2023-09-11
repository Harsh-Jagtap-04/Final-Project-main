from flask import Flask, render_template, Response, jsonify, request
from tblVihirVerificationRepository import *
from CommonFunction import *


def GetVihirVerification1():
    lst = GetVihirVerification()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr

def GetVihirVerificationById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetVihirVerificationById(Jid)
    return to_json(lst, Jid)

def saveVihirVerification1():
    JsonString = request.get_json()
    ret = saveVihirVerification(JsonString)
    return to_json(ret, ret.id)

def editVihirVerification1():
    JsonString = request.get_json()
    #editEditApplications(JsonString)

    ret = editVihirVerification(JsonString)
    return to_json(ret, ret.id)


def deleteVihirVerification1():
    JsonString = request.get_json()
    ret = deleteVihirVerification(JsonString)
    return to_json(ret, ret.id)