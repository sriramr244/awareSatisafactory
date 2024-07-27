// src/pages/AddInventory.js
import React, { useState } from "react";
import axios from "axios";

const AddInventory = () => {
  const [name, setName] = useState("");
  const [quantity, setQuantity] = useState(0);
  const [message, setMessage] = useState("");

  const addItem = async () => {
    try {
      const response = await axios.post(
        `${process.env.REACT_APP_API_URL}/inventory/`,
        {
          name,
          quantity,
        }
      );
      if (response.status === 200) {
        setMessage(`Added ${quantity} units of ${name} to the inventory`);
      }
    } catch (error) {
      setMessage("Failed to add item");
    }
  };

  return (
    <div>
      <h1>Add Inventory</h1>
      <input
        type="text"
        placeholder="Item Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="number"
        placeholder="Quantity"
        value={quantity}
        onChange={(e) => setQuantity(e.target.value)}
      />
      <button onClick={addItem}>Add Item</button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default AddInventory;
