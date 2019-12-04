'''
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
  
 '''
 
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server
import ev3dev
print(int(math.degrees(math.atan(1))))
def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

def testf(unused_addr, args):
  values = args.split(",");
  print(values)
  power = 0
  if (values[0] != None and values[1] != None):
  	x = int(values[0])
  	y = int(values[1])
  if (y == 0):
    y=1

# ms = MoveSteering(left_port='B', right_port='C')
  if (abs(x) < 7 and abs(y) < 7):
    print("Robot is idle")
    randomval = 2
  else: 
    steeringValue = int(math.degrees(math.atan(x/y)))
    # ms.on(steering=steeringValue, power=powerVal)
    print (str(x) + " and " + str(y) + " make "+ str(steeringValue))
  for (motor, power) in zip((left_motor, right_motor), steering(direction=steeringValue, power=powerVal)):
    motor.run_forever(speed_sp=powerVal)
      #print (str(values[0]))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="192.168.2.3", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=12000, help="The port to listen on")
  args = parser.parse_args()



  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/hook", hook)
  dispatcher.map("/test", testf)
  dispatcher.map("/t", print_compute_handler, "Log volume", math.log)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
