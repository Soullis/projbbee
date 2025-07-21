import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from . import ambiente

from pacote_cap.srv import SendCommand


class ControladorDrone(Node):
    def __init__(self):
        super().__init__('drone_controller')

        self.drone = ambiente.drone
        self.command_service = self.create_service(SendCommand, 'drone/send_command', self.command_callback)
    
        self.position_publisher_ = self.create_publisher(Point, "drone/position", 10)
        self.position_timer_ = self.create_timer(0.5, self.publish_position)

    def command_callback(self, request, response):
        command_str = request.command

        try:
            self.drone.command(command_str)
            response.success = True
        
        except Exception as e:
            self.get_logger().error(f"Falha ao executar comando: '{command_str}': {e}")
            response.success = False

        return response
    
    def publish_position(self):
        x, y, z = self.drone.pos

        msg = Point()
        msg.x = float(x)
        msg.y = float(y)
        msg.z = float(z)

        self.position_publisher_.publish(msg)
        self.get_logger.info(f"Drone Pos: {[msg.x, msg.y, msg.z]}")
    

def main(args=None):
    rclpy.init(args=args)
    drone_controller = ControladorDrone()
    rclpy.spin(drone_controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

