function FlashcardItem({ term, definition }) {
  let termToUperCase = term[0].toUpperCase() + term.slice(1);
  const [isFlipped, setIsFlipped] = React.useState();

  function flipCard() {
    return setIsFlipped(!isFlipped);
  }

  return (
    <div
      className={`flash-card-wrapper${isFlipped ? " flash-card-outline" : ""}`}
    >
      <div onClick={flipCard} className="flash-card">
        <div className="card-front">{termToUperCase}</div>
        <div className="card-back">{definition}</div>
      </div>
    </div>
  );
}
