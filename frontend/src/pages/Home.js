import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="container mt-5">
      <div className="row align-items-center">
        {/* LEFT */}
        <div className="col-md-6">
          <h1 className="hero-title">
            Healthcare Insider <br />
            <span style={{ color: "#4e73df" }}>
              Threat Detection Platform
            </span>
          </h1>

          <p className="hero-sub">
            A secure, ML-powered healthcare monitoring system designed
            to detect suspicious insider activity using audit logs,
            behavioral analysis, and explainable risk scoring.
          </p>

          <div className="row mt-4">
            <div className="col-md-6">
              <Link to="/dashboard" style={{ textDecoration: "none" }}>
                <div className="action-card blue">
                  📊 View Security Dashboard
                </div>
              </Link>
            </div>

            <div className="col-md-6">
              <Link to="/users" style={{ textDecoration: "none" }}>
                <div className="action-card green">
                  👥 View User Risk Table
                </div>
              </Link>
            </div>
          </div>
        </div>

        {/* RIGHT */}
        <div className="col-md-6 text-center">
          <img
            src="https://cdn-icons-png.flaticon.com/512/2966/2966327.png"
            alt="Medical Security"
            className="img-fluid"
            style={{ maxHeight: "380px" }}
          />
        </div>
      </div>
    </div>
  );
}

export default Home;
