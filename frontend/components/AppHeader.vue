<template>
    <section class="flex flex-col bg-inherit justify-center w-full py-10 md:py-0">
        <!-- Desktop menu (visible on md and up) -->
        <div class="hidden md:flex md:flex-row md:pl-12 justify-between bg-inherit" >
            <div class="flex-none">
                <NuxtLink class="hidden md:flex md:flex-row justify-center" :to="localePath('/')">
                    <img src="~/public/image/logos/logo.svg" class="mr-2 mx-auto my-auto max-w-[150px] h-auto p-1" loading="lazy"
                        alt="Exit Three - automatizacijska agencija" />
                </NuxtLink>
            </div>
            <div class="flex flex-row gap-x-1 md:gap-x-8 md:px-20">
                <NuxtLink :to="localePath('/use-case')" exact custom v-slot="{ href, navigate, isActive }">
                    <a :href="href" @click="navigate" class="py-3 px-6 mx-auto my-auto hidden xl:flex" :class="isActive
                        ? 'opacity-100 bg-pure_white text-project_black rounded-[6.25rem]'
                        : 'hidden hover:bg-pure_white rounded-[6.25rem]'">
                        <p class="relative w-max flex flex-row items-center">
                            <span class="text-[1rem] font-medium uppercase">
                                {{ $t('use_case_page') }}
                            </span>
                            <Icon name="entypo:dot-single" class="ml-2 pl-2 transition-all duration-300 my-auto w-8 h-8"
                                :class="isActive ? 'opacity-100 bg-project_black' : 'opacity-0'" />
                        </p>
                    </a>
                </NuxtLink>
                <Menu as="div" class="relative md:inline-block text-left md:mx-auto my-auto">
                    <template v-slot="{ open }">
                        <div>
                            <div
                                class="flex md:flex-row justify-end pr-4 md:pr-0 md:gap-x-6 md:mx-auto my-auto w-full md:w-auto">
                                <button class="button-primary hidden md:flex" @click="go('/contact', close)" aria-label="Contact us">
                                    <p class="group relative w-max flex flex-row items-center">
                                        <!-- Arrow: initially hidden and shifted left -->
                                        <Icon class="arrow transition-all duration-300 ml-2 w-8 h-8"
                                            name="meteor-icons:arrow-right-long" />
                                        <!-- Button text -->
                                        <span
                                            class="button-text px-auto py-auto text-[1rem] font-medium uppercase transition-transform duration-300">
                                            {{ $t('contact_page') }}
                                        </span>
                                        <!-- Icon: will fade out on hover -->
                                        <Icon
                                            class="icon mx-auto my-auto ml-2 pl-2 transition-opacity duration-300 w-8 h-8"
                                            name="entypo:dot-single" />
                                    </p>
                                </button>
                                <!-- Menu Button with dynamic sliding text -->
                                <MenuButton
                                    :class="open ? 'bg-pure_white text-project_black py-3 px-6 md:mx-auto my-auto rounded-[6.25rem] hover:bg-pure_white group' : 'bg-project_gray text-project_black py-3 px-6 md:mx-auto my-auto rounded-[6.25rem] hover:bg-pure_white group'">
                                    <p class="flex flex-row items-center overflow-hidden">
                                        <!-- The transition name changes based on open state -->
                                        <transition :name="open ? 'slide-up' : 'slide-down'" mode="out-in">
                                            <!-- Use a key that depends on open state so the transition re-triggers -->
                                            <span :key="open"
                                                class="block py-auto text-[1rem] font-medium uppercase w-[90px]">
                                                {{ open ? $t('close_button') : 'Menu' }}
                                            </span>
                                        </transition>
                                        <Icon
                                            class="ml-2 transition-transform duration-300 group-hover:rotate-90 w-8 h-8"
                                            name="entypo:dots-two-horizontal" />
                                    </p>
                                </MenuButton>
                            </div>

                            <!-- Dropdown Menu Items with a smooth fade/scale transition -->
                            <transition enter-active-class="transition ease-out duration-200 z-50"
                                enter-from-class="transform opacity-0 scale-95"
                                enter-to-class="transform opacity-100 scale-100"
                                leave-active-class="transition ease-in duration-150"
                                leave-from-class="transform opacity-100 scale-100"
                                leave-to-class="transform opacity-0 scale-95">
                                <MenuItems
                                    class="absolute mt-4 w-full transform bg-pure_white rounded-xl z-10 py-4 px-2">
                                    <div class="py-1">
                                        <!-- Each dropdown item is a button that navigates and then closes the menu -->
                                        <!-- Početna -->
                                        <MenuItem as="div" v-slot="{ close }">
                                        <button type="button" @click="go('/', close)" aria-label="Go to home page"
                                            class="menu-link group w-full text-left py-3 md:py-4 my-2 md:px-6 px-4 flex hover:bg-light_primary rounded-[6.25rem]">
                                            <p class="w-full flex flex-row justify-between">
                                                <span
                                                    class="menu-text relative inline-block overflow-hidden text-[1.375rem] font-medium uppercase my-auto">
                                                    <span class="menu-text-top block transition-transform ease-out">
                                                        {{ $t('home_page') }}
                                                    </span>
                                                    <span
                                                        class="menu-text-bottom block absolute top-0 left-0 transition-transform ease-out">
                                                        {{ $t('home_page') }}
                                                    </span>
                                                </span>
                                                <Icon name="entypo:dot-single"
                                                    class="ml-2 pl-2 transition-all duration-300 my-auto w-10 h-10 opacity-0 group-hover:opacity-100"
                                                    :class="{ 'opacity-100 bg-project_black': route.path === '/' || route.path === '/hr' }" />
                                            </p>
                                        </button>
                                        </MenuItem>

                                        <!-- case study -->
                                        <MenuItem as="div" v-slot="{ close }">
                                        <button type="button" @click="go('/use-case', close)" aria-label="Go to use case page"
                                            class="menu-link group w-full text-left py-3 md:py-4 my-2 md:px-6 px-4 flex hover:bg-light_primary rounded-[6.25rem]">
                                            <p class="w-full flex flex-row justify-between">
                                                <span
                                                    class="menu-text relative inline-block overflow-hidden text-[1.375rem] font-medium uppercase my-auto">
                                                    <span class="menu-text-top block transition-transform ease-out">
                                                        {{ $t('use_case_page') }}
                                                    </span>
                                                    <span
                                                        class="menu-text-bottom block absolute top-0 left-0 transition-transform ease-out">
                                                        {{ $t('use_case_page') }}
                                                    </span>
                                                </span>
                                                <Icon name="entypo:dot-single"
                                                    class="ml-2 pl-2 transition-all duration-300 my-auto w-10 h-10 opacity-0 group-hover:opacity-100"
                                                    :class="{ 'opacity-100 bg-project_black': route.path.startsWith('/use-case') || route.path.startsWith('/hr/use-case') }" />
                                            </p>
                                        </button>
                                        </MenuItem>

                                        <!-- Usluge -->
                                        <MenuItem as="div" v-slot="{ close }">
                                        <button type="button" @click="go('/services', close)" aria-label="Go to services page"
                                            class="menu-link group w-full text-left py-3 md:py-4 my-2 md:px-6 px-4 flex hover:bg-light_primary rounded-[6.25rem]">
                                            <p class="w-full flex flex-row justify-between items-center">
                                                <span
                                                    class="menu-text relative inline-block overflow-hidden text-[1.375rem] font-medium uppercase my-auto">
                                                    <span class="menu-text-top block transition-transform ease-out">
                                                        {{ $t('services_page') }}
                                                    </span>
                                                    <span
                                                        class="menu-text-bottom block absolute top-0 left-0 transition-transform ease-out">
                                                        {{ $t('services_page') }}
                                                    </span>
                                                </span>
                                                <Icon name="entypo:dot-single"
                                                    class="ml-2 pl-2 transition-all duration-300 my-auto w-10 h-10 opacity-0 group-hover:opacity-100"
                                                    :class="{ 'opacity-100 bg-project_black': route.path.startsWith('/services') || route.path.startsWith('/hr/services') }" />
                                            </p>
                                        </button>
                                        </MenuItem>

                                        <!-- kontakt (linked to /blog in this example) -->
                                        <MenuItem as="div" v-slot="{ close }">
                                        <button type="button" @click="go('/contact', close)" aria-label="Go to contact page"
                                            class="menu-link group w-full text-left py-3 md:py-4 my-2 md:px-6 px-4 flex hover:bg-light_primary rounded-[6.25rem]">
                                            <p class="w-full flex flex-row justify-between">
                                                <span
                                                    class="menu-text relative inline-block overflow-hidden text-[1.375rem] font-medium uppercase my-auto">
                                                    <span class="menu-text-top block transition-transform ease-out">
                                                        {{ $t('contact_page') }}
                                                    </span>
                                                    <span
                                                        class="menu-text-bottom block absolute top-0 left-0 transition-transform ease-out">
                                                        {{ $t('contact_page') }}
                                                    </span>
                                                </span>
                                                <Icon name="entypo:dot-single"
                                                    class="ml-2 pl-2 transition-all duration-300 my-auto w-10 h-10 opacity-0 group-hover:opacity-100"
                                                    :class="{ 'opacity-100 bg-project_black': route.path === '/contact' || route.path === '/hr/contact' }" />
                                            </p>
                                        </button>
                                        </MenuItem>
                                    </div>
                                </MenuItems>
                            </transition>
                        </div>

                    </template>
                </Menu>
                <LanguageSwitcher />
            </div>
        </div>
        <div class="flex flex-row md:pl-12 justify-between bg-inherit md:hidden" >
            <div class="flex flex-row gap-x-1 md:gap-x-8 md:px-28">
                <Menu as="div" class="relative w-full md:inline-block text-left md:mx-auto my-auto">
                    <template v-slot="{ open }">
                        <div>
                            <div
                                class="flex md:flex-row justify-end px-4 md:pr-0 md:mx-auto my-auto w-full md:w-auto">
                                <!-- Menu Button with dynamic sliding text -->
                                <MenuButton
                                    :class="open ? 'bg-pure_white text-project_black py-3 px-6 md:mx-auto my-auto rounded-[6.25rem] hover:bg-pure_white group' : 'bg-project_gray text-project_black py-3 px-6 md:mx-auto my-auto rounded-[6.25rem] hover:bg-pure_white group'">
                                    <p class="flex flex-row items-center overflow-hidden">
                                        <!-- The transition name changes based on open state -->
                                        <transition :name="open ? 'slide-up' : 'slide-down'" mode="out-in">
                                            <!-- Use a key that depends on open state so the transition re-triggers -->
                                            <span :key="open"
                                                class="block py-auto text-[1rem] font-medium uppercase w-[90px]">
                                                {{ open ? $t('close_button') : 'Menu' }}
                                            </span>
                                        </transition>
                                        <Icon
                                            class="ml-2 transition-transform duration-300 group-hover:rotate-90 w-8 h-8"
                                            name="entypo:dots-two-horizontal" />
                                    </p>
                                </MenuButton>
                            </div>

                            <!-- Dropdown Menu Items with a smooth fade/scale transition -->
                            <transition enter-active-class="transition ease-out duration-200 z-50"
                                enter-from-class="transform opacity-0 scale-95"
                                enter-to-class="transform opacity-100 scale-100"
                                leave-active-class="transition ease-in duration-150"
                                leave-from-class="transform opacity-100 scale-100"
                                leave-to-class="transform opacity-0 scale-95">
                                <MenuItems
                                    class="absolute mt-4 w-screen transform bg-pure_white rounded-xl z-10 py-4 px-2">
                                    <div class="py-1">
                                        <!-- Each dropdown item is a button that navigates and then closes the menu -->
                                        <!-- Početna -->
                                        <MenuItem as="div" v-slot="{ close }">
                                        <button type="button" @click="go('/', close)" aria-label="Go to home page"
                                            class="menu-link group w-full text-left py-3 md:py-4 my-2 md:px-6 px-4 flex hover:bg-light_primary rounded-[6.25rem]">
                                            <p class="w-full flex flex-row justify-between">
                                                <span
                                                    class="menu-text relative inline-block overflow-hidden text-[1.375rem] font-medium uppercase my-auto">
                                                    <span class="menu-text-top block transition-transform ease-out">
                                                        {{ $t('home_page') }}
                                                    </span>
                                                    <span
                                                        class="menu-text-bottom block absolute top-0 left-0 transition-transform ease-out">
                                                        {{ $t('home_page') }}
                                                    </span>
                                                </span>
                                                <Icon name="entypo:dot-single"
                                                    class="ml-2 pl-2 transition-all duration-300 my-auto w-10 h-10 opacity-0 group-hover:opacity-100"
                                                    :class="{ 'opacity-100 bg-project_black': route.path === '/' || route.path === '/hr' }" />
                                            </p>
                                        </button>
                                        </MenuItem>

                                        <!-- case study -->
                                        <MenuItem as="div" v-slot="{ close }">
                                        <button type="button" @click="go('/use-case', close)" aria-label="Go to use case page"
                                            class="menu-link group w-full text-left py-3 md:py-4 my-2 md:px-6 px-4 flex hover:bg-light_primary rounded-[6.25rem]">
                                            <p class="w-full flex flex-row justify-between">
                                                <span
                                                    class="menu-text relative inline-block overflow-hidden text-[1.375rem] font-medium uppercase my-auto">
                                                    <span class="menu-text-top block transition-transform ease-out">
                                                        {{ $t('use_case_page') }}
                                                    </span>
                                                    <span
                                                        class="menu-text-bottom block absolute top-0 left-0 transition-transform ease-out">
                                                        {{ $t('use_case_page') }}
                                                    </span>
                                                </span>
                                                <Icon name="entypo:dot-single"
                                                    class="ml-2 pl-2 transition-all duration-300 my-auto w-10 h-10 opacity-0 group-hover:opacity-100"
                                                    :class="{ 'opacity-100 bg-project_black': route.path.startsWith('/use-case') || route.path.startsWith('/hr/use-case') }" />
                                            </p>
                                        </button>
                                        </MenuItem>

                                        <!-- Usluge -->
                                        <MenuItem as="div" v-slot="{ close }">
                                        <button type="button" @click="go('/services', close)" aria-label="Go to services page"
                                            class="menu-link group w-full text-left py-3 md:py-4 my-2 md:px-6 px-4 flex hover:bg-light_primary rounded-[6.25rem]">
                                            <p class="w-full flex flex-row justify-between items-center">
                                                <span
                                                    class="menu-text relative inline-block overflow-hidden text-[1.375rem] font-medium uppercase my-auto">
                                                    <span class="menu-text-top block transition-transform ease-out">
                                                        {{ $t('services_page') }}
                                                    </span>
                                                    <span
                                                        class="menu-text-bottom block absolute top-0 left-0 transition-transform ease-out">
                                                        {{ $t('services_page') }}
                                                    </span>
                                                </span>
                                                <Icon name="entypo:dot-single"
                                                    class="ml-2 pl-2 transition-all duration-300 my-auto w-10 h-10 opacity-0 group-hover:opacity-100"
                                                    :class="{ 'opacity-100 bg-project_black': route.path.startsWith('/services') || route.path.startsWith('/hr/services') }" />
                                            </p>
                                        </button>
                                        </MenuItem>

                                        <!-- kontakt (linked to /blog in this example) -->
                                        <MenuItem as="div" v-slot="{ close }">
                                        <button type="button" @click="go('/contact', close)" aria-label="Go to contact page"
                                            class="menu-link group w-full text-left py-3 md:py-4 my-2 md:px-6 px-4 flex hover:bg-light_primary rounded-[6.25rem]">
                                            <p class="w-full flex flex-row justify-between">
                                                <span
                                                    class="menu-text relative inline-block overflow-hidden text-[1.375rem] font-medium uppercase my-auto">
                                                    <span class="menu-text-top block transition-transform ease-out">
                                                        {{ $t('contact_page') }}
                                                    </span>
                                                    <span
                                                        class="menu-text-bottom block absolute top-0 left-0 transition-transform ease-out">
                                                        {{ $t('contact_page') }}
                                                    </span>
                                                </span>
                                                <Icon name="entypo:dot-single"
                                                    class="ml-2 pl-2 transition-all duration-300 my-auto w-10 h-10 opacity-0 group-hover:opacity-100"
                                                    :class="{ 'opacity-100 bg-project_black': route.path === '/contact' || route.path === '/hr/contact' }" />
                                            </p>
                                        </button>
                                        </MenuItem>
                                    </div>
                                </MenuItems>
                            </transition>
                        </div>

                    </template>
                </Menu>
                <LanguageSwitcher />
            </div>
        </div>
    </section>
</template>

<script setup>
import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
import { useRouter, useRoute } from 'vue-router'

const localePath = useLocalePath()
const router = useRouter()
const route = useRoute()

function go(path, closeMenu) {
  // build the correct URL for your current locale
  const localized = localePath(path)
  // first close the menu
  closeMenu?.()
  // then navigate
  navigateTo(localized)
}
// navigateTo pushes the new route and then calls close() from the MenuItem slot.
function navigateTo(path, close) {
    router.push(path)
    close()
}
</script>
<style scoped>
.slide-up-enter-active,
.slide-up-leave-active {
    transition: transform 0.3s ease, opacity 0.3s ease;
}

.slide-up-enter-from {
    transform: translateY(100%);
    opacity: 0;
}

.slide-up-enter-to {
    transform: translateY(0);
    opacity: 1;
}

.slide-up-leave-from {
    transform: translateY(0);
    opacity: 1;
}

.slide-up-leave-to {
    transform: translateY(-100%);
    opacity: 0;
}

.slide-down-enter-active,
.slide-down-leave-active {
    transition: transform 0.3s ease, opacity 0.3s ease;
}

.slide-down-enter-from {
    transform: translateY(-100%);
    opacity: 0;
}

.slide-down-enter-to {
    transform: translateY(0);
    opacity: 1;
}

.slide-down-leave-from {
    transform: translateY(0);
    opacity: 1;
}

.slide-down-leave-to {
    transform: translateY(100%);
    opacity: 0;
}

.menu-text {
    position: relative;
    display: inline-block;
    overflow: hidden;
    /* Ensures only one copy of the text is visible */
}

/* Top text: moves out faster */
.menu-text-top {
    transform: translateY(0);
    transition: transform 0.2s ease-out;
    /* Faster transition */
}

/* Bottom text: slides in slower */
.menu-text-bottom {
    top: 0;
    left: 0;
    transform: translateY(100%);
    transition: transform 0.3s ease-out;
    /* Slightly slower transition */
}

/* Hover state: animate the texts */
.menu-link:hover .menu-text-top {
    transform: translateY(-100%);
}

.menu-link:hover .menu-text-bottom {
    transform: translateY(0);
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
</style>