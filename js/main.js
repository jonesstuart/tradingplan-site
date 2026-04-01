/* =========================================
   FAQ DATA
   ========================================= */
const faqs = [
  {
    q: "What platforms will TradingPlan be available on?",
    a: "TradingPlan is a native Apple app built for iPhone, iPad and Mac. All three are included in a single subscription. Your plan syncs seamlessly across all your devices via iCloud."
  },
  {
    q: "I already have a trading plan in a spreadsheet/Word doc. Why do I need this?",
    a: "A static document is better than nothing — but it's not a system. TradingPlan turns your plan into a living daily operating tool. Your checklist, your rules, your risk parameters are one tap away when you need them. And your plan evolves with you."
  },
  {
    q: "Is this for beginners or experienced traders?",
    a: "Both — but differently. Experienced traders will use it to formalise and systematise what they already know. Newer traders will use it to build the foundation of good habits from the start. What TradingPlan is not is a trading education platform or strategy provider."
  },
  {
    q: "When does TradingPlan launch?",
    a: "We're targeting launch in the coming months. Beta members will get access first and will be notified directly before public launch."
  },
  {
    q: "How much will it cost?",
    a: "Pricing hasn't been finalised. Beta members will receive founding member pricing — significantly below the standard subscription rate. We'll share details with the beta group before launch."
  },
  {
    q: "What markets does TradingPlan support?",
    a: "TradingPlan is market-agnostic. Whether you trade stocks, forex, futures, crypto or options — the principles of a structured trading plan apply universally. You build your plan around your market and your approach."
  },
  {
    q: "Is my data private?",
    a: "Yes. Your trading plan is stored privately on your device and synced via your personal iCloud account. We never see your trading plan data."
  },
  {
    q: "What if I join the beta and it's not right for me?",
    a: "No problem. The beta is free. No payment details required. If it's not the right fit, there's no obligation of any kind."
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
      item.classList.toggle('is-open');
      document.querySelectorAll('.faq-item').forEach(el => {
        if (el !== item) el.classList.remove('is-open');
      });
    });
    faqList.appendChild(item);
  });
}

/* =========================================
   ANIMATED COUNTERS
   ========================================= */
function runCounter(el) {
  const target = parseInt(el.dataset.target, 10);
  const suffix = el.dataset.suffix || '';
  const duration = 1400;
  const steps = duration / 16;
  const inc = target / steps;
  let current = 0;
  const timer = setInterval(() => {
    current = Math.min(current + inc, target);
    el.textContent = Math.round(current) + suffix;
    if (current >= target) clearInterval(timer);
  }, 16);
}

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      runCounter(entry.target);
      counterObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.stat__value[data-target]').forEach(el => counterObserver.observe(el));

/* =========================================
   WAITLIST FORM
   ========================================= */
const waitlistForm = document.getElementById('waitlistForm');
const waitlistBtn  = document.getElementById('waitlistBtn');
const waitlistSuccess = document.getElementById('waitlistSuccess');

if (waitlistForm) {
  waitlistForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const input = waitlistForm.querySelector('input[type="email"]');
    const email = input ? input.value.trim() : '';
    if (!email) return;

    waitlistBtn.disabled = true;
    waitlistBtn.textContent = 'Submitting…';

    try {
      await fetch('/save_email.php', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email })
      });
    } catch (_) { /* fail silently */ }

    waitlistForm.style.display = 'none';
    if (waitlistSuccess) waitlistSuccess.classList.add('is-visible');
  });
}

/* =========================================
   SMOOTH SCROLL
   ========================================= */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth' }); }
  });
});
