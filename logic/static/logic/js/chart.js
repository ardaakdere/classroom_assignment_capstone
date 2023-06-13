var xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
var yValues = [55, 49, 44, 24, 15];
var barColors = ["red", "green","blue","orange","brown"];

const config = {
    type: 'bar',
    data: {
      labels: xValues,
      datasets: [{
        label: 'Assigned Course Count',
        data: yValues,
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgb(255, 255, 255)',
        tension: 0.1
      }]
    },
    options: {
    }
  };


  var ctx = document.getElementById('myChart');
  var myChart = new Chart(ctx, config);


function loadDataChart() {
    $.ajax({
        url: '/chart-data/',
        success: (data) => {
            // Initialize arrays for labels and data
            let labels = [];
            let dataset = [];

            // Fill the arrays with data from the server's response
            for (let key in data) {
                labels.push(key);
                dataset.push(data[key]);
            }

            // Use the labels and data to update the chart
            myChart.config.data.labels = labels;
            myChart.config.data.datasets[0].data = dataset;
            myChart.update();
        }
    });
}


function invisible_chart() {
    ctx.style.visibility = 'hidden';
}

function visible_chart() {
    ctx.style.visibility = 'visible';
}