$('body').css('display', 'none');
$('body').fadeIn(400);


$(document).ready(function () {
    $('.smooth').click( function(e) {
        var rd = $(this).attr('href');
        e.preventDefault();

        $('body').fadeOut(400, function() {
            document.location.href = rd;
        })
    });

    $('input').keyup(function() {
        console.log($('input').val())
        $('.smooth').attr('href', '/info/' + $('input').val());
    })
});