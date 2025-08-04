# Training_UCY_2Sept
Training for PRof. DIMITRIS STAGONAS - Department of Civil and Environmental Engineering

## Workshop Overview & Why Copernicus Data?

This workshop is designed to equip participants with practical skills in handling and analyzing Earth Sciences data using Python. Throughout the day, you will explore binary data formats like GRIB2 and NetCDF4, understand their internal structure, and learn how to leverage powerful Python libraries such as `xarray` and `cartopy` for data manipulation and visualization.

A core part of the workshop focuses on accessing and working with **Copernicus** data — Europe’s flagship Earth observation program. **Note:** In this training, we will be working **exclusively with model-based data products** (i.e., forecast, reanalysis, or climate model outputs), and not with satellite imagery or raw in-situ data.

#### Why Copernicus?

Copernicus provides open, free, and high-quality climate and environmental data gathered from satellites, in-situ sensors, and models. The datasets are:

- **Comprehensive and Multi-dimensional**: Covering atmospheric, oceanic, land, and climate variables at global and regional scales.
- **Consistent and Reliable**: Maintained by trusted European institutions with rigorous quality control.
- **Timely and Updated**: Offering near-real-time monitoring and long historical records essential for scientific research and environmental decision-making.
- **Open Access**: Freely available to everyone, promoting transparency and collaborative research worldwide.

By mastering Copernicus **model data** access and analysis workflows, participants will be empowered to conduct robust environmental assessments, climate diagnostics, and develop reproducible tools for sustainability and policy.





# Workshop Agenda  
### Earth Sciences Data Analysis with Python  

| Time           | Session Description                                             |
|----------------|-----------------------------------------------------------------|
| 09:00 - 09:15  | Welcome & Introduction to the Day                               |
| 09:15 - 10:00  | Overview of Binary Data in Earth Sciences (NetCDF4)      |
| 10:00 - 10:45  | Structure and Architecture of NetCDF Files                      |
| 10:45 - 11:00  | Introduction to Copernicus & Practical Copernicus Example       |
| 11:00 - 11:30  | Python Essentials for Scientific Data Analysis                  |
| 11:30 - 13:00  | Introduction to xarray: Why and How                             |
| 13:00 - 13:45  | Lunch Break                                                     |
| 13:45 - 14:30  | Downloading Data from Copernicus API (Account & Setup)          |
| 14:30 - 15:15  | Working with NetCDF in Python using xarray                      |
| 15:15 - 16:00  | Data Slicing, Time Series Extraction, Anomaly & Climatology Computation |
| 16:00 - 16:45  | Visualization: From Time Series to Publication-Ready Maps with cartopy |
| 16:45 - 17:15  | Final Q&A, Wrap-Up, and Sharing of Resources                    |




## Run the notebook on Google Colab

## Running on Google Colab

This project can be run on [Google Colab](https://colab.research.google.com), which provides free cloud-based Jupyter notebooks.

> **Note:** To use Google Colab, you need a valid Google account. Please ensure you are signed in with your Google credentials to run the notebooks successfully.


[![Open In Colab]()
When viewed on GitHub, you will see the **“Open in Colab”** badge/icon at the top, which you can click to launch the notebook immediately in Google Colab with all the environment setup pre-configured.

## Theory

Below are the notebooks covering theoretical concepts. Click the **Open in Colab** badges to launch each notebook directly in Google Colab with environment setup ready.

[1_start_here.ipynb](https://colab.research.google.com/github/geacomputing/UCY2Sept/blob/main/Python_code/Theory/1_start_here.ipynb)  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/geacomputing/UCY2Sept/blob/main/Python_code/Theory/1_start_here.ipynb)

[2_Type_of_Variables.ipynb](https://colab.research.google.com/github/geacomputing/UCY2Sept/blob/main/Python_code/Theory/2_Type_of_Variables.ipynb)  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/geacomputing/UCY2Sept/blob/main/Python_code/Theory/2_Type_of_Variables.ipynb)

[3_Structure_and_Architecture_of_NetCDF_Files.ipynb](https://colab.research.google.com/github/geacomputing/UCY2Sept/blob/main/Python_code/Theory/3_Structure_and_Architecture_of_NetCDF_Files.ipynb)  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/geacomputing/UCY2Sept/blob/main/Python_code/Theory/3_Structure_and_Architecture_of_NetCDF_Files.ipynb)

[4_Introduction_to_Copernicus_and_Practical_Copernicus_Example.ipynb](https://colab.research.google.com/github/geacomputing/UCY2Sept/blob/main/Python_code/Theory/4_Introduction_%20to_Copernicus_and_Practical_Copernicus_Example.ipynb)  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/geacomputing/UCY2Sept/blob/main/Python_code/Theory/4_Introduction_%20to_Copernicus_and_Practical_Copernicus_Example.ipynb)

[5_Introduction_to_xarray.ipynb](https://colab.research.google.com/github/geacomputing/UCY2Sept/blob/main/Python_code/Theory/5_Introduction_to_xarray.ipynb)  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/geacomputing/UCY2Sept/blob/main/Python_code/Theory/5_Introduction_to_xarray.ipynb)

---

## Hands-on

*(Coming soon)*

You can add the practical notebooks here with the same style when ready.


## COPERNICUS Credentials

Students should create an account on the [COPERNICUS website](https://cds.climate.copernicus.eu/how-to-api) and follow the instructions to retrieve their **URL** and **key** variables.

These credentials are necessary to submit simple API requests to download climate data.

Make sure to keep your credentials confidential and never share them publicly.

Here is an example of what the credentials look like in a configuration file or environment variable:

```plaintext
url: https://cds.climate.copernicus.eu/api
key: <PERSONAL-ACCESS-TOKEN>
```

### Additional Resources

The official COPERNICCUS webpage [COPERNICUS website](https://cds.climate.copernicus.eu/how-to-api) provides detailed instructions on how to install and configure the CDS API client on your personal machine.

### Storing Credentials in Google Colab

In a typical local Linux environment, users store such credentials securely in their shell configuration files like `.bashrc` or `.bash_profile`. This approach allows the system or scripts to automatically load and use these sensitive variables without hardcoding them in scripts.

Since Google Colab is a cloud environment without persistent user home directories, we simulate this process by creating a temporary local file during the session that contains the necessary environment variables for the Copernicus Data Store API.

This method helps to:

- Keep credentials separate from the code  
- Avoid exposing keys directly in notebooks  
- Make it easier to reuse the credentials throughout the session  

Remember that this file and the environment variables exist only for the duration of your Colab session.


## Event Materials

This repository also contains a PDF slideshow used during the event. Everything that was projected and presented is available here, so don’t worry if you miss something — you can always retrieve it from this repo.


## About GEA COMPUTING


**GEA COMPUTING Ltd.** is a software development and consulting company focused on environmental data science, geospatial analytics, and scientific computing.  
We design and build tools and platforms to process, visualize, and interpret Earth observation and climate data efficiently—leveraging open-source technologies and promoting reproducible research practices.

Beyond software, we specialize in **training researchers, institutions, and professionals**, helping them gain hands-on skills in climate data workflows, geospatial processing, and Python-based analysis.


| Company                | EMS GEA Computing LTD             |
|------------------------|---------------------------------|
| Motto                  | Through numbers, the Earth.      |
| Email                  | office@geacomputing.eu           |
| Website                | [www.gea-computing.eu](https://www.gea-computing.eu) |
| Instagram              | [ems_gea_computing](https://www.instagram.com/ems_gea_computing/) |
