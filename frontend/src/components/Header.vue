<template>
  <header class="header">
    <div class="conteudo-cabecalho">
      <a href="#" class="logo">OrientAI</a>
      <div class="acoes-cabecalho">
        <a href="#" class="btn btn-primary" @click="$emit('iniciar-questionario')">Começar agora</a>
      </div>
    </div>
  </header>
</template>

<script>
import '../styles/header.css'

export default {
  name: 'Header',
  emits: ['iniciar-questionario']
}
</script>
