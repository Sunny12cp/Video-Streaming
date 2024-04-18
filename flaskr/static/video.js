const socket = io();
const url = window.location.href
const room = url.split("/").pop();

const video = document.getElementById("video");

Object.defineProperty(HTMLMediaElement.prototype, "playing", {
  get : function() {
    return !!(this.currentTime > 0 && !this.paused && !this.ended &&
              this.readyState > 2);
  }
})

socket.on("connect", () => { socket.emit("join", room); });

socket.on("check", (data) => {
  if (data["state"] === "play" && !video.playing) {
    video.currentTime = data["time"];
    video.play();
  } else if (data["state"] === "pause" && video.playing) {
    video.currentTime = data["time"];
    video.pause();
  }
});

function playVideo() {
  socket.emit("check", {state : "play", time : video.currentTime, room : room});
}

function pauseVideo() {
  socket.emit("check",
              {state : "pause", time : video.currentTime, room : room});
}

video.addEventListener("play", playVideo);
video.addEventListener("pause", pauseVideo);
