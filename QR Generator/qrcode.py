import pyqrcode 
from pyqrcode import QRCode 
  
s = "Hello"

url = pyqrcode.create(s) 
  
url.svg("myqr.svg", scale = 8) 
