import { useEffect, useState } from "react";
import { getUsers } from "../services/api";

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    getUsers().then(res => setUsers(res.data));
  }, []);

  const badge = (r) =>
    r === "HIGH" ? "danger" : r === "MEDIUM" ? "warning" : "success";

  return (
    <div className="container mt-4">
      <h2 className="fw-bold mb-4">👥 Users Risk Table</h2>

      <div className="table-card">
        <table className="table table-bordered table-hover align-middle">
          <thead>
            <tr>
              <th>User ID</th>
              <th>Total Accesses</th>
              <th>Avg / Day</th>
              <th>Risk</th>
              <th>Explanation</th>
            </tr>
          </thead>

          <tbody>
            {users.map(u => (
              <tr key={u.user_id}>
                <td className="fw-bold">{u.user_id}</td>
                <td>{u.total_accesses}</td>
                <td>{u.avg_accesses_per_day.toFixed(2)}</td>
                <td>
                  <span className={`badge bg-${badge(u.risk_severity)}`}>
                    {u.risk_severity}
                  </span>
                </td>
                <td>{u.explanation}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Users;
