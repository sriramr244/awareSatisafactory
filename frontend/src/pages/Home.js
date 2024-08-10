// src/pages/Home.js
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

const Home = () => {
  const [tabs, setTabs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTabs = async () => {
      try {
        const response = await axios.get(
          `${process.env.REACT_APP_API_URL}/tabs`
        );
        setTabs(response.data);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchTabs();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>Welcome to the Dashboard</h1>
      <ul>
        {tabs.map((tab) => (
          <li key={tab.id}>
            <Link to={tab.link}>{tab.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
