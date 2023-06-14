const flashMessage = document.getElementById("msg-item");
const flashMessageCloseButton = document.getElementById("msg-btn");
let flashMessageRemoveTimeout;

function hideFlashMessages(timeout = 0) {
  clearTimeout(flashMessageRemoveTimeout);
  setTimeout(() => {
    flashMessage.classList.add("exiting");
  }, timeout);
  setTimeout(() => {
    flashMessageRemoveTimeout = flashMessage.classList.add("removed");
  }, timeout + 400);
}

hideFlashMessages(2000);

flashMessageCloseButton.addEventListener("click", () => {
  hideFlashMessages();
});
