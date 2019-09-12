$(document).ready(() => {
    $('.project-item').on('click', (e) => {
        const item = $(e.target);
        if (item.hasClass('details')) {
            item.removeClass('details');
        } else {
            item.addClass('details');
        }
    });
});
