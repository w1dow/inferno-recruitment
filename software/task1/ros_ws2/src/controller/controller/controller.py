#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Controller(Node):
    def __init__(self):
        super().__init__("controller")
        self.pos_sub = self.create_subscription(
            Pose, '/turtle1/pose', self.pos_callback, 10
        )
        self.pos_pub = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )
        self.get_logger().info("Controller started")

    def pos_callback(self, pos: Pose):
        cmd = Twist()

        # Default forward motion
        cmd.linear.x = 2.0
        cmd.angular.z = 0.0

        if pos.x > 9.0 or pos.x < 2.0:
            cmd.angular.z = 1.5   

        if pos.y > 9.0 or pos.y < 2.0:
            cmd.angular.z = 1.5  

        self.pos_pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = Controller()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()