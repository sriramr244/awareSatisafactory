// src/App.js
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import AddInventory from "./pages/AddInventory";
import AnotherTab from "./pages/AnotherTab";
import Home from "./pages/Home";

function App() {
  return (
    <Router>
      <Sidebar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/add-inventory" element={<AddInventory />} />
        <Route path="/another-tab" element={<AnotherTab />} />
      </Routes>
    </Router>
  );
}

export default App;
