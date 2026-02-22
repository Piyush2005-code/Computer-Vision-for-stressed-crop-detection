<<<<<<< HEAD
# Image_Segmentation_nidar
=======
# Crop Stress Detection using Computer Vision

## Project Overview
This repository contains code for a real‑time computer vision algorithm that detects stressed crops, highlighted in yellow, using object detection and segmentation techniques.

- **Initial approach**: Implemented a U‑Net model for segmentation and real‑time inference.
- **Current direction**: Transitioned to YOLOv8n for object detection. The YOLOv8n training and inference scripts are planned but not yet included.

The project is intended for agricultural monitoring, enabling rapid identification of stressed regions in aerial or field images.

## Repository Structure
```
Image_Segmentation-master/
├── .DS_Store
├── .git/                     # Git repository metadata
├── Farm_top_images/          # Sample aerial images of farms
├── U_Net_implementation/    # U‑Net model code and utilities
│   ├── architecture.py
│   ├── unet.py
│   ├── dataset.py
│   ├── train.py
│   ├── inference.py
│   ├── video.py
│   └── unet.pt              # Pre‑trained weights
├── brain-segmentation-pytorch/  # Reference code for brain segmentation (used as a guide)
├── git_repo_image_segmentation/ # Additional reference repository for image segmentation
├── model_checkpoint1.pt      # Checkpoints from early experiments
├── model_checkpoint2.pt      # Additional checkpoint
├── yellow_patched/           # Images of crops with stress annotations
└── yellow_patched_mask/     # Corresponding mask images for segmentation
```

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Image_Segmentation-master.git
   cd Image_Segmentation-master
   ```
2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *If a `requirements.txt` file is not present, install the core libraries manually:* 
   ```bash
   pip install torch torchvision opencv-python tqdm
   ```

## Usage
### U‑Net Inference (currently available)
```bash
python U_Net_implementation/inference.py --image_path path/to/image.jpg
```
The script loads the pre‑trained `unet.pt` model and outputs a segmentation mask highlighting stressed regions.

### Training (U‑Net)
```bash
python U_Net_implementation/train.py --data_dir path/to/dataset
```
Adjust hyper‑parameters inside `train.py` as needed.

### YOLOv8n (Not added to the repository yet)
The repository will later include scripts for:
- Training YOLOv8n on the annotated crop images.
- Performing real‑time inference using the trained YOLOv8n model.

## Contributing
Contributions are welcome. Please follow these steps:
1. Fork the repository.
2. Create a new feature branch.
3. Submit a pull request with a clear description of changes.

## License
This project is licensed under the MIT License.

## Acknowledgements
- The U‑Net implementation was inspired by publicly available segmentation tutorials.
- Reference repositories: `brain-segmentation-pytorch` and `git_repo_image_segmentation` provided useful code patterns.
>>>>>>> master
