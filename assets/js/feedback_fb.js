// function more(id) {
//   console.log(id)
//   let idO = document.querySelector("#"+id + ".expanded");
//   console.log(idO)
//   var dots = document.getElementById("dots");
//   var moreText = document.getElementById("more");
//   var btnText = document.getElementById("btn");
//   let expanded = document.querySelector(".expanded");

//   if (idO.classList.contains("active")) {
//     expanded.classList.remove("active");
//     dots.style.display = "inline";
//     btnText.innerHTML = "Read more";
//     moreText.style.display = "none";
//   } else {
//     expanded.classList.add("active");
//     dots.style.display = "none";
//     btnText.innerHTML = "Read less";
//     moreText.style.display = "inline";
//   }
// }

function more(id) {
  console.log(id)
  const element = document.getElementById(id);
  const dots = element.querySelector("#dots");
  const moreText = element.querySelector(".more");
  const btnText = element.querySelector(".btn-more");

  
  console.log("h:",fullHeight)

  if (element.classList.contains("active")) {
    element.classList.remove("active");
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
    $('#'+id).animate({'height': 120}, 300);
  } else {
    element.classList.add("active");
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
    var fullHeight = element.querySelector(".block").offsetHeight;
    $('#'+id).css({'height': 120, 'max-height': 'none'}).animate({'height': fullHeight}, 300);
  }
}
