document.addEventListener("DOMContentLoaded", () => {
  const messages = document.getElementsByClassName("atom-message");
  for (let i = 0; i < messages.length; i++) {
    setTimeout(() => {
      messages[i].classList.remove("atom-message-hidden");
    }, 500);
    setTimeout(() => {
      messages[i].classList.add("atom-message-hidden");
      setTimeout(() => messages[0].remove(), 500);
    }, 5000);
  }
});