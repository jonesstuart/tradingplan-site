/* =========================================
   FAQ DATA
   ========================================= */
const faqs = [
  {
    q: "Is TradingPlan free?",
    a: "Yes — TradingPlan is free to download and includes a genuinely useful set of features: one full strategy with Strategy Flow, one routine with Routine Flow, the complete trade plan builder, and iCloud sync. PRO unlocks unlimited strategies, unlimited routines, the advanced risk framework, flow session history, and PDF export."
  },
  {
    q: "What platforms does TradingPlan run on?",
    a: "TradingPlan is a native Apple app that runs on iPhone, iPad, and Mac. All three are included in a single download — nothing extra to buy. Your plan syncs automatically across all your devices via iCloud."
  },
  {
    q: "What is Strategy Flow?",
    a: "Strategy Flow is TradingPlan's core feature. Once you've built your strategy rules across six sections — directional bias, analysis, entry, stop loss, target, and trade management — you launch a Flow before any trade. The app walks you through every rule step by step, tracking which ones pass and which don't. It turns your written rules into a live execution checklist."
  },
  {
    q: "I already have a trading plan in a spreadsheet. Why do I need this?",
    a: "A static document is better than nothing — but it's not a system. TradingPlan turns your plan into a daily operating tool. Your strategy rules, risk parameters, and routines are one tap away when it matters. The Strategy Flow makes it impossible to skip steps. And your plan evolves as you do."
  },
  {
    q: "Is TradingPlan for beginners or experienced traders?",
    a: "Both — but differently. Experienced traders use it to formalise and systematise what they already know. Newer traders use it to build the foundation of good habits from the start. TradingPlan is not a trading education platform or strategy provider — it's a discipline and execution tool."
  },
  {
    q: "What markets does TradingPlan support?",
    a: "TradingPlan is market-agnostic. Whether you trade stocks, forex, futures, crypto, or options — the principles of a structured trading plan apply universally. You build your strategy around your market and your approach."
  },
  {
    q: "Is my data private?",
    a: "Yes. Your trading plan is stored on your device and synced via your personal iCloud account. We never have access to your trading plan data."
  },
  {
    q: "What is the Lifetime plan?",
    a: "The Lifetime plan is a one-time purchase that gives you permanent PRO access — no renewals, ever. It includes all future PRO features at no additional charge. All billing is handled securely by Apple."
  },
  {
    q: "Can I try PRO before buying?",
    a: "The Annual plan includes a free trial for eligible new subscribers, subject to App Store eligibility. The free tier is genuinely useful — for a single-strategy trader, it's a complete tool with no artificial limits on the features it includes."
  }
];

/* =========================================
   RENDER FAQ
   ========================================= */
const faqList = document.getElementById('faqList');
if (faqList) {
  faqs.forEach(({ q, a }) => {
    const item = document.createElement('div');
    item.className = 'faq-item';
    item.innerHTML = `
      <button class="faq-item__q">
        <span>${q}</span>
        <span class="faq-item__icon">+</span>
      </button>
      <div class="faq-item__a"><p>${a}</p></div>
    `;
    item.querySelector('.faq-item__q').addEventListener('click', () => {
      const isOpen = item.classList.contains('is-open');
      document.querySelectorAll('.faq-item').forEach(el => el.classList.remove('is-open'));
      if (!isOpen) item.classList.add('is-open');
    });
    faqList.appendChild(item);
  });
}

/* =========================================
   SMOOTH SCROLL
   ========================================= */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});
