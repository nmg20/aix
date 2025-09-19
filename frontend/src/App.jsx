import { useState } from "react";
import { parsePlaylist, downloadFromPlaylist } from "./services/api";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [songs, setSongs] = useState([]);
  const [selectedSongs, setSelectedSongs] = useState([]);
  const [page, setPage] = useState([]);
  const [totalPages, setTotalPages] = useState(1);

  const handleParse = async (newPage = 1) => {
    const data = await parsePlaylist(url, newPage, 20);
    setSongs(data.items);
    setPage(newPage);
    setTotalPages(data.pages);
  };

  function toggleSelectSong(songUrl) {
    setSelectedSongs(prev =>
      prev.includes(songUrl)
        ? prev.filter(u => u !== songUrl)
        : [...prev, songUrl]
    );
  }

  function handleDownload() {
    downloadFromPlaylist(selectedSongs);
  }

  return (
    <div className="app">
      <div className="content">
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="URL de la playlist"
        />
        <button onClick={() => handleParse(1)}>Procesar</button>

      {songs.length> 0 && (
          <div className="playlist-container">
            <div className="song-list">
              {songs.map((song, i) => (
                <div className="song-item" key={song.url}>
                  <span>{song.title}</span>
                  <div
                    className={`circle ${selectedSongs.includes(song.url) ? 'selected' : ''}`}
                    onClick={() => toggleSelectSong(song.url)}
                  />
                </div>
              ))}
            </div>
            <div className="song-pages">
              <span className="page-arrow"
                disabled = {page === 1}
                onClick = {() => handleParse(page - 1)}>
                  &lt;
              </span>

              {[...Array(totalPages)].map((_, i) => {
                const pageNum = i + 1;
                return (
                  <span
                    key={pageNum}
                    className={`page-number ${pageNum === page ? "active" : ""}`}
                    onClick={() => handleParse(pageNum)}
                  >
                    {pageNum}
                  </span>
                );
              })}

              <span className="page-arrow"
                disabled = {page === totalPages}
                onClick = {() => handleParse(page + 1)}>
                  &gt;
              </span>
            </div>
            <button className="download-btn" onClick={handleDownload}>
              Descargar
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;