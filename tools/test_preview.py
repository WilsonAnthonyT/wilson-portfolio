from pathlib import Path
from playwright.sync_api import sync_playwright
import re,base64
p=Path(__file__).resolve().parents[1]
css=(p/'preview/styles.css').read_text();js=(p/'preview/site.js').read_text()
assets=p/'preview/assets'
css=css.replace("url('assets/skyline.svg')",'url("data:image/svg+xml;base64,'+base64.b64encode((assets/'skyline.svg').read_bytes()).decode()+'")')
def html(name):
 data=(p/'preview'/name).read_text()
 data=re.sub(r'<link rel="stylesheet" href="[^"]+">','<style>'+css+'</style>',data)
 data=re.sub(r'<script src="[^"]+"></script>','<script>'+js+'</script>',data)
 def inline(m):
  src=m.group(1);fn=src.rsplit('/',1)[-1]
  if (assets/fn).exists():return 'src="data:image/svg+xml;base64,'+base64.b64encode((assets/fn).read_bytes()).decode()+'"'
  return m.group()
 return re.sub(r'src="([^"]+\.svg)"',inline,data)
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for n,(w,h) in [('desktop',(1440,900)),('mobile',(390,844))]:
  page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1,color_scheme='dark')
  errors=[]; page.on('pageerror',lambda e:errors.append(str(e)))
  page.set_content(html('index.html'),wait_until='domcontentloaded');page.wait_for_timeout(400)
  page.screenshot(path=str(p/f'{n}-first-screen.png'))
  page.screenshot(path=str(p/f'{n}-full.png'),full_page=True)
  print(n,'title',page.title(),'projects',page.locator('.project-card').count(),'errors',errors)
  print('overflow',page.evaluate('document.documentElement.scrollWidth > innerWidth'))
  page.locator('#terminal-input').fill('whoami');page.locator('#terminal-input').press('Enter');print('terminal',page.locator('#terminal-history').inner_text().splitlines()[-1])
  prev=page.evaluate('document.documentElement.dataset.theme');page.locator('#theme-button').click();print('theme',prev,'->',page.evaluate('document.documentElement.dataset.theme'))
  if n=='mobile':
   page.locator('#mobile-toggle').click();print('menu visible',page.locator('#mobile-nav').is_visible())
  page.close()
 page=browser.new_page(viewport={'width':1250,'height':850},color_scheme='dark')
 page.set_content(html('projects/goal-digger/index.html'));page.locator('[data-scenario="milestone"]').click();print('failure case',page.locator('#lab-message').inner_text());page.screenshot(path=str(p/'goal-digger-case-preview.png'),full_page=True)
 page.set_content(html('projects/8051-runtime/index.html'));page.locator('#step-tick').click();print('threads tick',page.locator('#tick-count').inner_text())
 page.set_content(html('projects/invasion-requiem/index.html'));page.locator('#move-right').click();print('game',page.locator('#game-hud').inner_text())
 browser.close()
