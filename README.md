<p align="center">
 <img src="https://i.imgur.com/rHCXm9r.png" alt="Kawaii API" width="400" />
</p>
  <p align="center">Kawaii API written in <a href="https://www.python.org/" target="_blank">Python</a> using <a href="https://fastapi.tiangolo.com/" target="_blank">FastAPI</a> as framework.</p>

## Requirements
- [uv](https://docs.astral.sh/uv/)
- [OpenWeatherMap API Key](https://openweathermap.org/api)
- OpenAI API Key or compatible like DeepSeek


## Project setup

```bash
$ uv venv
$ uv sync
```

### Create your .env

As mentioned on requirements, you'll need the following API keys: OpenWeatherMap and a compatible OpenAI key, I'm personally using DeepSeek because it's cheaper.

```env
OPENWEATHERMAP_API_URL=https://api.openweathermap.org/data/2.5/weather
OPENWEATHERMAP_API_KEY=YOUR_AWESOME_KEY_GOES_HERE
OPENAI_API_URL=https://api.deepseek.com
OPENAI_API_KEY=sk-YOUR_AWESOME_KEY_GOES_HERE
```

### Local Development

```bash
$ uv run fastapi dev src/main.py 
```

## API Documentation

Swagger documentation can be found <a href="https://kawaii-api.wedzy.net/docs" target="_blank">here.</a>

### Avaiable endpoints

- GET `/random-curiosity` - Ask AI to generate a random curiosity, cache: 6h
- GET `/random-de-word/?level=` - Returns a random word in German with translations to English & French, level parameter can be set: A1 to C2 level.
- GET `/random-jp-word/?level=` - Returns a random word in Japanese with meaning translation to English, includes Furigana, level parameter can be set 5 to 1, representing: N5 to N1 level.


## Credits

- Author: [Lucas Hames](https://github.com/wedz0ff)
- Distributed under [MIT License](LICENSE)
