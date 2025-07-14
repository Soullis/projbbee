import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import ambiente as am
import time


class ObjDetectorSub(Node):
    def __init__(self):
        super().__init__("obj_detector_sub")

        self.subscription = self.create_subscription(
            String,
            'detection_topic',
            self.listener_callback,
            10
        )
        self.subscription

        self.last_cmmd = "rf"

    def listener_callback(self, msg):
        if msg.data != "-1":
            start = time.time()
            while time.time() - start < 3:
                am.drone.command("rf")
            start = time.time()
            while time.time() - start < 3:
                am.drone.command("pf")
            start = time.time()
            while time.time() - start < 3:
                am.drone.command("rb")
            am.current_obs += 1
        else:
            if am.drone.pos[0] == 0:
                self.last_cmmd = "rb"
            elif am.drone.pos[0] == 1000:
                self.last_cmmd = "rf"
            am.drone.command(self.last_cmmd)

def main(args=None):
    rclpy.init(args=args)
    obj_detector_sub = ObjDetectorSub()
    rclpy.spin(obj_detector_sub)

    obj_detector_sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
