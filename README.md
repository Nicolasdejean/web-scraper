# web-scraper
A tool to get question links from stackexchange website that contains certain words in its description.

## Installation of Python
You first need to install the python 2.7 to get all the package needed to use this tool:
* **Linux/Unix**: `sudo apt install python2.7 python-pip`
* **Windows**: install manually the package from the [python site](https://www.python.org/downloads/), and follow installation instructions, **make sure to put the path in the environnement when installing dependencies**.
* **Mac**: you must install **Homebrew** and install python like so: `brew install python`, I suggest you follow the instruction from this [site](http://docs.python-guide.org/en/latest/starting/install3/osx/)

### Package installation
Once this is done you can install those package with **pip**:
* **BeautifulSoup**: `pip install beautifulsoup4`
* **request**: `pip install requests`
* **bs4**: `pip install bs4`

## Use the Tool

to use the tool you must:
* **linux/mac**: use chmod to give an execution permission to the file like so:
```chmod +x research_question.py``` 
And then execute it like so:
```./research_questions.py```

* **Windows** execute it with **python.exe** like so:
```python.exe .\research_questions.py```

If it works you are going to have a help message giving you instruction in what to put in parameteres.

### Parameters to give

the tool is used like so:
```./research_question.py [tab] [forum] [words...]```
* **tab** is the section you want from the site it can be the new, hot, real-time... section.
* **forum** is the site you want to research it can be stackexchange, stackoverflow, superuser...
* **words** are the words you want to find in the question description it can be a list of words. The fewer the words the more question you will have and vice versa.

**This is tool is in developement** so it has a few bugs, any help/pull request is welcome.
