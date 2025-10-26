<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Línea de tiempo Abusos del clero (Pantalla completa)</title>
  <style>
    :root{
      --bg:#f7efe6; /* papel antiguo */
      --card:#fffaf4;
      --muted:#6b5a4a;
      --sepia-1:#5b3a29; /* oscuro */
      --sepia-2:#8b5a3c;
      --gold:#c59b4b;
      --accent:#a5663b;
      --glass: rgba(255,255,255,0.6);
      --maxh: 88vh;
      font-family: Inter, 'Helvetica Neue', Arial, sans-serif;
    }
    *{box-sizing:border-box}
    html,body{height:100%;margin:0;background:var(--bg);color:var(--sepia-1)}

    /* Fullscreen layout */
    .wrap{height:100vh;display:flex;flex-direction:column}
    header{display:flex;align-items:center;justify-content:space-between;padding:22px 36px;border-bottom:1px solid rgba(0,0,0,0.04)}
    header .title{display:flex;gap:18px;align-items:center}
    .logo{width:68px;height:68px;border-radius:10px;background:linear-gradient(135deg,var(--sepia-1),var(--sepia-2));display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;box-shadow:0 8px 20px rgba(91,58,41,0.12)}
    h1{font-size:1.25rem;margin:0;color:var(--sepia-1)}
    .subtitle{color:var(--muted);font-size:0.92rem}

    /* timeline viewport */
    .viewport{flex:1;display:flex;align-items:center;justify-content:center;padding:30px 24px}
    .timeline-wrap{position:relative;width:95%;height:var(--maxh);background:linear-gradient(180deg, rgba(255,250,245,1), rgba(247,240,232,1));border-radius:18px;box-shadow:0 20px 50px rgba(91,58,41,0.07);overflow:hidden;padding:28px}

    /* horizontal timeline */
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

    /* connector line and markers */
    .connector{position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);pointer-events:none}
    .line{position:absolute;left:2%;right:2%;top:50%;height:6px;background:linear-gradient(90deg,var(--sepia-2),var(--gold));border-radius:6px;opacity:0.9}
    .marker{position:absolute;top:50%;width:18px;height:18px;border-radius:50%;transform:translateY(-50%);background:var(--card);border:4px solid var(--accent);box-shadow:0 6px 12px rgba(0,0,0,0.08)}

    /* responsive */
    @media (max-width:900px){
      .node{flex:0 0 320px}
    }

    /* info panel */
    .panel{position:fixed;right:28px;bottom:28px;background:var(--glass);backdrop-filter:blur(6px);padding:14px 18px;border-radius:12px;border:1px solid rgba(101,77,55,0.08);color:var(--sepia-1)}
    .panel button{background:transparent;border:1px solid rgba(0,0,0,0.06);padding:8px 10px;border-radius:8px;cursor:pointer;color:var(--sepia-1)}

    footer{padding:12px 36px;color:var(--muted);font-size:0.9rem}

    /* subtle reveal */
    .node{opacity:0;transform:translateY(12px)}
    .node.show{opacity:1;transform:none}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="title">
        <div class="logo">LT</div>
        <div>
          <h1>Histórico de Abuso en el Clero</h1>
        </div>
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
          <!-- markers are positioned with inline styles per node -->
          <div id="markers"></div>
        </div>

        <div class="timeline" id="timeline">

          <!-- Node 1 -->
          <article class="node" data-pos="6" tabindex="0">
            <div class="media">
              <img src="https://brujulacotidiana.com/storage/imgs/san-pier-damiani-large-0-1.jpg" alt="Retrato estilizado de Pedro Damián">
            </div>
            <div class="date">Siglo XI</div>
            <div class="role">Pedro Damián — <strong>Denuncia</strong></div>
            <div class="text"><strong>Hecho:</strong> Escribe <em>Liber Gomorrhianus</em>, denunciando abusos sexuales de clérigos.<br><strong>Nota:</strong> La Iglesia no implementa sanciones efectivas.</div>
          </article>

          <!-- Node 2 -->
          <article class="node" data-pos="15" tabindex="0">
            <div class="media">
              <img src="https://zuercher-museen.ch/media/h1vf1g35/szefue_kvz_gzf-walter-huss_1440.jpg?width=1230&height=674&mode=crop&quality=80">
            </div>
            <div class="date">Finales del siglo XV</div>
            <div class="role">Katharina von Zimmern — <strong>Caso</strong></div>
            <div class="text"><strong>Hecho:</strong> Katharina y su hermana son retiradas de su abadía tras ser abusadas por sacerdotes.<br><strong>Polémica:</strong> Las víctimas fueron castigadas; los abusadores permanecen impunes.</div>
          </article>

          <!-- Node 3 -->
          <article class="node" data-pos="25" tabindex="0">
            <div class="media">
              <img src="https://ambientestereo.fm/sitio/wp-content/uploads/2024/12/Martin-Lutero.jpeg" alt="Retrato de Martín Lutero">
            </div>
            <div class="date">1531</div>
            <div class="role">Martín Lutero — <strong>Acusación</strong></div>
            <div class="text"><strong>Hecho:</strong> Denuncia al Papa León X por permitir prácticas aberrantes entre cardenales y niños.<br><strong>Negligencia:</strong> Encubrimiento institucional.</div>
          </article>

          <!-- Node 4 -->
          <article class="node" data-pos="35" tabindex="0">
            <div class="media">
              <img src="https://fsspx-sudamerica.org/sites/default/files/styles/content_image_16_9_desktop/public/drupal-7/pio12cabezal.jpg?itok=0zS7gU7Q" alt="Retrato de Pío XII">
            </div>
            <div class="date">1939–1958</div>
            <div class="role">Papa Pío XII — <strong>Período</strong></div>
            <div class="text"><strong>Hecho:</strong> Casos de abuso conocidos; no existen protocolos claros ni sanciones.<br><strong>Negligencia:</strong> Prioridad a la reputación institucional.</div>
          </article>

          <!-- Node 5 -->
          <article class="node" data-pos="45" tabindex="0">
            <div class="media">
              <img src="https://cdn.zendalibros.com/wp-content/uploads/2023/11/juan-xxiii.webp" alt="Retrato de Juan XXIII">
            </div>
            <div class="date">1958–1978</div>
            <div class="role">Juan XXIII & Pablo VI — <strong>Prácticas</strong></div>
            <div class="text"><strong>Hecho:</strong> Traslados de sacerdotes acusados a otras parroquias.<br><strong>Error histórico:</strong> Los abusos se repiten por falta de acción.</div>
          </article>

          <!-- Node 6 -->
          <article class="node" data-pos="55" tabindex="0">
            <div class="media">
              <img src="https://elpueblocatolico.org/wp-content/uploads/2023/10/Juan-Pablo-II.jpg" alt="Retrato de Juan Pablo II">
            </div>
            <div class="date">1978–2005</div>
            <div class="role">Juan Pablo II — <strong>Encubrimiento</strong></div>
            <div class="text"><strong>Hecho:</strong> Encubrimiento sistemático y traslados; procedimientos de Derecho Canónico sin justicia civil.<br><strong>Crítica:</strong> Representantes de víctimas lo acusaron de inacción.</div>
          </article>

          <!-- Node 7 -->
          <article class="node" data-pos="65" tabindex="0">
            <div class="media">
              <img src="https://media.revistavanityfair.es/photos/60e85ee0c575901c42629089/master/w_3940%2Cc_limit/49282.jpg" alt="Foto de Sinéad O'Connor">
            </div>
            <div class="date">1992</div>
            <div class="role">Sinéad O'Connor — <strong>Protesta</strong></div>
            <div class="text">Rompe una foto del Papa en <em>Saturday Night Live</em>, visibilizando el encubrimiento.</div>
          </article>

          <!-- Node 8 -->
          <article class="node" data-pos="75" tabindex="0">
            <div class="media">
              <img src="https://nuestra-voz.org/wp-content/uploads/2020/03/20180705T1237-18136-CNS-POPE-BALTIC-SCHEDULE_web.jpg" alt="Juan Pablo II en 2001">
            </div>
            <div class="date">2001</div>
            <div class="role">Juan Pablo II — <strong>Disculpa</strong></div>
            <div class="text">Emite disculpa pública: califica el abuso como "profunda contradicción de la enseñanza y el testimonio de Jesucristo".</div>
          </article>

          <!-- Node 9 -->
         <article class="node" data-pos="85" tabindex="0">
            <div class="media" style="text-align: center;">
              <img 
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/The_Boston_Globe.svg/1280px-The_Boston_Globe.svg.png" 
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


          <!-- Node 10 -->
          <article class="node" data-pos="95" tabindex="0">
            <div class="media">
              <img src="https://www.clonline.org/storage_files/43708/benedictoxvicpp-b-o.jpg" alt="Retrato de Benedicto XVI">
            </div>
            <div class="date">2005–2013</div>
            <div class="role">Benedicto XVI — <strong>Acciones</strong></div>
            <div class="text">Implementa protocolos internos, sanciona casos puntuales y se reúne con víctimas; las denuncias históricas siguen siendo un reto.</div>
          </article>

          <!-- Node 11 -->
          <article class="node" data-pos="105" tabindex="0">
            <div class="media">
              <img src="https://ichef.bbci.co.uk/news/1024/branded_mundo/8e4b/live/b62431d0-1eb3-11f0-9d4d-4370edfa48ef.jpg" alt="Retrato de Francisco">
            </div>
            <div class="date">2010–2017</div>
            <div class="role">Francisco — <strong>Crisis</strong></div>
            <div class="text">Inicial desacierto en Chile; comentarios que provocaron polémica y posteriores disculpas.</div>
          </article>

          <!-- Node 12 -->
          <article class="node" data-pos="115" tabindex="0">
            <div class="media">
              <img src="https://media.vaticannews.va/media/content/dam-archive/vaticannews/images-multimedia/srv/08504_18042014.jpg/_jcr_content/renditions/cq5dam.thumbnail.cropped.750.422.jpeg" alt="Francisco en 2019">
            </div>
            <div class="date">2018–2019</div>
            <div class="role">Francisco — <strong>Respuestas</strong></div>
            <div class="text">Disculpa pública por Chile; convoca cumbre mundial (2019) y promueve medidas de transparencia.</div>
          </article>

          <!-- Node 13 -->
          <article class="node" data-pos="125" tabindex="0">
            <div class="media">
              <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Flag_of_the_United_Nations.svg" alt="Logo ONU">
            </div>
            <div class="date">2021</div>
            <div class="role">ONU — <strong>Crítica</strong></div>
            <div class="text">Relatores critican al Vaticano por obstrucción en casos judiciales y falta de compensación a víctimas.</div>
          </article>

          <!-- Node 14 -->
          <article class="node" data-pos="135" tabindex="0">
            <div class="media">
              <img src="https://casamacondo.co/wp-content/uploads/2025/04/casamacondo-share.png" alt="Imagen representativa de periodismo investigativo">
            </div>
            <div class="date">2023</div>
            <div class="role">Casa Macondo — <strong>Investigación</strong></div>
            <div class="text">Periodismo investigativo en Colombia revela cientos de sacerdotes denunciados y archivos secretos; visibiliza décadas de encubrimiento.</div>
          </article>

        </div>

      </div>
    </div>

    <footer>
      Fuente: selección cronológica para fines informativos. Imágenes: Wikimedia Commons (uso ilustrativo). Diseño: Línea de tiempo didáctica.
    </footer>

    <div class="panel" aria-hidden="false">
      <strong>Atajos:</strong> ← →  |  <button id="toStart">Ir al inicio</button>
    </div>
  </div>

  <script>
    // Reveal nodes progressively
    const nodes = Array.from(document.querySelectorAll('.node'));
    const timeline = document.getElementById('timeline');

    const revealVisible = ()=>{
      const rect = timeline.getBoundingClientRect();
      nodes.forEach(n=>{
        const r = n.getBoundingClientRect();
        if(r.left < rect.right && r.right > rect.left){
          n.classList.add('show');
        }
      });
    }
    timeline.addEventListener('scroll', revealVisible);
    window.addEventListener('load', ()=>{
      revealVisible();
      // place markers along connector according to data-pos
      const markers = document.getElementById('markers');
      nodes.forEach(n=>{
        const p = parseFloat(n.dataset.pos);
        const m = document.createElement('div');
        m.className='marker';
        m.style.left = `calc(${p}% - 9px)`; // center marker
        markers.appendChild(m);
      });
    });

    // Controls
    document.getElementById('next').addEventListener('click', ()=>{
      timeline.scrollBy({left:420,behavior:'smooth'});
    });
    document.getElementById('prev').addEventListener('click', ()=>{
      timeline.scrollBy({left:-420,behavior:'smooth'});
    });
    document.getElementById('toStart').addEventListener('click', ()=>{
      timeline.scrollTo({left:0,behavior:'smooth'});
    });

    // Keyboard
    window.addEventListener('keydown', e=>{
      if(e.key === 'ArrowRight') timeline.scrollBy({left:420,behavior:'smooth'});
      if(e.key === 'ArrowLeft') timeline.scrollBy({left:-420,behavior:'smooth'});
    });
  </script>
</body>
</html>
