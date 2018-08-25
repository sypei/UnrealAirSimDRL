from xbox360controller import Xbox360Controller
from xbox360controller import controller
import time

def on_button_pressed(button):
    print('Button {} was pressed \n'.format(button.name))


def on_button_released(button):
    print('Button {0} was released \n'.format(button.name))


def on_axis_moved(axis):
    print('Axis {0} moved to {1} {2} \n'.format(axis.name, axis.x, axis.y))
    
def on_rawaxis_moved(axis):
    print('rawAxis {} moved to {} \n'.format(axis.name, axis._value))
    #print('rawAxis {} moved to \n'.format(axis._value))

while True:
    time.sleep(1)
    crtl = Xbox360Controller(0, axis_threshold=0.2)
    print("hhhhhhhhhhh")
    for i in range(len(crtl.buttons)-1):
        if crtl.buttons[i]._value != crtl.buttons[i]._last_value:
            last_button = i
            last_button_value = crtl.buttons[i]._value
            print("last button:{}    last button value:{}".format(last_button,last_button_value))
            
     
    
    for j in range(len(crtl.axes)-1):
        if isinstance(crtl.axes[j], controller.Axis):
            if (crtl.axes[j]._value_x != crtl.axes[j]._last_value_x)or(crtl.axes[j]._value_y != crtl.axes[j]._last_value_y):
                last_axis = j
                last_axis_value_x = crtl.axis[j]._value_x
                last_axis_value_y = crtl.axis[j]._value_y
                print("last axis:{}    last axis value:{}{}".format(last_axis,last_axis_value_x,last_axis_value_y))
        elif isinstance(crtl.axes[j], controller.RawAxis):
            if crtl.axes[j]._value != crtl.axes[j]._last_value:
                last_axis = j
                last_axis_value = crtl.axis[j]._value
                print("last rawaxis:{}    last rawaxis value:{}".format(last_axis,last_axis_value))





while False:
    time.sleep(1)
    crtl = Xbox360Controller(0, axis_threshold=0.2)
   
    for i in range(len(crtl.axes)-1):
        if i<=2:
            crtl.axes[i].when_moved = on_axis_moved
        elif i>2:
            crtl.axes[i].when_moved = on_rawaxis_moved
        else:
            pass
        #time.sleep(0.01)
        
    for j in range(len(crtl.buttons)-1):
        crtl.buttons[j].when_pressed = on_button_pressed
	crtl.buttons[j].when_released = on_button_released
        #time.sleep(0.01)
        


            
    
    














#import struct
#infile_path = "/dev/input/js0"
#EVENT_SIZE = struct.calcsize("LhBB")
#file = open(infile_path, "rb")
#event = file.read(EVENT_SIZE)
#while event:
#    print(struct.unpack("LhBB", event))
#    (tv_msec,  value, type, number) = struct.unpack("LhBB", event)
#    event = file.read(EVENT_SIZE)



#type=button, number=button number
#msec, value, type, number


# Open the joystick device.
#fn = '/dev/input/js0'
#print('Opening %s...' % fn)
#jsdev = open(fn, 'rb')
#while True:
#    print(jsdev.readline().tostring())
    
