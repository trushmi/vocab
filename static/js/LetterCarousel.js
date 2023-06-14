const slider = document.getElementById("slideshow");

const letters = [
  "Aa [ei]",
  "Bb [bi:]",
  "Cc [si:]",
  "Dd [di:]",
  "Ee [i:]",
  "Ff [ef]",
];
let index = 0;
let time = 1000;

const showLetters = () => {
  slider.innerHTML = letters[index];

  index < letters.length - 1 ? index++ : (index = 0);
  setTimeout("showLetters()", time);
};
window.onload = showLetters;
