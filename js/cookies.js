/* =========================================
   COOKIE BANNER + GA CONSENT MODE
   ========================================= */
(function () {
  const STORAGE_KEY = 'tp_cookie_consent';

  function updateConsent(granted) {
    if (typeof gtag === 'function') {
      gtag('consent', 'update', {
        analytics_storage: granted ? 'granted' : 'denied'
      });
    }
  }

  function hideBanner() {
    const banner = document.getElementById('cookieBanner');
    if (banner) {
      banner.style.opacity = '0';
      banner.style.transform = 'translateY(12px)';
      setTimeout(() => banner.remove(), 300);
    }
  }

  // If already decided, apply silently and stop
  const stored = localStorage.getItem(STORAGE_KEY);
  if (stored) {
    updateConsent(stored === 'granted');
    return;
  }

  // Inject banner
  const banner = document.createElement('div');
  banner.id = 'cookieBanner';
  banner.className = 'cookie-banner';
  banner.innerHTML = `
    <p class="cookie-banner__text">
      We use cookies to understand how visitors use our site.
      <a href="/privacy.html">Privacy Policy</a>.
    </p>
    <div class="cookie-banner__actions">
      <button class="cookie-banner__decline" id="cookieDecline">Decline</button>
      <button class="cookie-banner__accept" id="cookieAccept">Accept</button>
    </div>
  `;
  document.body.appendChild(banner);

  // Animate in
  requestAnimationFrame(() => {
    banner.style.opacity = '1';
    banner.style.transform = 'translateY(0)';
  });

  document.getElementById('cookieAccept').addEventListener('click', function () {
    localStorage.setItem(STORAGE_KEY, 'granted');
    updateConsent(true);
    hideBanner();
  });

  document.getElementById('cookieDecline').addEventListener('click', function () {
    localStorage.setItem(STORAGE_KEY, 'denied');
    updateConsent(false);
    hideBanner();
  });
})();
