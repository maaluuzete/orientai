<template>
  <div id="app">
    <Header v-if="paginaAtual == 'home'"  @iniciar-questionario="irParaFormulario" />
    <main>
      <Home v-if="paginaAtual === 'home'" @iniciar-questionario="irParaFormulario" />
      <Form v-if="paginaAtual === 'formulario'" @enviar-formulario="processarEnvio" @voltar="irParaHome" />
      <Results v-if="paginaAtual === 'resultados'" :recomendacao="recomendacao" @reiniciar="irParaHome" />
    </main>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Home from './components/Home.vue'
import Form from './components/Form.vue'
import Results from './components/Results.vue'

export default {
  name: 'App',
  components: {
    Header,
    Home,
    Form,
    Results
    //Results
  },
  data() {
    return {
      paginaAtual: 'home',
      recomendacao: null
    }
  },
  methods: {
    irParaFormulario() {
      this.paginaAtual = 'formulario'
    },
    processarEnvio(dadosFormulario) {
      this.recomendacao = {
        curso: 'Engenharia de Computação',
        area: 'Exatas / Tecnologia',
        explicacao: 'Você se destaca em matemática e lógica, gosta de programação e resolução de problemas complexos. Suas habilidades analíticas e interesse em tecnologia fazem de você um candidato ideal para esta área.'
      }
      this.paginaAtual = 'resultados'
    }
  }
}
</script>
