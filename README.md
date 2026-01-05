# Audio-Visual Software Architecture

This repository provides the **top-level orchestration and documentation** of a modular **Audio-Visual Sensor Fusion Software Architecture** developed for reproducible research on multi-modal detection, localization, tracking, and evaluation of moving speakers in indoor environments.

The repository serves as an **umbrella project** that integrates all software modules of the pipeline as **Git submodules**, alongside experimental data and thesis documentation.

![Architecture Overview](assets/AVSensorFusionArchitecture.svg)

---

## Overview

The complete processing pipeline consists of the following stages:

1. **Visual Scene Simulation** (Unity)
2. **Room Acoustics Simulation** (gpuRIR)
3. **Video Detector** (CNN-based object detection)
4. **Audio Detector** (3D positional sound source localization)
5. **Audio-Visual Sensor Fusion** (multi-object tracking)
6. **Tracking Evaluation** (HOTA / TrackEval)

Each stage is implemented as an **independent software module** and linked through standardized JSONL interfaces.

---

## Software Modules
Refer to the README of each git submodule repository for details.

### Visual Scene Simulation (Unity)
**Submodule:** `visualsimulationunity`

- Generates synthetic RGB and depth images
- Simulates fisheye cameras and dynamic human motion
- Exports time-stamped 3D ground-truth speaker positions

---

### Room Acoustics Simulation
**Submodule:** `gpuRIR`

- GPU-accelerated image source method (ISM)
- Generates room impulse responses (RIRs)
- Renders multi-channel microphone signals for moving speakers

---

### Video Detector
**Submodule:** `cnnvideodetektor`

- CNN-based video object detection
- Processes RGB image streams
- Outputs 3D video detections

---

### Audio Detector (3D-SSL)
**Submodule:** `ssl4ips`

- Closed-form analytical 3D positional sound source localization
- Uses β-GCC-PHAT for TDOA estimation
- Outputs audio localization detections in world coordinates

---

### Audio-Visual Sensor Fusion
**Submodule:** `audiovisualsensorfusion`

- Implements MS-GLMB multi-object tracking
- Fuses audio and video detections
- Handles track birth, death, and uncertainty

---

### Tracking Evaluation
**Submodule:** `trackeval`

- Uses TrackEval HOTA reference implementation
- Compares predicted tracks with ground-truth
- Reports detection, association, and localization metrics

---

## Data Flow and Interfaces

All modules communicate through **well-defined JSONL interfaces**:

- `groundtruth_sources.jsonl`
- `audio_localizations.jsonl`
- `video_localizations.jsonl`
- `fusion_tracks.jsonl`

This design allows:
- Modular replacement of algorithms
- Independent evaluation of components
- Reproducible experimentation

---

## Generated Experiment (Scenario) Folder Structure

Each simulation session follows a standardized directory structure shared across all software modules:

```
📁 experiment_001/
├── config.json
├── groundtruth_sources.jsonl
├── audio/
│   └── wav/
│       └── multichannel_audio_<timestamp>.wav
├── video/
│   ├── rgb/
│   │   └── RGB_frame_<timestamp>.png
│   └── depth/
│       └── Depth_frame_<timestamp>.png
├── localization/
│   ├── audio_localizations.jsonl
│   └── video_localizations.jsonl
└── tracking/
    ├── audio_tracking.jsonl
    ├── video_tracking.jsonl
    └── audio_video_tracking.jsonl
```

## Master’s Thesis Results

The following table summarizes the **combined tracking results over all scenarios**, as reported in the master’s thesis.

| Modality | HOTA ↑ | DetA ↑ | AssA ↑ | DetRe ↑ | DetPr ↑ | AssRe ↑ | AssPr ↑ | LocA ↑ |
|--------|--------|--------|--------|---------|---------|---------|---------|--------|
| M1 (Audio)          | 26.32 | 18.08 | 38.40 | 18.26 | 93.59 | 38.92 | 89.60 | 92.66 |
| M2 (Video)          | 68.54 | 68.61 | 68.49 | 70.40 | 93.10 | 70.17 | 93.74 | 91.83 |
| M3 (Audio + Video)  | **70.29** | 69.38 | 71.24 | 71.18 | 93.39 | 72.88 | 93.97 | 92.04 |

The results demonstrate that for the dataset MOT25A, MOT25V, MOT25AV, the **audio-visual fusion outperforms unimodal tracking**, particularly in terms of association accuracy and overall HOTA score.

---


## Publication

If you use this code, please cite the following papers:

```
@INPROCEEDINGS{2025_Sillekens_3DSSL_SRP,
  author={L. Sillekens and O. Rudolf and M. Thißen and I. Penner and S. Seyfarth and E. Hergenröther and J.-P. Akelbein},
  booktitle={2025 10th International Conference on Frontiers of Signal Processing (ICFSP)},
  title={A Non-invasive Measurement System for Evaluating 3D Indoor Sound Source Localization Techniques},
  year={2025},
  keywords={3D positional sound source localization, indoor microphone array geometry,
            beta-gcc-phat, high reverberation time, speaker localization}
}
```

```
@article{2025_Oskar_Rudolf,
  title={Implementation of visual people counting algorithms in embedded systems},
  author={O. Rudolf and R. Hecker and M. Thi{\ss}en and L. Sillekens and I. Penner and J.-P. Akelbein and S. Seyfarth and Elke Hergenr{\"o}ther},
  journal={Computer Science Research Notes},
  year={2025},
  url={http://www.doi.org/10.24132/CSRN.2025-4}
}
```

## Contact

Created by: **Laurens Sillekens**  