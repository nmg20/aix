import { useCallback, useState } from "react";
import { parsePlaylist, downloadFromPlaylist } from "./services/api";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [songs, setSongs] = useState([]);
  const [selected, setSelected] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleParse = async () => {
    if (!url) return alert("Introduce la URL de la playlist");
    setLoading(true);
    setError(null);
    try {
      const res = await parsePlaylist(url);
      setSongs(res);
    } catch (err) {
      console.error("Error al parsear playlist:", err);
    } finally {
      setLoading(false);
    }
  };

  const toggleSelect = (song) => {
    setSelected((prev) =>
      prev.includes(song.url)
        ? prev.filter((s) => s !== song.url)
        : [...prev, song.url]
    );
  };


  const handleDownload = async () => {
    if (!selected.length)
      return alert("Ningun tema seleccionado.")
    try {
      setLoading(true);
      const res = await downloadFromPlaylist(selected);
      if (res.zipUrl) window.open(res.zipUrl, "_blank");
      else alert("Descarga iniciada");
    } catch (error) {
      console.error(error);
      alert("Descarga fallida");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="card">
        <h1>Procesar playlist (Youtube)</h1>

        {/* FORMULARIO */}
        <form onSubmit={(e) => { e.preventDefault(); handleParse(); }}>
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="URL de la playlist"
          />
          <button type="submit">Procesar</button>
        </form>

        {/* ESTADO */}
        {loading && <p>Procesando...</p>}
        {error && <p className="error">{error}</p>}

        {/* LISTA */}
        {songs.length > 0 && (
          <div className="results">
            <ul>
              {songs.map((song, i) => (
                <li key={i}>
                  <span>
                    <strong>{song.title}</strong>
                  </span>
                  <input
                    type="checkbox"
                    checked={selected.includes(song.url)}
                    onChange={() => toggleSelect(song)}
                  />
                </li>
              ))}
            </ul>
            <button onClick={handleDownload} className="download-btn">
              Descargar seleccionadas
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;