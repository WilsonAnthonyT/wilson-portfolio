from pathlib import Path
import random, math
r=random.Random(741)
p=Path(__file__).resolve().parents[1]/'public/assets'
p.mkdir(parents=True,exist_ok=True)
def save(name,x): (p/name).write_text(x,encoding='utf-8')
head='''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="650" viewBox="0 0 1200 650"><defs><linearGradient id="sky" x1="0" y1="0" x2="0.8" y2="1"><stop stop-color="#091025"/><stop offset=".48" stop-color="#16234c"/><stop offset=".78" stop-color="#402351"/><stop offset="1" stop-color="#6b315e"/></linearGradient><radialGradient id="haze"><stop stop-color="#ab58b6" stop-opacity=".48"/><stop offset="1" stop-color="#ac5df1" stop-opacity="0"/></radialGradient><linearGradient id="ground" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#162440"/><stop offset="1" stop-color="#050b19"/></linearGradient><linearGradient id="pane" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#aa90ff"/><stop offset="1" stop-color="#6bd4ec"/></linearGradient></defs>'''
svg=[head,'<rect width="1200" height="650" fill="url(#sky)"/><ellipse cx="670" cy="415" rx="480" ry="300" fill="url(#haze)"/>']
for i in range(74):
 x=r.randrange(1200);y=r.randrange(50,420);rr=r.choice([.5,1,1.4]);svg.append(f'<circle cx="{x}" cy="{y}" r="{rr}" fill="#d0ddff" opacity="{r.uniform(.1,.5):.2f}"/>')
# subtle skyline, nearly black buildings
for layer in [0,1,2]:
 ybase=560+layer*43
 pos=0
 while pos<1250:
  w=r.randint(22,78);h=r.randint(85,240)+layer*25
  fill=['#182342','#101b32','#091426'][layer]
  svg.append(f'<rect x="{pos}" y="{ybase-h}" width="{w}" height="{h+120}" fill="{fill}"/>')
  if layer !=2:
   for yy in range(int(ybase-h+14),int(ybase-8),19):
    for xx in range(pos+7,pos+w-6,13):
     if r.random()<.26:svg.append(f'<rect x="{xx}" y="{yy}" width="4" height="7" rx=".5" fill="{r.choice(["#a784ef","#ee8e9f","#6db3d1"])}" opacity="{r.uniform(.12,.56):.2f}"/>')
  pos+=w+3
# futuristic signal tower at right
svg+=['<path d="M855 475 L877 226 L897 226 L919 475 Z" fill="#10162c" stroke="#ad73c5" stroke-opacity=".3"/>','<path d="M887 227 L887 124 M869 264 H905 M863 310 H911 M860 354 H914" stroke="#e08fc5" stroke-width="3" opacity=".55"/>','<path d="M852 412 H922" stroke="#7a8fcb" stroke-width="8"/>','<circle cx="887" cy="123" r="4" fill="#ffafca"/>']
svg+=['<path d="M0 566 Q220 542 440 574 T1200 552 V650 H0" fill="url(#ground)"/>','<path d="M0 574 Q330 548 660 576 T1200 572" stroke="#7a5f9d" stroke-opacity=".2" fill="none" stroke-width="3"/>','</svg>']
save('skyline.svg',''.join(svg))

def frame(title, inside, color='#9d86f7', label='CONCEPT VISUAL'):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="700" viewBox="0 0 1200 700"><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#17213a"/><stop offset=".58" stop-color="#101827"/><stop offset="1" stop-color="#202043"/></linearGradient><radialGradient id="a"><stop stop-color="{color}" stop-opacity=".22"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient></defs><rect width="1200" height="700" rx="26" fill="url(#bg)"/><circle cx="920" cy="335" r="460" fill="url(#a)"/><path d="M0 572H1200 M0 468H1200 M0 365H1200 M0 262H1200 M0 159H1200 M130 0V700 M330 0V700 M530 0V700 M730 0V700 M930 0V700 M1130 0V700" fill="none" stroke="#9ba6d0" stroke-opacity=".05"/><text x="48" y="67" fill="#a8b7d4" font-size="18" font-family="monospace" letter-spacing="3">{title}</text><text x="1153" y="664" text-anchor="end" fill="#b1b6cf" opacity=".62" font-family="monospace" font-size="13" letter-spacing="2">{label}</text>{inside}</svg>'''

def phone(x,y,w,h,number,caption,accent):
 content=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="30" fill="#050a15" stroke="#7283af" stroke-opacity=".75" stroke-width="3"/><rect x="{x+8}" y="{y+8}" width="{w-16}" height="{h-16}" rx="24" fill="#0d1729"/>'
 content+=f'<rect x="{x+w/2-33}" y="{y+11}" width="66" height="12" rx="6" fill="#03060e"/>'
 content+=f'<text x="{x+24}" y="{y+68}" fill="#f5f3ff" font-size="24" font-weight="bold" font-family="Arial">{caption}</text>'
 content+=f'<rect x="{x+22}" y="{y+91}" width="{w-44}" height="104" rx="16" fill="{accent}" opacity=".22"/><circle cx="{x+w/2}" cy="{y+140}" r="27" fill="{accent}" opacity=".38"/>'
 for j in range(3):
  content+=f'<rect x="{x+22}" y="{y+217+j*57}" width="{w-44}" height="45" rx="11" fill="#222f48" stroke="#57678b" stroke-opacity=".25"/><circle cx="{x+44}" cy="{y+240+j*57}" r="9" fill="{accent}" opacity=".75"/><rect x="{x+63}" y="{y+235+j*57}" width="{w-124-j*8}" height="9" rx="4" fill="#7789af" opacity=".48"/>'
 content+=f'<text x="{x+w/2}" y="{y+h-28}" text-anchor="middle" fill="#8392b3" font-size="14" font-family="monospace">0{number} / GOAL DIGGER</text>'
 return content
inner=phone(175,132,244,485,1,'My goals','#986eff')+phone(466,95,264,540,2,'Today','#76d9c4')+phone(777,132,244,485,3,'Focus','#f0a8c3')
save('goal-digger.svg',frame('GOAL DIGGER / APP CONCEPT',inner, '#9471e7'))
# Budgeting UI - spreadsheet style
inner='''<rect x="135" y="115" width="930" height="492" rx="28" fill="#0b1526" stroke="#50618a" stroke-width="2"/><rect x="135" y="115" width="930" height="61" rx="28" fill="#182943"/><circle cx="176" cy="147" r="7" fill="#8fcbd3"/><circle cx="199" cy="147" r="7" fill="#8e72c4"/><circle cx="222" cy="147" r="7" fill="#e5a6a6"/><text x="270" y="155" fill="#dce5f3" font-family="Arial" font-size="20" font-weight="bold">SaveWiser  /  Overview</text><text x="180" y="235" fill="#b1c2d9" font-family="monospace" font-size="16">MONTHLY OVERVIEW</text><text x="180" y="295" fill="#f8f8fd" font-family="Arial" font-size="52" font-weight="bold">$ 2,450</text><text x="180" y="332" fill="#83d8c1" font-family="Arial" font-size="18">Savings goal progress</text><rect x="180" y="359" width="320" height="13" rx="6" fill="#2c4054"/><rect x="180" y="359" width="215" height="13" rx="6" fill="#8ed8ce"/><rect x="590" y="216" width="417" height="325" rx="16" fill="#162541"/><text x="622" y="257" fill="#bdcce4" font-family="Arial" font-size="17">Spending activity</text>'''
for i,h in enumerate([90,148,116,176,132,218,178]):
 x=642+i*49; inner+=f'<rect x="{x}" y="{506-h}" width="25" height="{h}" rx="5" fill="{["#ab92f6","#79d7d1"][i%2]}" opacity=".85"/>'
inner+='''<rect x="180" y="429" width="320" height="112" rx="16" fill="#1a2d48"/><text x="202" y="461" fill="#bfcde0" font-family="Arial" font-size="16">Savings lock</text><text x="202" y="499" fill="#9cead2" font-family="Arial" font-weight="bold" font-size="26">Goal protected</text><path d="M455 471 v-12 a13 13 0 0 0 -26 0 v12 m-4 0 h34 v28 h-34 z" fill="none" stroke="#a6e5d9" stroke-width="3"/>'''
save('savewiser.svg',frame('SAVEWISER / UI CONCEPT',inner,'#70d6c0'))
# pixel stage
inn=['<rect x="80" y="113" width="1040" height="510" rx="17" fill="#071021" stroke="#485683" stroke-width="4"/>','<circle cx="900" cy="220" r="74" fill="#a77bd0" opacity=".2"/>','<circle cx="900" cy="220" r="43" fill="#eab8cd" opacity=".8"/>']
for i in range(29):
 x=90+i*37;h=r.randrange(50,160);inn.append(f'<rect x="{x}" y="{502-h}" width="{r.randint(23,44)}" height="{h+80}" fill="#142641"/>')
for i in range(31):
 x=80+i*34;inn.append(f'<rect x="{x}" y="560" width="34" height="50" fill="{["#3e4669","#596486"][i%2]}"/><path d="M{x} 560H{x+34}" stroke="#8a79b3" stroke-width="2"/>')
# character (stylized pixel hero)
inn+=['<rect x="308" y="397" width="42" height="36" fill="#d0a7c0"/><rect x="296" y="423" width="66" height="71" fill="#5b89ae"/><rect x="295" y="488" width="25" height="65" fill="#202943"/><rect x="338" y="488" width="25" height="65" fill="#202943"/><rect x="287" y="437" width="15" height="59" fill="#bd8e9a"/><rect x="362" y="437" width="16" height="59" fill="#bd8e9a"/><rect x="309" y="390" width="35" height="11" fill="#3d314d"/><rect x="323" y="411" width="7" height="7" fill="#24354d"/>']
for x,y in [(630,448),(783,456),(936,430)]:
 inn+= [f'<rect x="{x}" y="{y}" width="60" height="57" fill="#7b67ae"/>',f'<rect x="{x+12}" y="{y-17}" width="38" height="20" fill="#7b67ae"/>',f'<rect x="{x+12}" y="{y+15}" width="12" height="9" fill="#ec9bd1"/>',f'<rect x="{x+37}" y="{y+15}" width="12" height="9" fill="#ec9bd1"/>']
inn+=['<text x="125" y="159" font-family="monospace" font-size="19" fill="#d4d8fa">INVASION REQUIEM</text>','<text x="1040" y="160" text-anchor="end" font-family="monospace" font-size="15" fill="#f0b6e7">LEVEL 04   /   HP ▰▰▰</text>']
save('invasion.svg',frame('INVASION REQUIEM / PIXEL-ART CONCEPT',''.join(inn),'#c07ddc'))
# threads diagram
inn=['<rect x="125" y="137" width="950" height="435" rx="21" fill="#0c1729" stroke="#344a70" stroke-width="2"/>','<text x="163" y="186" fill="#92a6c4" font-family="monospace" font-size="18">TIME →</text>']
colors=['#b39bff','#81cfdf','#f6b68e']
for i,c in enumerate(colors):
 y=228+i*108
 inn.append(f'<text x="161" y="{y+27}" fill="#ced8ee" font-family="monospace" font-size="21">T{i+1}</text>')
 for j in range(9):
  x=263+j*78
  on=(j%3==i)
  inn.append(f'<rect x="{x}" y="{y}" width="65" height="44" rx="9" fill="{c if on else "#1b2a41"}" opacity="{.9 if on else .7}" stroke="{c}" stroke-opacity=".25"/>')
  if on:inn.append(f'<text x="{x+32}" y="{y+27}" text-anchor="middle" fill="#10192b" font-family="monospace" font-size="12" font-weight="bold">RUN</text>')
  else:inn.append(f'<text x="{x+32}" y="{y+27}" text-anchor="middle" fill="#8494ad" font-family="monospace" font-size="12">WAIT</text>')
inn+=['<text x="163" y="563" font-family="monospace" font-size="15" fill="#9baed1">context switch   ↔   scheduler tick   ↔   semaphore wait</text>']
save('threads.svg',frame('8051 / THREAD SCHEDULER CONCEPT',''.join(inn),'#879af4'))
print('assets:',[x.name for x in p.glob('*.svg')])
