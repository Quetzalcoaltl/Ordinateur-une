#TESTA A IA
from numpy import loadtxt
from keras.models import load_model
import tensorflow as tf
import numpy as np
import obd
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
print(ports)
connection = obd.OBD(ports[0],baudrate=38400)
while True:
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


    #print(predictions)
    #CCDTC = round(predictions[0][0]*100,2)
    CTDTC = round(predictions[0][0]*100,2)
    NODTC = round(predictions[0][1]*100,2)
    EGRDTC = round(predictions[0][2]*100,2)
    EMDTC = round(predictions[0][3]*100,2)
    EVAPDTC = round(predictions[0][4]*100,2)
    FTDTC = round(predictions[0][5]*100,2)
    KSDTC = round(predictions[0][6]*100,2)
    OSDTC = round(predictions[0][7]*100,2)

    #DTC_LIST = list()
    #DTC_LIST = [CCDTC,CTDTC,NODTC,EGRDTC,EMDTC,EVAPDTC,FTDTC,KSDTC,OSDTC]
    #DTC_LIST.sort()

    #print('CatalystConverterDTC: ' + str(CCDTC))
    print('CoolantThermostatDTC: ' + str(CTDTC))
    print('No DTCs:              ' + str(NODTC))
    print('EGRDTC:               ' + str(EGRDTC))
    print('EngineMisfireDTC:     ' + str(EMDTC))
    print('EVAPDTC:              ' + str(EVAPDTC))
    print('FuelTrimDTC:          ' + str(FTDTC))
    print('KnockSensorDTC:       ' + str(KSDTC))
    print('OxygenSensorDTC:      ' + str(OSDTC))
    print('-------------------------------------------------')
    time.sleep(3)