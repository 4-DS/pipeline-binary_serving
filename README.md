# step_template

Prerequisites

- Docker is up and running
- Git installed

# Deploy an environment for a single use

```
git clone --recursive https://github.com/4-DS/step_template.git
cd step_template
```

## To make use of it, run:
```
bash create.sh
bash run.sh
```

## To stop using it for a while, run:
```
bash stop.sh
```

## To continue using it, run:
```
bash run.sh
```

## To remove it, run:
```
bash remove.sh
```

![the picture](examples/example.png)

# Developing ML

## Go on http://127.0.0.1:8888/lab
```
git clone --recursive https://github.com/4-DS/step_template.git
cd step_template
```

## Run Init_Data.ipynb to get sample data

## Run step.dev.py in Terminal 

```python step.dev.py```

# Step repository naming conventions

We will recommend forming the git repo name as: <%pipeline_name>-<%step_name>

But this is not a mandatory requirement. And our library should work under any layouts with naming

The authoritative source of the pipeline and step names will now be exclusively in configs, and will not be tightly tied to the names of folders and git repositories