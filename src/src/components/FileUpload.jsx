import React from 'react';
import './App.css';
import blur from "./static/blurred.png";
import spin from "./static/punch.gif";

class FileUpload extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      file: blur,
      compressed: blur,
      value: 50,
      pixelDiff: 50,
      timeTaken: 0,
      downloadlink : "https://www.tomorrowtides.com/nft-bu-reini-telah-terjual-dengan-harga-23-juta.html",
      isCompressed: false,
      isCompressing: false,
    }    
    this.handleImageChange = this.handleImageChange.bind(this)
    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleValueChange(event){
    event.preventDefault();
    const inputValue = event.target.value;
    this.setState({
      value: inputValue
    })
  }

  

  handleImageChange(event) {
    event.preventDefault();
    this.setState({
      file: URL.createObjectURL(event.target.files[0]),
      compressed: blur,
      isCompressed: false,
    })
  }
  
 handleUploadImage(ev) {
  ev.preventDefault();
  ev.stopPropagation();
  ev.nativeEvent.stopImmediatePropagation();

  if (this.uploadInput.files[0] !== undefined) {
      this.setState({
        isCompressing: true,
      })
      const filename = this.uploadInput.files[0].name
      const data = new FormData();
      data.append('file', this.uploadInput.files[0]);
      data.append('filename', filename); 
      data.append('ratio', this.state.value);
      var startDate = Date.now();
      const config = {
        method: 'POST',
        body: data,
      }
      fetch('http://localhost:5000/compress', config)
      .then(() => {
        const postcompressionsrc = 'compress'.concat(filename);
        var endDate = (Date.now() - startDate)/1000; 
        this.setState({
          compressed: "http://127.0.0.1:5000/view/".concat(postcompressionsrc),
          downloadlink: "http://127.0.0.1:5000/download/".concat(postcompressionsrc),
          timeTaken : endDate,
          pixelDiff: 100 - this.state.value,
          isCompressed : true,
          isCompressing: false,
        });
      })
    }
  }

  
  
  render() {
    let downloadImg;
    if (this.state.isCompressed){
      downloadImg = (
        <div class="downloadBox">
          <button class="download" onClick={() => window.open(this.state.downloadlink)}>Download</button>
          <text class="time">Time taken: {this.state.timeTaken} seconds<br></br></text>
          <text class="pixel">Pixel difference: {this.state.pixelDiff}%</text>
        </div>
        )
    }

    let form;
    if (this.state.isCompressing){
      form = (
        <div>
          <h3>Compressing..</h3>
          <img class="loading" src={spin} alt="loading"></img>
        </div>
      )
    }
    else{
      form = (
        <div>
          <form onSubmit={(event) => {event.preventDefault(); this.handleUploadImage(event)}} class="container">
            <div>
              <input ref={(ref) => { this.uploadInput = ref; }} type="file" onChange={this.handleImageChange}/>
              <button>Convert!</button>
            </div>
            <div class="compressionText">
            <text>Compression Ratio</text>
            </div>
            <div class="inputLine">
              <input class="slider" type="range" min="1" max="100" value="50" value={this.state.value} onChange={(event) => {this.handleValueChange(event)}}></input>
              <input class="value" type="number" id="ratio" name="ratio" min="1" max="100" value={this.state.value} onChange={(event) => {this.handleValueChange(event)}}></input>
            </div>
          </form>
        </div>
      )
    }

    return (
      <div>
        {form}
        <div class="container">
          <div class="imageBox">
            <h3> Before </h3>
            <img class="userImg" src={this.state.file} alt="beforeIMG"></img>
          </div>
          <div class="imageBox">
            <h3> After </h3>
            <img class="userImg" src={this.state.compressed} alt="afterIMG"></img>
            {downloadImg}
          </div>
        </div>
      </div>
    );
  }
}

export default FileUpload;