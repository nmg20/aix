import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const parsePlaylist = async (url) => {
  const response = await axios.get(`${API_URL}/playlists/parse`, {
    params: { url }
  });
  return response.data;
};


export const downloadFromPlaylist = async (urls) => {
  const response = await axios.post(`${API_URL}/playlists/download`, { urls });
  return response;
};
