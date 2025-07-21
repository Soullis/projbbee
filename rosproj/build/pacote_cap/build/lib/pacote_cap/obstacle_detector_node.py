import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from geometry_msgs.msg import Point
from . import ambiente as am

class ObsDetector(Node):
    def __init__(self):
        super().__init__("obstacle_detector")

        self.current_drone_position = None

        self.obstacle_publisher_ = self.create_publisher(Bool, '/obstacle/detected', 10)

        self.position_subscriber_ = self.create_subscription(
            Point,
            '/drone/position',
            self.position_callback,
            10
        )

        self.detectio_timer_ = self.create_timer(0.5, self.run_detection_logic)

    def position_callback(self, msg):
        self.current_drone_position = msg

    def run_detection_logic(self):
        if self.current_drone_position is None:
            return
        
        obstacle_is_present = self.check_for_obstacles()

        msg = Bool()
        msg.data = obstacle_is_present
        self.obstacle_publisher_.publish(msg)

    def check_for_obstacles(self):
        for obstacle in am.obstaculos:
            if (obstacle.limits(8)[0] <= self.current_drone_position.x <= obstacle.limits(8)[1]) and (self.current_drone_position.y <= obstacle.posY <= self.current_drone_position + 200):
                return True
            return False

        


def main(args=None):
    rclpy.init(args=args)

    obs_detector = ObsDetector()
    
    rclpy.spin(obs_detector)

    obs_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
