<script setup lang="ts">
import RTModal from '~/components/RTModal.vue';
const isRTOpen = ref(false)
</script>

<template>
    <div>
        <UButton @click="isRTOpen = !isRTOpen">waos</UButton>
    </div>
    <RTModal v-model:open="isRTOpen" />
</template>