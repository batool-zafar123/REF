document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle Logic
    const themeToggle = document.getElementById('theme-toggle');
    const moonIcon = document.getElementById('moon-icon');
    const sunIcon = document.getElementById('sun-icon');
    const htmlEl = document.documentElement;
    
    // Check local storage for theme preference
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);

    themeToggle.addEventListener('click', () => {
        const currentTheme = htmlEl.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    });

    function setTheme(theme) {
        htmlEl.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        if (theme === 'dark') {
            moonIcon.style.display = 'block';
            sunIcon.style.display = 'none';
        } else {
            moonIcon.style.display = 'none';
            sunIcon.style.display = 'block';
        }
    }

    // Custom Cursor Logic
    const cursorGlow = document.querySelector('.cursor-glow');
    document.addEventListener('mousemove', (e) => {
        cursorGlow.style.left = e.clientX + 'px';
        cursorGlow.style.top = e.clientY + 'px';
    });

    // Code Tabs Logic (scoped to container)
    document.querySelectorAll('.code-showcase').forEach(showcase => {
        const tabs = showcase.querySelectorAll('.tab');
        const codeBlocks = showcase.querySelectorAll('.code-block');

        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                tabs.forEach(t => t.classList.remove('active'));
                codeBlocks.forEach(c => c.classList.remove('active'));

                tab.classList.add('active');
                const targetId = tab.getAttribute('data-target');
                const targetBlock = showcase.querySelector(`#${targetId}`);
                if (targetBlock) {
                    targetBlock.classList.add('active');
                }
            });
        });
    });

    // Universal Copy to Clipboard Logic
    document.querySelectorAll('.copy-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            let textToCopy = btn.getAttribute('data-copy');
            if (!textToCopy) {
                const parent = btn.closest('.terminal-body, .install-card, .code-block, .code-showcase');
                const codeEl = parent ? parent.querySelector('.command, code, pre') : null;
                textToCopy = codeEl ? codeEl.innerText.trim() : 'pip install matrix-solver-ref';
            }
            navigator.clipboard.writeText(textToCopy).then(() => {
                const originalHTML = btn.innerHTML;
                btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="#27c93f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>';
                setTimeout(() => {
                    btn.innerHTML = originalHTML;
                }, 2000);
            });
        });
    });

    // Scroll Animations using Intersection Observer
    const animatedElements = document.querySelectorAll('.fade-in-up');
    
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Unobserve after animating once for better performance
                obs.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Initial trigger for elements already in viewport on load
    setTimeout(() => {
        animatedElements.forEach(el => {
            if (el.classList.contains('hidden-onload')) {
                el.classList.remove('hidden-onload');
                el.classList.add('visible');
            } else {
                observer.observe(el);
            }
        });
    }, 100);

    // Scroll to Top Logic
    const scrollTopBtn = document.getElementById('scroll-top');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            scrollTopBtn.classList.add('visible');
        } else {
            scrollTopBtn.classList.remove('visible');
        }
    });

    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});
