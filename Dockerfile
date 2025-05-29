FROM ros:foxy

RUN apt-get update && apt-get install -y \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*

# FastAPI / uvicorn only if you expose a web API
RUN pip3 install fastapi "uvicorn[standard]"

COPY argus_command_bridge /ws/src/argus_command_bridge
WORKDIR /ws
RUN . /opt/ros/foxy/setup.sh && colcon build --event-handlers console_direct+

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["ros2", "run", "argus_command_bridge", "teleop_server"]
