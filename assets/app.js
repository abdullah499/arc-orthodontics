/* Arc Orthodontics — shared interactions (vanilla JS, no dependencies) */
(function(){
  "use strict";

  // --- Mobile drawer ---
  var drawer=document.getElementById('drawer'), openBtn=document.getElementById('openMenu');
  if(drawer&&openBtn){
    function setMenu(open){drawer.classList.toggle('open',open);openBtn.setAttribute('aria-expanded',open);document.body.style.overflow=open?'hidden':'';}
    openBtn.addEventListener('click',function(){setMenu(true);});
    drawer.addEventListener('click',function(e){if(e.target.closest('[data-close]'))setMenu(false);});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')setMenu(false);});
  }

  // --- Demo forms ---
  document.querySelectorAll('form[data-demo]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var req=f.querySelector('[required]');
      if(req&&!req.value){req.focus();return;}
      var ok=f.querySelector('.form-ok'); if(ok)ok.style.display='block';
      var btn=f.querySelector('button[type=submit]'); if(btn){btn.textContent='Sent ✓';btn.disabled=true;}
    });
  });

  // --- Before/After sliders ---
  document.querySelectorAll('[data-ba]').forEach(function(el){
    var after=el.querySelector('.ba-after'), handle=el.querySelector('.ba-handle'), dragging=false;
    function set(x){
      var r=el.getBoundingClientRect();
      var p=Math.max(0,Math.min(100,((x-r.left)/r.width)*100));
      after.style.clipPath='inset(0 0 0 '+p+'%)'; handle.style.left=p+'%';
    }
    function start(e){dragging=true;set((e.touches?e.touches[0]:e).clientX);}
    function move(e){if(dragging)set((e.touches?e.touches[0]:e).clientX);}
    function end(){dragging=false;}
    el.addEventListener('mousedown',start);window.addEventListener('mousemove',move);window.addEventListener('mouseup',end);
    el.addEventListener('touchstart',start,{passive:true});el.addEventListener('touchmove',move,{passive:true});el.addEventListener('touchend',end);
  });

  // --- Filter chips (reviews / journal / gallery) ---
  document.querySelectorAll('[data-filter-group]').forEach(function(group){
    var chips=group.querySelectorAll('.chip');
    var targets=document.querySelectorAll('[data-cat]');
    chips.forEach(function(chip){
      chip.addEventListener('click',function(){
        chips.forEach(function(c){c.classList.remove('active');});
        chip.classList.add('active');
        var f=chip.getAttribute('data-f');
        targets.forEach(function(t){
          var cats=(t.getAttribute('data-cat')||'').split(' ');
          t.style.display=(f==='all'||cats.indexOf(f)>-1)?'':'none';
        });
      });
    });
  });

  // --- Treatment finder ---
  var finder=document.querySelector('.finder');
  if(finder){
    var fSteps=finder.querySelectorAll('.f-step'), fProg=finder.querySelector('.progress i'),
        fResult=finder.querySelector('.finder-result'), fPill=finder.querySelector('.f-pill'), fWhy=finder.querySelector('.f-why'),
        fStepsWrap=finder.querySelector('.f-steps'), cur=0, answers=[];
    var R={
      adult:{n:'Invisalign — Adult',w:'Discreet, removable, and ideal for most adult cases. Your free scan confirms the exact plan.',h:'service-invisalign-adult.html'},
      teen:{n:'Invisalign — Teen',w:'Built for teen schedules and self-consciousness, with built-in wear tracking.',h:'service-invisalign-teen.html'},
      child:{n:'Early Treatment (Phase 1)',w:'Gentle, well-timed guidance while the jaw is still growing, often shortening later treatment.',h:'service-early.html'},
      fast:{n:'Modern Metal Braces',w:'The most efficient route for moving teeth quickly and predictably.',h:'service-metal.html'},
      budget:{n:'Modern Metal Braces',w:'Proven, effective, and the most budget-friendly path from $3,800.',h:'service-metal.html'},
      ceramic:{n:'Clear Ceramic Braces',w:'Tooth-coloured and low-profile: barely-there correction that still moves fast.',h:'service-ceramic.html'}
    };
    function show(i){fSteps.forEach(function(s,n){s.hidden=n!==i;});fProg.style.width=((i+1)/fSteps.length*100)+'%';}
    finder.querySelectorAll('.f-step [data-next]').forEach(function(btn){
      btn.addEventListener('click',function(){
        answers[cur]=Array.prototype.indexOf.call(btn.parentNode.querySelectorAll('[data-next]'),btn);
        cur++;
        if(cur<fSteps.length){show(cur);}
        else{
          var who=['adult','teen','child'][answers[0]||0], pref=answers[1], key=who;
          if(who==='adult'){key=pref===0?'ceramic':pref===1?'fast':pref===2?'budget':'adult';}
          var r=R[key]||R.adult;
          fPill.textContent=r.n; fWhy.textContent=r.w;
          var link=finder.querySelector('.f-link'); if(link)link.href=r.h;
          fStepsWrap.style.display='none'; fProg.style.width='100%'; fResult.classList.add('show');
        }
      });
    });
    var rs=finder.querySelector('.f-restart');
    if(rs)rs.addEventListener('click',function(){cur=0;answers=[];fStepsWrap.style.display='';fResult.classList.remove('show');show(0);});
  }

  // --- Cost calculator ---
  var calc=document.querySelector('.calc');
  if(calc){
    var cTreat=calc.querySelector('#cTreat'),cTerm=calc.querySelector('#cTerm'),cIns=calc.querySelector('#cIns'),
        cTermV=calc.querySelector('#cTermV'),cMonthly=calc.querySelector('#cMonthly'),cSummary=calc.querySelector('#cSummary'),
        cBase=calc.querySelector('#cBase'),cBen=calc.querySelector('#cBen'),cNet=calc.querySelector('#cNet');
    function money(n){return '$'+n.toLocaleString('en-US');}
    function run(){
      var base=+cTreat.value, term=+cTerm.value, ins=+cIns.value, net=Math.max(0,base-ins), monthly=Math.round(net/term);
      cTermV.textContent=term+' months';
      cBase.textContent=money(base);
      cBen.textContent=(ins>0?'– '+money(ins):'$0');
      cNet.textContent=money(net);
      cMonthly.textContent=monthly.toLocaleString('en-US');
      cSummary.textContent=money(net)+(ins>0?' after insurance':'')+', over '+term+' months · $0 down';
    }
    [cTreat,cTerm,cIns].forEach(function(el){if(el)el.addEventListener('input',run);});
    run();
  }

  // --- Footer year ---
  var y=document.getElementById('yr'); if(y)y.textContent=new Date().getFullYear();
})();
