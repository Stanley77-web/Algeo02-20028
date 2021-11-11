import React from 'react';
import './App.css';
import blur from "./static/blurred.png";
class FileUpload extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageLink: '',
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);
    data.append('filename', "image"); // idk how to delete this ill just let it be
    const objectURL = window.URL.createObjectURL(this.uploadInput.files[0]);
    
    fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      body: data,
    })
    .then((response) => {
      response.json().then((body) => {
        this.setState({ imageLink: {objectURL} });
      });
    });
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleUploadImage} class="container">
          <div>
            <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
          </div>
          <div>
            <button>Upload</button>
          </div>
          <img src="{{ url_for('display_image', filename='bg.png') }}" alt="img" />
        </form>
        <div class="container">
         {/* <img src={} alt="img"></img> */}
        </div>
      </div>

    );
  }
}

export default FileUpload;