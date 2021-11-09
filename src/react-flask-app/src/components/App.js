import React from 'react';
import './App.css';
import FileUpload from './FileUpload.jsx';

function App() {
  // const [currentTime, setCurrentTime] = useState(0);
  const ColoredLine = ({ color }, { height }) => (
    <hr
        style={{
            color: color,
            backgroundColor: color,
            height: height
        }}
    />
  );

  // useEffect(() => {
  //   fetch('/time').then(res => res.json()).then(data => {
  //     setCurrentTime(data.time);
  //   });
  // }, []); 
  // contoh api tp nanti blm diedit

  return (
    <div class="all-page">
      <h1 class="main-title">waifu0.5x</h1>
      <ColoredLine color="black" height="3" ></ColoredLine>
      <text class="shortdesc"><br></br>Single-Image Anime-Style Art downsizing using Singular Value Decomposition. And it supports other photos, if you're in to that.</text>
      <FileUpload></FileUpload>
    </div>
  );
}

export default App;