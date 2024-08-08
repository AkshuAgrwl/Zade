import type { AppInfoUserInput, SuperTokensConfig } from 'supertokens-auth-react/lib/build/types';

import { useRouter } from 'next/navigation';
import Session from 'supertokens-auth-react/recipe/session';
import EmailPassword from 'supertokens-auth-react/recipe/emailpassword';

const routerInfo: { router? : ReturnType<typeof useRouter>; pathname? : string; } = {};

export function setRouter(router: ReturnType<typeof useRouter>, pathname: string) {
  routerInfo.router = router;
  routerInfo.pathname = pathname;
}

const appInfo: AppInfoUserInput = {
  // @ts-ignore
  appName         : process.env.NEXT_PUBLIC_APP_NAME,
  // @ts-ignore
  apiDomain       : process.env.NEXT_PUBLIC_API_URI,
  apiBasePath     : process.env.NEXT_PUBLIC_API_AUTH_BASE_PATH,
  // @ts-ignore
  websiteDomain   : process.env.NEXT_PUBLIC_SITE_URL,
  websiteBasePath : '/'
};

export function frontendConfig(): SuperTokensConfig {
  return {
    appInfo,
    recipeList: [
      Session.init(),
      EmailPassword.init()
    ],
    windowHandler: original => ({
      ...original,
      location: {
        ...original.location,
        getPathName : () => routerInfo.pathname!,
        assign      : url => routerInfo.router!.push(url.toString()),
        setHref     : url => routerInfo.router!.push(url.toString()),
      }
    })
  };
}
