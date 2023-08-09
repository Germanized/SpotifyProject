// script.js

document.addEventListener("DOMContentLoaded", function () {
  const fetchSongsBtn = document.getElementById("fetch-songs-btn");
  const topSongsList = document.getElementById("top-songs-list");

  fetchSongsBtn.addEventListener("click", function () {
    // Replace this with your actual code to fetch and display songs
    // For demonstration purposes, I'll add a sample song to the list
    const sampleSong = "Sample Song";
    const li = document.createElement("li");
    li.textContent = sampleSong;
    topSongsList.appendChild(li);
  });
});
