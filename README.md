# Tony's Hardware

Tony's Hardware is a tech website aimed at gamers, developers, and tech enthusiasts. 
It provides(well for now it doesn't, but it will soon.... ) a pc components database, as well as 
comprehensive tutorials on building, fixing, and optimizing PCs and various components. 
The platform also incorporates a social-media theme, allowing logged-in users to showcase their 
PC builds and share their knowledge and experiences.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Features](#features)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Contact](#contact)

## Installation

To get started with Tony's Hardware, follow these steps:

1. Clone this repository: `git clone https://github.com/ajp3s/TonysHardware_v2.git`
2. Navigate to the project directory: `TonysHardware_v2`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Set up the database: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

## Usage

Tony's Hardware is easy to use. Once the development server is running, open your web browser and go to `http://localhost:8000`. You will be greeted with a user-friendly interface where you can:

- Browse through tutorials on PC building, fixing, and optimization.
- Create an account to access the social-media features.
- Showcase your own PC builds with images and descriptions.
- Interact with other users through comments and likes.

## Screenshots

![Home Page](screenshots/Screenshot%20(12).png)

## Features

- Extensive library of tutorials and guides for PC enthusiasts.
- User authentication and registration system.
- Social-media features for sharing PC builds and experiences.

## Contributing

We welcome contributions to Tony's Hardware! If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make changes and commit them: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Create a pull request.

Please ensure that your code follows the project's coding conventions and has appropriate test coverage.

## Credits

Tony's Hardware wouldn't be possible without the following open-source projects:

- [Django](https://www.djangoproject.com/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, suggestions, or just want to say hi, feel free to reach out to me at ajp3s@students.softuni.bg.
