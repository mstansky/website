# Creating base image for the container that will host my streamlit website, locally and on aws

# ———— BUILDING IMAGE ———— 

# ---- define parent image (using python 3.12, only installing packages I need)

ARG PYTHON_VERSION=3.12.0
FROM python:${PYTHON_VERSION}-slim as base

# ---- set working directory (workdir simultaneously creates the folder inside the image)
WORKDIR /home/app

# ---- Expose required ports for website to be accessible
# Tells the container to listen on a specified network port, here it's Streamlit's default port
EXPOSE 8501
# Healthcheck instructs Docker to check container is still working and listens to Streamlit port
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# ---- copy needed files for website and pages / applications, tells it where to save

# Website homepage (in app folder)
COPY homepage.py /home/app
# Subpages and application(s)		
COPY pages /home/app/pages

# ---- install any dependencies
RUN pip install streamlit numpy pandas joblib sci-kit-learn==1.3.2





# ———— CONTAINER START COMMAND(S) ———— 
 
# Using entrypoint to set container to run "as an executable"
ENTRYPOINT ["streamlit", "run", "homepage.py", "--server.port=8501", "--server.address=0.0.0.0"]

# CMD [“python”, “./home/app/homepage.py”]