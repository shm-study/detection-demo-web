url = "http://3.37.56.32:5000";

$(function() {

    $('#plus').click(function() {

        $.ajax({
            url: url + "/plus", // 클라이언트가 요청을 보낼 서버의 URL 주소
            data: { a: $('#a').val(), b: $('#b').val() },                // HTTP 요청과 함께 서버로 보낼 데이터
            type: "GET",                             // HTTP 요청 방식(GET, POST)
            dataType: "json"                         // 서버에서 보내줄 데이터의 타입
        })
        
        .done(function(json) {
            $("#result").val(json.ans);
        })

        // HTTP 요청이 실패하면 오류와 상태에 관한 정보가 fail() 메소드로 전달됨.
        .fail(function(xhr, status, errorThrown) {
            $("#result").text("오류가 발생했습니다.");
        })
    });


    $('#minus').click(function() {

        $.ajax({
            url: url + "/minus", // 클라이언트가 요청을 보낼 서버의 URL 주소
            data: { a: $('#a').val(), b: $('#b').val() },                // HTTP 요청과 함께 서버로 보낼 데이터
            type: "GET",                             // HTTP 요청 방식(GET, POST)
            dataType: "json"                         // 서버에서 보내줄 데이터의 타입
        })
        
        .done(function(json) {
            $("#result").val(json.ans);
        })

        // HTTP 요청이 실패하면 오류와 상태에 관한 정보가 fail() 메소드로 전달됨.
        .fail(function(xhr, status, errorThrown) {
            $("#result").text("오류가 발생했습니다.");
        })
    });

    $('#multiply').click(function() {

        $.ajax({
            url: url + "/multiply", // 클라이언트가 요청을 보낼 서버의 URL 주소
            data: { a: $('#a').val(), b: $('#b').val() },                // HTTP 요청과 함께 서버로 보낼 데이터
            type: "GET",                             // HTTP 요청 방식(GET, POST)
            dataType: "json"                         // 서버에서 보내줄 데이터의 타입
        })
        
        .done(function(json) {
            $("#result").val(json.ans);
        })

        // HTTP 요청이 실패하면 오류와 상태에 관한 정보가 fail() 메소드로 전달됨.
        .fail(function(xhr, status, errorThrown) {
            $("#result").text("오류가 발생했습니다.");
        })
    });

    $('#divide').click(function() {

        $.ajax({
            url: url + "/divide", // 클라이언트가 요청을 보낼 서버의 URL 주소
            data: { a: $('#a').val(), b: $('#b').val() },                // HTTP 요청과 함께 서버로 보낼 데이터
            type: "GET",                             // HTTP 요청 방식(GET, POST)
            dataType: "json"                         // 서버에서 보내줄 데이터의 타입
        })
        
        .done(function(json) {
            $("#result").val(json.ans);
        })

        // HTTP 요청이 실패하면 오류와 상태에 관한 정보가 fail() 메소드로 전달됨.
        .fail(function(xhr, status, errorThrown) {
            $("#result").text("오류가 발생했습니다.");
        })
    });
});