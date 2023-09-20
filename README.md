# dexhand_usb_serial
ROS2 serial connection package for communicating with DexHand firmware across a USB Serial Connection

## What Does This Package Do?
This package is a ROS 2 node that provides a communication bridge between ROS 2 and a USB Serial connection to the firmware running on the DexHand microcontroller. This firmware is available on GitHub Here - [DexHand-BLE Repository](https://github.com/iotdesignshop/dexhand-ble).

## ROS 2 Message Formats
The package is pretty simple, there are really two messages - input and output. These are tied to debug functions that are built into the firmware.

`dexhand_hw_command` - (Subscribed) Sends a string based command to the firmware via USB. [The commands supported by the firmware are described here](https://github.com/iotdesignshop/dexhand-ble).

`dexhand_hw_response` - (Published) Publishes string messages sent by the firmware back to ROS 2


## ROS 2 Command Line

To run the package:

`ros2 run dexhand_usb_serial usb_serial`

By default, it assumes the Arduino is connected to /dev/ttyACM0, and attempts to connect there. You can override this port by specifying the `serial_port` parameter on the command line.


