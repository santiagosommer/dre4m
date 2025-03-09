import { Outlet, Link } from "react-router-dom"
import './Navbar.css'

export const Navbar = () => {
  return (
    <>
      <nav className="navbar">
        <h1 className="navbar__logo">DRE4M</h1>
        <ul className="navbar__list">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/store">Tienda</Link>
          </li>
          <li>
            <Link to="/auth">Create User</Link>
          </li>
        </ul>
      </nav>
      <Outlet />
    </>
  )
}

export default Navbar