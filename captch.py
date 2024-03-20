import random
ch="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
captch=""
for _ in range(5):
    captch+=random.choice(ch)
print("Genrating Captcha:",captch)