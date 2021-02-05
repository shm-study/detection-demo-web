// 클릭 했을 때 

$(function() {
    $("#2nd").click(function() {
        size=parseInt($('#1st').css('font-size'));
        size=size+1;
        $("#1st").css("font-size",size + "px")
    });
});

// 마우스를 올렸을 때 mouseenter
$(function() {
    $("#1st").mouseenter(function() {
        $("#2nd").css("color", "yellow")
    });
});

// 마우스를 내렸을 때 mouseleave
$(function() {
    $("#1st").mouseleave(function() {
        $("#2nd").css("color", "black")
    });
});
