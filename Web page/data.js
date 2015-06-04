$(function () {
    var distances = [];
    var times = [];
    var switch1 = true;
    $.get('values.php', function (data) {

        data = data.split('/');
        for (var i in data) {
            if (switch1 == true) {
                distances.push(data[i]);
                switch1 = false;
            } else {
                times.push(parseFloat(data[i]));
                switch1 = true;
            }

        }
        distances.pop();

        $('#chart').highcharts({
            chart: {
                type: 'spline'
            },
            title: {
                text: "Don't Sleep"
            },
            xAxis: {
                title: {
                    text: ''
                },
                categories: distances
            },
            yAxis: {
                title: {
                    text: ''
                },
                labels: {
                    formatter: function () {
                        return this.value + 'cm'
                    }
                }
            },
            tooltip: {
                crosshairs: true,
                shared: true,
                valueSuffix: ''
            },
            plotOptions: {
                spline: {
                    marker: {
                        radius: 4,
                        lineColor: '#666666',
                        lineWidth: 1
                    }
                }
            },
            series: [{

                name: '°Å¸®',
                data: times
            }]
        });
    });
});