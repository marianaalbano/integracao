$("document").ready(function(){
    $(".stop-container").each(function(){
        $(this).click(function(e){
            var container_id = $(this).attr("id");
            $.ajax({
                url:"/container/stop/",
                type: "POST",
                data: {id:container_id}
                })
            .done(function(data){
                console.log(data);
                alert(data.message);
            })
            .fail(function(data){
                console.log(data);
                alert(data.message);
            })
        });
    });

    $(".start-container").each(function(){
        $(this).click(function(e){
            var container_id = $(this).attr("id");
            $.ajax({
                url:"/container/start/",
                type: "POST",
                data: {id:container_id}
                })
            .done(function(data){
                console.log(data);
                alert(data.message);
            })
            .fail(function(data){
                console.log(data);
                alert(data.message);
            })
        });
    });

    $(".remove-container").each(function(){
        $(this).click(function(e){
            var container_id = $(this).attr("id");
            $.ajax({
                url:"/container/remove/",
                type: "DELETE",
                data: {id:container_id}
                })
            .done(function(data){
                console.log(data);
                alert(data.message);
            })
            .fail(function(data){
                console.log(data);
                alert(data.message);
            })
        });
    });
});