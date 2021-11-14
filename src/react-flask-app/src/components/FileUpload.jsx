import React from 'react';
import './App.css';
import blur from "./static/blurred.png";
import fin from "./static/fin.jpeg";

class FileUpload extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      file: blur,
      compressed: blur,
      value: 50,
      timeTaken: 0,
      downloadlink : "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
      isCompressed: false,
    }    
    this.handleChange = this.handleChange.bind(this)
    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleValueChange(event){
    event.preventDefault();
    const inputValue = event.target.value;
    this.setState({
      value: inputValue
    })
  }

  

  handleChange(event) {
    event.preventDefault();
    this.setState({
      file: URL.createObjectURL(event.target.files[0])
      // compressed: blur
    })
  }
  handleCheckbox = Evn => {
    Evn.preventDefault();
    console.log(Evn.target.value)
  }
  
 handleUploadImage(ev) {
  ev.preventDefault();
  ev.stopPropagation();
  ev.nativeEvent.stopImmediatePropagation();

   const data = new FormData();
   data.append('file', this.uploadInput.files[0]);
   data.append('filename', this.uploadInput.files[0].name); 
    data.append('ratio', this.state.value);

    
    if (this.uploadInput.files[0] !== undefined) {
      var startDate = Date.now();
      const config = {
        method: 'POST',
        body: data,
      }
      fetch('http://localhost:5000/upload', config)
      .then(() => {
        const postcompressionsrc = 'compress'.concat(this.uploadInput.files[0].name);
        var endDate = (Date.now() - startDate)/1000; 
        this.setState({
          compressed: "http://127.0.0.1:5000/view/".concat(postcompressionsrc),
          downloadlink: "http://127.0.0.1:5000/download/".concat(postcompressionsrc),
          timeTaken : endDate,
          isCompressed : true
        });
      })
    }
    return false;
  }

  
  
  render() {
    let downloadImg;
    if (this.state.isCompressed){
      downloadImg = (
        <div class="downloadBox">
          <button class="download" onClick={() => window.open(this.state.downloadlink)}>Download</button>
          <text class="time">Time taken: {this.state.timeTaken} seconds</text>
        </div>
        )
    }
    return (
      <div>
          <form onSubmit={(event) => {event.preventDefault(); this.handleUploadImage(event)}} class="container">
            <div>
              <input ref={(ref) => { this.uploadInput = ref; }} type="file" onChange={this.handleChange}/>
              <button>Convert!</button>
            </div>
            <div class="compressionText">
            <text>Compression Ratio</text>
            </div>
            <div class="inputLine">
              <input class="slider" type="range" min="0" max="100" value="50" value={this.state.value} onChange={(event) => {this.handleValueChange(event)}}></input>
              <input class="value" type="number" id="ratio" name="ratio" min="1" max="100" value={this.state.value} onChange={(event) => {this.handleValueChange(event)}}></input>
              {/* <text>{this.state.value}</text> */}
            </div>
           {/* <div class="inputCheck">
              <input type="checkbox" onChange={this.handleCheckbox} value="true"></input>
              <text>Check to transparent the background</text>
            </div> */}
          </form>
        {/* {imageForm} */}
        <div class="container">
          <div class="imageBox">
            <h3> Before </h3>
            <img src={this.state.file} alt="beforeIMG"></img>
          </div>
          <div class="imageBox">
            <h3> After </h3>
            <img src={this.state.compressed} alt="afterIMG"></img>
            {downloadImg}
          </div>
        </div>
      </div>

    );
  }
}

export default FileUpload;