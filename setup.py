from setuptools import setup, find_packages

setup(
    name="chalice-spec",
    version="0.7.0",
    description="Chalice x APISpec x Pydantic plug-ins",
    author="Deniz",
    author_email="landom3562@hotmail.com",
    url="https://github.com/Landom3562/chalice-spec",
    license="MIT",
    keywords=["Chalice", "AWS", "APIspec", "OpenAPI", "Pydantic"],
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.7",
    install_requires=[
        "apispec>=6.0.2",
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
