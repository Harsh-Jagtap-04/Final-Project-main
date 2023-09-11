from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from mstAdminRepository import *
from CommonFunction import *

def GetAdmin1():
    lst = GetAdmin()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetAdminById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetAdminById(Jid)
    return to_json(lst, Jid)

def saveAdmin1():
    JsonString = request.get_json()
    ret = saveAdmin(JsonString)
    return to_json(ret, ret.id)


def editAdmin1():
    JsonString = request.get_json()
    ret = editAdmin(JsonString)
    return to_json(ret, ret.id)


def deleteAdmin1():
    JsonString = request.get_json()
    ret = deleteAdmin(JsonString)
    return to_json(ret, ret.id)

def GetAdminByEmail1():
    JsonString = request.get_json()
    email = JsonString['email']
    lst = getAdminByEmail(email)
    return to_json(lst, email)
