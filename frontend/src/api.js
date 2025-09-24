// frontend/src/api.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/', // APIのベースURL
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;
