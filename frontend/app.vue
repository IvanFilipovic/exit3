<template>
  <div class="bg-project_white">
      <!-- Structured Data for SEO -->
      <StructuredData />

      <div class="mx-0 md:mx-auto backdrop-blur-sm md:bg-project_white/20 md:backdrop-blur-lg z-50 fixed top-0 w-full">
          <AppHeader />
      </div>
      <div>
        <NuxtPage />
        <AppFooter />
      </div>
      <CookieControl :locale="locale" />
  </div>
</template>
<script setup lang="ts">
import Cookies from 'js-cookie'
import { useGtm } from '@gtm-support/vue-gtm'

const gtm = useGtm()
const { locale } = useI18n()
const {
  cookiesEnabledIds
} = useCookieControl()

const acceptCookies = () => {
  Cookies.set('userConsent', 'granted', { expires: 365 })
  gtm.enable(true)
}

const declineCookies = () => {
  Cookies.set('userConsent', 'denied', { expires: 365 })
  gtm.enable(false)
}
const removeAnalyticsCookies = () => {
  const gaCookies = ['_ga', '_gid', '_gat', '_gcl_au']
  gaCookies.forEach(name => {
    Cookies.remove(name)

    Cookies.remove(name, { domain: window.location.hostname.replace(/^www\./, '') })

    Cookies.remove(name, { path: '/' })
  })
}
onMounted(() => {
  Cookies.set('userConsent', 'denied', { expires: 365 })
})
watch(
  () => cookiesEnabledIds.value,
  (current, previous) => {
    const hasNow = current.includes('analytics')
    const hadBefore = previous?.includes?.('analytics')

    if (!hadBefore && hasNow) {
      acceptCookies()
    } else if (hadBefore && !hasNow) {
      declineCookies()
      removeAnalyticsCookies()
    }
  },
  { immediate: false }
)

</script>
<style>
body {
  background-color: #e4e6ef;
  font-family: 'Noto Sans', sans-serif;
  font-display: swap;
}

.page-enter-active,
.page-leave-active {
  transition: all 0.9s;
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1.2rem);
}
</style>