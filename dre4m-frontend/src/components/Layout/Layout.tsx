import { Outlet } from "react-router-dom";
import Navbar from "../Navbar/Navbar";
import './Layout.css'
import Marquee from "../Marquee";

function Layout() {
    return (
        <>
            <Navbar />
            <Marquee />
            <main className="content">
                <Outlet />
            </main>
        </>
    );
}

export default Layout;