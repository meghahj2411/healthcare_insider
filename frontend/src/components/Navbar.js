import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar navbar-dark bg-dark px-4">
      <span className="navbar-brand fw-bold">
        🛡️ Insider Threat System
      </span>

      <div className="ms-auto">
        <Link to="/" className="nav-btn">Home</Link>
        <Link to="/dashboard" className="nav-btn">Dashboard</Link>
        <Link to="/users" className="nav-btn">Users</Link>
      </div>
    </nav>
  );
}

export default Navbar;
