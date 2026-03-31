/* =========================================
   MOBILE NAV TOGGLE
   ========================================= */
const burger = document.querySelector('.nav__burger');
const navLinks = document.querySelector('.nav__links');
const navCta = document.querySelector('.nav__cta');

if (burger) {
  burger.addEventListener('click', () => {
    const isOpen = burger.classList.toggle('is-open');
    if (navLinks) navLinks.style.display = isOpen ? 'flex' : '';
    if (navCta) navCta.style.display = isOpen ? 'inline-flex' : '';
  });
}

/* =========================================
   WAITLIST FORM
   ========================================= */
const waitlistForm = document.getElementById('waitlistForm');

if (waitlistForm) {
  waitlistForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = waitlistForm.querySelector('input[type="email"]');
    const email = input ? input.value.trim() : '';

    if (!email) return;

    fetch('/save_email.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email })
    }).then(() => {
      waitlistForm.innerHTML = `
        <p style="color: var(--color-primary); font-weight: 600; font-size: 1.05rem;">
          You're on the list! We'll be in touch.
        </p>
      `;
    });
  });
}

/* =========================================
   SMOOTH NAV ACTIVE STATE
   ========================================= */
const sections = document.querySelectorAll('section[id]');
const navAnchors = document.querySelectorAll('.nav__links a[href^="#"]');

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      navAnchors.forEach((a) => {
        a.classList.toggle('is-active', a.getAttribute('href') === `#${entry.target.id}`);
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach((s) => observer.observe(s));
