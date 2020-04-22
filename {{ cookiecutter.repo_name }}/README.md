# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Organization

```
├── LICENSE
├── Makefile              <- Makefile with commands like `make data` or `make train`
├── README.md             <- The top-level README for developers using this project.
├── data
│   ├── external          <- Data from third party sources.
│   ├── interim           <- Intermediate data that has been transformed.
│   ├── processed         <- The final, canonical data sets for modeling.
│   └── raw               <- The original, immutable data dump.
│
├── docs                  <- A default Sphinx project; see sphinx-doc.org for details
│
├── models                <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks             <- Jupyter notebooks. Naming convention is a number (for ordering),
│                            the creator's initials, and a short `-` delimited description, e.g.
│                            `1.0-jqp-initial-data-exploration`.
│
├── references            <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports               <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures           <- Generated graphics and figures to be used in reporting
│
├── requirements-dev.txt  <- The requirements file for contributing to this codebase.
│
├── requirements.txt      <- The requirements file for reproducing the analysis environment, e.g.
│                            generated with `pip freeze > requirements.txt`
│
├── setup.cfg
├── setup.py
├── src                   <- Location of the local python package containing all analyis
│   └── {{ cookiecutter.library_name }}
│       ├── __init__.py
│       ├── cli.py
│       ├── data          <- Scripts to download or generate data
│       │   └── __init__.py
│       ├── features      <- Scripts to turn raw data into features for modeling
│       │   └── __init__.py
│       ├── models        <- Scripts to train models and then use trained models to make
│       │   │                predictions
│       │   └── __init__.py
│       ├── version.py
│       └── visualization <- Scripts to create exploratory and results oriented visualizations
│           └── __init__.py
│
├── tests                 <- tests for the source code
│
└── tox.ini               <- tox file with settings for running tox; see tox.testrun.org
```

## Getting started

You will need to have the `conda` command line tool installed.
See [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
Most of the basic development steps available are `make` targets.
Run `make` with no argumnets to see what are the possible options.

To get started on reproducing this analysis, set up a conda environment using
the steps below.

```bash
make create_environment
conda activate {{ cookiecutter.project_name }}
make requirements
```
{% if cookiecutter.strip_ipynb_output == 'Y' %}
To prevent data leakage, jupyter notebooks shouldn't be commited with any output
cells.
Once you've created your environment execute the following command to add a hook
in your `.git/config`.

```bash
nbstripout --install
```

This will ensure no output cell contents will be committed
to `git`, without altering your local copy.
{% endif %}
## Contributing

All code within the `src` directory should be linted to enforce code quality.
You can test your code for linting errors and the unit tests using the command:

```bash
make test
```

To automatically style your code to pass all linting checks run:

```bash
make style
```

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
