$(document).ready(function () {
    console.log('hello');
    $('textarea#id_code').on('input', function () {
        if ($(this).val().includes('JSON')) {
            $(this).addClass('rainbow')
        } else {
            $(this).removeClass('rainbow')
        }
    })
});