# SmartWaste 🗑️

An AI-powered waste classification system that automatically detects and categorizes waste using deep learning.

## Features ✨

- **Waste Classification**: Automatically classifies waste into 6 categories:
  - Cardboard ♻️
  - Glass 🍾
  - Metal 🥫
  - Paper 📰
  - Plastic 🧴
  - Trash 🗑️

- **Human Detection**: Protects privacy by preventing human images from being processed
- **Real-time Predictions**: Get instant classification with confidence scores
- **Web Interface**: Easy-to-use web application for uploading images

## Installation 🔧

### Requirements
- Python 3.7+
- PyTorch
- Flask
- OpenCV

### Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/smartwaste.git
cd smartwaste
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open browser and go to: `http://localhost:5000`

## How to Use 📸

1. Upload a waste image (PNG, JPG, GIF, BMP)
2. The app checks if image contains people (privacy protection)
3. If safe, it classifies the waste type
4. Get confidence score and waste classification result

## Technologies Used 🛠️

- **Framework**: Flask (Python web framework)
- **Deep Learning**: PyTorch, TorchVision
- **Model Architecture**: ResNet18 (Fine-tuned for waste classification)
- **Image Processing**: OpenCV, Pillow
- **Frontend**: HTML, CSS, JavaScript

## Model Details 📊

- **Architecture**: ResNet18 (18-layer Residual Network)
- **Classes**: 6 waste categories
- **Input Size**: 224x224 pixels (RGB)
- **Accuracy**: High precision waste classification

## Authors & Contributors 👥

- **Abdul Aziz Mensah** - Lead Developer & AI Integration
- **Co-author** - Project Collaboration

## Project Structure 📁

```
smartwaste/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/
    └── index.html        # Web interface
```

## Features Breakdown 🔍

### Waste Classification
- Uses trained ResNet18 model
- Classifies into 6 categories
- Returns confidence scores

### Privacy Protection
- Detects human presence in images
- Blocks images with people
- Message: "⚠️ Please upload waste images only, not people"

### Real-time Processing
- Instant predictions
- No server delays
- Responsive web interface

## Future Improvements 🚀

- [ ] Mobile app version
- [ ] Batch processing for multiple images
- [ ] Cloud API deployment
- [ ] Database for classification history
- [ ] Real-time camera feed support
- [ ] Multi-language support

## License 📄

MIT License - Free for personal and commercial use

## Disclaimer ⚠️

This is a portfolio project demonstrating AI/ML capabilities. The production version with trained model weights is deployed separately on PythonAnywhere.

## Contact & Support 📧

For questions or issues, feel free to open an issue on GitHub.

---

**Made with ❤️ for better waste management**
