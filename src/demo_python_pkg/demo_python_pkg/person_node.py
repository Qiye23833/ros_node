import rclpy
from rclpy.node import Node

class PersonNode(Node):
    def __init__(self,node_name,name,age):
        super().__init__(node_name)
        self.name=name
        self.age=age

    def eat(self,food):
        # print(f"名字：{self.name}，年龄：{self.age}，吃：{food}")
        self.get_logger().info(f"名字：{self.name}，年龄：{self.age}，吃：{food}")

def main():
    rclpy.init()
    node=PersonNode('node_zhangsan',"张三",22)
    node.eat("苹果")                                
    rclpy.spin(node)
    rclpy.shutdown()
