const themeSwitch = document.getElementById("theme-switch");
const themeIndicator = document.getElementById("theme-indicator");
const page = document.body;

const themeStates = ["light", "dark"];
const indicators = ["fa-moon", "fa-sun"];
const pageClass = ["bg-gray-100", "dark-page"];

function setTheme(theme) {
    localStorage.setItem("theme", themeStates[theme]);
}

function setIndicator(theme) {
    themeIndicator.classList.remove(indicators[1]);
    themeIndicator.classList.remove(indicators[0]);
    themeIndicator.classList.add(indicators[theme]);
}

function setPage(theme) {
    page.classList.remove(pageClass[0]);
    page.classList.remove(pageClass[1]);
    page.classList.add(pageClass[theme]);
}

setTheme(1);
setIndicator(1);
setPage(1);
themeSwitch.checked = true;

themeSwitch.addEventListener('change', function () {
    const themeIndex = this.checked ? 1 : 0;
    setTheme(themeIndex);
    setIndicator(themeIndex);
    setPage(themeIndex);
});