// helper funcs
function getRandInt(minVal, maxVal) {
    return Math.floor(Math.random()*(maxVal-minVal) + minVal);
}

function getRandElem(arr) {
    v = getRandInt(0, arr.length);
    return arr[v];
}

$(document).ready(function() {

    
    // time

    time = moment().format("h:mm");
    day = moment().format("dddd, MMMM Do");

    $('.time').text(time);
    $('.day').text(day);
    setInterval(function() {
        time = moment().format("h:mm");
        day = moment().format("dddd, MMMM Do");
        $('.time').text(time);
        $('.day').text(day);
    },5000);


    // resizing & overflow
    
    var height = $(window).height();
    $('.mainContainer').css('height', height);
    $('.rightContainer').css('max-height', height);
    $('.rightContainer').css('overflow', "auto");


    $(window).resize(function() {
        var height = $(window).height();
        $('.mainContainer').css('height', height);
    });

    // placeholder
    
    var random_placeholder = [
        "todo #category",
        "todo #category",
        "homework #study",
        "flask web app #code",
        "laundry #errands"
        ];

    $('#todo').attr("placeholder", getRandElem(random_placeholder));
    $('#todo').attr("autocomplete","off");
    $('#todo').attr("size", "30");

    $('.form-group').css('display','inline-block');
    $('.button-div').css('display','inline-block');

    
    // active tab

    $('.completedActive').css('display','none');
    $('.leftNav li').on('click', function() {
        $('.leftNav li').removeClass('active');
        $(this).addClass('active');
        if ($(this).hasClass('tags')) {
            $('.tagsActive').css("display","block");
            $('.completedActive').css('display','none');
        } else if ($(this).hasClass('completed')) {
            $('.tagsActive').css('display','none');
            $('.completedActive').css("display","block");
        }
    });

    // change checkbox
    $(".check").click(function() {
        var fa = '<i class="fa fa-circle check-done animated fadeIn"></i>';
        $(this).text("");
        $(this).append($(fa));
        $(this).next().css("text-decoration","line-through");
        $(this).parent().fadeOut();
    });

});