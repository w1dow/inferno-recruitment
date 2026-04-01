import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/w1dow/inferno/software/task1/ros_ws2/install/controller'
