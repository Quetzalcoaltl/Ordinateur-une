import obd
import time

def isItNone(arg):
        if arg is None:
            return arg
        else:
            return arg.magnitude


ports = obd.scan_serial()
print(ports)
 # auto-connects to USB or RF port
connection = obd.OBD(ports[0],baudrate=38400)
while True:
    #TESTE PARA Catalyst Converter (P0420 e P0430)
    #print('FRONT: ',connection.query(obd.commands.O2_B1S1).value)
    #print('BACK: ',connection.query(obd.commands.O2_B1S2).value)

    #TESTE PARA Fuel Trim (P0171 e P0174)
    #print('SHORT B1: ',connection.query(obd.commands.SHORT_FUEL_TRIM_1).value)
    #print('LONG B1: ',connection.query(obd.commands.LONG_FUEL_TRIM_1).value)
    #print('SHORT B2: ',connection.query(obd.commands.SHORT_FUEL_TRIM_2).value)
    #print('LONG B2: ',connection.query(obd.commands.LONG_FUEL_TRIM_2).value)

    #TESTE PARA Coolant Thermostat (P0128)
    #print('Coolant Temp:',connection.query(obd.commands.COOLANT_TEMP).value)
    #print('Air Temp:',connection.query(obd.commands.INTAKE_TEMP).value)
    #print('Run Time:',connection.query(obd.commands.RUN_TIME).value)

    #TESTE PARA KnockOut Sensor (P0325)
    #print(connection.query(obd.commands.RPM).value)
    #print(connection.query(obd.commands.COOLANT_TEMP).value)
    #print(connection.query(obd.commands.RUN_TIME).value)
    #print(connection.query(obd.commands.AUX_INPUT_STATUS).value)

    #TESTE PARA Oyxgen Sensor (P0133, P0135 e P0141)
    #print('Coolant Temp:',connection.query(obd.commands.COOLANT_TEMP).value)
    #print('Air Temp:',connection.query(obd.commands.INTAKE_TEMP).value)
    #print('Run Time:',connection.query(obd.commands.RUN_TIME).value)
    #print('RPM:',connection.query(obd.commands.RPM).value)
    #print('Baro Pressure:',connection.query(obd.commands.BAROMETRIC_PRESSURE).value)
    #print('MAF:',connection.query(obd.commands.MAF).value)
    #print('Throttle Pos:',connection.query(obd.commands.THROTTLE_POS).value)


    #TESTE para EGR (P0401)
    #print('RPM:',connection.query(obd.commands.RPM).value)
    #print('Fuel Rate:',connection.query(obd.commands.FUEL_RATE).value)
    #print('Ambient Air Temp:',connection.query(obd.commands.AMBIANT_AIR_TEMP).value)
    #print('Coolant Temp:',connection.query(obd.commands.COOLANT_TEMP).value)
    #print('Baro Pressure:',connection.query(obd.commands.BAROMETRIC_PRESSURE).value)
    #print('EGR Pos:',connection.query(obd.commands.COMMANDED_EGR).value)
    #print('Throttle Pos:',connection.query(obd.commands.THROTTLE_POS).value)

    #TESTE para Engine Misfire (P0300 a P0305)
    #print('RPM:',connection.query(obd.commands.RPM).value)
    #print('Fuel Rate:',connection.query(obd.commands.FUEL_RATE).value)
    #print('Coolant Temp:',connection.query(obd.commands.COOLANT_TEMP).value)

    #TESTE para EVAP (P0411 P0440 P0442 P0446 P0455)
    #print('RUN_TIME:',connection.query(obd.commands.RUN_TIME).value)
    #print('AMBIANT_AIR_TEMP:',connection.query(obd.commands.AMBIANT_AIR_TEMP).value)
    #print('BIOMETRIC_PRESSURE',connection.query(obd.commands.BAROMETRIC_PRESSURE).value)
    #print('Coolant Temp:',connection.query(obd.commands.COOLANT_TEMP).value)

    #TESTE para TODOS OS SENSORES DA COLETA
    #print('B1S1:',connection.query(obd.commands.O2_B1S1).value)
    #print('B1S2:',connection.query(obd.commands.O2_B1S2).value)
    #print('B2S1:',connection.query(obd.commands.O2_B2S1).value)
    #print('SHORT_FUEL_TRIM_1:',connection.query(obd.commands.SHORT_FUEL_TRIM_1).value)
    #print('LONG_FUEL_TRIM_1:',connection.query(obd.commands.LONG_FUEL_TRIM_1).value)
    #print('SHORT_FUEL_TRIM_2:',connection.query(obd.commands.SHORT_FUEL_TRIM_2).value)
    #print('LONG_FUEL_TRIM_2:',connection.query(obd.commands.LONG_FUEL_TRIM_2).value)
    #print('COOLANT_TEMP:',connection.query(obd.commands.COOLANT_TEMP).value)
    #print('INTAKE_TEMP:',connection.query(obd.commands.INTAKE_TEMP).value)
    #print('AMBIANT_AIR_TEMP:',connection.query(obd.commands.AMBIANT_AIR_TEMP).value)
    #print('MAF:',connection.query(obd.commands.MAF).value)
    #print('BIOMETRIC_PRESSURE',connection.query(obd.commands.BAROMETRIC_PRESSURE).value)
    #print('RUN_TIME:',connection.query(obd.commands.RUN_TIME).value)
    #print('RPM:',connection.query(obd.commands.RPM).value)
    #print('THROTTLE_POS:',connection.query(obd.commands.THROTTLE_POS).value)
    #print('FUEL_RATE:',connection.query(obd.commands.FUEL_RATE).value)
    #print('COMMANDED_EGR:',connection.query(obd.commands.COMMANDED_EGR).value)
    #print('AUX_INPUT_STATUS:',connection.query(obd.commands.AUX_INPUT_STATUS).value)

   
    print('_________________________________________________________________')
    time.sleep(3)
