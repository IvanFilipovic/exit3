<template>
  <section class="container pb-16">
      <h1 class="mx-auto text-[2rem] md:text-[2.5rem] text-start py-6 max-w-7xl px-4">{{ $t('faq_title') }}</h1>
    <div class="content mx-auto rounded-2xl py-16">
      <Disclosure as="div" v-slot="{ open }">
        <DisclosureButton as="button" 
          class="flex w-full justify-between rounded-lg bg-primary px-4 py-2 text-left text-[1rem] font-medium text-pure_white hover:bg-primary/80 my-3"
        >
          <span>{{ $t('faq_question_1') }}</span>
          <Icon name="entypo:chevron-up"
            :class="open ? 'rotate-180 transform' : ''"
            class="h-5 w-5 text-pure_white"
          />
        </DisclosureButton>
        <DisclosurePanel
          v-if="open"
          v-motion-slide-top
          class="px-4 pb-2 pt-4 text-[1rem] text-project_black"
        >
          {{ $t('faq_answer_1') }}
        </DisclosurePanel>
      </Disclosure>
      <Disclosure as="div" v-slot="{ open }">
        <DisclosureButton as="button" 
          class="flex w-full justify-between rounded-lg bg-primary px-4 py-2 text-left text-[1rem] font-medium text-pure_white hover:bg-primary/80 my-3"
        >
          <span>{{ $t('faq_question_2') }}</span>
          <Icon name="entypo:chevron-up"
            :class="open ? 'rotate-180 transform' : ''"
            class="h-5 w-5 text-pure_white"
          />
        </DisclosureButton>
        <DisclosurePanel
          v-if="open"
          v-motion-slide-top
          class="px-4 pb-2 pt-4 text-[1rem] text-project_black"
        >
          {{ $t('faq_answer_2') }}
        </DisclosurePanel>
      </Disclosure>
      <Disclosure as="div" v-slot="{ open }">
        <DisclosureButton as="button" 
          class="flex w-full justify-between rounded-lg bg-primary px-4 py-2 text-left text-[1rem] font-medium text-pure_white hover:bg-primary/80 my-3"
        >
          <span>{{ $t('faq_question_3') }}</span>
          <Icon name="entypo:chevron-up"
            :class="open ? 'rotate-180 transform' : ''"
            class="h-5 w-5 text-pure_white"
          />
        </DisclosureButton>
        <DisclosurePanel
          v-if="open"
          v-motion-slide-top
          class="px-4 pb-2 pt-4 text-[1rem] text-project_black"
        >
          {{ $t('faq_answer_3') }}
        </DisclosurePanel>
      </Disclosure>
      <Disclosure as="div" v-slot="{ open }">
        <DisclosureButton as="button" 
          class="flex w-full justify-between rounded-lg bg-primary px-4 py-2 text-left text-[1rem] font-medium text-pure_white hover:bg-primary/80 my-3"
        >
          <span>{{ $t('faq_question_4') }}</span>
          <Icon name="entypo:chevron-up"
            :class="open ? 'rotate-180 transform' : ''"
            class="h-5 w-5 text-pure_white"
          />
        </DisclosureButton>
        <DisclosurePanel
          v-if="open"
          v-motion-slide-top
          class="px-4 pb-2 pt-4 text-[1rem] text-project_black"
        >
          {{ $t('faq_answer_4') }}
        </DisclosurePanel>
      </Disclosure>
      <Disclosure as="div" v-slot="{ open }">
        <DisclosureButton as="button" 
          class="flex w-full justify-between rounded-lg bg-primary px-4 py-2 text-left text-[1rem] font-medium text-pure_white hover:bg-primary/80 my-3"
        >
          <span>{{ $t('faq_question_5') }}</span>
          <Icon name="entypo:chevron-up"
            :class="open ? 'rotate-180 transform' : ''"
            class="h-5 w-5 text-pure_white"
          />
        </DisclosureButton>
        <DisclosurePanel
          v-if="open"
          v-motion-slide-top
          class="px-4 pb-2 pt-4 text-[1rem] text-project_black"
        >
          {{ $t('faq_answer_5') }}
        </DisclosurePanel>
      </Disclosure>
    </div>
  </section>
</template>

<script setup>
import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue'
</script>
