<template>
  <UFooter>
    <template #left>
      <p class="text-muted text-sm">Copyright © {{ new Date().getFullYear() }}</p>
    </template>

    <template #right>
      <UButton
        icon="i-simple-icons-linkedin"
        color="neutral"
        variant="ghost"
        to="https://linkedin.com/in/acgv22"
        target="_blank"
        aria-label="Linkedin"
      />
      <UButton
        icon="i-simple-icons-github"
        color="neutral"
        variant="ghost"
        to="https://github.com/knameless27"
        target="_blank"
        aria-label="GitHub"
      />
    </template>
  </UFooter>
</template>
