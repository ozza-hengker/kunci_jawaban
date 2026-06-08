#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <chrono>

using namespace std;
using namespace std::chrono_literals;

class KapalOtonomNode : public rclcpp::Node {
public:
    KapalOtonomNode() : Node("kapal_otonom") {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/cmd_vel", 10);
        
        // Timer dipanggil setiap 500 milidetik
        timer_ = this->create_wall_timer(
            500ms, std::bind(&KapalOtonomNode::gerak_otomatis, this));
            
        RCLCPP_INFO(this->get_logger(), "Kapal Otonom (C++) Siap!");
    }

private:
    void gerak_otomatis() {
        auto twist = geometry_msgs::msg::Twist();
        twist.linear.x = 0.5;
        twist.angular.z = 0.5;
        publisher_->publish(twist);
    }
    
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(make_shared<KapalOtonomNode>());
    rclcpp::shutdown();
    return 0;
}
