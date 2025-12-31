<template>
    <div class="py-32">
        <CaseStudy :caseStudies="caseStudies" :showSeeAll="false" />
    </div>
</template>
<script setup>
const { t } = useI18n()

const caseStudies = [
    {
        title: t('social_media_automation_title'),
        category: t('social_media_automation_category'),
        description: t('social_media_automation_description'),
        link: t('social_media_automation_link'),
        image: "ai-social.svg",
        alt: t('social_media_automation_title')
    },
    {
        title: t('ecommerce_automation_title'),
        category: t('ecommerce_automation_category'),
        description: t('ecommerce_automation_description'),
        link: t('ecommerce_automation_link'),
        image: "profit-automation.svg",
        alt: t('ecommerce_automation_title')
    },
    {
        title: t('lead_management_automation_title'),
        category: t('lead_management_automation_category'),
        description: t('lead_management_automation_description'),
        link: t('lead_management_automation_link'),
        image: "search2.svg",
        alt: t('lead_management_automation_title')
    }
]
</script>
