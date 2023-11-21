wordy-weather
=============

While functional, this high-school experiment is very 2013 and gets only security updates. Modern substitutes include [weather.gov](https://www.weather.gov) and your local NWS office’s Area Forecast Discussion.

Bring me online with `docker compose up`, `docker compose up -d` to start in the background, or `docker compose up --build` if necessary.

JSON API endpoint is `https://wordyweather.com/api/<zip code>`.

For an easily grok-able plain-text view that's good through `curl`, use `https://wordyweather.com/curl/<zip code>`.`

Thanks to Jeremy Stanley and his [weather cli](http://fungi.yuggoth.org/weather/) for some database info.
