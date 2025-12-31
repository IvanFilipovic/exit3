<template>
    <section id="service" class="container py-16">
        <div class="content flex-col rounded-xl space-y-8">
            <h1 class="text-base">{{ $t('services_title') }}</h1>
            <div class="relative text-project_black flex flex-col justify-between space-y-8 md:space-y-16">
                <div
                    class="relative bg-pure_white w-full rounded-xl py-4 flex md:flex-row-reverse flex-col-reverse z-10 overflow-hidden">
                    <div class="absolute left-0 top-0 h-1/2 w-5 bg-project_black"></div>
                    <div class="absolute left-0 bottom-0 h-1/2 w-5 bg-primary"></div>
                    <div class="flex flex-col text-start md:text-start md:w-[60%] my-auto justify-center px-4 ml-10 pb-2">
                        <h1 data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                            class="text-[1.63rem] md:text-[2rem] py-4 text-start">{{ $t('automation_service_title') }}
                        </h1>
                        <p data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                            class="py-1 text-[1rem] pr-4 text-start">
                            {{ $t('automation_service_description') }}
                        </p>
                        <div data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                            class="py-6 flex flex-col md:flex-row justify-center md:justify-start text-startmd:mx-0 md:space-x-2">
                            <h1 class="bg-primary text-pure_white px-4 rounded-[6.25rem] text-sm p-2 my-2 w-fit">{{ $t('automation_service_field_one') }}
                            </h1>
                            <h1 class="bg-primary text-pure_white px-4 rounded-[6.25rem] text-sm p-2 my-2 w-fit">{{ $t('automation_service_field_two') }}</h1>
                        </div>
                        <NuxtLink :to="localePath('/services/automation')" aria-label="Read more about automation services"
                            class="group relative w-max flex flex-row items-center py-2">
                            <!-- Arrow: initially hidden and shifted left -->
                            <Icon class="arrow ml-2 w-6 h-6 text-primary" name="meteor-icons:arrow-up-right" />
                            <!-- Button text -->
                            <span
                                class="button-text px-auto py-auto text-[1.25rem] font-base transition-transform duration-300">
                                {{ $t('read_more_button')}}
                            </span>
                        </NuxtLink>

                    </div>
                    <div class="flex justify-center w-[60%] md:w-[40%] mx-auto z-20">
                        <img src="~/public/image/ai-process.svg" alt="Automatizacija procesa" loading="lazy"
                            class="max-w-[100%] mx-auto my-auto h-auto" />
                    </div>
                </div>
                <div
                    class="relative bg-pure_white w-full rounded-xl py-4 flex md:flex-row-reverse flex-col-reverse z-10 overflow-hidden">
                    <div class="absolute left-0 top-0 h-1/2 w-5 bg-project_black"></div>
                    <div class="absolute left-0 bottom-0 h-1/2 w-5 bg-primary"></div>
                    <div class="flex flex-col text-start md:text-start md:w-[60%] my-auto justify-center px-4 ml-10 pb-2">
                        <h1 data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                            class="text-[1.63rem] md:text-[2rem] py-4 md:px-0 text-start">{{ $t('web_development_service_title') }}
                        </h1>

                        <p data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                            class="py-1 text-[1rem] pr-4 text-start">
                            {{ $t('web_development_service_description') }}
                        </p>
                        <div data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                            class="py-6 flex flex-col md:flex-row justify-center md:justify-start text-start md:mx-0 md:space-x-2">
                            <h1 class="bg-primary text-pure_white px-4 rounded-[6.25rem] text-sm p-2 my-2 w-fit">{{ $t('web_development_service_field_one') }}
                            </h1>
                            <h1 class="bg-primary text-pure_white px-4 rounded-[6.25rem] text-sm p-2 my-2 w-fit">{{ $t('web_development_service_field_two') }}</h1>
                        </div>
                        <NuxtLink :to="localePath('/services/development')" aria-label="Read more about development services"
                            class="group relative w-max flex flex-row items-center py-2">
                            <!-- Arrow: initially hidden and shifted left -->
                            <Icon class="arrow ml-2 w-6 h-6 text-primary" name="meteor-icons:arrow-up-right" />
                            <!-- Button text -->
                            <span
                                class="button-text px-auto py-auto text-[1.25rem] font-base transition-transform duration-300">
                                {{ $t('read_more_button') }}
                            </span>
                        </NuxtLink>

                    </div>
                    <div class="flex justify-center w-[60%] md:w-[40%] mx-auto z-20">
                        <img src="~/public/image/ai-dev.svg" alt="Automatizacija procesa" loading="lazy"
                            class="max-w-[100%] mx-auto my-auto h-auto" />
                    </div>
                </div>
                <div
                    class="relative bg-pure_white w-full rounded-xl py-4 flex md:flex-row-reverse flex-col-reverse z-10 overflow-hidden">
                    <div class="absolute left-0 top-0 h-1/2 w-5 bg-project_black"></div>
                    <div class="absolute left-0 bottom-0 h-1/2 w-5 bg-primary"></div>
                    <div class="flex flex-col text-start md:text-start md:w-[60%] my-auto justify-center px-4 ml-10 pb-2">
                        <h1 data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                            class="text-[1.63rem] md:text-[2rem] py-4 md:px-0">{{ $t('automated_testing_service_title') }}</h1>
                        <p data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500" class="py-1 text-[1rem] pr-4 text-start">
                            {{ $t('automated_testing_service_description') }}</p>
                            <div data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                            class="py-6 flex flex-col md:flex-row justify-center md:justify-start text-start md:mx-0 md:space-x-2">
                            <h1 class="bg-primary text-pure_white px-4 rounded-[6.25rem] text-sm p-2 my-2 w-fit">{{ $t('automated_testing_service_field_one') }}
                            </h1>
                            <h1 class="bg-primary text-pure_white px-4 rounded-[6.25rem] text-sm p-2 my-2 w-fit">{{ $t('automated_testing_service_field_two') }}</h1>
                        </div>
                        <NuxtLink :to="localePath('/services/testing')" aria-label="Read more about testing services"
                            class="group relative w-max flex flex-row items-center py-2">
                            <!-- Arrow: initially hidden and shifted left -->
                            <Icon class="arrow ml-2 w-6 h-6 text-primary" name="meteor-icons:arrow-up-right" />
                            <!-- Button text -->
                            <span
                                class="button-text px-auto py-auto text-[1.25rem] font-base transition-transform duration-300">
                                {{ $t('read_more_button') }}
                            </span>
                        </NuxtLink>

                    </div>
                    <div class="flex justify-center w-[60%] md:w-[40%] mx-auto z-20">
                        <img src="~/public/image/ai-test.svg" alt="Automatizacija procesa" loading="lazy"
                            class="max-w-[100%] mx-auto my-auto h-auto" />
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script setup>
const localePath = useLocalePath()

</script>
<style scoped>
img {
  opacity: 0;
  transition: opacity 0.5s ease;
}
img[loading="lazy"]:not([src=""]) {
  opacity: 1;
}
/* Default bottom border */
.group {
    transition: color 0.4s ease-in-out;
    text-decoration: none;
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