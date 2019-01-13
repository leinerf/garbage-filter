import React from 'react';
import { Text, View, TouchableOpacity, Button, Image } from 'react-native';
import { Camera, Permissions } from 'expo';

export default class CameraExample extends React.Component {
  constructor(){
    super()
    this.state = {
      hasCameraPermission: null,
      type: Camera.Constants.Type.back,
      takenPhoto: false,
      photoURI: "",
      photoLabel: null
    };
  }
  

  async componentDidMount() {
    const { status } = await Permissions.askAsync(Permissions.CAMERA);
    this.setState({ hasCameraPermission: status === 'granted' });
  }

  postPicture() {
    const apiUrl = "http://8c6f9fa0.ngrok.io/picture/";
    const uri = this.state.photoURI.uri;
    console.log(uri)
    const uriParts = uri.split('.');
    const fileType = uriParts[uriParts.length - 1];
    const formData = new FormData();
        formData.append('photo', {
          uri,
          name: `photo.${fileType}`,
          type: `image/${fileType}`,
        });
    const options = {
          method: 'POST',
          body: formData,
          headers: {
            Accept: 'application/json',
            'Content-Type': 'multipart/form-data',
          },
        };
    
    return fetch(apiUrl, options);
  }
  
  sendToApi = async() => {
    const response = await this.postPicture().then((promise) => (promise.json())).then((json) => (json))
    console.log("it finish sending response")
    this.setState({photoLabel: response["message"][0]})
  }

  snap = async () => {
    if (this.camera) {
      let photo = await this.camera.takePictureAsync();
      this.setState({ takenPhoto: true});
      this.setState({photoURI: photo})
    }
  };

  render() {
    const { hasCameraPermission, takenPhoto, photoURI, photoLabel } = this.state;
    console.log(photoLabel)
    if (hasCameraPermission === null) {
      return <View />;
    } else if (hasCameraPermission === false) {
      return <Text>No access to camera</Text>;
    } else {
      return (
        <View style={{ flex: 1}}>
        {takenPhoto ? 
          <Image
          style={{width: 250, height: 250, alignSelf:"center", marginTop: 100}}
          source={{uri: photoURI.uri}}
          /> : 
          <Camera style={{ flex: 0.3, }} type={this.state.type} ref={ref => { this.camera = ref; }}>
            <View
              style={{
                flex: 1,
                backgroundColor: 'transparent',
                flexDirection: 'row',
              }}>
              <TouchableOpacity
                style={{
                  flex: 0.1,
                  alignSelf: 'flex-end',
                  alignItems: 'center',
                }}
                onPress={() => {
                  this.setState({
                    type: this.state.type === Camera.Constants.Type.back
                      ? Camera.Constants.Type.front
                      : Camera.Constants.Type.back,
                  });
                }}>
                <Text
                  style={{ fontSize: 18, marginBottom: 10, color: 'white' }}>
                  {' '}Flip{' '}
                </Text>
              </TouchableOpacity>
            </View>
          </Camera>
          
        }
        <Button onPress={this.snap}
          title="Capture Photo"
          color="#841584"
          accessibilityLabel="Learn more about this purple button"
        />
        {takenPhoto ?
        <Button onPress={this.sendToApi}
          title="Analyze"
          color="#841004"
          accessibilityLabel="Learn more about this purple button"
        />:
        <Text>Take photo to analyze</Text>
        }
        {photoLabel != null?
          <View style={{alignSelf:"center"}}>
            <Text>This is {photoLabel.tagName}</Text>
            <Text>With a {photoLabel.probability}</Text>
          </View>
          :
          <Text>Nothing has been labeled yet</Text>
        }
        </View>
      );
    }
  }
}

