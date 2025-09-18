import { useState } from "react";
import { parsePlaylist, downloadFromPlaylist } from "./services/api";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [songs, setSongs] = useState([]);
  const [selectedSongs, setSelectedSongs] = useState([]);

  const handleParse = async () => {
    const data = await parsePlaylist(url);
    setSongs(data.songs);
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
          defaultValue={"https://www.youtube.com/watch?v=W-UepwIyHfc&list=PLR-pSqh8ddm3FQM_eMiCfXqTwDK8qLRMt&pp=gAQB"}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="URL de la playlist"
        />
        <button onClick={handleParse}>Procesar</button>

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