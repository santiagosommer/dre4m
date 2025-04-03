import { useForm, SubmitHandler, FieldValues, DefaultValues, Path } from 'react-hook-form'

// Defines the interface for the form props
// These are the props that the FormComponent will receive
interface IFormProps<T extends FieldValues> {
    onSubmit: SubmitHandler<T>
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
    defaultValues,
    fields = [],
    submitButtonText = "Submit"
}: IFormProps<T>) => {

    // The useForm hook returns predefined functions and objects for handling form state
    const { register, handleSubmit, formState: { errors } } = useForm<T>({
        defaultValues: defaultValues as DefaultValues<T>
    });

    return (
        <form onSubmit={handleSubmit(onSubmit)} noValidate>
            {fields.map((field) => (
                <div key={field.name as string}>
                    <label htmlFor={field.name as string}>{field.label}</label>
                    <input
                        id={field.name as string}
                        type={field.type}
                        placeholder={field.placeholder}
                        {...register(field.name as Path<T>, field.validation)}
                    />
                    {errors[field.name] && <p style={{ color: 'red' }}>{(errors[field.name] as any)?.message}</p>}
                </div>
            ))}
            <button type="submit">{submitButtonText}</button>
        </form>
    );
};
