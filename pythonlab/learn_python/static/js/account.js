$(document).ready(function () {
    var inputs = $('table.user-profile tr td:not(.no-edit):nth-of-type(2n) input');
    $('div#user-profile input[type=submit]').click(function (event) {
        if (($(this).attr('data-edited')) === 'false'){
            event.preventDefault();
            if ($(this).hasClass('save')) {
                inputs.attr('readonly', true);
                $(this).val('edytuj').removeClass('save');
                $(this).attr('data-edited', true);
            } else {
                inputs.attr('readonly', false);
                $(this).val('zapisz').addClass('save');
                $(this).attr('data-edited', true);
            }
        }

    });
});