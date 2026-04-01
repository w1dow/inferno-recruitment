import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class getpos(Node):
    def __init__(self):
        super().__init__("get_pose")
        self.subscriber=self.create_subscription(Pose,'/turtle1/pose',self.call,10)
    
    def call(self,msg:Pose):
        self.get_logger().info(str(msg))
        
        
    
    
def main(args=None):
    rclpy.init(args=args)
    node = getpos()
    rclpy.spin(node)
    rclpy.shutdown()