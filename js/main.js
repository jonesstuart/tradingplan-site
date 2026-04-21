/* =========================================
   FAQ ACCORDION
   FAQ items are pre-rendered in HTML for crawlers.
   JS wires up accordion behaviour only.
   ========================================= */
document.querySelectorAll('.faq-item__q').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const isOpen = item.classList.contains('is-open');
    document.querySelectorAll('.faq-item').forEach(el => el.classList.remove('is-open'));
    if (!isOpen) item.classList.add('is-open');
  });
});

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
