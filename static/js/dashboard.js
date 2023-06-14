"use_strict";

const form = document.getElementById("findWordId");
const dashboardId = form.getAttribute("data-dashboard-id");
const generateDefinitionButton = document.getElementById("generate-definition");
const defintionTextArea = document.getElementById("defintion");
const playAudioBtn = document.getElementById("play-audio");
const audioUrlInput = document.getElementById("audio-url");
const audioIcon = document.getElementById("audio-icon");
const spanishKey = document.getElementById("spanishKey").value;
const noDefinition = document.getElementById("msq");

let definition = defintionTextArea.value;
let audiotrack = "";
let time = 3000;

function showNoDefinitionMassage() {
  noDefinition.classList.toggle("no-definiton-msq");
  setTimeout(() => {
    noDefinition.classList.toggle("no-definiton-msq");
  }, time);
}

const languages = {
  en: {
    getUrl: (word) => `https://api.dictionaryapi.dev/api/v2/entries/en/${word}`,
    mapper: function getDefinitionOnEnglish(data) {
      const definition = data[0]?.meanings[0]?.definitions[0]?.definition;
      if (!definition) {
        showNoDefinitionMassage();
      }
      audioTrack = data[0]?.phonetics[0 || 1]?.audio;
      return {
        definition: definition || "",
        audioTrack,
      };
    },
  },
  es: {
    getUrl: (word) =>
      `https://dictionaryapi.com/api/v3/references/spanish/json/${word}?key=${spanishKey}`,
    mapper: function getDefinitionOnSpanish(data) {
      const definition = data[0]?.shortdef?.[0];

      console.log("this is definition", definition);
      if (!definition) {
        showNoDefinitionMassage();
      }
      const audioName = data[0]?.hwi?.prs?.[0]?.sound.audio;
      const audioTrack = `https://media.merriam-webster.com/audio/prons/es/me/mp3/${audioName[0]}/${audioName}.mp3`;

      return {
        definition: definition || "",
        audioTrack,
      };
    },
  },
};

generateDefinitionButton.addEventListener("click", () => {
  const word = document.getElementById("word").value;
  let currentLanguage = document.getElementById("language").value;
  const { getUrl, mapper } = languages[currentLanguage] || languages.en;
  if (languages[currentLanguage]) {
    fetch(getUrl(word))
      .then((response) => response.json())
      .then((data) => mapper(data))
      .then(({ definition, audioTrack }) => {
        defintionTextArea.value = definition;
        audioUrlInput.value = audioTrack;
      });
  }
});

document
  .getElementById("dashboard-container")
  .addEventListener("click", function (event) {
    if (event.target.classList.contains("toggle-button")) {
      const button = event.target;
      const form = button.parentElement.querySelector(".edit-form");
      if (button.textContent === "Edit") {
        form.style = "display: block;";
        button.textContent = "Close";
      } else {
        form.style = "display: none;";
        button.textContent = "Edit";
      }
    }
  });
