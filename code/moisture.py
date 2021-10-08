import machine

def main():
    adc = machine.ADC(0) # Pin to Read sensor voltage

    try:

        ######################
        # Sensor calibration #
        ######################

        # values on right are inverse * 1000 values on left
        # dry air = 759 (0%) = 1.31752305665349143610013175231
        # water = 382 (100%) = 2.61780104712041884816753926702
        # The Difference     = 1.30027799046692741206740751471
        # 1 %                = 0.0130027799046692741206740751471

        SoilMoistVal = (((1 / adc.read())* 1000) / 0.0130027799046692741206740751471) - 101
        if SoilMoistVal > 100:
            SoilMoistVal = 100
        if SoilMoistVal < 0:
            SoilMoistVal = 0
            
        print(SoilMoistVal)

        '''url = 'http://192.168.1.2:8000/nodemcu_2'
        headers = {'content-type': 'application/json'}
        data = '{"Value": "%s", "Time": "%s"}' % (SoilMoistVal, timestr)
        resp = urequests.post(url, data=data, headers=headers) # Send the request
        print(resp.json())'''

    except:
        machine.reset()
    
if __name__ == '__main__':
    main()