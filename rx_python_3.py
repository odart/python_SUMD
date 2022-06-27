#!/usr/bin/env python3
import serial
import time

class Receiver:

    START_BYTE = 0xA8 
    FRAME_LEN = 29
    NUM_CHANNELS = 12


    def __init__(self, port):

        self._frame = bytearray()
        self.ser = serial.Serial(
            port,
            baudrate=115200,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE
            )
        self.frames = self.ser.read(size=Receiver.FRAME_LEN*3)
        self.data_received(self.frames)   

    def data_received(self, data):
        self._in_frame = False
        for b in data:
            if self._in_frame:
                self._frame.append(b)              
                if len(self._frame) == Receiver.FRAME_LEN:
                    decoded_frame = self.decode( self._frame)
                    #print('decoded', decoded_frame)
                    self._in_frame = False
                    del self.frames  
                    self.frames = self.ser.read(size=Receiver.FRAME_LEN*3)
                    
            else:
                if b == Receiver.START_BYTE:
                    self._in_frame = True
                    i=0
                    self._frame.clear()
                    self._frame.append(b)

    def decode(self, frame):
        self.Channels = [None] * Receiver.NUM_CHANNELS
        channel_sum_data=[]
        for n in range(len(frame)-5):
            channel_sum_data.append(frame[3+n])
        val=0
        for ch in range(0, Receiver.NUM_CHANNELS):
            self.Channels[ch] = channel_sum_data[val]*32 + channel_sum_data[(val+1)]/8#channel_sum & 0xff #0x7ff
            val=val+2
        return self.Channels

def main(port='COM9'): #'/dev/ttyS0'
    sumd = Receiver(port)
    channels=sumd.Channels
    #print('ch 1',channels[0],'ch 2',channels[1],'ch 3',channels[2],'ch 4',channels[3],'ch 5',channels[4],
          #'ch 6',channels[5],'ch 7',channels[6],'ch 8',channels[7])
    return channels

        
if __name__ == '__main__':
    while True:
        channels = main()
        print(channels)
        time.sleep(.3)

