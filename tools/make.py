import re,cairosvg,os
OUT='./icons-out'
def path(f):return re.search(r' d="([^"]+)"',open(f).read()).group(1)
def tile(bg,inner,bg2=None,defs=''):
    bg2=bg2 or bg
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{bg}"/><stop offset="1" stop-color="{bg2}"/></linearGradient>
<linearGradient id="gl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="c"><rect width="512" height="512" rx="120"/></clipPath>{defs}</defs>
<g clip-path="url(#c)"><rect width="512" height="512" fill="url(#bg)"/>{inner}
<ellipse cx="256" cy="40" rx="300" ry="190" fill="url(#gl)"/></g></svg>'''
def glyph(f,fill,s=17,cx=256,cy=256,vb=24):
    return f'<g transform="translate({cx-vb*s/2},{cy-vb*s/2}) scale({s})"><path fill="{fill}" d="{path(f)}"/></g>'
W='#fff'
def stroke(inner,col=W,w=22):return f'<g fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{inner}</g>'
def bank(col=W,extra='',sc=1):
    # classic bank building, no currency symbol
    return f'''<g transform="translate(256 262) scale({sc}) translate(-256 -262)"><path d="M256 120 L400 196 H112 Z" fill="{col}"/>
<rect x="128" y="214" width="42" height="124" rx="10" fill="{col}"/><rect x="198" y="214" width="42" height="124" rx="10" fill="{col}"/>
<rect x="272" y="214" width="42" height="124" rx="10" fill="{col}"/><rect x="342" y="214" width="42" height="124" rx="10" fill="{col}"/>
<rect x="108" y="356" width="296" height="34" rx="14" fill="{col}"/><rect x="92" y="400" width="328" height="30" rx="14" fill="{col}"/>{extra}</g>'''
def txt(t,x,y,size,fill=W,fam="Noto Sans CJK SC, DejaVu Sans",wt=800,anchor='middle',ls=0):
    return f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" font-weight="{wt}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{t}</text>'
I={}
# ---- brands
I['bunq']=tile('#ffffff',glyph('bunq.svg','url(#rb)',s=19),defs='<linearGradient id="rb" x1="0" x2="1"><stop offset="0" stop-color="#ff3b30"/><stop offset=".25" stop-color="#ffb800"/><stop offset=".5" stop-color="#34c759"/><stop offset=".75" stop-color="#1e90ff"/><stop offset="1" stop-color="#9b51e0"/></linearGradient>')
I['sumup']=tile('#1f2933',f'<g transform="translate(76 76) scale(15)"><path fill="#fff" d="{path("sumup.svg")}"/></g>','#0b0f14')
I['whatsapp']=tile('#4ee07f',glyph('whatsapp.svg',W,s=17),'#1fb855')
I['hsbc']=tile('#ffffff',glyph('hsbc.svg','#db0011',s=17),'#f1f1f1')
I['blizzard']=tile('#1a2a4a',glyph('battledotnet.svg','#00aeff',s=18),'#0a1226')
I['twitter']=tile('#2b2b2b',glyph('x.svg',W,s=16),'#000')
I['meta']=tile('#ffffff',glyph('meta.svg','#0668e1',s=18),'#eaf2ff')
# Maya: neon green, black wordmark
I['maya']=tile('#3dff9b',txt('maya',256,296,150,'#0b0b0b',fam='Mulish, DejaVu Sans',wt=900,ls=-4),'#00c46a')
# Kraken: purple tile, ghost-like dome glyph
I['krak']=tile('#8a5cff',f'''<path d="M256 108 C168 108 118 168 118 248 V330 C118 372 168 380 168 332 C168 392 224 392 224 336 C224 372 256 380 256 346 C256 380 288 372 288 336 C288 392 344 392 344 332 C344 380 394 372 394 330 V248 C394 168 344 108 256 108Z" fill="#fff"/>
''','#5b36d9')
# Bybit: dark tile, white BY with yellow Y
I['bybit-eu']=tile('#2a2c33',''.join(txt(c,px,290,96,col,fam='DejaVu Sans',wt=900,anchor='start') for c,px,col in [('B',106,'#fff'),('Y',170,'#f7a600'),('B',230,'#fff'),('I',296,'#fff'),('T',338,'#fff')])+'<rect x="110" y="322" width="292" height="16" rx="8" fill="#f7a600"/>','#14151a')
# MEXC: blue, white M of two chevrons
I['mexc']=tile('#2f86ff',f'''<path d="M110 372 V170 L190 270 L256 190 L322 270 L402 170 V372 H350 V262 L322 296 L256 216 L190 296 L162 262 V372Z" fill="#fff" stroke="#fff" stroke-width="10" stroke-linejoin="round"/>''','#0f5ee0')
# Bitget: dark tile, cyan B-like mark
I['bitget-wallet']=tile('#22262e',f'''<g fill="none" stroke="#00f0ff" stroke-width="40" stroke-linecap="round" stroke-linejoin="round"><path d="M170 120 V392 H290 C350 392 380 360 380 322 C380 284 350 256 300 256 H170"/><path d="M170 256 H300 C340 256 360 230 360 200 C360 168 336 120 290 120 H170" stroke="#00b8ff"/></g>''','#10131a')
# Blackcat: black tile, white cat head
I['blackcat']=tile('#3a3a40','''<path d="M126 140 L206 206 C236 196 276 196 306 206 L386 140 V300 C386 368 330 410 256 410 C182 410 126 368 126 300 Z" fill="#fff"/>
<ellipse cx="212" cy="290" rx="20" ry="30" fill="#1b1b1f"/><ellipse cx="300" cy="290" rx="20" ry="30" fill="#1b1b1f"/><path d="M240 336 H272 L256 356Z" fill="#ff7aa8"/>''','#0c0c0e')
# ---- generic bank family (blue gradient), no currency
B1,B2='#5aa9ff','#2f6bff'
I['bank-overseas']=tile(B1,bank(extra='')+'<g transform="translate(372 372)"><circle r="62" fill="#fff"/><circle r="62" fill="none" stroke="#2f6bff" stroke-width="12"/><ellipse rx="26" ry="62" fill="none" stroke="#2f6bff" stroke-width="10"/><path d="M-62 0H62" stroke="#2f6bff" stroke-width="10"/></g>',B2)
I['bank-eu']=tile('#3a6bff',bank(sc=.86,extra='')+''.join(f'<circle cx="{256+86*__import__("math").cos(a*3.14159/6)}" cy="{80+0}" r="0"/>' for a in range(0)) ,'#1e3fb8').replace('</g></svg>','</g></svg>')
import math
stars=''.join(f'<circle cx="{256+60*math.cos(i*math.pi/6)}" cy="{120+60*math.sin(i*math.pi/6)}" r="10" fill="#ffd84a"/>' for i in range(12))
I['bank-eu']=tile('#3a6bff',bank(sc=.78,extra='').replace('translate(256 262)','translate(256 300)')+f'<g transform="translate(0 -2)">{stars}</g>','#1e3fb8')
I['bank-hk']=tile('#ff5a6e',bank(sc=.86)+'<g transform="translate(380 380)"><circle r="68" fill="#fff"/>'+txt('HK',0,24,62,'#e0344a',wt=900)+'</g>','#d81e3d')
I['bank-sg']=tile('#ff6b6b',bank(sc=.86)+'<g transform="translate(380 380)"><circle r="68" fill="#fff"/>'+txt('SG',0,24,62,'#e0344a',wt=900)+'</g>','#e0242f')
I['biz-banking']=tile('#2fc4a5',bank(sc=.9,extra='')+'<g transform="translate(366 372)"><rect x="-64" y="-46" width="128" height="92" rx="20" fill="#fff"/><path d="M-26 -46 V-66 H26 V-46" fill="none" stroke="#fff" stroke-width="14" stroke-linejoin="round"/><rect x="-64" y="-8" width="128" height="10" fill="#2fc4a5"/></g>','#13957c')
I['brokers']=tile('#34c98a',''.join(f'<rect x="{x}" y="{y}" width="40" height="{h}" rx="12" fill="#fff"/><rect x="{x+16}" y="{y-34}" width="8" height="{h+68}" rx="4" fill="#fff"/>' for x,y,h in [(112,270,70),(188,214,100),(264,250,70),(340,150,130)])+'<path d="M110 400 H402" stroke="#fff" stroke-width="16" stroke-linecap="round"/>','#14a066')
I['nomad-tools']=tile('#ffa24a',f'<circle cx="256" cy="256" r="150" fill="none" stroke="#fff" stroke-width="26"/><path d="M256 126 L296 256 L256 386 L216 256Z" fill="#fff" transform="rotate(40 256 256)"/><circle cx="256" cy="256" r="18" fill="#ff8a1e"/>','#ff7a18')
# ---- category icons
I['fintech']=tile('#7a6bff','<rect x="86" y="140" width="340" height="232" rx="42" fill="#fff"/><rect x="86" y="188" width="340" height="50" fill="#7a6bff" opacity=".85"/><rect x="124" y="296" width="96" height="26" rx="13" fill="#7a6bff"/><circle cx="352" cy="310" r="26" fill="#ffb800"/><circle cx="324" cy="310" r="26" fill="#ff5a6e" opacity=".9"/>','#4b3fe0')
I['nomad-work']=tile('#4fb6ff','<rect x="118" y="146" width="276" height="180" rx="26" fill="#fff"/><rect x="142" y="170" width="228" height="132" rx="12" fill="#4fb6ff"/><path d="M80 350 H432 L412 384 Q408 392 398 392 H114 Q104 392 100 384Z" fill="#fff"/><circle cx="256" cy="236" r="34" fill="none" stroke="#fff" stroke-width="12"/><path d="M222 236 H290 M256 202 C240 222 240 250 256 270 M256 202 C272 222 272 250 256 270" stroke="#fff" stroke-width="8" fill="none"/>','#1f7ae0')
sp=lambda cx,cy,r:f'<path d="M{cx} {cy-r} C{cx+r*.12} {cy-r*.25} {cx+r*.25} {cy-r*.12} {cx+r} {cy} C{cx+r*.25} {cy+r*.12} {cx+r*.12} {cy+r*.25} {cx} {cy+r} C{cx-r*.12} {cy+r*.25} {cx-r*.25} {cy+r*.12} {cx-r} {cy} C{cx-r*.25} {cy-r*.12} {cx-r*.12} {cy-r*.25} {cx} {cy-r}Z" fill="#fff"/>'
I['ai-more']=tile('#b36bff',sp(228,244,128)+sp(364,160,56)+sp(372,350,46),'#6b3fe8')
I['social-more']=tile('#ff7eb6','<path d="M100 150 Q100 112 138 112 H290 Q328 112 328 150 V248 Q328 286 290 286 H196 L140 336 V286 H138 Q100 286 100 248Z" fill="#fff"/><path d="M360 206 H376 Q412 206 412 242 V330 Q412 366 376 366 H372 V412 L318 366 H236 Q206 366 196 340 H290 Q350 340 358 280 Z" fill="#fff" opacity=".85"/><circle cx="160" cy="200" r="14" fill="#ff7eb6"/><circle cx="214" cy="200" r="14" fill="#ff7eb6"/><circle cx="268" cy="200" r="14" fill="#ff7eb6"/>','#e0457f')
I['shop-more']=tile('#ff9b4a','<path d="M120 190 H392 L376 392 Q374 410 356 410 H156 Q138 410 136 392Z" fill="#fff"/><path d="M190 190 V160 Q190 108 256 108 Q322 108 322 160 V190" fill="none" stroke="#fff" stroke-width="26" stroke-linecap="round"/><path d="M200 262 Q256 330 312 262" fill="none" stroke="#ff9b4a" stroke-width="22" stroke-linecap="round"/>','#f0641e')
I['privacy']=tile('#3ccf91','<rect x="96" y="120" width="320" height="270" rx="44" fill="#fff"/><circle cx="256" cy="255" r="78" fill="#3ccf91"/><circle cx="256" cy="255" r="50" fill="none" stroke="#fff" stroke-width="14"/><path d="M256 255 L292 219 M256 255 V196 M256 255 L316 255" stroke="#fff" stroke-width="12" stroke-linecap="round"/><circle cx="256" cy="255" r="12" fill="#fff"/><rect x="130" y="390" width="40" height="26" rx="10" fill="#fff"/><rect x="342" y="390" width="40" height="26" rx="10" fill="#fff"/>','#17986a')
I['cn-bank-direct']=tile('#e8423f',bank(sc=.86,extra='')+txt('银行',256,452,60,'#fff',wt=900).replace('y="452"','y="468"'),'#b01d1d')
for k,v in I.items():
    cairosvg.svg2png(bytestring=v.encode(),write_to=f'{OUT}/{k}.png',output_width=512,output_height=512)
print(len(I),sorted(I))
