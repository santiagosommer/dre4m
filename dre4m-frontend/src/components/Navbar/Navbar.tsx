import { Link } from "react-router-dom"
import "./Navbar.css"
import { useAuth } from "../../context/AuthContext"

export const Navbar = () => {
  const { isAuthenticated } = useAuth();

  return (
    <>
      <nav className="navbar">
        <h1 className="navbar-logo">
          <Link className="navbar-log-ref" to="/">DRE4M</Link>
        </h1>
        <ul className="navbar-list">
          <li>
            <Link to="/store">Tienda</Link>
          </li>
          <li>
            <div className="dropdown">
              <div className="droplnk">
                <Link to="/collections">
                  Collections
                  <i className="arrow down"></i>
                </Link>
              </div>
              <div className="dropdown-content">
                <a href="#">ART</a>
                <a href="#">BRUTALISM</a>
                <a href="#">ASIA</a>
              </div>
            </div>
          </li>
          <li>
            <Link to="/faq">FAQ</Link>
          </li>
          <li>
            {isAuthenticated
              ? <Link to="/my-account">My Account</Link>
              : <Link to="/auth/login">Login</Link>
            }
          </li>
          <li>
            <Link to="/cart">Cart</Link>
          </li>
        </ul>
      </nav>
    </>
  )
}

export default Navbar