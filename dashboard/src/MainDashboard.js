import React, { useState, useEffect } from 'react';
import axios from 'axios';

function MainDashboard() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/api/vendor_clients/')
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Main Dashboard!</h1>
      <p>{message}</p>
    </div>
  );
}

export default MainDashboard;