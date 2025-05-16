import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { LoginForm } from "../components/Forms/LoginForm/LoginForm";
import { useAuth } from "../context/AuthContext";

export const Login = () => {
    const { isAuthenticated } = useAuth();
    const navigate = useNavigate();

    useEffect(() => {
        if (isAuthenticated) {
            navigate("/");
        }
    }, [isAuthenticated, navigate]);

    return (
        <>
            {!isAuthenticated && <LoginForm />}
        </>
    );
};

export default Login;