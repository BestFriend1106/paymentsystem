import { createStore } from "vuex";
import axios from "axios";
export default createStore({
  state: {
    invoices: [
      {
        id: 0,
        invoiceNumber: null,
        clientName: null,
        Amount: 0,
        paymentStatus: null,
      },
    ],
  },
  mutations: {
    SET_INVOICES(state, payload) {
      state.invoices = payload;
    },
    ADD_INVOICE(state, payload) {
      state.invoices.push(payload);
    },
    UPDATE_INVOICE(state, payload) {
      const index = state.invoices.findIndex((u) => u.id === payload.id);
      if (index !== -1) {
        state.invoices.splice(index, 1, payload);
      }
    },
    DELETE_INVOICE(state, id) {
      const index = state.invoices.findIndex((u) => u.id === id);
      if (index !== -1) {
        state.invoices.splice(index, 1);
      }
    },
  },
  actions: {
    async fetchInvoices({ commit }) {
      const response = await axios.get("/invoices");
      commit("SET_INVOICES", response.data);
    },
    async addInvoice({ commit }, payload) {
      const response = await axios.post("/invoices", payload);
      commit("ADD_INVOICE", response.data);
    },
    async updateInvoice({ commit }, payload) {
      const response = await axios.put(`/invoices/${payload.id}`, payload);
      commit("UPDATE_INVOICE", response.data);
    },
    async deleteInvoice({ commit }, id) {
      await axios.delete(`/invoices/${id}`);
      commit("DELETE_INVOICE", id);
    },
  },
  getters: {
    getInvoices: (state) => state.invoices,
    getInvoice: (state) => (id) => {
      return state.invoices.find((u) => u.id === id);
    },
  },
});
