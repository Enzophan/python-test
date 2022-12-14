import wifi_qrcode_generator as qr
import matplotlib.pyplot as plt

# qr.wifi_qrcode('Vnpt', False, 'WPA', 'hiennhan47')
data = qr.wifi_qrcode('TOTOLINK_A3', False, 'WPA', 'hiennhan47')


plt.imshow(data)
plt.axis('off') # this will remove the axes from the chart 
plt.show()

