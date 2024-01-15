function divisors(integer) {
    let r = []
    for(let i = 1; i<integer/2+1; i++){
      if(integer%i == 0) r.push([i, integer/i])
    }
    return r
  }
  
  
  function isprime(integer) {
    if(integer <= 2) return false;
  
    factors = divisors(integer);
  
    if(factors.length == 1) return true;
    return false;
  }
  
  function drawboxes(c, k, size, n, color) {
    for (let i = 0; i < n; i++) {
      c.beginPath();
      c.lineWidth = "1";
      c.strokeStyle = "white";
      c.fillStyle = color;
      c.rect(i*size, k, size, size);
      c.stroke();
      c.fill();
    } 
    return 
  }
  
  function drawfactors(c, factors, multiplier, offset){
    k = 0;
  
    for (let i = 0; i < factors.length; i++) {
      size = factors[i][0];
      n = factors[i][1];
  
      if(isprime(size)){
        color = "green";
      } else {
        color = "blue";
      }
      drawboxes(c, k+offset, multiplier*size, n, color);
      k = k + size*multiplier;
    }
    return k
  }
  
  function drawPerfectNumber(canvas_id, integer, multiplier) {
    const canvas = document.getElementById(canvas_id);
    canvas.width = integer*multiplier;
    canvas.height = (integer+25)*multiplier;
    
    // initiating 2D context on it
    const c = canvas.getContext('2d')
  
    addEventListener('resize', () => {
      canvas.width = innerWidth
      canvas.height = innerHeight
    })
  
    c.font = "12px serif";
    c.fillText(integer.toString(), 10, 15);
    offset = 24;
  
    factors = divisors(integer);
    k = drawfactors(c, factors, multiplier, offset);
    
    c.beginPath();
    c.lineWidth = "2";
    c.strokeStyle = "red";
    c.rect(0, offset, integer*multiplier, integer*multiplier);
    c.stroke();
  
    return
  }
  
  m = 10;
  
  drawPerfectNumber('2', 2, m);
  drawPerfectNumber('3', 3, m);
  drawPerfectNumber('4', 4, m);
  drawPerfectNumber('5', 5, m);
  drawPerfectNumber('6', 6, m);
  drawPerfectNumber('7', 7, m);
  drawPerfectNumber('8', 8, m);
  drawPerfectNumber('9', 9, m);
  drawPerfectNumber('10', 10, m);
  drawPerfectNumber('11', 11, m);
  drawPerfectNumber('12', 12, m);
  drawPerfectNumber('13', 13, m);
  drawPerfectNumber('14', 14, m);
  
  drawPerfectNumber('6.1', 6, 16);
  drawPerfectNumber('28', 28, 8);
  drawPerfectNumber('496', 496, 1);
  
  drawPerfectNumber('48', 8128, 0.1);
  
  
  // function findPerfectNumbers(n) {
  //   const r = new Set();
  //   for(let i = 2; i<n; i++){
  //     factors = divisors(i);
  //     t = 0;
  //     for (let i = 0; i < factors.length; i++) {
  //       t = t + factors[i][0];
  //     }
  //     r.add(t);
  //   }
  //   x = Array.from(r);
  //   x.sort(function(a, b){return a - b});
  //   return x
  // }
  
  console.log(isprime(3));