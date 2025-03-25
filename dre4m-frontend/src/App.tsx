import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Layout from './components/Layout'
import Auth from './pages/Auth'
import { ProductCreation } from './pages/ProductCreation'

function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="/auth" element={<Auth />} />
            <Route path="/product-creation" element={<ProductCreation />} />
          </Route>
        </Routes>
      </BrowserRouter>

    </>
  )
}

export default App
