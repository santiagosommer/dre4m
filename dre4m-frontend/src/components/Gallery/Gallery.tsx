import { useState, useEffect } from "react";
import "./Gallery.css"

export const Gallery = ({ images }) => {
    const [selected, setSelected] = useState(images[0]?.id ?? "");
    const [fade, setFade] = useState(false);

    useEffect(() => {
        setSelected(images[0]?.id ?? "");
    }, [images]);

    const handleSelect = (id: string) => {
        if (id === selected) return;
        setFade(true);
        setTimeout(() => {
            setSelected(id);
            setFade(false);
        }, 400);
    };

    const current = images.find(img => img.id === selected);

    if (!current) return null;

    return (
        <section className="gallery">
            <div className={`gallery-main ${fade ? "fade-out" : ""}`}>
                <img
                    src={current.src}
                    alt=""
                    className="gallery-img"
                />
            </div>
            <div className="gallery-thumbs">
                {images.map((img) => (
                    <button
                        key={img.id}
                        className={`gallery-thumb-btn${selected === img.id ? " active" : ""}`}
                        onClick={() => handleSelect(img.id)}
                        tabIndex={0}
                        aria-label="Select image"
                    >
                        <img src={img.thumb} alt="" className="gallery-thumb" />
                    </button>
                ))}
            </div>
        </section>
    );
};

export default Gallery;