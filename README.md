# ThePaganBot (AKA Hello Kitty)
*This repository is a fork of @kkrypt0nn's template, thank you to them for this.*

## Support

Before requesting support, you should know that this template requires you to have at least a **basic knowledge** of
Python and the library is made for **advanced users**. Do not use this template if you don't know the
basics or some advanced topics such as OOP or async. [Here's](https://pythondiscord.com/pages/resources) a link for resources to learn python.

If you need some help for something, do not hesitate to create an issue over [here](https://github.com/kkrypt0nn/Python-Discord-Bot-Template/issues), but don't forget the read the [frequently asked questions](https://github.com/kkrypt0nn/Python-Discord-Bot-Template/wiki/Frequently-Asked-Questions) before.

All the updates of the template are available [here](UPDATES.md).

## Disclaimer

This bot is made for a specific server, some if not all features may not be applicable to your server.

## How to start

### The _"usual"_ way

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt (
Windows)
.

Before running the bot you will need to install all the requirements with this command:

```
python -m pip install -r requirements.txt
```

After that you can start it with

```
python bot.py
```

> **Note**: You may need to replace `python` with `py`, `python3`, `python3.11`, etc. depending on what Python versions you have installed on the machine.

### Docker

Support to start the bot in a Docker container has been added. After having [Docker](https://docker.com) installed on your machine, you can simply execute:

```
docker compose up -d --build
```

> **Note**: `-d` will make the container run in detached mode, so in the background.

## Built With

- [Python 3.12.9](https://www.python.org/)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
