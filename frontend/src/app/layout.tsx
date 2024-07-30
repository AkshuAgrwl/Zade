import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });
import { HomeBackground } from '@/components/background';

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
