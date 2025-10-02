import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [status, setStatus] = useState('loading...');

  useEffect(() => {
    // Vite's env variables are exposed on import.meta.env
    const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';

    axios.get(`${apiUrl}/api/v1/health`)
      .then(response => {
        if (response.data.status === 'ok') {
          setStatus('Backend is running!');
        } else {
          setStatus('Backend has an issue.');
        }
      })
      .catch(() => {
        setStatus('Failed to connect to backend.');
      });
  }, []);

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-900 text-white">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-4">Rectifex Analyzer Pro-Score</h1>
        <p className="text-xl">Frontend is running.</p>
        <p className="text-lg mt-2">Backend Status: <span className="font-semibold text-cyan-400">{status}</span></p>
      </div>
    </div>
  )
}

export default App