# -*- coding: utf-8 -*-
"""Scan for any backslash-escaped quotes that shouldn't be there in app code."""
p = r'D:\桌面\work\2026-08-23-07-33-00\客户跟进工作台.html'
with open(p, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Check app code area: lines 1200-1900 (sidebar HTML + early JS) and 5900-6113 (event bindings)
ranges = [(1200, 1900), (5900, 6113)]
bad_lines = []
for start, end in ranges:
    for i in range(start-1, min(end, len(lines))):
        line = lines[i]
        # Look for \\\" pattern (backslash followed by quote) which is wrong in JS source
        if '\\' in line and '\\"' in line:
            # Check if it's a legit escape inside a string (rare in our app code)
            bad_lines.append((i+1, line.rstrip()))

for ln, line in bad_lines:
    print(f'Line {ln}: {line[:150]}')

print(f'\nTotal suspicious lines: {len(bad_lines)}')
