import pyautogui
import time
print('Press Ctrl+C to Exit')
import win32gui
import webcolors


class colorFinding:
    def mouse_position(self):

        try:
            while True:
                # x, y = pyautogui.position()
                # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                # print(positionStr, end='')
                # print('\b' * len(positionStr), end='', flush=True)
                # print(pyautogui.position())
                x_position=pyautogui.position()[0]
                y_position = pyautogui.position()[1]

                time.sleep(1)

                i_desktop_window_id = win32gui.GetDesktopWindow()
                i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
                long_colour = win32gui.GetPixel(i_desktop_window_dc, x_position, y_position)
                i_colour = int(long_colour)
                r=(i_colour & 0xff)
                g=((i_colour >> 8) & 0xff)
                b=((i_colour >> 16) & 0xff)
                # return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

                requested_color_rgb=(r,g,b)

                min_colours = {}
                for key, name in webcolors.css3_hex_to_names.items():
                    r_c, g_c, b_c = webcolors.hex_to_rgb(key)
                    rd = (r_c - requested_color_rgb[0]) ** 2
                    gd = (g_c - requested_color_rgb[1]) ** 2
                    bd = (b_c - requested_color_rgb[2]) ** 2
                    min_colours[(rd + gd + bd)] = name
                closest=min_colours[min(min_colours.keys())]
                print("closest "+closest)





                # color_name=webcolors.normalize_integer_triplet((r,g,b))
                # color=webcolors.rgb_to_name(color_name)
                # print(color)
        except KeyboardInterrupt:
            print('\nDone')





colorObj=colorFinding()
colorObj.mouse_position()

