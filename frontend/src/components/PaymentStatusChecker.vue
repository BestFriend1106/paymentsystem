<template>
  <div class="max-w-md mx-auto">
    <h1 class="text-3xl font-bold text-center mb-6 mt-10">
      Payment Status Checker
    </h1>
    <form
      class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"  
    >
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="invoiceID"
          >Invoice ID:</label
        >
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="invoice-id"
          type="text"
          v-model="invoiceID"
          required
        />
      </div>
      <div class="flex items-center justify-between">
        <button  @click.prevent="checkStatus"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
   
        >
          Check Payment Status
        </button>
      </div>
    </form>
     
  </div>
</template>
<script>

import axios from "axios";
export default {
  data() {
    return {
      invoiceId: "",
      status: "",
    };
  },
  methods: {
    async checkStatus() {
      // Call backend to check invoice status
      const response = await axios.get(`/api/invoice/${this.invoiceId}`);

      if (response.data.status === "paid") {
        this.status = "Invoice has been paid.";
      } else {
        this.status = "Invoice is still pending payment.";
      }
    },
  },
};
</script>
