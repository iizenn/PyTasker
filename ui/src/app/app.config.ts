export interface AppConfig {
  production: boolean;
  apiBase: string;
}

export const appConfig: AppConfig = {
  production: false,
  apiBase: 'http://localhost:5000',
};
