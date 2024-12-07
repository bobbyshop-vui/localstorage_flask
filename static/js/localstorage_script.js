if (typeof(Storage) !== 'undefined') {
localStorage.setItem("username", "currentUser");
localStorage.setItem("theme", "dark");
var username = localStorage.getItem("username");
var theme = localStorage.getItem("theme");
} else {
console.error('localStorage is not supported.');
}