import setuptools

version = "0.5.3"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name="Tempita",
      version=version,
      description="A very small text templating language",
      long_description=long_description,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Topic :: Text Processing",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
      ],
      keywords="templating template language html",
      author="Ian Bicking",
      author_email="ianb@colorstudy.com",
      url="http://pythonpaste.org/tempita/",
      license="MIT",
      packages=setuptools.find_packages(),
      tests_require=["nose"],
      test_suite="nose.collector",
      include_package_data=True,
      zip_safe=True,
      use_2to3=True)
