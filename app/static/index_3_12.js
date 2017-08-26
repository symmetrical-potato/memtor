$('body').css('display', 'none');
$('body').fadeIn(400);


$(document).ready(function () {



    $('.smooth').click( function(e) {
        var rd = $(this).attr('href');
        e.preventDefault();

        $('body').fadeOut(400, function() {
            document.location.href = rd;
        })
    })

    // $('.input-group-btn').click( function() {
    //     $(this).children('button').html('<div class="loader"></div>');
    //
    //     console.log('111');
    //     console.log(showTestView);
    //
    //     setTimeout(500, function () {
    //         $('body').fadeOut(400, function () {
    //             console.log(document.location.href);
    //             window.location.href = 'http://localhost:5000/test';
    //         });
    //     });
    // });

    // $('#smooth').click(function (e) {
    //     var rd = $(this).attr('href');
    //     e.preventDefault();
    //
    // })
});