(() => {
  const header = document.querySelector('[data-header]');
  const menuToggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-menu]');
  const backToTop = document.querySelector('[data-back-to-top]');

  const onScroll = () => {
    const y = window.scrollY;
    header?.classList.toggle('is-scrolled', y > 24);
    backToTop?.classList.toggle('is-visible', y > 600);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  menuToggle?.addEventListener('click', () => {
    const open = menu?.classList.toggle('is-open');
    document.body.classList.toggle('menu-open', open);
    menuToggle.setAttribute('aria-expanded', String(Boolean(open)));
  });
  menu?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    menu.classList.remove('is-open');
    document.body.classList.remove('menu-open');
    menuToggle?.setAttribute('aria-expanded', 'false');
  }));
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      menu?.classList.remove('is-open');
      document.body.classList.remove('menu-open');
      menuToggle?.setAttribute('aria-expanded', 'false');
      closeLightbox();
    }
  });
  backToTop?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  // Scroll reveal
  const reveals = [...document.querySelectorAll('[data-reveal]')];
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px' });
    reveals.forEach(el => observer.observe(el));
  } else reveals.forEach(el => el.classList.add('is-visible'));

  // Reference filters
  const filterButtons = document.querySelectorAll('[data-filter]');
  const filterItems = document.querySelectorAll('.filter-gallery [data-category]');
  filterButtons.forEach(button => button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    filterButtons.forEach(b => b.classList.toggle('is-active', b === button));
    filterItems.forEach(item => item.classList.toggle('is-hidden', filter !== 'all' && item.dataset.category !== filter));
  }));

  // Lightbox
  const lightbox = document.querySelector('[data-lightbox]');
  const lightboxImage = lightbox?.querySelector('img');
  const lightboxCaption = lightbox?.querySelector('p');
  const closeButton = lightbox?.querySelector('.lightbox-close');
  function openLightbox(src, caption) {
    if (!lightbox || !lightboxImage) return;
    lightboxImage.src = src;
    lightboxImage.alt = caption || 'Nagyított referenciafotó';
    if (lightboxCaption) lightboxCaption.textContent = caption || '';
    lightbox.hidden = false;
    document.body.style.overflow = 'hidden';
    closeButton?.focus();
  }
  function closeLightbox() {
    if (!lightbox) return;
    lightbox.hidden = true;
    document.body.style.overflow = '';
    if (lightboxImage) lightboxImage.src = '';
  }
  document.querySelectorAll('[data-lightbox-src]').forEach(btn => btn.addEventListener('click', () => openLightbox(btn.dataset.lightboxSrc, btn.dataset.lightboxCaption)));
  closeButton?.addEventListener('click', closeLightbox);
  lightbox?.addEventListener('click', e => { if (e.target === lightbox) closeLightbox(); });

  // Contact form: prepares a mailto, no hidden data transmission in the static prototype.
  const contactForm = document.querySelector('[data-contact-form]');
  contactForm?.addEventListener('submit', e => {
    e.preventDefault();
    if (!contactForm.reportValidity()) return;
    const data = new FormData(contactForm);
    const destination = contactForm.dataset.email;
    const subject = encodeURIComponent(`Weboldali megkeresés – ${data.get('type') || 'projekt'}`);
    const body = encodeURIComponent([
      `Név / cégnév: ${data.get('name') || ''}`,
      `E-mail: ${data.get('email') || ''}`,
      `Telefon: ${data.get('phone') || ''}`,
      `Projekt típusa: ${data.get('type') || ''}`,
      '',
      'Projekt leírása:',
      data.get('message') || ''
    ].join('\n'));
    const status = contactForm.querySelector('.form-status');
    if (status) status.textContent = 'Megnyitjuk a levelezőprogramot az előkészített üzenettel.';
    window.location.href = `mailto:${destination}?subject=${subject}&body=${body}`;
  });

  // Demo newsletter forms
  document.querySelectorAll('[data-demo-form]').forEach(form => form.addEventListener('submit', e => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    const button = form.querySelector('button');
    const original = button.textContent;
    button.textContent = 'Rögzítve';
    button.disabled = true;
    setTimeout(() => { button.textContent = original; button.disabled = false; form.reset(); }, 1800);
  }));

  // Minimal cookie notice
  const banner = document.querySelector('[data-cookie-banner]');
  const accepted = localStorage.getItem('legradi-cookie-notice');
  if (banner && !accepted) banner.hidden = false;
  banner?.querySelector('[data-cookie-accept]')?.addEventListener('click', () => {
    localStorage.setItem('legradi-cookie-notice', 'accepted');
    banner.hidden = true;
  });
})();
