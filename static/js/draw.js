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
        backgroundColor: '#404a59',
        title: {
            text: '最近物体实时距离',
            textStyle: {
                fontWeight: 'normal',
                fontSize: 20,
                color: '#F1F1F3'
            },
            left: '6%'
        },
        tooltip: {
            trigger: 'axis', //触发类型。[ default: 'item' ] :数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用;'axis'坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用
            axisPointer: {
                lineStyle: {
                    color: '#57617B'
                }
            }
        },
        grid: {
            left: '3%', //grid 组件离容器左侧的距离。
            right: '4%', //grid 组件离容器右侧的距离。
            bottom: '3%', //grid 组件离容器下侧的距离。
            containLabel: true //grid 区域是否包含坐标轴的刻度标签[ default: false ]
        },
        xAxis: [{
            type: 'value',
            boundaryGap: false, //坐标轴两边留白策略，类目轴和非类目轴的设置和表现不一样
            axisLine: {
                lineStyle: {
                    color: '#F1F1F3' //坐标轴线线的颜色。
                }
            },
            data: data.map(function (item) {
                let item1 = JSON.parse(item);
                console.log(item1['time']);
                return item1['time'];
            })
        }],
        yAxis: [{
            type: 'value', //坐标轴类型。'value' 数值轴，适用于连续数据;'category' 类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据;'time' 时间轴;'log' 对数轴.
            name: '（cm）', //坐标轴名称。
            axisTick: {
                show: false //是否显示坐标轴刻度
            },
            axisLine: {
                lineStyle: {
                    color: '#F1F1F3' //坐标轴线线的颜色
                }
            },
            axisLabel: {
                margin: 10, //刻度标签与轴线之间的距离
                textStyle: {
                    fontSize: 14 //文字的字体大小
                }
            },
            splitLine: {
                lineStyle: {
                    color: '#57617B' //分隔线颜色设置
                }
            }
        }],
        series: [{
            name: '距离',
            type: 'line',
            smooth: true,
            symbol: 'circle',
            symbolSize: 5,
            showSymbol: false,
            lineStyle: {
                normal: {
                    width: 1
                }
            },
            itemStyle: {
                normal: {
                    color: 'rgb(0,136,212)',
                    borderColor: 'rgba(0,136,212,0.2)',
                    borderWidth: 12

                }
            },
            data: data.map(function (item) {
                let item1 = JSON.parse(item);
                console.log(item1['value']);
                return item1['value'];
            })
        },]
    };

    dom_name.setOption(option);
}


