<template>
  <div class="home">
    <section class="hero">
      <div class="hero-content">
        <h1>
          Descubra seu futuro com o <span class="gradient-text">OrientAI</span>
        </h1>
        <p>
          IA que entende seu perfil e indica o caminho ideal para sua carreira
        </p>
        <div class="hero-buttons">
          <a href="#" class="btn btn-primary" @click="$emit('iniciar-questionario')">
            Começar Agora
          </a>
          <a href="#" class="btn btn-secondary" @click="rolarParaSecao">
            Ver Como Funciona
          </a>
        </div>
      </div>
    </section>

    <section id="como-funciona" class="section section-white">
      <div class="container">
        <h2 class="section-title">Como Funciona</h2>
        <p class="section-subtitle">
          Em apenas 3 passos simples, nossa IA analisa seu perfil e gera recomendações personalizadas
        </p>
        <div class="cards-grid">
          <div class="card">
            <div class="card-number">1</div>
            <h3>Responda perguntas rápidas</h3>
            <p>Nosso questionário inteligente coleta informações sobre seus interesses, habilidades e objetivos de forma rápida e intuitiva.</p>
          </div>
          <div class="card">
            <div class="card-number">2</div>
            <h3>A IA analisa seu perfil</h3>
            <p>Nossa inteligência artificial processa seus dados usando algoritmos avançados para entender seu perfil único.</p>
          </div>
          <div class="card">
            <div class="card-number">3</div>
            <h3>Receba recomendações personalizadas</h3>
            <p>Obtenha sugestões precisas de cursos e universidades que combinam perfeitamente com seu perfil e aspirações.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="cta">
      <div class="container">
        <h2>Pronto para descobrir seu futuro?</h2>
        <p>Junte-se a nossos estudantes que já encontraram seu caminho com a OrientAI</p>
             <a href="#" class="btn btn-primary" @click="$emit('iniciar-questionario')">
               Começar Agora!
             </a>
      </div>
    </section>

    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-section">
            <h3>OrientAI</h3>
            <p>Plataforma de inteligência artificial que ajuda estudantes a descobrir cursos e faculdades ideais para seu futuro.</p>
          </div>
          <div class="footer-section">
            <h3>Contato</h3>
            <p>orient.ai.behring@gmail.com</p>
            <p>21 989144595</p>
          </div>
        </div>
        <div class="footer-bottom">
          <p>© 2025 OrientAI. Todos os direitos reservados.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import '../styles/home.css'

export default {
  name: 'Home',
  emits: ['iniciar-questionario'],
  methods: {
    rolarParaSecao() {
      const elemento = document.getElementById('como-funciona')
      if (elemento) {
        elemento.scrollIntoView({ behavior: 'smooth' })
      }
    }
  }
}
</script>
