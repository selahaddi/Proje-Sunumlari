import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

with open('ai-bulten.html', 'r', encoding='utf-8') as f:
    ai_html = f.read()

# 1. Replace tailwind config
tailwind_cfg = re.search(r'<script id="tailwind-config">.*?</script>', index_html, re.DOTALL).group(0)
ai_html = re.sub(r'<script id="tailwind-config">.*?</script>', tailwind_cfg, ai_html, flags=re.DOTALL)

# 2. Extract CSS Variables from index.html
css_vars = re.search(r':root \{.*?\n\}\n\n\.dark \{.*?\n\}', index_html, re.DOTALL).group(0)

# Inject into ai-bulten.html's <style> block right after <style>
ai_html = re.sub(r'<style>', f'<style>\n{css_vars}\n', ai_html, count=1)

# 3. Update body background
ai_html = ai_html.replace('background-color: #fdfbf7;', 'background-color: var(--background);')
ai_html = ai_html.replace('color: theme(\'colors.on-background\');', 'color: var(--on-background);')

# 4. Extract Tactile, Volumetric and Glass nav CSS
tactile_css = re.search(r'  /\* 3D TACTILE CARDS \*/.*?  /\* ORGANIC BACKGROUND \*/', index_html, re.DOTALL).group(0)

# Replace in ai_bulten
ai_html = re.sub(r'    /\* 3D TACTILE CARDS \*/.*?    /\* ORGANIC BACKGROUND \*/', tactile_css, ai_html, flags=re.DOTALL)

# 5. Add GPU acceleration to blobs
blob_replacement = """    pointer-events: none;
      will-change: transform;
      transform: translateZ(0);
      backface-visibility: hidden;"""
ai_html = ai_html.replace('pointer-events: none;', blob_replacement)

# Update blob colors to variables
ai_html = ai_html.replace('background: #FFB86C;', 'background: var(--secondary);')
ai_html = ai_html.replace('background: #5AF5C8;', 'background: var(--primary);')
ai_html = ai_html.replace('background: #FFF4E0;', 'background: var(--tertiary);')

# 6. Update nav class
ai_html = ai_html.replace('premium-glass', 'liquid-glass-nav')

# 7. Add Theme Toggle Button
theme_btn = '<button id="themeToggle" onclick="toggleTheme()" class="volumetric-btn-secondary px-3 py-2 rounded-full text-xs font-bold flex items-center gap-2 border border-surface-variant hover:bg-surface-dim transition-colors"><span class="material-symbols-outlined text-[16px]" id="themeIcon">dark_mode</span></button>'
ai_html = ai_html.replace('<button id="langToggle"', theme_btn + '\n      <button id="langToggle"')

# 8. Add Lenis and Toggle scripts
scripts_to_add = re.search(r'<script>\n  function toggleTheme\(\).*?</html>', index_html, re.DOTALL).group(0)
# Clean up
scripts_to_add = scripts_to_add.replace('</body>\n</html>', '')

# Replace end of ai-bulten
ai_html = re.sub(r'  </script>\n</body>\n</html>', '  </script>\n\n' + scripts_to_add + '\n</body>\n</html>', ai_html)

with open('ai-bulten.html', 'w', encoding='utf-8') as f:
    f.write(ai_html)

print("Success")
