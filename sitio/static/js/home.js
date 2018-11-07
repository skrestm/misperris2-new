$(document).ready(function () {
    $(".owl-home").owlCarousel({
        loop: true,
        nav: true,
        items: 1,
        dots: false,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                autoWidth: false,
                autoHeight: false,
                center: false
            },
            768: {
                autoWidth: true,
                autoHeight: true,
                center: true
            }
        }

    });
});
