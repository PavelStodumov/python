import time

class TraficLight:
    __color = None
    def running(self):
        TraficLight.__color = 'red'
        print(TraficLight.__color)
        time.sleep(7)
        TraficLight.__color = 'yellow'
        print(TraficLight.__color)
        time.sleep(2)
        TraficLight.__color = 'green'
        print(TraficLight.__color)
        time.sleep(2)
        TraficLight.__color = None


light = TraficLight()
light.running()
