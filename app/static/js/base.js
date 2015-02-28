$(document).ready(function() {
    var elem = $(".btn");
    var div = "<div class='button-div text-center'> </div>";
    $(elem).wrap(div);

    $("form").attr("autocomplete", "off");
});