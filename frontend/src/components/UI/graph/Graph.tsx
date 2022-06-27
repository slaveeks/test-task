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

const labels = ['1', '2', '3', '4', '5'];

const options = {
  responsive: true,
  scales: {
    y: {
      ticks: {
        stepSize: 2000,
      },
    },
    x: {
      grid: {
        display: false,
      },
      ticks: {
        maxRotation: 45,
        minRotation: 45,
      },
    },
  },
  plugins: {
    legend: {
      display: false,
    },
  },
};

const a = [55, 100, 5000, 58000, 10000];

let data = {
  labels,
  datasets: [
    {
      data: a.map((a) => a),
      pointRadius: 0,
      borderColor: '#084de0',
    },
  ],
};

const Graph: React.FC = () => {
  const [googleLabels, setLabels] = useState<SortedData | undefined>(undefined);

  useEffect(() => {
    const exec = async (): Promise<void> => {
      const response = await Transport.getOrderedData();
      console.log(response);
      setLabels(response);
    };

    exec();
  }, []);
  if (googleLabels) {
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
