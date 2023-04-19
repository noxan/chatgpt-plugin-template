# ChatGPT plugin template

THE template to create ChatGPT plugins.

1. Automatic API specification generation ✨ (powered by [FastAPI](https://fastapi.tiangolo.com))
2. Ready to use 🚀 (works out of the box)
3. All in one `main.py` file 📄 (keeps things simple and clean)

## Coming soon

1. Deployment (let me know which providers you use)
2. Continuous integration (Github Actions)
3. ...

## Installation

To get started with the template, clone the repository and run the setup script.

```bash
./scripts/setup.sh
```

You can start a local development server with the following command.

```bash
./scripts/run.sh
```

Or alternatively if you have virtual environment enabled.

```bash
python main.py
```

If everything works you can view the plugin manifest in your browser at [http://127.0.0.1:8000/.well-known/ai-plugin.json](http://127.0.0.1:8000/.well-known/ai-plugin.json).

## Documentation

The api documentation is automatically generated from your code. You can view the documentation by visiting [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

## Inspiration

This plugin template is inspired by the official [ChatGPT plugin example](https://github.com/openai/plugins-quickstart).
