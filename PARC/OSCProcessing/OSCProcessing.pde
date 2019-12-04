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

import netP5.*;
import oscP5.*;

import processing.serial.*;
OscP5 oscP5;
OscP5 oscP5tcpClient;
NetAddress myRemoteLocation;
Serial myPort;
String val="start";
String prev;
void setup() {
  frameRate(25);
  oscP5 = new OscP5(this,13000);
  //oscP5tcpClient = new OscP5(this, "192.168.2.2", 17000, OscP5.UDP);
  size(800,1000);
  print(Serial.list());
  String portName = Serial.list()[1];
  myPort = new Serial(this, portName, 9600); //2400
  //print(Serial.list());
  myRemoteLocation = new NetAddress("192.168.2.3",12000);
}


void draw() {
  background(0);
  if ( myPort.available() > 0) 
  {  // If data is available,
    val = myPort.readString();
    print (val);
    oscSend(val);
    //print("Sent!");
    // read it and store it in val
  }
  
  if (keyPressed) {
   if (key == '-') {
    hook();
    print("sent!");
   }
  }
  
  ///DRAWING...
  String[] parts = val.split(",");
  textSize(90);
  text(parts[0], 400, 400);
  textAlign(CENTER, CENTER);
  //redraw();
  }

void oscSend(String val) {
  //String[] parts = val.split(",");
  
  OscMessage test = new OscMessage("/test");
  if(val != null) {
  test.add(val);
  //test.add("Test");
  oscP5.send(test, myRemoteLocation);
  }
  flush();
}

void hook () {
 OscMessage hook = new OscMessage("/hook");
 oscP5.send(hook, myRemoteLocation);
}

void oscEvent(OscMessage theOscMessage) {
  /* print the address pattern and the typetag of the received OscMessage */
  print(theOscMessage.get(0));
 // print("### received an osc message.");
  //print(" addrpattern: "+theOscMessage.addrPattern());
  //println(" typetag: "+theOscMessage.typetag());
}