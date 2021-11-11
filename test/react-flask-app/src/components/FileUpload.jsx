import React from 'react';
import './App.css';
import blur from "./static/blurred.png";
class FileUpload extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      file: blur,
    }    
    this.handleChange = this.handleChange.bind(this)
    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleChange(event) {
    this.setState({
      file: URL.createObjectURL(event.target.files[0])
    })
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
    return (
      <div>
        <form onSubmit={this.handleUploadImage} class="container">
          <div>
            <input ref={(ref) => { this.uploadInput = ref; }} type="file" onChange={this.handleChange}/>
          </div>
          <div>
            <button>Upload</button>
          </div>
        </form>
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
      </div>

    );
  }
}

export default FileUpload;