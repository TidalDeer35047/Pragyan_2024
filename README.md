# Air Quality Prediction Web Application

This web application provides real-time and predicted air quality information for the city of Alipur, Delhi, India. It combines SARIMA and LSTM models to make future predictions and Flask for the user interface.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Getting Started

### Prerequisites

Make sure you have the necessary prerequisites installed on your machine:

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation/)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/air-quality-prediction.git
```
2. Install the required libraries and modules used.

```bash
  pip install -r requirements.txt
```

3. Obtain the API key from our data source:

[https://aqicn.org/api/](https://aqicn.org/api/)

### Usage

Enter the following line into your terminal (Linux only):

```bash
sh main.sh
```

The main.sh script is responsible for starting all the necessary programs and scripts required to run the Flask application integrated with real-time air quality data collection, and the python model that predicts future concentrations of the PM2.5 (Particulate Matter 2.5), PM10 (Particulate Matter 10), O3 (Ozone), NO2 (Nitrogen Dioxide), SO2 (Sulphur Dioxide) and CO(Carbon Monoxide) in the air, in the particular region of interest. The script transfers information between the python model and the user interface application. The application changes dynamically per hour, as soon as the next value is released to the public.

### File Structure


