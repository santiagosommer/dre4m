import "./Marquee.css";
import { GoPackage } from "react-icons/go";

const Marquee = () => {
    return (
        <div className="wrapper">
            <div className="marquee-text">
                <div className="marquee-text-track">
                    <p>
                        <GoPackage style={{ marginRight: "0.5rem" }} /> ENVIO GRATIS A PARTIR DE $1500
                    </p>
                    <p>
                        <GoPackage style={{ marginRight: "0.5rem" }} /> ENVIO GRATIS A PARTIR DE $1500
                    </p>
                    <p>
                        <GoPackage style={{ marginRight: "0.5rem" }} /> ENVIO GRATIS A PARTIR DE $1500
                    </p>
                    <p aria-hidden="true">
                        <GoPackage style={{ marginRight: "0.5rem" }} /> ENVIO GRATIS A PARTIR DE $1500
                    </p>
                    <p aria-hidden="true">
                        <GoPackage style={{ marginRight: "0.5rem" }} /> ENVIO GRATIS A PARTIR DE $1500
                    </p>
                </div>
            </div>
        </div>
    );
};

export default Marquee;