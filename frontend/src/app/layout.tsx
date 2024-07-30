import './globals.css';

import type { Metadata } from 'next';

import { Poppins } from 'next/font/google';

import { HomeBackground } from '@/components/background';

const inter = Poppins({
  weight  : [ '100', '200', '300', '400', '500', '600', '700', '800', '900' ],
  subsets : [ 'latin' ]
});

export const metadata: Metadata = {
  title       : 'Zade',
  description : 'The Music Streaming Platform',
};

export default function RootLayout(
  { children }: Readonly<{
    children: React.ReactNode;
  }>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <HomeBackground />
        {children}
      </body>
    </html>
  );
}
