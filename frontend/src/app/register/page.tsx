import Link from 'next/link';
import { Button, Input } from '@/components/ui';

export default function Register() {
  return (
    <div className="w-screen h-screen flex justify-center items-center bg-cover">
      <div className="bg-[rgba(0,0,0,0.80)] grid justify-center items-center p-16 rounded">
        <p className="text-6xl font-extrabold tracking-tighter text-tertiary">
          Be an awesome
        </p>{' '}
        <p className="text-9xl font-extrabold tracking-tighter mb-7 text-secondary shadow-inner">
          LISTNER
        </p>

        <Input label="Name" type="text" placeholder="Enter an username" />
        <Input label="Email" type="email" placeholder="Enter your email" />
        <Input label="Create Password" type="password" placeholder="Create your password" />
        <Input label="Confirm Password" type="password" placeholder="Confirm your password" />
        <p className="inline mb-5 font-semibold text-senary">
          Have one already?{' '}
          <Link className="text-tertiary hover:text-quinary" href="/login">Login</Link>{' '}
          instead
        </p>
        <Button>Let{"'"}s Go!</Button>
      </div>
    </div>
  );
}
