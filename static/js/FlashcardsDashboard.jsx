function FlashcardsDashboard({ title, words }) {
  const [index, setIndex] = React.useState(0);
  const [flippedWord, setFlippedWord] = React.useState();

  function nextWord() {
    index === words.length - 1 ? setIndex(0) : setIndex(index + 1);
  }

  function prevWord() {
    index === 0 ? setIndex(words.length - 1) : setIndex(index - 1);
  }

  return (
    <div className="container">
      {words[index] ? (
        <div className="flash-card-container">
          <FlashcardItem
            term={words[index].term}
            definition={words[index].definition}
          />
          <div className="toggle-cards">
            <button onClick={prevWord} className="btn-toggle-card">
              Previous
            </button>
            <div>
              {index + 1}/{words.length}
            </div>
            <button onClick={nextWord} className="btn-toggle-card">
              Next
            </button>
          </div>
        </div>
      ) : (
        <div>This dashboard is empty. You have to add words first</div>
      )}
    </div>
  );
}
