import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    colors: {
      primary   : '#000000',
      secondary : '#ffffff',
      tertiary  : '#7b2cbf',
      quinary   : '#5a189a',
      senary    : '#8d99ae',
      accent    : '#0E0E0E'
    },
    extend: {},
  },
  plugins: [],
};
export default config;
