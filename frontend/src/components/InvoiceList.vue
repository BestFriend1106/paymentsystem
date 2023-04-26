<template>
  <div class="container mx-auto py-8">
    <h2 class="text-2xl font-bold text-gray-800 mb-4">Invoice List</h2>
    <div class="w-full overflow-auto">
      <table class="w-full border-collapse bg-white shadow-md rounded">
        <thead>
          <tr
            class="bg-gray-200 text-gray-700 uppercase text-sm leading-normal"
          >
            <th class="py-3 px-6 text-left">Invoice ID</th>
            <th class="py-3 px-6 text-left">Name</th>
            <th class="py-3 px-6 text-left">Email</th>
            <th class="py-3 px-6 text-left">Amount</th>
            <th class="py-3 px-6 text-left">Date</th>
            <th class="py-3 px-6 text-left">Status</th>             
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="invoice in invoices"
            :key="invoice.invoiceId"
            class="border-b border-gray-200 hover:bg-gray-100"
          >
            <td class="py-4 px-6">{{ invoice.invoiceId }}</td>
            <td class="py-4 px-6">{{ invoice.name }}</td>
            <td class="py-4 px-6">{{ invoice.email }}</td>
            <td class="py-4 px-6">{{ invoice.amount }}</td>
            <td class="py-4 px-6">{{ invoice.date }}</td>
            <td class="py-4 px-6">{{ invoice.status }}</td>
  
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      invoices: [],
    };
  },

  async mounted() {
    // Call backend to get list of invoices
    const response = await axios.get("/api/invoice");
    this.invoices = response.data.invoices;
  },
  
};
</script>

<style scoped>
table td {
  vertical-align: top;
}

@media only screen and (max-width: 768px) {
  table td {
    display: block;
  }
  table tr {
    border-bottom: 1px solid #ddd;
    display: block;
    padding: 5px 0;
  }
  table tr:nth-of-type(even) {
    background-color: rgba(0, 0, 0, 0.05);
  }
  table tr:nth-of-type(odd) {
    background-color: #fff;
  }
  table th {
    display: none;
  }
}
</style>
