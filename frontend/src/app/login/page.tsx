import Link from 'next/link';
import { Button, Input } from '@/components/ui';

export default function Login() {
  return (
    <div className="w-screen h-screen flex justify-center items-center bg-cover">
      <div className="grid justify-center items-center p-16 rounded bg-[rgba(0,0,0,0.80)]">
        <p className="text-6xl font-extrabold tracking-tighter text-tertiary">
          Welcome Back
        </p>
        {' '}
        <p className="text-9xl font-extrabold tracking-tighter mb-7 text-secondary shadow-inner">
          LISTNER
        </p>
        <Input label="Email" type="text" placeholder="Enter your email" />
        <Input label="Password" type="password" placeholder="Enter your password" />
        <p className="inline mb-5 font-semibold text-senary">
          Wait what ? Not registered yet ? Come on just{' '}
          <Link href="/register" className="text-tertiary hover:text-quinary">Register</Link>
        </p>
        <Button type="submit">Login</Button>
        <p className="inline my-5 font-semibold text-senary">
          Forgot password?{' '}
          <Link href="/login/reset-password" className="text-tertiary hover:text-quinary">Click Here</Link></p>
      </div>
    </div>
  );
}
