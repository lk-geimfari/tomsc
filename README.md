## Preview

<img width="1405" alt="Screenshot 2020-12-13 at 13 30 41" src="https://user-images.githubusercontent.com/15812620/102009280-703dc200-3d47-11eb-8777-48c2d09ef39e.png">


## Prerequisites

You will need:

- `Docker`
- `Pipenv`

## Running

Clone repository and go to the project directory (in where Dockerfile is):
```
~ git clone git@github.com:lk-geimfari/tomsc.git
~ cd tomsc
```

and then build FastAPI image:

```
docker build -t tomsc .
```

Run a container based on your image:

```
docker run --name tomsc -p 80:80 tomsc
```

Now you can use frontend, just open file `fronted/index.html` in your browser or just go to [isaak.dev/tomsc/frontend/](https://isaak.dev/tomsc/frontend/)


## Tests

First of all, you need to install all the development dependencies, like this:

```
pipenv install --dev
```

Then run tests:

```
pipenv run pytest .
```

or just:

```
pytest .
```
