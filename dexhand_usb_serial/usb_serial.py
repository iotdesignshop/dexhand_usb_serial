import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class USBSerialNode(Node):
    def __init__(self):
        super().__init__('usb_serial')

        # Get the serial port parameter with a default value of '/dev/ttyACM0'
        self.declare_parameter("serial_port", "/dev/ttyACM0")
        serial_port = self.get_parameter("serial_port").get_parameter_value().string_value
        
        self.publisher_ = self.create_publisher(String, 'dexhand_hw_response', 10)
        self.subscription = self.create_subscription(String, 'dexhand_hw_command', self.listener_callback, 10)
        
        self.serial_conn = serial.Serial(serial_port, 9600)
        self.timer = self.create_timer(0.1, self.read_from_serial)

    def listener_callback(self, msg):
        message = msg.data+'\n'
        self.get_logger().info('Sending to Arduino: "%s"' % message)
        self.serial_conn.write(message.encode('utf-8'))

    def read_from_serial(self):
        if self.serial_conn.in_waiting:
            response = self.serial_conn.readline().decode('utf-8').strip()
            self.get_logger().info('Received from Arduino: "%s"' % response)
            msg = String()
            msg.data = response
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    dexhand_node = USBSerialNode()
    rclpy.spin(dexhand_node)
    dexhand_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
