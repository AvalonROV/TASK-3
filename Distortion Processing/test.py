from rospy import *

if(color_red==True):
    
    while(area_red!=True and shapeIdentifier(shapeIdentifier('TRI_R','RECT_R',1,0)):
        
            rosservice call /joint_command -- rad servo_id i #Create a for loop to increment 'i' from -pi/2 to pi/2
            
    if(area_red==True and shapeIdentifier()==True):
        
        rosservice call /joint_command -- rad 1 2.0 #Open Gripper which is Servo 1
        
        while(area_red>400 and area<800):
            rosservice call /joint_command -- rad 3 2.0 #Move servo 3 closer to the red colour until area==800
        rosservice call /joint_command -- rad 1 1.0 #Close Gripper as it should now have the red object
        
    if(area_red!=0): # To check if the red object has been picked up
        #Repeat Line 5-9, until the red object is picked up
    rosservice call /joint_command -- rad 2 2.0 #Make the arm return to the initial position(2.0)
    rosservice call /joint_command -- rad 3 2.0 #Make the arm return to the initial position(2.0)
    rosservice call /joint_command -- rad 3 2.8 #Turn the arm 90˚ to reach the platform where the component can be dropped
    rosservice call /joint_command -- rad 1 2.0 #Open the gripper
    #Come back to this position and repeat this process

        

