import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    redirect: "/paints",
  },
  {
    path: "/paints",
    name: "paints",
    component: () => import("../views/PaintsView.vue"),
  },
  {
    path: "/palettes",
    name: "palettes",
    component: () => import("../views/PalettesView.vue"),
  },
  {
    path: "/scale-effect",
    name: "scale-effect",
    component: () => import("../views/ScaleEffectView.vue"),
  },
  {
    path: "/modulation",
    name: "modulation",
    component: () => import("../views/ModulationView.vue"),
  },
  {
    path: "/history",
    name: "history",
    component: () => import("../views/HistoryView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
