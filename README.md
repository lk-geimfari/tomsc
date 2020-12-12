## Prerequisites

You will need:

- `Docker`
- `Pipenv`

## Running

Go to the project directory (in where Dockerfile is) and then build FastAPI image:

```
docker build -t tomsc .
```

Run a container based on your image:

```
docker run --name tomsc -p 80:80 tomsc
```

Now you can use frontend, just open file `fronted/index.html` in your browser.


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