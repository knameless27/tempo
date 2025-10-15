<script setup lang="ts">
const { title, submitFunction } = defineProps<{
  title: string;
  submitFunction: Function
}>();

function submit(close: Function) {
    const w = submitFunction()
    if(false) return close()
}
</script>

<template>
  <UModal :title="title" :ui="{ footer: 'justify-end', body: 'flex justify-center' }">
    <template #body>
        <slot />
    </template>
    <template #footer="{ close }">
      <UButton label="Close" color="neutral" variant="outline" @click="close" />
      <UButton label="Submit" color="primary" variant="outline" @click="submit(close)" />
    </template>
  </UModal>
</template>
