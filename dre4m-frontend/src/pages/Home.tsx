import shirtImage from '../assets/example-shirt.jpg'
import './Home.css'

export const Home = () => {
  return (
    <>
      <img draggable='false' className="landing-image" src={shirtImage} alt="Example Shirt" />
    </>
  )
}

export default Home