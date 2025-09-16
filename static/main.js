const API_URL = "http://127.0.0.1:8000";

async function loadPlaylists() {
    response = await fetch(API_URL+"/playlists/")
    playlists = await response.json();

    const ul = document.getElementById("playlist-list")
    ul.innerHTML = "";
    playlists.array.forEach(p => {
        const li = document.createElement("li")
        li.textContent = p.name;
        // li.onclick = () => loadSongs(p.id);
        ul.appendChild(li);
    });
}

async function loadSongs(playlistId) {
    const response = await fetch();
}