# Financial Dashboard Application

## Overview
The Financial Dashboard application is a web-based tool designed for personal finance management. It allows users to monitor their income, expenses, and profit through an interactive dashboard, add new transactions, and visualize financial data via a dynamic pie chart.

---

## Features
1. **Interactive Dashboard:**
   - Displays a summary of income, expenses, and profit.
   - Automatically updates after adding new transactions.

2. **Add Transactions:**
   - Allows users to input financial transactions (income or expenses) with a description, amount, and date.

3. **Dynamic Visualization:**
   - Visualizes financial data as a pie chart using Chart.js.

4. **Real-time Data Fetching:**
   - Updates the dashboard dynamically by interacting with a Python-based backend server.

---

## Technologies Used
1. **Frontend:**
   - **HTML/CSS:** For structuring and styling the user interface.
   - **JavaScript:** For dynamic interactions and API calls.
   - **Chart.js:** For rendering financial data as charts.

2. **Backend:**
   - **Python:** Hosts the backend server for managing and serving financial data.
   - **HTTPServer Module:** Handles HTTP requests and responses.

3. **Communication:**
   - JSON-based API for data exchange between the frontend and backend.

---

## File Structure
- **`dashboard.html`**: Main HTML file containing the financial dashboard interface.
- **`style.css`** (optional): External stylesheet for additional styling.
- **`script.js` (embedded)**: JavaScript for dynamic behavior and API interaction.
- **`server.py`**: Python file serving as the backend server.

---

## Instructions to Use

### Setup
1. **Prepare the Backend:**
   - Ensure Python is installed.
   - Place `server.py` and `dashboard.html` in the same directory.

2. **Run the Server:**
   - Open a terminal.
   - Navigate to the directory containing `server.py`.
   - Run the server: `python server.py`.

3. **Access the Dashboard:**
   - Open a web browser and visit `http://<HOST>:<PORT>/` (replace `<HOST>` and `<PORT>` with the values specified in `server.py`).


