import { defineConfig, searchForWorkspaceRoot } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    fs: {
      allow: [
        searchForWorkspaceRoot(process.cwd()),
        '/home/kuba/Desktop/Studia/sem7/paint_projekt_moje/paint-project-frontendd/node_modules/allow',
      ],
    },
  },
})
