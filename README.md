# Project Repository

This repository contains several projects categorized into different folders: `helpdesk`, `marketing`, and `sales`. Each folder contains specific sub-projects or scripts that fulfill different functionalities. This README provides an overview of the repository and instructions on how to set up and run the different projects.

## Table of Contents

- [Setup Instructions](#setup-instructions)
  - [Common Setup](#common-setup)
  - [Helpdesk Setup](#1-helpdesk-setup)
  - [Marketing Setup](#2-marketing-setup)
  - [Sales Setup](#3-sales-setup)
- [Folder Overview](#folder-overview)
  - [helpdesk/sqlagent](#helpdesksqlagent)
  - [marketing](#marketing)
  - [sales](#sales)
- [License](#license)



## Setup Instructions

### Common Setup

Before proceeding to individual project setups, follow these common steps:

#### Clone the Repository

To get started, first, clone the repository to your local machine using:

```bash
git clone https://github.com/nepagroup/spyder.git
```
This will create a local copy of the repository on your machine. Now, follow the folder-specific setup instructions below.

## 1. Helpdesk Setup

1.1 Navigate inside folder path:

Navigate to the `helpdesk/sqlagent` folder where the SQL agent project resides:
```bash
cd helpdesk/sqlagent
```

1.2 Install Dependencies:

Install the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

1.3 Run the Jupyter Notebook:

Ensure that Jupyter Notebook is installed, then run the Jupyter Notebook server or corresponding environment:
```bash
pip install notebook  # If not already installed
jupyter notebook

```
Open `agent.ipynb` and execute the cells sequentially.

for documentation visit: [click here](https://github.com/nepagroup/spyder/blob/main/helpdesk/sqlagent/document.txt)
<br>

## 2. Marketing Setup

2.1 Navigate to `marketing` path:

Navigate to the marketing folder where the `marketing` scripts are located:
```bash
cd marketing
```
2.1.1 for `custom Lead generation` project:

Navigate to the folder path for this project:
```bash
cd custom_lead_generation
```

Install Dependencies:

Install the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
Run the Jupyter Notebook:

Ensure that Jupyter Notebook is installed, then run the Jupyter Notebook server or corresponding environment:
```bash
pip install notebook  # If not already installed
jupyter notebook

```
Open `lead_generator.ipynb` and execute the cells sequentially.

for documentation visit: [click here](https://github.com/nepagroup/spyder/blob/main/marketing/email_generattion/leadmail/document.txt)

<br>

2.1.2 for `recommended_product_email_generation` project:

Navigate to the folder path for this project:

```bash
cd recommended_product_email_generation
```

Install Dependencies:

Install the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
Run the Jupyter Notebook:

Ensure that Jupyter Notebook is installed, then run the Jupyter Notebook server or corresponding environment:
```bash
pip install notebook  # If not already installed
jupyter notebook

```
step 1: open `merge.ipynb` and execute the cells sequentially.

setp 2: open `email_generator.ipynb` and execute the cells sequentially. 

step 3: open `processing_cleaning_final_mails.ipynb` and execute the cells sequentially.




for documentation visit: [click here](https://github.com/nepagroup/spyder/blob/main/marketing/email_generattion/recommended_product/document.txt)

for workflow diagram visit: [click here](https://github.com/nepagroup/spyder/blob/main/marketing/recommended_product_email_generation/full_flow.png)



## 3. Sales Setup

3.1 Navigate to `sales` path:

Navigate to the sales folder where the `sales` scripts are located:
```bash
cd sales
```
3.1.1 for `googlemap_scrapiee` project:

Navigate to the folder path for this project:
```bash
cd googlemap_scrapiee
```

Install Dependencies:

Install the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
Run the python File:
```bash
python inp_gui.py
```
This will open Gui window in your machine enter `location` and `keyword` you want to search into gui

for documentation visit: [click here](https://github.com/nepagroup/spyder/blob/main/sales/googlemap_scrapiee/document.txt)

<br>

3.1.2 for `maps_route` project:

Navigate to the folder path for this project:

```bash
cd maps_route
```

Run the Html file from `live server` or into `browser` manually:

For your custom place route Open that html file into code editor and place your desired location for route

for documentation visit: [click here](https://github.com/nepagroup/spyder/blob/main/sales/maps_route/document.txt)

<br>

3.1.3 for `product_corrections_llm` project:

Navigate to the folder path for this project:
```bash
cd product_corrections_llm
```

Install Dependencies:

Install the required dependencies using the `requirements.txt` file:
```bash
pip install -r req.txt
```
Run the Jupyter Notebook:

Ensure that Jupyter Notebook is installed, then run the Jupyter Notebook server or corresponding environment:
```bash
pip install notebook  # If not already installed
jupyter notebook

```
open `product_matching.ipynb` and execute the cells sequentially.

for documentation visit: [click here](https://github.com/nepagroup/spyder/blob/main/sales/product_corrections_llm/docs.pdf)

<br>

3.1.4 for `sales_pitch` project:

Navigate to the folder path for this project:

```bash
cd sales_pitch
```

Install Dependencies:

Install the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```
Run the Jupyter Notebook:

Ensure that Jupyter Notebook is installed, then run the Jupyter Notebook server or corresponding environment:
```bash
pip install notebook  # If not already installed
jupyter notebook

```
step 1: open `product_shop_concat.ipynb` and execute the cells sequentially.

setp 2: open `review_append.ipynb` and execute the cells sequentially. 

step 3: open `review_summarize.ipynb` and execute the cells sequentially.

step 4: open `sales_pitch_text.ipynb` and execute the cells sequentially.

step 5: open `app.ipynb` and execute the cells sequentially.

for documentation visit: [click here](https://github.com/nepagroup/spyder/blob/main/sales/sales_pitch/document.txt)


## Folder Overview

### helpdesk/sqlagent

This folder contains projects related to SQL agents and helpdesk automation:

- **Files**:
  - `agent.ipynb`: Jupyter Notebook containing the SQL agent script.
  - `docs.docx`: Documentation file for the SQL agent.
  - `requirements.txt`: List of dependencies required for this project.

### marketing

This folder contains various marketing-related scripts and projects:

- **Subfolders**:
  - `custom_lead_generation`: Scripts for generating custom leads based on various parameters.
  - `recommended_product_email_g`: Scripts for generating recommended product emails.

### sales

This folder includes projects related to sales operations and automation:

- **Subfolders**:
  - `googlemap_scrapiee`: A script or tool for scraping Google Maps for relevant sales data.
  - `maps_route`: Scripts related to optimizing routes for salespersons.
  - `product_corrections_llm`: Tool or script for correcting product-related data using language models.
  - `sales_pitch`: Scripts for generating or improving sales pitches.


## License
[View License](https://github.com/nepagroup/spyder/blob/main/LICENSE)
