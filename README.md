# ChatGPT plugin template

THE template to create ChatGPT plugins.

1. Automatic API specification generation ✨ (powered by [FastAPI](https://fastapi.tiangolo.com))
2. Ready to use 🚀 (works out of the box)
3. All in one `main.py` file 📄 (keeps things simple and clean)

## Coming soon

1. Deployment (let me know which providers you use)
2. Continuous integration (Github Actions)
3. ...

## Development

To get started with development on your computer run the setup script.

```bash
./scripts/setup.sh
```

You can start a local development server with the following command.

```bash
./scripts/run.sh
```

Or alternatively if you have the virtual environment enabled.

```bash
python main.py
```

If everything works you can view the plugin manifest in your browser at [http://localhost:8000/.well-known/ai-plugin.json](http://localhost:8000/.well-known/ai-plugin.json).


## Installation

1. Open [ChatGPT](https://chat.openai.com/) in your browser (requires [plugin access](https://openai.com/waitlist/plugins))
2. In the top central `Model` dropdown select `Plugins (ALPHA)` (if you do not see this option you do not have plugin access yet)
3. Click the `Plugins` dropdown on the right and select `Plugin store`, which opens a popup
4. Select `Develop your own plugin` on the bottom left
5. Enter `localhost:8000` in the `Domain` field and click `Find manifest file`

Tip: You can enable the plugin devtools in the bottom left `Settings` menu item.


## API documentation and specification

The api documentation is automatically generated from your code. You can view the documentation by visiting [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

The api specifications are automatically generated based on your code. You can view the specifications by visiting [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json) in your browser.


## ChatGTP plugin documentation

https://platform.openai.com/docs/plugins/introduction

## Inspiration

This plugin template is inspired by the official [ChatGPT plugin example](https://github.com/openai/plugins-quickstart).
