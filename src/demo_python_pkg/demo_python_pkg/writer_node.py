import rclpy
from rclpy.node import Node
from demo_python_pkg.person_node import PersonNode

class WriterNode(PersonNode):
    def __init__(self,node_name,name,age,book):
        super().__init__(node_name,name,age)
        self.book=book

    def write(self,content):
        # print(f"名字：{self.name}，年龄：{self.age}，写：{content},书名：{self.book}")
        self.get_logger().info(f"名字：{self.name}，年龄：{self.age}，写：{content},书名：{self.book}")

def main():
    rclpy.init()
    node=WriterNode('node_lisi',"李四",23,"红楼梦")
    node.write("你好")
    node.eat("苹果")
    rclpy.spin(node)
    rclpy.shutdown()

