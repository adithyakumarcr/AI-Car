import smbus			#import SMBus module of I2C
from time import sleep          #import
import csv
import math
#some MPU6050 Registers and their Address

PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47
gyro_z_cal=0
angle_yaw =0
angle_pitch_output=0
angle_roll_output=0
angle_yaw_output=0

def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	
	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)
	
	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	
	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")

csv_file_name="imu.csv"

#with open(csv_file_name, "w") as csv_file:
#	writer = csv.writer(csv_file, delimiter= ',')
#	writer.writerow(("Gx", "Gy", "Gz", "Ax", "Ay", "Az"))

for i in range (50):
	#gyro_x = read_raw_data(GYRO_XOUT_H)/131.0
	#gyro_y = read_raw_data(GYRO_YOUT_H)/131.0
	gyro_z = read_raw_data(GYRO_ZOUT_H)/131.0

	#gyro_x_cal = gyro_x_cal+gyro_x
	#gyro_y_cal = gyro_y_cal+gyro_y
	gyro_z_cal = gyro_z_cal+gyro_z


#gyro_x_cal = gyro_x_cal/50
#gyro_y_cal = gyro_y_cal/50
gyro_z_cal = gyro_z_cal/50


print("Offset set")
#print(gyro_x_cal)
#print(gyro_y_cal)
print(gyro_z_cal)





while True:	
	#Read Accelerometer raw value
	#acc_x = read_raw_data(ACCEL_XOUT_H)/16384.0
	#acc_y = read_raw_data(ACCEL_YOUT_H)/16384.0
	#acc_z = read_raw_data(ACCEL_ZOUT_H)/16384.0
	
	#Read Gyroscope raw value
	#gyro_x = read_raw_data(GYRO_XOUT_H)/131.0
	#gyro_y = read_raw_data(GYRO_YOUT_H)/131.0
	gyro_z = read_raw_data(GYRO_ZOUT_H)/131.0

	#print(gyro_x, gyro_y,gyro_z)
	
	#gyro_x = gyro_x - gyro_x_cal
	#gyro_y = gyro_y - gyro_y_cal
	gyro_z = gyro_z - gyro_z_cal


	#print(gyro_x, gyro_y,gyro_z)

	
	#angle_pitch = angle_pitch + gyro_x * 0.0000611
	#angle_roll = angle_roll + gyro_y * 0.0000611
	print(gyro_z)
	angle_yaw  = angle_yaw + gyro_z * 0.001066*0.85714285*90*0.609447*0.9812871*0.9935


	print("Angle Yaw = ", angle_yaw)
	#angle_pitch = angle_pitch + angle_roll*(math.sin(gyro_z * 0.000001066))
	#angle_roll = angle_pitch  - angle_pitch*(math.sin(gyro_z * 0.000001066))
	#acc_total_vector = math.sqrt((acc_x*acc_x)+(acc_y*acc_y)+(acc_z*acc_z)) #Calculate the total accelerometer vector


	#angle_pitch_acc = math.asin(float(acc_y/acc_total_vector))*90       #Calculate the pitch angle
	#angle_roll_acc = math.asin(float(acc_x/acc_total_vector))*-90       #Calculate the roll angle
	#angle_yaw_acc = math.asin(float(acc_x/acc_total_vector))*90
	#angle_yaw_acc = 0.001
	#angle_pitch_acc = angle_pitch_acc +11.77                                          #Accelerometer calibration value for pitch
	#angle_roll_acc = angle_roll_acc + 13.414                                         #Accelerometer calibration value for roll
	#angle_yaw_acc = angle_yaw_acc -123.46414

	#if set_gyro_angles==True:
	#	angle_pitch = angle_pitch * 0.9996 + angle_pitch_acc*0.0004    #Correct the drift of the gyro pitch angle with the accelerometer pitch angle
	#	angle_roll = angle_roll * 0.9996 + angle_roll_acc*0.0004      #Correct the drift of the gyro roll angle with the accelerometer roll angle
		#angle_yaw  = angle_yaw *0.996 + angle_yaw_acc *0.004
	#else:
		#angle_pitch = angle_pitch_acc                                    #Set the gyro pitch angle equal to the accelerometer pitch angle 
		#angle_roll = angle_roll_acc                                      #Set the gyro roll angle equal to the accelerometer roll angle 
		#angle_yaw = angle_yaw_acc
		#set_gyro_angles = True                                        #Set the IMU started flag
	
	#angle_pitch_output = angle_pitch_output * 0.9 + angle_pitch * 0.1	 #Take 90% of the output pitch value and add 10% of the raw pitch value
	#angle_roll_output = angle_roll_output * 0.9 + angle_roll * 0.1      #Take 90% of the output roll value and add 10% of the raw roll value
	#angle_yaw_output = angle_yaw_output * 0.9 + angle_yaw *0.1

	#print("AngleZ = ", angle_pitch_output)
	#print("Angle  = ", angle_roll_output)
	

#	with open(csv_file_name, "a") as csv_file:
#		writer = csv.writer(csv_file, delimiter= ',')
#		writer.writerow((Gx, Gy, Gz, Ax, Ay, Az))
	               

