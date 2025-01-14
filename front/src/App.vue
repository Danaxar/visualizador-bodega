<template>
  <div id="app">
    <h1>Inventario</h1>
    <div v-if="data">
      <table id="inventario-table-A">
        <tr>
          <td class="">A37</td>
          <td class="">A38</td>
          <!-- A43 -->
          <td class="">
            <table class="nested-table">
              <tr>
                <td class="subcell">A43</td>
              </tr>
              <tr>
                <td class="subcell">A39</td>
              </tr>
            </table>
          </td>
          <!-- A44 -->
          <td class="">
            <table class="nested-table">
              <tr>
                <td class="subcell">A44</td>
              </tr>
              <tr>
                <td class="subcell">A40</td>
              </tr>
            </table>
          </td>
          <!-- A45 -->
          <td class="">
            <table class="nested-table">
              <tr>
                <td class="subcell">A45</td>
              </tr>
              <tr>
                <td class="subcell">A41</td>
              </tr>
            </table>
          </td>
          <!-- A46 -->
          <td class="">
            <table class="nested-table">
              <tr>
                <td class="subcell">A46</td>
              </tr>
              <tr>
                <td class="subcell">A42</td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td>A31</td>
          <td>A32</td>
          <td>A33</td>
          <td>A34</td>
          <td>A35</td>
          <td>A36</td>
        </tr>
        <tr>
          <td>A25</td>
          <td>A26</td>
          <td>A27</td>
          <td>A28</td>
          <td>A29</td>
          <td>A30</td>
        </tr>
        <tr>
          <td>A19</td>
          <td>A20</td>
          <td>A21</td>
          <td>A22</td>
          <td>A23</td>
          <td>A24</td>
        </tr>
        <tr>
          <td>A13</td>
          <td>A14</td>
          <td>A15</td>
          <td>A16</td>
          <td>A17</td>
          <td>A18</td>
        </tr>
        <tr>
          <td>A7</td>
          <td>A8</td>
          <td>A9</td>
          <td>A10</td>
          <td>A11</td>
          <td>A12</td>
        </tr>
        <tr>
          <td>A1</td>
          <td>A2</td>
          <td>A3</td>
          <td>A4</td>
          <td>A5</td>
          <td>A6</td>
        </tr>
      </table>
    </div>
    <div>
      <input type="text" placeholder="Buscar por codigo" v-model="codigoBuscar">
      <button @click="buscar">Buscar</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'App',
  data() {
    return {
      data: null,
      estanteA: {},
      cantidadEstantes: 2,
      cantidadFilas: 7,

      // Busqueda
      codigoBuscar: '',
      ubicacion: '',
      celdaResaltada: '',
    }
  },
  watch: {
    data: {
      handler: function () {
        console.log('Ahora llegó la data del inventario');
        console.log(this.data);
      },
      deep: true
    }
  },
  methods: {
    async getInventario() {
      const response = await axios.get('http://localhost:5000/api/inventario');
      this.data = response.data;
    },
    async buscar() {
      console.log('Buscando...');
    const response = await axios.get('http://localhost:5000/api/inventario/' + this.codigoBuscar);
    console.log(response.data);
    this.ubicacion = response.data[0].ubicacion;

    // alert('La ubicación es ' + this.ubicacion);

    // Limpia el resaltado anterior
    document.querySelectorAll('.highlight').forEach((celda) => celda.classList.remove('highlight'));

    let encontrada = false;

    // Busca en celdas principales
    const celdas = document.querySelectorAll('#inventario-table-A td');
    celdas.forEach((celda) => {
      if (celda.innerHTML.trim() === this.ubicacion) {
        celda.classList.add('highlight');
        encontrada = true;
      }
    });

    // Busca en subceldas (tablas anidadas)
    if (!encontrada) {
      const subCeldas = document.querySelectorAll('#inventario-table-A .nested-table td');
      subCeldas.forEach((subCelda) => {
        if (subCelda.innerHTML.trim() === this.ubicacion) {
          subCelda.classList.add('highlight');
          encontrada = true;
        }
      });
    }

    if (!encontrada) {
      // alert(`La celda o subcelda ${this.ubicacion} no fue encontrada.`);
    } else {
      // alert(`La celda ${this.ubicacion} fue resaltada.`);
    }
    }
  },
  created() {
    this.getInventario();
  }
}
</script>

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
  text-align: center;
}

th,
td {
  border: 1px solid #000;
  padding: 10px;
}

.highlight {
  background-color: yellow;
  /* Estilo de la celda resaltada */
}
</style>
