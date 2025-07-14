// Additional transition effects
document.addEventListener('DOMContentLoaded', function() {
    // Parallax effect for sections
    const parallaxSections = document.querySelectorAll('.parallax');

    window.addEventListener('scroll', function() {
        const scrollPosition = window.pageYOffset;

        parallaxSections.forEach(section => {
            const speed = parseFloat(section.dataset.parallaxSpeed) || 0.5;
            const offset = scrollPosition * speed;
            section.style.backgroundPositionY = `${offset}px`;
        });
    });

    // Card hover animations
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
            this.style.boxShadow = '0 15px 30px rgba(0,0,0,0.15)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 5px 15px rgba(0,0,0,0.1)';
        });
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
});