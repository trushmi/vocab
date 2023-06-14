function WordToGuess({ wordToGuess, guessedLettersSet }) {
  return (
    <div className="intro-section">
      <div className="guess-word-title">Guess the word:</div>
      <div className="guess-word-description">{wordToGuess.definition}</div>
      <div className="guess-word-container">
        {wordToGuess.term.split("").map((letter, index) => (
          <div key={index} className="single-letter-to-guess">
            {guessedLettersSet.has(letter) ? letter : ""}
          </div>
        ))}
      </div>
    </div>
  );
}
