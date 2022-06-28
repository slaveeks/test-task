import React, {useState, useEffect} from 'react';
import {Line} from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import {Transport} from '../../../transport/transport';
import {SortedData} from '../../../transport/types/SortedData';

ChartJS.register(
    CategoryScale,
    LinearScale,
    LineElement,
    PointElement,
    Title,
    Tooltip,
    Legend,
);

// Base labels for Graph
const baseLabels = ['22.05.22', '25.05.22'];

// Base data for graph
const baseData = [0, 0, 0, 0];

const options = {
  // Make responsive for parent
  responsive: true,
  scales: {
    y: {
      ticks: {
        // Make y coords labels' steps 2000
        stepSize: 2000,
      },
    },
    x: {
      grid: {
        // Not display x lines
        display: false,
      },
      ticks: {
        // X labels rotation
        maxRotation: 45,
        minRotation: 45,
      },
    },
  },
  plugins: {
    legend: {
      // Do not display legend
      display: false,
    },
  },
};

// Initiate base data for graph
let data = {
  labels: baseLabels,
  datasets: [
    {
      data: baseData.map((data) => data),
      pointRadius: 0,
      borderColor: '#084de0',
    },
  ],
};

const Graph: React.FC = () => {
  // Make state to change graph
  const [googleLabels, setLabels] = useState<SortedData | undefined>(undefined);

  useEffect(() => {
    const exec = async (): Promise<void> => {
      // Make response to get data for graph
      const response = await Transport.getOrderedData();
      setLabels(response);
    };

    exec();
  }, []);
  if (googleLabels) {
    // Change graph data
    data = {
      labels: googleLabels.labels,
      datasets: [
        {
          data: googleLabels.values.map((val) => val),
          pointRadius: 0,
          borderColor: '#084de0',
        },
      ],
    };
  }
  return (
    <Line data={data} options={options} />
  );
};

export default Graph;
