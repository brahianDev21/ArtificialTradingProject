// fundamental.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('Script loaded');
    
    try {
        const container = document.getElementById('chart');
        if (!container) {
            throw new Error('Chart container not found');
        }

        // Process the data with proper time formatting
        const historicalPrices = rawData.map(price => ({
            // Convert YYYY-MM-DD to timestamp
            time: price.date.split('T')[0], // Extract date part only
            open: parseFloat(price.open),
            high: parseFloat(price.high),
            low: parseFloat(price.low),
            close: parseFloat(price.close)
        }));
        
        console.log('Sample data point:', historicalPrices[0]);

        const chart = LightweightCharts.createChart(container, {
            width: 600,
            height: 300,
            layout: {
                background: { type: 'solid', color: '#ffffff' },
                textColor: '#333',
            },
            grid: {
                vertLines: { color: '#f0f0f0' },
                horzLines: { color: '#f0f0f0' },
            },
            timeScale: {
                timeVisible: true,
                secondsVisible: false,
            },
        });

        const candleSeries = chart.addCandlestickSeries({
            upColor: '#26a69a', 
            downColor: '#ef5350',
            borderVisible: false,
            wickUpColor: '#26a69a', 
            wickDownColor: '#ef5350'
        });

        // Sort data by date ascending
        historicalPrices.sort((a, b) => new Date(a.time) - new Date(b.time));
        
        candleSeries.setData(historicalPrices);
        chart.timeScale().fitContent();

    } catch (error) {
        console.error('Error creating chart:', error);
        console.error('Sample data:', rawData[0]);
    }
});