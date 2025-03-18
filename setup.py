from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="ersschema",
    install_requires=[
        "kafka",
        "googleapis-common-protos"
    ],
    extras_require={"develop": [
        "ipdb",
        "ipython",
        "ruff",
    ]},
)
