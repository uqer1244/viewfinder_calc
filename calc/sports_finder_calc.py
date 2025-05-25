

m = 1
d = 40 # distance of frameline and eye

vertical = 48
horizontal = 24

f= 50

# x1.33 with anamorphic adaptor : 48 * 24
# xpan panorama : 65 * 24
# 135 film : 36 * 24
# 120 645 film - vertical 645 : 45 * 60

def k_calc(m,d,f):
    return (vertical*m*d) / f, (horizontal*m*d) / f

kv,kh = k_calc(m, d, f)

print("distance of eye and frameline : %dmm / kv,kh : %.2fmm, %.2fmm" %(d,kv,kh))