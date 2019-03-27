let temp_dom = echarts.init(document.getElementById(TEMPERATURE_DOM));
let light_dom = echarts.init(document.getElementById(LIGHT_DOM));
let distance_dom = echarts.init(document.getElementById(DISTANCE_DOM));

let vm = avalon.define({
    $id: 'platform',
    distance_list: [],
    temperature: '0',
    light: '0',
    start: 0,
    structure_similarity_degree: 0,
    fresh_data: function () {
        $.ajax({
            url: '/get_data?start=' + vm.start,
            type: 'get',
            success: function (data) {
                console.log(data.distance_list.length);
                if (data.distance_list.length > 0){

                     vm.distance_list = vm.distance_list.concat(data.distance_list);
                     vm.draw_distance();
                }

                if (data.temperature) {
                    vm.temperature = data.temperature.value;
                    vm.draw_temperature();
                }
                if (data.light) {
                    vm.light = data.light.value;
                    vm.draw_light();
                }
                vm.start = data.start;

            }
        })
    },
    draw_temperature: function () {
        console.log("draw gauge");
        draw_gauge(temp_dom, vm.temperature, '油箱温度');
    },
    draw_light: function () {
        console.log("draw pie");
        draw_pie(light_dom, vm.light, '光照强度')
    },
    
    draw_distance: function () {
        console.log("draw line");
        draw_line(distance_dom, vm.distance_list);
    }

});

vm.$watch("light", function (new_value, old_value) {
    if (new_value > 1000) {
        console.log('change to light');
        $('#car_light').css("background-image", "url(\"../static/image/car_light.png\")")
    } else {
        console.log('change to no light');
        $('#car_light').css("background-image", "url(\"../static/image/car_no_light.png\")")
    }
});
$(document).ready(function () {
    vm.draw_temperature();
    vm.draw_light();
    vm.draw_distance();
    vm.fresh_data();
    setInterval(function () {
        vm.fresh_data();
    }, 1000);
});
