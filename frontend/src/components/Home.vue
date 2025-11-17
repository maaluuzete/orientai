<template>
  <div class="home">
    <section class="hero">
      <div class="conteudo-hero">
        <h1>
          Descubra seu futuro com <br> <span class="gradient-text">OrientAI</span>
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

    <section class="secao-equipe secao" id="equipe">
      <div class="container">
        <h2 class="titulo-secao">Nossa Equipe</h2>
        <p class="subtitulo-secao">
          Conheça o time por trás do OrientAI
        </p>

        <div class="grade-equipe">
          <div class="flip-card">
            <div class="flip-card-inner">
              <div class="flip-card-front">
                <div class="foto-equipe">
                  <img src="../assets/malu.jpeg" >
                </div>
                <p class="frase-equipe">
                  Malu Araujo<br>
                  Back-end Developer  </p>
              </div>
              <div class="flip-card-back">
                <p class="texto-equipe">
                  Malu Azevedo
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam ex velit soluta mollitia impedit fugiat, tempora, earum officiis eligendi recusandae beatae, ad alias! Dolores iure asperiores quasi voluptas error nihil..
                </p>
              </div>
            </div>
          </div>

          <div class="flip-card">
            <div class="flip-card-inner">
              <div class="flip-card-front">
                <div class="foto-equipe">
                  <img src="../assets/marcos.jpeg" alt="Membro da equipe">
                </div>
                <p class="frase-equipe">
                  Marcos Vinicio<br>
                  Front-end Developer</p>
              </div>
              <div class="flip-card-back">
                <p class="texto-equipe">
                  Marcos Vinicio<br>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam ex velit soluta mollitia impedit fugiat, tempora, earum officiis eligendi recusandae beatae, ad alias! Dolores iure asperiores quasi voluptas error nihil..
                </p>
              </div>
            </div>
          </div>

          <div class="flip-card">
            <div class="flip-card-inner">
              <div class="flip-card-front">
                <div class="foto-equipe">
                  <img src="../assets/sabrina.jpeg" alt="Membro da equipe">
                </div>
                  <p class="frase-equipe">
                    Sabrina Paszko<br>
                    AI Engineer</p>
              </div>
              <div class="flip-card-back">
                <p class="texto-equipe">
                  Sabrina Paszko<br><br>
                  Gosto de arte, livros de fantasia, Marvel, Arctic Monkeys e comédias românticas. 
                    Acredito no poder da IA para transformar a educação — e naquela felicidade quase mística quando um pipeline roda de primeira.
Atuei na concepção, arquitetura e fluxo do sistema, implementei a camada de IA, defini a stack, contribuí para integrações e deploys da OrientAI e ajudei a organizar tarefas e cronogramas para a equipe.
                </p>
              </div>
            </div>
          </div>

          <div class="flip-card">
            <div class="flip-card-inner">
              <div class="flip-card-front">
                <div class="foto-equipe">
                  <img src="../assets/vini.jpeg" alt="Membro da equipe">
                </div>
                <p class="frase-equipe">
                  Vinicius Knop<br>
                  Data Engineer</p>
              </div>
              <div class="flip-card-back">
                <p class="texto-equipe">
                  Vinicius Knop<br>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam ex velit soluta mollitia impedit fugiat, tempora, earum officiis eligendi recusandae beatae, ad alias! Dolores iure asperiores quasi voluptas error nihil..
                </p>
              </div>
            </div>
          </div>

        
        </div>

        

      </div>
    </section>

    <section class="chamada-acao secao">
      <div class="container">
        <h2>Pronto para descobrir seu futuro?</h2>
        <p>Junte-se a nossos estudantes que já encontraram seu caminho com o OrientAI</p>
             <a href="#" class="btn btn-primary" @click="$emit('iniciar-questionario')">
               Começar Agora!
             </a>
      </div>
    </section>

    <footer class="rodape">
      <div class="container" id="contato">
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
          <p>©2025 OrientAI. Todos os direitos reservados.</p>
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
