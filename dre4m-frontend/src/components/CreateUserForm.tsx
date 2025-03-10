import { FormComponent } from './FormComponent'

interface CreateUserAuthData {
    email: string
    password: string
}

const onSubmit = async (data: CreateUserAuthData) => {
    try {
        const response = await fetch("http://127.0.0.1:8000/users/", {
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
        const json = await response.json()
        console.log(json)
    }
    catch (error) {
        console.error(error)
    }
}

export const CreateUserForm = () => {
    return (
        <>
            <h1>Create User</h1>
            <FormComponent<CreateUserAuthData>
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
                    }
                ]}
            />
        </>
    )
}
