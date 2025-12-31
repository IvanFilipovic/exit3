<template>
    <section class="container my-16">
        <div class="content flex flex-col justify-center">
            <h1 class="text-base text-project_black text-start py-8">{{ $t('cta_intro') }}</h1>
            <h2 data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                class="text-center text-[2rem] md:text-[2.5rem] text-project_black">{{ $t('cta_headline') }}</h2>
            <h3 data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500"
                class="text-center text-[1.5rem] md:text-[2rem] text-project_black">{{ $t('cta_subheadline') }}</h3>
            <div data-aos="fade-up" data-aos-easing="linear" data-aos-duration="500" class="py-8 mx-auto z-10">
                <NuxtLink :to="localePath('/contact')" aria-label="Go to contact page" class="button-primary flex flex-row w-fit justify-start items-center mt-4">
                    <p class="group relative w-max flex flex-row items-start">
                        <!-- Arrow: initially hidden and shifted left -->
                        <Icon class="arrow transition-all duration-300 ml-2 w-8 h-8"
                            name="meteor-icons:arrow-right-long" />
                        <!-- Button text -->
                        <span
                            class="button-text px-auto py-auto text-[1rem] font-medium uppercase transition-transform duration-300 my-auto">
                            {{ $t('cta_button') }}
                        </span>
                        <!-- Icon: will fade out on hover -->
                        <Icon class="icon mx-auto my-auto ml-2 pl-2 transition-opacity duration-300 w-8 h-8"
                            name="entypo:dot-single" />
                    </p>
                </NuxtLink>
            </div>

        </div>
    </section>
</template>
<script setup>
const localePath = useLocalePath()
</script>
<style scoped>
.arrow {
    opacity: 0;
    transform: translateX(-8px);
    /* Adjust offset as needed */
    transition: transform 0.3s ease, opacity 0.3s ease;
}

/* Icon: initially visible */
.icon {
    opacity: 1;
    transition: opacity 0.3s ease;
}

/* Button text: initially in place */
.button-text {
    transform: translateX(0);
    transition: transform 0.3s ease;
}

/* Hover state: reveal arrow, move text right, and fade out the icon */
.group:hover .arrow {
    opacity: 1;
    transform: translateX(0);
}

.group:hover .button-text {
    transform: translateX(16px);
    /* Shifts text to the right; adjust value as needed */
}

.group:hover .icon {
    opacity: 0;
}
</style>
