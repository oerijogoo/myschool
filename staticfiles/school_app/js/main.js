// Initialize Bootstrap components
document.addEventListener('DOMContentLoaded', function() {
    // Enable tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize carousel with pause on hover
    const heroCarousel = document.getElementById('heroCarousel');
    if (heroCarousel) {
        const carousel = new bootstrap.Carousel(heroCarousel, {
            interval: 5000,
            pause: 'hover'
        });
    }

    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });

    // Initialize hero transitions
    initHeroTransitions();
});

function initHeroTransitions() {
    const heroContainer = document.querySelector('.hero-transition');
    if (!heroContainer) return;

    const transitionStyle = heroContainer.dataset.transition;
    const slides = heroContainer.querySelectorAll('.hero-slide');
    let currentSlide = 0;

    // Activate first slide
    slides[currentSlide].classList.add('active');

    // Transition to next slide
    setInterval(() => {
        // Remove active class from current slide
        slides[currentSlide].classList.remove('active');

        // Move to next slide
        currentSlide = (currentSlide + 1) % slides.length;

        // Add active class to new slide
        slides[currentSlide].classList.add('active');
    }, 5000); // Change slide every 5 seconds
}