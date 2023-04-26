<template>
  <div class="p-4 md:p-8">
    <h1 class="text-2xl md:text-4xl font-bold mb-4">Invoice Dashboard</h1>
    <div
      class="chart-container bg-white shadow-md rounded-lg p-4 relative mb-4 md:mb-8"
    >
      <canvas ref="chart" class="chart-canvas"></canvas>
    </div>

    <div class="summary-container grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
      <div class="total-container bg-white shadow-md rounded-lg p-4">
        <div class="paid-container">
          <h3 class="text-xl font-bold mb-2">Paid Invoices</h3>
          <p class="mb-1">{{ paidCount }} Invoices</p>
          <p class="font-bold text-lg mb-2">Total Amount: {{ paidTotal }}</p>
        </div>
      </div>
      <div class="total-container bg-white shadow-md rounded-lg p-4">
        <div class="unpaid-container">
          <h3 class="text-xl font-bold mb-2">Unpaid Invoices</h3>
          <p class="mb-1">{{ unpaidCount }} Invoices</p>
          <p class="font-bold text-lg mb-2">Total Amount: {{ unpaidTotal }}</p>
        </div>
      </div>
    </div>
    <table class="w-full table-auto">
      <thead>
        <tr>
          <th class="px-4 py-2">Invoice Number</th>
          <th class="px-4 py-2">Client Name</th>
          <th class="px-4 py-2">Amount</th>
          <th class="px-4 py-2">Payment Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="invoice in invoices" :key="invoice.id">
          <td class="border px-4 py-2">{{ invoice.invoice_number }}</td>
          <td class="border px-4 py-2">{{ invoice.client_name }}</td>
          <td class="border px-4 py-2">{{ invoice.amount }}</td>
          <td class="border px-4 py-2">{{ invoice.payment_status }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style>
.chart-container {
  height: 400px;
}

.chart-canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100% !important;
  height: 100% !important;
}
</style>

<script>
import Chart from "chart.js/auto";
import { useStore } from "vuex";

export default {
  name: "Dashboard",
  setup() {
    const store = useStore();
    store.dispatch("fetchInvoices");
  },
  data() {
    return {
      invoices: [
        {
          id: 1,
          invoice_number: "INV001",
          client_name: "John Smith",
          amount: 100,
          payment_status: "Paid",
        },
        {
          id: 2,
          invoice_number: "INV002",
          client_name: "Jane Doe",
          amount: 200,
          payment_status: "Pending",
        },
        {
          id: 3,
          invoice_number: "INV003",
          client_name: "Bob Johnson",
          amount: 300,
          payment_status: "Unpaid",
        },
      ],
    };
  },
  mounted() {
    this.initInvoice();
    this.renderChart();
  },
  computed: {
    paidTotal() {
      return this.invoices
        .filter((invoice) => invoice.payment_status === "Paid")
        .reduce((a, b) => a + b.amount, 0);
    },
    unpaidTotal() {
      return this.invoices
        .filter((invoice) => invoice.payment_status === "Unpaid")
        .reduce((a, b) => a + b.amount, 0);
    },
    paidCount() {
      return this.invoices.filter(
        (invoice) => invoice.payment_status === "Paid"
      ).length;
    },
    unpaidCount() {
      return this.invoices.filter(
        (invoice) => invoice.payment_status === "Unpaid"
      ).length;
    },
  },
  methods: {
    initInvoice() {
      this.invoices = this.$store.getters.getInvoices;
    },
    renderChart() {
      const amounts = this.invoices.map((invoice) => invoice.amount);
      const chartData = {
        labels: ["Invoice 1", "Invoice 2", "Invoice 3"],
        datasets: [
          {
            label: "Invoice Amounts",
            data: amounts,
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
            ],
            borderWidth: 1,
          },
        ],
      };
      const chartOptions = {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      };
      const chart = new Chart(this.$refs.chart, {
        type: "bar",
        data: chartData,
        options: chartOptions,
      });
    },
  },
};
</script>
