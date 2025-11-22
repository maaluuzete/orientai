<template>
  <div class="results">
    <div class="container">
      <h1>Suas Recomendações</h1>
      
      <div class="recommendation-card">
        <h2>{{ recomendacao.curso }}</h2>
        <div class="area">{{ recomendacao.area }}</div>
        <div class="explanation">{{ recomendacao.explicacao }}</div>
      </div>
      
      <div class="actions">
        <button @click="$emit('reiniciar')" class="btn">
          Fazer Novo Teste
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import '../styles/results.css'

export default {
  name: 'Results',
  props: {
    recomendacao: {
      type: Object,
      required: true
    }
  },
  emits: ['reiniciar']
}
</script>

