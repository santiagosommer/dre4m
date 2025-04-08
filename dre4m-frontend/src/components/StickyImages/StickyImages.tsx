import { useEffect, useState } from 'react'

import './StickyImages.css'
import dre4m from '../../assets/dre4m-back-shirt.png'
import koi from '../../assets/koi-back-shirt.png'
import goya from '../../assets/goya-back-shirt.png'


interface Product {
    name: string;
    price: string;
    img: string;
}


export const StickyImages = () => {
    const [products, setProducts] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    const fetchProducts = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/product');
            if (!response.ok) {
                throw new Error('Error al recuperar los datos');
            }
            const data = await response.json();
            setProducts(data);
            setLoading(false);
        }
        catch (err) {
            setError(err.message);
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchProducts();
    }, []);

    if (loading) {
        return <p>Cargando productos...</p>;
    }

    if (error) {
        return <p>Error: {error}</p>;
    }

    return (
        <>
            <div className="sticky-container">
                <div className='image-wrapper1'>
                    <img className='sticky-image1' src={goya} />
                </div>
                <div className='section-wrapper'>
                    <p className='section-name'>LAST RELEASE</p>
                    <div className='image-section-wrapper'>
                        {products.map((product) => (
                            < div key={product.id} className="product-card" >
                                {/* <img className="flex-image" src={product.image} alt={product.name} /> */}
                                <img className="flex-image" src={goya} alt={product.name} />
                                <h3>{product.name}</h3>
                                <p>${product.price}</p>
                            </div>
                        ))}
                    </div>
                </div>
                <div className='image-wrapper2'>
                    <img className='sticky-image2' src={dre4m} />
                </div>
                <div className='image-wrapper3'>
                    <img className='sticky-image3' src={koi} />
                </div>
            </div >
        </>
    )
}

export default StickyImages
