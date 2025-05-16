import "./Footer.css"
import { FaInstagram } from "react-icons/fa";
import SubscribeForm from "../Forms/SubscribeForm/SubscribeForm";


export const Footer = () => {
    return (
        <>
            <footer className="footer-container">
                <section className="footer-header">
                    <h2>ENTER OUR WORLD, CHASE DRE4MS</h2>
                    <h3>Suscríbete a nuestro newsletter para recibir información de nuestras últimas colecciones, promociones y descuentos exclusivos</h3>
                    <SubscribeForm />
                </section>
                <section className="footer-info">
                    <nav className='footer-info-project'>
                        <h1>The Project</h1>
                        <a href="https://www.instagram.com/dre4m.uy/" className="instagram-icon" aria-label="Instagram de DRE4M">
                            <FaInstagram />
                        </a>
                        <a href="mailto:support@dre4m.in" className="email-link">support@dre4m.in</a>
                    </nav>
                    <nav className='footer-info-about'>
                        <h1>dre4m</h1>
                        <a href="/about">About us</a>
                        <a href="/contact">Contacto</a>
                    </nav>
                    <nav className='footer-info-buy'>
                        <h1>Comprar</h1>
                        <a href="#">FAQ - Como comprar</a>
                        <a href="#">Devoluciones</a>
                        <a href="#">Politicas</a>
                    </nav>
                    <nav className='footer-info-account'>
                        <h1>Cuenta</h1>
                        <a href="#">My Account</a>
                    </nav>
                </section>
                <section className="footer-copyright">
                    <p>Copyright © 2025 DRE4M</p>
                </section>
            </footer>
        </>
    )
}

export default Footer