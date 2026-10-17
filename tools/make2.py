import json,math,cairosvg
from make import *
hexs=json.load(open('hex.json'))
def lum(h):
    r,g,b=[int(h[i:i+2],16) for i in (0,2,4)];return (.299*r+.587*g+.114*b)/255
def shade(h,f):
    r,g,b=[int(h[i:i+2],16) for i in (0,2,4)];return '#%02x%02x%02x'%tuple(max(0,min(255,int(c*f))) for c in (r,g,b))
def lite(h,f):
    r,g,b=[int(h[i:i+2],16) for i in (0,2,4)];return '#%02x%02x%02x'%tuple(int(c+(255-c)*f) for c in (r,g,b))
S={}
for g,h in hexs.items():
    f=f'b/{g}.svg'
    if g=='sumup':continue
    if lum(h)>.8 or g in('notion','wikimedia','google'):
        col='#000' if g in('notion','wikimedia') else '#'+h
        if g=='google':col='#4285F4'
        S[g]=tile('#ffffff',glyph(f,col,s=17),'#f0f0f0')
    else:
        S[g]=tile(lite(h,.18),glyph(f,W,s=17),shade(h,.82))
S['github']=tile('#3a3f47',glyph('b/github.svg',W,s=17),'#0d1117')
S['apple']=tile('#4a4a4f',glyph('b/apple.svg',W,s=16),'#000')
# --- hand-drawn brands (simplified)
S['ai']=tile('#2fd4a4','<rect x="150" y="150" width="212" height="212" rx="50" fill="#fff"/><g fill="#2fd4a4"><rect x="120" y="200" width="30" height="16" rx="8"/><rect x="120" y="296" width="30" height="16" rx="8"/><rect x="362" y="200" width="30" height="16" rx="8"/><rect x="362" y="296" width="30" height="16" rx="8"/><rect x="200" y="120" width="16" height="30" rx="8"/><rect x="296" y="120" width="16" height="30" rx="8"/><rect x="200" y="362" width="16" height="30" rx="8"/><rect x="296" y="362" width="16" height="30" rx="8"/></g>'+sp(256,256,70).replace('#fff','#2fd4a4')+sp(318,196,24).replace('#fff','#2fd4a4'),'#12987a')
S['disney']=tile('#2a5bd7',txt('D',210,330,230,W,fam='DejaVu Serif',wt=700)+'<path d="M330 196 V286 M285 241 H375" stroke="#fff" stroke-width="28" stroke-linecap="round"/>','#10286b')
S['primevideo']=tile('#14a3ff',txt('prime',256,262,120,W,fam='DejaVu Sans',wt=800)+txt('video',256,342,70,'#d6f0ff',fam='DejaVu Sans',wt=700)+'<path d="M140 372 Q256 430 372 372" fill="none" stroke="#fff" stroke-width="18" stroke-linecap="round"/>','#0a63c9')
S['linkedin']=tile('#2f8fdc','<rect x="104" y="196" width="60" height="196" rx="14" fill="#fff"/><circle cx="134" cy="140" r="36" fill="#fff"/><path d="M200 196 H258 V224 C274 200 298 190 326 190 C376 190 408 218 408 280 V392 H348 V292 C348 262 336 246 312 246 C286 246 260 262 260 296 V392 H200Z" fill="#fff"/>','#0a58a8')
S['nintendo']=tile('#ff4a4a',txt('Nintendo',256,285,68,W,fam='DejaVu Sans',wt=900)+'<rect x="34" y="190" width="444" height="140" rx="70" fill="none" stroke="#fff" stroke-width="16"/>','#c2131f')
S['xbox']=tile('#3bd16f','<circle cx="256" cy="256" r="156" fill="#fff"/>'+txt('X',256,330,230,'#17a34a',fam='DejaVu Sans',wt=900),'#0d7a35')
S['microsoft']=tile('#ffffff','<rect x="116" y="116" width="124" height="124" rx="14" fill="#f25022"/><rect x="272" y="116" width="124" height="124" rx="14" fill="#7fba00"/><rect x="116" y="272" width="124" height="124" rx="14" fill="#00a4ef"/><rect x="272" y="272" width="124" height="124" rx="14" fill="#ffb900"/>','#eef0f4')
S['onedrive']=tile('#3aa0ff','<path d="M150 360 C96 360 80 296 126 276 C130 220 190 190 236 214 C262 164 346 176 358 244 C416 238 442 320 392 350 C384 358 372 360 360 360Z" fill="#fff"/>','#1262d6')
S['slack']=tile('#ffffff','<rect x="190" y="108" width="48" height="240" rx="24" fill="#e01e5a"/><rect x="290" y="164" width="48" height="240" rx="24" fill="#36c5f0"/><rect x="108" y="190" width="240" height="48" rx="24" fill="#2eb67d"/><rect x="164" y="290" width="240" height="48" rx="24" fill="#ecb22e"/>','#eef0f4')
S['amazon']=tile('#38424f',txt('amazon',256,250,104,W,fam='DejaVu Sans',wt=800)+'<path d="M120 308 Q256 372 392 308" fill="none" stroke="#ff9900" stroke-width="20" stroke-linecap="round"/><path d="M372 292 L396 306 L376 326" fill="none" stroke="#ff9900" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>','#11161c')
# --- category icons
def pad():  # gamepad
    return '<path d="M150 190 H362 C420 190 440 250 424 320 C412 372 372 384 346 350 L318 316 H194 L166 350 C140 384 100 372 88 320 C72 250 92 190 150 190Z" fill="#fff"/>'
dpad='<path d="M168 226 V282 M140 254 H196" stroke="{c}" stroke-width="22" stroke-linecap="round"/><circle cx="330" cy="232" r="16" fill="{c}"/><circle cx="372" cy="270" r="16" fill="{c}"/>'
S['games-cn']=tile('#ff6a5c',pad()+dpad.format(c='#ff6a5c')+txt('国服',256,372,64,W,wt=900).replace('y="372"','y="426"'),'#d92b2b')
S['games-more']=tile('#9a6bff',pad()+dpad.format(c='#9a6bff'),'#5a34d6')
S['crypto']=tile('#ffbe3b','<circle cx="256" cy="256" r="150" fill="#fff"/><circle cx="256" cy="256" r="118" fill="none" stroke="#ffbe3b" stroke-width="12"/>'+txt('B',256,320,190,'#f59e0b',fam='DejaVu Sans',wt=900)+'<path d="M232 112 V150 M280 112 V150 M232 362 V400 M280 362 V400" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>','#f08a00')
S['crypto-more']=tile('#ff9d4a','<rect x="96" y="170" width="320" height="220" rx="44" fill="#fff"/><path d="M96 220 H416" stroke="#ff9d4a" stroke-width="14"/><rect x="316" y="268" width="130" height="80" rx="36" fill="#ffd0a0"/><circle cx="350" cy="308" r="16" fill="#ff7a18"/><circle cx="226" cy="130" r="48" fill="#ffd25a"/><circle cx="296" cy="112" r="38" fill="#ffbe3b"/>','#f0641e')
S['pt']=tile('#37c6c0','<path d="M256 110 V310 M170 232 L256 318 L342 232" fill="none" stroke="#fff" stroke-width="40" stroke-linecap="round" stroke-linejoin="round"/><path d="M112 372 H400" stroke="#fff" stroke-width="40" stroke-linecap="round"/>','#16908f')
S['scholar']=tile('#4a7cff','<path d="M256 120 L430 200 L256 280 L82 200Z" fill="#fff"/><path d="M148 246 V320 C148 350 198 372 256 372 C314 372 364 350 364 320 V246 L256 296Z" fill="#fff" opacity=".92"/><path d="M420 214 V320" stroke="#fff" stroke-width="16" stroke-linecap="round"/><circle cx="420" cy="330" r="16" fill="#fff"/>','#2547c4')
S['media-more']=tile('#ff6fa8','<rect x="86" y="130" width="340" height="230" rx="40" fill="#fff"/><path d="M226 190 L330 245 L226 300Z" fill="#ff6fa8"/><rect x="150" y="390" width="212" height="22" rx="11" fill="#fff" opacity=".9"/>','#d93a7a')
S['travel']=tile('#4dc3ff','<path d="M432 114 C440 108 404 100 380 124 L300 204 L130 160 L100 190 L236 262 L190 312 L130 304 L106 328 L184 370 L226 448 L250 424 L242 362 L292 316 L364 452 L394 422 L350 262 L428 184 C446 164 446 124 432 114Z" fill="#fff"/>','#1c86e0')
S['cloud-dev']=tile('#6a7dff','<path d="M142 336 C84 336 70 266 118 246 C122 190 188 160 232 188 C260 136 346 150 358 218 C420 214 446 300 394 330 C386 334 376 336 366 336Z" fill="#fff"/><path d="M216 252 L180 286 L216 320 M296 252 L332 286 L296 320 M268 238 L244 334" stroke="#6a7dff" stroke-width="18" fill="none" stroke-linecap="round" stroke-linejoin="round"/>','#3a44d6')
S['trackers']=tile('#7a8599','<path d="M70 256 C130 160 382 160 442 256 C382 352 130 352 70 256Z" fill="#fff"/><circle cx="256" cy="256" r="58" fill="#7a8599"/><path d="M110 120 L402 392" stroke="#fff" stroke-width="34" stroke-linecap="round"/><path d="M110 120 L402 392" stroke="#4a5365" stroke-width="12" stroke-linecap="round"/>','#4a5365')
S['ads']=tile('#ff6b6b','<path d="M110 220 H190 L330 130 V382 L190 292 H110Z" fill="#fff"/><path d="M370 210 Q410 256 370 302" fill="none" stroke="#fff" stroke-width="22" stroke-linecap="round"/><circle cx="256" cy="256" r="176" fill="none" stroke="#fff" stroke-width="26"/><path d="M132 132 L380 380" stroke="#fff" stroke-width="26" stroke-linecap="round"/>','#d62c3c')
S['telemetry']=tile('#9f7bff','<circle cx="256" cy="290" r="100" fill="none" stroke="#fff" stroke-width="22"/><circle cx="256" cy="290" r="50" fill="none" stroke="#fff" stroke-width="22"/><circle cx="256" cy="290" r="14" fill="#fff"/><path d="M256 290 L350 190" stroke="#fff" stroke-width="22" stroke-linecap="round"/><path d="M110 120 L402 410" stroke="#fff" stroke-width="30" stroke-linecap="round"/><path d="M110 120 L402 410" stroke="#6a3fe0" stroke-width="10" stroke-linecap="round"/>','#5a34d6')
done=[]
for k,v in S.items():
    if k in I and k!='github':pass
    cairosvg.svg2png(bytestring=v.encode(),write_to=f'{OUT}/{k}.png',output_width=512,output_height=512);done.append(k)
print(len(done),sorted(done))
