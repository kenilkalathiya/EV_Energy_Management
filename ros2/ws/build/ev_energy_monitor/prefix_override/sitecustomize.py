import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kenil/ev-energy-management/ros2/ws/install/ev_energy_monitor'
