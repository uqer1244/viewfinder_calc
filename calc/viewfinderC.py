pcv_fl_list = [-25,-35,-50,-100]
pcx_fl_list = [12,15,18,20,24,25,30,36,42,48,50,54,60,72,84,100]

vertical = 24
horizontal = 48

f = 50

# x1.33 with anamorphic adaptor : 48 * 24
# xpan panorama : 65 * 24
# 135 film : 36 * 24
# 120 645 film - vertical 645 : 45 * 60

# m = |f1|/|f2|
# d = f1 + f2
# k_len = (vertical * m * d) / f
# k_height  = (horizontal * m * d) / f

def k_calc(m,d,f):
    return (vertical*m*d) / f, (horizontal*m*d) / f

def dia_calc(kv,kh) :
    return (kv**2+kh**2)**0.5

tmp = []
for f1 in pcv_fl_list:
    for f2 in pcx_fl_list:
        m = abs(f1) / abs(f2)
        if 0.5 < m < 0.9: # magnification maximum / minimum
            d = f1+f2
            kv, kh = k_calc(m,d,f)
            dia = dia_calc(kv,kh)
            tmp.append([f1,f2,m,d,kv,kh,dia])

print(tmp)
for i in tmp:
    print("pcv = %d / pcx = %d / m = %f / d = %d / kv,kh = %f * %f / dia = %f" %(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))