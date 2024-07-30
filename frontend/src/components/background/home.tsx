import Image from 'next/image';
import bgImage from './bg-image.png';

export default function HomeBackground() {
  return (
    <Image
      alt="Background"
      src={bgImage}
      placeholder="blur"
      quality={100}
      fill
      sizes="100vw"
      style={{
        objectFit : 'cover',
        zIndex    : -100
      }}
    />
  );
}
