<template>
  <div class="max-w-xl mx-auto">
    <h1 class="text-2xl text-center font-bold mt-10 mb-4">Invoice Generator</h1>
    <form  class="bg-gray-100 rounded-lg p-4">
      
      <div class="mb-4">
        <label for="name" class="block font-medium text-gray-700"
          >Name:</label
        >
        <input
          type="text"
          id="name"
          v-model="name"
          required
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 py-2 px-3"
        />
      </div>
      <div class="mb-4">
        <label for="email" class="block font-medium text-gray-700"
          >Email:</label
        >
        <input
          type="email"
          id="email"
          v-model="email"
          required
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 py-2 px-3"
        />
      </div>
      <div class="mb-4">
        <label for="amount" class="block font-medium text-gray-700"
          >Amount:</label
        >
        <input
          type="number"
          id="amount"
          v-model="amount"
          required
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 py-2 px-3"
        />
      </div>
      <div class="mb-4">
        <label for="dueDate" class="block font-medium text-gray-700"
          >Date:</label
        >
        <input
          type="date"
          id="dueDate"
          v-model="dueDate"
          required
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 py-2 px-3"
        />
      </div>
      <div class="text-center">
        <button
          @click.prevent="generateInvoice"
          class="inline-block bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded"
        >
          Generate Invoice
        </button>
      </div>
    </form>
     
  </div>
</template>
<script>
//import contractInstance from '../contractInstance'
export default {
  name: "InvoiceGenerator",
  data() {
    return {       
      name: "",
      email: "",
      amount: "",
      date: "",
    };
  },
  methods: {
    async generateInvoice() {
      // Call backend to generate invoice and get invoice ID
      const response = await axios.post("/api/invoice", {
        name: this.name,
        email: this.email,
        amount: this.amount,
        date: this.date,
      });
      const invoiceId = response.data.invoiceId;

      // Redirect to Payment page with invoice ID as parameter
      this.$router.push(`/payment/${invoiceId}`);
    },
  },
};
</script>
<style>
input {
  height: 40px !important;
  padding-left: 10px !important;
  padding-right: 10px !important;
}

textarea {
  padding: 10px !important;
}

input:focus,
textarea:focus {
  outline: none !important;
  border: solid 1px rgb(59 130 246 / 0.5) !important;
}
</style>
