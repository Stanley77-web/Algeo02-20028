import React from 'react';
import './App.css';
import blur from "./static/blurred.png";
import axios from 'axios';
class FileUpload extends React.Component {
  constructor(props) {
    super(props);
    var running = 0;
    var startTime;


    this.state = {
      file: blur,
      compressed: blur,
      value: 50,
      time: 0,
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
   const data = new FormData();
   ev.preventDefault();
   data.append('file', this.uploadInput.files[0]);
    data.append('filename', this.uploadInput.files[0].name); // idk how to delete this ill just let it be
    data.append('ratio', this.state.value);
    // const objectURL = window.URL.createObjectURL(this.uploadInput.files[0]);
    
    if (this.uploadInput.files[0] !== undefined) {
      var startDate = Date.now();
      const config = {
        method: 'POST',
        body: data,
      }
      fetch('http://localhost:5000/upload', config).then(() => {
        const postcompressionsrc = 'converted_'.concat(this.uploadInput.files[0].name);
        this.setState({
          compressed: process.env.PUBLIC_URL + postcompressionsrc
        });
        var endDate = (Date.now() - startDate); 
        console.log(endDate);
        alert(endDate);
        if (module.hot && process.env.NODE_ENV !== 'production') {
          module.hot.accept();
          }
      })
      // .then((response) => {
      //   this.setState({
      //     compressed: process.env.PUBLIC_URL + 'converted_ngetest.png'
      //   });
      // })
      // .catch((err) => {
      //   alert("jancok");
      // })
      // compressed: postcompressionsrc,
      // ev.preventDefault();
      
      // .then(() => {
      //   const postcompressionsrc = "./static/".concat('converted_', this.uploadInput.files[0].name);
      //   const testImg = require("./static/user_uploaded/algeo3.jpg")
      //   this.setState({
      //     compressed: test,
      //   })
      // })
    }
  }

  
  
  render() {
    // let imageForm;
    // imageForm = (
    // )

    return (
      <div>
          <form onSubmit={this.handleUploadImage} class="container">
            <div>
              <input ref={(ref) => { this.uploadInput = ref; }} type="file" onChange={this.handleChange}/>
              <button>Upload</button>
            </div>
            <div class="compressionText">
            <text>Compression Ratio</text>
            </div>
            <div class="inputLine">
              <input class="slider" type="range" min="0" max="100" value="50" value={this.state.value} onChange={(event) => {this.handleValueChange(event)}}></input>
              <input class="value" type="number" id="ratio" name="ratio" min="1" max="100" value={this.state.value} onChange={(event) => {this.handleValueChange(event)}}></input>
              {/* <text>{this.state.value}</text> */}
            </div>
            <div class="inputCheck">
              <input type="checkbox" onChange={this.handleCheckbox} value="true"></input>
              <text>Check to transparent the background</text>
            </div>
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
          </div>
        </div>
        <form>
          <button>Download</button>
        </form>
      </div>

    );
  }
}

export default FileUpload;