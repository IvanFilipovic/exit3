<script setup>
import { computed } from 'vue'
import { useI18n } from '#imports' // for Nuxt 3 + @nuxtjs/i18n

const { locale, locales } = useI18n()
const switchLocalePath = useSwitchLocalePath()

// Show only the locale that is NOT currently active
const availableLocales = computed(() =>
  locales.value.filter(i => i.code !== locale.value)
)
</script>

<template>
  <div class="flex items-center gap-2">
    <NuxtLink
      v-for="loc in availableLocales"
      :key="loc.code"
      :to="switchLocalePath(loc.code)"
      class="flex items-center gap-1 hover:scale-105 transition-transform"
    >
      <Icon class="ml-2 w-6 h-6 text-primary" :name="loc.icon" />
      <span class="text-sm">{{ loc.name }}</span>
    </NuxtLink>
  </div>
</template>
