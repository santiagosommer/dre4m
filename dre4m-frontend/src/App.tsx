import { BrowserRouter, Routes, Route } from "react-router-dom"
import Home from "./pages/Home"
import Layout from "./components/Layout/Layout"
import Auth from "./pages/Auth"
import { ProductCreation } from "./pages/ProductCreation"
import { AddressCreation } from "./pages/AddressCreation"
import { Footer } from "./components/Footer/Footer"
import Store from "./pages/Store"
import "./App.css"
import { MyAccount } from "./pages/MyAccount/MyAccount"
import Login from "./pages/Login"
import SignUp from "./pages/SignUp"
import AuthProvider from "./context/AuthContext"
import ProtectedRoute from "./components/ProtectedRoute"

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="store" element={<Store />} />
            <Route path="auth" element={<Auth />}>
              <Route path="login" element={<Login />} />
              <Route path="signup" element={<SignUp />} />
            </Route>
            <Route path="product-creation" element={<ProductCreation />} />
            <Route path="address-creation" element={<AddressCreation />} />
            <Route path="my-account" element={
              <ProtectedRoute>
                <MyAccount />
              </ProtectedRoute>
            } />
          </Route>
        </Routes>
        <Footer />
      </BrowserRouter>
    </AuthProvider>
  )
}

export default App
