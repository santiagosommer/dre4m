import { Outlet } from "react-router-dom";
import Navbar from "../Navbar/Navbar";
import './Layout.css'
import Marquee from "../Marquee/Marquee";
import SideCart from "../SideCart/SideCart";
import { useState } from "react";

function Layout() {
    const [showCart, setShowCart] = useState(false);

    return (
        <>
            <Navbar onCartClick={() => setShowCart(true)} />
            <Marquee />
            {/* Backdrop */}
            {showCart && <div className="cart-backdrop" onClick={() => setShowCart(false)} />}
            <SideCart open={showCart} onClose={() => setShowCart(false)} />
            <main className="content">
                <Outlet />
            </main>
        </>
    );
}

export default Layout;