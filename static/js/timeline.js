function sendWeibo() {
    $.ajax({
        url: '/timeline/send/',
        type: 'get',
        data: $('#weibo_send_form').serialize(),
        success: function (repo) {
            location.reload();
        },
        error:function(error){
            console.log($('#weibo_send_form').serialize());
        }

    });

}