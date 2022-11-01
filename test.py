import modi
import time
import keyboard
import mouse

if __name__ == '__main__':
    # modi.update_module_firmware()
    bundle = modi.MODI()
    gyro, button = bundle.gyros[0], bundle.buttons[0]

    keyboard.wait('space')
    speed = 5
    while True:
        # if button.clicked:
        #     keyboard.write('we are writing')
        # if button.double_clicked:
        #     keyboard.write('double clicked')
        if button.double_clicked:
            break
        if button.clicked:
            mouse.click()
        x, y = -gyro.angular_vel_z, -gyro.angular_vel_x
        mouse.move(speed * x, speed * y, absolute=False, duration=0.1)

    
   


