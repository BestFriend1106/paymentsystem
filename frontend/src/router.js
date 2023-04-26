import { createRouter, createWebHashHistory } from "vue-router";
import Dashboard from "./components/Dashboard.vue";
import InvoiceGenerator from "./components/InvoiceGenerator.vue";
import InvoiceList from "./components/InvoiceList.vue";
import PaymentConfirmation from "./components/PaymentConfirmation.vue";
import PaymentStatusChecker from "./components/PaymentStatusChecker.vue";

const routes = [
  { path: "/", name: "Dashboard", component: Dashboard },
  {
    path: "/invoice-generator",
    name: "InvoiceGenerator",
    component: InvoiceGenerator,
  },
  { path: "/invoice-list", name: "InvoiceList", component: InvoiceList },
  {
    path: "/payment-confirmation",
    name: "PaymentConfirmation",
    component: PaymentConfirmation,
  },
  {
    path: "/payment-status-checker",
    name: "PaymentStatusChecker",
    component: PaymentStatusChecker,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;