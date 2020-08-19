# Make sure that you're wheel diameter is correct:
wheel_diameter=62.4

# Aditionally if you're robot is not using some of the sensors or motors that we're using, make sure you go to line 340 and edit the devices

import pygame
import tkinter as tk
from tkinter import filedialog
import time
import math
import os

root = tk.Tk()

# All comands under "measure"

def measure():
    measureWindow = tk.Toplevel(root)
    measureWindow.title("Measurements")
    measureCanvas = tk.Canvas(measureWindow, width=200, bg="white")
    measureCanvas.pack()
    measureFrame = tk.Frame(measureWindow, bg="white")
    measureFrame.place(relwidth=1, relheight=1)
    labels = ["measure"]
    pygame.init()

    global turnCount

    win = pygame.display.set_mode((1326, 629))
    winLine = pygame.display.set_mode((1326, 629))
    pygame.display.set_caption("Viusal Navigation (Measure)")

    x=50
    y=50
    width = 40
    height=40
    radius=20
    vel=5
    bg = pygame.image.load("/Users/abdur-rahman/Desktop/Python Code/FIRST-LEGO-League-Challenge-Mat-single.jpg")
    win.blit(bg, (0,0))
    
    def redrawGameWidnow():
        pygame.display.update()

    run = True
    while run:
        pygame.time.delay(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x-=vel
        if keys[pygame.K_RIGHT]:
            x+=vel
        if keys[pygame.K_DOWN]:
            y+=vel
        if keys[pygame.K_UP]:
            y-=vel
        if pygame.mouse.get_pressed()[0]:
            cursorPos = pygame.mouse.get_pos()
            x = cursorPos[0]
            y = cursorPos[1]
        if keys[pygame.K_q]:
            cursorPos = pygame.mouse.get_pos()
            x = cursorPos[0]
            y = cursorPos[1]
            pygame.draw.circle(win, (48, 155, 255), (x,y), 15)
            lastPoint= cursorPos
            print(f"x_y_config({cursorPos[0]}, {(cursorPos[1]* -1)})")
            labels.append(f"x_y_config({cursorPos[0]}, {(cursorPos[1]* -1)})")
            del labels[0]
            for label in labels:
                measureLabel = tk.Label(measureWindow, text=label, font=20)
                measureLabel.pack()


        if keys[pygame.K_f]:
            cursorPos = pygame.mouse.get_pos()
            currentPoint = cursorPos
            pygame.draw.circle(win, (235, 64, 52), currentPoint, 15)
            pygame.draw.line(winLine, (235, 64, 52), lastPoint, currentPoint, 5)
            print(f"waypoint({cursorPos[0]}, {(cursorPos[1]* -1)})")
            lastPoint=currentPoint
            labels.append(f"waypoint({cursorPos[0]}, {(cursorPos[1]* -1)})")
            del labels[0]
            for label in labels:
                measureLabel = tk.Label(measureWindow, text=label, font=20)
                measureLabel.pack()

        if keys[pygame.K_l]:
            cursorPos = pygame.mouse.get_pos()
            currentPoint = cursorPos
            x1 = lastPoint[0]
            y1 = lastPoint[1]*-1
            x2 = currentPoint[0]
            y2 = currentPoint[1]*-1
            pygame.draw.circle(win, (0,0,255), currentPoint, 15)
            pygame.draw.line(winLine, (0,0,255), lastPoint, currentPoint, 5)
            distance = math.sqrt(((x2-x1)**2+(y2-y1)**2)*3.65*360/(wheel_diameter*math.pi))
            print(f"line_follow({distance})")
            labels.append(f"line_follow({distance})")
            del labels[0]
            for label in labels:
                measureLabel = tk.Label(measureWindow, text=label, font=20)
                measureLabel.pack()
            lastPoint=currentPoint

        if keys[pygame.K_t]:
            cursorPos = pygame.mouse.get_pos()
            currentPoint = cursorPos
            x1 = lastPoint[0]
            y1 = lastPoint[1]*-1
            x2 = currentPoint[0]
            y2 = currentPoint[1]*-1
            pygame.draw.circle(win, (4, 217, 57), currentPoint, 15)
            if x2>x1 and y2>y1:
                angle = (math.atan(abs(x2-x1)/abs(y2-y1)))*180/math.pi
            if x2>x1 and y2<y1:
                angle = (math.atan(abs(y2-y1)/abs(x2-x1)))*180/math.pi+90
            if x2<x1 and y2>y1:
                angle = (math.atan(abs(x2-x1)/abs(y2-y1)))*-180/math.pi
            if x2<x1 and y2<y1:
                angle = ((math.atan(abs(y2-y1)/abs(x2-x1)))*-180/math.pi)-90
            if x2==x1 and y2>y1:
                angle = 0
            if x2==x1 and y2<y1:
                angle = 180
            if x2>x1 and y2==y1:
                angle = 90
            if x2<x1 and y2==y1:
                angle = 270
            print(f"turn({angle})")
            labels.append(f"turn({angle})")
            del labels[0]
            for label in labels:
                measureLabel = tk.Label(measureWindow, text=label, font=20)
                measureLabel.pack()

        redrawGameWidnow()

    pygame.quit()

# All comands under "write to existing file"

def exist():
    measureWindow = tk.Toplevel(root)
    measureWindow.title("Measurements")
    measureCanvas = tk.Canvas(measureWindow, width=200, bg="white")
    measureCanvas.pack()
    measureFrame = tk.Frame(measureWindow, bg="white")
    measureFrame.place(relwidth=1, relheight=1)
    labels = ["measure"]
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select target file",filetypes = (("python files","*.py"),("all files","*.*")))
    f = open(f"{filename}", "a")
    pygame.init()

    global turnCount

    win = pygame.display.set_mode((1326, 629))
    winLine = pygame.display.set_mode((1326, 629))
    pygame.display.set_caption("Viusal Navigation (Measure)")

    x=50
    y=50
    width = 40
    height=40
    radius=20
    vel=5

    bg = pygame.image.load("/Users/abdur-rahman/Desktop/Python Code/FIRST-LEGO-League-Challenge-Mat-single.jpg")
    win.blit(bg, (0,0))
    
    def redrawGameWidnow():
        pygame.display.update()

    run = True
    while run:
        pygame.time.delay(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x-=vel
            turnCount+=1
        if keys[pygame.K_RIGHT]:
            x+=vel
        if keys[pygame.K_DOWN]:
            y+=vel
        if keys[pygame.K_UP]:
            y-=vel
        if pygame.mouse.get_pressed()[0]:
            cursorPos = pygame.mouse.get_pos()
            x = cursorPos[0]
            y = cursorPos[1]
        if keys[pygame.K_q]:
            cursorPos = pygame.mouse.get_pos()
            x = cursorPos[0]
            y = cursorPos[1]
            pygame.draw.circle(win, (48, 155, 255), (x,y), 15)
            lastPoint= cursorPos
            print(f"x_y_config({cursorPos[0]}, {(cursorPos[1]* -1)})")
            labels.append(f"x_y_config({cursorPos[0]}, {(cursorPos[1]* -1)})")
            del labels[0]
            for label in labels:
                measureLabel = tk.Label(measureWindow, text=label, font=20)
                measureLabel.pack()
            f.write('''
''')
            f.write(f"x_y_config({cursorPos[0]}, {(cursorPos[1]* -1)})")
            f.write('''
''')
        if keys[pygame.K_f]:
            cursorPos = pygame.mouse.get_pos()
            currentPoint = cursorPos
            pygame.draw.circle(win, (235, 64, 52), currentPoint, 15)
            pygame.draw.line(winLine, (235, 64, 52), lastPoint, currentPoint, 5)
            print(f"waypoint({cursorPos[0]}, {(cursorPos[1]* -1)})")
            labels.append(f"waypoint({cursorPos[0]}, {(cursorPos[1]* -1)})")
            del labels[0]
            for label in labels:
                measureLabel = tk.Label(measureWindow, text=label, font=20)
                measureLabel.pack()
            f.write('''
''')
            f.write(f"waypoint({cursorPos[0]}, {(cursorPos[1]* -1)})")
            f.write('''
''')
            lastPoint=currentPoint

        if keys[pygame.K_l]:
            cursorPos = pygame.mouse.get_pos()
            currentPoint = cursorPos
            x1 = lastPoint[0]
            y1 = lastPoint[1]*-1
            x2 = currentPoint[0]
            y2 = currentPoint[1]*-1
            pygame.draw.circle(win, (0,0,255), currentPoint, 15)
            pygame.draw.line(winLine, (0,0,255), lastPoint, currentPoint, 5)
            distance = math.sqrt(((x2-x1)**2+(y2-y1)**2)*3.65*360/(wheel_diameter*math.pi))
            print(f"line_follow({distance})")
            labels.append(f"line_follow({distance})")
            del labels[0]
            for label in labels:
                measureLabel = tk.Label(measureWindow, text=label, font=20)
                measureLabel.pack()
            f.write('''
''')
            f.write(f"line_follow({distance})")
            f.write('''
''')
            lastPoint=currentPoint

        if keys[pygame.K_t]:
            cursorPos = pygame.mouse.get_pos()
            currentPoint = cursorPos
            x1 = lastPoint[0]
            y1 = lastPoint[1]*-1
            x2 = currentPoint[0]
            y2 = currentPoint[1]*-1
            pygame.draw.circle(win, (4, 217, 57), currentPoint, 15)
            if x2>x1 and y2>y1:
                angle = (math.atan(abs(x2-x1)/abs(y2-y1)))*180/math.pi
            if x2>x1 and y2<y1:
                angle = (math.atan(abs(y2-y1)/abs(x2-x1)))*180/math.pi+90
            if x2<x1 and y2>y1:
                angle = (math.atan(abs(x2-x1)/abs(y2-y1)))*-180/math.pi
            if x2<x1 and y2<y1:
                angle = ((math.atan(abs(y2-y1)/abs(x2-x1)))*-180/math.pi)-90
            if x2==x1 and y2>y1:
                angle = 0
            if x2==x1 and y2<y1:
                angle = 180
            if x2>x1 and y2==y1:
                angle = 90
            if x2<x1 and y2==y1:
                angle = 270
            labels.append(f"turn({angle})")
            del labels[0]
            for label in labels:
                measureLabel = tk.Label(measureWindow, text=label, font=20)
                measureLabel.pack()
            print(f"turn({angle})")
            f.write('''
''')
            f.write(f"turn({angle})")
            f.write('''
''')

        redrawGameWidnow()

    pygame.quit()

# All comands under "write to new file"
def new():
    newWindow = tk.Toplevel(root)
    newWindow.title("Enter Folder Name")
    canvasnew = tk.Canvas(newWindow, width=600, bg="white")
    canvasnew.pack()
    newFrame = tk.Frame(newWindow, bg = "white")
    newFrame.place(relwidth = 1, relheight = 1)
    entry = tk.Entry(newFrame, font = 40, bg = "#b8e1ff")
    entry.place(relwidth = 0.8, relheight = 0.4, relx=0.2, rely=0.2)

    button = tk.Button(newFrame, text="Enter", fg="#3c73e8", font=40, command = lambda: assign(entry.get()))
    button.place(relwidth = 0.2 , relheight=0.4, rely=0.2)
    
    measureWindow = tk.Toplevel(root)
    measureWindow.title("Measurements")
    measureCanvas = tk.Canvas(measureWindow, height=200, width=200, bg="white")
    measureCanvas.pack()
    measureFrame = tk.Frame(measureWindow, bg="white")
    measureFrame.place(relwidth=1, relheight=1)
    labels = ["measure"]

    def assign(entry):
        folder_name = entry
        
        os.makedirs(f"/Users/abdur-rahman/Desktop/Robot Things/Robot Code/{folder_name}/.vscode")

        main_file1 = open(f"/Users/abdur-rahman/Desktop/Robot Things/Robot Code/{folder_name}/main.py", "x")
        main_file1.write(f'''#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Modules
import math

# Devices
ev3 = EV3Brick()
rightlm = Motor(Port.A)
leftlm = Motor(Port.B)
gyro = GyroSensor(Port.S2)
rights = ColorSensor(Port.S1)
robot = DriveBase(leftlm, rightlm, {wheel_diameter}, 96)

# Functions
def x_y_config(lastx_, lasty_):
    global lastx
    global lasty
    lastx = lastx_
    lasty = lasty_

def waypoint(currentx, currenty, angle_changer=0, target_speed=150):
    # Distance calculated with pythagorean theorem
    global lastx
    global lasty
    distance = math.sqrt((currentx-lastx)**2+(currenty-lasty)**2)*1.556
    # Series of logic gates to figure out angle between line and x axis using inverse of tan

    if currentx>lastx and currenty>lasty:
        currentangle = (math.atan(abs(currentx-lastx)/abs(currenty-lasty)))*180/math.pi
    if currentx>lastx and currenty<lasty:
        currentangle = (math.atan(abs(currenty-lasty)/abs(currentx-lastx)))*180/math.pi+90
    if currentx<lastx and currenty>lasty:
        currentangle = (math.atan(abs(currentx-lastx)/abs(currenty-lasty)))*-180/math.pi
    if currentx<lastx and currenty<lasty:
        currentangle = ((math.atan(abs(currenty-lasty)/abs(currentx-lastx)))*-180/math.pi)-90
    if currentx==lastx and currenty>lasty:
        angle = 0
    if currentx==lastx and currenty<lasty:
        angle = 180
    if currentx>lastx and currenty==lasty:
        angle = 90
    if currentx<lastx and currenty==lasty:
        angle = 270

    print("Current gyro angle before turn is")
    print(gyro.angle())
    print(" ")
    print("Target distance in mm is")
    print(distance)
    print(" ")

    currentangle1 = currentangle+0
    if currentangle>=0:
        currentangle2 = currentangle-360
    else:
        currentangle2 = currentangle+360

    if abs(gyro.angle() - currentangle1) < abs(gyro.angle() - currentangle2):
    
        print("Target angle is")
        print(currentangle1)
        print(" ")

        if gyro.angle()>currentangle1:
            while gyro.angle()>currentangle1+3.9-angle_changer:
                rightlm.run(90)
                leftlm.run(-90)
        else:
            while gyro.angle()<currentangle1-3.9+angle_changer:
                rightlm.run(-90)
                leftlm.run(90)
    else:
        print("Target angle is")
        print(currentangle2)
        print(" ")

        if gyro.angle()>currentangle2:
            while gyro.angle()>currentangle2+3.9-angle_changer:
                rightlm.run(90)
                leftlm.run(-90)
        else:
            while gyro.angle()<currentangle2-3.9+angle_changer:
                rightlm.run(-90)
                leftlm.run(90)

    print("gyro angle after turn is")
    print(gyro.angle())
    print(" ")
    print("time needed to drive")
    time = abs(distance/target_speed*1000)
    print(time)
    
    # Execution of drive command
    print("______________________________________________________________")
    print(" ")
    robot.drive_time(target_speed, 0, time)

    lastx = currentx
    lasty = currenty

def button():
    while True:
        pressed = Button.CENTER in ev3.buttons.pressed()
        if pressed:
            break

def turn(target_angle, turn_speed=90):
    if target_angle>gyro.angle():
        while gyro.angle()<target_angle-4:
            rightlm.run(-1*turn_speed)
            leftlm.run(turn_speed)
    else:
        while gyro.angle()>target_angle+4:
            rightlm.run(turn_speed)
            leftlm.run(-1*turn_speed)


def waypoint_drive(x, y, objective_speed=150):
    global lastx 
    global lasty
    distance = math.sqrt((abs(x-lastx))**2+(abs(x-lastx))**2)
    time = distance/objective_speed*1000
    robot.drive(objective_speed, 0, time)

def line_follow(distance, l_r_sensor='r', l_r='r',  speed=120):
    derivative = 0
    integral = 0
    last_error = 0
    speed_factor=2
    kp = 0.45
    ki = 0.0015
    kd = 0.4
    if l_r  == 'l':
        a = 1
    if l_r =='r':
        a = -1
    if l_r_sensor == 'r':
        while leftlm.angle()<distance:
            proportional = rsensor.reflection()-45
            integral += proportional
            steering = a*((kp * proportional)+(ki*integral)+(kd*derivative))
            drive_speed = speed-(speed_factor*(abs(proportional-last_error)))
            robot.drive(drive_speed, steering)
            last_error = proportional
            derivative = last_error-proportional
        robot.stop()

    else:
        while leftlm.angle()<distance:
            proportional = lsensor.reflection()-45
            integral += proportional
            steering = a*((kp * proportional)+(ki*integral)+(kd*derivative))
            drive_speed = speed-(speed_factor*(abs(proportional-last_error)))
            robot.drive(drive_speed, steering)
            last_error = proportional
            derivative = last_error-proportional
        robot.stop()

# Commands
ev3.speaker.beep()

''')

        extension = open(f"/Users/abdur-rahman/Desktop/Robot Things/Robot Code/{folder_name}/.vscode/extensions.json", "x")
        extension.write('''{
        // See http://go.microsoft.com/fwlink/?LinkId=827846 to learn about workspace recommendations.
        // Extension identifier format: ${publisher}.${name}. Example: vscode.csharp

        // List of extensions which should be recommended for users of this workspace.
        "recommendations": [
            "lego-education.ev3-micropython"
        ],
        // List of extensions recommended by VS Code that should not be recommended for users of this workspace.
        "unwantedRecommendations": [
            "ms-python.python"
        ]
    }''')

        launch = open(f"/Users/abdur-rahman/Desktop/Robot Things/Robot Code/{folder_name}/.vscode/launch.json", "x")
        launch.write('''{
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Download and Run",
                "type": "ev3devBrowser",
                "request": "launch",
                "program": "/home/robot/${workspaceRootFolderName}/main.py"
            }
        ]
    }''')

        settings = open(f"/Users/abdur-rahman/Desktop/Robot Things/Robot Code/{folder_name}/.vscode/settings.json", "x")
        settings.write('''// Place your settings in this file to overwrite default and user settings.
        {
        "files.eol": "\n",
        "debug.openDebug": "neverOpen",
        "python.linting.enabled": false
    }''')

        gitignore = open(f"/Users/abdur-rahman/Desktop/Robot Things/Robot Code/{folder_name}/.gitignore", "x")
        gitignore.write('''__pycache__/
    *.pyc
    venv/''')

        f = open(f"/Users/abdur-rahman/Desktop/Robot Things/Robot Code/{folder_name}/main.py", 'a')
        pygame.init()


        win = pygame.display.set_mode((1326, 629))
        winLine = pygame.display.set_mode((1326, 629))
        pygame.display.set_caption("Viusal Navigation (Measure)")

        x=50
        y=50
        width = 40
        height=40
        radius=20
        vel=5

        bg = pygame.image.load("/Users/abdur-rahman/Desktop/Python Code/FIRST-LEGO-League-Challenge-Mat-single.jpg")
        win.blit(bg, (0,0))
        
        def redrawGameWidnow():
            pygame.display.update()

        run = True
        while run:
            pygame.time.delay(120)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                x-=vel
            if keys[pygame.K_RIGHT]:
                x+=vel
            if keys[pygame.K_DOWN]:
                y+=vel
            if keys[pygame.K_UP]:
                y-=vel
            if pygame.mouse.get_pressed()[0]:
                cursorPos = pygame.mouse.get_pos()
                x = cursorPos[0]
                y = cursorPos[1]
            if keys[pygame.K_q]:
                cursorPos = pygame.mouse.get_pos()
                x = cursorPos[0]
                y = cursorPos[1]
                pygame.draw.circle(win, (48, 155, 255), (x,y), 15)
                lastPoint = cursorPos
                print(f"x_y_config({cursorPos[0]}, {(cursorPos[1]* -1)})")
                labels.append(f"x_y_config({cursorPos[0]}, {(cursorPos[1]* -1)})")
                del labels[0]
                for label in labels:
                    measureLabel = tk.Label(measureWindow, text=label, font=20)
                    measureLabel.pack()
                f.write('''
''')
                f.write(f"x_y_config({cursorPos[0]}, {(cursorPos[1]* -1)})")
                f.write('''
''')
            if keys[pygame.K_f]:
                cursorPos = pygame.mouse.get_pos()
                currentPoint = cursorPos
                pygame.draw.circle(win, (235, 64, 52), currentPoint, 15)
                pygame.draw.line(winLine, (235, 64, 52), lastPoint, currentPoint, 5)
                print(f"waypoint({cursorPos[0]}, {(cursorPos[1]* -1)})")
                labels.append(f"waypoint({cursorPos[0]}, {(cursorPos[1]* -1)})")
                del labels[0]
                for label in labels:
                    measureLabel = tk.Label(measureWindow, text=label, font=20)
                    measureLabel.pack()
                f.write('''
''')
                f.write(f"waypoint({cursorPos[0]}, {(cursorPos[1]* -1)})")
                f.write('''
''')
                lastPoint=currentPoint

            if keys[pygame.K_l]:
                cursorPos = pygame.mouse.get_pos()
                currentPoint = cursorPos
                x1 = lastPoint[0]
                y1 = lastPoint[1]*-1
                x2 = currentPoint[0]
                y2 = currentPoint[1]*-1
                pygame.draw.circle(win, (0,0,255), currentPoint, 15)
                pygame.draw.line(winLine, (0,0,255), lastPoint, currentPoint, 5)
                distance = math.sqrt(((x2-x1)**2+(y2-y1)**2)*3.65*360/(wheel_diameter*math.pi))
                print(f"line_follow({distance})")
                labels.append(f"line_follow({distance})")
                del labels[0]
                for label in labels:
                    measureLabel = tk.Label(measureWindow, text=label, font=20)
                    measureLabel.pack()
                f.write('''
''')
                f.write(f"line_follow({distance})")
                f.write('''
''')
                lastPoint=currentPoint

            if keys[pygame.K_t]:
                cursorPos = pygame.mouse.get_pos()
                currentPoint = cursorPos
                x1 = lastPoint[0]
                y1 = lastPoint[1]*-1
                x2 = currentPoint[0]
                y2 = currentPoint[1]*-1
                pygame.draw.circle(win, (4, 217, 57), currentPoint, 15)
                if x2>x1 and y2>y1:
                    angle = (math.atan(abs(x2-x1)/abs(y2-y1)))*180/math.pi
                if x2>x1 and y2<y1:
                    angle = (math.atan(abs(y2-y1)/abs(x2-x1)))*180/math.pi+90
                if x2<x1 and y2>y1:
                    angle = (math.atan(abs(x2-x1)/abs(y2-y1)))*-180/math.pi
                if x2<x1 and y2<y1:
                    angle = ((math.atan(abs(y2-y1)/abs(x2-x1)))*-180/math.pi)-90
                if x2==x1 and y2>y1:
                    angle = 0
                if x2==x1 and y2<y1:
                    angle = 180
                if x2>x1 and y2==y1:
                    angle = 90
                if x2<x1 and y2==y1:
                    angle = 270
                labels.append(f"turn({angle})")
                del labels[0]
                for label in labels:
                    measureLabel = tk.Label(measureWindow, text=label, font=20)
                    measureLabel.pack()
                print(f"turn({angle})")
                f.write('''
''')
                f.write(f"turn({angle})")
                f.write('''
''')

            redrawGameWidnow()

        pygame.quit()


# Main GUI

root.title("Visual Navigation Main Menu")

canvas = tk.Canvas(root, height = 800, width = 800, bg="white")
canvas.pack()

frame = tk.Frame(root, bg="#e6e6e6")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

title = tk.Label(frame, text="FLL Visual Navigation", bg="#7595d1")
title.place(relwidth = 0.75, relheight = 0.1, relx=0.125, rely=0.125)
title.config(font=("Courier", 30))

measure_button = tk.Button(frame, text="measure", fg="#ff2200", font = 40, command=measure)
measure_button.place(relwidth=0.3, relheight = 0.08, anchor="n", relx=0.33, rely=0.5)

exist_button = tk.Button(frame, text="write to existing file", fg="#ba19ff", font = 40, command=exist)
exist_button.place(relwidth=0.3, relheight = 0.08, anchor="n", relx=0.66, rely=0.5)

new_button = tk.Button(frame, text="write to new file", fg="#3c73e8", font = 40, command=new)
new_button.place(relwidth=0.631, relheight = 0.08, anchor="nw", relx=0.18, rely=0.615)

root.mainloop()