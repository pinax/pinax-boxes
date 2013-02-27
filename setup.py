from distutils.core import setup


setup(
    name = "django-boxes",
    version = "2.0b1.dev1",
    author = "Eldarion",
    author_email = "development@eldarion.com",
    description = "a reusable Django content-boxes application",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/eldarion/boxes",
    install_requires = [
        "django-reversion",
    ],
    packages = [
        "boxes",
        "boxes.templatetags",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
