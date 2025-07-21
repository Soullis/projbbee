import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from pacote_cap.srv import SendCommand
import time


class Navigator(Node):
    def __init__(self):
        super().__init__("obj_detector_sub")

        self.obstacle_subscriber = self.create_subscription(
            Bool,
            "/obstacle_detected",
            self.listener_callback,
            10
        )
        self.obstacle_subscriber

        
        self.command_client = self.create_client(SendCommand, 'drone/send_command')


    def obstacle_callback(self, msg):
        if msg.data is True:
            self.get_logger().warn("Obstacle detected!")
            time_duration = 3

            start = time.time()
            while time.time() - start < time_duration:
                self.send_drone_command('rf')
            start = time.time()
            while time.time() - start < time_duration:
                self.send_drone_command('pb')
            start = time.time()
            while time.time() - start < time_duration:
                self.send_drone_command('rb')
        else:
            self.send_drone_command('rf')


    def send_drone_command(self, cmd_string):
        request = SendCommand.Request()

        request.command = cmd_string

        self.command_client.call_async(request)


def main(args=None):
    rclpy.init(args=args)
    drone_navigator = Navigator()
    rclpy.spin(drone_navigator)

    drone_navigator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
