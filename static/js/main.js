let temp_dom = echarts.init(document.getElementById(TEMPERATURE_DOM));

let vm = avalon.define({
    $id: 'platform',
    distance_list: [],
    temperature: 0,
    light: 0,
    start: 0,

    fresh_data: function(){
        $.ajax({
            url: '/get_data?start=' + vm.start,
            type: 'get',
            success: function (data) {
                if(data.distance_list.length > 0)
                    vm.distance_list = data.distance_list;
                if(data.temperature){
                    vm.temperature = data.temperature;
                    vm.draw_temperature(vm.temperature);
                }

                    
                if(data.light)
                    vm.light = data.light;
                vm.start = data.start;

            }
        })
    },
    draw_temperature: function () {
        draw_gauge(temp_dom, vm.temperature, '油箱温度');
    }

});

$(document).ready(function () {
    vm.draw_temperature();
    setInterval(function () {
        vm.fresh_data();
    }, 1000);

});
