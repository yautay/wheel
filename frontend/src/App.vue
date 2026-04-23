<script setup lang="ts">
const navItems = [
  { label: "Paints", to: "/paints" },
  { label: "Palettes", to: "/palettes" },
  { label: "Scale Effect", to: "/scale-effect" },
  { label: "Modulation", to: "/modulation" },
  { label: "History", to: "/history" },
];
</script>

<template>
  <div class="min-h-screen bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 text-slate-100">
    <div class="mx-auto flex min-h-screen w-full max-w-6xl flex-col px-4 py-8 sm:px-6 lg:px-10">
      <header class="mb-8 rounded-xl border border-slate-700/70 bg-slate-900/80 p-5 shadow-lg shadow-black/20">
        <p class="text-xs uppercase tracking-[0.3em] text-amber-300">Model Paint MVP</p>
        <h1 class="mt-2 text-2xl font-semibold text-slate-100 sm:text-3xl">Workflow Sandbox</h1>
        <p class="mt-2 text-sm text-slate-300">
          Foundation shell for paints, palettes, scale effect, modulation, and history flows.
        </p>
      </header>

      <nav class="mb-8 flex flex-wrap gap-2">
        <RouterLink
          v-for="item in navItems"
          :key="item.to"
          :to="item.to"
          class="rounded-md border border-slate-700 bg-slate-800 px-3 py-2 text-sm text-slate-200 transition hover:border-amber-300 hover:text-amber-200"
          active-class="!border-amber-300 !text-amber-200"
        >
          {{ item.label }}
        </RouterLink>
      </nav>

      <main class="flex-1 rounded-xl border border-slate-700/80 bg-slate-900/70 p-6">
        <RouterView />
      </main>
    </div>
  </div>
</template>
