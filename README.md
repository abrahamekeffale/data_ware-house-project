# data_ware-house-project
# Object Detection & FastAPI Data Exposure Project

This project demonstrates the use of YOLO (You Only Look Once) for object detection and exposes the detection results via a FastAPI API. The project collects images from the Chemed Telegram channel, detects objects in those images, and stores the detection data in a PostgreSQL database. It then provides an API to query the detection data.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Environment Setup](#environment-setup)
  - [YOLOv5 Setup](#yolov5-setup)
  - [FastAPI Setup](#fastapi-setup)
- [Usage](#usage)
  - [Object Detection](#object-detection)
  - [API Endpoints](#api-endpoints)
- [Logging](#logging)
- [Monitoring](#monitoring)

## Project Structure

