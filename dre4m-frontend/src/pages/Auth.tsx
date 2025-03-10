import { LoginForm } from "../components/LoginForm"
import { CreateUserForm } from "../components/CreateUserForm"

export const Auth = () => {
  return (
    <>
      <h1>Login or Create User</h1>
      <LoginForm />
      <CreateUserForm />
    </>
  )
}

export default Auth