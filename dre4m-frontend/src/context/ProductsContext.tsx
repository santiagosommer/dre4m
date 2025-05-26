import { createContext, useContext, useState, useEffect } from "react";


interface ProductContextType {
    products: any[];
}

const ProductContext = createContext<ProductContextType | undefined>(undefined)

const ProductsProvider = ({ children }) => {
    const [products, setProducts] = useState([])

    const fetchProducts = async () => {
        try {
            const response = await fetch("https://localhost:8000/products/list", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
                credentials: "include"
            })
            if (response.ok) {
                const data = await response.json()
                setProducts(data)
                console.log(data)
            }
        }
        catch (err) {

        }
    };

    useEffect(() => {
        fetchProducts()
    }, [])

    return (
        <ProductContext.Provider value={{ products }}>
            {children}
        </ProductContext.Provider>)
}

export const useProducts = () => {
    const context = useContext(ProductContext);
    if (!context) {
        throw new Error("Outside AuthProvider");
    }
    return context;
};

export default ProductsProvider