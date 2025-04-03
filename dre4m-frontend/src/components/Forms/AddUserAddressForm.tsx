import { FormComponent } from './FormComponent'

interface AddAddressData {
    street_address: String
    address_info: String
    city: String
    state_or_province: String
    zip_code: String
    country: String
    phone_number: String
}

const onSubmit = async (data: AddAddressData) => {
    try {
        const response = await fetch("http://127.0.0.1:8000/addresses/", {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                street_address: data.street_address,
                address_info: data.address_info,
                city: data.city,
                state_or_province: data.state_or_province,
                zip_code: data.zip_code,
                country: data.country,
                phone_number: data.phone_number
            }),
        })
        const json = await response.json()
        console.log(json)
    }
    catch (error) {
        console.error(error)
    }
}

export const AddUserAddressForm = () => {
    return (
        <>
            <h1>Add address</h1>
            <FormComponent<AddAddressData>
                onSubmit={onSubmit}
                fields={[
                    {
                        name: 'street_address',
                        label: 'Street Address',
                        type: 'text',
                        placeholder: 'Enter your street address',
                        validation: {
                            required: 'Street Address is required'
                        }
                    },
                    {
                        name: 'address_info',
                        label: 'Apartment/Suit/etc',
                        type: 'text',
                        placeholder: 'Enter Apartment/Suit/etc',
                        validation: {
                            required: 'This field is required'
                        }
                    },
                    {
                        name: 'city',
                        label: 'City',
                        type: 'text',
                        placeholder: 'Enter your city',
                        validation: {
                            required: 'Please enter your city',
                        }
                    },
                    {
                        name: 'state_or_province',
                        label: 'State or province',
                        type: 'text',
                        placeholder: 'Enter your state or province',
                        validation: {
                            required: 'Please enter your city',
                        }
                    },
                    {
                        name: 'zip_code',
                        label: 'Zip code',
                        type: 'text',
                        placeholder: 'Enter your zip code',
                        validation: {
                            required: 'Please enter your zip code',
                        }
                    },
                    {
                        name: 'country',
                        label: 'Country',
                        type: 'text',
                        placeholder: 'Enter your country',
                        validation: {
                            required: 'Please enter your country',
                        }
                    },
                    {
                        name: 'phone_number',
                        label: 'Phone number',
                        type: 'text',
                        placeholder: 'Enter your phone number',
                        validation: {
                            required: 'Please enter your phone number',
                        }
                    },
                ]}
            />
        </>
    )
}
