<template>
  <div class="pt-32 py-16 lg:min-h-screen flex flex-col w-full">
    <ServicesDetails :service="service" />
    <section class="border-animated w-full md:border-t md:border-project_gray/40 h-full relative z-20">
      <div class="max-w-7xl flex flex-col md:flex-row md:gap-6 justify-center mx-auto">
        <div v-for="(step, index) in steps" :key="index" class="step-box">
          <!-- Dot Icon -->
          <Icon class="dot-icon z-50 hidden md:block" name="entypo:dot-single" />

          <!-- Title & Description -->
          <h1 class="text-[1.2rem] py-2 font-medium">{{ step.title }}</h1>
          <p class="text-[1rem] py-2">{{ step.description }}</p>
        </div>
      </div>
    </section>
    <CallToAction />
  </div>
</template>
<script setup>
const { t } = useI18n()

const steps = [
  { title: t('testing_step_1_title'), description: t('testing_step_1_description') },
  { title: t('testing_step_2_title'), description: t('testing_step_2_description') },
  { title: t('testing_step_3_title'), description: t('testing_step_3_description') }
]
const service = {
  title: t('testing_service_title'),
  small_description: t('testing_service_small_description'),
  descriptionOne: t('testing_service_descriptionOne'),
  descriptionTwo: t('testing_service_descriptionTwo'),
  image: "testing.svg",
  alt: "QA Automation",
  jobs: [
    { name: t('job_mobile_app_automation'), icon: "devicon:selenium", isIcon: true },
    { name: t('job_api_automation'), icon: "devicon:postman", isIcon: true },
    { name: t('job_web_app_automation'), icon: "devicon:playwright", isIcon: true }
  ]
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

/* Parent container */
.border-animated {
  position: relative;
  overflow: visible;
}

/* Glowing light pulse border */
.border-animated::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  filter: blur(0.7rem);
  border-radius: 200px 200px 200px 200px;
  height: 8px;
  width: 3%;
  -webkit-box-shadow: 0px 0px 30px 5px rgba(179, 180, 189, 1);
  -moz-box-shadow: 0px 0px 30px 5px rgba(179, 180, 189, 1);
  box-shadow: 0px 0px 30px 5px rgba(179, 180, 189, 1);
  animation: pulseBorder 5.5s ease-in-out infinite;
}

.step-box {
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 4rem 1rem;
  background: transparent;
  z-index: 1;
}

/* Dot Icon */
.dot-icon {
  position: absolute;
  top: -20px;
  left: 0;
  width: 2.5rem;
  height: 2.5rem;
  color: #0A21C0;
}

@media (max-width: 768px) {
  .border-animated::after {
    display: none;
  }
}

@keyframes pulseBorder {
  0% {
    left: 0;
    opacity: 0.8;
  }

  50% {
    left: 40%;
    opacity: 1;
  }

  100% {
    left: 100%;
    opacity: 0;
  }
}
</style>