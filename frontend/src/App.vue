<template>
  <div id="app">
    <Header v-if="paginaAtual === 'home'" />
    <main>
      <Home v-if="paginaAtual === 'home'" @iniciar-questionario="irParaFormulario" />
      <Form v-if="paginaAtual === 'formulario'" @enviar-formulario="processarEnvio" @voltar="irParaHome" />
      <Results v-if="paginaAtual === 'resultados'" :recomendacao="recomendacao" @reiniciar="irParaHome" />
      <Loading v-if="loading" />
    </main>
  </div>
</template>

<script>
import axios from 'axios'
import Header from './components/Header.vue'
import Home from './components/Home.vue'
import Form from './components/Form.vue'
import Results from './components/Results.vue'
import Loading from './components/Loading.vue'

export default {
  name: 'App',
  components: {
    Header,
    Home,
    Form,
    Results,
    Loading
  },
  data() {
    return {
      paginaAtual: 'home',
      recomendacao: {recommendations: []},
      loading: false
    }
  },
  methods: {
    irParaFormulario() {
      this.paginaAtual = 'formulario'
    },
    irParaHome() {
      this.paginaAtual = 'home'
    },
    async processarEnvio(dadosFormulario) {
      this.loading = true;
      const API_RENDER = "https://orientaibackend.onrender.com";
      try{
        const resposta = await axios.post(`${API_RENDER}/api/recommend`, dadosFormulario,
      {
        headers:{
          "Content-Type": "application/json"
        }
      }
    );
      console.log("Resposta do Backend:", resposta.data);
      this.recomendacao = {
          recommendations: resposta.data.recommendations ?? []
      };
      this.paginaAtual = 'resultados';
      }catch (erro){
        console.error("Erro ao enviar dados:", erro);
        this.recomendacao={
          recommendations:[
            {
              course: "Erro",
              area: "---",
              reason: "Não foi possível conectar ao servidor."
            }
          ]
        };
        this.paginaAtual = 'resultados';
  }
  this.loading = false;
    }
  }
}
</script>
