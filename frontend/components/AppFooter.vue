<template>
    <section class="flex flex-col bg-pure_white py-6">
        <div class="flex flex-col lg:flex-row justify-evenly pt-8">
            <div class="flex flex-col lg:w-[40%] xl:w-[30%] px-4">
                <div class="flex flex-row justify-between lg:justify-between">
                    <div class="flex flex-col gap-y-1 justify-start items-start">
                        <p class="group relative w-max flex flex-row items-center px-4 py-2 hover:text-primary">
                            <!-- Arrow: initially hidden and shifted left -->
                            <Icon class="arrow transition-all duration-300 ml-2 w-6 h-6"
                                name="meteor-icons:arrow-up-right" />
                            <!-- Button text -->
                            <span
                                class="button-text px-auto py-auto text-[1.25rem] font-light transition-transform duration-300">
                                Linkedin
                            </span>
                        </p>
                        <p class="group relative w-max flex flex-row items-center px-4 py-2 hover:text-primary">
                            <!-- Arrow: initially hidden and shifted left -->
                            <Icon class="arrow transition-all duration-300 ml-2 w-6 h-6"
                                name="meteor-icons:arrow-up-right" />
                            <!-- Button text -->
                            <span
                                class="button-text px-auto py-auto text-[1.25rem] font-light transition-transform duration-300">
                                Facebook
                            </span>
                        </p>
                        <p class="group relative w-max flex flex-row items-center px-4 py-2 hover:text-primary">
                            <!-- Arrow: initially hidden and shifted left -->
                            <Icon class="arrow transition-all duration-300 ml-2 w-6 h-6"
                                name="meteor-icons:arrow-up-right" />
                            <!-- Button text -->
                            <span
                                class="button-text px-auto py-auto text-[1.25rem] font-light transition-transform duration-300">
                                X
                            </span>
                        </p>
                        <p class="group relative w-max flex flex-row items-center px-4 py-2 hover:text-primary">
                            <!-- Arrow: initially hidden and shifted left -->
                            <Icon class="arrow transition-all duration-300 ml-2 w-6 h-6"
                                name="meteor-icons:arrow-up-right" />
                            <!-- Button text -->
                            <span
                                class="button-text px-auto py-auto text-[1.25rem] font-light transition-transform duration-300">
                                Instagram
                            </span>
                        </p>
                    </div>
                    <div class="flex flex-col gap-y-1 justify-start items-start">
                        <NuxtLink :to="localePath('/')" exact-active-class="active-link"
                            class="inline-flex items-center px-4 py-2 hover:text-primary font-light">
                            <span class="text-[1.25rem] my-auto">{{ $t('home_page') }}</span>
                            <Icon name="entypo:dot-single"
                                class="ml-2 transition-all duration-300 my-auto w-6 h-6 opacity-0 group-hover:opacity-100"
                                :class="{ 'opacity-100 text-primary': route.path === '/' || route.path === '/hr' }" />
                        </NuxtLink>

                        <!-- Case Study -->
                        <NuxtLink :to="localePath('/use-case')" exact-active-class="active-link"
                            class="inline-flex items-center px-4 py-2 hover:text-primary font-light">
                            <span class="text-[1.25rem] my-auto">{{ $t('use_case_page') }}</span>
                            <Icon name="entypo:dot-single"
                                class="ml-2 transition-all duration-300 my-auto w-6 h-6 opacity-0 group-hover:opacity-100"
                                :class="{ 'opacity-100 text-primary': route.path.startsWith('/use-case') || route.path.startsWith('/hr/use-case') }" />
                        </NuxtLink>

                        <!-- Usluge -->
                        <NuxtLink :to="localePath('/services')" exact-active-class="active-link"
                            class="inline-flex items-center px-4 py-2 hover:text-primary font-light">
                            <span class="text-[1.25rem] my-auto">{{ $t('services_page') }}</span>
                            <Icon name="entypo:dot-single"
                                class="ml-2 transition-all duration-300 my-auto w-6 h-6 opacity-0 group-hover:opacity-100"
                                :class="{ 'opacity-100 text-primary': route.path.startsWith('/services') || route.path.startsWith('/hr/services') }" />
                        </NuxtLink>

                        <!-- Kontakt (e.g., Blog route) -->
                        <NuxtLink :to="localePath('/contact')" exact-active-class="active-link"
                            class="inline-flex items-center px-4 py-2 hover:text-primary font-light">
                            <span class="text-[1.25rem] my-auto">{{ $t('contact_page') }}</span>
                            <Icon name="entypo:dot-single"
                                class="ml-2 transition-all duration-300 my-auto w-6 h-6 opacity-0 group-hover:opacity-100"
                                :class="{ 'opacity-100 text-primary': route.path.startsWith('/contact') || route.path.startsWith('/hr/contact') }" />
                        </NuxtLink>
                    </div>
                </div>
                <div
                    class="flex flex-row gap-x-4 py-4 justify-center md:justify-center lg:justify-start items-center lg:items-start px-8 pt-8 text-[0.95rem]">
                    <p class="group relative w-max flex flex-row items-center lg:px-4 py-2">
                        <span class="px-auto py-auto font-light transition-transform duration-300">
                            {{ $t('contact_page') }}
                        </span>
                    </p>
                    <p class="group relative w-max flex flex-row items-center lg:px-4 py-2 hover:text-primary">
                        <span class="px-auto py-auto font-light transition-transform duration-300">
                            mail@mail.com
                        </span>
                    </p>
                </div>
            </div>


            <div class="flex flex-col gap-y-1 justify-center lg:justify-start items-center lg:items-start px-4">
                <p class="relative flex flex-row items-center py-2 lg:w-[70%]">
                    <span class="px-auto py-auto text-[2rem] md:text-[2.5rem] font-normal">
                        {{ $t('subscribe_newsletter_button') }}
                    </span>
                </p>
                <div class="relative w-full max-w-lg z-50">
                    <input
                        type="email"
                        v-model="email"
                        :placeholder="$t('subscribe_newsletter_placeholder')"
                        class="w-full px-4 py-4 pr-16 rounded-[0.85rem] bg-light_primary text-Project_black placeholder-project_dark_gray focus:outline-none"
                    />
                    <div class="absolute inset-y-0 right-0 flex items-center pr-4">
                        <button
                        type="button"
                        @click="submitNewsletter"
                        aria-label="Subscribe to newsletter"
                        class="flex items-center justify-center w-10 h-10 text-project_black hover:text-black transition"
                        >
                        <Icon name="lucide:arrow-right" class="w-6 h-6" />
                        </button>
                    </div>
                </div>
                <transition name="fade">
                    <div
                        v-if="showSuccessPopup"
                        class="fixed inset-0 flex items-center justify-center z-50"
                    >
                        <div
                        class="bg-success text-project_black text-lg px-6 py-8 rounded-xl shadow-xl animate-bounce-in"
                        >
                        🎉 Subscribed Successfully!
                        </div>
                    </div>
                </transition>
            </div>
        </div>
        <div class="flex flex-col lg:flex-row justify-evenly pt-8">
            <p class="font-normal text-base px-6 mx-auto text-center">All Rights Reserved &copy; Exit Three {{ currentYear }}. Built by exit3 team with 💙</p>
        </div>
    </section>
</template>
<script setup>
import { useRoute } from 'vue-router'
const localePath = useLocalePath()
const route = useRoute()
const currentYear = new Date().getFullYear();

const email = ref('')
const error = ref(null)
const showSuccessPopup = ref(false)

const submitNewsletter = async () => {
  if (!email.value) return
  error.value = null
  showSuccessPopup.value = false

  const config = useRuntimeConfig()

  const { data, error: fetchError } = await useFetch('/backend/api/newsletter/', {
    method: 'POST',
    body: { email: email.value, is_subscribed: true },
    baseURL: config.public.baseUrl, 
    headers: {
      Authorization: `Basic ${config.public.basicApiKey}`
    }
  })

  if (fetchError.value) {
    error.value = 'Something went wrong. Please try again.'
    return
  }

  // ✅ Show success popup
  showSuccessPopup.value = true
  email.value = ''
  setTimeout(() => {
    showSuccessPopup.value = false
  }, 2000)
}


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
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
@keyframes bounce-in {
  0% {
    transform: scale(0.9);
    opacity: 0;
  }
  60% {
    transform: scale(1.05);
    opacity: 1;
  }
  100% {
    transform: scale(1);
  }
}

.animate-bounce-in {
  animation: bounce-in 0.5s ease;
}

</style>