import RPi.GPIO as GPIO
import DButil as dbu
import Sensor
import OutputDevice as od

led_port = 20
buzzer_port = 21

od.init(20) # LED
od.init(21) # buzzer
Sensor.init(23, 24)
dbu.init('nosleep', 'mysql!nosleep1', 'db_no_sleep')
dbu.test()

try:
    while True :
        isOnoff = 0
        distance = Sensor.getDistance()

        if(distance >= 20.0): 
            od.LEDon(led_port)
            od.buzz(buzzer_port, 10.0, 1.0)    
            isOnoff = 1
        else:
            od.LEDoff(led_port)
    
        print "distance : " + str(distance)
        sql = "INSERT INTO tb_timetable(distance, onoff) VALUE(" + str(distance) + ", " + str(isOnoff) + ");"
        dbu.exeSql(sql)

except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
