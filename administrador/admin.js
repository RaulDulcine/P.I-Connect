const mockUsuarios = [
  { iniciais:'JS', color:'blue-av',   nome:'João Vitor',      email:'joao.vitor@senac.br',      funcao:'Estudante',     curso:'ADS',            projetos:8  },
  { iniciais:'MS', color:'gray-av',   nome:'Raissa Ferreira', email:'maria.santos@senac.br',    funcao:'Administrador', curso:'-',              projetos:0  },
  { iniciais:'AC', color:'purple-av', nome:'Ana Costa',       email:'ana.costa@senac.br',       funcao:'Estudante',     curso:'ADS',            projetos:5  },
  { iniciais:'CM', color:'orange-av', nome:'Carlos Mendes',   email:'carlos.mendes@senac.br',   funcao:'Professor',     curso:'ADS',            projetos:0  },
  { iniciais:'BL', color:'green-av',  nome:'Beatriz Lima',    email:'beatriz.lima@senac.br',    funcao:'Estudante',     curso:'Jogos Digitais', projetos:12 },
  { iniciais:'RS', color:'blue-av',   nome:'Rafael Santos',   email:'rafael.santos@senac.br',   funcao:'Estudante',     curso:'Jogos Digitais', projetos:3  },
  { iniciais:'JO', color:'purple-av', nome:'Juliana Oliveira',email:'juliana.oliveira@senac.br',funcao:'Estudante',     curso:'ADS',            projetos:7  },
  { iniciais:'PA', color:'orange-av', nome:'Pedro Alves',     email:'pedro.alves@senac.br',     funcao:'Professor',     curso:'Jogos Digitais', projetos:0  },
  { iniciais:'CR', color:'green-av',  nome:'Camila Rocha',    email:'camila.rocha@senac.br',    funcao:'Estudante',     curso:'ADS',            projetos:4  },
  { iniciais:'LF', color:'blue-av',   nome:'Lucas Ferreira',  email:'lucas.ferreira@senac.br',  funcao:'Estudante',     curso:'Jogos Digitais', projetos:1  },
];

const mockProjetos = [
  { titulo:'Sistema de Gestão Escolar',        estudante:'João Vitor',       curso:'ADS',            tema:'ODS 4',           enviado:'15/03/2026', status:'Aprovado'  },
  { titulo:'App de Sustentabilidade Urbana',   estudante:'João Vitor',       curso:'ADS',            tema:'ODS 11',          enviado:'10/04/2026', status:'Pendente'  },
  { titulo:'Dashboard de Métricas ESG',        estudante:'João Vitor',       curso:'ADS',            tema:'ESG - Governança',enviado:'05/04/2026', status:'Aprovado'  },
  { titulo:'Sistema de Reciclagem Inteligente',estudante:'Ana Costa',        curso:'ADS',            tema:'ODS 12',          enviado:'11/04/2026', status:'Pendente'  },
  { titulo:'App de Mobilidade Urbana',         estudante:'Beatriz Lima',     curso:'Jogos Digitais', tema:'ODS 11',          enviado:'08/04/2026', status:'Aprovado'  },
  { titulo:'Sistema de Gestão de Resíduos',    estudante:'Juliana Oliveira', curso:'ADS',            tema:'ODS 12',          enviado:'20/05/2025', status:'Aprovado'  },
  { titulo:'Plataforma de Educação Inclusiva', estudante:'Rafael Santos',    curso:'Jogos Digitais', tema:'ODS 10',          enviado:'12/09/2025', status:'Aprovado'  },
  { titulo:'Sistema de Energia Solar',         estudante:'João Vitor',       curso:'ADS',            tema:'ODS 7',           enviado:'03/11/2025', status:'Aprovado'  },
  { titulo:'Portal de Transparência',          estudante:'Lucas Ferreira',   curso:'Jogos Digitais', tema:'ESG - Social',    enviado:'14/08/2024', status:'Rejeitado' },
  { titulo:'Dashboard de Sustentabilidade',    estudante:'Ana Costa',        curso:'ADS',            tema:'ESG - Ambiental', enviado:'05/11/2024', status:'Aprovado'  },
];

const cursosCiclo = ['Todos os Cursos', 'ADS', 'Jogos Digitais'];
const statusCiclo = ['Todos os Status', 'Aprovado', 'Pendente', 'Rejeitado'];
let cursoIdx = 0, statusIdx = 0;

function funcaoBadge(f) {
  const map = { 'Estudante':'badge-purple', 'Professor':'badge-orange', 'Administrador':'badge-blue' };
  return `<span class="badge ${map[f] || 'badge-gray'}">${f}</span>`;
}

function statusBadge(s) {
  const map = { 'Aprovado':'badge-green', 'Pendente':'badge-orange', 'Rejeitado':'badge-red' };
  return `<span class="badge ${map[s]||'badge-gray'}">${s}</span>`;
}

function projetoAcoes(status) {
  const ver = `<button class="action-btn" title="Ver"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg></button>`;
  const dl  = `<button class="action-btn download" title="Baixar"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg></button>`;
  const apr = `<button class="action-btn approve" title="Aprovar"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></button>`;
  const rej = `<button class="action-btn reject"  title="Rejeitar"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>`;
  return `<div class="action-btn-group">${ver}${dl}${status==='Pendente'?apr+rej:''}</div>`;
}

function logout() {
  window.location.href = '../index.html';
}

function adminNav(section, el) {
  document.querySelectorAll('#page-admin .nav-item').forEach(n => n.classList.remove('active'));
  if (el) el.classList.add('active');
  document.querySelectorAll('#page-admin .subpage').forEach(s => s.classList.remove('active'));
  document.getElementById(`admin-${section}`).classList.add('active');
}

function renderAdmin() {
  const tbody = document.getElementById('admin-usuarios-table');
  if(!tbody) return;
  tbody.innerHTML = mockUsuarios.map(u => `
    <tr>
      <td>
        <div class="user-cell">
          <div class="avatar ${u.color}" style="width:32px;height:32px;font-size:11px;">${u.iniciais}</div>
          <span class="user-name">${u.nome}</span>
        </div>
      </td>
      <td style="color:var(--gray-500);font-weight:400;">${u.email}</td>
      <td>${funcaoBadge(u.funcao)}</td>
      <td style="color:var(--gray-500);font-weight:400;">${u.curso}</td>
      <td style="color:var(--gray-500);font-weight:400;">${u.projetos}</td>
    </tr>`).join('');
}

function cycleProjFilter(type) {
  if (type === 'curso') { 
    cursoIdx = (cursoIdx + 1) % cursosCiclo.length; 
    document.getElementById('filter-curso').textContent = cursosCiclo[cursoIdx]; 
  } else { 
    statusIdx = (statusIdx + 1) % statusCiclo.length; 
    document.getElementById('filter-status').textContent = statusCiclo[statusIdx]; 
  }
  renderProjetos();
}

function renderProjetos() {
  const query  = (document.getElementById('proj-search')?.value||'').toLowerCase();
  const cFilt  = cursosCiclo[cursoIdx];
  const sFilt  = statusCiclo[statusIdx];
  const tbody  = document.getElementById('admin-projetos-table');
  if (!tbody) return;
  
  tbody.innerHTML = mockProjetos
    .filter(p =>
      (!query || p.titulo.toLowerCase().includes(query) || p.estudante.toLowerCase().includes(query)) &&
      (cFilt === 'Todos os Cursos'  || p.curso   === cFilt) &&
      (sFilt === 'Todos os Status'  || p.status  === sFilt)
    )
    .map(p => `<tr>
      <td style="font-weight:600;color:var(--gray-900)">${p.titulo}</td>
      <td style="color:var(--gray-500);font-weight:400">${p.estudante}</td>
      <td style="color:var(--gray-500);font-weight:400">${p.curso}</td>
      <td style="color:var(--gray-500);font-weight:400">${p.tema}</td>
      <td style="color:var(--gray-500);font-weight:400">${p.enviado}</td>
      <td>${statusBadge(p.status)}</td>
      <td>${projetoAcoes(p.status)}</td>
    </tr>`).join('');
}

window.onload = function() {
  renderAdmin();
  renderProjetos();

 lucide.createIcons();
};