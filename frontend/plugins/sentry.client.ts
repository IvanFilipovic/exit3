import * as Sentry from '@sentry/vue'

export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig()

  // Only initialize Sentry if DSN is provided
  if (config.public.sentryDsn) {
    Sentry.init({
      app: nuxtApp.vueApp,
      dsn: config.public.sentryDsn,
      environment: process.env.NODE_ENV || 'development',
      
      // Performance monitoring
      tracesSampleRate: 0.2, // 20% of transactions for performance monitoring
      
      // Session replay for debugging
      replaysSessionSampleRate: 0.1, // 10% of sessions
      replaysOnErrorSampleRate: 1.0, // 100% of sessions with errors
      
      integrations: [
        Sentry.browserTracingIntegration(),
        Sentry.replayIntegration({
          maskAllText: true,
          blockAllMedia: true,
        }),
      ],

      // Filter out sensitive data
      beforeSend(event, hint) {
        // Don't send events in development
        if (process.env.NODE_ENV === 'development') {
          return null
        }
        return event
      },
    })
  } else {
    console.warn('Sentry DSN not configured. Error monitoring is disabled.')
  }
})
