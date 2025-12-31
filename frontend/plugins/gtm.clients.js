import { createGtm } from '@gtm-support/vue-gtm'
import Cookies from 'js-cookie'

export default defineNuxtPlugin((nuxtApp) => {
  const runtimeConfig = useRuntimeConfig().public
  const consentGiven = Cookies.get('userConsent') === 'granted'
  const router = useRouter()

  nuxtApp.vueApp.use(
    createGtm({
      id: runtimeConfig.gtm_id,
      defer: false,
      compatibility: false,
      enabled: runtimeConfig.gtm_enabled && consentGiven,
      debug: runtimeConfig.gtm_debug,
      loadScript: true,
      vueRouter: router,
      trackOnNextTick: false,
    }),
  )
})
