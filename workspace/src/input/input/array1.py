import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class Array1(Node):
    def __init__(self):
        super().__init__('array1')
        self.publisher_ = self.create_publisher(Int32MultiArray, '/input/array1', 10)
        
        # msg.data = [0, 2, 4, 5, 6]
        # self.publisher_.publish(msg)
        # self.get_logger().info('Publishing: "%s"' % msg.data)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int32MultiArray()
        msg.data = [0, 2, 4, 5, 6]
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)



def main(args=None):
    rclpy.init(args=args)

    array1 = Array1()

    rclpy.spin(array1)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    array1.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
