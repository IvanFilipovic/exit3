<script setup lang="ts">
const config = useRuntimeConfig()

useHead({
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Organization',
        name: 'Exit Three',
        url: config.public.baseUrl || 'https://www.exit3.online',
        logo: `${config.public.baseUrl || 'https://www.exit3.online'}/image/logos/logo.svg`,
        description: 'Automation and custom software solutions that help businesses streamline operations, boost productivity, and stay ahead of the competition.',
        sameAs: [
          'https://www.linkedin.com/company/exit-three',
          'https://www.facebook.com/exitthree',
          'https://twitter.com/exitthree'
        ],
        contactPoint: {
          '@type': 'ContactPoint',
          contactType: 'Sales',
          availableLanguage: ['English', 'Croatian', 'en', 'hr']
        },
        address: {
          '@type': 'PostalAddress',
          addressCountry: 'HR'
        },
        foundingDate: '2023',
        serviceType: [
          'Business Process Automation',
          'AI Marketing Automation',
          'Web Development',
          'Mobile App Development',
          'Automated Testing',
          'Social Media Automation'
        ]
      })
    },
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'WebSite',
        name: 'Exit Three',
        url: config.public.baseUrl || 'https://www.exit3.online',
        description: 'Transform your business with automation and custom software solutions.',
        potentialAction: {
          '@type': 'SearchAction',
          target: {
            '@type': 'EntryPoint',
            urlTemplate: `${config.public.baseUrl || 'https://www.exit3.online'}/search?q={search_term_string}`
          },
          'query-input': 'required name=search_term_string'
        }
      })
    },
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'ProfessionalService',
        name: 'Exit Three',
        image: `${config.public.baseUrl || 'https://www.exit3.online'}/image/logos/logo.svg`,
        '@id': config.public.baseUrl || 'https://www.exit3.online',
        url: config.public.baseUrl || 'https://www.exit3.online',
        telephone: '',
        priceRange: '$$',
        address: {
          '@type': 'PostalAddress',
          addressCountry: 'HR'
        },
        openingHoursSpecification: {
          '@type': 'OpeningHoursSpecification',
          dayOfWeek: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday'
          ],
          opens: '09:00',
          closes: '17:00'
        },
        sameAs: [
          'https://www.linkedin.com/company/exit-three',
          'https://www.facebook.com/exitthree',
          'https://twitter.com/exitthree'
        ]
      })
    }
  ]
})
</script>

<template>
  <!-- This component only injects structured data, no visual output -->
</template>
