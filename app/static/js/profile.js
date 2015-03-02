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
        $('.rightContainer').css('max-height', height);
        $('.rightContainer').css('overflow', "auto");
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
            $('.tagsActive').fadeIn('fast');
            $('.completedActive').hide();
        } else if ($(this).hasClass('completed')) {
            $('.tagsActive').hide();
            $('.completedActive').fadeIn('fast');
        }
    });

    $('.todo').hover(function() {
        $(this).find('.check').css({
            "color": "#26ba15"
        });
    }, function() {
        $(this).find('.check').css({
            "color": '#4d80b7'
        });
    });


    // change checkbox
    $(".check").on('click', function() {
        $(this).off('click');
        var post_url = "/done/"+$(this).get(0).id;
        var fa = '<i class="fa fa-circle check-done animated fadeIn"></i>';
        $(this).text("");
        $(this).append($(fa));
        $(this).next().css("text-decoration","line-through");
        $(this).parent().fadeOut();
        $.ajax({
            type: "POST",
            contentType: "application/json; chartype=utf-8",
            url: post_url,
            success: function(response) {
                window.location.href = response;
            }
        });
    });

    // undo completed task
    $(".times").on("click", function() {
        var post_url = "/done/"+$(this).get(0).id;
        $(this).parent().fadeOut();
        
        $.ajax({
            type: "POST",
            contentType: "application/json; chartype=utf-8",
            url: post_url,
            success: function(response) {
                window.location.href = response;
            }
        });
    });

    // delete completed task
    $(".trash").on("click", function() {
        var post_url = "/deleteTodo/"+$(this).get(0).id;
        $(this).parent().fadeOut();
        $.ajax({
            type: "POST",
            contentType: "application/json; chartype=utf-8",
            url: post_url,
            success: function() {
                console.log("deleted");
            }
        });
    });


    // filter tags 

    function filterByTag(tag) {
        $(".todo").each(function(e) {
            var tags = $(this).find(".hashtags").text();
            if (tags.indexOf(tag) < 0) {
                $(this).css({
                    "opacity":"0.2"
                });
            } else {
                $(this).css({
                    "opacity":"1"
                });
            }
        });
    }


    $(".allTags").on("click", function() {
        $(".allTags").removeClass("activeTag");
        $(this).addClass("activeTag");
        var thetag = $(this).find(".thetag").text()
        filterByTag(thetag);
    });

});




