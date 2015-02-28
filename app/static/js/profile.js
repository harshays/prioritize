function getRandInt(minVal, maxVal) {
    return Math.floor(Math.random()*(maxVal-minVal) + minVal);
}

function getRandElem(arr) {
    v = getRandInt(0, arr.length);
    return arr[v];
}
time = moment().format("h:mm A");

$(document).ready(function() {
    
    // time
    $('.time').text(time);
    setInterval(function() {
        time = moment().format("h:mm A");
        $('.time').text(time);
        
    },5000);


    // resizing
    var height = $(window).height();
    $('.mainContainer').css('height', height);

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
        ]

    $('#todo').attr("placeholder", getRandElem(random_placeholder));
    $('#todo').attr("autocomplete","off");
    $('#todo').attr("size", "30");

    // // adding custom submit button
    // $('.form-group').after('<div class="button-div"></div>')
    // $('.button-div').append("<div class='button-div'><i class='fa fa-plus'></i></div>");
    // $('.form-group').css('display','inline-block');
    // $('.button-div').css('display','inline-block');

    
    // var $btn = $("body").find('.button-div');
    // $($btn).on('click', function() {
    //     $.post('/profile', $('#todo').serialize(), function() {
    //         console.log($('#todo').serialize());
    //     });
    // });
});