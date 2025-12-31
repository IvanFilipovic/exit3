<template>
    <section class="container pt-32">
        <div class="content flex flex-col justify-center items-center">
            <h1 class="text-center mb-8 flex flex-col items-center">
                <span class="text-[2rem] md:text-[2.5rem] font-bold px-6">{{ $t('use_case_lead_management_title')}}</span>
            </h1>
            <nav aria-label="breadcrumb" class="w-full p-4 mx-auto">
                <ol class="flex h-8 space-x-2 text-project_dark_gray mx-auto justify-center">
                    <li class="flex items-center">
                        <NuxtLink :to="localePath('/')" title="Back to homepage"
                            class="flex items-center hover:underline">{{ $t('home_page')}}</NuxtLink>
                    </li>
                    <li class="flex items-center space-x-1">
                        <span class="dark:text-gray-600">/</span>
                        <NuxtLink :to="localePath('/use-case')"
                            class="flex items-center px-1 capitalize hover:underline">{{ $t('use_case_page')}}</NuxtLink>
                    </li>
                </ol>
            </nav>
            <div class="">
                <div class="text-project_black my-auto pl-1 md:p-6 py-8 pb-18">
                    
                    <div class="flex flex-col-reverse md:flex-row justify-between">
                        <div class="flex flex-col md:w-2/3 my-auto">
                            <p class="text-[1.63rem] py-2 font-semibold">
                            {{ $t('use_case_lead_management_section1_title')}}
                            </p>
                            <p class="text-[1.13rem] py-2">
                            {{ $t('use_case_lead_management_section1_text')}}
                            </p>
                            <p class="text-[1.13rem] py-2">
                            {{ $t('use_case_lead_management_section1_text2')}}
                            </p>
                        </div>
                        <div class:="flex w-full">
                            <img :src="`/image/bigger/${caseStudy.image_challenge}`" :alt="caseStudy.alt"
                            class="max-w-[50%] md:max-w-[100%] h-auto md:float-left mx-auto py-6 md:py-0" />
                        </div>
                        
                    </div>
                </div>
                <div class="text-project_black my-auto md:bg-pure_white rounded-xl pl-1 md:p-6 flex flex-col space-y-3 max-w-full">
                    <div class="py-8 md:pr-12">
                        <div class="flex flex-col md:flex-row justify-between items-center">
                            <div class="flex flex-col text-project_black my-auto md:w-2/3 space-y-3">
                                <p class="text-[1.63rem] py-2 font-semibold">
                                {{ $t('use_case_lead_management_section2_title')}}
                                </p>
                                <p class="mt-4 text-[1.13rem] pb-2">
                                    {{ $t('use_case_lead_management_section2_text')}}
                                </p>
                                <p class="text-[1.63rem] py-2 font-semibold">
                                    {{ $t('tools')}}
                                </p>
                                <div class="flex flex-row item py-2 space-x-3 w-full">
                                    <p v-for="(job, index) in caseStudy.jobs" :key="index" class="flex flex-row">
                                        <img v-if="!job.isIcon" :src="`/image/logos/${job.image}`" :alt="job.alt" class="w-8 h-8" />
                                        <span class="my-auto pl-4">{{ job.name }}</span>
                                    </p>
                                </div>
                            </div>
                            <div>
                                <img :src="`/image/bigger/${caseStudy.image_solution}`" :alt="caseStudy.alt"
                                class="max-w-[0%] md:max-w-[80%] h-auto mx-auto md:float-right my-auto" />
                            </div>
                        </div>
                        <div class="flex flex-col text-project_black my-auto">
                            <p class="mt-4 text-[1.13rem] pb-5">
                                <span class="font-semibold">
                                    {{ $t('use_case_lead_management_first_bullet_title')}}
                                </span>
                            </p>
                            <ul class="space-y-5">
                                <li
                                class="flex items-start"
                                >
                                    <Icon
                                        name="entypo:dot-single"
                                        class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                    />
                                    <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words md:my-auto">
                                        {{ $t('use_case_lead_management_first_bullet1')}}
                                    </p>
                                </li>
                                <li
                                class="flex items-start"
                                >
                                    <Icon
                                        name="entypo:dot-single"
                                        class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                    />
                                    <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words md:my-auto">
                                        {{ $t('use_case_lead_management_first_bullet2')}}
                                    </p>
                                </li>
                            </ul>
                        </div>
                        <div class="flex flex-col text-project_black my-auto">
                            <p class="mt-4 text-[1.13rem] pb-5">
                                <span class="font-semibold">
                                    {{ $t('use_case_lead_management_second_bullet_title')}}
                                </span>
                            </p>
                            <ul class="space-y-5">
                                <li
                                class="flex items-start"
                                >
                                    <Icon
                                        name="entypo:dot-single"
                                        class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                    />
                                    <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words md:my-auto">
                                        {{ $t('use_case_lead_management_second_bullet1')}}
                                    </p>
                                </li>
                                <li
                                class="flex items-start"
                                >
                                    <Icon
                                        name="entypo:dot-single"
                                        class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                    />
                                    <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words md:my-auto">
                                        {{ $t('use_case_lead_management_second_bullet2')}}
                                    </p>
                                </li>
                            </ul>
                        </div>
                        <div class="flex flex-col text-project_black my-auto">
                            <p class="mt-4 text-[1.13rem] pb-5">
                                <span class="font-semibold">
                                    {{ $t('use_case_lead_management_third_bullet_title')}}
                                </span>
                            </p>
                            <ul class="space-y-5">
                                <li
                                class="flex items-start"
                                >
                                    <Icon
                                        name="entypo:dot-single"
                                        class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                    />
                                    <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words md:my-auto">
                                        {{ $t('use_case_lead_management_third_bullet1')}}
                                    </p>
                                </li>
                                <li
                                class="flex items-start"
                                >
                                    <Icon
                                        name="entypo:dot-single"
                                        class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                    />
                                    <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words md:my-auto">
                                        {{ $t('use_case_lead_management_third_bullet2')}}
                                    </p>
                                </li>
                            </ul>
                        </div>
                        <div class="flex flex-col text-project_black my-auto">
                            <p class="mt-4 text-[1.13rem] pb-5">
                                <span class="font-semibold">
                                    {{ $t('use_case_lead_management_fourth_bullet_title')}}
                                </span>
                            </p>
                            <ul class="space-y-5">
                                <li
                                class="flex items-start"
                                >
                                    <Icon
                                        name="entypo:dot-single"
                                        class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                    />
                                    <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words md:my-auto">
                                        {{ $t('use_case_lead_management_fourth_bullet1')}}
                                    </p>
                                </li>
                                <li
                                class="flex items-start"
                                >
                                    <Icon
                                        name="entypo:dot-single"
                                        class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                    />
                                    <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words md:my-auto">
                                        {{ $t('use_case_lead_management_fourth_bullet2')}}
                                    </p>
                                </li>
                            </ul>
                        </div>
                        <p class="text-[1.13rem] py-6 pt-6">
                            {{ $t('use_case_lead_management_section2_text2')}}
                        </p>
                    </div>
                    
                </div>
                <div class="text-project_black my-auto ml-1 md:p-6 flex flex-col py-12 w-full">
                    <p class="text-[1.63rem] py-2 font-semibold">{{ $t('use_case_lead_management_section3_title')}}</p>
                    <p class="text-[1.13rem] py-4">{{ $t('use_case_lead_management_section3_text')}}</p>
                    <div class="flex flex-col text-project_black my-auto">
                        <p class="mt-4 text-[1.13rem] pb-5">
                            <span class="font-semibold">
                                {{ $t('use_case_lead_management_section3_bullet_title')}}
                            </span>
                        </p>
                        <ul class="space-y-5">
                            <li
                            class="flex items-start"
                            >
                                <Icon
                                    name="entypo:dot-single"
                                    class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                />
                                <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words my-auto">
                                    {{ $t('use_case_lead_management_section3_first_bullet1')}}
                                </p>
                            </li>
                            <li
                            class="flex items-start"
                            >
                                <Icon
                                    name="entypo:dot-single"
                                    class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                />
                                <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words my-auto">
                                    {{ $t('use_case_lead_management_section3_first_bullet2')}}
                                </p>
                            </li>
                        </ul>
                    </div>
                    <div class="flex flex-col text-project_black my-auto">
                        <p class="mt-4 text-[1.13rem] pb-5">
                            <span class="font-semibold">
                                {{ $t('use_case_lead_management_section3_second_bullet_title')}}
                            </span>
                        </p>
                        <ul class="space-y-5">
                            <li
                            class="flex items-start"
                            >
                                <Icon
                                    name="entypo:dot-single"
                                    class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                />
                                <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words my-auto">
                                    {{ $t('use_case_lead_management_section3_second_bullet1')}}
                                </p>
                            </li>
                        </ul>
                    </div>
                    <div class="flex flex-col text-project_black my-auto">
                        <p class="mt-4 text-[1.13rem] pb-5">
                            <span class="font-semibold">
                                {{ $t('use_case_lead_management_section3_third_bullet_title')}}
                            </span>
                        </p>
                        <ul class="space-y-5">
                            <li
                            class="flex items-start"
                            >
                                <Icon
                                    name="entypo:dot-single"
                                    class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                />
                                <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words my-auto">
                                    {{ $t('use_case_lead_management_section3_third_bullet1')}}
                                </p>
                            </li>
                        </ul>
                    </div>
                    <div class="flex flex-col text-project_black my-auto">
                        <p class="mt-4 text-[1.13rem] pb-5">
                            <span class="font-semibold">
                                {{ $t('use_case_lead_management_section3_fourth_bullet_title')}}
                            </span>
                        </p>
                        <ul class="space-y-5">
                            <li
                            class="flex items-start"
                            >
                                <Icon
                                    name="entypo:dot-single"
                                    class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                />
                                <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words my-auto">
                                    {{ $t('use_case_lead_management_section3_fourth_bullet1')}}
                                </p>
                            </li>
                        </ul>
                    </div>
                    <div class="flex flex-col text-project_black my-auto">
                        <p class="mt-4 text-[1.13rem] pb-5">
                            <span class="font-semibold">
                                {{ $t('use_case_lead_management_section3_fifth_bullet_title')}}
                            </span>
                        </p>
                        <ul class="space-y-5">
                            <li
                            class="flex items-start"
                            >
                                <Icon
                                    name="entypo:dot-single"
                                    class="flex-wrap mt-1 w-9 h-9 md:ml-2"
                                />
                                <p class="flex-1 md:ml-4 text-[1.13rem] leading-snug break-words my-auto">
                                    {{ $t('use_case_lead_management_section3_fifth_bullet1')}}
                                </p>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="text-project_black my-auto ml-1 md:p-6 flex flex-col py-2 w-full">
                    <p class="text-[1.63rem] py-2 font-semibold">{{ $t('use_case_lead_management_section4_title')}}</p>

                    <p class="mt-4 text-[1.13rem] pb-5">
                        {{ $t('use_case_lead_management_section4_text')}}
                    </p>
                    <p class="mt-4 text-[1.13rem] pb-5">
                        {{ $t('use_case_lead_management_section4_text2')}}
                    </p>
                </div>
            </div>
            <CallToAction />
        </div>
    </section>
</template>
<script setup>
const localePath = useLocalePath()
const { t } = useI18n()
    const caseStudy = {
        image_solution: "profit-automation.svg",
        image_challenge: "manual_work.svg",
        jobs: [
            { name: "", isIcon: false, image: "openai.svg", alts: "OpenAI" },
            { name: "", isIcon: false, image: "make.svg", alts: "make.com" },
            { name: "", isIcon: false, image: "n8n.svg", alts: "n8n" },
            { name: "", isIcon: false, image: "mailchimp.jpeg", alts: "Mailchimp" },

        ]

    }
</script>