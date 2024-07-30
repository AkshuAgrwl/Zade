import React from 'react';
import { cn } from '@/utils';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?          : string;
  labelClassName? : string;
}

export default function Input({ label, labelClassName, ...inputProps }: InputProps) {
  return (
    <div className="flex flex-col">
      {label ? <label className={cn('font-bold text-secondary ', labelClassName)}>{label}</label> : null}
      <input
        {...inputProps}
        className={cn(
          'p-2.5 pl-0 mb-7 text-sm font-semibold text-secondary border-b-2 outline-none border-secondary bg-[transparent] transition ease-in-out delay-150 hover:border-tertiary active:border-tertiary ',
          inputProps.className
        )}
      />
    </div>
  );
}
