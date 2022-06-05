# Send audio data to Omniverse Audio2Face

### Prerequisites

* Windows PC or workstation with Nvidia RTX GPU
* Download and Install Omniverse Launcher

  * [NVIDIA Omniverse install guide](https://docs.omniverse.nvidia.com/prod_install-guide/prod_install-guide.html)
  * Download Omniverse Launcher [here](https://www.nvidia.com/en-us/omniverse/download/).
  * Omniverse installation [video tutorial](https://www.youtube.com/watch?v=Ol-bCNBgyFw)

* Install [Omniverse Audio2Face](https://www.nvidia.com/en-us/omniverse/apps/audio2face/). Next, simply install Omniverse Audio2Face and you're good to go.

| ![](https://i.imgur.com/N94KDTc.png) |
|:--:|
| *Omniverse Audio2Face* |

### Omniverse Audio2Face setup

To get our Python program interacts with Omniverse Audio2Face, you should use streaming audio player that allows developers to stream audio data from an external source or applications via the gRPC protocol.

| ![](https://i.imgur.com/qZUQVS0.png) |
|:--:|
| *streaming audio player allows developers to stream audio data from an external source* |

1. following steps this [tutorial](https://www.youtube.com/watch?v=qKhPwdcOG_w&t=17s), in your Omniverse audio2face app, create an audio player and connect it to the audio2face instance using the omnigraph editor.
1. Prepare a wave file, e.g. `placeholder.wav`
1. On the Windows, install python3 and packages required by `test_audio2face.py`, run `python3 test_audio2face.py`

### Reference

* Overview of Streaming Audio Player in Omniverse Audio2Face: [Youtube](https://youtu.be/qKhPwdcOG_w)
* omni.audio2face.player: `C:\Users\{NAME}\AppData\Local\ov\pkg\audio2face-2021.3.2\exts\omni.audio2face.player`
* default wav files: `C:\Users\{NAME}\AppData\Local\ov\pkg\audio2face-2021.3.2\exts\omni.audio2face.player_deps\deps\audio2face-data\tracks`
* <https://github.com/metaiintw/build-an-avatar-with-ASR-TTS-Transformer-Omniverse-Audio2Face>
