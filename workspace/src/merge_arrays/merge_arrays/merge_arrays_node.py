import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

# class MergeArraysNode(Node):
#     def __init__(self):
#         super().__init__('merge_arrays_node')

#         # array1 = message_filters.Subscriber('array1', Int32MultiArray)
#         # array2 = message_filters.Subscriber('array2', Int32MultiArray)

#         # ts = message_filters.TimeSynchronizer([array1, array2], 10)
#         # ts.registerCallback(callback)

#         self.subscription = self.create_subscription(
#             Int32MultiArray,
#             '/input/array1',
#             self.listener_callback,
#             10)
#         self.subscription  # prevent unused variable warning

#     def listener_callback(self, msg):
#         self.get_logger().info('I heard: "%s"' % msg.data)


# def main(args=None):
#     rclpy.init(args=args)

#     subscriber = MergeArraysNode()

#     rclpy.spin(subscriber)

#     # Destroy the node explicitly
#     # (optional - otherwise it will be done automatically
#     # when the garbage collector destroys the node object)
#     subscriber.destroy_node()
#     rclpy.shutdown()


# def callback(array1, array2):

#     MergeArraysNode.get_logger().info('I heard: "%s"' % array1.data)
#     MergeArraysNode.get_logger().info('I heard: "%s"' % array2.data)


# if __name__ == '__main__':
#     main()

array1 = Int32MultiArray()
array2 = Int32MultiArray()

haveTopic1 = False
haveTopic2 = False
finalArray = Int32MultiArray()

class MergeNode(Node):
    def __init__(self):
        super().__init__('merge_arrays_node')
        self.publisher_ = self.create_publisher(Int32MultiArray, '/output/array', 10)
        
        topic1_subscription = self.create_subscription(
            Int32MultiArray,
            '/input/array1',
            topic1_callback,
            10  # QoS profile depth
        )
        
        topic2_subscription = self.create_subscription(
            Int32MultiArray,
            '/input/array2',
            topic2_callback,
            10  # QoS profile depth
        )
        
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        self.publisher_.publish(finalArray)
        self.get_logger().info('Publishing: "%s"' % finalArray.data)
    


def topic1_callback(msg):
    # Callback function for the first topic
    array1.data = msg.data
    print(f"Received from Topic 1: {msg.data}")
    do_merge()


def topic2_callback(msg):
    # Callback function for the second topic
    array2.data = msg.data
    print(f"Received from Topic 2: {msg.data}")
    do_merge()


def do_merge():
    merged_list = []
    i = 0
    j = 0
    print(array1.data)
    print(array2.data)
    if (len(array1.data) == 0 or len(array2.data) == 0):
        return
    
    for x in range(0, len(array1.data) + len(array2.data)):
        if array1.data[i] < array2.data[j]:
            merged_list.append(array1.data[i])
            if (i < len(array1.data) - 1):
                i += 1
            else:
                break
        else:
            merged_list.append(array2.data[j])
            if (j < len(array2.data) - 1):
                j += 1
            else:
                break

    if (len(array1.data) - 1 == i):  
        for z in range (j, len(array2.data)):
            merged_list.append(array2.data[z])

    if (len(array2.data) - 1 == j):  
        for z in range (i, len(array1.data)):
            merged_list.append(array1.data[z])

    print(f"Merged List: {merged_list}")
    finalArray.data = merged_list

def main(args=None):
    rclpy.init(args=args)
    # Create subscriptions for two different topics
    node = MergeNode()

    # Spin the node to listen for messages
    rclpy.spin(node)

    # Cleanup
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

