/** @type {import('tailwindcss').Config} */
export default {
  content: [],
  theme: {
    extend: {
      colors: {
        background_color: '#e4e6ef',
        light_primary: '#e5e7fd',
        primary: '#0A21C0',
        success: '#21CA0A',
        dark_primary: '#050A44',
        pure_white: '#f4f5f8',
        project_white: '#e4e6ef',
        project_black: '#141619',
        project_gray: '#B3B4BD',
        project_dark_gray: '#2C2E3A',
        text_color: '#141619',
        lighter_primary: '#2C2E3A',
        darker_primary: '#314455'
      }
    }
  },
  plugins: [
    require('tailwindcss-animated')
  ],
}

