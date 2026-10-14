# -*- coding: utf-8 -*-
"""Extract the JS portion and check for basic syntax issues."""
p = r'D:\桌面\work\2026-08-23-07-33-00\客户跟进工作台.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

# Check 1: Are there any \\\" sequences in the sidebar HTML area (lines 1250-1320)?
lines = c.split('\n')
for i in range(1249, min(1330, len(lines))):
    line = lines[i]
    if '\\' in line:
        print(f'L{i+1}: {line[:120]}')

print('---')

# Check 2: Look for the navTheme span wrapping - is it causing issues?
for i in range(1298, min(1310, len(lines))):
    print(f'L{i+1}: {lines[i][:120]}')

print('---')

# Check 3: Look for any obviously broken JS patterns in the event binding area
for i in range(5995, min(6025, len(lines))):
    line = lines[i]
    # Check for patterns like $(\" instead of $("
    if '$(\\"' in line or '$(\\\"' in line:
        print(f'BROKEN L{i+1}: {line[:120]}')
    # Check for any backslash before quote that's not in a string
    if 'onclick=' in line and '\\' in line:
        print(f'SUSPECT L{i+1}: {line[:120]}')

print('Done')
