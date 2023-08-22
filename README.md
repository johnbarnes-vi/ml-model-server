# Dockerized Flask App for Serving Machine Learning Models

This repository contains a Flask application that's Dockerized for ease of deployment. It provides an API to serve machine learning models and is designed with development environments in mind.

## Features

- **Docker Integration**: Easily build and run the app using Docker.
- **ML Model Serving**: Serve your pre-trained machine learning models through a RESTful API.
- **Image Processing**: Includes endpoints for image preprocessing and manipulation.

## Quick Start

### Prerequisites

- Docker installed on your system.

### Build and Run the Docker Container

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Build the Docker image:

   ```bash
   docker build -t image_name .
   ```

4. Run the Docker container:

   ```bash
   docker run -p 7077:7077 image_name
   ```

5. Access the API at `http://localhost:7077`.

## Endpoints

- **/flip**: POST endpoint that takes a Base64-encoded image and returns the horizontally flipped image.

## Development

This project is intended for development and testing purposes. It is not recommended for production use without further enhancements.

## Contributing

Feel free to contribute to this project by submitting issues, bug reports, or pull requests.

## Contact

For any questions or support, please contact the maintainer at [johnbarnes.vi@gmail.com](mailto:johnbarnes.vi@gmail.com).

---
