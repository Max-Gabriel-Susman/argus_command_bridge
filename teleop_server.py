import rclpy, threading, time
from rclpy.node import Node
from geometry_msgs.msg import Twist
from fastapi import FastAPI
import uvicorn

TIMEOUT_S = 0.5          # stop robot if no new cmd arrives

class CmdBridge(Node):
    def __init__(self):
        super().__init__('cmd_bridge')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.last_msg_time = time.time()
        self.create_timer(0.02, self._watchdog)   # 50 Hz watchdog

        # Expose a simple ROS service you can drive from tests or CLI
        self.create_service(Twist, 'direct_cmd_vel', self._direct)

    def _direct(self, req, res):
        self.pub.publish(req)
        self.last_msg_time = time.time()
        return res          # empty OK

    def _watchdog(self):
        if time.time() - self.last_msg_time > TIMEOUT_S:
            self.pub.publish(Twist())   # zero-velocity

    app = FastAPI()

    @app.post("/cmd_vel")
    async def cmd_vel(cmd: dict):
        msg = Twist()
        msg.linear.x  = cmd.get("lx", 0.0)
        msg.angular.z = cmd.get("az", 0.0)
        bridge.pub.publish(msg)
        bridge.last_msg_time = time.time()
        return {"ok": True}

    def run_web():
        uvicorn.run(app, host="0.0.0.0", port=8000)