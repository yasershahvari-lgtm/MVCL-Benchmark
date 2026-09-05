from setuptools import setup

setup(
    name="mvcl-benchmark",
    version="1.1.0",
    author="MVCL Benchmark Authors",
    description="Benchmark artifact utilities for MVCL inconsistency detection and tolerance classification",
    py_modules=["generator", "evaluator", "tolerance", "utils"],
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.21",
        "scipy>=1.7",
        "pandas>=1.3",
        "matplotlib>=3.4",
        "jsonschema>=4.0",
        "tqdm>=4.62",
        "click>=8.0",
        "scikit-learn>=1.0",
        "jinja2>=3.0",
    ],
)
