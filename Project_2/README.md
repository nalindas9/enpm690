#Shady Robot Teleop Control and Obstacle Avoidance using Hokuyo Laser RangeFinder

Please follow the steps below to run the simulations:

1. Clone this repository.
2. Navigate to the "Project 2" Folder.
3. Inside you will find the simulation videos for the Shady Robot.
4. You will also find the Project Report titled "ENPM690_HW3_Nalin_Das_Report"
5. Copy the "shady_ws" locally on your computer's home.
6. Navigate to this folder in the terminal.
7. Enter the command "catkin_make" inside this folder to initialize it as a ROS workspace.
8. Once you have done this, go back to home and then source this ROS workspace using "source ~/shady_ws/devel/setup.bash"
9. Once this is done, you can run the Shady Robot Gazebo world simulation using the command - "roslaunch shady_gazebo shady_gazebo_world.launch".
10. You can also run the RVIZ simulation usinf the command - "roslaunch shady_description shady_rviz.launch"
11. Once you have successfully run the gazebo and rviz simulations, run the teleop keyboard program to control the Robot using Keyboard I/P's using the command - "rosrun teleop_twist_keyboard teleop_twist_keyboard.py"
12. To run the obstacle avoidance demo, close the teleop control node using CTRL-C.
13. Then run the python script for initializing the Laser scanner node - "rosrun shady_examples shady_laser_scanner.py"
14. After it runs successfully, you can run the controller node to start the control - "rosrun shady_examples shady_controller.py " 
