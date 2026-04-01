#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircle(Node):
    def __init__(self):
        super().__init__("trtlcontroller")
        self.publisher = self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.create_timer(0.5,self.sendvel)
        self.get_logger().info("moving turle")
    def sendvel(self):
        msg=Twist()
        msg.linear.x=2.0
        msg.angular.z=1.0
        self.publisher.publish(msg)
        
        
def main(args=None):
    rclpy.init(args=args)
    node = DrawCircle()
    rclpy.spin(node)
    rclpy.shutdown()

