import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const parsePlaylist = async (url, page=1, size=20, search="") => {
  params: { 
    url , page, size
  }
  if (search) params.search = search
  const response = await axios.get(
    `${API_URL}/playlists/parse`,
      { params }
  );
  return response.data;
};


export const downloadFromPlaylist = async (urls) => {
  const response = await axios.post(`${API_URL}/playlists/download`, { urls });
  return response;
};
