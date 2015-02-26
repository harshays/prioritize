function getRandInt(minVal, maxVal) {
    return Math.floor(Math.random()*(maxVal-minVal) + minVal);
}

function getRandElem(arr) {
    v = getRandInt(0, arr.length);
    return arr[v];
}


$(document).ready(function() {
    var random_placeholder = [
        "todo #category @priority",
        "netflix #procrastinate @4",
        "math homework #study @2",
        "flask web app #code @1",
        "laundry #errands @3"
        ]

    $('#todo').attr("placeholder", getRandElem(random_placeholder));
    $('#todo').attr("autcomplete","off");
});