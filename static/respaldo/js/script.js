const body = document.querySelector('body'),
  sidebar = body.querySelector('nav'),
  toggle = body.querySelector('.toggle'),
  searchBtn = body.querySelector('.search-box'),
  modeSwitch = body.querySelector('.toggle-switch'),
  modeText = document.querySelector('.mode-text'),
  nameElement = document.querySelector('.name'),
  name1Element = document.querySelector('.name1');

toggle.addEventListener("click", () => {
  sidebar.classList.toggle("close");
  nameElement.classList.toggle('hidden');
  name1Element.classList.toggle('hidden');
});

searchBtn.addEventListener("click", () => {
  sidebar.classList.remove("close");
});

modeSwitch.addEventListener("click", () => {
  body.classList.toggle("dark");
  if (body.classList.contains("dark")) {
    modeText.innerHTML = "Light mode";
  } else {
    modeText.innerHTML = "Dark mode";
  }
});
