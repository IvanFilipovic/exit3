<template>
    <section :class="showSeeAll ? 'w-full bg-project_white py-10' : 'w-full bg-project_white py-10'">
        <div class="relative content max-w-7xl flex flex-col space-y-8">
            <h1 v-if="showSeeAll"  class="text-base text-project_black">/ How we do it</h1>

            <!-- Loop through case studies -->
            <div data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500" v-for="(caseStudy, index) in caseStudies" :key="index"
                class="relative w-full bg-pure_white flex flex-row rounded-xl overflow-hidden z-20">
                <div class="absolute left-0 top-0 h-1/2 w-5 bg-project_black"></div>
                <div class="absolute left-0 bottom-0 h-1/2 w-5 bg-primary"></div>

                <div class="p-10 ml-10 md:w-3/5">
                    <h2 class="text-[1rem] font-bold text-primary mb-2">{{ caseStudy.category }}</h2>
                    <h1 class="text-[1.63rem] md:text-[2rem] font-bold text-project_black">{{ caseStudy.title }}</h1>
                    <p class="text-project_dark_gray mt-4 text-[1rem]">
                        {{ caseStudy.description }}
                    </p>
                    <NuxtLink :to="caseStudy.link" class="group relative w-max flex flex-row items-center py-2 mt-4">
                        <Icon class="arrow ml-2 w-6 h-6 text-primary" name="meteor-icons:arrow-up-right" />
                        <span
                            class="button-text px-auto py-auto text-[1.25rem] font-base transition-transform duration-300">
                            {{ $t('read_more_button') }}
                        </span>
                    </NuxtLink>
                </div>

                <div class="relative w-2/5 mx-auto my-auto hidden md:block">
                    <img :src="`/image/bigger/${caseStudy.image}`" loading="lazy" :alt="caseStudy.alt" class="max-w-[70%] h-auto mx-auto my-auto" />
                </div>
            </div>

            <!-- Show "See all Case Studies" button only if showSeeAll is true -->
            <NuxtLink v-if="showSeeAll" :to="localePath('/use-case')"
                class="z-20 group-case bg-project_gray text-project_black py-3 px-14 mx-auto my-auto rounded-[6.25rem] hover:bg-pure_white flex flex-row items-center transition-all duration-300 w-fit">
                <span class="block text-[1rem] font-medium uppercase w-full">{{  $t('see_all_use_cases_button') }}</span>
                <Icon class="ml-2 w-9 h-9 transition-transform duration-300 group-case-hover:rotate-90"
                    name="entypo:dots-two-horizontal" />
            </NuxtLink>
        </div>
    </section>
</template>

<script setup>
const localePath = useLocalePath()
defineProps({
    caseStudies: {
        type: Array,
        required: true
    },
    showSeeAll: {
        type: Boolean,
        default: false
    }
})
</script>

<style scoped>
/* Default bottom border */
.group {
    transition: color 0.4s ease-in-out;
    text-decoration: none;
}

.group-case:hover .ml-2 {
    transform: rotate(90deg);
}

.group::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: 5px;
    width: 100%;
    height: 1px;
    background-color: #000;
    /* Default border color */
    transform: translateX(0);
    transition: transform 0.4s ease-in-out, background-color 0.4s ease-in-out;
}

/* Hover effect: border color change and movement */
.group:hover {
    color: #0A21C0;
    /* New border color on hover */
}

.group:hover::after {
    background-color: #0A21C0;
    transform: translateX(16px);
    /* Moves only the border */
}

/* Arrow icon transition */
.arrow {
    transform: translateX(-8px);
    transition: transform 0.4s ease-in-out;
}

/* Button text transition */
.button-text {
    transform: translateX(0);
    transition: transform 0.4s ease-in-out;
}

/* Hover effects for arrow and text */
.group:hover .arrow {
    transform: translateX(4px);
}

.group:hover .button-text {
    transform: translateX(16px);
}
</style>