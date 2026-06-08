import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class KapalOtonom(Node):
    def __init__(self):
        super().__init__('kapal_otonom')
        # Membuat publisher ke topik /cmd_vel
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Membuat timer untuk mengeksekusi fungsi gerak_otomatis setiap 0.5 detik
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.gerak_otomatis)
        self.get_logger().info("Kapal Otonom Siap! Kapal akan bergerak melingkar.")

    def gerak_otomatis(self):
        twist = Twist()
        
        # Kombinasi linear x dan angular z membuat kapal bergerak melingkar
        twist.linear.x = 0.5   # Kecepatan maju
        twist.angular.z = 0.5  # Kecepatan rotasi/belok
        
        self.publisher_.publish(twist)
        self.get_logger().info(f"Otomatis Mengirim: linear_x={twist.linear.x}, angular_z={twist.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    node = KapalOtonom()
    
    try:
        rclpy.spin(node) # Menjaga node tetap hidup dan menjalankan timer
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
