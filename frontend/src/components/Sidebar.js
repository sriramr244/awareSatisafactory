// src/components/Sidebar.js
import React from "react";
import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/add-inventory">Add Inventory</Link>
        </li>
        <li>
          <Link to="/another-tab">Another Tab</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Sidebar;
