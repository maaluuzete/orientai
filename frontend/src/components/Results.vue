<template>
  <div class="results">
    <div class="container">
      <h1>Suas Recomendações</h1>
        <div v-for="(rec, index) in recomendacao.recommendations" :key="index" class="recommendation-card">
          <h2>{{rec.course}}</h2>
          <div class="area">{{rec.area}}</div>
          <div class="explanation">{{rec.reason}}</div>
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

