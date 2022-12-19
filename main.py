import modi
import time
import keyboard
import mouse

if __name__ == '__main__':
    # modi.update_module_firmware()
    
    bundle = modi.MODI() # 30831ACC
    num_buttons = 12
    Buttons = [bundle.buttons[i] for i in range(num_buttons)]

    # bundle2 = modi.MODI(network_uuid='7B81D22')
    # buttons = bundle2.buttons[0]
    

    gyro = bundle.gyros[0]
    gyro2 = bundle.gyros[1]

    frequent_chars = "abcdefghilmnoprstuwy"

    # keyboard.wait('space')
    speed = 10
    t = 3  # tolerance
    alphabet = {0:'',
                1:'TD',
                2:'ER',
                3:'AL',
                4:'IU',
                5:'NC',
                6:'OM',
                7:'SF',
                8:'HW',
                9:'YG',
                10:'PB',
                11:''
                }
    print('start')
    bundle.print_topology_map(print_id=True)
    #keyboard.wait('space')
    delay = 0.5
    while True:
        if Buttons[0].clicked:
            mouse.click('left')

        if Buttons[0].double_clicked:
            mouse.click('right')

        if Buttons[1].clicked:
            keyboard.write(alphabet[1][0])
            time.sleep(delay)
        if Buttons[1].double_clicked:
            keyboard.write(alphabet[1][1])
            time.sleep(delay)

        if Buttons[2].clicked:
            keyboard.write(alphabet[2][0])
            time.sleep(delay)

        if Buttons[2].double_clicked:
            keyboard.write(alphabet[2][1])
            time.sleep(delay)
        
        if Buttons[3].clicked:
            keyboard.write(alphabet[3][0])
            time.sleep(delay)
        if Buttons[3].double_clicked:
            keyboard.write(alphabet[3][1])
            time.sleep(delay)
        
        if Buttons[4].clicked:
            keyboard.write(alphabet[4][0])
            time.sleep(delay)
        if Buttons[4].double_clicked:
            keyboard.write(alphabet[4][1])
            time.sleep(delay)

        if Buttons[5].clicked:
            keyboard.write(alphabet[5][0])
            time.sleep(delay)
        if Buttons[5].double_clicked:
            keyboard.write(alphabet[5][1])
            time.sleep(delay)

        if Buttons[6].clicked:
            keyboard.write(alphabet[6][0])
            time.sleep(delay)
        if Buttons[6].double_clicked:
            keyboard.write(alphabet[6][1])
            time.sleep(delay)

        if Buttons[7].clicked:
            keyboard.write(alphabet[7][0])
            time.sleep(delay)

        if Buttons[7].double_clicked:
            keyboard.write(alphabet[7][1])
            time.sleep(delay)
        
        if Buttons[8].clicked:
            keyboard.write(alphabet[8][0])
            time.sleep(delay)
        if Buttons[8].double_clicked:
            keyboard.write(alphabet[8][1])
            time.sleep(delay)
        
        if Buttons[9].clicked:
            keyboard.write(alphabet[9][0])
            time.sleep(delay)
        if Buttons[9].double_clicked:
            keyboard.write(alphabet[9][1])
            time.sleep(delay)

        if Buttons[10].clicked:
            keyboard.write(alphabet[10][0])
            time.sleep(delay)
        if Buttons[10].double_clicked:
            keyboard.write(alphabet[10][1])
            time.sleep(delay)         
        
        if Buttons[11].clicked:
            keyboard.press('space')
            time.sleep(delay)
        if Buttons[11].double_clicked:
            keyboard.press('enter')
            time.sleep(delay)    
        
        x, y = gyro.pitch, gyro.roll

        # print(x,y)
        if abs(x) < t:
            x = 0
        if abs(y) < t:
            y = 0
        mouse.move(speed * x, speed * y, absolute=False, duration=0.1)
        x2, y2 = gyro2.pitch, gyro2.roll
        # print(x,y)
        if x2 > t:
            keyboard.press('right arrow')
            time.sleep(3 * delay) 
        if x2 < -1 * t:
            keyboard.press('left arrow')
            time.sleep(3 *delay) 
        if y2 > t:
            keyboard.press('up arrow')
            time.sleep(3 *delay) 
        if y2 < -1 * t -1:
            keyboard.press('down arrow')
            time.sleep(3 *delay) 

    bundle.print_topology_map(print_id=True)
    


