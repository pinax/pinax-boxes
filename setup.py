from distutils.core import setup


setup(
    name = "django-boxes",
    version = "0.1.dev2",
    author = "Eldarion",
    author_email = "development@eldarion.com",
    description = "a reusable Django content-boxes application",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/eldarion/boxes",
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
