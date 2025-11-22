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
      recomendacao: null,
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
    processarEnvio() {
      this.recomendacao = {
        curso: 'Engenharia de Computação',
        area: 'Exatas / Tecnologia',
        explicacao: 'Você se destaca em matemática e lógica, gosta de programação e resolução de problemas complexos. Suas habilidades analíticas e interesse em tecnologia fazem de você um candidato ideal para esta área.'
      }
      this.loading = true
      setTimeout(() => {
        this.loading = false
      }, 4000);
      this.paginaAtual = 'resultados'
    }
  }
}
</script>
