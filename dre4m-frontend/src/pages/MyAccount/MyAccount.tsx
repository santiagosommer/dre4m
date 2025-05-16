import { useEffect, useState } from "react";
import { useAuth } from "../../context/AuthContext"
import { useNavigate } from "react-router-dom";
import "./MyAccount.css"

export const MyAccount = () => {
    const { isAuthenticated } = useAuth();
    const navigate = useNavigate()
    const [toggleState, setToggleState] = useState(1);

    const toggleTab = (index: number) => {
        setToggleState(index)
    }

    useEffect(() => {
        if (!isAuthenticated) {
            navigate("/")
        }
    }, [])

    if (isAuthenticated === null) {
        return null;
    }

    return (
        <div className="tabs-container">
            <div className="tabs-wrapper">


                <nav className="block-tabs">
                    <h1 className="block-title">
                        My Account
                    </h1>
                    <div className="buttons-container">
                        <button onClick={() => toggleTab(1)} className={toggleState === 1 ? "tabs active-tabs" : "tabs"} >Orders</button>
                        <button onClick={() => toggleTab(2)} className={toggleState === 2 ? "tabs active-tabs" : "tabs"} >Log out</button>
                    </div>
                </nav>
                <div className="content-tabs">
                    <div className={toggleState === 1 ? "active-content" : "inactive"}>
                        <h2>This is a header</h2>
                        <br />
                        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. e specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
                    </div>
                    <div className={toggleState === 2 ? "active-content" : "inactive"}>
                        <h2>2 This is a header</h2>
                        <br />
                        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default MyAccount