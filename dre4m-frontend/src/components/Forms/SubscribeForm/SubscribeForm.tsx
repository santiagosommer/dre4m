import { useForm, SubmitHandler } from "react-hook-form";
import "./SubscribeForm.css"

interface SuscriptionEmailData {
    email: string;
}

export const SubscribeForm = () => {
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<SuscriptionEmailData>()
    const onSubmit: SubmitHandler<SuscriptionEmailData> = async (data: SuscriptionEmailData) => {
        try {
            const response = await fetch("https://localhost:8000/auth/me", {
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

    return (
        <div>
            <form className="subscribe-form" onSubmit={handleSubmit(onSubmit)}>
                <input className="subscribe-input"
                    {...register("email", {
                        required: "El correo electrónico es obligatorio",
                        pattern: {
                            value: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/,
                            message: "Correo inválido",
                        },
                    })}
                    placeholder="Correo electrónico"
                />
                {errors.email && <span style={{ color: 'red' }}>{errors.email.message}</span>}

                <button className="subscribe-button" type="submit">Suscribirse</button>
            </form>
        </div>
    )
}

export default SubscribeForm