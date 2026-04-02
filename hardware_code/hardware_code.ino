/*
  Ping))) Sensor

  This sketch reads a PING))) ultrasonic rangefinder and returns the distance
  to the closest object in range. To do this, it sends a pulse to the sensor to
  initiate a reading, then listens for a pulse to return. The length of the
  returning pulse is proportional to the distance of the object from the sensor.

  The circuit:
	- +V connection of the PING))) attached to +5V
	- GND connection of the PING))) attached to ground
	- SIG connection of the PING))) attached to digital pin 7

  created 3 Nov 2008
  by David A. Mellis
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  https://docs.arduino.cc/built-in-examples/sensors/Ping/
*/

#include <Servo.h>

Servo myservo;

// initialise variables
int servoPos = 0;
long duration;
long inches;

// initialise constants
const int trigPin = 13;
const int echoPin = 12;
const int servoPin = 10;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialise pin modes 
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  // attach the servoPin to the servo object 
  myservo.attach(servoPin);

  Serial.print("Position");
  Serial.print(" ");
  Serial.print("Distance");
  Serial.println();
}

void loop() {

  for (servoPos = 0; servoPos <= 180; servoPos +=1) {
    myservo.write(servoPos);
    delay(5);
    Serial.print(servoPos);
    Serial.print(" ");
    long inches = recordDistance();
  }

  for (servoPos = 180; servoPos >= 0; servoPos -=1) {
    myservo.write(servoPos);
    delay(5);
    Serial.print(servoPos);
    Serial.print(" ");
    long inches = recordDistance();
  }
}


int recordDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(trigPin, LOW);

  // The same pin is used to read the signal from the PING))): a HIGH pulse
  // whose duration is the time (in microseconds) from the sending of the ping
  // to the reception of its echo off of an object.
  duration = pulseIn(echoPin, HIGH);

  // convert the time into a distance
  inches = microsecondsToInches(duration);

  Serial.print(inches);
  Serial.println();

  delay(5);
  return inches;
}

long microsecondsToInches(long microseconds) {
  // According to Parallax's datasheet for the PING))), there are 73.746
  // microseconds per inch (i.e. sound travels at 1130 feet per second).
  // This gives the distance travelled by the ping, outbound and return,
  // so we divide by 2 to get the distance of the obstacle.
  // See: https://www.parallax.com/package/ping-ultrasonic-distance-sensor-downloads/
  return microseconds / 74 / 2;
}

