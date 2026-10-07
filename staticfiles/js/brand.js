document.addEventListener("DOMContentLoaded", function () {

    const brandSlider = document.querySelector(".index-brand-slider");
    const brandTrack = document.querySelector(".index-brand-track");

    if (!brandSlider || !brandTrack) {
        return;
    }

    /* =========================================
       Pause slider when mouse enters
    ========================================= */

    brandSlider.addEventListener("mouseenter", function () {
        brandTrack.style.animationPlayState = "paused";
    });


    /* =========================================
       Resume slider when mouse leaves
    ========================================= */

    brandSlider.addEventListener("mouseleave", function () {
        brandTrack.style.animationPlayState = "running";
    });


    /* =========================================
       Touch support
    ========================================= */

    brandSlider.addEventListener("touchstart", function () {
        brandTrack.style.animationPlayState = "paused";
    }, { passive: true });


    brandSlider.addEventListener("touchend", function () {
        brandTrack.style.animationPlayState = "running";
    }, { passive: true });

});