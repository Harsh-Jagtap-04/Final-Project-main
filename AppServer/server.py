import json
import os
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from mstVihirInfocontract import *
from tblVihirDocumentscontract import *
from tblVihirVerificationcontract import *
from mstRegisterUsercontract import *
from mstAdmincontract import *
from SendMail import generate_otp, send_otp_email, verify_otp, otp_data
from mstRegisterUserRepository import *
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
cors = CORS(app)

CORS(app, resources={r'/*': {'origins': '*'}})


# ------------------------------Email-------------------------------------------------------------

@app.route('/generateOtp', methods=['POST'])
@cross_origin()
def generate_otp_route():
    data = request.get_json()
    email = data.get('email')

    if email:
        otp = generate_otp()
        otp_data[email] = otp  # Store OTP in otp_data dictionary
        send_otp_email(email, otp)
        return jsonify({"message": "OTP sent successfully."})
    else:
        return jsonify({"error": "Invalid data."}), 400


@app.route('/verifyOtp', methods=['POST'])
@cross_origin()
def verify_otp_route():
    data = request.get_json()
    email = data.get('email')
    otp = data.get('otp')

    if email and otp:
        if verify_otp(email, otp):
            return jsonify({"message": "OTP verified successfully."})
        else:
            return jsonify({"error": "Invalid OTP."}), 400
    else:
        return jsonify({"error": "Invalid data."}), 400

# -----------------------------VihirInfo------------------------------------------------------------


@app.route('/GetVihirInfo', methods=['GET'])
@cross_origin()
def GetVihirInfo():
    return GetVihirInfo1()


@app.route('/GetVihirInfoById', methods=['POST'])
@cross_origin()
def GetVihirInfoById():
    return GetVihirInfoById1()


@app.route('/saveVihirInfo', methods=['POST'])
@cross_origin()
def saveVihirInfo():
    return saveVihirInfo1()


@app.route('/editVihirInfo', methods=['POST'])
@cross_origin()
def editVihirInfo():
    return editVihirInfo1()


@app.route('/deleteVihirInfo', methods=['POST'])
@cross_origin()
def deleteVihirInfo():
    return deleteVihirInfo1()

# Routes for authorization steps
@app.route('/authorizeGrampanchayatOperator', methods=['POST'])
@cross_origin()
def authorize_grampanchayat_operator():
    return authorizeGrampanchayatOperator1()

@app.route('/rejectGrampanchayatOperator', methods=['POST'])
@cross_origin()
def reject_grampanchayat_operator():
    return rejectGrampanchayatOperator1()

@app.route('/authorizePanchayatSamitiOperator', methods=['POST'])
@cross_origin()
def authorize_panchayat_samiti_operator():
    return authorizePanchayatSamitiOperator1()

@app.route('/rejectPanchayatSamitiOperator', methods=['POST'])
@cross_origin()
def reject_panchayat_samiti_operator():
    return rejectPanchayatSamitiOperator1()

@app.route('/authorizeGrampanchayat', methods=['POST'])
@cross_origin()
def authorize_grampanchayat():
    return authorizeGrampanchayat1()

@app.route('/rejectGrampanchayat', methods=['POST'])
@cross_origin()
def reject_grampanchayat():
    return rejectGrampanchayat1()

@app.route('/authorizePanchayatSamiti', methods=['POST'])
@cross_origin()
def authorize_panchayat_samiti():
    return authorizePanchayatSamiti1()

@app.route('/rejectPanchayatSamiti', methods=['POST'])
@cross_origin()
def reject_panchayat_samiti():
    return rejectPanchayatSamiti1()

@app.route('/authorizeZillhaParishad', methods=['POST'])
@cross_origin()
def authorize_zillha_parishad():
    return authorizeZillhaParishad1()

@app.route('/rejectZillhaParishad', methods=['POST'])
@cross_origin()
def reject_zillha_parishad():
    return rejectZillhaParishad1()



# -----------------------------VihirDocuments------------------------------------------------------------

@app.route('/GetVihirDocuments', methods=['GET'])
@cross_origin()
def GetVihirDocuments():
    return GetVihirDocuments1()

@app.route('/GetVihirDocumentsById', methods=['POST'])
@cross_origin()
def GetVihirDocumentsById():
    return GetVihirDocumentsById1()

@app.route('/saveVihirDocuments', methods=['POST'])
@cross_origin()
def saveVihirDocuments():
    return saveVihirDocuments1()

@app.route('/editVihirDocuments', methods=['POST'])
@cross_origin()
def editVihirDocuments():
    return editVihirDocuments1()

@app.route('/deleteVihirDocuments', methods=['POST'])
@cross_origin()
def deleteVihirDocuments():
    return deleteVihirDocuments1()

# -----------------------------VihirVerification----------------------------------------------------------

@app.route('/GetVihirVerification', methods=['GET'])
@cross_origin()
def GetVihirVerification():
    return GetVihirVerification1()

@app.route('/GetVihirVerificationById', methods=['POST'])
@cross_origin()
def GetVihirVerificationById():
    return GetVihirVerificationById1()

@app.route('/saveVihirVerification', methods=['POST'])
@cross_origin()
def saveVihirVerification():
    return saveVihirVerification1()

@app.route('/editVihirVerification', methods=['POST'])
@cross_origin()
def editVihirVerification():
    return editVihirVerification1()

@app.route('/deleteVihirVerification', methods=['POST'])
@cross_origin()
def deleteVihirVerification():
    return deleteVihirVerification1()

# -----------------------------RegisterUser----------------------------------------------------------

@app.route('/GetRegisterUser', methods=['GET'])
@cross_origin()
def GetRegisterUser():
    return GetRegisterUser1()

@app.route('/GetRegisterUserById', methods=['POST'])
@cross_origin()
def GetRegisterUserById():
    return GetRegisterUserById1()

@app.route('/saveRegisterUser', methods=['POST'])
@cross_origin()
def saveRegisterUser():
    return saveRegisterUser1()

@app.route('/editRegisterUser', methods=['POST'])
@cross_origin()
def editRegisterUser():
    return editRegisterUser1()

@app.route('/deleteRegisterUser', methods=['POST'])
@cross_origin()
def deleteRegisterUser():
    return deleteRegisterUser1()

# ------------------------------- Login -----------------------------------------------------------------

@app.route('/checkEmail', methods=['POST'])
@cross_origin()
def checkEmail():
    try:
        data = request.get_json()
        email = data.get('email')

        if email:
            email_exists = checkEmailExists(email)
            return jsonify({"isRegistered": email_exists})

        return jsonify({"isRegistered": False})
    except Exception as e:
        print("Error in checkEmail route:", str(e))
        return jsonify({"isRegistered": False})


# -----------------------------Admin------------------------------------------------------------
"""
@app.route('/checkAdminEmail', methods=['POST'])
@cross_origin()
def checkAdminEmail():
    try:
        data = request.get_json()
        email = data.get('email')

        if email:
            email_exists, admin_id = checkAdminEmailExists(email)
            response_data = {
                "isRegistered": email_exists,
                "admin_id": admin_id  # Include the admin_id in the response
            }
            return jsonify(response_data)

        return jsonify({"isRegistered": False, "admin_id": None})
    except Exception as e:
        print("Error in checkEmail route:", str(e))
        return jsonify({"isRegistered": False, "admin_id": None})
"""
@app.route('/checkAdminEmail', methods=['POST'])
@cross_origin()
def checkAdminEmail():
    try:
        data = request.get_json()
        email = data.get('email')

        if email:
            email_exists, admin_data = checkAdminEmailExists(email)
            response_data = {
                "isRegistered": email_exists,
                "admin_id": admin_data.get("id", None),  # Include the admin_id in the response
                "admin_data": admin_data  # Include all admin data in the response
            }
            return jsonify(response_data)

        return jsonify({"isRegistered": False, "admin_id": None, "admin_data": None})
    except Exception as e:
        print("Error in checkEmail route:", str(e))
        return jsonify({"isRegistered": False, "admin_id": None, "admin_data": None})

@app.route('/GetAdmin', methods=['GET'])
@cross_origin()
def GetAdmin():
    return GetAdmin1()

@app.route('/GetAdminById', methods=['POST'])
@cross_origin()
def GetAdminById():
    return GetAdminById1()

@app.route('/saveAdmin', methods=['POST'])
@cross_origin()
def saveAdmin():
    return saveAdmin1()

@app.route('/editAdmin', methods=['POST'])
@cross_origin()
def editAdmin():
    return editAdmin1()

@app.route('/deleteAdmin', methods=['POST'])
@cross_origin()
def deleteAdmin():
    return deleteAdmin1()

@app.route('/checkAdmin', methods=['POST'])
@cross_origin()
def GetAdminByEmails():
    return GetAdminByEmail1()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, threaded=True)

