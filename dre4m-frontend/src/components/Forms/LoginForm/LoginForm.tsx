import { FormComponent } from "../FormComponent/FormComponent"
import { useNavigate } from "react-router-dom"
import { useAuth } from "../../../context/AuthContext"

interface LoginAuthData {
    email: string
    password: string
}



export const LoginForm = () => {
    const navigate = useNavigate()
    const { setIsAuthenticated } = useAuth();

    const onSubmit = async (data: LoginAuthData) => {
        try {

            const response = await fetch("https://localhost:8000/auth/token", {
                method: "POST",
                credentials: "include",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    email: data.email,
                    password: data.password,
                }),
            })

            if (response.ok) {

            }
            const json = await response.json()
            console.log(json)
            setIsAuthenticated(true)
            navigate("/")
        }
        catch (error) {
            console.error(error)
        }
    }
    return (
        <>
            <FormComponent<LoginAuthData>
                onSubmit={onSubmit}
                isLogin={true}
                showError={null}
                title={"Login"}
                submitButtonText="Enter"
                fields={[
                    {
                        name: 'email',
                        label: 'Email',
                        type: 'email',
                        placeholder: 'Enter your email',
                        validation: {
                            required: 'Email is required',
                            pattern: {
                                value: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/,
                                message: 'Invalid email address'
                            }
                        }
                    },
                    {
                        name: 'password',
                        label: 'Password',
                        type: 'password',
                        placeholder: 'Enter your password',
                        validation: {
                            required: 'Password is required',
                            minLength: {
                                value: 6,
                                message: 'Password must be at least 6 characters long'
                            }
                        }
                    }
                ]}
            />
        </>
    )
}
