
let vm = avalon.define({
    $id: 'platform',

    fresh_data: function(){
        $.ajax({
            url: '/fresh_data',
            type: 'get',
            success: function (data) {
                
            }
        })
    }

});