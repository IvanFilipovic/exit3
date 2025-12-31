<template>
    <section class="hero-container flex flex-row min-h-screen my-auto justify-center items-center w-screen">
        <div class="content flex">
            <div class="text-project_black xl:w-[70%]">
                <h1 class="text-[2rem] md:text-[4.35rem] font-normal text-project_black md:leading-[4.80rem] py-2">
                    <span class="text-primary relative inline-block stroke-current">{{ $t('hero_colored') }}
                        <svg class="absolute -bottom-0.5 w-full max-h-1.5" viewBox="0 0 55 5"
                            xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
                            <path d="M0.652466 4.00002C15.8925 2.66668 48.0351 0.400018 54.6853 2.00002"
                                stroke-width="2"></path>
        
                        </svg>
                    </span>
                    {{ $t('hero_colored_black') }}
                </h1>
                <p class="text-[1rem] md:text-[1.2rem] font-normal text-project_black py-2 w-[85%]">
                    {{ $t('hero_subtitle') }}
                </p>
                <transition name="slide-up-down" mode="out-in">
                    <h1 :key="currentIndex" class="text-[1.1rem] font-normal py-2 my-4">
                        {{ words[currentIndex] }}
                    </h1>
                </transition>
                <NuxtLink to="/contact" class="button-primary flex flex-row w-fit justify-start items-center mt-4">
                    <p class="group relative w-max flex flex-row items-start">
                        <!-- Arrow: initially hidden and shifted left -->
                        <Icon class="arrow transition-all duration-300 ml-2 w-8 h-8"
                            name="meteor-icons:arrow-right-long" />
                        <!-- Button text -->
                        <span
                            class="button-text px-auto py-auto text-[1rem] font-medium uppercase transition-transform duration-300 my-auto">
                            {{ $t('hero_button') }}
                        </span>
                        <!-- Icon: will fade out on hover -->
                        <Icon class="icon mx-auto my-auto ml-2 pl-2 transition-opacity duration-300 w-8 h-8"
                            name="entypo:dot-single" />
                    </p>
                </NuxtLink>
            </div>
            <div class="ball w-[30%] hidden xl:flex mx-auto my-auto py-10"></div>
        </div>
    </section>
</template>



<script setup lang="ts">
import { ref, onMounted } from "vue";
const currentIndex = ref(0)
let intervalId: number | null = null
const { t } = useI18n()

const words = [
  t('word1'),
  t('word2'),
  t('word3'),
  t('word4'),
]
onMounted(() => {
    intervalId = setInterval(() => {
        currentIndex.value = (currentIndex.value + 1) % words.length;
    }, 2000)
})
</script>

<style scoped>
.hero-container {
  contain: layout style paint;
}

/* Transition for rotating text */
.slide-up-down-enter-active,
.slide-up-down-leave-active {
    transition: transform 0.3s ease, opacity 0.3s ease;
}

.slide-up-down-enter-from {
    transform: translateY(30%);
    opacity: 0;
}

.slide-up-down-enter-to {
    transform: translateY(0);
    opacity: 1;
}

.slide-up-down-leave-from {
    transform: translateY(0);
    opacity: 1;
}

.slide-up-down-leave-to {
    transform: translateY(-30%);
    opacity: 0;
}

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

.ball {
    width: 350px;
    height: 350px;
    border-radius: 50%;
    box-shadow:
        inset 0 0 50px #f4f5f8,
        inset 20px 0 60px #e5e7fd,
        inset -20px 0 60px #0A21C0,

        inset 20px 0 300px #e5e7fd,
        inset -20px 0 300px #0A21C0,

        0 0 5px #f4f5f8,
        -10px 0 60px #e5e7fd,
        10px 0 60px #0A21C0;
    animation: load 1.7s linear infinite;
}

@keyframes load {
    0% {
        transform: rotate(0deg);
        filter: hue-rotate(0deg);
    }

    1.66%,
    3.33% {
        transform: rotate(12deg);
    }

    4.99%,
    6.66% {
        transform: rotate(24deg);
    }

    8.32%,
    9.99% {
        transform: rotate(36deg);
    }

    11.65%,
    13.32% {
        transform: rotate(48deg);
    }

    14.98%,
    16.65% {
        transform: rotate(60deg);
    }

    18.31%,
    19.98% {
        transform: rotate(72deg);
    }

    21.65%,
    23.31% {
        transform: rotate(84deg);
    }

    24.98%,
    26.65% {
        transform: rotate(96deg);
    }

    28.31%,
    29.98% {
        transform: rotate(108deg);
    }

    31.65%,
    33.33% {
        transform: rotate(120deg);
    }

    34.98%,
    36.65% {
        transform: rotate(132deg);
    }

    38.33%,
    39.98% {
        transform: rotate(144deg);
    }

    41.65%,
    43.33% {
        transform: rotate(156deg);
    }

    44.98%,
    46.65% {
        transform: rotate(168deg);
    }

    48.33%,
    50% {
        transform: rotate(180deg);
    }

    51.65%,
    53.33% {
        transform: rotate(192deg);
    }

    54.99%,
    56.65% {
        transform: rotate(204deg);
    }

    58.33%,
    59.99% {
        transform: rotate(216deg);
    }

    61.65%,
    63.33% {
        transform: rotate(228deg);
    }

    64.99%,
    66.66% {
        transform: rotate(240deg);
    }

    68.33%,
    69.99% {
        transform: rotate(252deg);
    }

    71.66%,
    73.33% {
        transform: rotate(264deg);
    }

    74.99%,
    76.66% {
        transform: rotate(276deg);
    }

    78.33%,
    79.99% {
        transform: rotate(288deg);
    }

    81.66%,
    83.33% {
        transform: rotate(300deg);
    }

    84.99%,
    86.66% {
        transform: rotate(312deg);
    }

    88.33%,
    89.99% {
        transform: rotate(324deg);
    }

    91.66%,
    93.33% {
        transform: rotate(336deg);
    }

    94.99%,
    96.66% {
        transform: rotate(348deg);
    }

    98.33%,
    100% {
        transform: rotate(360deg);
    }
}
</style>