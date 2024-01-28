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
2. Install the required libraries and modules used. Unzip the static zip file for third party CSS/JavaScript libraries. 

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


### Implementation
- SARIMAX-LSTM hybrid Time Series Model
  
  The model used to predict the future values for the components in air quality. The data is first pre-processed to fill missing values and be normalized. The SARIMAX model calculates the auto regressve moving   average of the given variable, taking into account the influence of the exogenous variables (the other variables in the distribution). Once the SARIMAX model is fit to the data, a lag is introduced and an
  LSTM model is trained on the modified data. This LSTM deep learning model is trained to recognize fine tuned patterns in the data and can accurately predict the future values of the given variable,leveraging   the advantages of both the machine learning SARIMAX approach and the deep learning LSTM approach. The output data comprises the values of the air quality components for the succeeding 12 hours.


      
- LLM : Falcon-7B-Instruct as a Virtual Assistant

  
  This model leverages the Falcon-7B-Instruct language model into a virtual assistant to address users and stockholders’ queries with real-time data kept in context for the LLM. A text generation pipeline is     created, incorporating real-time parameters to enhance the generation process. The user is prompted to input a query and a context prompt containing the real-time environmental parameter is concatenated into   the query. The LM then generates precise answers for the given query. This approach balances efficiency and accuracy, making it particularly suitable for scenarios with computation resource constraints.

  
  Model Comparison and Constraints:

  
  The code initially experimented with various models (Mistral 7B, Ollama, Nous Hermes 13B, GPT2, Llama 7B, Wizard-Vicuna-13B Quantized). Due to heavy computation constraints, the chosen Falcon-7B-Instruct       model strikes a balance between resource efficiency and text generation quality. Additional implementation include optimized models and RAG.
  


