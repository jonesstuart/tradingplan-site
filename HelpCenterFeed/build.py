#!/usr/bin/env python3
"""
Build TradingPlan help centre: convert MD files → HTML articles.
Run from any directory. Outputs to help/articles/.
"""

import re, json
from pathlib import Path

BASE = Path("/Users/stuart/Library/Mobile Documents/com~apple~CloudDocs/_JS/TradingPlanApp/TradingPlanSite")
FEED = BASE / "HelpCenterFeed"
OUT  = BASE / "help/articles"
DATE = "2026-04-21"

# ── Article registry ─────────────────────────────────────────────────────────
ARTICLES = [
    # (folder, slug, id, category)
    ("01-Getting-Started",          "welcome-and-overview",              "001", "Getting Started"),
    ("01-Getting-Started",          "setting-up-your-plan",              "002", "Getting Started"),
    ("01-Getting-Started",          "navigating-the-app",                "003", "Getting Started"),
    ("02-Strategies",               "creating-your-first-strategy",      "011", "Strategies"),
    ("02-Strategies",               "understanding-strategy-rules",      "012", "Strategies"),
    ("02-Strategies",               "running-a-strategy-flow",           "013", "Strategies"),
    ("02-Strategies",               "including-strategies-in-your-plan", "014", "Strategies"),
    ("03-Trade-Plan",               "trade-plan-overview",               "021", "Trade Plan"),
    ("03-Trade-Plan",               "your-trading-philosophy",           "022", "Trade Plan"),
    ("03-Trade-Plan",               "trader-mindset",                    "023", "Trade Plan"),
    ("03-Trade-Plan",               "your-why",                          "024", "Trade Plan"),
    ("03-Trade-Plan",               "business-notes",                    "025", "Trade Plan"),
    ("04-Risk-Management",          "risk-management-overview",          "031", "Risk Management"),
    ("04-Risk-Management",          "position-sizing",                   "032", "Risk Management"),
    ("04-Risk-Management",          "advanced-risk-features",            "033", "Risk Management"),
    ("05-Routines",                 "creating-a-routine",                "041", "Routines"),
    ("05-Routines",                 "running-your-routine-flow",         "042", "Routines"),
    ("05-Routines",                 "routine-templates",                 "043", "Routines"),
    ("06-Account-and-Subscription", "free-vs-pro",                      "051", "Account & Subscription"),
    ("06-Account-and-Subscription", "upgrading-to-pro",                 "052", "Account & Subscription"),
    ("06-Account-and-Subscription", "managing-your-subscription",       "053", "Account & Subscription"),
    ("06-Account-and-Subscription", "sign-in-with-apple",               "054", "Account & Subscription"),
    ("07-Data-and-Sync",            "icloud-sync",                       "061", "Data & Sync"),
    ("07-Data-and-Sync",            "multiple-devices",                  "062", "Data & Sync"),
    ("08-Troubleshooting",          "data-not-syncing",                  "102", "Troubleshooting"),
    ("08-Troubleshooting",          "cant-sign-in",                      "103", "Troubleshooting"),
    ("08-Troubleshooting",          "missing-data",                      "104", "Troubleshooting"),
    ("08-Troubleshooting",          "subscription-not-activating",       "105", "Troubleshooting"),
    ("08-Troubleshooting",          "biometric-lock-issues",             "106", "Troubleshooting"),
    ("08-Troubleshooting",          "app-crashes",                       "107", "Troubleshooting"),
    ("08-Troubleshooting",          "strategy-flow-not-working",         "108", "Troubleshooting"),
    ("09-Tips-and-Features",        "customising-the-dashboard",         "111", "Tips & Features"),
    ("09-Tips-and-Features",        "achievements",                      "112", "Tips & Features"),
    ("09-Tips-and-Features",        "notifications",                     "113", "Tips & Features"),
    ("09-Tips-and-Features",        "using-on-mac",                      "114", "Tips & Features"),
]

# ── Inline markdown formatting ────────────────────────────────────────────────
def fmt(text):
    # Bold (before italic to avoid conflict)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic (not adjacent to another *)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    # Links
    def repl(m):
        t, u = m.group(1), m.group(2)
        if u.startswith('http'):
            return f'<a href="{u}" target="_blank" rel="noopener">{t}</a>'
        if u.endswith('.md'):
            u = u[:-3] + '.html'
        return f'<a href="{u}">{t}</a>'
    text = re.sub(r'\[(.+?)\]\((.+?)\)', repl, text)
    return text

# ── Table ─────────────────────────────────────────────────────────────────────
def render_table(rows):
    headers = [c.strip() for c in rows[0].split('|') if c.strip()]
    data = []
    for row in rows[2:]:
        cells = [c.strip() for c in row.split('|')]
        cells = [c for c in cells if c != '']
        if cells:
            data.append(cells)
    h = '<div class="table-wrap"><table class="help-table"><thead><tr>'
    for hdr in headers:
        h += f'<th>{fmt(hdr)}</th>'
    h += '</tr></thead><tbody>'
    for row in data:
        h += '<tr>' + ''.join(f'<td>{fmt(c)}</td>' for c in row) + '</tr>'
    h += '</tbody></table></div>'
    return h

# ── Is a metadata/skip line ───────────────────────────────────────────────────
def is_meta(line):
    s = line.strip()
    return s.startswith('**Category:**') or s.startswith('**Helpful for:**')

# ── Convert markdown body to HTML ─────────────────────────────────────────────
def convert(lines):
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()

        # Empty / HR / metadata — skip
        if not s or s == '---' or is_meta(line):
            i += 1
            continue

        # H1 — used as article title, skip in body
        if re.match(r'^# (?!#)', line):
            i += 1
            continue

        # H2
        if line.startswith('## '):
            out.append(f'<h2>{fmt(line[3:].strip())}</h2>')
            i += 1
            continue

        # H3
        if line.startswith('### '):
            out.append(f'<h3>{fmt(line[4:].strip())}</h3>')
            i += 1
            continue

        # Blockquote → callout
        if line.startswith('> '):
            parts = []
            while i < len(lines) and lines[i].startswith('> '):
                parts.append(lines[i][2:].strip())
                i += 1
            out.append(f'<div class="callout">{fmt(" ".join(parts))}</div>')
            continue

        # Unordered list
        if re.match(r'^[-*] ', line):
            items = []
            while i < len(lines) and re.match(r'^[-*] ', lines[i]):
                items.append(f'<li>{fmt(lines[i][2:].strip())}</li>')
                i += 1
            out.append('<ul>\n' + '\n'.join(items) + '\n</ul>')
            continue

        # Ordered list
        if re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                content = re.sub(r'^\d+\. ', '', lines[i]).strip()
                items.append(f'<li>{fmt(content)}</li>')
                i += 1
            out.append('<ol>\n' + '\n'.join(items) + '\n</ol>')
            continue

        # Table (line starts with | and has multiple cells)
        if s.startswith('|') and s.count('|') >= 2:
            tbl = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                tbl.append(lines[i])
                i += 1
            out.append(render_table(tbl))
            continue

        # Paragraph: collect consecutive non-special lines
        para = []
        while i < len(lines):
            l = lines[i]
            ls = l.strip()
            if (not ls or ls == '---' or is_meta(l) or l.startswith('#')
                    or l.startswith('> ') or re.match(r'^[-*] ', l)
                    or re.match(r'^\d+\. ', l)
                    or (ls.startswith('|') and ls.count('|') >= 2)):
                break
            para.append(l.strip())
            i += 1
        if para:
            out.append(f'<p>{fmt(" ".join(para))}</p>')

    return '\n'.join(out)

# ── Extract plain-text excerpt ────────────────────────────────────────────────
def excerpt(lines):
    for line in lines:
        s = line.strip()
        if (not s or s == '---' or is_meta(line)
                or re.match(r'^#', line) or s.startswith('|')):
            continue
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
        text = re.sub(r'\*(.+?)\*', r'\1', text)
        text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
        if len(text) > 10:
            return text[:180] + ('…' if len(text) > 180 else '')
    return ''

# ── Full article HTML template ────────────────────────────────────────────────
def article_page(art_id, title, category, body, prev_art, next_art):
    nav_prev = f'<a href="{prev_art[0]}.html">← {prev_art[1]}</a>' if prev_art else '<span></span>'
    nav_next = f'<a href="{next_art[0]}.html">{next_art[1]} →</a>' if next_art else '<span></span>'

    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — TradingPlan Help</title>
  <meta name="description" content="{title}. TradingPlan help centre." />
  <meta name="robots" content="index, follow" />

  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('consent', 'default', {{ analytics_storage: 'denied', wait_for_update: 2000 }});
  </script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-YSX1N3B838"></script>
  <script>gtag('js', new Date()); gtag('config', 'G-YSX1N3B838');</script>

  <link rel="stylesheet" href="../../css/main.css?v=3" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
    .article-wrap {{ max-width: 720px; padding: 56px 0 120px; }}
    .article-back {{ display:inline-flex; align-items:center; gap:6px; font-size:.85rem; color:var(--color-text-muted); text-decoration:none; margin-bottom:40px; transition:color .15s; }}
    .article-back:hover {{ color:var(--color-primary); }}
    .article-meta {{ display:flex; align-items:center; gap:12px; margin-bottom:16px; flex-wrap:wrap; }}
    .article-id {{ font-size:.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:var(--color-primary); background:rgba(166,206,255,.1); border:1px solid rgba(166,206,255,.2); padding:3px 10px; border-radius:100px; }}
    .article-cat {{ font-size:.72rem; font-weight:600; color:var(--color-text-dim); text-decoration:none; transition:color .15s; }}
    .article-cat:hover {{ color:var(--color-primary); }}
    .article-date {{ font-size:.8rem; color:var(--color-text-dim); }}
    .article-title {{ font-size:clamp(1.6rem,3vw,2.2rem); font-weight:800; letter-spacing:-.5px; margin-bottom:32px; line-height:1.2; }}
    .article-body h2 {{ font-size:1.05rem; font-weight:700; margin:36px 0 10px; color:var(--color-text); }}
    .article-body h3 {{ font-size:.82rem; font-weight:700; margin:20px 0 6px; color:var(--color-text-dim); text-transform:uppercase; letter-spacing:.8px; }}
    .article-body p {{ font-size:.95rem; color:var(--color-text-muted); line-height:1.8; margin-bottom:14px; }}
    .article-body ul, .article-body ol {{ padding-left:20px; margin-bottom:16px; }}
    .article-body li {{ font-size:.95rem; color:var(--color-text-muted); line-height:1.8; margin-bottom:6px; }}
    .article-body strong {{ color:var(--color-text); font-weight:600; }}
    .article-body em {{ font-style:italic; }}
    .article-body a {{ color:var(--color-primary); text-decoration:none; }}
    .article-body a:hover {{ text-decoration:underline; }}
    .callout {{ background:var(--color-surface); border:1px solid var(--color-border); border-left:3px solid var(--color-primary); border-radius:var(--radius-sm); padding:16px 20px; margin:20px 0; font-size:.9rem; color:var(--color-text-muted); line-height:1.7; }}
    .callout strong {{ color:var(--color-text); }}
    .table-wrap {{ overflow-x:auto; margin:20px 0; border:1px solid var(--color-border); border-radius:var(--radius-sm); }}
    .help-table {{ width:100%; border-collapse:collapse; font-size:.875rem; }}
    .help-table th, .help-table td {{ padding:10px 16px; text-align:left; border-bottom:1px solid var(--color-border); }}
    .help-table th {{ font-weight:700; color:var(--color-text); background:var(--color-surface-2); font-size:.78rem; text-transform:uppercase; letter-spacing:.5px; }}
    .help-table td {{ color:var(--color-text-muted); }}
    .help-table tr:last-child td {{ border-bottom:none; }}
    .contact-box {{ background:var(--color-surface); border:1px solid var(--color-border); border-radius:var(--radius); padding:28px; margin-top:48px; }}
    .contact-box h2 {{ font-size:1.05rem; font-weight:700; margin-bottom:8px; }}
    .contact-box p {{ font-size:.9rem; color:var(--color-text-muted); margin-bottom:16px; line-height:1.7; }}
    .contact-box .btn {{ color:#000 !important; }}
    .article-divider {{ border:none; border-top:1px solid var(--color-border); margin:48px 0 32px; }}
    .article-nav {{ display:flex; justify-content:space-between; gap:16px; flex-wrap:wrap; }}
    .article-nav a {{ font-size:.875rem; color:var(--color-text-muted); text-decoration:none; transition:color .15s; }}
    .article-nav a:hover {{ color:var(--color-primary); }}
  </style>
</head>
<body>

  <nav class="nav">
    <div class="container nav__inner">
      <a href="/" class="nav__logo">
        <img src="../../img/logo160.png" alt="TradingPlan" class="nav__logo-img" />TradingPlan<span>.io</span>
      </a>
      <ul class="nav__links">
        <li><a href="/help/">Help Centre</a></li>
      </ul>
      <a href="https://apps.apple.com/app/id6761687862" class="btn btn--primary nav__cta" target="_blank" rel="noopener">Download Free</a>
    </div>
  </nav>

  <div class="container">
    <div class="article-wrap">

      <a href="/help/" class="article-back">← Help Centre</a>

      <div class="article-meta">
        <span class="article-id">#{art_id}</span>
        <a href="/help/" class="article-cat">{category}</a>
        <span class="article-date">Last updated: April 2026</span>
      </div>

      <h1 class="article-title">{title}</h1>

      <div class="article-body">
{body}

        <div class="contact-box">
          <h2>Still need help?</h2>
          <p>If this article didn't answer your question, our support team is happy to help.</p>
          <a href="mailto:support@tradingplan.io" class="btn btn--primary">Email support@tradingplan.io</a>
        </div>
      </div>

      <hr class="article-divider" />

      <div class="article-nav">
        {nav_prev}
        <a href="/help/">All Articles</a>
        {nav_next}
      </div>

    </div>
  </div>

  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand">
        <a href="/" class="nav__logo">
          <img src="../../img/logo160.png" alt="TradingPlan" class="nav__logo-img" />TradingPlan<span>.io</span>
        </a>
        <p class="footer__copy">&copy; 2026 TradingPlan Ltd.</p>
        <p class="footer__disclaimer">TradingPlan is not a financial advisor. Nothing in this app constitutes financial advice.</p>
      </div>
      <ul class="footer__links">
        <li><a href="https://apps.apple.com/app/id6761687862" target="_blank" rel="noopener">Download on the App Store</a></li>
        <li><a href="/help/">Help Centre</a></li>
        <li><a href="mailto:hello@tradingplan.io">Contact Us</a></li>
        <li><a href="/terms.html">Terms of Service</a></li>
        <li><a href="/privacy.html">Privacy Policy</a></li>
      </ul>
    </div>
  </footer>

  <script src="../../js/cookies.js"></script>
</body>
</html>'''

# ── Helpers ───────────────────────────────────────────────────────────────────
def get_title(lines):
    for l in lines:
        if re.match(r'^# (?!#)', l):
            return l[2:].strip()
    return ''

def get_neighbors(slug, category):
    cat = [(f, s, a, c) for f, s, a, c in ARTICLES if c == category]
    idx = next((i for i, (_, s, _, _) in enumerate(cat) if s == slug), None)
    prev_art = next_art = None
    if idx is not None:
        if idx > 0:
            pf, ps, _, _ = cat[idx - 1]
            pm = FEED / pf / f"{ps}.md"
            if pm.exists():
                pt = get_title(pm.read_text().splitlines())
                prev_art = (ps, pt)
        if idx < len(cat) - 1:
            nf, ns, _, _ = cat[idx + 1]
            nm = FEED / nf / f"{ns}.md"
            if nm.exists():
                nt = get_title(nm.read_text().splitlines())
                next_art = (ns, nt)
    return prev_art, next_art

def keywords_for(title, category):
    words = re.findall(r'\b[a-z]{3,}\b', title.lower())
    return list(set(words + [category.lower(), category.lower().replace(' & ', ' ').replace(' ', '-')]))

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    results = []

    for folder, slug, art_id, category in ARTICLES:
        md_path = FEED / folder / f"{slug}.md"
        if not md_path.exists():
            print(f"  MISSING  {md_path.name}")
            continue

        lines = md_path.read_text(encoding='utf-8').splitlines()
        title  = get_title(lines)
        ex     = excerpt(lines)
        body   = convert(lines)
        prev_art, next_art = get_neighbors(slug, category)

        html = article_page(art_id, title, category, body, prev_art, next_art)
        out  = OUT / f"{slug}.html"
        out.write_text(html, encoding='utf-8')
        print(f"  OK  #{art_id}  {out.name}")

        results.append({
            'id': art_id, 'title': title, 'category': category,
            'date': DATE, 'excerpt': ex,
            'keywords': keywords_for(title, category),
            'url': f'articles/{slug}.html',
        })

    # ── Print articles array for help/index.html ──────────────────────────────
    print("\n\n── Paste into help/index.html <script> ──────────────────────────────────")
    print("const articles = [")
    for r in results:
        print(f"  {{ id: '{r['id']}', title: {json.dumps(r['title'])}, category: {json.dumps(r['category'])}, "
              f"date: '{r['date']}', excerpt: {json.dumps(r['excerpt'])}, "
              f"keywords: {json.dumps(r['keywords'])}, url: '{r['url']}' }},")
    print("];")

if __name__ == '__main__':
    main()
