# Dynamixel - Moveit
Move dynamixel motors with moveit.


Dynamixel-Moveit documentation

The package orange_controller is not needed for moveit!

The only important web page to consider is the following if the goal is to move real dynamixel with moveit:
https://emanual.robotis.com/docs/en/platform/openmanipulator_x/ros_controls/

Create a catkin workspace and clone these packages:

$ cd ~/catkin_ws/src/
$ git clone https://github.com/ROBOTIS-GIT/open_manipulator_controls.git
$ git clone https://github.com/ROBOTIS-GIT/open_manipulator_dependencies.git
Create an additional package called for example robot_description, create a urdf folder and place your urdf or xacro inside.

Use the moveit setup assistant to create the robot_moveit_config package, and remember to generate also the ros_controllers.yaml file needed control real robots (while doing the setup assistant)

Copy the content of the following launch file: open_manipulator_controls/open_manipulator_controllers/launch/joint_trajectory_controller.launch

And paste it for example in robot_moveit_config/launch (I called the new launch file: dynamixel_open_moveit.launch)

The following step is to delete all the script nedded for Gazebo and modify the remaining code to match it with your custom robot and no more with the open_manipulator.

By setting sim=false we are disabling Gazebo and activating the real robot. Remember to set you correct usb port.

  <arg name="sim" default="false"/>
  <arg name="usb_port" default="/dev/ttyUSB0" />

Instead, inside this following file, set your correct usb port as well as the baud_rate of your motors (if you don’t know them, check them using the Dynamixel Wizard 2 software):

  <include file="$(find open_manipulator_hw)/launch/open_manipulator_control.launch">

In the hardware.yaml file write the joint names of your robot (also used in the urdf or xacro) and the ID (again, the ID can be found using Wizard 2):

  <arg name="yaml_file" default="$(find open_manipulator_hw)/config/hardware.yaml"/>

The last line of the open_manipulator_control.launch calls the xacro, modify it accordingly to match you xacro file and location. I case you are using a urdf, substitute the line with:

<param name="robot_description" textfile="$(find robot_description)/urdf/robot.urdf" />

Going back to dynamixel_open_moveit.launch file, the last part needs to be modified:

  <group unless="$(arg sim)">
    <rosparam file="$(find open_manipulator_controllers)/config/joint_trajectory_controller.yaml" command="load"/>
  </group>
  <node name="arm_controller_spawner" pkg="controller_manager" type="controller_manager" respawn="false" output="screen" args="spawn robot_arm_controller"/>

In  joint_trajectory_controller.yaml substitute the first line with your controller name, e.g. robot_arm_controller (this name must be specified in the launch file, as you can see above in bolt) and write your joint names. Delete the gripper controller if you don’t have one.
In  joint_trajectory_controller.yaml you can speify the type, either position_controller or effort_controller, make sure it is the same you specified also in the urdf or xacro.
