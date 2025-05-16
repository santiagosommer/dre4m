import { useForm, SubmitHandler, FieldValues, DefaultValues, Path } from 'react-hook-form'
import "./FormComponent.css"

// Defines the interface for the form props
// These are the props that the FormComponent will receive
interface IFormProps<T extends FieldValues> {
    onSubmit: SubmitHandler<T>
    title: string
    isLogin: boolean
    showError: any
    defaultValues?: T
    fields: Array<{
        name: keyof T
        label: string
        type: string
        placeholder: string
        validation?: object
    }>
    submitButtonText?: string
}

// The FormComponent is a generic component that takes a type parameter T
// The type parameter T is constrained to FieldValues
export const FormComponent = <T extends FieldValues>({
    onSubmit,
    title,
    isLogin,
    showError,
    defaultValues,
    fields = [],
    submitButtonText = "Submit"
}: IFormProps<T>) => {

    // The useForm hook returns predefined functions and objects for handling form state
    const { register, handleSubmit, formState: { errors } } = useForm<T>({
        defaultValues: defaultValues as DefaultValues<T>
    });

    return (
        <div className="card-container">
            <div className="form-container">
                <h1>{title}</h1>
                <p>Please enter your e-mail and your password:</p>
                {showError && <p style={{ color: 'red' }}>{showError}</p>}
                <form className="form-fields" onSubmit={handleSubmit(onSubmit)} noValidate>
                    {fields.map((field) => (
                        <div className="input-container" key={field.name as string}>
                            <input
                                id={field.name as string}
                                type={field.type}
                                placeholder={field.placeholder}
                                {...register(field.name as Path<T>, field.validation)}
                            />
                            {errors[field.name] && (
                                <p className="error-message show">
                                    {(errors[field.name] as any)?.message}
                                </p>
                            )}
                        </div>
                    ))}
                    <button type="submit">{submitButtonText}</button>
                </form>
            </div>
            {isLogin && (
                <p>Don't have an account? <a href="/auth/signup" className="sign-up-link">Create one</a></p>
            )}
        </div>
    );
};
