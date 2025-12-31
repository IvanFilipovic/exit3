export default defineNuxtPlugin(() => {
  const route = useRoute()
  const { public: { baseUrl } } = useRuntimeConfig()

  // inicijalno
  useHead({
    link: [{ rel: 'canonical', href: `${baseUrl}${route.fullPath}` }]
  })
  useSeoMeta({ ogUrl: `${baseUrl}${route.fullPath}` })

  // na svaku promjenu rute
  watch(() => route.fullPath, (path) => {
    const url = `${baseUrl}${path}`
    useHead({ link: [{ rel: 'canonical', href: url }] })
    useSeoMeta({ ogUrl: url })
  }, { immediate: false })
})
