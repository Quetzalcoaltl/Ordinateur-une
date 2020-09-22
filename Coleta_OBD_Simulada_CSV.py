import obd
import time
import csv
import datetime

def isItNone(arg):
        if (arg is None or type(arg) == str):
                return arg
        else:
                return arg.magnitude


ports = obd.scan_serial()
print(ports)
 # auto-connects to USB or RF port
connection = obd.OBD(ports[0],baudrate=38400)
now = datetime.datetime.now()

csvname = "SimuData_" + str(now.strftime("%d%m%y")) + "_" + str(now.strftime("%H%M%S")) + ".csv"

header = ["O2_B1S1","O2_B1S2","O2_B2S1","SHORT_FUEL_TRIM_1","LONG_FUEL_TRIM_1",
"SHORT_FUEL_TRIM_2","LONG_FUEL_TRIM_2","COOLANT_TEMP","INTAKE_TEMP","AMBIANT_AIR_TEMP",
"MAF","BAROMETRIC_PRESSURE","RUN_TIME", "RPM","THROTTLE_POS","FUEL_RATE","COMMANDED_EGR",
"AUX_INPUT_STATUS"]
x = 0
with open(csvname,'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        while x<500:
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

                writer.writerow([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18])
                time.sleep(0.001)
                x = x + 1
                if (x%100 == 0):
                        print(x)