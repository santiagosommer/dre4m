import { FormComponent } from './FormComponent/FormComponent'

interface ProductData {
    name: String
    description: String
    price: number
    stock: number
    product_img: String
}

const onSubmit = async (data: ProductData) => {
    try {
        const response = await fetch("https://localhost:8000/products/", {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: data.name,
                description: data.description,
                price: data.price,
                stock: data.stock,
                product_img: data.product_img
            }),
        })
        const json = await response.json()
        console.log(json)
    }
    catch (error) {
        console.error(error)
    }
}

export const ProductCreationForm = () => {
    return (
        <>
            <h1>Add product</h1>
            <FormComponent<ProductData>
                onSubmit={onSubmit}
                fields={[
                    {
                        name: 'name',
                        label: 'Product name',
                        type: 'text',
                        placeholder: 'Enter new products name',
                        validation: {
                            required: 'Product name required'
                        }
                    },
                    {
                        name: 'description',
                        label: 'Product description',
                        type: 'text',
                        placeholder: 'Enter your products description',
                        validation: {
                            required: 'Description is required'
                        }
                    },
                    {
                        name: 'price',
                        label: 'Products price',
                        type: 'text',
                        placeholder: 'Enter your products price',
                        validation: {
                            required: 'Price is required'
                        }
                    },
                    {
                        name: 'stock',
                        label: 'Stock amount',
                        type: 'text',
                        placeholder: 'Enter stock amount',
                        validation: {
                            required: 'Stock amount is required'
                        }
                    },
                    {
                        name: 'product_img',
                        label: 'Image',
                        type: 'file',
                        placeholder: 'Enter your products description',
                        validation: {
                            required: 'An image is required'
                        }
                    }
                ]}
            />
        </>
    )
}
