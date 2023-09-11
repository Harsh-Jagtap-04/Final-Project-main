from flask import Flask, render_template, Response, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import sys
from mstCompanyRepository import *
from CommonFunction import *


def GetCompany1():
    lst = GetCompany()
    list = []
    for s in lst:
        list.append(to_json(s, s.id))
    jsonStr = json.dumps(list, default=myconverter)
    return jsonStr


def GetCompanyById1():
    JsonString = request.get_json()
    Jid = JsonString['id']
    lst = GetCompanyById(Jid)
    return to_json(lst, Jid)


def saveCompany1():
    JsonString = request.get_json()
    ret = saveCompany(JsonString)
    return to_json(ret, ret.id)


def editCompany1():
    JsonString = request.get_json()
    ret = editCompany(JsonString)
    return to_json(ret, ret.id)


def deleteCompany1():
    JsonString = request.get_json()
    ret = deleteCompany(JsonString)
    return to_json(ret, ret.id)
