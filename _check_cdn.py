# -*- coding: utf-8 -*-
import urllib.request, urllib.parse

base = 'https://customer-workbench-c59.pages.dev/'
path = urllib.parse.quote('客户跟进工作台.html')
url = base + path

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req, timeout=30)
    content = resp.read().decode('utf-8')
    
    if 'sidebarCollapse' in content:
        print('DEPLOYED: Latest version with sidebarCollapse - fix is live')
    else:
        print('DEPLOYED: Old version - fix NOT yet deployed')
    
    idx = content.find('navAdd')
    if idx >= 0:
        snippet = content[idx-15:idx+30]
        print('Around navAdd:', repr(snippet))
    
    if '.collapsed' in content:
        print('Has .collapsed CSS: Yes')
    else:
        print('Has .collapsed CSS: No')
        
except Exception as e:
    print(f'Error: {e}')
