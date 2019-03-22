function draw_pie(dom_name, data, title) {

    let option = {
        tooltip: {
            formatter: "{a} <br/>{b} : {c}%"
        },
        toolbox: {
            feature: {
                restore: {},
                saveAsImage: {}
            }
        },
        series: [
            {
                name: title,
                type: 'gauge',
                detail: {formatter: '{value}%'},
                data: [{value: 50, name: '完成率'}]
            }
        ]
    };
    dom_name.setOption(option);
}


