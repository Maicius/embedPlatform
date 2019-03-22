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

function draw_line(dom_name, data) {
    let option = {
        title: {
            text: '实时距离',
            left: 'left',
            textStyle: {
                color: '#fff'
            }
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        backgroundColor: '#404a59',
        tooltip: {
            trigger: 'axis'
        },
        xAxis: {
            data: data.map(function (item) {
                let item1 = JSON.parse(item);
                return item1['time'];
            }),
            axisLine: {
                lineStyle: {
                    color: 'white',
                    width: 2
                }
            }
        },
        yAxis: {
            splitLine: {
                show: false
            },
            axisLine: {
                lineStyle: {
                    color: 'white',
                    width: 2
                }
            }
        },
        dataZoom: [{
            startValue: '2017-06-01 00:00:00',
            textStyle: {
                color: '#8392A5'
            },
            dataBackground: {
                areaStyle: {
                    color: '#8392A5'
                },
                lineStyle: {
                    opacity: 0.8,
                    color: '#8392A5'
                }
            },
        }, {
            type: 'inside'
        }],
        visualMap: {
            top: 10,
            right: 10,
            textStyle: {
                color: '#fff'
            },
            pieces: [{
                gt: 0,
                lte: 5,
                color: '#096'
            }, {
                gt: 5,
                lte: 10,
                color: '#ffde33'
            }, {
                gt: 10,
                lte: 30,
                color: '#ff9933'
            }, {
                gt: 30,
                lte: 60,
                color: '#cc0033'
            }, {
                gt: 60,
                lte: 90,
                color: '#660099'
            }, {
                gt: 90,
                color: '#7e0023'
            }],
            outOfRange: {
                color: '#999'
            }
        },
        series: [{
            name: 'distance',
            left: 'center',
            type: 'line',
            data: data.map(function (item) {
                let item2 = JSON.parse(item);
                return item2['value'];
            })
        }]
    };
    dom_name.setOption(option);
}


