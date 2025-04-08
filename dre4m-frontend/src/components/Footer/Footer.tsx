import './Footer.css'
import { FaInstagram } from "react-icons/fa";
import { FormComponent } from '../Forms/FormComponent'

interface SuscriptionEmailData {
    email: string
}

const onSubmit = async (data: SuscriptionEmailData) => {
    try {
        const response = await fetch("http://127.0.0.1:8000/newsletter/", {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-type": "application/json",
            },
            body: JSON.stringify({
                email: data.email,
            }),
        })
        const json = await response.json()
        console.log(json)
    }
    catch (error) {
        console.error(error)
    }
}


export const Footer = () => {
    return (
        <>
            <footer className="footer-container">
                <section className="footer-header">
                    <h2>ENTER OUR WORLD, CHASE DRE4MS</h2>
                    <h3>Suscríbete a nuestro newsletter para recibir información de nuestras últimas colecciones, promociones y descuentos exclusivos</h3>
                    <FormComponent<SuscriptionEmailData>
                        onSubmit={onSubmit}
                        fields={[
                            {
                                name: 'email',
                                label: '',
                                type: 'email',
                                placeholder: 'Correo electrónico',
                                validation: {
                                    required: 'Este campo es obligatorio',
                                    pattern: {
                                        value: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/,
                                        message: 'Correo inválido'
                                    }
                                }
                            },
                        ]}
                        submitButtonText='Suscribirse'
                    />
                </section>
                <section className="footer-info">
                    <div className='footer-info-project'>
                        <h1>The Project</h1>
                        <a href="https://www.instagram.com/dre4m.uy/" className="instagram-icon">
                            <FaInstagram />
                        </a>
                        <a href="mailto:support@dre4m.in" className="email-link">support@dre4m.in</a>
                    </div>
                    <div className='footer-info-about'>
                        <h1>dre4m</h1>
                        <p>About us</p>
                        <p>Contacto</p>
                    </div>
                    <div className='footer-info-buy'>
                        <h1>Comprar</h1>
                        <p>FAQ - Como comprar</p>
                        <p>Devoluciones</p>
                        <p>Politicas</p>
                    </div>
                    <div className='footer-info-account'>
                        <h1>Cuenta</h1>
                        <p>Mi cuenta</p>
                    </div>
                </section>
                <section className="footer-copyright">
                    <p>Copyright © 2025 DRE4M</p>
                </section>
            </footer>
        </>
    )
}

export default Footer