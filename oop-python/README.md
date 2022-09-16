# Learning
$ https://www.youtube.com/c/PythonEngineer/videos
$ https://www.youtube.com/playlist?list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2

## ENV
$ conda env list
$ conda activate oop-python

# Best practice, use an environment rather than install in the base env
conda create -n my-env
conda activate my-env
# If you want to install from conda-forge
conda config --env --add channels conda-forge
# The actual install command
conda install numpy