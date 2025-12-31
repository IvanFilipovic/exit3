<template>
    <section class="container my-auto bg-transparent md:py-16">
        <div class="content flex flex-col py-20">
            <div class="flex flex-col">
                <div class="relative w-full mx-auto my-auto flex flex-col-reverse md:flex-row pt-20">
                    <div class="py-6 md:w-3/5 text-center md:text-start my-auto flex flex-col">
                        <h1 class="text-[2.5rem] py-6 text-center md:text-start">{{ service.title }}</h1>
                        <h1 class="text-[1.2rem] py-6 text-center md:text-start my-auto">{{
                        service.small_description }}</h1>
                        <p class="text-[1.1rem] py-6 text-center md:text-start my-auto">{{
                        service.descriptionOne }}</p>
                        <p class="text-[1.1rem] py-6 text-center md:text-start my-auto">{{
                        service.descriptionTwo }}</p>
                    </div>
                    <img :src="`/image/bigger/${service.image}`" :alt="service.alt" loading="lazy"  class="hidden md:block  mx-auto my-auto w-1/3"  />
                </div>
                <div class="relative w-full mx-auto my-auto">
                    <div class="flex flex-col md:flex-row w-full items-start justify-start text-[1rem]">
                        <!-- First Column -->
                        <div class="flex flex-col py-2 space-y-4 w-full">
                            <p v-for="(job, index) in firstColumn" :key="index" class="flex flex-row">
                                <img v-if="!job.isIcon" :src="`/image/logos/${job.image}`" :alt="job.alt" loading="lazy"
                                    class="w-8 h-8" />

                                <Icon v-if="job.isIcon" :name="job.icon" class="w-8 h-8" />
                                <span class="my-auto pl-4">{{ job.name }}</span>
                            </p>
                        </div>
                        <!-- Second Column -->
                        <div class="flex flex-col py-2 space-y-4 w-full">
                            <p v-for="(job, index) in secondColumn" :key="index" class="flex flex-row">
                                <img v-if="!job.isIcon" :src="`/image/logos/${job.image}`" :alt="job.alt" loading="lazy"
                                    class="w-8 h-8" />

                                <Icon v-if="job.isIcon" :name="job.icon" class="w-8 h-8" />
                                <span class="my-auto pl-4">{{ job.name }}</span>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="benefit" class="content flex flex-col max-w-7xl">
            <h1 data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500" class="text-base z-20">{{
                benefit.title }}</h1>
            <h1 data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                class="text-[1.1rem] leading-relaxed py-4 z-20">{{ benefit.subtitle }}</h1>
            <div class="flex flex-col md:flex-row justify-start py-16 gap-x-8 gap-y-8">
                <div v-for="(item, index) in benefit.items" :key="index"
                    class="flex flex-row mx-auto py-4 w-full bg-pure_white rounded-xl px-4 z-20">
                    <div class="flex flex-col w-[70%]">
                        <span :class="[
                            'animate-[counter_3s_ease-out_forwards]',
                            'tabular-nums',
                            { [`[counter-set:_num_var(${item.counter})]`]: item.counter }
                        ]" class="before:content-[counter(num)] text-[36px] font-semibold text-project_black">
                            <span class="sr-only">{{ item.value }}</span> {{ item.suffix }}
                        </span>
                        <p class="text-[1rem] py-1 text-project_black">{{ item.description }}</p>
                    </div>
                    <div class="rounded-full bg-project_white p-4 mx-auto my-auto">
                        <MdiIcon :icon="item.icon" class="text-primary h-10 w-10" />
                    </div>
                </div>
            </div>
        </div>
        <div class="content flex flex-col max-w-7xl mt-20">
            <p class="text-[1.3rem] py-1 text-project_black text-center font-semibold">{{ $t('services_page_development_phases')}}</p>
        </div>
    </section>
</template>
<script setup>
const props = defineProps({
    service: {
        type: Object,
        required: true
    },
    benefit: {
        type: Object,
        required: true
    }
})
const midpoint = computed(() => Math.ceil(props.service.jobs.length / 2));

const firstColumn = computed(() => props.service.jobs.slice(0, midpoint.value));
const secondColumn = computed(() => props.service.jobs.slice(midpoint.value));
</script>
