function draw_gauge(dom_name, data, title) {
    let option = {
        tooltip: {
            formatter: "{a}: <br/>{c} <sup>o</sup>C"
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        series: [
            {
                name: title,
                type: 'gauge',
                detail: {formatter: '{value}'},
                data: [{value: data, name: title}],
                axisLine: { // 坐标轴线
                    lineStyle: { // 属性lineStyle控制线条样式
                        color: [
                            [0.2, 'lime'],
                            [0.82, '#1e90ff'],
                            [1, '#ff4500']
                        ],
                        width: 20,
                        shadowColor: '#fff', //默认透明
                        shadowBlur: 10
                    }
                },
                title: {
                    textStyle: { // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                        fontWeight: 'bolder',
                        fontSize: 20,
                        fontStyle: 'italic',
                        color: '#fff',
                        shadowColor: '#fff', //默认透明
                        shadowBlur: 10
                    }
                },

            },

        ]
    };
    dom_name.setOption(option);
}

function draw_pie(dom_name, data_light, title) {
    let option = {
            backgroundColor: '#404a59',

            title: {
                text: data_light,
                x: 'center',
                y: 'center',
                textStyle: {
                    color: '#98a0c4',
                    fontWeight: 'bolder',
                    fontSize: 32,
                }
            },
            series: [{
                type: 'pie',
                radius: ['39%', '49%'],
                silent: true,
                label: {
                    normal: {
                        show: false,
                    }
                },

                data: [{
                    value: 1,
                    itemStyle: {
                        normal: {
                            color: '#404a59',
                            shadowBlur: 10,
                            shadowColor: '#1b1e25',
                        }
                    }
                }],

                animation: false
            },

                {
                    type: 'pie',
                    radius: ['39%', '49%'],
                    silent: true,
                    label: {
                        normal: {
                            show: false,
                        }
                    },

                    data: [{
                        value: 1,
                        itemStyle: {
                            normal: {
                                color: '#313443',
                                shadowBlur: 50,
                                shadowColor: '#1b1e25'
                            }
                        }
                    }],

                    animation: false
                },

                {
                    name: 'main',
                    type: 'pie',
                    radius: ['50%', '51%'],
                    label: {
                        normal: {
                            show: false,
                        }
                    },
                    data: [{
                        value: data_light,
                        itemStyle: {
                            normal: {
                                color: '#fb358a',
                                shadowBlur: 10,
                                shadowColor: '#fb358a'
                            }
                        }
                    }, {
                        value: 1 - data_light,
                        itemStyle: {
                            normal: {
                                color: 'transparent'
                            }
                        }
                    }],

                    animationEasingUpdate: 'cubicInOut',
                    animationDurationUpdate:
                        500
                }
            ]
        }
    ;
    dom_name.setOption(option);
}


