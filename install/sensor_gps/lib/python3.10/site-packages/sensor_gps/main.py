import L76X
import time
import math

try:
    x=L76X.L76X()
    x.L76X_Set_Baudrate(115200)
    #x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
    #time.sleep(2)
    #x.L76X_Set_Baudrate(115200)

    x.L76X_Send_Command(x.SET_POS_FIX_400MS);

    #Set output message
    x.L76X_Send_Command(x.SET_NMEA_OUTPUT);

    x.L76X_Exit_BackupMode();
    while(1):
        x.L76X_Gat_GNRMC()
        if(x.Status == 1):
            print('Already positioned')
        else:
            print('No positioning')
        print('Time:','{:02}'.format(x.Time_H),':{:02}'.format(x.Time_M),':{:02}'.format(int(x.Time_S)))
        print('Lon = %f'%x.Lon,'  Lat=',x.Lat)
        # x.L76X_Baidu_Coordinates(x.Lat, x.Lon)
        # print('Baidu coordinate ',x.Lat_Baidu,',',x.Lon_Baidu)
        print('Number of satelites:',x.Satellites)
        print('Speed:',x.SpeedMh,'m/s')
        print('HDOP:', x.HDOP, 'Estimated Accuracy:', x.EstimatedAccuracy, 'm')
except KeyboardInterrupt:
    #GPIO.cleanup()
    print("\nProgram end")
    exit()
