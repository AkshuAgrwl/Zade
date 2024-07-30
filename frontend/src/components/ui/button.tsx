import React from 'react';
import { cn } from '@/utils';

export default function Button({ ...buttonProps }: React.ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      {...buttonProps}
      className={cn(
        'bg-tertiary text-secondary mr-5 rounded w-fit p-4 cursor-pointer font-bold text-l transition ease-in-out delay-250 hover:bg-quinary ',
        buttonProps.className
      )}
    />
  );
}
