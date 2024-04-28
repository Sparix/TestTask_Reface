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

// За замовчуванням встановлюємо тему "dark"
setTheme(1);
setIndicator(1);
setPage(1);
themeSwitch.checked = true; // Позначаємо перемикач як ввімкнений

// Обробник події для зміни теми при взаємодії з перемикачем
themeSwitch.addEventListener('change', function () {
    const themeIndex = this.checked ? 1 : 0; // Визначаємо індекс теми на основі положення перемикача
    setTheme(themeIndex);
    setIndicator(themeIndex);
    setPage(themeIndex);
});