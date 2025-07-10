// Admin Panel JavaScript
$(document).ready(function() {
    // Enable tooltips
    $('[data-bs-toggle="tooltip"]').tooltip();

    // Enable popovers
    $('[data-bs-toggle="popover"]').popover();

    // Auto-dismiss alerts after 5 seconds
    setTimeout(function() {
        $('.alert').fadeTo(500, 0).slideUp(500, function() {
            $(this).remove();
        });
    }, 5000);

    // Highlight active sidebar item
    const currentUrl = window.location.pathname;
    $('#sidebar .nav-link').each(function() {
        const linkUrl = $(this).attr('href');
        if (currentUrl === linkUrl) {
            $(this).addClass('active');
        }
    });

    // Toggle sidebar on mobile
    $('#sidebarCollapse').on('click', function() {
        $('#sidebar').toggleClass('active');
    });

    // File input label
    $('.custom-file-input').on('change', function() {
        let fileName = $(this).val().split('\\').pop();
        $(this).next('.custom-file-label').addClass("selected").html(fileName);
    });

    // Confirm before delete
    $('.delete-btn').on('click', function() {
        return confirm('Are you sure you want to delete this item?');
    });
});