from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from mstRegisterUserRepository import *
from CommonFunction import *


def GetRegisterUser1():
    lst = GetRegisterUser()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetRegisterUserById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetRegisterUserById(Jid)
    return to_json(lst, Jid)

def saveRegisterUser1():
    JsonString = request.get_json()
    ret = saveRegisterUser(JsonString)
    return to_json(ret, ret.id)



def editRegisterUser1():
    JsonString = request.get_json()
    ret = editRegisterUser(JsonString)
    return to_json(ret, ret.id)


def deleteRegisterUser1():
    JsonString = request.get_json()
    ret = deleteRegisterUser(JsonString)
    return to_json(ret, ret.id)
