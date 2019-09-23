$(document).ready(() => {
    $('.tagline').t({
        speed_vary: true,
        mistype: 1,
        caret: "_",
        blink: true,
        blink_perm: false,
    });

    $('.project-item').on('mouseover', (e) => {
        const item = $(e.currentTarget);
        if (item.hasClass('details')) {
            item.removeClass('details');
        } else {
            $('.project-item').removeClass('details');
            item.addClass('details');
        }
    });
});
