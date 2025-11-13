from setuptools import setup, find_packages

setup(
    name="icing_utils",
    version="0.1.0",
    author="Hirvonen Jarkko",
    description="Yleiskäyttöiset funktiot jäätämisdatan hakemiseen, laskentaan ja visualisointiin",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "requests",
        "matplotlib",
        "cmocean",
        "chardet",
        "folium",
        "streamlit"
    ],
    python_requires=">=3.8",
)
