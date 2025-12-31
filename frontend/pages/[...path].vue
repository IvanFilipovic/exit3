<template>
    <div class="min-h-screen w-full flex flex-col-reverse md:flex-row justify-center items-center bg-inherit py-36">
        <div class="w-[50%] flex flex-col  py-12">
            <h1 class="text-[2rem] font-bold text-project_black md:text-end text-center">404</h1>
            <p class="text-[1.5rem] font-base md:text-end text-center">Page Not Found</p>
            <div class="py-8 flex justify-end">
                <NuxtLink to="/" class="button-primary flex flex-row w-fit justify-start items-center mx-auto md:mx-0">
                    <p class="group relative w-max flex flex-row items-start">
                        <!-- Arrow: initially hidden and shifted left -->
                        <Icon class="arrow transition-all duration-300 ml-2 w-8 h-8"
                            name="meteor-icons:arrow-right-long" />
                        <!-- Button text -->
                        <span
                            class="button-text px-auto py-auto text-[1rem] font-medium uppercase transition-transform duration-300 my-auto">
                            Početna
                        </span>
                        <!-- Icon: will fade out on hover -->
                        <Icon class="icon mx-auto my-auto ml-2 pl-2 transition-opacity duration-300 w-8 h-8"
                            name="entypo:dot-single" />
                    </p>
                </NuxtLink>
            </div>
        </div>
        <div class="w-[50%]">
            <img src="/image/bigger/404.svg" alt="404" class="w-[500px] mx-auto" />
        </div>
    </div>
</template>
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