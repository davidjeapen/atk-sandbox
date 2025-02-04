import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray

class MergeArraysNode(Node):

    def __init__(self):
        super().__init__('merge_arrays_node')
        self.subscription = self.create_subscription(
            Int32MultiArray,
            'array1',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    subscriber = MergeArraysNode()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

