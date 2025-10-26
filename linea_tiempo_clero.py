import streamlit as st

# Configuración de página moderna
st.set_page_config(
    page_title="Línea de tiempo — Abusos del clero",
    layout="wide",
)


# Código HTML incrustado
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
      --maxh: 82vh;
      font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    }
    *{box-sizing:border-box}
    html,body{height:100%;margin:0;background:var(--bg);color:var(--sepia-1)}
    .wrap{height:100%;display:flex;flex-direction:column}
    header{display:flex;align-items:center;justify-content:space-between;padding:20px 30px;border-bottom:1px solid rgba(0,0,0,0.04)}
    header .title{display:flex;gap:14px;align-items:center}
    .logo{width:56px;height:56px;border-radius:10px;background:linear-gradient(135deg,var(--sepia-1),var(--sepia-2));display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;box-shadow:0 6px 16px rgba(91,58,41,0.12)}
    h1{font-size:1.2rem;margin:0;color:var(--sepia-1)}
    .viewport{flex:1;display:flex;align-items:center;justify-content:center;padding:20px}
    .timeline-wrap{position:relative;width:95%;height:var(--maxh);background:linear-gradient(180deg, rgba(255,250,245,1), rgba(247,240,232,1));border-radius:16px;box-shadow:0 20px 40px rgba(91,58,41,0.07);overflow:hidden;padding:20px}
    .timeline{display:flex;gap:24px;align-items:stretch;height:100%;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:12px}
    .timeline::-webkit-scrollbar{height:10px}
    .timeline::-webkit-scrollbar-thumb{background:linear-gradient(90deg,var(--sepia-2),var(--gold));border-radius:6px}
    .node{flex:0 0 380px;scroll-snap-align:center;background:var(--card);border-radius:14px;padding:14px;display:flex;flex-direction:column;gap:10px;box-shadow:0 6px 16px rgba(0,0,0,0.06);position:relative;border-top:5px solid var(--accent);transition:transform .25s ease}
    .node:hover{transform:translateY(-6px)}
    .media{height:150px;border-radius:10px;overflow:hidden;flex-shrink:0;background:#eee;display:flex;align-items:center;justify-content:center}
    .media img{width:100%;height:100%;object-fit:cover}
    .date{font-weight:700;color:var(--sepia-1)}
    .role{font-size:0.88rem;color:var(--muted)}
    .text{color:var(--sepia-1);font-size:0.95rem}
    .connector{position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);pointer-events:none}
    .line{position:absolute;left:2%;right:2%;top:50%;height:5px;background:linear-gradient(90deg,var(--sepia-2),var(--gold));border-radius:6px;opacity:0.9}
    .marker{position:absolute;top:50%;width:14px;height:14px;border-radius:50%;transform:translateY(-50%);background:var(--card);border:3px solid var(--accent);box-shadow:0 4px 8px rgba(0,0,0,0.08)}
    footer{padding:10px 30px;color:var(--muted);font-size:0.85rem;text-align:center}
    @media (max-width:900px){.node{flex:0 0 300px}}
    .node{opacity:0;transform:translateY(10px)}
    .node.show{opacity:1;transform:none}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="title">
        <div class="logo">LT</div>
        <div><h1>Histórico de Abusos del Clero</h1></div>
      </div>
      <nav>
        <button id="prev">◀︎</button>
        <button id="next">▶︎</button>
      </nav>
    </header>

    <div class="viewport">
      <div class="timeline-wrap">
        <div class="connector">
          <div class="line"></div>
          <div id="markers"></div>
        </div>
        <div class="timeline" id="timeline">

          <!-- Aquí ya están los eventos ordenados cronológicamente -->
          <article class="node" data-pos="5"><div class="media"><img src="https://brujulacotidiana.com/storage/imgs/san-pier-damiani-large-0-1.jpg"></div><div class="date">Siglo XI</div><div class="role">Pedro Damián — Denuncia</div><div class="text">Escribe <em>Liber Gomorrhianus</em>, denunciando abusos sexuales de clérigos.</div></article>
          <article class="node" data-pos="15"><div class="media"><img src="https://zuercher-museen.ch/media/h1vf1g35/szefue_kvz_gzf-walter-huss_1440.jpg"></div><div class="date">Siglo XV</div><div class="role">Katharina von Zimmern — Caso</div><div class="text">Abusos en abadías; víctimas castigadas, abusadores impunes.</div></article>
          <article class="node" data-pos="25"><div class="media"><img src="https://ambientestereo.fm/sitio/wp-content/uploads/2024/12/Martin-Lutero.jpeg"></div><div class="date">1531</div><div class="role">Martín Lutero — Acusación</div><div class="text">Denuncia corrupción y abusos en la Iglesia Católica.</div></article>
          <article class="node" data-pos="35"><div class="media"><img src="https://fsspx-sudamerica.org/sites/default/files/styles/content_image_16_9_desktop/public/drupal-7/pio12cabezal.jpg"></div><div class="date">1939–1958</div><div class="role">Papa Pío XII — Período</div><div class="text">Encubrimiento de casos, sin protocolos claros.</div></article>
          <article class="node" data-pos="45"><div class="media"><img src="https://cdn.zendalibros.com/wp-content/uploads/2023/11/juan-xxiii.webp"></div><div class="date">1958–1978</div><div class="role">Juan XXIII & Pablo VI — Prácticas</div><div class="text">Traslados de sacerdotes acusados sin sanción.</div></article>
          <article class="node" data-pos="55"><div class="media"><img src="https://elpueblocatolico.org/wp-content/uploads/2023/10/Juan-Pablo-II.jpg"></div><div class="date">1978–2005</div><div class="role">Juan Pablo II — Encubrimiento</div><div class="text">Casos ocultos; procedimientos internos sin justicia civil.</div></article>
          <article class="node" data-pos="65"><div class="media"><img src="https://media.revistavanityfair.es/photos/60e85ee0c575901c42629089/master/w_3940%2Cc_limit/49282.jpg"></div><div class="date">1992</div><div class="role">Sinéad O’Connor — Protesta</div><div class="text">Rompe foto del Papa en TV, denuncia encubrimiento.</div></article>
          <article class="node" data-pos="75"><div class="media"><img src="https://nuestra-voz.org/wp-content/uploads/2020/03/20180705T1237-18136-CNS-POPE-BALTIC-SCHEDULE_web.jpg"></div><div class="date">2001</div><div class="role">Juan Pablo II — Disculpa</div><div class="text">Pide perdón por los abusos del clero.</div></article>
          <article class="node" data-pos="85"><div class="media"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/The_Boston_Globe.svg/1280px-The_Boston_Globe.svg.png" 
                style="width: 300px; height: auto; border-radius: 8px; margin-top: 10px;">
              <p style="font-size: 14px; color: #555; margin-top: 5px;">
              </p>
            </div>

            <div class="date">2002</div>
            <div class="role">Investigación — <strong>Boston Globe</strong></div>
            <div class="text">
              Revela encubrimiento sistemático en Estados Unidos; inspira investigaciones globales y la película <em>Spotlight</em>.
            </div>
          </article>
          <article class="node" data-pos="95"><div class="media"><img src="https://www.clonline.org/storage_files/43708/benedictoxvicpp-b-o.jpg"></div><div class="date">2005–2013</div><div class="role">Benedicto XVI — Acciones</div><div class="text">Inicia sanciones internas y reuniones con víctimas.</div></article>
          <article class="node" data-pos="105"><div class="media"><img src="https://ichef.bbci.co.uk/news/1024/branded_mundo/8e4b/live/b62431d0-1eb3-11f0-9d4d-4370edfa48ef.jpg"></div><div class="date">2010–2017</div><div class="role">Papa Francisco — Crisis</div><div class="text">Errores iniciales y disculpas públicas.</div></article>
          <article class="node" data-pos="115"><div class="media"><img src="https://media.vaticannews.va/media/content/dam-archive/vaticannews/images-multimedia/srv/08504_18042014.jpg/_jcr_content/renditions/cq5dam.thumbnail.cropped.750.422.jpeg"></div><div class="date">2018–2019</div><div class="role">Francisco — Cumbre Mundial</div><div class="text">Convoca reunión global sobre abusos.</div></article>
          <article class="node" data-pos="125"><div class="media"><img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Flag_of_the_United_Nations.svg"></div><div class="date">2021</div><div class="role">ONU — Crítica</div><div class="text">Acusa al Vaticano de falta de transparencia judicial.</div></article>
          <article class="node" data-pos="135"><div class="media"><img src="https://casamacondo.co/wp-content/uploads/2025/04/casamacondo-share.png"></div><div class="date">2023</div><div class="role">Casa Macondo — Investigación</div><div class="text">Periodismo colombiano revela denuncias históricas.</div></article>

        </div>
      </div>
    </div>
    <footer>
      Fuente: recopilación educativa. — Diseño optimizado para Streamlit 2025.
    </footer>

    <script>
      const nodes = document.querySelectorAll('.node');
      const timeline = document.getElementById('timeline');
      const revealVisible = () => {
        const rect = timeline.getBoundingClientRect();
        nodes.forEach(n => {
          const r = n.getBoundingClientRect();
          if (r.left < rect.right && r.right > rect.left) n.classList.add('show');
        });
      };
      timeline.addEventListener('scroll', revealVisible);
      window.addEventListener('load', () => {
        revealVisible();
        const markers = document.getElementById('markers');
        nodes.forEach(n => {
          const p = parseFloat(n.dataset.pos);
          const m = document.createElement('div');
          m.className = 'marker';
          m.style.left = `calc(${p}% - 7px)`;
          markers.appendChild(m);
        });
      });
      document.getElementById('next').addEventListener('click', () => { timeline.scrollBy({ left: 420, behavior: 'smooth' }); });
      document.getElementById('prev').addEventListener('click', () => { timeline.scrollBy({ left: -420, behavior: 'smooth' }); });
    </script>
  </div>
</body>
</html>
"""

# Render en Streamlit
st.components.v1.html(html_code, height=900, scrolling=True)
