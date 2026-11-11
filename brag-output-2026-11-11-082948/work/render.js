const { chromium } = require('playwright');
const fs=require('fs');
(async () => {
  const mode=process.argv[2]; const out=process.argv[3];
  const b = await chromium.launch();
  const pg = await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
  await pg.goto('http://127.0.0.1:8765/brag-output-2026-11-11-082948/work/stage.html');
  await pg.evaluate(()=>window.ready);
  // warm iframe lazy images by scrolling once
  await pg.evaluate(async()=>{const w=document.getElementById('frame').contentWindow;for(let y=0;y<3200;y+=300){w.scrollTo(0,y);await new Promise(r=>setTimeout(r,40))}w.scrollTo(0,0)});
  await pg.waitForTimeout(800);
  let times=[];
  if(mode==='stills') times=process.argv.slice(4).map(Number);
  else { const n=Math.round(30*0.625*30); for(let i=0;i<n;i++) times.push(i/30); }
  fs.mkdirSync(out,{recursive:true});
  for(let i=0;i<times.length;i++){
    await pg.evaluate(t=>window.render(t),times[i]);
    await pg.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
    const name= mode==='stills'?`s_${times[i].toFixed(2)}.jpg`:`f_${String(i).padStart(4,'0')}.jpg`;
    await pg.screenshot({path:`${out}/${name}`,type:'jpeg',quality:95});
  }
  await b.close();
})();
