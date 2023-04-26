<script>
import router from "./router";

export default {
  name: "App",
  router,
};
</script>

<template>
  <div>
    <nav class="bg-white shadow">
      <div
        class="container mx-auto py-4 px-6 md:flex md:justify-between md:items-center"
      >
        <div class="flex items-center justify-between"></div>
        <div class="hidden md:flex md:flex-1 md:justify-center"></div>
        <div class="hidden md:flex md:flex-1 md:justify-end">
          <div class="flex items-center justify-between md:ml-6">
            <router-link
              class="text-gray-500 py-2 px-4 transition-colors duration-300"
              :class="{
                'hover:text-gray-700 bg-gray-200': $route.path === '/',
              }"
              to="/"
              >Dashboard</router-link
            >
            <router-link
              class="text-gray-500 py-2 px-4 transition-colors duration-300"
              :class="{
                'hover:text-gray-700 bg-gray-200':
                  $route.path === '/invoice-generator',
              }"
              to="/invoice-generator"
              >InvoiceGenerator</router-link
            >
            <router-link
              class="text-gray-500 py-2 px-4 transition-colors duration-300"
              :class="{
                'hover:text-gray-700 bg-gray-200':
                  $route.path === '/invoice-list',
              }"
              to="/invoice-list"
              >InvoiceList</router-link
            >
            <router-link
              class="text-gray-500 py-2 px-4 transition-colors duration-300"
              :class="{
                'hover:text-gray-700 bg-gray-200':
                  $route.path === '/payment-confirmation',
              }"
              to="/payment-confirmation"
              >PaymentConfirmation</router-link
            >
            <router-link
              class="text-gray-500 py-2 px-4 transition-colors duration-300"
              :class="{
                'hover:text-gray-700 bg-gray-200':
                  $route.path === '/payment-status-checker',
              }"
              to="/payment-status-checker"
              >PaymentStatusChecker</router-link
            >
          </div>
        </div>
        <div class="md:hidden" :class="{ hidden: !open }">
          <div class="pt-2 pb-3">
            <router-link
              class="text-gray-500 py-2 px-4 transition-colors duration-300"
              :class="{
                'hover:text-gray-700 bg-gray-200': $route.path === '/',
              }"
              to="/"
              >Dashboard</router-link
            >
            <router-link
              class="text-gray-500 py-2 px-4 transition-colors duration-300"
              :class="{
                'hover:text-gray-700 bg-gray-200':
                  $route.path === '/invoice-generator',
              }"
              to="/invoice-generator"
              >InvoiceGenerator</router-link
            >
            <router-link
              class="text-gray-500 py-2 px-4 transition-colors duration-300"
              :class="{
                'hover:text-gray-700 bg-gray-200':
                  $route.path === '/invoice-list',
              }"
              to="/invoice-list"
              >InvoiceList</router-link
            >
            <router-link
              class="text-gray-500 py-2 px-4 transition-colors duration-300"
              :class="{
                'hover:text-gray-700 bg-gray-200':
                  $route.path === '/payment-confirmation',
              }"
              to="/payment-confirmation"
              >PaymentConfirmation</router-link
            >
            <router-link
              class="text-gray-500 py-2 px-4 transition-colors duration-300"
              :class="{
                'hover:text-gray-700 bg-gray-200':
                  $route.path === '/payment-status-checker',
              }"
              to="/payment-status-checker"
              >PaymentStatusChecker</router-link
            >
          </div>
        </div>
      </div>
    </nav>
    <router-view />
  </div>
</template>
