<template>
    <div class="relative">
        
        <div class="bg-project_white py-16 h-screen my-auto">
            <Hero />
        </div>
        <div class="relative">
            <Numbers />
            <Services />
            <CaseStudy :caseStudies="caseStudies" :showSeeAll="true" />
            <CallToAction />
            <svg viewBox="0 0 10 3167" fill="none" xmlns="http://www.w3.org/2000/svg" class="linija hidden md:block">
                <path
                    d="M774 119C597.973 -79.1738 177.652 25.8267 115.5 283.5C81.6565 423.811 221.181 495.897 213 640C205.056 779.924 97.1448 835.067 83 974.5C63.7607 1164.15 221.999 1254.59 213 1445C203.559 1644.75 24.0932 1720.53 23 1920.5C22.224 2062.44 112.739 2130.08 115.5 2272C118.481 2425.27 -18.2744 2505.86 23 2653.5C99.0196 2925.43 601.856 2862.6 734.5 2782"
                    stroke="#0A21C0" stroke-linecap="round" stroke-linejoin="round" stroke-width="20" />
            </svg>
        </div>
    </div>
</template>
<script setup>
import { onMounted } from 'vue'
const { t } = useI18n()
definePageMeta({
  prerender: true
})
const caseStudies = [
    {
        title: t('social_media_automation_title'),
        category: t('social_media_automation_category'),
        description: t('social_media_automation_description'),
        link: t('social_media_automation_link'),
        image: "market-automation.svg",
        alt: "Social media automation"
    },
    {
        title: t('ecommerce_automation_title'),
        category: t('ecommerce_automation_category'),
        description: t('ecommerce_automation_description'),
        link: t('ecommerce_automation_link'),
        image: "ai-campaings.svg",
        alt: "AI Campaigns"
    }
    ,
    {
        title: t('use_case_lead_management_title'),
        category: t('lead_management_automation_category'),
        description: t('lead_management_automation_description'),
        link: t('lead_management_automation_link'),
        image: "search2.svg",
        alt: "AI Campaigns"
    }
]

onMounted(() => {
    const svg = document.querySelector('svg.linija')
    if (!svg) return // Avoid errors if SVG doesn't exist

    const path = svg.querySelector('path')
    if (!path) return // Avoid errors if path doesn't exist

    const scroll = () => {
        const distance = window.scrollY
        const totalDistance = document.body.clientHeight - window.innerHeight
        const percentage = distance / totalDistance
        const pathLength = path.getTotalLength()
        path.style.strokeDasharray = `${pathLength}`
        path.style.strokeDashoffset = `${pathLength * (1 - percentage)}`
    }

    scroll()
    window.addEventListener('scroll', scroll)
})
</script>
<style>
svg.linija {
    position: absolute;
    width: 100vh;
    height: 400vh;
    top: 0;
    right: 0;
    z-index: 1;
}

svg.linija path {
    stroke-dasharray: 2000;
    stroke-dashoffset: 2000;
    animation: dash 5s linear forwards;
}
</style>
