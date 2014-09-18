import subprocess, re
f = open('core-theme-style.html', 'w')
f.write('<core-style id="theme">')
css = subprocess.check_output(['stylus', '-p', 'core-theme.styl'])
f.write(re.sub(r'\_([a-zA-Z]*)([0-9]*)\_', r'{{colors[\1][\2]}}', css))
f.write('</core-style>')
f.close()