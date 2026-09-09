---
title: Food Vision
colorFrom: indigo
colorTo: gray
sdk: gradio
sdk_version: 6.26.0
python_version: '3.12'
app_file: app.py
pinned: false
---

# FoodVision Big

An image classifier that identifies **101 different types of food** from a photo, built with a fine-tuned **EfficientNet-B2** model in PyTorch and served with **Gradio**.

Upload a photo of a dish and the model returns its top 5 predicted classes with confidence scores, plus how long inference took.

## How it works

- **Base model:** `torchvision.models.efficientnet_b2`, pretrained on ImageNet
- **Fine-tuning:** the base layers are frozen and only a new classifier head (`Dropout` + `Linear`) is trained on the [Food101](https://www.tensorflow.org/datasets/catalog/food101) dataset (101 classes, trained on a 20% subset)
- **Inference:** runs on Hugging Face's [ZeroGPU](https://huggingface.co/docs/hub/spaces-zerogpu), which allocates a GPU on demand per request

## Files

| File | Purpose |
|---|---|
| `app.py` | Gradio interface and prediction function |
| `model.py` | Builds the EfficientNet-B2 model and its image transforms |
| `class_names.txt` | The 101 Food101 class labels, one per line |
| `09_pretrained_effnetb2_feature_extractor_food101_20_percent.pth` | Trained model weights |
| `requirements.txt` | Python dependencies |

## Run it locally

```bash
pip install -r requirements.txt
python app.py
```

Then open the local URL Gradio prints (usually `http://127.0.0.1:7860`).

## Credits

Built by following the [PyTorch Deep Learning course](https://www.learnpytorch.io/09_pytorch_model_deployment/) by Daniel Bourke.
