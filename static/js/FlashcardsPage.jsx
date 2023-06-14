function FlashcardsPage() {
  const [flashcards, setFlashcards] = React.useState([]);
  const [selectedDashboardId, setSelectedDashboardId] = React.useState(false);

  React.useEffect(() => {
    fetch("/api/flashcards")
      .then((response) => response.json())
      .then((data) => {
        setFlashcards(data);
        setSelectedDashboardId(data[0].id);
      });
  }, []);

  const selectedDashboard = flashcards.find(
    (flashcard) => flashcard.id === selectedDashboardId
  );
  return (
    <React.Fragment>
      {flashcards.length ? (
        <div className="select-flashcard-container ">
          <select
            name=""
            className="text-input"
            id="selectDashboard"
            onChange={(event) =>
              setSelectedDashboardId(Number(event.target.value))
            }
          >
            {flashcards.map((card) => (
              <option value={card.id} key={card.id}>
                {card.title}
              </option>
            ))}
          </select>
        </div>
      ) : (
        <div className="empty-page-message">
          <div>Your flashcards are empty. Creat dashboard with words first</div>
          <a href="/dashboards"> Create first dashboard</a>{" "}
        </div>
      )}

      {selectedDashboard && (
        <FlashcardsDashboard
          key={selectedDashboard.id}
          title={selectedDashboard.title}
          words={selectedDashboard.words}
        />
      )}
    </React.Fragment>
  );
}

ReactDOM.render(<FlashcardsPage />, document.getElementById("flashcards"));
