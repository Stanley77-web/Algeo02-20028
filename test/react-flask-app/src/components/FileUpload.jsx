import React from 'react';
import './App.css';
class FileUpload extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);
    data.append('filename', "useless"); // idk how to delete this ill just let it be

    fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        this.setState({ imageURL: `http://localhost:3000/${body.file}` });
      });
    });
  }

  render() {
    return (
      <form onSubmit={this.handleUploadImage}>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
        </div>
        <div>
          <button>Upload</button>
        </div>
        {/* <img src="{{ url_for('display_image', filename='bg.png') }}" alt="img" /> */}
      </form>
    );
  }
}

export default FileUpload;