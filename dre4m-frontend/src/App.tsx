import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Layout from './components/Layout/Layout'
import Auth from './pages/Auth'
import { ProductCreation } from './pages/ProductCreation'
import { AddressCreation } from './pages/AddressCreation'
import { Footer } from './components/Footer/Footer'
import Store from './pages/Store'
import "./App.css"

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path='/store' element={<Store />}></Route>
            <Route path="/auth" element={<Auth />} />
            <Route path="/product-creation" element={<ProductCreation />} />
            <Route path="/login" element={<Auth />} />
            <Route path="/address-creation" element={<AddressCreation />} />
            <Route path="/footer" element={<Footer />} />
          </Route>
        </Routes>
        <Footer />
      </BrowserRouter>
    </>
  )
}

export default App
