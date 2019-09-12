$(document).ready(() => {
    $('.project-item').on('click', (e) => {
        const item = $(e.currentTarget);
        if (item.hasClass('details')) {
            item.removeClass('details');
        } else {
            $('.project-item').removeClass('details');
            item.addClass('details');
        }
    });
});
