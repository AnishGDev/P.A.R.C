
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
