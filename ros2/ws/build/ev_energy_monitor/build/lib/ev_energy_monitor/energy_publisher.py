#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class EnergyPublisher(Node):
    def __init__(self):
        super().__init__('energy_publisher')

        self.soc_pub = self.create_publisher(Float32, 'battery_soc', 10)
        self.power_pub = self.create_publisher(Float32, 'power_consumption', 10)
        self.eco_pub = self.create_publisher(String, 'eco_mode_status', 10)

        self.soc = 80.0
        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        power = 15.0
        self.soc -= 0.1

        eco = "Normal"
        if self.soc < 50:
            eco = "ECO"
        if self.soc < 30:
            eco = "Strong ECO"

        self.soc_pub.publish(Float32(data=self.soc))
        self.power_pub.publish(Float32(data=power))
        self.eco_pub.publish(String(data=eco))

        self.get_logger().info(
            f"SOC: {self.soc:.1f}% | Power: {power} kW | Mode: {eco}"
        )

def main():
    rclpy.init()
    node = EnergyPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
