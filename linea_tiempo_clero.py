import streamlit as st

st.set_page_config(
    page_title="Línea de tiempo — Abusos del clero",
    layout="wide"
)

html_code = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Línea de tiempo — Abusos del clero (Pantalla completa)</title>
  <style>
    :root{
      --bg:#f7efe6;
      --card:#fffaf4;
      --muted:#6b5a4a;
      --sepia-1:#5b3a29;
      --sepia-2:#8b5a3c;
      --gold:#c59b4b;
      --accent:#a5663b;
      --glass: rgba(255,255,255,0.6);
      --maxh: 88vh;
      font-family: Inter, 'Helvetica Neue', Arial, sans-serif;
    }
    *{box-sizing:border-box}
    html,body{height:100%;margin:0;background:var(--bg);color:var(--sepia-1)}
    .wrap{height:100vh;display:flex;flex-direction:column}
    header{display:flex;align-items:center;justify-content:space-between;padding:22px 36px;border-bottom:1px solid rgba(0,0,0,0.04)}
    header .title{display:flex;gap:18px;align-items:center}
    .logo{width:68px;height:68px;border-radius:10px;background:linear-gradient(135deg,var(--sepia-1),var(--sepia-2));display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;box-shadow:0 8px 20px rgba(91,58,41,0.12)}
    h1{font-size:1.25rem;margin:0;color:var(--sepia-1)}
    .subtitle{color:var(--muted);font-size:0.92rem}
    .viewport{flex:1;display:flex;align-items:center;justify-content:center;padding:30px 24px}
    .timeline-wrap{position:relative;width:95%;height:var(--maxh);background:linear-gradient(180deg, rgba(255,250,245,1), rgba(247,240,232,1));border-radius:18px;box-shadow:0 20px 50px rgba(91,58,41,0.07);overflow:hidden;padding:28px}
    .timeline{display:flex;gap:28px;align-items:stretch;height:100%;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:18px}
    .timeline::-webkit-scrollbar{height:12px}
    .timeline::-webkit-scrollbar-thumb{background:linear-gradient(90deg,var(--sepia-2),var(--gold));border-radius:6px}
    .node{flex:0 0 420px;scroll-snap-align:center;background:var(--card);border-radius:14px;padding:16px;display:flex;flex-direction:column;gap:12px;box-shadow:0 8px 18px rgba(0,0,0,0.06);position:relative;border-top:6px solid var(--accent);transition:transform .28s ease}
    .node:focus-within,.node:hover{transform:translateY(-6px)}
    .media{height:160px;border-radius:10px;overflow:hidden;flex-shrink:0;background:#eee;display:flex;align-items:center;justify-content:center}
    .media img{width:100%;height:100%;object-fit:cover;display:block}
    .date{font-weight:700;color:var(--sepia-1)}
    .role{font-size:0.88rem;color:var(--muted)}
    .text{color:var(--sepia-1);font-size:0.96rem}
    .connector{position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);pointer-events:none}
    .line{position:absolute;left:2%;right:2%;top:50%;height:6px;background:linear-gradient(90deg,var(--sepia-2),var(--gold));border-radius:6px;opacity:0.9}
    .marker{position:absolute;top:50%;width:18px;height:18px;border-radius:50%;transform:translateY(-50%);background:var(--card);border:4px solid var(--accent);box-shadow:0 6px 12px rgba(0,0,0,0.08)}
    @media (max-width:900px){.node{flex:0 0 320px}}
    .panel{position:fixed;right:28px;bottom:28px;background:var(--glass);backdrop-filter:blur(6px);padding:14px 18px;border-radius:12px;border:1px solid rgba(101,77,55,0.08);color:var(--sepia-1)}
    .panel button{background:transparent;border:1px solid rgba(0,0,0,0.06);padding:8px 10px;border-radius:8px;cursor:pointer;color:var(--sepia-1)}
    footer{padding:12px 36px;color:var(--muted);font-size:0.9rem}
    .node{opacity:0;transform:translateY(12px)}
    .node.show{opacity:1;transform:none}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="title">
        <div class="logo">LT</div>
        <div><h1>Histórico de Abuso en el Clero</h1></div>
      </div>
      <nav aria-label="Controles">
        <button id="prev">◀︎ Anterior</button>
        <button id="next">Siguiente ▶︎</button>
      </nav>
    </header>

    <div class="viewport">
      <div class="timeline-wrap" role="region" aria-label="Línea de tiempo horizontal">
        <div class="connector">
          <div class="line"></div>
          <div id="markers"></div>
        </div>
        <div class="timeline" id="timeline">
          <!-- Aquí van tus <article class="node"> ... </article> exactamente igual -->
          🔽 (pega aquí los nodos de eventos que ya tienes)
        </div>
      </div>
    </div>

    <footer>
      Fuente: selección cronológica para fines informativos. Imágenes: Wikimedia Commons (uso ilustrativo).
    </footer>

    <div class="panel" aria-hidden="false">
      <strong>Atajos:</strong> ← →  |  <button id="toStart">Ir al inicio</button>
    </div>
  </div>

  <script>
    const nodes = Array.from(document.querySelectorAll('.node'));
    const timeline = document.getElementById('timeline');
    const revealVisible = ()=>{
      const rect = timeline.getBoundingClientRect();
      nodes.forEach(n=>{
        const r = n.getBoundingClientRect();
        if(r.left < rect.right && r.right > rect.left){ n.classList.add('show'); }
      });
    }
    timeline.addEventListener('scroll', revealVisible);
    window.addEventListener('load', ()=>{
      revealVisible();
      const markers = document.getElementById('markers');
      nodes.forEach(n=>{
        const p = parseFloat(n.dataset.pos);
        const m = document.createElement('div');
        m.className='marker';
        m.style.left = `calc(${p}% - 9px)`;
        markers.appendChild(m);
      });
    });
    document.getElementById('next').addEventListener('click', ()=>{timeline.scrollBy({left:420,behavior:'smooth'});});
    document.getElementById('prev').addEventListener('click', ()=>{timeline.scrollBy({left:-420,behavior:'smooth'});});
    document.getElementById('toStart').addEventListener('click', ()=>{timeline.scrollTo({left:0,behavior:'smooth'});});
    window.addEventListener('keydown', e=>{
      if(e.key === 'ArrowRight') timeline.scrollBy({left:420,behavior:'smooth'});
      if(e.key === 'ArrowLeft') timeline.scrollBy({left:-420,behavior:'smooth'});
    });
  </script>
</body>
</html>
"""

# Mostrar en Streamlit
st.components.v1.html(html_code, height=900, scrolling=True)
