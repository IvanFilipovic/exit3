<template>
  <section class="container">
    <div class="content flex flex-col">
      <div v-if="loading" class="my-auto">
        <p class="mx-auto py-16 text-center text-[2rem] tracking-wide" role="status" aria-live="polite">
          {{ $t('contact_form_sending') }}
        </p>
        <div class="loading mx-auto flex items-center justify-center" aria-hidden="true">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
      <div v-else-if="success" class="my-auto">
        <p class="mx-auto py-6 text-center text-[2rem] tracking-wide" role="status" aria-live="polite">
          {{ $t('contact_form_success') }}
        </p>
        <div class="mx-auto pb-10 flex items-center justify-center">
          <MdiIcon icon="mdiCheckCircleOutline" class="text-primary h-14 w-14" aria-hidden="true" />
        </div>
        <NuxtLink to="/" class="button-primary flex flex-row w-fit justify-start items-center mt-4 mx-auto"
          :aria-label="$t('home_page_link')">
          <p class="group relative w-max flex flex-row items-start">
            <!-- Arrow: initially hidden and shifted left -->
            <Icon class="arrow transition-all duration-300 ml-2 w-8 h-8" name="meteor-icons:arrow-right-long"
              aria-hidden="true" />
            <!-- Button text -->
            <span
              class="button-text px-auto py-auto text-[1rem] font-medium uppercase transition-transform duration-300 my-auto">
              {{ $t('home_page_link') }}
            </span>
            <!-- Icon: will fade out on hover -->
            <Icon class="icon mx-auto my-auto ml-2 pl-2 transition-opacity duration-300 w-8 h-8"
              name="entypo:dot-single" aria-hidden="true" />
          </p>
        </NuxtLink>
      </div>
      <div v-else class="py-24">
        <h1 class="text-[2rem] md:text-[2.5rem] text-project_black font-semibold">{{ $t('contact_page_title') }}</h1>
        <p class="text-project_black text-[1rem] mb-6 leading-relaxed">
          {{ $t('contact_page_intro') }}
        </p>
        <div class="py-10 w-full">
          <p class="text-[1.5rem] font-medium text-project_black mb-4">{{ $t('contact_page_topics_intro') }}</p>
          <div class="flex flex-wrap gap-3">
            <button v-for="(cat, index) in categories" :key="index" @click="selectTopic(cat)" :class="[
              'px-6 py-2 rounded-full border text-[1rem] font-base transition',
              selectedTopic === cat.value
                ? 'bg-primary text-pure_white'
                : 'bg-pure_white border-project_gray text-project_black hover:bg-light_primary'
            ]"
            aria-label="Select topic">
              {{ cat.label }}
            </button>
          </div>
        </div>
        <!-- Error Message Display -->
        <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-4"
          role="alert" aria-live="assertive">
          <div class="flex justify-between items-start">
            <p>{{ errorMessage }}</p>
            <button @click="errorMessage = null" class="text-sm underline hover:no-underline ml-4"
              :aria-label="$t('dismiss')">
              {{ $t('dismiss') }}
            </button>
          </div>
        </div>

        <form @submit.prevent="submitForm" class="mt-8 space-y-6 py-4" novalidate>
          <div class="flex flex-col md:flex-row md:items-end md:space-x-2">
            <label for="name" class="text-project_black text-[1rem] font-medium">
              {{ $t('contact_page_greeting') }}
            </label>
            <input id="name" type="text" v-model="formData.name" :placeholder="$t('contact_page_placeholder_name')"
              class="flex-grow p-2 border-b border-project_black focus:outline-none focus:border-primary bg-inherit"
              :aria-required="true" :aria-invalid="formAttempted && !formData.name.trim()" />
            <span class="hidden md:flex" aria-hidden="true">,</span>
          </div>

          <div class="flex flex-col md:flex-row md:items-end md:space-x-2 space-y-2">
            <label for="jobTitle" class="text-project_black text-[1rem] font-medium">
              {{ $t('contact_page_job_title') }}
            </label>
            <input id="jobTitle" type="text" v-model="formData.jobTitle"
              :placeholder="$t('contact_page_placeholder_job')"
              class="flex-grow p-2 border-b border-project_black focus:outline-none focus:border-primary bg-inherit"
              :aria-required="true" :aria-invalid="formAttempted && !formData.jobTitle.trim()" />
            <span class="pt-2 md:pt-0" aria-hidden="true">{{ $t('contact_page_company_connector') }}</span>
            <label for="company" class="sr-only">{{ $t('contact_page_placeholder_company') }}</label>
            <input id="company" type="text" v-model="formData.company"
              :placeholder="$t('contact_page_placeholder_company')"
              class="flex-grow p-2 border-b border-project_black focus:outline-none focus:border-primary bg-inherit"
              :aria-required="true" :aria-invalid="formAttempted && !formData.company.trim()" />
            <span class="hidden md:flex" aria-hidden="true">.</span>
          </div>

          <!-- Email -->
          <div class="flex flex-col md:flex-row md:items-end md:space-x-2 space-y-2 relative">
            <label for="email" class="text-project_black text-[1rem] font-medium">
              {{ $t('contact_page_email_intro') }}
            </label>
            <input id="email" type="email" v-model="formData.email"
              :placeholder="$t('contact_page_placeholder_email')"
              class="flex-grow p-2 border-b focus:outline-none bg-inherit" :class="{
                'border-project_black focus:border-primary': isEmailValid || !formData.email,
                'border-red-500/90 focus:border-red-500/90': !isEmailValid && formData.email
              }" :aria-required="true" :aria-invalid="!isEmailValid && formData.email !== ''"
              :aria-describedby="!isEmailValid && formData.email ? 'email-error' : undefined" />
            <span v-if="!isEmailValid && formData.email" id="email-error"
              class="text-red-500/90 text-[1rem] font-medium absolute right-0" role="alert">
              {{ $t('contact_page_invalid_email') }}
            </span>
          </div>
          <div class="flex py-8">
            <button class="group flex flex-row w-fit uppercase mx-auto mt-4 py-3 px-6 my-auto rounded-[6.25rem]" aria-label="Submit contact form"
              :class="isFormValid && isEmailValid ? 'bg-project_black text-pure_white hover:bg-primary w-fit' : 'bg-project_gray text-project_black w-fit'"
              :disabled="!isFormValid || !isEmailValid" type="submit">
              <Icon class="arrow transition-all duration-300 ml-2 w-8 h-8" name="meteor-icons:arrow-right-long" />
              <span class="button-text px-auto py-auto my-auto">{{ $t('contact_page_button') }}</span>
              <Icon class="icon mx-auto my-auto ml-2 pl-2 transition-opacity duration-300 w-8 h-8"
                name="entypo:dot-single" />
            </button>
          </div>

        </form>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

// TypeScript interfaces
interface FormData {
  name: string
  jobTitle: string
  company: string
  email: string
}

interface Category {
  label: string
  value: string
}

// Composables
const { t } = useI18n()

// Reactive state
const loading = ref<boolean>(false)
const success = ref<boolean>(false)
const errorMessage = ref<string | null>(null)
const formAttempted = ref<boolean>(false)

// Topic categories
const categories: Category[] = [
  { label: 'Web Development', value: 'web_dev' },
  { label: 'Mobile Development', value: 'mobile_dev' },
  { label: 'Automated Testing', value: 'automated_testing' },
  { label: 'Social Media Automation', value: 'social_media_auto' },
  { label: 'E-commerce Automation', value: 'ecommerce_auto' },
  { label: 'Sales Automation', value: 'sales_auto' },
]

const selectedTopic = ref<string | null>(null)
const formData = ref<FormData>({
  name: '',
  jobTitle: '',
  company: '',
  email: '',
})

// Email validation
const isEmailValid = computed<boolean>(() => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(formData.value.email) || formData.value.email === ''
})

// Topic selection
const selectTopic = (topic: Category): void => {
  selectedTopic.value = topic.value
}

// Form validation
const isFormValid = computed<boolean>(() => {
  return (
    formData.value.name.trim() !== '' &&
    formData.value.jobTitle.trim() !== '' &&
    formData.value.company.trim() !== '' &&
    formData.value.email.trim() !== '' &&
    selectedTopic.value !== null
  )
})

// Form submission
const submitForm = async (): Promise<void> => {
  formAttempted.value = true
  errorMessage.value = null

  if (!isFormValid.value) {
    return
  }

  loading.value = true

  try {
    await $fetch('/api/submit-lead', {
      method: 'POST',
      body: {
        full_name: formData.value.name,
        position: formData.value.jobTitle,
        company_name: formData.value.company,
        email: formData.value.email,
        category: selectedTopic.value,
      },
    })

    loading.value = false
    success.value = true
  } catch (error: any) {
    loading.value = false
    console.error('Form submission error:', error)

    // Display user-friendly error message
    if (error?.statusCode === 500 || error?.data?.statusCode === 500) {
      errorMessage.value = t('contact_form_error_message')
    } else if (error?.name === 'FetchError' || !navigator.onLine) {
      errorMessage.value = t('contact_form_network_error')
    } else {
      errorMessage.value = error?.data?.statusMessage || t('contact_form_error_message')
    }
  }
}
</script>
<style scoped>
/* Screen reader only - visually hidden but accessible to screen readers */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.loading span {
  width: 15px;
  height: 15px;
  margin: 0 5px;
  background-color: #0A21C0;
  border-radius: 50%;
  display: inline-block;
  animation-name: jumpingDots;
  animation-duration: 1.4s;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}

.loading span:nth-child(2) {
  animation-delay: 0.3s
}

.loading span:nth-child(3) {
  animation-delay: 0.6s
}

@keyframes jumpingDots {
  20% {
    transform: translateY(0px);
  }

  50% {
    transform: translateY(-13px)
  }
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