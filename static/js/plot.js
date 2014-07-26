!function($) {
  $(function() {
    var $rows = $('#table > tbody > tr'),
        data = [];

    $rows.each(function() {
      point = [];
      date = $(this).children('td.date').text().trim();
      date = date.split(/-/gm);
      date = Date.UTC(parseFloat(date[0]), parseFloat(date[1])-1, parseFloat(date[2]));
      point.push(date);
      value = $(this).children('td.value').text().trim();
      value = value.substr(1);
      value = parseFloat(value);
      point.push(value);
      data.push(point);
    });
    data.reverse();

    $('#plot').highcharts('StockChart', {
      rangeSelector : {
        selected : 2,
        inputEnabled: $('#plot').width() > 480,
        buttons: [{
          type: 'day',
          count: 3,
          text: '3d'
        }, {
          type: 'week',
          count: 1,
          text: '1w'
        }, {
          type: 'week',
          count: 2,
          text: '2w'
        }, {
          type: 'month',
          count: 1,
          text: '1m'
        }, {
          type: 'all',
          text: 'All'
        }]
      },
      title : {
        text : 'Portfolio vs Time'
      },
      series : [{
        name : 'Portfolio Value',
        data : data,
        tooltip: {
          valueDecimals: 2
        }
      }],
      xAxis: {
        tickInterval: (24 * 3600 * 1000)*3,
        minRange: (24 * 3600 * 1000)*3
      },
    });
  });
}(window.jQuery)
