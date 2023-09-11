from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from mstVihirInfoRepository import *
from CommonFunction import *


def GetVihirInfo1():
    lst = GetVihirInfo()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetVihirInfoById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetVihirInfoById(Jid)
    return to_json(lst, Jid)


def saveVihirInfo1():
    JsonString = request.get_json()
    ret = saveVihirInfo(JsonString)
    return to_json(ret, ret.id)


def editVihirInfo1():
    JsonString = request.get_json()
    ret = editVihirInfo(JsonString)
    return to_json(ret, ret.id)


def deleteVihirInfo1():
    JsonString = request.get_json()
    ret = deleteVihirInfo(JsonString)
    return to_json(ret, ret.id)

def authorizeGrampanchayatOperator1():
    JsonString = request.get_json()
    application_id = JsonString['id']
    ret = authorizeGrampanchayatOperator(application_id)
    return to_json(ret, ret.id)

def rejectGrampanchayatOperator1():
    JsonString = request.get_json()
    application_id = JsonString['id']
    remark = JsonString.get('remark', None)  # Optional remark
    ret = rejectGrampanchayatOperator(application_id, remark)
    return to_json(ret, ret.id)

def authorizePanchayatSamitiOperator1():
    JsonString = request.get_json()
    application_id = JsonString['id']
    ret = authorizePanchayatSamitiOperator(application_id)
    return to_json(ret, ret.id)

def rejectPanchayatSamitiOperator1():
    JsonString = request.get_json()
    application_id = JsonString['id']
    remark = JsonString.get('remark', None)  # Optional remark
    ret = rejectPanchayatSamitiOperator(application_id, remark)
    return to_json(ret, ret.id)

def authorizeGrampanchayat1():
    JsonString = request.get_json()
    application_id = JsonString['id']
    ret = authorizeGrampanchayat(application_id)
    return to_json(ret, ret.id)

def rejectGrampanchayat1():
    JsonString = request.get_json()
    application_id = JsonString['id']
    remark = JsonString.get('remark', None)  # Optional remark
    ret = rejectGrampanchayat(application_id, remark)
    return to_json(ret, ret.id)

def authorizePanchayatSamiti1():
    JsonString = request.get_json()
    application_id = JsonString['id']
    ret = authorizePanchayatSamiti(application_id)
    return to_json(ret, ret.id)

def rejectPanchayatSamiti1():
    JsonString = request.get_json()
    application_id = JsonString['id']
    remark = JsonString.get('remark', None)  # Optional remark
    ret = rejectPanchayatSamiti(application_id, remark)
    return to_json(ret, ret.id)

def authorizeZillhaParishad1():
    JsonString = request.get_json()
    application_id = JsonString['id']
    ret = authorizeZillhaParishad(application_id)
    return to_json(ret, ret.id)

def rejectZillhaParishad1():
    JsonString = request.get_json()
    application_id = JsonString['id']
    remark = JsonString.get('remark', None)  # Optional remark
    ret = rejectZillhaParishad(application_id, remark)
    return to_json(ret, ret.id)