<template>
  <div class="max-w-lg mx-auto mt-8">
    <h1 class="text-3xl text-center font-bold mb-8">
      Payment Confirmation 
    </h1>
    <form
      class="bg-white rounded-lg shadow-md p-6"
    >
      <div class="mb-4">
        <label for="InvoiceId" class="block text-gray-700 font-medium mb-2"
          >Invoice ID:</label
        >
        <input
          type="text"
          id="InvoiceId"
          v-model="InvoiceId"
          required
          class="border-2 border-gray-400 rounded-md w-full py-2 px-3 focus:outline-none focus:border-indigo-500"
        />
      </div>
      <div class="mb-4">
        <label for="name" class="block text-gray-700 font-medium mb-2"
          >Name:</label
        >
        <input
          type="name"
          id="name"
          v-model="name"
          required
          class="border-2 border-gray-400 rounded-md w-full py-2 px-3 focus:outline-none focus:border-indigo-500"
        />
      </div>
      <div class="mb-4">
        <label for="email" class="block text-gray-700 font-medium mb-2"
          >Email:</label
        >
        <input
          type="email"
          id="email"
          v-model="email"
          required
          class="border-2 border-gray-400 rounded-md w-full py-2 px-3 focus:outline-none focus:border-indigo-500"
        />
      </div>
      <div class="mb-4">
        <label for="amount" class="block text-gray-700 font-medium mb-2"
          >amount:</label
        >
        <input
          type="number"
          id="amount"
          v-model="amount"
          required
          class="border-2 border-gray-400 rounded-md w-full py-2 px-3 focus:outline-none focus:border-indigo-500"
        />
      </div>
      <div class="mt-6 text-center">
        <button
          @click.prevent="payInvoice"
          class="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-full" 
        >
          Confirm Payment
        </button>
      </div>
    </form>
     
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "PaymentConfirmation",
  data () {
      return {
       invoiceId: this.$route.params.invoiceId,
       name: "",
       email: "",
       amount: "",
      }
    },
    async mounted() {
    // Call backend to get invoice details
      const response = await axios.get(`/api/invoice/${this.invoiceId}`);
      this.name = response.data.name;
      this.email = response.data.email;
      this.amount = response.data.amount;
  },
  methods: {
    async payInvoice() {
      // Open TRONlink wallet to pay the invoice
      const result = await window.tronWeb.requestPayment(
        this.amount * 1000000,
        "Payment for invoice " + this.invoiceId
      );
      const txId = result.txid;

      // Call backend to update invoice status with transaction ID
      await axios.put(`/api/invoice/${this.invoiceId}`, { txId });

      // Redirect to Payment Status page with invoice ID as parameter
      this.$router.push(`/payment-status/${this.invoiceId}`);
    },
  },
};
</script>
