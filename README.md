# python_SUMD

Python driver from Graupner SUMD protocol.

Based on:
  
  -https://www.deviationtx.com/media/kunena/attachments/98/HoTT-SUMD-Spec-REV01-12062012-pdf.pdf
  
  -https://github.com/Benoit3/Sumd-for-Arduino
  
  
Tested with GR-12L Reciever on Windows and Ubuntu 16.04 with USB to serial converter (cp210x type).


There are two versions of the python file 2.7 and 3 which correspond to the tested python version. In 2.7 the bytes have to be handled differently.


TODO:
*Implement CRC calculation
*Read Byte 2 as number of channels
*Incorporate FailSafe

