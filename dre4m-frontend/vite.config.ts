import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    https: {
      key: './certs/localhost-key.pem',
      cert: './certs/localhost.pem',
    },
    host: 'localhost',
    port: 5173,
  },
})
