var tour = new Tour({
    onEnd: function() {
        $(".tags").trigger('click');
    },
    steps: [
    {
        element: "#step1",
        title: "Add a task!",
        content: "Add a task with its category as a hashtag!"
    },
    {
        element: "#step2",
        title: "Pending tasks",
        content: "View, edit, delete or mark a task complete here",
        placement: 'left'
    },
    {
        element:'#step3',
        title: "Filter with tags",
        content: "Click a tag to view only those tasks that have the tag",
        onNext: function(tour) {
            $(".completed").trigger('click');
        }
    },
    {
        element:"#step4",
        title: "Completed tasks",
        content:"View, undo or delete completed tasks",
    }
]});

$(window).load(function() {
    tour.init();
    tour.start(true);
});