import { LoginForm } from "../components/Forms/LoginForm"
import { CreateUserForm } from "../components/Forms/CreateUserForm"

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