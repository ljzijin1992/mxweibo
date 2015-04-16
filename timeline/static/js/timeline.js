function sendWeibo() {
    $.ajax({
        url: '/timeline/send/',
        type: 'POST',
        data: $('#weibo_send_form').serialize(),
        success: function (resp) {
            if(resp =='200'){location.reload();}
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function likes() {
    $.ajax({
        url: '/timeline/likes/',
        type: 'POST',
        data: {'timeline_id':$('#timeline_id').text()},
        success: function (resp) {
            if(resp =='200'){location.reload();}
        },
        error: function (error) {
            console.log(error);
        }
    });
}