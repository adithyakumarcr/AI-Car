#include "Simple_MPU6050.h"
#define MPU6050_ADDRESS_AD0_LOW     0x68 // address pin low (GND), default for InvenSense evaluation board
#define MPU6050_ADDRESS_AD0_HIGH    0x69 // address pin high (VCC)
#define MPU6050_DEFAULT_ADDRESS     MPU6050_ADDRESS_AD0_LOW

Simple_MPU6050 mpu;
#define OFFSETS  -5374,    -3252,    2600,     -9,       -67,      -49  // My Last offsets.
#define spamtimer(t) for (static uint32_t SpamTimer; (uint32_t)(millis() - SpamTimer) >= (t); SpamTimer = millis()) // (BLACK BOX) Ya, don't complain that I used "for(;;){}" instead of "if(){}" for my Blink Without Delay Timer macro. It works nicely!!!

#define printfloatx(Name,Variable,Spaces,Precision,EndTxt) print(Name); {char S[(Spaces + Precision + 3)];Serial.print(F(" ")); Serial.print(dtostrf((float)Variable,Spaces,Precision ,S));}Serial.print(EndTxt);//Name,Variable,Spaces,Precision,EndTxt

int PrintValues(int32_t *quat, uint16_t SpamDelay = 100) {
  Quaternion q;
  VectorFloat gravity;
  float ypr[3] = { 0, 0, 0 };
  float xyz[3] = { 0, 0, 0 };
  spamtimer(SpamDelay) {// non blocking delay before printing again. This skips the following code when delay time (ms) hasn't been met
    mpu.GetQuaternion(&q, quat);
    mpu.GetGravity(&gravity, &q);
    mpu.GetYawPitchRoll(ypr, &q, &gravity);
    mpu.ConvertToDegrees(ypr, xyz);
//    Serial.printfloatx(F("Yaw")  , xyz[0], 9, 4, F(", ")); //printfloatx is a Helper Macro that works with Serial.print that I created (See #define above)
//    Serial.printfloatx(F("Pitch"), xyz[1], 9, 4, F(", "));
//    Serial.printfloatx(F("Roll") , xyz[2], 9, 4, F("\n"));
    Serial.println(xyz[0]);
  }
}

int ChartValues(int32_t *quat, uint16_t SpamDelay = 100) {
  Quaternion q;
  VectorFloat gravity;
  float ypr[3] = { 0, 0, 0 };
  float xyz[3] = { 0, 0, 0 };
  spamtimer(SpamDelay) {// non blocking delay before printing again. This skips the following code when delay time (ms) hasn't been met
    mpu.GetQuaternion(&q, quat);
    mpu.GetGravity(&gravity, &q);
    mpu.GetYawPitchRoll(ypr, &q, &gravity);
    mpu.ConvertToDegrees(ypr, xyz);
    Serial.printfloatx("", xyz[0], 9, 4, F(",")); //printfloatx is a Helper Macro that works with Serial.print that I created (See #define above)
    Serial.printfloatx("", xyz[1], 9, 4, F(","));
    Serial.printfloatx("", xyz[2], 9, 4, F("\n"));
  }
}

//Gyro, Accel and Quaternion
int PrintAllValues(int16_t *gyro, int16_t *accel, int32_t *quat, uint16_t SpamDelay = 100) {
  Quaternion q;
  VectorFloat gravity;
  float ypr[3] = { 0, 0, 0 };
  float xyz[3] = { 0, 0, 0 };
  spamtimer(SpamDelay) {// non blocking delay before printing again. This skips the following code when delay time (ms) hasn't been met
    mpu.GetQuaternion(&q, quat);
    mpu.GetGravity(&gravity, &q);
    mpu.GetYawPitchRoll(ypr, &q, &gravity);
    mpu.ConvertToDegrees(ypr, xyz);
    Serial.printfloatx(F("Yaw")  , xyz[0], 9, 4, F(",   ")); //printfloatx is a Helper Macro that works with Serial.print that I created (See #define above)
    Serial.printfloatx(F("Pitch"), xyz[1], 9, 4, F(",   "));
    Serial.printfloatx(F("Roll") , xyz[2], 9, 4, F(",   "));
    Serial.printfloatx(F("ax")   , accel[0], 5, 0, F(",   "));
    Serial.printfloatx(F("ay")   , accel[1], 5, 0, F(",   "));
    Serial.printfloatx(F("az")   , accel[2], 5, 0, F(",   "));
    Serial.printfloatx(F("gx")   , gyro[0],  5, 0, F(",   "));
    Serial.printfloatx(F("gy")   , gyro[1],  5, 0, F(",   "));
    Serial.printfloatx(F("gz")   , gyro[2],  5, 0, F("\n"));
    Serial.println();
  }
}

int ChartAllValues(int16_t *gyro, int16_t *accel, int32_t *quat, uint16_t SpamDelay = 100) {
  Quaternion q;
  VectorFloat gravity;
  float ypr[3] = { 0, 0, 0 };
  float xyz[3] = { 0, 0, 0 };
  spamtimer(SpamDelay) {// non blocking delay before printing again. This skips the following code when delay time (ms) hasn't been met
    mpu.GetQuaternion(&q, quat);
    mpu.GetGravity(&gravity, &q);
    mpu.GetYawPitchRoll(ypr, &q, &gravity);
    mpu.ConvertToDegrees(ypr, xyz);
    Serial.printfloatx("", xyz[0], 9, 4, F(",")); //printfloatx is a Helper Macro that works with Serial.print that I created (See #define above)
    Serial.printfloatx("", xyz[1], 9, 4, F(","));
    Serial.printfloatx("", xyz[2], 9, 4, F(", "));
    Serial.printfloatx("", accel[0], 5, 0, F(","));
    Serial.printfloatx("", accel[1], 5, 0, F(","));
    Serial.printfloatx("", accel[2], 5, 0, F(","));
    Serial.printfloatx("", gyro[0],  5, 0, F(","));
    Serial.printfloatx("", gyro[1],  5, 0, F(","));
    Serial.printfloatx("", gyro[2],  5, 0, F("\n"));
  }
}

int PrintQuaternion(int32_t *quat, uint16_t SpamDelay = 100) {
  Quaternion q;
  spamtimer(SpamDelay) {// non blocking delay before printing again. This skips the following code when delay time (ms) hasn't been met
    mpu.GetQuaternion(&q, quat);
    Serial.printfloatx(F("quat w")  , q.w, 9, 4, F(",   ")); //printfloatx is a Helper Macro that works with Serial.print that I created (See #define above)
    Serial.printfloatx(F("x")       , q.x, 9, 4, F(",   "));
    Serial.printfloatx(F("y")       , q.y, 9, 4, F(",   "));
    Serial.printfloatx(F("z")       , q.z, 9, 4, F("\n"));
  }
}

int PrintEuler(int32_t *quat, uint16_t SpamDelay = 100) {
  Quaternion q;
  float euler[3];         // [psi, theta, phi]    Euler angle container
  float eulerDEG[3];         // [psi, theta, phi]    Euler angle container
  spamtimer(SpamDelay) {// non blocking delay before printing again. This skips the following code when delay time (ms) hasn't been met
    mpu.GetQuaternion(&q, quat);
    mpu.GetEuler(euler, &q);
    mpu.ConvertToDegrees(euler, eulerDEG);
    Serial.printfloatx(F("euler  ")  , eulerDEG[0], 9, 4, F(",   ")); //printfloatx is a Helper Macro that works with Serial.print that I created (See #define above)
    Serial.printfloatx(F("")       , eulerDEG[1], 9, 4, F(",   "));
    Serial.printfloatx(F("")       , eulerDEG[2], 9, 4, F("\n"));
  }
}

int PrintRealAccel(int16_t *accel, int32_t *quat, uint16_t SpamDelay = 100) {
  Quaternion q;
  VectorFloat gravity;
  VectorInt16 aa, aaReal;
  spamtimer(SpamDelay) {// non blocking delay before printing again. This skips the following code when delay time (ms) hasn't been met
    mpu.GetQuaternion(&q, quat);
    mpu.GetGravity(&gravity, &q);
    mpu.SetAccel(&aa, accel);
    mpu.GetLinearAccel(&aaReal, &aa, &gravity);
    Serial.printfloatx(F("aReal x")  , aaReal.x , 9, 4, F(",   ")); //printfloatx is a Helper Macro that works with Serial.print that I created (See #define above)
    Serial.printfloatx(F("y")        , aaReal.y , 9, 4, F(",   "));
    Serial.printfloatx(F("z")        , aaReal.z, 9, 4, F("\n"));
  }
}


int PrintWorldAccel(int16_t *accel, int32_t *quat, uint16_t SpamDelay = 100) {
  Quaternion q;
  VectorFloat gravity;
  VectorInt16 aa, aaReal, aaWorld;
  spamtimer(SpamDelay) {// non blocking delay before printing again. This skips the following code when delay time (ms) hasn't been met
    mpu.GetQuaternion(&q, quat);
    mpu.GetGravity(&gravity, &q);
    mpu.SetAccel(&aa, accel);
    mpu.GetLinearAccel(&aaReal, &aa, &gravity);
    mpu.GetLinearAccelInWorld(&aaWorld, &aaReal, &q);
    Serial.printfloatx(F("aWorld x")  , aaWorld.x , 9, 4, F(",   ")); //printfloatx is a Helper Macro that works with Serial.print that I created (See #define above)
    Serial.printfloatx(F("y")        , aaWorld.y, 9, 4, F(",   "));
    Serial.printfloatx(F("z")        , aaWorld.z, 9, 4, F("\n"));
  }
}


void print_Values (int16_t *gyro, int16_t *accel, int32_t *quat, uint32_t *timestamp) {
  uint8_t Spam_Delay = 10; // Built in Blink without delay timer preventing Serial.print SPAM

  PrintValues(quat, Spam_Delay);
  // ChartValues(quat, Spam_Delay);
  //PrintAllValues(gyro, accel, quat, Spam_Delay);
  // ChartAllValues(gyro, accel, quat, Spam_Delay);
  // PrintQuaternion(quat, Spam_Delay);
  // PrintEuler(quat, Spam_Delay);
  // PrintRealAccel(accel, quat,  Spam_Delay);
  // PrintWorldAccel(accel, quat, Spam_Delay);
}

void setup() {
  uint8_t val;
  // join I2C bus (I2Cdev library doesn't do this automatically)
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
  Wire.begin();
  Wire.setClock(400000); // 400kHz I2C clock. Comment this line if having compilation difficulties
#ifdef __AVR__  
  Wire.setWireTimeout(3000, true); //timeout value in uSec
#endif
#elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
  Fastwire::setup(400, true);
#endif
  // initialize serial communication
  Serial.begin(115200);
  while (!Serial); // wait for Leonardo enumeration, others continue immediately
  //Serial.println(F("Start:"));
    mpu.Set_DMP_Output_Rate_Hz(100);           // Set the DMP output rate from 200Hz to 5 Minutes.
  //mpu.Set_DMP_Output_Rate_Seconds(10);   // Set the DMP output rate in Seconds
  //mpu.Set_DMP_Output_Rate_Minutes(5);    // Set the DMP output rate in Minute
#ifdef OFFSETS
  //Serial.println(F("Using Offsets"));
  mpu.SetAddress(MPU6050_DEFAULT_ADDRESS).load_DMP_Image(OFFSETS); // Does it all for you

#else
//  Serial.println(F(" Since no offsets are defined we aregoing to calibrate this specific MPU6050,\n"
//                   " Start by having the MPU6050 placed stationary on a flat surface to get a proper accellerometer calibration\n"
//                   " Place the new offsets on the #define OFFSETS... line at top of program for super quick startup\n\n"
//                   " \t\t\t[Press Any Key]"));
  while (Serial.available() && Serial.read()); // empty buffer
  while (!Serial.available());                 // wait for data
  while (Serial.available() && Serial.read()); // empty buffer again
  mpu.SetAddress(MPU6050_DEFAULT_ADDRESS).CalibrateMPU().load_DMP_Image();// Does it all for you with Calibration
#endif
  mpu.on_FIFO(print_Values);
}

void loop() {
  mpu.dmp_read_fifo();// Must be in loop
}
