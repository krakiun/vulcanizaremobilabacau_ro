const header=document.querySelector('header');
addEventListener('scroll',()=>header.classList.toggle('scrolled',scrollY>8),{passive:true});
const burger=document.querySelector('.burger'),mm=document.querySelector('.mobile-menu');
burger.addEventListener('click',()=>{const o=mm.classList.toggle('open');burger.setAttribute('aria-expanded',o)});
mm.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{mm.classList.remove('open');burger.setAttribute('aria-expanded',false)}));
if('IntersectionObserver' in window){
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
}else document.querySelectorAll('.reveal').forEach(el=>el.classList.add('in'));
