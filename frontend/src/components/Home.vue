<template>
  <div class="home">
    <section class="hero">
      <div class="conteudo-hero">
        <h1>
          Descubra seu futuro com o <span class="gradient-text">OrientAI</span>
        </h1>
        <p>
          IA que entende seu perfil e indica o caminho ideal para sua carreira
        </p>
        <div class="botoes-hero">
          <a href="#" class="btn btn-primary" @click="$emit('iniciar-questionario')">
            Começar Agora
          </a>
          <a href="#" class="btn btn-secondary" @click="rolarParaSecao">
            Ver Como Funciona
          </a>
        </div>
      </div>
    </section>

    <section id="como-funciona" class="secao secao-branca">
      <div class="container">
        <h2 class="titulo-secao">Como Funciona</h2>
        <p class="subtitulo-secao">
          Em apenas 3 passos simples, nossa IA analisa seu perfil e gera recomendações personalizadas
        </p>
        <div class="grade-cards">
          <div class="card">
            <div class="numero-card">1</div>
            <h3>Responda perguntas rápidas</h3>
            <p>Nosso questionário inteligente coleta informações sobre seus interesses, habilidades e objetivos de forma rápida e intuitiva.</p>
          </div>
          <div class="card">
            <div class="numero-card">2</div>
            <h3>A IA analisa seu perfil</h3>
            <p>Nossa inteligência artificial processa seus dados usando algoritmos avançados para entender seu perfil único.</p>
          </div>
          <div class="card">
            <div class="numero-card">3</div>
            <h3>Receba recomendações personalizadas</h3>
            <p>Obtenha sugestões precisas de cursos e universidades que combinam perfeitamente com seu perfil e aspirações.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="chamada-acao">
      <div class="container">
        <h2>Pronto para descobrir seu futuro?</h2>
        <p>Junte-se a nossos estudantes que já encontraram seu caminho com o OrientAI</p>
             <a href="#" class="btn btn-primary" @click="$emit('iniciar-questionario')">
               Começar Agora!
             </a>
      </div>
    </section>

    <footer class="rodape">
      <div class="container">
        <div class="conteudo-rodape">
          <div class="secao-rodape">
            <h3>OrientAI</h3>
            <p>Plataforma de inteligência artificial que ajuda estudantes a descobrir cursos e faculdades ideais para seu futuro.</p>
          </div>
          <div class="secao-rodape">
            <h3>Contato</h3>
            <p>orient.ai.behring@gmail.com</p>
            <p>21 989144595</p>
          </div>
        </div>
        <div class="rodape-inferior">
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
