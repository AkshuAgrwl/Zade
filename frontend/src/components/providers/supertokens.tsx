'use client';

import React from 'react';
import { usePathname, useRouter } from 'next/navigation';
import SuperTokensReact from 'supertokens-auth-react';
import { SuperTokensWrapper } from 'supertokens-auth-react';
import { frontendConfig, setRouter } from '@/config/supertokens';


if (typeof window !== 'undefined') {
  SuperTokensReact.init(frontendConfig());
}

export const SuperTokensProvider: React.FC<React.PropsWithChildren<{}>> = ({
  children,
}) => {
  setRouter(useRouter(), usePathname() || window.location.pathname);

  return <SuperTokensWrapper>{children}</SuperTokensWrapper>;
};
