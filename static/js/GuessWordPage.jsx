function GuessWordPage() {
  const [dashboards, setDashboards] = React.useState([]);
  const [selectedDashboard, setSelectedDashboard] = React.useState();
  const [wordToGuess, setWordToGuess] = React.useState();
  const [guessedLettersSet, setGuessedLettersSet] = React.useState(new Set());
  const [userChoiceCount, setUserChoiceCount] = React.useState(0);
  const englishAlphabet = "abcdefghijklmnopqrstuvwxyz";
  const spanishAlphabet = "abcdefghijklmnñopqrstuvwxyz";
  const selectedLanguage = selectedDashboard && selectedDashboard.language;

  const supportedLanguages = {
    en: "abcdefghijklmnopqrstuvwxyz",
    es: "abcdefghijklmnñopqrstuvwxyz",
    other: "abcdefghijklmnopqrstuvwxyz",
  };

  const onLetterClick = (letter) => {
    const newSet = new Set(guessedLettersSet);
    newSet.add(letter);
    setGuessedLettersSet(newSet);
    setUserChoiceCount(userChoiceCount + 1);
  };

  React.useEffect(() => {
    fetch("/api/flashcards")
      .then((response) => response.json())
      .then((dasboards) => {
        setDashboards(dasboards);
        setSelectedDashboard(dasboards[0]);
      });
  }, []);

  const selectRandomWord = () => {
    if (selectedDashboard && selectedDashboard.words.length) {
      const words = selectedDashboard.words;
      const randomWord = words[Math.floor(Math.random() * words.length)];
      setWordToGuess(randomWord);
    } else {
      setWordToGuess(null);
    }
  };

  React.useEffect(() => {
    selectRandomWord();
    startAgain();
  }, [selectedDashboard]);

  const startAgain = () => {
    setUserChoiceCount(0);
    selectRandomWord();
    setGuessedLettersSet(new Set());
  };
  const limit = wordToGuess && wordToGuess.term.length * 2;
  const hasLost = userChoiceCount >= limit;
  const hasWon =
    wordToGuess &&
    wordToGuess.term.split("").every((letter) => guessedLettersSet.has(letter));

  const isGameOver = hasLost || hasWon;
  const language = supportedLanguages[selectedLanguage];

  if (!dashboards.length) {
    return (
      <div className="empty-page-message">
        <div>Your flashcards are empty. Creat dashboard with words first</div>
        <a href="/dashboards"> Create first dashboard</a>{" "}
      </div>
    );
  }

  if (wordToGuess && isGameOver) {
    return (
      <div className="game-result-container">
        <div>{hasWon ? "Congrats!" : "Sorry! You used all your quesses"}</div>
        <button onClick={startAgain} className="play-again-btn">
          Play again
        </button>
      </div>
    );
  }

  return (
    <React.Fragment>
      <div className="select-dashboard-container">
        <select
          name=""
          id="selectDashboard"
          className="text-input"
          onChange={(event) =>
            setSelectedDashboard(
              dashboards.find(
                (dashboard) => dashboard.id === Number(event.target.value)
              )
            )
          }
        >
          {dashboards.map((dashboard) => (
            <option value={dashboard.id} key={dashboard.id}>
              {dashboard.title}
            </option>
          ))}
        </select>
      </div>

      {wordToGuess ? (
        <div>
          <WordToGuess
            wordToGuess={wordToGuess}
            guessedLettersSet={guessedLettersSet}
          />
          <div className="letters-btn-container">
            {language &&
              language.split("").map((letter) => (
                <button
                  key={letter}
                  disabled={guessedLettersSet.has(letter)}
                  onClick={() => onLetterClick(letter)}
                  className="letter-btn"
                >
                  {letter}
                </button>
              ))}
          </div>
          <div className="count-guess-block">
            Number of guesses {userChoiceCount} / {limit}
          </div>
        </div>
      ) : (
        <div className="empty-page-message">
          This dashboard is empty. You have to add words first or select another
          one
        </div>
      )}
    </React.Fragment>
  );
}
ReactDOM.render(<GuessWordPage />, document.getElementById("guessWordPage"));
