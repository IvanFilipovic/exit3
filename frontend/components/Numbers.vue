<template>
    <section class="bg-inherti w-full z-10 text-project_black">
        <div class="content flex flex-col max-w-7xl">
            <h1 data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500" class="text-base z-20">{{ $t('benefits_title') }}</h1>
            <h1 data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                class="text-[1.2rem] md:text-[2.3rem] leading-relaxed py-4 z-20">{{ $t('benefits_subtitle') }}</h1>
            <div class="flex flex-col md:flex-row justify-start py-16 gap-x-8 gap-y-8">
                <div class="flex flex-row mx-auto py-4 w-full bg-pure_white rounded-xl px-4">
                    <div class="flex flex-col w-[70%]">
                        <span
                            class="animate-[counter_3s_ease-out_forwards] tabular-nums [counter-set:_num_var(--num-hours)] before:content-[counter(num)] text-[36px] font-semibold text-project_black">
                            <span class="sr-only">40</span> % </span>
                        <p class="text-[1rem] py-1 text-project_black">{{ $t('benefits_one') }}</p>
                    </div>
                    <div class="rounded-full bg-project_white p-4 mx-auto my-auto">
                        <MdiIcon icon="mdiCashMultiple" class="text-primary h-10 w-10" />
                    </div>
                </div>
                <div class="flex flex-row mx-auto py-4 w-full bg-pure_white rounded-xl px-4 z-20">
                    <div class="flex flex-col w-[70%]">
                        <span
                            class="animate-[counter_3s_ease-out_forwards] tabular-nums [counter-set:_num_var(--num-profit)] before:content-[counter(num)] text-[36px] font-semibold text-project_black">
                            <span class="sr-only">2-3</span> x </span>
                        <p class="text-[1rem] py-1 text-project_black">{{ $t('benefits_two') }}</p>
                    </div>
                    <div class="rounded-full bg-project_white p-4 mx-auto my-auto">
                        <MdiIcon icon="mdiSpeedometer" class="text-primary h-10 w-10" />
                    </div>
                </div>
                <div class="flex flex-row mx-auto py-4 w-full bg-pure_white rounded-xl px-4 z-20">
                    <div class="flex flex-col w-[70%]">
                        <span
                            class="animate-[counter_3s_ease-out_forwards] tabular-nums [counter-set:_num_var(--num-leads)] before:content-[counter(num)] text-[36px] font-semibold text-project_black">
                            <span class="sr-only">99</span> % </span>
                        <p class="text-[1rem] py-1 text-project_black">{{ $t('benefits_three') }}</p>
                    </div>
                    <div class="rounded-full bg-project_white p-4 mx-auto my-auto">
                        <MdiIcon icon="mdiShieldCheck" class="text-primary h-10 w-10" />
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<style scoped></style>