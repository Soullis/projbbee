import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.append(parent_dir)

import ambiente as am

class ObjDetector(Node):
    def __init__(self, max_obs):
        super().__init__("obj_detector_pub")

        self.publisher_ =self.create_publisher(String, 'detection_topic', 10)

        timer_period = 0.5

        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.max_obs = max_obs
        self.current_obs = 0

    def timer_callback(self):
        msg = String()
        if am.obstaculos[i].limits(8)[0] <= am.drone.pos[0] <= am.obstaculos[self.current_obs].limits(8)[1] and am.drone.obj_detector_range[0] <= am.obstaculos[self.current_obs].posY <= am.drone.obj_detector_range[1]:
            msg.data = f"{am.obstaculos[self.current_obs].posY - am.drone.pos[2]}"
        else:
            msg.data = "-1"

        self.publisher_.publish(msg)

        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)

    obj_detector_pub = ObjDetector()
    
    rclpy.spin(obj_detector_pub)

    obj_detector_pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
