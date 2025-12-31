export default defineNitroPlugin(() => {
  // Only validate in production
  if (process.env.NODE_ENV !== 'production') {
    return
  }

  const config = useRuntimeConfig()
  const errors: string[] = []

  // Required public environment variables
  if (!config.public.baseUrl) {
    errors.push('NUXT_PUBLIC_BASE_URL is required in production')
  }

  if (!config.public.gtm_id) {
    console.warn('NUXT_PUBLIC_GTAG_ID is not set - Google Tag Manager will not work')
  }

  // Required private environment variables
  if (!config.basicApiKey) {
    errors.push('BASIC_API_KEY is required for backend API authentication')
  }

  // Throw error if critical variables are missing
  if (errors.length > 0) {
    throw new Error(`Missing required environment variables:\n${errors.join('\n')}`)
  }

  console.log('✅ Environment variables validated successfully')
})
