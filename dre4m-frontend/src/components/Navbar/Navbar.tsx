import { Link } from "react-router-dom"
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
          <li>
            <Link to="/product-creation">Create Product</Link>
          </li>
          <li>
            <Link to="/address-creation">Create address</Link>
          </li>
        </ul>
      </nav>
    </>
  )
}

export default Navbar