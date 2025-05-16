import { useState } from 'react'
import { FormComponent } from './FormComponent/FormComponent'
import { useNavigate } from 'react-router-dom'

interface CreateUserAuthData {
    email: string
    password: string
    confirmPassword: string
}

export const CreateUserForm = () => {
    const [errorMessage, setErrorMessage] = useState<string | null>(null)
    const navigate = useNavigate()

    const onSubmit = async (data: CreateUserAuthData) => {
        try {
            const response = await fetch("https://localhost:8000/users/create", {
                method: "POST",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    email: data.email,
                    password: data.password,
                }),
            })

            if (!response.ok) {
                const errorData = await response.json()
                setErrorMessage('A user with this email already exists.')

                return
            }

            const json = await response.json()
            console.log(json)
            setErrorMessage(null)
            navigate("/")
        } catch (error) {
            console.error(error)
            setErrorMessage('An unexpected error occurred. Please try again.')
        }
    }

    return (
        <>
            <FormComponent<CreateUserAuthData>
                title="Sign Up"
                isLogin={false}
                showError={errorMessage}
                onSubmit={onSubmit}
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
                    },
                    {
                        name: 'confirmPassword',
                        label: 'Confirm Password',
                        type: 'password',
                        placeholder: 'Confirm your password',
                        validation: {
                            required: 'Please confirm your password',
                            validate: (value: string, context: CreateUserAuthData) => value === context.password || 'Passwords do not match'
                        }
                    }
                ]}
            />
        </>
    )
}
