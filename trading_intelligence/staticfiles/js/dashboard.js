document.addEventListener('DOMContentLoaded', function() {

    const ctx = document.getElementById('balanceChart');
    const chartData = JSON.parse('{{ chart_data|safe }}');
    
    console.log('Sample data point:');
    
    new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [{
                label: 'Account Balance',
                data: chartData,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1,
                fill: false
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day'
                    },
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Balance'
                    }
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Account Balance Over Time'
                }
            }
        }
    });
});
