// static/js/hero-transitions.js

document.addEventListener('DOMContentLoaded', function() {
    const heroSlider = document.querySelector('.hero-slider');
    if (!heroSlider) return;

    const slides = document.querySelectorAll('.hero-slide');
    if (slides.length <= 1) return;

    const prevBtn = document.querySelector('.hero-prev');
    const nextBtn = document.querySelector('.hero-next');
    const indicators = document.querySelectorAll('.hero-indicator');

    let currentSlide = 0;
    let slideInterval;
    const slideDuration = 5000; // 5 seconds

    // Initialize slider
    function initSlider() {
        slides[0].classList.add('active');
        if (indicators.length > 0) {
            indicators[0].classList.add('active');
        }
        startSlideShow();
    }

    // Go to specific slide
    function goToSlide(n) {
        slides[currentSlide].classList.remove('active');
        slides[currentSlide].classList.add('prev');

        currentSlide = (n + slides.length) % slides.length;

        slides[currentSlide].classList.add('active');
        slides[currentSlide].classList.remove('prev');

        updateIndicators();
    }

    // Next slide
    function nextSlide() {
        goToSlide(currentSlide + 1);
    }

    // Previous slide
    function prevSlide() {
        goToSlide(currentSlide - 1);
    }

    // Update indicators
    function updateIndicators() {
        indicators.forEach((indicator, index) => {
            if (index === currentSlide) {
                indicator.classList.add('active');
            } else {
                indicator.classList.remove('active');
            }
        });
    }

    // Start slideshow
    function startSlideShow() {
        slideInterval = setInterval(nextSlide, slideDuration);
    }

    // Pause slideshow
    function pauseSlideShow() {
        clearInterval(slideInterval);
    }

    // Event listeners
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            pauseSlideShow();
            nextSlide();
            startSlideShow();
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            pauseSlideShow();
            prevSlide();
            startSlideShow();
        });
    }

    if (indicators.length > 0) {
        indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => {
                pauseSlideShow();
                goToSlide(index);
                startSlideShow();
            });
        });
    }

    // Pause on hover
    heroSlider.addEventListener('mouseenter', pauseSlideShow);
    heroSlider.addEventListener('mouseleave', startSlideShow);

    // Initialize
    initSlider();
});