const mockProjetosAluno = [
  { id:1, titulo:'Sistema de Gestão Escolar',        curso:'Análise e Desenvolvimento de Sistemas', tema:'ODS 4 - Educação de Qualidade',        ano:2026, data:'15/03/2026', status:'Aprovado',  desc:'Plataforma web para gestão completa de atividades escolares, incluindo controle de alunos, professores, notas e frequência.' },
  { id:2, titulo:'App de Sustentabilidade Urbana',   curso:'Análise e Desenvolvimento de Sistemas', tema:'ODS 11 - Cidades Sustentáveis',         ano:2026, data:'10/04/2026', status:'Pendente',  desc:'Aplicativo mobile para monitoramento de indicadores de sustentabilidade urbana.' },
  { id:3, titulo:'Dashboard de Métricas ESG',        curso:'Análise e Desenvolvimento de Sistemas', tema:'ESG - Governança',                      ano:2026, data:'05/04/2026', status:'Aprovado',  desc:'Sistema de visualização de indicadores ESG empresariais com dashboards interativos.' },
  { id:4, titulo:'Plataforma de Economia Circular',  curso:'Jogos Digitais',                        tema:'ESG - Ambiental',                      ano:2026, data:'28/03/2026', status:'Aprovado',  desc:'Marketplace digital que conecta empresas interessadas em práticas de economia circular.' },
  { id:5, titulo:'Sistema de Gestão de Resíduos',    curso:'Análise e Desenvolvimento de Sistemas', tema:'ODS 12 - Consumo Responsável',          ano:2025, data:'20/11/2025', status:'Aprovado',  desc:'Aplicação para monitoramento e gestão de coleta seletiva em condomínios residenciais.' },
  { id:6, titulo:'App de Inclusão Digital',          curso:'Jogos Digitais',                        tema:'ODS 10 - Redução de Desigualdades',     ano:2025, data:'15/10/2025', status:'Aprovado',  desc:'Plataforma educacional para ensino de tecnologia básica a comunidades de baixa renda.' },
  { id:7, titulo:'Portal de Transparência',          curso:'Análise e Desenvolvimento de Sistemas', tema:'ESG - Social',                          ano:2025, data:'08/09/2025', status:'Rejeitado', desc:'Portal de acesso público a relatórios de transparência corporativa.' },
  { id:8, titulo:'Sistema de Energia Renovável',     curso:'Análise e Desenvolvimento de Sistemas', tema:'ODS 7 - Energia Limpa',                 ano:2025, data:'25/08/2025', status:'Aprovado',  desc:'Software para monitoramento de painéis solares e otimização do consumo energético.' },
];

const mockExplorar = [
  { titulo:'Sistema de Gestão Escolar',       autor:'Maria Santos',    curso:'Análise e Desenvolvimento de Sistemas', tema:'ODS 4 - Educação de Qualidade',        techs:['React','Node.js','PostgreSQL'], ano:2026, views:342 },
  { titulo:'EcoQuest: Jogo Educativo Ambiental', autor:'Pedro Oliveira', curso:'Jogos Digitais',                     tema:'ODS 13 - Ação Contra a Mudança do Clima', techs:['Unity','C#','Blender'],       ano:2026, views:528 },
  { titulo:'App de Sustentabilidade Urbana',  autor:'Ana Costa',       curso:'Análise e Desenvolvimento de Sistemas', tema:'ODS 11 - Cidades Sustentáveis',        techs:['React Native','Firebase','Python'], ano:2026, views:215 },
  { titulo:'Plataforma de Economia Circular', autor:'Carlos Mendes',   curso:'Análise e Desenvolvimento de Sistemas', tema:'ESG - Ambiental',                      techs:['Vue.js','Django','MongoDB'],   ano:2025, views:412 },
  { titulo:'RPG Narrativo: Vozes da Inclusão',autor:'Juliana Ferreira',curso:'Jogos Digitais',                       tema:'ODS 10 - Redução de Desigualdades',     techs:['Unreal Engine','C++','Substance Painter'], ano:2026, views:691 },
  { titulo:'Dashboard de Métricas ESG',       autor:'Roberto Lima',    curso:'Análise e Desenvolvimento de Sistemas', tema:'ESG - Governança',                     techs:['Angular','Express','MySQL'],   ano:2026, views:289 },
  { titulo:'Sistema de Energia Solar',        autor:'Fernanda Souza',  curso:'Análise e Desenvolvimento de Sistemas', tema:'ODS 7 - Energia Limpa',                techs:['Python','Django','Chart.js'],  ano:2025, views:374 },
  { titulo:'Plataforma de Educação Inclusiva',autor:'Rafael Santos',   curso:'Análise e Desenvolvimento de Sistemas', tema:'ODS 10 - Redução de Desigualdades',   techs:['Next.js','PostgreSQL'],        ano:2026, views:445 },
];

function statusBadge(s) {
  const map = { 'Aprovado':'badge-green','Pendente':'badge-orange','Rejeitado':'badge-red' };
  return `<span class="badge ${map[s]||'badge-gray'}">${s}</span>`;
}

function alunoNav(section, el) {
  document.querySelectorAll('#page-aluno .nav-item').forEach(n => n.classList.remove('active'));
  if (el) el.classList.add('active');
  document.querySelectorAll('#page-aluno .subpage').forEach(s => s.classList.remove('active'));
  document.getElementById(`aluno-${section}`).classList.add('active');
  if (section === 'explorar') renderExplorar();
}

function abrirEditar(id) {
  const p = mockProjetosAluno.find(x => x.id === id);
  if (!p) return;
  document.getElementById('edit-titulo').value = p.titulo;
  document.getElementById('edit-curso').value  = p.curso;
  document.getElementById('edit-tema').value   = p.tema;
  document.getElementById('edit-ano').value    = p.ano;
  document.getElementById('edit-data').value   = p.data;
  document.getElementById('edit-status-badge').innerHTML = statusBadge(p.status);
  alunoNav('editar-projeto', null);
}

function renderAluno() {
  const recentes = mockProjetosAluno.slice(0, 4);
  document.getElementById('aluno-projetos-recentes').innerHTML = recentes.map(p => `
    <div class="project-item">
      <div class="project-item-info">
        <div class="proj-title">${p.titulo}</div>
        <div class="proj-sub">${p.curso}</div>
      </div>
      <div class="project-item-meta">
        <span class="project-date">${p.data}</span>
        ${statusBadge(p.status)}
      </div>
    </div>`).join('');

  document.getElementById('aluno-projetos-table').innerHTML = mockProjetosAluno.map(p => `
    <tr>
      <td>${p.titulo}</td>
      <td style="color:var(--gray-500);font-weight:400;">${p.curso}</td>
      <td style="color:var(--gray-500);font-weight:400;">${p.tema}</td>
      <td style="color:var(--gray-500);font-weight:400;">${p.ano}</td>
      <td style="color:var(--gray-500);font-weight:400;">${p.data}</td>
      <td>${statusBadge(p.status)}</td>
      <td><span class="text-link" onclick="abrirEditar(${p.id})">Editar</span></td>
    </tr>`).join('');

  const aprovados = mockProjetosAluno.filter(p => p.status === 'Aprovado');
  document.getElementById('portfolio-projects-list').innerHTML = aprovados.map(p => `
    <div class="portfolio-card">
      <div class="portfolio-card-title">${p.titulo}</div>
      <div class="portfolio-card-desc">${p.desc}</div>
      <div class="portfolio-card-meta">
        <span class="badge badge-blue" style="font-size:11px;">${p.tema}</span>
        <span>Ano: ${p.ano}</span><span>•</span>
        <span>${Math.floor(Math.random()*200)+50} visualizações</span>
        <span>•</span><span>${p.data}</span>
      </div>
    </div>`).join('');
}

function renderExplorar() {
  const q = (document.getElementById('explorar-search')?.value || '').toLowerCase();
  const filtered = mockExplorar.filter(p =>
    !q || p.titulo.toLowerCase().includes(q) || p.autor.toLowerCase().includes(q) ||
    p.techs.some(t => t.toLowerCase().includes(q))
  );
  document.getElementById('explorar-count').textContent = `${filtered.length} projeto${filtered.length !== 1 ? 's' : ''} encontrado${filtered.length !== 1 ? 's' : ''}`;
  document.getElementById('explorar-table').innerHTML = filtered.map(p => {
    const tags = p.techs.slice(0,2).map(t => `<span class="tech-tag">${t}</span>`).join('') +
      (p.techs.length > 2 ? `<span class="tech-tag">+${p.techs.length - 2}</span>` : '');
    return `<tr>
      <td>
        <div class="explorar-proj-cell">
          <div class="explorar-proj-icon"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div>
          <div>
            <div class="explorar-proj-title">${p.titulo}</div>
            <div style="font-size:11px;color:var(--gray-400);">${p.curso}</div>
          </div>
        </div>
      </td>
      <td style="font-weight:400;color:var(--gray-700);">${p.autor}<br><span style="font-size:11px;color:var(--gray-400);">${p.curso}</span></td>
      <td><span class="badge badge-blue" style="font-size:11px;white-space:nowrap;">${p.tema.length > 28 ? p.tema.substring(0,28)+'…' : p.tema}</span></td>
      <td>${tags}</td>
      <td style="color:var(--gray-500);font-weight:400;">${p.ano}</td>
      <td style="color:var(--gray-500);font-weight:400;">
        <div style="display:flex;align-items:center;gap:5px;">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
          ${p.views}
        </div>
      </td>
    </tr>`;
  }).join('');
}

function logout() {
  window.location.href = '../index.html';
}

window.onload = function() { renderAluno(); };

lucide.createIcons();