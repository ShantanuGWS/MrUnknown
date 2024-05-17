#base by GWS(QR_Code_Generator.)
#re-upload? recode? copy code? give credit :)
#YouTube: http://www.youtube.com/@DCsArpit
#Instagram: @dcsradioyt12
#Telegram: t.me/gws143
#GitHub: @ShantanuGWS
#WhatsApp: +918090541900
#want more free scripts? subscribe to my youtube channel: https://youtube.com/@DCsArpit
#owner: GWS - Unknown Gamer
#Author: Shantanu Patel

logo = """
  ______        ______  
 / ___\ \      / / ___| 
| |  _ \ \ /\ / /\___ \ 
| |_| | \ V  V /  ___) |
 \____|  \_/\_/  |____/ 

"""

print(logo)

style = """

Owner: Gaming World Studio OR Mr.Unknown

Script Creater: Shantanu

YT Channel: http://www.youtube.com/@DCsArpit 

Github: ShantanuGWS
"""
print(style)

import qrcode as qr

while True:
    inp = input("Enter Any Text Or Website URL For QR Code:")
    img = qr.make(inp)
    save_name = input("Enter Name Of QR With Extension Of png\nEx:- Hello.png:")
    img.save(save_name)
    print("\nQR Generated Successfull!. Go And Search QR Name In Your Mobile Phone Storage\n")

