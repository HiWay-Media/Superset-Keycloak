import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: 'Superset Keycloak',
  description: '',
  base: '/superset-keycloak/',
  themeConfig: {
    outline: [2, 3],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/HiWay-Media/Superset-Keycloak' },
    ],
    sidebar: [
      { text: 'Introduction', link: '/' },
    ],
  },
})
