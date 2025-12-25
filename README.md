# FOKA USV - Onboard Control System (ROS 2 / RPi 4) 🚤

This repository contains the source code for the control system running on the onboard computer (**Raspberry Pi 4B**) of the **FOKA** autonomous boat. This project was developed as part of my Engineering Thesis: *"Steering algorithms of floating robots"*.

![FOKA USV](foka_boat.png)
*Fig 1. The FOKA robot during field tests on the Oder River.*

## 🌟 About Project FOKA

I am the **founder and project lead** of Project FOKA. This initiative was dedicated to developing an autonomous research platform of the USV (Unmanned Surface Vehicle) class.

Key project achievements:
* **Full-scale Construction:** Developed a fully functional catamaran-type robot from scratch.
* **Funding:** Successfully secured **EU grants** and **ministerial funding** for research and development.
* **Innovation:** Implemented original control and navigation algorithms tailored for small-scale autonomous vessels.

## ⚙️ System Architecture (ROS 2)

The system is built on the **ROS 2** framework and consists of several specialized packages (located in the `src/` directory) that handle hardware abstraction and low-level logic:

* **`gps_reader`**: Interfaces with the GPS module (UART/NMEA) to provide real-time global positioning.
* **`imu_reader`**: Manages the Inertial Measurement Unit (LSM9DS1) via I2C to provide acceleration, angular velocity, and magnetic field data.
* **`motor_controller`**: Controls the BLDC motors using PWM signals via ESC drivers.
* **`radio_reader`**: Interfaces with the RC receiver for manual override and safety control.
* **`aggregator`**: Collects and synchronizes data from all sensors for logging or further fusion.
* **`telemetry_handler`**: Manages real-time data logging to `.csv` files (stored in the `data/` folder) and handles communication with the Ground Control Station (GCS).



### Hardware Specifications
* **Main Computer:** Raspberry Pi 4B (Running Ubuntu Server 22.04)
* **Sensors:** GPS (Waveshare L76K), IMU (LSM9DS1 9-DoF)
* **Propulsion:** 2x BLDC Underwater Thrusters in a differential drive configuration
* **Power:** Custom Li-Ion Battery Pack (5S8P)



## 🚀 Getting Started

The system is designed to be self-contained. Startup scripts are located in the root directory:

```bash
# Grant execution permissions (one-time)
chmod +x start_ros.sh

# Launch the complete ROS 2 stack
./start_ros.sh
