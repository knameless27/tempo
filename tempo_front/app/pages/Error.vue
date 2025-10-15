<script setup lang="ts">
const route = useRoute();

const error = ref<{
  statusCode: number;
  statusMessage: string;
  message: string;
}>({
  statusCode: route.query.statusCode ? +route.query.statusCode : 404,
  statusMessage: route.query.statusMessage
    ? returningStringFromPossibleArray(route.query.statusMessage)
    : "Page not found",
  message: route.query.message
    ? returningStringFromPossibleArray(route.query.message)
    : "The page you are looking for does not exist.",
});

function returningStringFromPossibleArray(
  char:
    | import("vue-router").LocationQueryValue
    | import("vue-router").LocationQueryValue[]
) {
  if (Array.isArray(char)) {
    return (char[0] ?? "") as string;
  }
  return (char ?? "") as string;
}
</script>

<template>
  <UError :error="error" />
</template>
