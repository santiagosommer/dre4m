import { useNavigate } from "react-router-dom";
import { CreateUserForm } from "../components/Forms/SignUpForm"
import { useAuth } from "../context/AuthContext"
import { useEffect } from "react";

export const SignUp = () => {
    const { isAuthenticated } = useAuth();
    const navigate = useNavigate();

    useEffect(() => {
        if (isAuthenticated) {
            navigate("/")
        }
    }, [isAuthenticated, navigate])

    return (
        <>
            {!isAuthenticated && <CreateUserForm />}
        </>
    )
}

export default SignUp