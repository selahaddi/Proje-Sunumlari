import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

with open('ai-bulten.html', 'r', encoding='utf-8') as f:
    ai_html = f.read()

# Get the exact tailwind config and root styles from index.html
match_index = re.search(r'<script id="tailwind-config">.*?</style>', index_html, re.DOTALL)
if match_index:
    theme_css = match_index.group(0)
    # Replace in ai-bulten.html
    ai_html = re.sub(r'<script id="tailwind-config">.*?</style>', theme_css, ai_html, flags=re.DOTALL)

# Fix body styles in ai-bulten.html
ai_html = ai_html.replace(
    "background-color: #fdfbf7;", 
    "background-color: var(--background);")
ai_html = ai_html.replace(
    "color: theme('colors.on-background');", 
    "color: var(--on-background);")

# Write back
with open('ai-bulten.html', 'w', encoding='utf-8') as f:
    f.write(ai_html)

print('Theme colors injected successfully.')
