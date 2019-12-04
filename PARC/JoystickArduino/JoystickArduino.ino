/*
 * 
 *  Name: Anish Ghai
 *  School: Parramatta High School
 *  My inputs are the joystick and the button. The raw values are remapped 
 *  thrown into Processing, where it gets OSC'd to the MindStorms robot. 
 *  The Python OSC Server listening for the data packets then, assigns x and y variables
 *  and uses tan inverse to calculate the relative angle. The relative angle is then used 
 *  to control the direction of the robot for a fluid movement experience, and the y value 
 *  is assigned to the power so that it controls the acceleration
 *  
 *  My ouputs are the GUI in Processing which show the speed at which the Robot is currently going at. 
 *  My other output is the RGB Light, which show the current state of the robot. Green = Moving. Red = IDLE.
 *  
  To use the device:
  1) Flash EV3DEV operating system to your EV3.
  2) Establish a network connection between your EV3 and your computer.
  3) Open a shell terminal and SSH into the EV3.
  4) Upload the python script into your EV3 via SSH (pythonOSCServer..py)
  5) Upload the Arduino code to the Arduino
  6) Upload the Processing code.
  7) Execute Python script and wait (approx 10-15 seconds) while it starts up a server.
  8) Launch Processing.
  9) Control the Robot and have fun!
  
 */

#include <Esplora.h>
#include <Keyboard.h>
int joyX;
int joyY;
int speedX;
int speedY;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //2400 best
}

void loop() {
  int slider = Esplora.readSlider();
  int hook = map(slider, 1023, 0, 93, -72);
  //Serial.println(hook);
  int button = Esplora.readButton(SWITCH_DOWN);
  // put your main code here, to run repeatedly:
  if (button == LOW) {
    Keyboard.press('-');
    delay(10);
    //Keyboard.releaseAll();
  } else {
    Keyboard.releaseAll();
  }
  joyX = Esplora.readJoystickX();
  joyY = Esplora.readJoystickY();
  speedX = map(joyX, 512, -512, -100, 100);
  speedY = map(joyY, 512,-512,-100,100);
  Serial.println(speedX);
  Serial.print(",");
  Serial.print(speedY);
  Serial.println();
  delay(200);
  if (abs(speedX) < 20 && abs(speedY) < 20) {
    Esplora.writeRGB(255,0,0);
  } else {
    Esplora.writeRGB(0, 255, 0);
    
  }
  }
