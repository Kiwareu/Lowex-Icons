import math,cairosvg
from make2 import *
def ftile(inner):  # flag tile: no gloss gradient bg; flag fills clip
    return tile('#fff',inner)
def star(cx,cy,r,col='#fff',n=5,rot=-90,inner=None):
    inner=inner or r*0.382;pts=[]
    for i in range(n*2):
        a=math.radians(rot+i*180/n);rr=r if i%2==0 else inner;pts.append(f'{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="{col}"/>'
F={}
F['JP']=ftile('<rect width="512" height="512" fill="#fff"/><circle cx="256" cy="256" r="130" fill="#e60026"/>')
F['FR']=ftile('<rect width="171" height="512" fill="#2442a8"/><rect x="171" width="170" height="512" fill="#fff"/><rect x="341" width="171" height="512" fill="#e1262d"/>')
F['DE']=ftile('<rect width="512" height="171" fill="#222"/><rect y="171" width="512" height="171" fill="#dd0000"/><rect y="342" width="512" height="170" fill="#ffce00"/>')
F['US']=ftile(''.join(f'<rect y="{i*39.4}" width="512" height="39.4" fill="{"#d22a3a" if i%2==0 else "#fff"}"/>' for i in range(13))+'<rect width="240" height="276" fill="#2a3a8c"/>'+''.join(star(30+i*38+(19 if r%2 else 0),28+r*34,11) for r in range(7) for i in range(6 if r%2==0 else 5)))
F['UK']=ftile('<rect width="512" height="512" fill="#1f3a8a"/><path d="M0 0 L512 512 M512 0 L0 512" stroke="#fff" stroke-width="90"/><path d="M0 0 L512 512 M512 0 L0 512" stroke="#d22a3a" stroke-width="34"/><path d="M256 0 V512 M0 256 H512" stroke="#fff" stroke-width="140"/><path d="M256 0 V512 M0 256 H512" stroke="#d22a3a" stroke-width="84"/>')
F['EU']=ftile('<rect width="512" height="512" fill="#1f45a8"/>'+''.join(star(256+150*math.cos(i*math.pi/6),256+150*math.sin(i*math.pi/6),24,'#ffd91c') for i in range(12)))
F['SG']=ftile('<rect width="512" height="256" fill="#ee2536"/><rect y="256" width="512" height="256" fill="#fff"/><circle cx="170" cy="130" r="80" fill="#fff"/><circle cx="198" cy="130" r="74" fill="#ee2536"/>'+''.join(star(262+66*math.cos(math.radians(-90+i*72)),128+66*math.sin(math.radians(-90+i*72)),20) for i in range(5)))
F['HK']=ftile('<rect width="512" height="512" fill="#de2910"/>'+''.join(f'<ellipse cx="256" cy="176" rx="34" ry="86" fill="#fff" transform="rotate({i*72} 256 256)"/>' for i in range(5))+'<circle cx="256" cy="256" r="26" fill="#de2910"/>')
F['TW']=ftile('<rect width="512" height="512" fill="#e11d3b"/><rect width="256" height="256" fill="#1f3b9a"/><circle cx="128" cy="128" r="70" fill="#fff"/><circle cx="128" cy="128" r="56" fill="#1f3b9a"/><circle cx="128" cy="128" r="46" fill="#fff"/>')
F['KR']=ftile('<rect width="512" height="512" fill="#fff"/><path d="M146 256 A110 110 0 0 1 366 256 A55 55 0 0 1 256 256 A55 55 0 0 0 146 256Z" fill="#cd2e3a"/><path d="M366 256 A110 110 0 0 1 146 256 A55 55 0 0 1 256 256 A55 55 0 0 0 366 256Z" fill="#0047a0"/><g stroke="#000" stroke-width="16"><path d="M60 80 L110 40 M45 105 L95 65 M75 55 L125 15" transform="translate(0 40)"/><path d="M402 472 L452 432 M417 447 L467 407 M387 497 L437 457" transform="translate(0 -40)"/></g>')
F['OT']=tile('#3aa0ff','<circle cx="256" cy="256" r="160" fill="none" stroke="#fff" stroke-width="24"/><ellipse cx="256" cy="256" rx="70" ry="160" fill="none" stroke="#fff" stroke-width="20"/><path d="M96 256 H416 M120 170 H392 M120 342 H392" stroke="#fff" stroke-width="18"/>','#1262d6')
# core + s:
C={}
C['cn']=tile('#e8423f',txt('中',256,336,260,'#ffd84a',wt=900),'#b01d1d')
C['private']=tile('#7a8599','<path d="M256 110 L420 250 H376 V400 H136 V250 H92Z" fill="#fff"/><rect x="226" y="290" width="60" height="110" rx="10" fill="#7a8599"/>','#4a5365')
C['proxy-fallback']=tile('#ff7a59','<path d="M256 100 L400 156 V270 C400 350 336 400 256 428 C176 400 112 350 112 270 V156Z" fill="#fff"/><path d="M196 262 L240 306 L322 214" fill="none" stroke="#ff7a59" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>','#d83c1c')
C['s-proxy']=tile('#ff6fa8','<path d="M256 90 C330 140 350 230 330 330 H182 C162 230 182 140 256 90Z" fill="#fff"/><circle cx="256" cy="210" r="34" fill="#ff6fa8"/><path d="M182 290 L130 350 L190 336Z M330 290 L382 350 L322 336Z" fill="#fff"/><path d="M226 350 Q256 430 286 350Z" fill="#ffd25a"/>','#d93a7a')
C['s-direct']=tile('#3ccf91','<path d="M110 256 H380 M300 170 L390 256 L300 342" fill="none" stroke="#fff" stroke-width="44" stroke-linecap="round" stroke-linejoin="round"/>','#17986a')
C['s-final']=tile('#9a6bff','<path d="M150 110 V410" stroke="#fff" stroke-width="30" stroke-linecap="round"/><path d="M164 130 H380 L330 190 L380 250 H164Z" fill="#fff"/>','#5a34d6')
C['s-update']=tile('#4fb6ff','<path d="M390 220 A140 140 0 0 0 150 170 M122 120 V190 H192" fill="none" stroke="#fff" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/><path d="M122 292 A140 140 0 0 0 362 342 M390 392 V322 H320" fill="none" stroke="#fff" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>','#1f7ae0')
C['s-home']=tile('#ffa24a','<path d="M256 100 L420 246 H378 V404 H134 V246 H92Z" fill="#fff"/><path d="M226 404 V300 H286 V404" fill="#ffa24a"/>','#f0641e')
C['s-autoAll']=tile('#ffd25a','<path d="M290 90 L150 290 H244 L222 424 L362 224 H268Z" fill="#fff"/>','#f59e0b')
C['s-manAll']=tile('#6a7dff','<path d="M200 270 V160 a24 24 0 0 1 48 0 V230 V130 a24 24 0 0 1 48 0 V230 V150 a24 24 0 0 1 48 0 V300 C344 380 300 420 250 420 C200 420 170 380 150 330 L124 276 a24 24 0 0 1 42 -24Z" fill="#fff"/>','#3a44d6')
C['s-lb']=tile('#2fc4a5','<g fill="none" stroke="#fff" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"><path d="M112 190 H330 M280 130 L340 190 L280 250"/><path d="M400 322 H182 M232 262 L172 322 L232 382"/></g>','#13957c')
out=[]
for k,v in F.items():
    cairosvg.svg2png(bytestring=v.encode(),write_to=f'{OUT}/region-{k}.png',output_width=512,output_height=512);out.append('region-'+k)
for k,v in C.items():
    cairosvg.svg2png(bytestring=v.encode(),write_to=f'{OUT}/{k}.png',output_width=512,output_height=512);out.append(k)
print(len(out))
