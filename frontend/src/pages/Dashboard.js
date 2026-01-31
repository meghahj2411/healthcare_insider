import { useEffect, useState } from "react";
import { getUsers } from "../services/api";
import { Bar, Pie } from "react-chartjs-2";
import "chart.js/auto";

function Dashboard() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    getUsers().then(res => setUsers(res.data));
  }, []);

  const total = users.length;
  const high = users.filter(u => u.risk_severity === "HIGH").length;
  const medium = users.filter(u => u.risk_severity === "MEDIUM").length;
  const low = users.filter(u => u.risk_severity === "LOW").length;

  return (
    <div className="container mt-4">
      <h2 className="fw-bold mb-4">📊 Security Dashboard</h2>

      <div className="row g-4">
        <div className="col-md-6">
          <div className="stat-card">
            <h5>User Risk Distribution</h5>
            <Pie
              data={{
                labels: ["LOW", "MEDIUM", "HIGH"],
                datasets: [{
                  data: [low, medium, high],
                  backgroundColor: ["#1cc88a", "#f6c23e", "#e74a3b"]
                }]
              }}
            />
          </div>
        </div>

        <div className="col-md-6">
          <div className="stat-card">
            <h5>System Overview</h5>
            <Bar
              data={{
                labels: ["Total Users", "High Risk"],
                datasets: [{
                  data: [total, high],
                  backgroundColor: ["#4e73df", "#e74a3b"]
                }]
              }}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
