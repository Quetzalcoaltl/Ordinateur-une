import requests
import obd
from numpy import loadtxt
from keras.models import load_model
import tensorflow as tf
import numpy as np
import time

def isItNone(arg):
        if (arg is None):
                return 0
        else:
            if (type(arg) == str):
                return arg
            else:
                return str(arg.magnitude)

model = load_model('model.h5')
model.summary()

ports = obd.scan_serial()
connection = obd.OBD(ports[0],baudrate=38400)

url = 'http://server.bora-iot.com/device/secret/9f44aee5e03cb21852ec3f1e1fc27b81ea7804917a8dcd7ed53eaa5adaf6d94d/data'

#RPM - RPM
#SPEED - SPEED
#COOLANT_THERMOSTAT - COOLANT_TEMP
#FUEL_RATE - FUEL_RATE
#THROTTLE_POS - THROTTLE_POS
#INTAKE_TEMP - INTAKE_TEMP

#NO_DTC
#CC_DTC
#EGR_DTC
#EM_DTC
#EVAP_DTC
#FT_DTC
#KS_DTC
#OS_DTC
SCTDTC=0
SNODTC=0
SEGRDTC=0
SEMDTC=0
SEVAPDTC=0
SFTDTC=0
SKSDTC=0
SOSDTC=0
countAI = 0
countCAR = 0
while True:
        #CAR DATA TO SHOW
        RPM = isItNone(connection.query(obd.commands.RPM).value)
        SPEED = isItNone(connection.query(obd.commands.SPEED).value)
        COOLANT_THERMOSTAT = isItNone(connection.query(obd.commands.COOLANT_TEMP).value)
        FUEL_RATE = round(connection.query(obd.commands.FUEL_RATE).value.magnitude,2)
        THROTTLE_POS = round(connection.query(obd.commands.THROTTLE_POS).value.magnitude,2)
        INTAKE_TEMP = isItNone(connection.query(obd.commands.INTAKE_TEMP).value)

        #CAR DATA TO FEED AI
        v1 = isItNone(connection.query(obd.commands.O2_B1S1).value)
        v2 = isItNone(connection.query(obd.commands.O2_B1S2).value)
        v3 = isItNone(connection.query(obd.commands.O2_B2S1).value)
        v4 = isItNone(connection.query(obd.commands.SHORT_FUEL_TRIM_1).value)
        v5 = isItNone(connection.query(obd.commands.LONG_FUEL_TRIM_1).value)
        v6 = isItNone(connection.query(obd.commands.SHORT_FUEL_TRIM_2).value)
        v7 = isItNone(connection.query(obd.commands.LONG_FUEL_TRIM_2).value)
        v8 = isItNone(connection.query(obd.commands.COOLANT_TEMP).value)
        v9 = isItNone(connection.query(obd.commands.INTAKE_TEMP).value)
        v10 = isItNone(connection.query(obd.commands.AMBIANT_AIR_TEMP).value)
        v11 = isItNone(connection.query(obd.commands.MAF).value)
        v12 = isItNone(connection.query(obd.commands.BAROMETRIC_PRESSURE).value)
        v13 = isItNone(connection.query(obd.commands.RUN_TIME).value)
        v14 = isItNone(connection.query(obd.commands.RPM).value)
        v15 = isItNone(connection.query(obd.commands.THROTTLE_POS).value)
        v16 = isItNone(connection.query(obd.commands.FUEL_RATE).value)
        v17 = isItNone(connection.query(obd.commands.COMMANDED_EGR).value)
        v18 = (connection.query(obd.commands.AUX_INPUT_STATUS).value)

        if v18:
                v18 = '1'
        else:
                v18 = '0'

        test_data = v1+','+v2+','+v3+','+v4+','+v5+','+v6+','+v7+','+v8+','+v9+','+v10+','+v11+','+v12+','+v13+','+v14+','+v15+','+v16+','+v17+','+v18
        matrix_data = np.matrix(test_data)
        matrix_data_normalized = tf.keras.utils.normalize(matrix_data, axis=1)
        predictions = model.predict(matrix_data_normalized)

        CTDTC = round(predictions[0][0]*100,2)
        NODTC = round(predictions[0][1]*100,2)
        EGRDTC = round(predictions[0][2]*100,2)
        EMDTC = round(predictions[0][3]*100,2)
        EVAPDTC = round(predictions[0][4]*100,2)
        FTDTC = round(predictions[0][5]*100,2)
        KSDTC = round(predictions[0][6]*100,2)
        OSDTC = round(predictions[0][7]*100,2)

        if (countAI<30):
            SCTDTC+=CTDTC
            SNODTC+=NODTC
            SEGRDTC+=EGRDTC
            SEMDTC+=EMDTC
            SEVAPDTC+=EVAPDTC
            SFTDTC+=FTDTC
            SKSDTC+=KSDTC
            SOSDTC+=OSDTC
            countAI+=1
        else:
            CTDTC=round(SCTDTC/30,2)
            NODTC=round(SNODTC/30,2)
            EGRDTC=round(SEGRDTC/30,2)
            EMDTC=round(SEMDTC/30,2)
            EVAPDTC=round(SEVAPDTC/30,2)
            FTDTC=round(SFTDTC/30,2)
            KSDTC=round(SKSDTC/30,2)
            OSDTC=round(SOSDTC/30,2)
            myobj = {"CTDTC":CTDTC,
                    "NODTC":NODTC,
                    "EGRDTC":EGRDTC,
                    "EMDTC":EMDTC,
                    "EVAPDTC":EVAPDTC,
                    "FTDTC":FTDTC,
                    "KSDTC":KSDTC,
                    "OSDTC":OSDTC}
            x = requests.post(url, json = myobj)
            SCTDTC=0
            SNODTC=0
            SEGRDTC=0
            SEMDTC=0
            SEVAPDTC=0
            SFTDTC=0
            SKSDTC=0
            SOSDTC=0
            countAI = 0
            countCAR = 0
            print(x)
            time.sleep(3)
            countAI=0
        if (countCAR>=4):
            myobj = {"RPM":RPM,
                    "SPEED":SPEED,
                    "COOLANT_THERMOSTAT":COOLANT_THERMOSTAT,
                    "FUEL_RATE":FUEL_RATE,
                    "THROTTLE_POS":THROTTLE_POS,
                    "INTAKE_TEMP":INTAKE_TEMP}
            x = requests.post(url, json = myobj)
            print(x)
            time.sleep(1)
            countCAR=0
        else:
            countCAR+=1
        time.sleep(1)
        






