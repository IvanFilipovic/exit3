<script setup>
const { scrollToAnchor } = useAnchorScroll({
  toTop: {
    scrollOptions: {
      behavior: 'smooth', // Slows down scroll speed
      offsetTop: 30,
    },
  },
})
</script>
<template>
    <section class="flex flex-col min-h-screen my-auto justify-center items-center relative">
        <div class="content flex">
            <div class="text-project_black xl:w-[80%]">
                <h1
                    class="text-[2.3rem] md:text-[4.35rem] font-normal text-project_black md:leading-[4.4rem] py-2">
                    {{ $t('services_page_headline_prefix') }}
                    <span class="text-primary relative inline-block stroke-current">{{ $t('services_page_headline_highlight') }}
                        <svg class="absolute -bottom-0.5 w-full max-h-1.5" viewBox="0 0 55 5"
                            xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
                            <path d="M0.652466 4.00002C15.8925 2.66668 48.0351 0.400018 54.6853 2.00002"
                                stroke-width="2"></path>
                        </svg>
                    </span>
                </h1>
                <h1 class="text-[1.2rem] mx-auto py-12 text-end w-[70%]">{{ $t('services_page_subheadline') }}</h1>
            </div>
            <div class="hidden md:block">
                <img src="/image/bigger/ai-work.svg" loading="lazy" alt="service.alt" class="max-w-[150%] h-autoobject-cover mx-auto my-auto" />
            </div>
        </div>
        <NuxtLink
        href="#service"
        @click.prevent="scrollToAnchor('service', 2000)"
        aria-label="Scroll to service section"
        class="absolute bottom-[110px] flex items-center justify-center w-16 h-16 rounded-full bg-project_black dark:bg-dark_primary"
        >
            <Icon class="w-8 h-8 text-pure_white dark:text-primary" name="entypo:chevron-thin-down" />
        </NuxtLink>
    </section>
</template>