import { Link } from "react-router-dom"
import './Navbar.css'

export const Navbar = () => {
  return (
    <>
      <nav className="navbar">
        <h1 className="navbar__logo">
          <Link className="navbar__log__ref" to="/">DRE4M</Link>
        </h1>
        <ul className="navbar__list">
          <li>
            <Link to="/store">Tienda</Link>
          </li>
          <li>
            <div className="dropdown">
              <a className="droplnk">
                <Link to="/collections">
                  Collections
                  <i className="arrow down"></i>
                </Link>
              </a>
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
            <Link to="/my-account">Mi cuenta</Link>
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