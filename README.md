# EV Energy Management & Real-Time Monitoring System (Python, ROS2)


## Overview
This project implements a software-based Electric Vehicle (EV) Energy Management System.
It models vehicle energy consumption, battery State of Charge (SOC), and eco-mode logic,
and extends the system using ROS2 for real-time signal communication.

The project demonstrates how core EV energy algorithms can be integrated into a
ROS2-based automotive software architecture.


## Features
- Physics-based energy consumption model
- City vs highway efficiency analysis (Wh/km)
- Battery State of Charge (SOC) tracking
- SOC-based eco-mode and energy optimization logic
- Modular and extensible software architecture
- ROS2-based real-time energy monitoring
- ROS2 publisher–subscriber communication

## System Architecture

Core EV Logic (Python):
- Vehicle model
- Energy consumption model
- Battery SOC model
- Eco-mode control logic

ROS2 Layer:
- Energy Publisher Node
  - Publishes battery SOC
  - Publishes power consumption
  - Publishes eco-mode status
- Energy Subscriber Node
  - Subscribes to SOC data
  - Demonstrates real-time signal reception


## Tech Stack
- Python
- NumPy
- Matplotlib


## How to Run

### Requirements
- Ubuntu 22.04 / 24.04
- ROS2 (Jazzy or Humble)
- Python 3.10+

### Build ROS2 Workspace
```bash
cd ros2/ws
colcon build
source install/setup.bash


