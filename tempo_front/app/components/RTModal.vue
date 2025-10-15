<script setup lang="ts">
import DefaultModal from "./DefaultModal.vue";
import * as v from "valibot";
import type { FormSubmitEvent } from "@nuxt/ui";

type Schema = v.InferOutput<typeof schema>;

const rtForm = ref<any>(null);
const toast = useToast();
const schema = v.object({
  email: v.pipe(v.string(), v.email("Invalid email")),
  password: v.pipe(v.string(), v.minLength(8, "Must be at least 8 characters")),
});

const state = reactive({
  email: "",
  password: "",
});

// event: FormSubmitEvent<Schema>
async function onSubmit() {
  if (!rtForm.value) return false;
  try {
  await rtForm.value.validate();
  toast.add({
    title: "Success",
    description: "The form has been submitted.",
    color: "success",
  });
    console.log(rtForm.value.errors)
    // const xd = rtForm.value.getErrors();
    // console.log(xd);
  } catch (error) {
    console.log(error);
    return false;
  }
}
</script>

<template>
  <DefaultModal title="Routine types" :submit-function="onSubmit">
    <UForm ref="rtForm" :schema="schema" :state="state" class="space-y-4">
      <UFormField label="Email" name="email">
        <UInput v-model="state.email" />
      </UFormField>

      <UFormField label="Password" name="password">
        <UInput v-model="state.password" type="password" />
      </UFormField>
    </UForm>
  </DefaultModal>
</template>
