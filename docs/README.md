# NeuroDash !
Team : François Paugam & Maëlle Freteault
Contributor for the dashboard module: Maëlle Freteault
Contributor for the visualisation module : François Paugam

This project is made during BrainHack School 2020 !
This repository contains the code for the dashboard module, and the scripts for the integration of the visualisation module

[link to the presentation](https://docs.google.com/presentation/d/1glGlgnHoYoe2fxgS5SDSvCW82fZQKU_U1vwovwJn5q0/edit?usp=sharing)

## Background

Hi everyone ! I'm Maëlle Freteault and I have a background of cognitive neurosciences, but with some training experience in programming in differents langages (python of course, but also C, C#, java, matlab...). I'm a first year pHD working on some encoding model of Auditory processing in the brain. 

What's an encoding model, you might ask ? An encoding model is a machine learning model (such as neural networks, svm, ...) that has been trained to be capable of processing complex, natural stimuli a similar way that the brain does. For example, if we have some fmri preprocessed files from subjects watching a film, we can give to the model the audio of the film, then train the model to transform our audio input in an output with the shape of fmri results (here for example, as a parcellation of fmri results, so a matrix with 210 values for the 201 regions of interest). At the end, we can compare the predicted matrix with the real recorded fmri output, and see wich regions have been better predicted with the audio input.

## Project definition

### Context

My PhD project is part of a bigger project, the Courtois Neuromod project. 

![cneuromod_dataset](https://github.com/brainhack-school2020/maellef_IDK_project/blob/master/graphics/Neuromod_dataset.png)

[link to the cNeuromod official website](https://www.cneuromod.ca/)

This project has for goal to model brain processes using AI. One important feature of the cNeuromod project is the creation of an extensive dataset of 6 subjects brains, with diverses techniques such as fMRI, MEG and biosignals recordings. The dataset is crucial when training a AI model, and having a large dataset is really a big asset to create better models. the Neuromod dataset is going to grow over 5 years, with weekly recordings of the subjects on differents tasks such as classical paradigms used in the Human Connectome Project, but also films viewing, video games and many more ... For now, I only used the films viewing dataset, called Movie10, but I wish to have a better understanding on what is available on the dataset, and the differents specs. 

I decided to create a Dashboard, that will let people easily visualize the dataset, and that is capable of evolving with the growth of the cNeuromod Dataset.

![first_mockup](https://github.com/brainhack-school2020/maellef_IDK_project/blob/master/graphics/mockup_1.png)

As the cNeuromod Dataset follows the BIDS standard, I also want to create a dashboard generic enouch to be adapted to other fmri datasets following the BIDS standard. 

### Tools

My goal in this project is to improve my capacity in project management, by making clean, organized projects that can be easily shareable in a context of Open Science. With this goal in mind, I will use some of the following tools : 

- Python :
  - data processing : numpy, pandas, ...
  - project management : CookieCutter
  - gestion of BIDS dataset : pybids
  - DashBoard maker : Dash By Plotly [plotly official website](https://plotly.com/dash/)

- virtualization : conda venv

- Containerization : Docker, Singularity

- Git, GitHub

And maybe some others, depending on how the project evolve !

### Data

For this project, I will be working on the Courtois Neuromod Dataset(fMRI for now). This Dataset follows the BIDS standard, 
so I will use other fMRI datasets with BIDS standard to test the dashboard at the end of BrainHack.

### Deliverables

 - A DashBoard
 - A Shareable repository
 - And maybe more ! 

## Results

### Progress overview

WIP

### Tools I learned during this project
 
 We will see !
 
### Results

 We will see !
 
## Conclusion and acknowledgement
Thanks to all the BrainHack team and the students. In the end, I hope to have a great time with this project 
and with all of you !

[links to braintastics cookies cutters](https://www.thingiverse.com/thing:3820314)
