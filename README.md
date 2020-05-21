# NeuroDash !

To everyone passing by this README.md : Hello ! I hope you're having a good day, wherever you're in the world ! Please, have a cookie.

![brain cookies !](https://github.com/brainhack-school2020/maellef_IDK_project/blob/master/graphics/brain_cookies.jpg)

[links to these braintastics cookies cutters](https://www.thingiverse.com/thing:3820314)


## Presentation

Hi everyone ! I'm Maëlle Freteault and I have a background of cognitive neurosciences, but with some training experience with programming in differents langages (python of course, but also C, C#, java, matlab...). I'm a first year pHD working on some encoding model of Auditory processing in the brain. 

What's an encoding model, you might ask ? An encoding model is a machine learning model (such as neural networks, svm, ...) that has been trained to be capable of processing complex, natural stimuli a similar way that the brain does. For example, if we have some fmri preprocessed files from subjects watching a film, we can give to the model the audio of the film, then train the model to transform our audio input in an output with the shape of fmri results (here for example, as a parcellation of fmri results, so a matrix with 210 values for the 201 regions of interest). At the end, we can compare the predicted matrix with the real recorded fmri output, and see wich regions have been better predicted with the audio input.

## Project definition

### Background

My PhD project is part of a bigger project, the Courtois Neuromod project. 

![cneuromod_logo](https://github.com/brainhack-school2020/maellef_IDK_project/blob/master/graphics/logo_neuromod_black.png)

[link to the cNeuromod official website](https://www.cneuromod.ca/)

This project has for goal to model brain processes using AI, and to further our understanding of our dear brain's inner work. One important feature of the cNeuromod project is the creation of an extensive dataset of 6 subjects brains, with diverses techniques such as fMRI, MEG and biosignals recordings. The dataset is crucial when training a AI model, and having a large dataset is really a big asset to create better models. the Neuromod dataset is going to grow over 5 years, with weekly recordings of the subjects on differents tasks such as classical paradigms used in the Human Connectome Project, but also films viewing, video games and many more ... For now, I only used the films viewing dataset, called Movie10, but I wish to have a better understanding on what is available on the dataset, and the differents specs. I decided to create a Dashboard, that will let people easily visualize the dataset, and that is capable of evolving with the growth of the cNeuromod Dataset. If possible, I also want it to make it generic enouch to be adapted to other fmri datasets. 

   This project is made during BrainHack School 2020 ! 

### Tools

I already have some programming experience, with python, and some generic libraries, like numpy, pandas, matplotlib, ... and some others more specialised like nilearn, nistats for fmri processing, or pytorch for machine learning. But in this project, I want to focus on project management, and having a code that is clean and easily shareable. So I will mainly work with git, github, some containerization tools (like virtualization with conda, or maybe using Docker ?), cookiecutters, pyBids for the fmri files, and to create the dash board, I will use the framework Dash by PlotLy. With Dash, I can create a web application that i can easily share, without going too much into specifics aspects of applications like back-end, front-end, ...

I already have some experience with the folowing tools :
- Python :
  - numpy, pandas, ...
  - matplotlib (but i'm clearly not the best)
  - nilearn, scikit-learn
  - Pytorch
- Git, GitHub

In this project, I want to learn more on :

- containerization : Docker, conda venv, ... 
- project management : pyBids, cookiecutter ?
- Dash by plotly : [plotly official website](https://plotly.com/dash/)

more to come !

### Data

For this project, I will be working on cNeuromod Dataset

### Deliverables

## Results

### Progress overview

### Tools I learned during this project

### Results

## Conclusion and acknowledgement

In the end, I hope to have a great time with this project and with all of you !
