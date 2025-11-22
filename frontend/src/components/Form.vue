<template>
  <div class="form">
    <h1>Questionário de Orientação</h1>
    <p class="subtitulo">Preencha os campos abaixo para receber suas recomendações personalizadas</p>
    
    <form @submit.prevent="enviarFormulario">
      <div class="secao">
        <h2>Dados básicos</h2>
        
        <div class="campo">
          <label>Nome *</label>
          <input type="text" v-model="dadosFormulario.name" required>
        </div>
        
        <div class="campo">
          <label>Idade *</label>
          <input type="number" v-model="dadosFormulario.age" min="13" max="25" required>
        </div>
        
        <div class="campo">
          <label>Ano escolar *</label>
          <select v-model="dadosFormulario.year" required>
            <option value="">Selecione...</option>
            <option value="9º ano do Ensino Fundamental">9º ano do Ensino Fundamental</option>
            <option value="1º ano do Ensino Médio">1º ano do Ensino Médio</option>
            <option value="2º ano do Ensino Médio">2º ano do Ensino Médio</option>
            <option value="3º ano do Ensino Médio">3º ano do Ensino Médio</option>
          </select>
        </div>
        
        <div class="campo">
          <label>Cidade *</label>
          <input type="text" v-model="dadosFormulario.city" required>
        </div>
        
        <div class="campo">
          <label>Estado *</label>
          <select v-model="dadosFormulario.state" required>
            <option value="">Selecione...</option>
            <option value="Acre">Acre</option>
            <option value="Alagoas">Alagoas</option>
            <option value="Amapá">Amapá</option>
            <option value="Amazonas">Amazonas</option>
            <option value="Bahia">Bahia</option>
            <option value="Ceará">Ceará</option>
            <option value="Distrito Federal">Distrito Federal</option>
            <option value="Espírito Santo">Espírito Santo</option>
            <option value="Goiás">Goiás</option>
            <option value="Maranhão">Maranhão</option>
            <option value="Mato Grosso">Mato Grosso</option>
            <option value="Mato Grosso do Sul">Mato Grosso do Sul</option>
            <option value="Minas Gerais">Minas Gerais</option>
            <option value="Pará">Pará</option>
            <option value="Paraíba">Paraíba</option>
            <option value="Paraná">Paraná</option>
            <option value="Pernambuco">Pernambuco</option>
            <option value="Piauí">Piauí</option>
            <option value="Rio de Janeiro">Rio de Janeiro</option>
            <option value="Rio Grande do Norte">Rio Grande do Norte</option>
            <option value="Rio Grande do Sul">Rio Grande do Sul</option>
            <option value="Rondônia">Rondônia</option>
            <option value="Roraima">Roraima</option>
            <option value="Santa Catarina">Santa Catarina</option>
            <option value="São Paulo">São Paulo</option>
            <option value="Sergipe">Sergipe</option>
            <option value="Tocantins">Tocantins</option>
          </select>
        </div>
        
        <div class="campo">
          <label>País *</label>
          <input type="text" v-model="dadosFormulario.country" required>
        </div>
      </div>

      <div class="secao">
        <h2>Interesses e preferências</h2>
        
        <div class="campo">
          <label>Áreas de interesse acadêmico *</label>
          <div class="checkboxes">
            <label class="checkbox-item" :class="{ checked: dadosFormulario.interest_areas.includes('Exatas') }">
              <input type="checkbox" value="Exatas" v-model="dadosFormulario.interest_areas">
              <span class="checkbox-custom"></span>
              <span>Exatas</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.interest_areas.includes('Humanas') }">
              <input type="checkbox" value="Humanas" v-model="dadosFormulario.interest_areas">
              <span class="checkbox-custom"></span>
              <span>Humanas</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.interest_areas.includes('Biológicas') }">
              <input type="checkbox" value="Biológicas" v-model="dadosFormulario.interest_areas">
              <span class="checkbox-custom"></span>
              <span>Biológicas</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.interest_areas.includes('Artes') }">
              <input type="checkbox" value="Artes" v-model="dadosFormulario.interest_areas">
              <span class="checkbox-custom"></span>
              <span>Artes</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.interest_areas.includes('Tecnologia') }">
              <input type="checkbox" value="Tecnologia" v-model="dadosFormulario.interest_areas">
              <span class="checkbox-custom"></span>
              <span>Tecnologia</span>
            </label>
          </div>
        </div>
        
        <div class="campo">
          <label>Matérias favoritas *</label>
          <div class="checkboxes">
            <label class="checkbox-item" :class="{ checked: dadosFormulario.favorite_subjects.includes('Matemática') }">
              <input type="checkbox" value="Matemática" v-model="dadosFormulario.favorite_subjects">
              <span class="checkbox-custom"></span>
              <span>Matemática</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.favorite_subjects.includes('Física') }">
              <input type="checkbox" value="Física" v-model="dadosFormulario.favorite_subjects">
              <span class="checkbox-custom"></span>
              <span>Física</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.favorite_subjects.includes('Química') }">
              <input type="checkbox" value="Química" v-model="dadosFormulario.favorite_subjects">
              <span class="checkbox-custom"></span>
              <span>Química</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.favorite_subjects.includes('Biologia') }">
              <input type="checkbox" value="Biologia" v-model="dadosFormulario.favorite_subjects">
              <span class="checkbox-custom"></span>
              <span>Biologia</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.favorite_subjects.includes('História') }">
              <input type="checkbox" value="História" v-model="dadosFormulario.favorite_subjects">
              <span class="checkbox-custom"></span>
              <span>História</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.favorite_subjects.includes('Geografia') }">
              <input type="checkbox" value="Geografia" v-model="dadosFormulario.favorite_subjects">
              <span class="checkbox-custom"></span>
              <span>Geografia</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.favorite_subjects.includes('Português') }">
              <input type="checkbox" value="Português" v-model="dadosFormulario.favorite_subjects">
              <span class="checkbox-custom"></span>
              <span>Português</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.favorite_subjects.includes('Inglês') }">
              <input type="checkbox" value="Inglês" v-model="dadosFormulario.favorite_subjects">
              <span class="checkbox-custom"></span>
              <span>Inglês</span>
            </label>
          </div>
        </div>
        
        <div class="campo">
          <label>Matérias menos favoritas*</label>
          <div class="checkboxes">
            <label class="checkbox-item" :class="{ checked: dadosFormulario.least_subjects.includes('Química') }">
              <input type="checkbox" value="Química" v-model="dadosFormulario.least_subjects">
              <span class="checkbox-custom"></span>
              <span>Química</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.least_subjects.includes('Geografia') }">
              <input type="checkbox" value="Geografia" v-model="dadosFormulario.least_subjects">
              <span class="checkbox-custom"></span>
              <span>Geografia</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.least_subjects.includes('Matemática') }">
              <input type="checkbox" value="Matemática" v-model="dadosFormulario.least_subjects">
              <span class="checkbox-custom"></span>
              <span>Matemática</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.least_subjects.includes('Física') }">
              <input type="checkbox" value="Física" v-model="dadosFormulario.least_subjects">
              <span class="checkbox-custom"></span>
              <span>Física</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.least_subjects.includes('Biologia') }">
              <input type="checkbox" value="Biologia" v-model="dadosFormulario.least_subjects">
              <span class="checkbox-custom"></span>
              <span>Biologia</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.least_subjects.includes('História') }">
              <input type="checkbox" value="História" v-model="dadosFormulario.least_subjects">
              <span class="checkbox-custom"></span>
              <span>História</span>
            </label>
          </div>
        </div>
        
        <div class="campo">
          <label>Hobbies / atividades extracurriculares</label>
          <textarea v-model="dadosFormulario.hobbies" placeholder="Praticar esportes, ler livros e etc..."></textarea>
        </div>
      </div>

      <div class="secao">
        <h2>Desempenho e habilidades</h2>
        
        <div class="campo">
          <label>Pontos fortes *</label>
          <div class="checkboxes">
            <label class="checkbox-item" :class="{ checked: dadosFormulario.strengths.includes('Raciocínio lógico') }">
              <input type="checkbox" value="Raciocínio lógico" v-model="dadosFormulario.strengths">
              <span class="checkbox-custom"></span>
              <span>Raciocínio lógico</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.strengths.includes('Criatividade') }">
              <input type="checkbox" value="Criatividade" v-model="dadosFormulario.strengths">
              <span class="checkbox-custom"></span>
              <span>Criatividade</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.strengths.includes('Escrita') }">
              <input type="checkbox" value="Escrita" v-model="dadosFormulario.strengths">
              <span class="checkbox-custom"></span>
              <span>Escrita</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.strengths.includes('Comunicação') }">
              <input type="checkbox" value="Comunicação" v-model="dadosFormulario.strengths">
              <span class="checkbox-custom"></span>
              <span>Comunicação</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.strengths.includes('Organização') }">
              <input type="checkbox" value="Organização" v-model="dadosFormulario.strengths">
              <span class="checkbox-custom"></span>
              <span>Organização</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.strengths.includes('Liderança') }">
              <input type="checkbox" value="Liderança" v-model="dadosFormulario.strengths">
              <span class="checkbox-custom"></span>
              <span>Liderança</span>
            </label>
          </div>
        </div>
        
        <div class="campo">
          <label>Pontos a melhorar</label>
          <div class="checkboxes">
            <label class="checkbox-item" :class="{ checked: dadosFormulario.improvements.includes('Escrita') }">
              <input type="checkbox" value="Escrita" v-model="dadosFormulario.improvements">
              <span class="checkbox-custom"></span>
              <span>Escrita</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.improvements.includes('Memorização') }">
              <input type="checkbox" value="Memorização" v-model="dadosFormulario.improvements">
              <span class="checkbox-custom"></span>
              <span>Memorização</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.improvements.includes('Organização') }">
              <input type="checkbox" value="Organização" v-model="dadosFormulario.improvements">
              <span class="checkbox-custom"></span>
              <span>Organização</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.improvements.includes('Concentração') }">
              <input type="checkbox" value="Concentração" v-model="dadosFormulario.improvements">
              <span class="checkbox-custom"></span>
              <span>Concentração</span>
            </label>
            <label class="checkbox-item" :class="{ checked: dadosFormulario.improvements.includes('Matemática') }">
              <input type="checkbox" value="Matemática" v-model="dadosFormulario.improvements">
              <span class="checkbox-custom"></span>
              <span>Matemática</span>
            </label>
          </div>
        </div>
      </div>

      <div class="secao">
        <h2>Objetivos e estilo de aprendizado</h2>
        
        <div class="campo">
          <label>Preferência por modalidade de estudo *</label>
          <div class="radios">
            <label class="radio-item" :class="{ checked: dadosFormulario.study_modality === 'Presencial' }">
              <input type="radio" value="Presencial" v-model="dadosFormulario.study_modality">
              <span class="radio-custom"></span>
              <span>Presencial</span>
            </label>
            <label class="radio-item" :class="{ checked: dadosFormulario.study_modality === 'Online' }">
              <input type="radio" value="Online" v-model="dadosFormulario.study_modality">
              <span class="radio-custom"></span>
              <span>Online</span>
            </label>
            <label class="radio-item" :class="{ checked: dadosFormulario.study_modality === 'Híbrido' }">
              <input type="radio" value="Híbrido" v-model="dadosFormulario.study_modality">
              <span class="radio-custom"></span>
              <span>Híbrido</span>
            </label>
          </div>
        </div>
        
        <div class="campo">
          <label>Objetivos de carreira / curso dos sonhos</label>
          <textarea v-model="dadosFormulario.dream_course" placeholder="Descreva seus objetivos profissionais!"></textarea>
        </div>
      </div>

      <div class="secao">
        <h2>Perfil de personalidade</h2>
        
        <div class="campo">
          <label>Prefere trabalhar sozinho ou em equipe? *</label>
          <div class="radios">
            <label class="radio-item" :class="{ checked: dadosFormulario.team_pref === 'Trabalho em equipe' }">
              <input type="radio" value="Trabalho em equipe" v-model="dadosFormulario.team_pref">
              <span class="radio-custom"></span>
              <span>Trabalho em equipe</span>
            </label>
            <label class="radio-item" :class="{ checked: dadosFormulario.team_pref === 'Trabalho sozinho' }">
              <input type="radio" value="Trabalho sozinho" v-model="dadosFormulario.team_pref">
              <span class="radio-custom"></span>
              <span>Trabalho sozinho</span>
            </label>
          </div>
        </div>
        
        <div class="campo">
          <label>Estilo de trabalho *</label>
          <div class="radios">
            <label class="radio-item" :class="{ checked: dadosFormulario.work_style === 'Trabalho presencial' }">
              <input type="radio" value="Trabalho presencial" v-model="dadosFormulario.work_style">
              <span class="radio-custom"></span>
              <span>Trabalho presencial</span>
            </label>
            <label class="radio-item" :class="{ checked: dadosFormulario.work_style === 'Trabalho remoto' }">
              <input type="radio" value="Trabalho remoto" v-model="dadosFormulario.work_style">
              <span class="radio-custom"></span>
              <span>Trabalho remoto</span>
            </label>
            <label class="radio-item" :class="{ checked: dadosFormulario.work_style === 'Trabalho híbrido' }">
              <input type="radio" value="Trabalho híbrido" v-model="dadosFormulario.work_style">
              <span class="radio-custom"></span>
              <span>Trabalho híbrido</span>
            </label>
          </div>
        </div>
        
        <div class="campo">
          <label>Tolerância a desafios* <br><br> 1 = Não gosto de desafios <br>5 = Gosto de desafios complexos</label>
          <div class="radio-input-1">
            <label>
              <input value="1" name="challenge-radio" id="challenge-1" type="radio" v-model="dadosFormulario.challenge_tolerance">
              <span>1</span>
            </label>
            <label>
              <input value="2" name="challenge-radio" id="challenge-2" type="radio" v-model="dadosFormulario.challenge_tolerance">
              <span>2</span>
            </label>
            <label>
              <input value="3" name="challenge-radio" id="challenge-3" type="radio" v-model="dadosFormulario.challenge_tolerance">
              <span>3</span>
            </label>
            <label>
              <input value="4" name="challenge-radio" id="challenge-4" type="radio" v-model="dadosFormulario.challenge_tolerance">
              <span>4</span>
            </label>
            <label>
              <input value="5" name="challenge-radio" id="challenge-5" type="radio" v-model="dadosFormulario.challenge_tolerance">
              <span>5</span>
            </label>
            <span class="selection"></span>
          </div>
        </div>

        
        <div class="campo">
          <label>Preferência por rotina * <br><br> 1 = Rotina flexível <br> 5 = Rotina estruturada</label>
          <div class="radio-input">
            <label>
              <input value="1" name="routine-radio" id="routine-1" type="radio" v-model="dadosFormulario.routine_preference">
              <span>1</span>
            </label>
            <label>
              <input value="2" name="routine-radio" id="routine-2" type="radio" v-model="dadosFormulario.routine_preference">
              <span>2</span>
            </label>
            <label>
              <input value="3" name="routine-radio" id="routine-3" type="radio" v-model="dadosFormulario.routine_preference">
              <span>3</span>
            </label>
            <label>
              <input value="4" name="routine-radio" id="routine-4" type="radio" v-model="dadosFormulario.routine_preference">
              <span>4</span>
            </label>
            <label>
              <input value="5" name="routine-radio" id="routine-5" type="radio" v-model="dadosFormulario.routine_preference">
              <span>5</span>
            </label>
            <span class="selection"></span>
          </div>
        </div>
      </div>

      <div class="botoes">
        <button class="btn-voltar" type="button" @click="$emit('voltar')">Voltar</button>
        <button class="btn-gerar" type="submit" @click="enviarFormulario">Gerar Recomendações</button>
      </div>
    </form>
  </div>
</template>

<script>
import '../styles/form.css'

export default {
  name: 'Form',
  emits: ['enviar-formulario', 'voltar'],
  data() {
    return {
      dadosFormulario: {
        name: '',
        age: '',
        year: '',
        city: '',
        state: '',
        country: '',
        interest_areas: [],
        favorite_subjects: [],
        least_subjects: [],
        hobbies: '',
        strengths: [],
        improvements: [],
        study_modality: '',
        dream_course: '',
        team_pref: '',
        work_style: '',
        challenge_tolerance: 3,
        routine_preference: 3
      }
    }
  },
  methods: {
    enviarFormulario() {
      if (!this.dadosFormulario.name || !this.dadosFormulario.age || !this.dadosFormulario.year || 
          !this.dadosFormulario.city || !this.dadosFormulario.state || !this.dadosFormulario.country ||
          this.dadosFormulario.interest_areas.length === 0 || this.dadosFormulario.favorite_subjects.length === 0 ||
          this.dadosFormulario.strengths.length === 0 || !this.dadosFormulario.study_modality ||
          !this.dadosFormulario.team_pref || !this.dadosFormulario.work_style) {
        alert('Preencha todos os campos obrigatorios *');
        return;
      }
      
      this.$emit('enviar-formulario', this.dadosFormulario);
    }
  }
}
</script>

