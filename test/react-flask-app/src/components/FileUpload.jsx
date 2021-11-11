import React from 'react';
import './App.css';
import blur from "./static/blurred.png";
class FileUpload extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      file: blur,
      value: 50,
    }    
    this.handleChange = this.handleChange.bind(this)
    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleValueChange(event){
    const inputValue = event.target.value;
    this.setState({
      value: inputValue
    })
  }

  handleChange(event) {
    this.setState({
      file: URL.createObjectURL(event.target.files[0])
    })
  }
  handleCheckbox = Evn => {
    console.log(Evn.target.value)
  }
  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);
    data.append('filename', "image"); // idk how to delete this ill just let it be
    // const objectURL = window.URL.createObjectURL(this.uploadInput.files[0]);
    
    if (this.uploadInput.files[0] !== undefined) {
      fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: data,
      })
      // .then((response) => {
      //   response.json().then((body) => {
      //     this.setState({ imageLink: URL.createObjectURL(this.uploadInput.files[0])});
      //   });
      // });
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
            <div>
            </div>
            <div class="inputLine">
              <input class="value" type="number" id="ratio" name="ratio" min="1" max="100" value={this.state.value} onChange={(event) => {this.handleValueChange(event)}}></input>
              <input class="slider" type="range" min="0" max="100" value="50" value={this.state.value} onChange={(event) => {this.handleValueChange(event)}}></input>
              <text>{this.state.value}</text>
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
            <img src={blur} alt="afterIMG"></img>
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