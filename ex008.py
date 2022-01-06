v1 = float(input('Um valor em metros:'))
km = v1/1000
hm = v1/100
dam = v1/10
dm = v1*10
cm = v1*100
mm = v1*1000
print('KM:{}\nHM:{}\nDAM:{}\nDM:{:.0f}\nCM:{:.0f}\nMM:{:.0f}\n'.format(km, hm, dam, dm, cm, mm))


v1 = float(input('Um valor em metros:'))
print('KM:{}\nHM:{}\nDAM:{}\nDM:{:.0f}\nCM:{:.0f}\nMM:{:.0f}\n'.format(v1/1000, v1/100, v1/10, v1*10, v1*100, v1*1000))
