from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

HOST = "99999" #Use your own IPv4 address
PORT = 9999

# Sample financial data
financial_data = {
    "income": 6000,
    "expenses": 3000,
    "profit": 3000,
    "transactions": [
        {"date": "2024-12-01", "type": "income", "amount": 6000, "description": "Salary"},
        {"date": "2024-12-05", "type": "expense", "amount": 3000, "description": "Rent"},
    ]
}

class FinancialDashboardHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":  # Main Dashboard
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Serve a simple HTML page
            with open("dashboard.html", "r") as file:
                self.wfile.write(bytes(file.read(), "utf-8"))

        elif self.path == "/api/data":  # Serve Financial Data
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(bytes(json.dumps(financial_data), "utf-8"))
        
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/add":  # Add new transaction
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_transaction = json.loads(post_data)

            # Update the financial data
            financial_data["transactions"].append(new_transaction)
            if new_transaction["type"] == "income":
                financial_data["income"] += new_transaction["amount"]
            elif new_transaction["type"] == "expense":
                financial_data["expenses"] += new_transaction["amount"]

            financial_data["profit"] = financial_data["income"] - financial_data["expenses"]

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps({"status": "success"}), "utf-8"))

server = HTTPServer((HOST, PORT), FinancialDashboardHTTP)
print(f"Server running at http://{HOST}:{PORT}/")
server.serve_forever()
