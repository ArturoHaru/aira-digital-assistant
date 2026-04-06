
# {project_name}

<div align="center">
  <img src="logo.png" alt="{project_name} Logo" width="200" height="200">
  
  <p># Aira Digital Assistant

    <strong>{project_description}</strong>
  </p>
  
</div>

## 🌟 Overview
Aira is a digital assistant interface that uses local llm to talk to your Home Assistant installation. It uses the Speaches service to transcribe and synthesize.

## ✨ Features

- **Privacy first** - Built with privacy in mind
- **Responsive** - The web page works on every device with a microphone
-  **Control devices** - Control your devices with your voice through the Home Assistant integration

## 🎯 Quick Start

### Prerequisites

- Docker
- Home Assistant - [get it here](https://www.home-assistant.io/installation)
- Speaches - [get it here](https://speaches.ai/)
- A NVIDIA GPU with 4Gb of VRAM or more
- A linux environment that supports docker GPU passthrough
- (optional) Https. Only needed if the frontend is gonna be run on a different machine than the backend. 

### Installation with docker

1. **Clone the repository**
   ```bash
   git clone --recurvise https://github.com/{username}/{project_name}.git
   cd {project_name}
   ```

2. **Fill out all the dummy.env file fields in the aira-express and rename it to .env**
   ```bash
   #aira-express/dummy.env
    LLM_WEBSOCKET=
    LLM_MODEL=
    HOME_ASSISTANT_BASE_URL=
    HOME_ASSISTANT_TOKEN=
    SPEACHES_BASE_URL=
    OPENWAKEWORD_ENDPOINT=
    SPEACHES_TRANSCRIPTION_MODEL=
    SPEACHES_SYNTHESIS_MODEL=
    SPEACHES_SYNTHESIS_VOICE=
    CHROMA_VOLUME_LOCATION=
   ```

3. (Optional) **Set the server URL in the environment.ts file**
If you are going to use the frontend on a different machine than the backend, change serverUrl line in the environment.ts file. Otherwise, you can skip this step.
"localhost"  -> your server url (you need to use https or the browser will block  microphone input). 
```typescript
# in aira-angular/src/environment.ts
export const environment = {
  production: true,
  serverUrl: 'http://localhost/api', // change this line 
  interactionEndpoint: '/interaction',
  transcriptionEndpoint: '/speaches/transcribe',
  transcriptionModel: 'kp-forks/faster-whisper-small',
  openwakewordEndpoint: '/check_wakeword',
};
```
TODO work in progress... There are more steps, I will push all the changes soon

### Ways to Contribute

- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests

## 📊 Roadmap

- [ ] Web searches
- [ ] Set timer and reminders
- [ ] Auto Device discovery
- [x] ~~Adaptability~~

See the [open issues](https://github.com/{username}/{project_name}/issues) for a full list of proposed features and known issues.


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
