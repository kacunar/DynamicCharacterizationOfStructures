
n = input('Digite tiempo de prueba = ')
f = input('Digitar frecuencia de muestreo = ')
t = 1./f
k = n*f 

from adxl345 import ADXL345
import time
import xlwt
from datetime import datetime
import matplotlib.pyplot as plt
tiempo = datetime.now()

estilo = xlwt.easyxf('font: name Times New Roman,colour black, bold on')
estilo1 = xlwt.easyxf('font: name Times New Roman,colour black')
wb = xlwt.Workbook()
ws = wb.add_sheet('Mediciones RB')
ws.write(0,0,'X',estilo)
ws.write(0,1,'Y',estilo)
ws.write(0,2,'Z',estilo)
ws.write(0,3,'time',estilo)

a=0
b=0
while (a<k):  
  adxl345 = ADXL345()
    
  axes = adxl345.getAxes(True)
  print "ADXL345 on address 0x%x:" % (adxl345.address)
  print " x =  %.3fG" % ( axes['x'] )
  print " y =  %.3fG" % ( axes['y'] )
  print " z =  %.3fG" % ( axes['z'] )
  print " "
 
  ws.write(a+1,0,'%.4f' % (axes['x']*9.8 ),estilo1)
  ws.write(a+1,1,'%.4f' % (axes['y']*9.8 ),estilo1)
  ws.write(a+1,2,'%.4f' % (axes['z']*9.8 ),estilo1)
  ws.write(a+1,3,b,estilo1)
  
  b = b + t
  a=a+1
  time.sleep(t)


wb.save('medicionRB%s.xls')
print"Se acabo la prueba de",n,"segundos con una frecuencia de",f,"Hz"," y se tomaron",k,"datos"

