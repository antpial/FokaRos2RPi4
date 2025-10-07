#!/bin/bash

# Uruchomienie ROS2 launch
echo "[INFO] Startowanie: ros2 launch system_launcher launch_all.py"
ros2 launch system_launcher launch_all.py &

# Poczekaj chwilę na start węzłów (opcjonalne, np. 5 sekund)
sleep 5

# Uruchomienie telemetry
echo "[INFO] Startowanie: ros2 run telemetry telemetry"
ros2 run telemetry telemetry
