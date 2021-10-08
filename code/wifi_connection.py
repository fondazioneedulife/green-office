import network

def main():
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('edu-ospiti', 'Edulife311VR')
        while not sta_if.isconnected():
            pass
    
    print('network config:', sta_if.ifconfig())

if __name__ == '__main__':
    main()