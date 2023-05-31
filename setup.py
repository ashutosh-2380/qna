from setuptools import setup, find_packages

setup(
    name="streamlit-question-answering",
    version="1.0",
    author="Your Name",
    author_email="your@email.com",
    description="Question Answering App with Streamlit",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "transformers"
    ],
)
